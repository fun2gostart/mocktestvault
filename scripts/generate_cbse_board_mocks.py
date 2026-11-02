#!/usr/bin/env python3
"""
CBSE Class 10 Full 80-Mark Board Mock Papers Generator
Generates 3 full-syllabus 80-mark mock papers (80 Qs each = 240 Qs):
1. Science (Code 086) — 80 Questions
2. Mathematics (Code 041/241) — 80 Questions
3. Social Science (Code 087) — 80 Questions
"""

import json
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "in", "cbse10")
OUT_DIR = os.path.join(BASE_DIR, "sample-papers")
os.makedirs(OUT_DIR, exist_ok=True)

def load_chapter_sets(subj, ch_name):
    """Load sets 1, 2, 3 for a given chapter."""
    ch_path = os.path.join(BASE_DIR, subj)
    sets = {}
    for s in [1, 2, 3]:
        fpath = os.path.join(ch_path, f"{ch_name}_set{s}.json")
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                d = json.load(f)
                sets[s] = d["questions"] if isinstance(d, dict) else d
        else:
            print(f"Warning: Missing {fpath}")
            sets[s] = []
    return sets

def pick_balanced_qs(sets, count):
    """
    Picks 'count' questions from sets 1, 2, 3.
    Balances across Set 1 (core), Set 2 (exemplar/applied), and Set 3 (assertion/case).
    """
    picked = []
    # Distribution
    s1_count = max(1, count // 2)
    s3_count = max(1, count // 4)
    s2_count = count - s1_count - s3_count
    
    # Slice carefully from each set
    s1_slice = sets.get(1, [])[:s1_count]
    s2_slice = sets.get(2, [])[:s2_count]
    s3_slice = sets.get(3, [])[:s3_count]
    
    picked.extend(s1_slice)
    picked.extend(s2_slice)
    picked.extend(s3_slice)
    
    # If short, fill from remaining
    if len(picked) < count:
        for s in [1, 2, 3]:
            for q in sets.get(s, []):
                if q not in picked and len(picked) < count:
                    picked.append(q)
    return picked[:count]

# =========================================================================
# 1. SCIENCE (80 Questions)
# =========================================================================
science_blueprint = [
    # Section A: Chemistry (25 Qs)
    ("ch01_chemical_reactions", 6, "Section A: Chemical Substances"),
    ("ch02_acids_bases_salts", 6, "Section A: Chemical Substances"),
    ("ch03_metals_non_metals", 6, "Section A: Chemical Substances"),
    ("ch04_carbon_compounds", 7, "Section A: Chemical Substances"),
    # Section B: Biology (28 Qs)
    ("ch05_life_processes", 9, "Section B: World of Living"),
    ("ch06_control_coordination", 7, "Section B: World of Living"),
    ("ch07_how_organisms_reproduce", 7, "Section B: World of Living"),
    ("ch08_heredity", 5, "Section B: World of Living"),
    # Section C: Physics (23 Qs)
    ("ch09_light_reflection_refraction", 7, "Section C: Natural Phenomena & Effects of Current"),
    ("ch10_human_eye_colourful_world", 5, "Section C: Natural Phenomena & Effects of Current"),
    ("ch11_electricity", 6, "Section C: Natural Phenomena & Effects of Current"),
    ("ch12_magnetic_effects_electric_current", 5, "Section C: Natural Phenomena & Effects of Current"),
    # Section D: Natural Resources (4 Qs)
    ("ch13_our_environment", 4, "Section D: Natural Resources")
]

science_questions = []
q_id = 1
for ch_name, count, sec_name in science_blueprint:
    sets = load_chapter_sets("science", ch_name)
    chosen = pick_balanced_qs(sets, count)
    for q in chosen:
        q_copy = dict(q)
        q_copy["id"] = f"cbse10-sqp-sci-{q_id:03d}"
        q_copy["section"] = sec_name
        science_questions.append(q_copy)
        q_id += 1

print(f"Total Science Questions: {len(science_questions)}")
assert len(science_questions) == 80, f"Expected 80 Science questions, got {len(science_questions)}"

# =========================================================================
# 2. MATHEMATICS (80 Questions)
# =========================================================================
math_blueprint = [
    # Section A: Number Systems & Algebra (25 Qs)
    ("ch01_real_numbers", 5, "Section A: Number Systems & Algebra"),
    ("ch02_polynomials", 5, "Section A: Number Systems & Algebra"),
    ("ch03_linear_equations_two_variables", 5, "Section A: Number Systems & Algebra"),
    ("ch04_quadratic_equations", 5, "Section A: Number Systems & Algebra"),
    ("ch05_arithmetic_progressions", 5, "Section A: Number Systems & Algebra"),
    # Section B: Geometry & Coordinate Geometry (20 Qs)
    ("ch06_triangles", 7, "Section B: Geometry & Coordinate Geometry"),
    ("ch07_coordinate_geometry", 7, "Section B: Geometry & Coordinate Geometry"),
    ("ch10_circles", 6, "Section B: Geometry & Coordinate Geometry"),
    # Section C: Trigonometry & Mensuration (20 Qs)
    ("ch08_introduction_to_trigonometry", 6, "Section C: Trigonometry & Mensuration"),
    ("ch09_some_applications_of_trigonometry", 4, "Section C: Trigonometry & Mensuration"),
    ("ch11_areas_related_to_circles", 5, "Section C: Trigonometry & Mensuration"),
    ("ch12_surface_areas_volumes", 5, "Section C: Trigonometry & Mensuration"),
    # Section D: Statistics & Probability (15 Qs)
    ("ch13_statistics", 8, "Section D: Statistics & Probability"),
    ("ch14_probability", 7, "Section D: Statistics & Probability")
]

math_questions = []
q_id = 1
for ch_name, count, sec_name in math_blueprint:
    sets = load_chapter_sets("mathematics", ch_name)
    chosen = pick_balanced_qs(sets, count)
    for q in chosen:
        q_copy = dict(q)
        q_copy["id"] = f"cbse10-sqp-math-{q_id:03d}"
        q_copy["section"] = sec_name
        math_questions.append(q_copy)
        q_id += 1

print(f"Total Mathematics Questions: {len(math_questions)}")
assert len(math_questions) == 80, f"Expected 80 Math questions, got {len(math_questions)}"

# =========================================================================
# 3. SOCIAL SCIENCE (80 Questions)
# =========================================================================
sst_blueprint = [
    # Section A: History (20 Qs)
    ("ch01_rise_of_nationalism_europe", 4, "Section A: History (India & Contemporary World II)"),
    ("ch02_nationalism_in_india", 5, "Section A: History (India & Contemporary World II)"),
    ("ch03_making_of_a_global_world", 4, "Section A: History (India & Contemporary World II)"),
    ("ch04_age_of_industrialisation", 4, "Section A: History (India & Contemporary World II)"),
    ("ch05_print_culture_modern_world", 3, "Section A: History (India & Contemporary World II)"),
    # Section B: Geography (20 Qs)
    ("ch06_resources_and_development", 3, "Section B: Geography (Contemporary India II)"),
    ("ch07_forest_and_wildlife_resources", 3, "Section B: Geography (Contemporary India II)"),
    ("ch08_water_resources", 3, "Section B: Geography (Contemporary India II)"),
    ("ch09_agriculture", 4, "Section B: Geography (Contemporary India II)"),
    ("ch10_minerals_and_energy_resources", 3, "Section B: Geography (Contemporary India II)"),
    ("ch11_manufacturing_industries", 2, "Section B: Geography (Contemporary India II)"),
    ("ch12_lifelines_of_national_economy", 2, "Section B: Geography (Contemporary India II)"),
    # Section C: Political Science (20 Qs)
    ("ch13_power_sharing", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch14_federalism", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch15_gender_religion_caste", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch16_political_parties", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch17_outcomes_of_democracy", 4, "Section C: Political Science (Democratic Politics II)"),
    # Section D: Economics (20 Qs)
    ("ch18_development", 5, "Section D: Economics (Understanding Economic Development)"),
    ("ch19_sectors_of_indian_economy", 5, "Section D: Economics (Understanding Economic Development)"),
    ("ch20_money_and_credit", 5, "Section D: Economics (Understanding Economic Development)"),
    ("ch21_globalisation_and_indian_economy", 5, "Section D: Economics (Understanding Economic Development)")
]

sst_questions = []
q_id = 1
for ch_name, count, sec_name in sst_blueprint:
    sets = load_chapter_sets("social-science", ch_name)
    chosen = pick_balanced_qs(sets, count)
    for q in chosen:
        q_copy = dict(q)
        q_copy["id"] = f"cbse10-sqp-sst-{q_id:03d}"
        q_copy["section"] = sec_name
        sst_questions.append(q_copy)
        q_id += 1

print(f"Total Social Science Questions: {len(sst_questions)}")
assert len(sst_questions) == 80, f"Expected 80 Social Science questions, got {len(sst_questions)}"

# Write out JSON files
with open(os.path.join(OUT_DIR, "science_board_mock01.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": science_questions}, f, indent=2, ensure_ascii=False)

with open(os.path.join(OUT_DIR, "mathematics_board_mock01.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": math_questions}, f, indent=2, ensure_ascii=False)

with open(os.path.join(OUT_DIR, "social_science_board_mock01.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sst_questions}, f, indent=2, ensure_ascii=False)

print("✓ Successfully generated all 3 CBSE Class 10 Full 80-Mark Sample Question Papers!")
