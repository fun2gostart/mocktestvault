#!/usr/bin/env python3
"""
Comprehensive Question Bank Auditor
Scans every JSON question file in mocktestvault.com/data/
Validates:
1. JSON syntax and structure
2. Question text and non-empty prompt
3. Exactly 4 unique options
4. Answer index in range 0..3 (or letter A..D)
5. Explanation present and consistency with answer
6. Duplicate questions within files
7. Placeholder detection (TODO, TBD, Lorem, etc.)
"""

import os
import glob
import json
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

total_files = 0
total_questions = 0
issues = []
warnings = []

def normalize_answer(q):
    if 'answer' in q:
        ans = q['answer']
    elif 'correct' in q:
        ans = q['correct']
    elif 'correctAnswer' in q:
        ans = q['correctAnswer']
    else:
        return None
        
    if isinstance(ans, int):
        return ans
    if isinstance(ans, str):
        ans_s = ans.strip().upper()
        mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        if ans_s in mapping:
            return mapping[ans_s]
        if ans_s.isdigit():
            return int(ans_s)
    return None

for root, _, files in os.walk(DATA_DIR):
    for fname in sorted(files):
        if not fname.endswith('.json'):
            continue
            
        fpath = os.path.join(root, fname)
        rel_path = os.path.relpath(fpath, DATA_DIR)
        total_files += 1
        
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            issues.append(f"[{rel_path}] JSON SYNTAX ERROR: {e}")
            continue
            
        if isinstance(data, dict) and 'questions' in data:
            qs = data['questions']
        elif isinstance(data, list):
            qs = data
        else:
            issues.append(f"[{rel_path}] UNKNOWN FORMAT: neither list nor dict with 'questions'")
            continue
            
        file_q_texts = set()
        for idx, q in enumerate(qs):
            total_questions += 1
            qid = q.get('id', f'q_{idx}')
            prefix = f"[{rel_path} | #{idx+1} ({qid})]"
            
            # 1. Question text
            q_text = q.get('question', '')
            if not isinstance(q_text, str) or not q_text.strip():
                issues.append(f"{prefix} Missing or empty question text")
            elif len(q_text.strip()) < 10:
                warnings.append(f"{prefix} Extremely short question text: '{q_text}'")
                
            # Duplicate text check within file
            norm_q = " ".join(q_text.lower().split())
            if norm_q in file_q_texts:
                warnings.append(f"{prefix} Duplicate question text in same file")
            else:
                file_q_texts.add(norm_q)
                
            # Placeholders
            for ph in ['TODO', 'TBD', 'LOREM IPSUM', 'REPLACE ME']:
                if ph in q_text.upper():
                    issues.append(f"{prefix} Contains placeholder '{ph}' in question")
                    
            # 2. Options
            opts = q.get('options', [])
            if not isinstance(opts, list):
                issues.append(f"{prefix} 'options' is not a list")
                continue
            # Allow 4 options normally, or 5 options for GRE
            expected_count = 5 if 'gre' in rel_path.lower() else 4
            if len(opts) not in [4, 5]:
                issues.append(f"{prefix} Expected 4 or 5 options, found {len(opts)}")
            elif 'gre' not in rel_path.lower() and len(opts) != 4:
                issues.append(f"{prefix} Non-GRE test expected 4 options, found {len(opts)}")
            else:
                for o_idx, opt in enumerate(opts):
                    if not str(opt).strip():
                        issues.append(f"{prefix} Option {o_idx} is empty")
                # Duplicate options
                norm_opts = [str(o).strip().lower() for o in opts]
                if len(set(norm_opts)) < len(norm_opts):
                    warnings.append(f"{prefix} Duplicate option texts: {opts}")
                    
            # 3. Answer index
            ans_idx = normalize_answer(q)
            if ans_idx is None:
                issues.append(f"{prefix} Missing or invalid answer key: {q.get('answer')}")
            elif ans_idx < 0 or ans_idx >= len(opts):
                issues.append(f"{prefix} Answer index {ans_idx} out of bounds (options len={len(opts)})")
                
            # 4. Explanation
            exp = q.get('explanation', '')
            if not isinstance(exp, str) or not exp.strip():
                warnings.append(f"{prefix} Missing explanation")
            else:
                # Check for obvious letter contradiction in explanation
                # e.g. "Option (A) is correct" when ans_idx == 2 (C)
                letters = ['A', 'B', 'C', 'D']
                match = re.search(r'\b(?:Option|Choice)\s*\(([A-D])\)\s*is\s*correct', exp, re.IGNORECASE)
                if not match:
                    match = re.search(r'\b(?:Option|Choice)\s*([A-D])\s*is\s*correct', exp, re.IGNORECASE)
                if not match:
                    match = re.search(r'^\s*\(?([A-D])\)?\s*is\s*(?:the\s*)?correct', exp, re.IGNORECASE)
                if not match:
                    match = re.search(r'^\s*Correct\s*(?:Option|Answer):\s*\(?([A-D])\)?', exp, re.IGNORECASE)
                    
                if match and ans_idx is not None and ans_idx < 4:
                    mentioned_letter = match.group(1).upper()
                    expected_letter = letters[ans_idx]
                    if mentioned_letter != expected_letter:
                        # Check if explanation literally says another option is correct
                        warnings.append(f"{prefix} POTENTIAL KEY MISMATCH: Explanation mentions '{mentioned_letter}' is correct, but answer index is {ans_idx} ({expected_letter})")

print("=" * 60)
print(f"AUDIT SUMMARY: Scanned {total_files} files, {total_questions} total questions")
print("=" * 60)

print(f"\nCRITICAL ISSUES ({len(issues)}):")
for iss in issues[:30]:
    print(" ❌", iss)
if len(issues) > 30:
    print(f" ... and {len(issues) - 30} more issues")

print(f"\nWARNINGS / POTENTIAL MISMATCHES ({len(warnings)}):")
for w in warnings[:30]:
    print(" ⚠️", w)
if len(warnings) > 30:
    print(f" ... and {len(warnings) - 30} more warnings")

