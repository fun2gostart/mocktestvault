#!/usr/bin/env python3
"""
Check answer key distribution (A, B, C, D) across all suites
"""

import os
import glob
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

suites = {
    "Digital SAT Math (100 Qs)": glob.glob(os.path.join(DATA_DIR, "us", "sat", "digital_sat_math_set*.json")),
    "Digital SAT Reading (100 Qs)": glob.glob(os.path.join(DATA_DIR, "us", "sat", "digital_sat_reading_set*.json")),
    "AP Calculus AB (100 Qs)": glob.glob(os.path.join(DATA_DIR, "us", "ap", "ap_calculus_ab_set*.json")),
    "AP Physics 1 (100 Qs)": glob.glob(os.path.join(DATA_DIR, "us", "ap", "ap_physics_1_set*.json")),
    "AP US History (100 Qs)": glob.glob(os.path.join(DATA_DIR, "us", "ap", "ap_us_history_set*.json")),
    "IELTS Reading (60 Qs)": glob.glob(os.path.join(DATA_DIR, "global", "ielts", "ielts_reading_set*.json")),
    "GRE Quant (20 Qs)": glob.glob(os.path.join(DATA_DIR, "global", "gre", "gre_quant_set*.json")),
    "GRE Verbal (20 Qs)": glob.glob(os.path.join(DATA_DIR, "global", "gre", "gre_verbal_set*.json")),
    "SSC CGL Tier 1 Mock 01 (100 Qs)": [os.path.join(DATA_DIR, "in", "ssc", "cgl_tier1_mock01_full.json")],
    "CBSE 80M Sample Papers (240 Qs)": glob.glob(os.path.join(DATA_DIR, "in", "cbse10", "sample-papers", "*.json"))
}

letters = ['A', 'B', 'C', 'D', 'E']

print(f"{'Exam Suite':<35} | {'Total':<6} | {'A':<6} | {'B':<6} | {'C':<6} | {'D':<6} | {'E':<6}")
print("-" * 75)

for name, files in suites.items():
    dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    total = 0
    for f in sorted(files):
        data = json.load(open(f))
        qs = data.get('questions', data) if isinstance(data, dict) else data
        for q in qs:
            ans = q.get('answer', q.get('correct'))
            if isinstance(ans, int) and ans in dist:
                dist[ans] += 1
                total += 1
    pcts = [f"{dist[i]/max(1, total)*100:0.0f}%" for i in range(5)]
    print(f"{name:<35} | {total:<6} | {pcts[0]:<6} | {pcts[1]:<6} | {pcts[2]:<6} | {pcts[3]:<6} | {pcts[4]:<6}")

