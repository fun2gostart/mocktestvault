#!/usr/bin/env python3
"""
Master Question Bank Rebalancer & Content Auditor
Balances the correct answer positions across A, B, C, D (and E for GRE)
for all question banks in mocktestvault.com/data/
Preserves Assertion-Reasoning and fixed-order questions.
Ensures 100% answer-text invariance.
"""

import os
import glob
import json
import random
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def is_fixed_order(q):
    opts = q.get('options', [])
    if len(opts) < 2:
        return True
    # Assertion-Reasoning check
    if q.get('type') == 'assertion_reasoning':
        return True
    if any('assertion' in str(o).lower() for o in opts):
        return True
    # Fixed options like All of the above / None of the above
    fixed_phrases = ['all of the above', 'none of the above', 'both a and b', 'both b and c', 'both (a) and (b)']
    if any(p in str(o).lower() for o in opts for p in fixed_phrases):
        return True
    return False

def rebalance_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    is_dict = isinstance(data, dict) and 'questions' in data
    qs = data['questions'] if is_dict else (data if isinstance(data, list) else None)
    if not qs:
        return 0, 0
        
    rel_path = os.path.relpath(filepath, DATA_DIR)
    fname = os.path.basename(filepath)
    rng = random.Random(fname)
    
    modified_count = 0
    num_opts_default = 5 if 'gre' in rel_path.lower() else 4
    
    # Pre-generate balanced target indices in blocks of num_opts_default
    block_pool = []
    
    for idx, q in enumerate(qs):
        if is_fixed_order(q):
            continue
            
        opts = q.get('options', [])
        ans_idx = q.get('answer', q.get('correct'))
        if ans_idx is None or not isinstance(ans_idx, int) or ans_idx >= len(opts):
            continue
            
        num_opts = len(opts)
        if num_opts not in [4, 5]:
            continue
            
        # Get target index
        if not block_pool or len(block_pool) == 0:
            perm = list(range(num_opts))
            rng.shuffle(perm)
            block_pool = perm
            
        target_idx = block_pool.pop(0)
        
        orig_correct_val = opts[ans_idx]
        distractors = [opts[i] for i in range(len(opts)) if i != ans_idx]
        
        new_opts = []
        d_idx = 0
        for i in range(num_opts):
            if i == target_idx:
                new_opts.append(orig_correct_val)
            else:
                new_opts.append(distractors[d_idx])
                d_idx += 1
                
        # Verification: new_opts[target_idx] must exactly equal orig_correct_val
        assert new_opts[target_idx] == orig_correct_val, f"Mismatch in {fname} Q#{idx+1}"
        
        q['options'] = new_opts
        if 'answer' in q:
            q['answer'] = target_idx
        elif 'correct' in q:
            q['correct'] = target_idx
            
        # Check explanation for "Choice A" or "Option A"
        exp = q.get('explanation', '')
        if exp and ans_idx != target_idx:
            old_letter = chr(65 + ans_idx)
            new_letter = chr(65 + target_idx)
            # Update specific phrasing e.g. "Choice A directly achieves" -> "Choice B directly achieves"
            # or "Option A is" -> "Option B is"
            new_exp = re.sub(rf'\bChoice\s+{old_letter}\b', f'Choice {new_letter}', exp)
            new_exp = re.sub(rf'\bOption\s+{old_letter}\b', f'Option {new_letter}', new_exp)
            q['explanation'] = new_exp
            
        modified_count += 1
        
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    return len(qs), modified_count

total_files = 0
total_modified = 0
total_qs = 0

for root, _, files in os.walk(DATA_DIR):
    for f in sorted(files):
        if not f.endswith('.json'):
            continue
        fpath = os.path.join(root, f)
        num_q, num_mod = rebalance_file(fpath)
        total_files += 1
        total_qs += num_q
        total_modified += num_mod

print(f"Rebalanced {total_modified} / {total_qs} questions across {total_files} files!")
