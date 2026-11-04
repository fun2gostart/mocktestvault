#!/usr/bin/env python3
"""
Systematically inject Google tag (gtag.js: G-05SFM1Q4MV) into all production HTML pages
on MockTestVault immediately following the opening <head> tag.
"""

import os
from pathlib import Path

ROOT_DIR = Path("/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com")

GTAG_SNIPPET = """<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-05SFM1Q4MV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-05SFM1Q4MV');
  </script>"""

def main():
    html_files = sorted(ROOT_DIR.glob("**/*.html"))
    updated = 0
    skipped = 0

    for file_path in html_files:
        # Skip Google verification file
        if file_path.name.startswith("google") and file_path.name.endswith(".html"):
            continue

        content = file_path.read_text(encoding="utf-8")

        if "G-05SFM1Q4MV" in content:
            skipped += 1
            continue

        if "<head>" in content:
            new_content = content.replace("<head>", GTAG_SNIPPET, 1)
            file_path.write_text(new_content, encoding="utf-8")
            updated += 1
        else:
            print(f"Warning: No <head> tag in {file_path}")

    print("=" * 60)
    print(f"Google Tag Injection Complete:")
    print(f"  • Updated files: {updated}")
    print(f"  • Already tagged / skipped: {skipped}")
    print(f"  • Total verified: {updated + skipped}")
    print("=" * 60)

if __name__ == "__main__":
    main()
