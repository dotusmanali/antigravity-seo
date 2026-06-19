#!/usr/bin/env python3
"""
Ahrefs Domain Rating - Free Endpoint Wrapper
Author: dotusmanali <dotusmanali@gmail.com>
Repository: https://github.com/dotusmanali/antigravity-seo
License: MIT

This script fetches the free Domain Rating (DR) score for a domain or URL
using Ahrefs' public free endpoint. No API key required.
"""

import argparse
import sys
import json
import requests

def get_domain_rating(target: str) -> dict:
    """
    Fetch Domain Rating from Ahrefs free endpoint.
    
    Args:
        target (str): Domain or URL to check.
        
    Returns:
        dict: A dictionary containing "domain_rating" (float) and "license" (str).
    """
    resp = requests.get(
        "https://api.ahrefs.com/v3/public/domain-rating-free",
        params={"target": target, "output": "json"},
        headers={"Accept": "application/json"},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()["domain_rating"]

def main():
    parser = argparse.ArgumentParser(description="Fetch Ahrefs Domain Rating for a target domain or URL")
    parser.add_argument("target", help="Target domain or URL (e.g. example.com)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON response")
    args = parser.parse_args()
    
    try:
        dr_data = get_domain_rating(args.target)
        if args.json:
            print(json.dumps(dr_data, indent=2))
        else:
            print(f"Domain: {args.target}")
            print(f"Ahrefs Domain Rating: {dr_data.get('domain_rating', 0.0)}")
            print(f"Attribution: {dr_data.get('license', 'Domain Rating by Ahrefs (ahrefs.com)')}")
    except Exception as e:
        if args.json:
            print(json.dumps({"error": str(e)}))
        else:
            print(f"Error fetching Domain Rating: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
