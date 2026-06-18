"""Startup dependency checker for Antigravity SEO scripts.

Import this module at the top of any script that uses third-party
packages. Call ``check()`` with a dict mapping import names to pip
package names. If any are missing, the script prints a friendly
message and exits instead of crashing with an ImportError traceback.

Usage::

    from _dep_check import check
    check({"bs4": "beautifulsoup4", "requests": "requests"})
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


def check(deps: dict[str, str]) -> None:
    """Verify *deps* are importable; exit gracefully if not.

    Parameters
    ----------
    deps : dict
        Mapping of ``{import_name: pip_package_name}``, e.g.
        ``{"bs4": "beautifulsoup4", "lxml": "lxml"}``.
    """
    missing: list[str] = []
    for mod, pkg in deps.items():
        try:
            importlib.import_module(mod)
        except ImportError:
            missing.append(pkg)
    if missing:
        req = Path(__file__).resolve().parent.parent / "requirements.txt"
        print(f"[!] Missing required Python dependencies: {', '.join(missing)}")
        print(f"    Please run: pip install {' '.join(missing)}")
        if req.exists():
            print(f"    Or install all: pip install -r {req}")
        sys.exit(1)
