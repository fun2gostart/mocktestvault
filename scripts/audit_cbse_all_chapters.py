#!/usr/bin/env python3
"""
Deep Content & Answer Verification for All 48 CBSE Class 10 Chapters (2,880 Questions)
"""

import os
import glob
import json
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "in", "cbse10")

total_qs = 0
flagged = []

for root, _, files in os.walk(DATA_DIR):
    for fname in sorted(files):
        if not fname.endswith('.json') or 'sample-papers' in root:
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, DATA_DIR)
        
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        qs = data.get('questions', data) if isinstance(data, dict) else data
        
        for idx, q in enumerate(qs):
            total_qs += 1
            qid = q.get('id', f'q_{idx}')
            opts = q.get('options', [])
            ans = q.get('answer', q.get('correct'))
            exp = q.get('explanation', '')
            
            if ans is None or not (0 <= ans < len(opts)):
                flagged.append((rel, idx + 1, qid, f"Invalid answer index {ans}"))
                continue
                
            chosen_opt = str(opts[ans]).strip()
            
            # Check for contradiction: Does the explanation explicitly say "Option (X)" or "(X) is correct" where X != ans?
            letters = ['A', 'B', 'C', 'D']
            m = re.search(r'\b(?:Option|Choice)\s*\(([A-D])\)\s*is\s*correct', exp, re.IGNORECASE)
            if not m:
                m = re.search(r'\b(?:Option|Choice)\s*([A-D])\s*is\s*correct', exp, re.IGNORECASE)
            if not m:
                m = re.search(r'^\s*\(?([A-D])\)?\s*is\s*(?:the\s*)?correct', exp, re.IGNORECASE)
            if not m:
                m = re.search(r'^\s*Correct\s*(?:Option|Answer):\s*\(?([A-D])\)?', exp, re.IGNORECASE)
                
            if m:
                exp_letter = m.group(1).upper()
                key_letter = letters[ans]
                if exp_letter != key_letter:
                    flagged.append((rel, idx + 1, qid, f"Explanation claims ({exp_letter}) is correct, but answer is index {ans} ({key_letter})"))

print(f"Scanned {total_qs} CBSE Class 10 chapter questions.")
print(f"Flagged contradiction items: {len(flagged)}")
for item in flagged:
    print("❌", item)
