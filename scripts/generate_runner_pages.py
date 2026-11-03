#!/usr/bin/env python3
"""
Generates the 8 runner HTML pages for MockTestVault:
1. mocktestvault.com/ssc-cgl/mock-02.html
2. mocktestvault.com/ssc-cgl/sectional-reasoning-02.html
3. mocktestvault.com/ssc-cgl/sectional-general-awareness-02.html
4. mocktestvault.com/ssc-cgl/sectional-quantitative-aptitude-02.html
5. mocktestvault.com/ssc-cgl/sectional-english-02.html
6. mocktestvault.com/global/gre/quantitative-reasoning-02.html
7. mocktestvault.com/global/gre/verbal-reasoning-02.html
8. mocktestvault.com/global/ielts/reading-practice-04.html
"""

import os

BASE_DIR = '/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com'

# --- 1. SSC CGL Mock 02 (Full 100 Qs) ---
with open(os.path.join(BASE_DIR, 'ssc-cgl/mock-01.html'), 'r', encoding='utf-8') as f:
    mock01_content = f.read()

mock02_content = mock01_content.replace(
    'SSC CGL Tier 1 Official Full Mock Test 01',
    'SSC CGL Tier 1 Official Full Mock Test 02'
).replace(
    'SSC CGL 2025–2026 Tier 1 Official Full Mock Test 01',
    'SSC CGL 2025–2026 Tier 1 Official Full Mock Test 02'
).replace(
    'Full Mock Test 01 (100 Qs)',
    'Full Mock Test 02 (100 Qs)'
).replace(
    'cgl_tier1_mock01_full.json',
    'cgl_tier1_mock02_full.json'
)

with open(os.path.join(BASE_DIR, 'ssc-cgl/mock-02.html'), 'w', encoding='utf-8') as f:
    f.write(mock02_content)
print("Created ssc-cgl/mock-02.html")

# --- 2. SSC CGL Sectional Reasoning 02 ---
with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-reasoning-01.html'), 'r', encoding='utf-8') as f:
    sec_reas_content = f.read()

sec_reas02_content = sec_reas_content.replace(
    'Reasoning Speed Test 01',
    'Reasoning Speed Test 02'
).replace(
    'Reasoning Speed Drill 01',
    'Reasoning Speed Drill 02'
).replace(
    'Test 01 Solutions & Shortcuts',
    'Test 02 Solutions & Shortcuts'
).replace(
    'cgl_tier1_mock01_reasoning.json',
    'cgl_tier1_mock02_reasoning.json'
)

with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-reasoning-02.html'), 'w', encoding='utf-8') as f:
    f.write(sec_reas02_content)
print("Created ssc-cgl/sectional-reasoning-02.html")

# --- 3. SSC CGL Sectional General Awareness 02 ---
with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-general-awareness-01.html'), 'r', encoding='utf-8') as f:
    sec_ga_content = f.read()

sec_ga02_content = sec_ga_content.replace(
    'General Awareness Speed Test 01',
    'General Awareness Speed Test 02'
).replace(
    'General Awareness Speed Drill 01',
    'General Awareness Speed Drill 02'
).replace(
    'Test 01 Solutions',
    'Test 02 Solutions'
).replace(
    'cgl_tier1_mock01_ga.json',
    'cgl_tier1_mock02_ga.json'
)

with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-general-awareness-02.html'), 'w', encoding='utf-8') as f:
    f.write(sec_ga02_content)
print("Created ssc-cgl/sectional-general-awareness-02.html")

# --- 4. SSC CGL Sectional Quantitative Aptitude 02 ---
with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-quantitative-aptitude-01.html'), 'r', encoding='utf-8') as f:
    sec_quant_content = f.read()

sec_quant02_content = sec_quant_content.replace(
    'Quantitative Aptitude Speed Test 01',
    'Quantitative Aptitude Speed Test 02'
).replace(
    'Quantitative Aptitude Speed Drill 01',
    'Quantitative Aptitude Speed Drill 02'
).replace(
    'Test 01 Solutions & Derivations',
    'Test 02 Solutions & Derivations'
).replace(
    'cgl_tier1_mock01_quant.json',
    'cgl_tier1_mock02_quant.json'
)

with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-quantitative-aptitude-02.html'), 'w', encoding='utf-8') as f:
    f.write(sec_quant02_content)
