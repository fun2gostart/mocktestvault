#!/usr/bin/env python3
"""
Scan for any letter designations in explanations across all JSON files
"""

import os
import json
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
found = []

for root, _, files in os.walk(DATA_DIR):
    for f in sorted(files):
        if not f.endswith('.json'):
            continue
        fpath = os.path.join(root, f)
        rel = os.path.relpath(fpath, DATA_DIR)
        d = json.load(open(fpath))
        qs = d.get('questions', d) if isinstance(d, dict) else d
        for idx, q in enumerate(qs):
            exp = q.get('explanation', '')
            # Look for phrases like: "option A", "option (b)", "choice C", "correct answer is D", etc.
            m = re.findall(r'\b(?:option|choice|answer is|correct is)\s*\(?([a-eA-E])\)?\b', exp, re.IGNORECASE)
            if m:
                found.append((rel, idx + 1, q.get('id'), m, exp[:100]))

print(f"Total letter mentions found in explanations: {len(found)}")
for item in found[:20]:
    print(f"  {item[0]} Q#{item[1]} ({item[2]}): {item[3]} -> {item[4]}")
if len(found) > 20:
    print(f"  ... and {len(found) - 20} more")
