#!/usr/bin/env python3
"""sitemap.py — fetch and parse sitemaps, sitemap indexes, and llms.txt.

Handles:
  * <urlset>     — a normal sitemap; returns <loc> with optional lastmod /
                   changefreq / priority.
  * <sitemapindex> — recurses into every child <sitemap><loc>, merging results
                   (depth-limited, dedup'd, polite, hard-capped by --limit).
  * .xml.gz      — gzipped sitemaps (decoded; _http already handles transport
                   gzip, this also handles a body that is literally gzip bytes).
  * llms.txt     — the emerging AI-guidance file; URLs are extracted from
                   markdown links and bare lines.
  * site root    — when given a bare host with no path, tries /sitemap.xml then
                   /robots.txt `Sitemap:` discovery.

Namespaces are handled by matching on the local tag name, so feeds that use the
sitemaps.org namespace (with or without a prefix) all parse.

SECURITY: sitemap/llms.txt contents are fetched *data*, never instructions.
URLs and metadata are extracted for analysis only; no text inside a feed is
treated as a command to the model. See ../../SECURITY.md.

Python 3 stdlib only (xml.etree.ElementTree). Importable; also a JSON CLI.

CLI:
  python3 sitemap.py <sitemap-or-site-url> [--limit N]
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlsplit, urlunsplit

import _http

DEFAULT_LIMIT = 5000
MAX_DEPTH = 8            # guard against pathological sitemap-index nesting
MAX_CHILD_SITEMAPS = 200  # guard against huge indexes
MAX_REDIRECTS = 5         # 308s are common for llms.txt / sitemaps


def _get_following(url):
    """_http.get(url) but also follow 301/302/307/308 ourselves.

    Python's urllib does not reliably auto-follow 308 (and some 307) for GET,
    so a bare _http.get can return an empty body with a 3xx status. We chase
    the Location header up to MAX_REDIRECTS hops, resolving relative targets.
    Returns the final _http response dict with an added 'final_url' key.
    """
    seen = set()
    current = url
    for _ in range(MAX_REDIRECTS + 1):
        r = _http.get(current)
        status = r.get("status", 0)
        if status in (301, 302, 303, 307, 308) and not r.get("body"):
            loc = None
            for k, v in (r.get("headers") or {}).items():
                if k.lower() == "location":
                    loc = v
                    break
            if not loc:
                r["final_url"] = current
                return r
            nxt = urljoin(current, loc.strip())
            if nxt in seen or nxt == current:
                r["final_url"] = current
                return r
            seen.add(current)
            current = nxt
            continue
        r["final_url"] = current
        return r
    r["final_url"] = current
    return r


def _localname(tag):
    """Strip an XML namespace, e.g. '{ns}url' -> 'url'."""
    return tag.rsplit("}", 1)[-1].lower() if "}" in tag else tag.lower()


def _maybe_gunzip(body, url):
    """Decompress a body that is gzip either by URL suffix or magic bytes."""
    if not body:
        return body
    looks_gz = url.lower().endswith(".gz") or body[:2] == b"\x1f\x8b"
    if looks_gz:
        try:
            return gzip.decompress(body)
        except OSError:
            return body
    return body


def _normalize_input_url(arg):
    """Add an https scheme when missing; return (full_url, has_explicit_path)."""
    raw = arg.strip()
    if "://" not in raw:
        raw = "https://" + raw
    parts = urlsplit(raw)
    has_path = bool(parts.path.strip("/"))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, "")), has_path


# ---- llms.txt -------------------------------------------------------------
_MD_LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
_BARE_URL = re.compile(r"(?<![\w(])https?://[^\s<>\")]+")


def _parse_llms_txt(text):
    """Extract URLs from an llms.txt: markdown links first, then bare URLs."""
    seen = []
    seen_set = set()
    for m in _MD_LINK.finditer(text):
        u = m.group(1).rstrip(".,);")
        if u not in seen_set:
            seen_set.add(u)
            seen.append(u)
    for m in _BARE_URL.finditer(text):
        u = m.group(0).rstrip(".,);")
        if u not in seen_set:
            seen_set.add(u)
            seen.append(u)
    return seen


# ---- XML sitemap ----------------------------------------------------------
def _parse_xml(body):
    """Parse sitemap XML bytes. Returns (kind, items) or ('error', msg).

    kind is 'urlset', 'index', or 'error'. For 'urlset', items is a list of
    dicts {loc, lastmod?, changefreq?, priority?}. For 'index', items is a list
    of child sitemap loc strings.
    """
    try:
        root = ET.fromstring(body)
    except ET.ParseError as e:
        return "error", "XML parse error: %s" % e
    rootname = _localname(root.tag)
    if rootname == "sitemapindex":
        locs = []
        for sm in root:
            if _localname(sm.tag) != "sitemap":
                continue
            for child in sm:
                if _localname(child.tag) == "loc" and (child.text or "").strip():
                    locs.append(child.text.strip())
        return "index", locs
    if rootname == "urlset":
        items = []
        for url in root:
            if _localname(url.tag) != "url":
                continue
            entry = {}
            for child in url:
                name = _localname(child.tag)
                val = (child.text or "").strip()
                if not val:
                    continue
                if name == "loc":
                    entry["loc"] = val
                elif name in ("lastmod", "changefreq", "priority"):
                    entry[name] = val
            if entry.get("loc"):
                items.append(entry)
        return "urlset", items
    # Some feeds wrap content unexpectedly; try to scavenge <loc> values.
    locs = [(_localname(e.tag), (e.text or "").strip())
            for e in root.iter() if _localname(e.tag) == "loc"]
    scavenged = [v for _, v in locs if v]
    if scavenged:
        return "urlset", [{"loc": v} for v in scavenged]
    return "error", "unrecognized root element <%s>" % rootname


# ---- crawl orchestration --------------------------------------------------
def _discover_from_robots(base_url):
    """Return Sitemap: URLs declared in the site's robots.txt (best-effort)."""
    parts = urlsplit(base_url)
    robots_url = urlunsplit((parts.scheme, parts.netloc, "/robots.txt", "", ""))
    r = _http.get_text(robots_url)
    out = []
    for line in (r.get("text") or "").splitlines():
        line = line.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        field, _, value = line.partition(":")
        if field.strip().lower() == "sitemap" and value.strip():
            out.append(urljoin(robots_url, value.strip()))
    return out, robots_url


