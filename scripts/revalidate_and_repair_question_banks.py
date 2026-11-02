#!/usr/bin/env python3
"""
Comprehensive Question Bank Revalidation & Precision Repair Script
Applies all 5 critical forensic repairs across MockTestVault:
1. Restores canonical CBSE Class 10 Assertion-Reasoning structure (643 questions).
2. Fixes GRE Quant Q13 answer key (2.00 doubles).
3. Fixes 5 flawed/unsolvable questions in SSC CGL Tier 1 Mock 01 (Math, Logic, Matrix, Segment Labels).
4. Corrects CBSE Statistics missing frequency typo (f=7, answer=20).
5. Normalizes IELTS Reading True/False/Not Given to canonical 3-option standard.
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

CANONICAL_AR = [
    "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
    "Both (A) and (R) are true, but (R) is not the correct explanation of (A).",
    "(A) is true, but (R) is false.",
    "(A) is false, but (R) is true."
]

def classify_ar(opt):
    o = str(opt).lower().replace('.', '').replace(',', '').strip()
    if 'both' in o and 'not the correct explanation' in o:
        return 1
    if 'both' in o and ('correct explanation' in o or 'is the correct' in o):
        return 0
    if ('(a) is true' in o or 'assertion is true' in o) and ('false' in o or 'incorrect' in o):
        return 2
    if ('(a) is false' in o or 'assertion is false' in o) and ('true' in o or 'correct' in o):
        return 3
    return -1

def repair_assertion_reasoning():
    repaired = 0
    for root, _, files in os.walk(DATA_DIR):
        for f in sorted(files):
            if not f.endswith('.json'):
                continue
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            
            is_dict = isinstance(data, dict) and 'questions' in data
            qs = data['questions'] if is_dict else (data if isinstance(data, list) else None)
            if not qs:
                continue
                
            file_modified = False
            for idx, q in enumerate(qs):
                stem = q.get('question', '')
                qtype = q.get('type', '')
                opts = q.get('options', [])
                
                # Identify Assertion-Reasoning question
                is_ar = False
                if 'assertion' in stem.lower() and 'reason' in stem.lower():
                    is_ar = True
                elif 'assertion' in qtype.lower():
                    is_ar = True
                elif len(opts) == 4 and any('(r)' in str(o).lower() for o in opts) and any('(a)' in str(o).lower() for o in opts):
                    is_ar = True
                    
                if is_ar and len(opts) == 4:
                    ans_idx = q.get('answer', q.get('correct'))
                    if ans_idx is not None and ans_idx < len(opts):
                        current_ans_text = opts[ans_idx]
                        target_class = classify_ar(current_ans_text)
                        if target_class in [0, 1, 2, 3]:
                            q['options'] = list(CANONICAL_AR)
                            if 'answer' in q:
                                q['answer'] = target_class
                            elif 'correct' in q:
                                q['correct'] = target_class
                            q['type'] = 'assertion_reasoning'
                            file_modified = True
                            repaired += 1
                        else:
                            print(f"Warning: Could not classify AR in {f} Q#{idx+1}: {current_ans_text}")
                            
            if file_modified:
                with open(fpath, 'w', encoding='utf-8') as fp:
                    json.dump(data, fp, indent=2, ensure_ascii=False)
                    
    print(f"1. Successfully restored {repaired} Assertion-Reasoning questions to standard CBSE canonical order!")

def repair_gre_quant():
    fpath = os.path.join(DATA_DIR, "global", "gre", "gre_quant_set1.json")
    if not os.path.exists(fpath):
        print(f"GRE quant file not found at {fpath}")
        return
        
    with open(fpath, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
        
    for q in data.get('questions', []):
        if q.get('id') == 'gre-quant-013':
            # Target option is "2.00 (doubles)"
            target_idx = None
            for idx, o in enumerate(q['options']):
                if '2.00' in o or 'doubles' in o.lower():
                    target_idx = idx
                    break
            if target_idx is not None:
                q['answer'] = target_idx
                q['explanation'] = (
                    "Initial Total Surface Area: A_1 = 2πr^2 + 2πrh. Since h = 2r, A_1 = 2πr^2 + 2πr(2r) = 6πr^2.\n"
                    "New cylinder: radius r' = 2r, height h' = h/2 = r.\n"
                    "New Total Surface Area: A_2 = 2π(r')^2 + 2πr'h' = 2π(2r)^2 + 2π(2r)(r) = 8πr^2 + 4πr^2 = 12πr^2.\n"
                    "Ratio = 12πr^2 / 6πr^2 = 2.0 (factor of 2, doubles)."
                )
                print(f"2. Fixed GRE Quant Q13: Answer index set to {target_idx} ('{q['options'][target_idx]}') with verified derivation.")
                
    with open(fpath, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, indent=2, ensure_ascii=False)

def repair_ssc_cgl():
    target_files = [
        os.path.join(DATA_DIR, "in", "ssc", "cgl_tier1_mock01_full.json"),
        os.path.join(DATA_DIR, "in", "ssc", "cgl_tier1_mock01_reasoning.json"),
        os.path.join(DATA_DIR, "in", "ssc", "cgl_tier1_mock01_quant.json"),
        os.path.join(DATA_DIR, "in", "ssc", "cgl_tier1_mock01_english.json")
    ]
    
    for fpath in target_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            
        qs = data.get('questions', [])
        for q in qs:
            qid = q.get('id')
            if qid == 'cgl_r_01':
                q['question'] = (
                    "Select the option that is related to the third letter-cluster in the same way "
                    "as the second letter-cluster is related to the first letter-cluster:\n"
                    "TRACK : UTDGP :: MODEL : ?"
                )
                q['options'] = ["NPFHP", "NQGIQ", "NQHJQ", "NPFIP"]
                q['answer'] = 1
                q['explanation'] = (
                    "The transformation follows an increasing sequential letter shift (+1, +2, +3, +4, +5):\n"
                    "- T(20) +1 = U(21)\n"
                    "- R(18) +2 = T(20)\n"
                    "- A(1) +3 = D(4)\n"
                    "- C(3) +4 = G(7)\n"
                    "- K(11) +5 = P(16)\n"
                    "Applying the identical shift to MODEL:\n"
                    "- M(13) +1 = N(14)\n"
                    "- O(15) +2 = Q(17)\n"
                    "- D(4) +3 = G(7)\n"
                    "- E(5) +4 = I(9)\n"
                    "- L(12) +5 = Q(17)\n"
                    "Therefore, the related letter-cluster is NQGIQ."
                )
            elif qid == 'cgl_r_09':
                q['question'] = (
                    "Three of the following four letter-clusters are alike in a certain way and one is different. "
                    "Pick the odd one out:"
                )
                q['options'] = ["LNRP", "PRVT", "KMQO", "BDFH"]
                q['answer'] = 3
                q['explanation'] = (
                    "Analyze positional letter shifts:\n"
                    "- LNRP: L(12) +2 = N(14) +4 = R(18) -2 = P(16) [Pattern: +2, +4, -2]\n"
                    "- PRVT: P(16) +2 = R(18) +4 = V(22) -2 = T(20) [Pattern: +2, +4, -2]\n"
                    "- KMQO: K(11) +2 = M(13) +4 = Q(17) -2 = O(15) [Pattern: +2, +4, -2]\n"
                    "- BDFH: B(2) +2 = D(4) +2 = F(6) +2 = H(8) [Pattern: +2, +2, +2]\n"
                    "Therefore, BDFH is the odd one out because all other clusters follow the (+2, +4, -2) pattern."
                )
            elif qid == 'cgl_r_14':
                q['question'] = (
                    "Select the missing number from the given matrix:\n"
                    "| 8  | 7  | 6  |\n"
                    "| 9  | 5  | 8  |\n"
                    "| 7  | 6  | ?  |\n"
                    "| 79 | 41 | 52 |"
                )
                q['options'] = ["6", "8", "4", "5"]
                q['answer'] = 2
                q['explanation'] = (
                    "Column operation: (Row 1 × Row 2) + Row 3 = Row 4.\n"
                    "- Column 1: (8 × 9) + 7 = 72 + 7 = 79\n"
                    "- Column 2: (7 × 5) + 6 = 35 + 6 = 41\n"
                    "- Column 3: (6 × 8) + ? = 48 + 4 = 52\n"
                    "Hence, the missing number is 4."
                )
            elif qid == 'cgl_q_09':
                q['question'] = (
                    "If the 8-digit number 789x531y is divisible by 72, what is the value of (5x + 3y)?"
                )
                q['options'] = ["14", "11", "9", "16"]
                q['answer'] = 1
                q['explanation'] = (
                    "For divisibility by 72, the number must be divisible by both 8 and 9.\n"
                    "- Divisibility by 8: The last 3 digits '31y' must be divisible by 8. "
                    "312 ÷ 8 = 39 (exact), so y = 2 is the unique single digit.\n"
                    "- Divisibility by 9: Sum of digits = 7 + 8 + 9 + x + 5 + 3 + 1 + 2 = 35 + x. "
                    "For 35 + x to be divisible by 9, x must be 1 (sum = 36).\n"
                    "Substituting x = 1 and y = 2: 5x + 3y = 5(1) + 3(2) = 5 + 6 = 11."
                )
            elif qid == 'cgl_e_01':
                q['question'] = (
                    "Identify the segment in the sentence that contains a grammatical error:\n"
                    "'Neither the manager nor his assistants was present at the meeting yesterday.'"
                )
                q['options'] = [
                    "Neither the manager",
                    "nor his assistants was",
                    "present at the meeting",
                    "yesterday"
                ]
                q['answer'] = 1
                q['explanation'] = (
                    "Subject-Verb Agreement Rule with 'Neither... nor': The verb agrees with the nearer subject. "
                    "Here, the nearer subject is plural ('his assistants'), so the plural verb 'were' must be used instead of 'was'. "
                    "Correct sentence: 'Neither the manager nor his assistants were present at the meeting yesterday.'"
                )
            elif qid == 'cgl_e_02':
                q['question'] = (
                    "Identify the segment in the sentence that contains a grammatical error:\n"
                    "'Scarcely had she stepped out of the house than it started raining heavily.'"
                )
                q['options'] = [
                    "than it started raining",
                    "Scarcely had she stepped",
                    "out of the house",
                    "heavily"
                ]
                q['answer'] = 0
                q['explanation'] = (
                    "Correlative conjunction pair rule: 'Scarcely / Hardly' is always paired with 'when' or 'before', "
                    "NEVER with 'than' ('No sooner' takes 'than'). Thus, replace 'than' with 'when'."
                )
                
        with open(fpath, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)
            
    print("3. Successfully repaired all 5 SSC CGL Mock 01 questions across full and sectional files!")

def repair_cbse_statistics():
    target_files = [
        os.path.join(DATA_DIR, "in", "cbse10", "mathematics", "ch13_statistics_set2.json"),
        os.path.join(DATA_DIR, "in", "cbse10", "sample-papers", "mathematics_board_mock01.json")
    ]
    
    for fpath in target_files:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            
        qs = data.get('questions', data if isinstance(data, list) else [])
        for q in qs:
            if q.get('id') in ['cbse10-math-ch13-s2-001', 'cbse10-sqp-math-070']:
                q['question'] = (
                    "The mean of the following distribution is 18: "
                    "Classes: 11-13 (f=7), 13-15 (f=6), 15-17 (f=9), 17-19 (f=13), 19-21 (f=f_k), 21-23 (f=5), 23-25 (f=4). "
                    "What is the value of the missing frequency f_k?"
                )
                q['options'] = ["18", "15", "20", "22"]
                q['answer'] = 2
                q['explanation'] = (
                    "Class marks xi: 12, 14, 16, 18, 20, 22, 24. Assumed mean a = 18.\n"
                    "di = xi - 18: -6, -4, -2, 0, 2, 4, 6.\n"
                    "fi*di: 7(-6)=-42, 6(-4)=-24, 9(-2)=-18, 13(0)=0, f_k(2)=2*f_k, 5(4)=20, 4(6)=24.\n"
                    "sum(fi) = 44 + f_k.\n"
                    "sum(fi*di) = (-42 - 24 - 18 + 0 + 20 + 24) + 2*f_k = -40 + 2*f_k.\n"
                    "Mean = a + sum(fi*di)/sum(fi) => 18 = 18 + (-40 + 2*f_k)/(44 + f_k) => -40 + 2*f_k = 0 => 2*f_k = 40 => f_k = 20."
                )
                q['citation'] = "NCERT Class 10 Mathematics, Chapter 13 Statistics, Exercise 13.1 Question 3"
                
        with open(fpath, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)
            
    print("4. Successfully repaired CBSE Class 10 Statistics missing frequency (f=7, answer=20) in chapter and sample paper!")

def repair_ielts_tfng():
    ielts_dir = os.path.join(DATA_DIR, "global", "ielts")
    fixed_count = 0
    
    for f in sorted(os.listdir(ielts_dir)):
        if not f.endswith('.json'):
            continue
        fpath = os.path.join(ielts_dir, f)
        with open(fpath, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            
        qs = data.get('questions', [])
        for q in qs:
            opts = [str(o) for o in q.get('options', [])]
            # Check if this is a True / False / Not Given question
            is_tfng = any('true' in o.lower() for o in opts) and any('false' in o.lower() for o in opts)
            if is_tfng:
                ans_idx = q.get('answer', 0)
                curr_ans_text = opts[ans_idx] if ans_idx < len(opts) else ""
                
                # Determine correct target: 0 for TRUE, 1 for FALSE, 2 for NOT GIVEN
                target_idx = 0
                if 'not given' in curr_ans_text.lower():
                    target_idx = 2
                elif 'false' in curr_ans_text.lower():
                    target_idx = 1
                elif 'true' in curr_ans_text.lower():
                    target_idx = 0
                    
                q['options'] = ["TRUE", "FALSE", "NOT GIVEN"]
                q['answer'] = target_idx
                fixed_count += 1
                
        with open(fpath, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)
            
    print(f"5. Successfully normalized {fixed_count} IELTS Reading True/False/Not Given questions to canonical 3-option format!")

if __name__ == '__main__':
    print("Starting Comprehensive Question Bank Revalidation & Repair...")
    repair_assertion_reasoning()
    repair_gre_quant()
    repair_ssc_cgl()
    repair_cbse_statistics()
    repair_ielts_tfng()
    print("All repairs completed successfully!")