print("Created ssc-cgl/sectional-quantitative-aptitude-02.html")

# --- 5. SSC CGL Sectional English 02 ---
with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-english-01.html'), 'r', encoding='utf-8') as f:
    sec_eng_content = f.read()

sec_eng02_content = sec_eng_content.replace(
    'English Comprehension Speed Test 01',
    'English Comprehension Speed Test 02'
).replace(
    'English Comprehension Speed Drill 01',
    'English Comprehension Speed Drill 02'
).replace(
    'Test 01 Rules & Explanations',
    'Test 02 Rules & Explanations'
).replace(
    'cgl_tier1_mock01_english.json',
    'cgl_tier1_mock02_english.json'
)

with open(os.path.join(BASE_DIR, 'ssc-cgl/sectional-english-02.html'), 'w', encoding='utf-8') as f:
    f.write(sec_eng02_content)
print("Created ssc-cgl/sectional-english-02.html")

# --- 6. GRE Quantitative Reasoning 02 ---
with open(os.path.join(BASE_DIR, 'global/gre/quantitative-reasoning-01.html'), 'r', encoding='utf-8') as f:
    gre_quant_content = f.read()

gre_quant02_content = gre_quant_content.replace(
    'quantitative-reasoning-01.html',
    'quantitative-reasoning-02.html'
).replace(
    'Quantitative Reasoning Diagnostic Drill 01',
    'Quantitative Reasoning Diagnostic Drill 02'
).replace(
    'Quantitative Reasoning Diagnostic Test 01',
    'Quantitative Reasoning Diagnostic Test 02'
).replace(
    'gre_quant_set1.json',
    'gre_quant_set2.json'
)

with open(os.path.join(BASE_DIR, 'global/gre/quantitative-reasoning-02.html'), 'w', encoding='utf-8') as f:
    f.write(gre_quant02_content)
print("Created global/gre/quantitative-reasoning-02.html")

# --- 7. GRE Verbal Reasoning 02 ---
with open(os.path.join(BASE_DIR, 'global/gre/verbal-reasoning-01.html'), 'r', encoding='utf-8') as f:
    gre_verb_content = f.read()

gre_verb02_content = gre_verb_content.replace(
    'verbal-reasoning-01.html',
    'verbal-reasoning-02.html'
).replace(
    'Verbal Reasoning Diagnostic Drill 01',
    'Verbal Reasoning Diagnostic Drill 02'
).replace(
    'Verbal Reasoning Diagnostic Test 01',
    'Verbal Reasoning Diagnostic Test 02'
).replace(
    'gre_verbal_set1.json',
    'gre_verbal_set2.json'
)

with open(os.path.join(BASE_DIR, 'global/gre/verbal-reasoning-02.html'), 'w', encoding='utf-8') as f:
    f.write(gre_verb02_content)
print("Created global/gre/verbal-reasoning-02.html")

# --- 8. IELTS Academic Reading Practice Test 04 ---
with open(os.path.join(BASE_DIR, 'global/ielts/reading-practice-03.html'), 'r', encoding='utf-8') as f:
    ielts_content = f.read()

ielts04_content = ielts_content.replace(
    'reading-practice-03.html',
    'reading-practice-04.html'
).replace(
    'Practice Test 03: Cryptography, Cryosphere & Biomimetics',
    'Practice Test 04: Hydrothermal Vents, Mycorrhizal Networks & Acoustic Archaeology'
).replace(
    'Practice Test 03',
    'Practice Test 04'
).replace(
    'featuring the Voynich Manuscript, polar albedo feedback mechanisms, and gecko dry adhesion biomimetics.',
    'featuring deep-sea hydrothermal vents, mycorrhizal fungal networks, and Upper Paleolithic acoustic archaeology.'
).replace(
    "initialSet: 'set3',",
    "initialSet: 'set4',"
).replace(
    "set3: '../../data/global/ielts/ielts_reading_set3.json'",
    "set3: '../../data/global/ielts/ielts_reading_set3.json',\n          set4: '../../data/global/ielts/ielts_reading_set4.json'"
)

with open(os.path.join(BASE_DIR, 'global/ielts/reading-practice-04.html'), 'w', encoding='utf-8') as f:
    f.write(ielts04_content)
print("Created global/ielts/reading-practice-04.html")
