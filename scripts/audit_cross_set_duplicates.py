#!/usr/bin/env python3
"""
Check for duplicate questions across sets within the same exam suite
"""

import os
import glob
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

suites = {
    "Digital SAT Math": glob.glob(os.path.join(DATA_DIR, "us", "sat", "digital_sat_math_set*.json")),
    "Digital SAT Reading": glob.glob(os.path.join(DATA_DIR, "us", "sat", "digital_sat_reading_set*.json")),
    "AP Calculus AB": glob.glob(os.path.join(DATA_DIR, "us", "ap", "ap_calculus_ab_set*.json")),
    "AP Physics 1": glob.glob(os.path.join(DATA_DIR, "us", "ap", "ap_physics_1_set*.json")),
    "AP US History": glob.glob(os.path.join(DATA_DIR, "us", "ap", "ap_us_history_set*.json")),
    "IELTS Academic Reading": glob.glob(os.path.join(DATA_DIR, "global", "ielts", "ielts_reading_set*.json")),
    "GRE Quant": glob.glob(os.path.join(DATA_DIR, "global", "gre", "gre_quant_set*.json")),
    "GRE Verbal": glob.glob(os.path.join(DATA_DIR, "global", "gre", "gre_verbal_set*.json")),
    "CBSE 80M Sample Papers": glob.glob(os.path.join(DATA_DIR, "in", "cbse10", "sample-papers", "*.json"))
}

duplicates_found = 0

for suite_name, files in suites.items():
    seen_prompts = {}
    print(f"\n--- Checking {suite_name} ({len(files)} files) ---")
    for f in sorted(files):
        fname = os.path.basename(f)
        data = json.load(open(f))
        qs = data.get('questions', data) if isinstance(data, dict) else data
        for idx, q in enumerate(qs):
            # Normalize prompt
            prompt = " ".join(q.get('question', '').lower().split())
            if prompt in seen_prompts:
                orig_file, orig_idx, orig_id = seen_prompts[prompt]
                print(f"  ⚠️ DUPLICATE DETECTED:")
                print(f"     Set A: {orig_file} #{orig_idx} ({orig_id})")
                print(f"     Set B: {fname} #{idx+1} ({q.get('id')})")
                print(f"     Snippet: {prompt[:80]}...")
                duplicates_found += 1
            else:
                seen_prompts[prompt] = (fname, idx + 1, q.get('id'))

print(f"\nTotal cross-set duplicates found across standardized suites: {duplicates_found}")
