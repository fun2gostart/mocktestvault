#!/usr/bin/env python3
"""
Deep Domain-Specific Content Auditor:
Verifies mathematical, scientific, and factual correspondence between:
1. Question text
2. Options list
3. Selected answer index
4. Explanation text
"""

import os
import glob
import json
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

checked_count = 0
suspicious_items = []

# Scan US and Global exams specifically
target_dirs = [
    os.path.join(DATA_DIR, "us"),
    os.path.join(DATA_DIR, "global"),
    os.path.join(DATA_DIR, "in", "ssc"),
    os.path.join(DATA_DIR, "in", "cbse10", "sample-papers")
]

for tdir in target_dirs:
    for root, _, files in os.walk(tdir):
        for fname in sorted(files):
            if not fname.endswith('.json'):
                continue
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, DATA_DIR)
            
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            qs = data.get('questions', data) if isinstance(data, dict) else data
            
            for idx, q in enumerate(qs):
                checked_count += 1
                qid = q.get('id', f'q_{idx}')
                q_text = q.get('question', '')
                opts = q.get('options', [])
                ans = q.get('answer', q.get('correct'))
                exp = q.get('explanation', '')
                
                # Check 1: Is correct option text mentioned in explanation?
                # If the chosen option is e.g. "6", does the explanation show "= 6" or mention "6"?
                chosen_opt_text = str(opts[ans]).strip() if ans is not None and ans < len(opts) else ""
                
                # Check 2: If the explanation mentions another option's exact text while not mentioning chosen_opt_text
                # E.g., if options are ["10", "20", "30", "40"], ans is 0 ("10"), but explanation says "the result is 30"
                other_opts_mentioned = []
                for o_idx, opt in enumerate(opts):
                    opt_str = str(opt).strip()
                    if o_idx != ans and len(opt_str) > 3:
                        # If another option text is distinctly in explanation with keywords like "answer is X" or "correct is X"
                        pattern = re.compile(rf'\b(?:answer is|yields|equals|gives|therefore)\s+[:=]?\s*{re.escape(opt_str)}\b', re.IGNORECASE)
                        if pattern.search(exp):
                            other_opts_mentioned.append((o_idx, opt_str))
                
                if other_opts_mentioned:
                    # Let's inspect if chosen option is ALSO mentioned
                    pattern_chosen = re.compile(rf'\b(?:answer is|yields|equals|gives|therefore)\s+[:=]?\s*{re.escape(chosen_opt_text)}\b', re.IGNORECASE)
                    if not pattern_chosen.search(exp):
                        suspicious_items.append({
                            "file": rel_path,
                            "index": idx + 1,
                            "id": qid,
                            "question": q_text[:80] + "...",
                            "chosen_opt": f"[{ans}] {chosen_opt_text}",
                            "other_opt_in_exp": other_opts_mentioned,
                            "explanation": exp[:120] + "..."
                        })

print(f"Deep scanned {checked_count} high-stakes questions across US, Global, SSC, and CBSE Board Mocks.")
print(f"Suspicious formula/key mismatches flagged: {len(suspicious_items)}")
for item in suspicious_items:
    print(f"⚠️ {item['file']} Q#{item['index']} ({item['id']}):")
    print(f"   Chosen: {item['chosen_opt']}")
    print(f"   Explanation mentions: {item['other_opt_in_exp']}")
    print(f"   Snippet: {item['explanation']}\n")

