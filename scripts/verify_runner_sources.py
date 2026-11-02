#!/usr/bin/env python3
"""
Verify all JSON sources referenced by HTML test runners
"""

import os
import glob
import re
import json

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")

html_files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)

referenced_json_paths = set()
missing_refs = []
runner_count = 0

for hpath in html_files:
    if ".git" in hpath or "google608ef" in hpath:
        continue
    with open(hpath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Match setSources or fetch paths
    matches = re.findall(r'[\'"]([^\'"]+\.json)[\'"]', content)
    if matches:
        runner_count += 1
        hdir = os.path.dirname(hpath)
        for m in matches:
            resolved = os.path.normpath(os.path.join(hdir, m))
            referenced_json_paths.add(resolved)
            if not os.path.exists(resolved):
                missing_refs.append((hpath, m, resolved))

print(f"Total HTML Runners with JSON references: {runner_count}")
print(f"Total Unique JSON files referenced: {len(referenced_json_paths)}")

if missing_refs:
    print(f"\n❌ MISSING REFERENCES ({len(missing_refs)}):")
    for h, m, r in missing_refs:
        print(f"  {h} -> {m} (resolved to {r})")
else:
    print("\n✓ 100% of referenced JSON files exist on disk!")