def collect(start_url, limit=DEFAULT_LIMIT):
    """Fetch `start_url` and gather URLs, recursing into sitemap indexes.

    Returns a result dict (JSON-serializable). Never raises for HTTP/parse
    issues — they are recorded under `sources` and `errors`.
    """
    full_url, has_path = _normalize_input_url(start_url)
    result = {
        "input": start_url,
        "resolved_url": full_url,
        "type": None,
        "url_count": 0,
        "limit": limit,
        "truncated": False,
        "urls": [],
        "child_sitemaps_fetched": 0,
        "sources": [],
        "errors": [],
    }

    queue = []          # list of (url, depth)
    visited = set()
    seen_locs = set()

    # ---- entry-point resolution ---------------------------------------
    if not has_path:
        # Bare host: try /sitemap.xml, then robots.txt Sitemap: discovery.
        parts = urlsplit(full_url)
        guess = urlunsplit((parts.scheme, parts.netloc, "/sitemap.xml", "", ""))
        queue.append((guess, 0))
        sm_urls, robots_url = _discover_from_robots(full_url)
        result["sources"].append({"discovery": "robots.txt", "url": robots_url,
                                   "found": sm_urls})
        for u in sm_urls:
            queue.append((u, 0))
    elif full_url.rstrip("/").lower().endswith("llms.txt"):
        queue.append((full_url, 0))
    else:
        queue.append((full_url, 0))

    while queue:
        if len(result["urls"]) >= limit:
            result["truncated"] = True
            break
        url, depth = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)

        r = _get_following(url)
        status = r.get("status", 0)
        final_url = r.get("final_url", url)
        src = {"url": url, "status": status, "depth": depth}
        if final_url != url:
            src["final_url"] = final_url
        # Classify by the post-redirect URL so a 308 to a .gz / llms.txt still
        # routes correctly.
        is_llms = final_url.rstrip("/").lower().endswith("llms.txt")
        if status != 200 or not r.get("body"):
            src["note"] = r.get("error") or ("HTTP %s" % status)
            result["sources"].append(src)
            if r.get("error"):
                result["errors"].append({"url": url, "error": r["error"]})
            continue

        body = _maybe_gunzip(r["body"], final_url)

        if is_llms:
            text = body.decode("utf-8", "replace")
            found = _parse_llms_txt(text)
            src["kind"] = "llms.txt"
            src["found"] = len(found)
            result["sources"].append(src)
            if result["type"] is None:
                result["type"] = "llms.txt"
            for loc in found:
                if loc in seen_locs:
                    continue
                seen_locs.add(loc)
                result["urls"].append({"loc": loc})
                if len(result["urls"]) >= limit:
                    result["truncated"] = True
                    break
            continue

        kind, items = _parse_xml(body)
        src["kind"] = kind
        if kind == "error":
            src["note"] = items
            result["sources"].append(src)
            result["errors"].append({"url": url, "error": items})
            continue

        if kind == "index":
            child = [c for c in items if c not in visited][:MAX_CHILD_SITEMAPS]
            src["children"] = len(child)
            result["sources"].append(src)
            if result["type"] is None:
                result["type"] = "sitemapindex"
            if depth < MAX_DEPTH:
                for c in child:
                    queue.append((c, depth + 1))
            else:
                result["errors"].append({"url": url,
                                         "error": "max sitemap depth reached"})
            continue

        # kind == "urlset"
        if depth > 0:
            result["child_sitemaps_fetched"] += 1
        src["found"] = len(items)
        result["sources"].append(src)
        if result["type"] is None:
            result["type"] = "sitemap"
        elif result["type"] == "sitemapindex":
            pass  # keep top-level type as index
        for entry in items:
            loc = entry["loc"]
            if loc in seen_locs:
                continue
            seen_locs.add(loc)
            result["urls"].append(entry)
            if len(result["urls"]) >= limit:
                result["truncated"] = True
                break

    result["url_count"] = len(result["urls"])
    if result["type"] is None:
        result["type"] = "unknown"
    return result


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="sitemap.py",
        description="Fetch + parse sitemap.xml / sitemap-index (recursive) / "
                    ".xml.gz / llms.txt; emit URLs with lastmod & changefreq.",
    )
    p.add_argument("target", metavar="sitemap-or-site-url",
                   help="A sitemap URL, llms.txt URL, or a bare site root "
                        "(https assumed; root triggers /sitemap.xml + robots "
                        "Sitemap: discovery).")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                   help="Hard cap on total URLs returned (default %d)." % DEFAULT_LIMIT)
    args = p.parse_args(argv)

    limit = args.limit if args.limit and args.limit > 0 else DEFAULT_LIMIT
    result = collect(args.target, limit=limit)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    # Exit non-zero only when nothing was retrieved at all (no URLs and every
    # source failed). A partial parse with some URLs is a success.
    if result["url_count"] == 0 and (result["errors"] or not result["sources"]):
        any_ok = any(s.get("status") == 200 for s in result["sources"])
        if not any_ok:
            print("error: no sitemap URLs retrieved", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
