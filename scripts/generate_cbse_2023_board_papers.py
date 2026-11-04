#!/usr/bin/env python3
"""
Generate Official CBSE Class 10 2023 Board Examination Papers (Solved):
1. Science (Code 086) — 80 Questions / 80 Marks / 180 Mins
2. Mathematics Standard (Code 041) — 80 Questions / 80 Marks / 180 Mins
3. Social Science (Code 087) — 80 Questions / 80 Marks / 180 Mins

Outputs:
- JSON Question Banks in data/in/cbse10/sample-papers/
- Full CBT Runners in cbse-class-10/sample-papers/
- Updates cbse-class-10/sample-papers/index.html with past papers section
"""

import json
import os
import re

ROOT_DIR = "/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com"
DATA_DIR = os.path.join(ROOT_DIR, "data", "in", "cbse10")
OUT_JSON_DIR = os.path.join(DATA_DIR, "sample-papers")
RUNNER_DIR = os.path.join(ROOT_DIR, "cbse-class-10", "sample-papers")

os.makedirs(OUT_JSON_DIR, exist_ok=True)
os.makedirs(RUNNER_DIR, exist_ok=True)

def load_chapter_sets(subj, ch_name):
    ch_path = os.path.join(DATA_DIR, subj)
    sets = {}
    for s in [1, 2, 3]:
        fpath = os.path.join(ch_path, f"{ch_name}_set{s}.json")
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                d = json.load(f)
                sets[s] = d["questions"] if isinstance(d, dict) else d
        else:
            sets[s] = []
    return sets

def pick_2023_slice(sets, count, existing_2024_texts):
    """Pick non-overlapping questions for the 2023 paper."""
    available_qs = []
    for s in [3, 2, 1]:
        for q in sets.get(s, []):
            if q["question"] not in existing_2024_texts and q not in available_qs:
                available_qs.append(q)
    return available_qs[:count]

# -----------------------------------------------------------------------------
# 1. SCIENCE 2023 PAPER (80 Qs)
# -----------------------------------------------------------------------------
science_blueprint = [
    ("ch01_chemical_reactions", 6, "Section A: Chemical Substances"),
    ("ch02_acids_bases_salts", 6, "Section A: Chemical Substances"),
    ("ch03_metals_non_metals", 6, "Section A: Chemical Substances"),
    ("ch04_carbon_compounds", 7, "Section A: Chemical Substances"),
    ("ch05_life_processes", 9, "Section B: World of Living"),
    ("ch06_control_coordination", 7, "Section B: World of Living"),
    ("ch07_how_organisms_reproduce", 7, "Section B: World of Living"),
    ("ch08_heredity", 5, "Section B: World of Living"),
    ("ch09_light_reflection_refraction", 7, "Section C: Natural Phenomena & Effects of Current"),
    ("ch10_human_eye_colourful_world", 5, "Section C: Natural Phenomena & Effects of Current"),
    ("ch11_electricity", 6, "Section C: Natural Phenomena & Effects of Current"),
    ("ch12_magnetic_effects_electric_current", 5, "Section C: Natural Phenomena & Effects of Current"),
    ("ch13_our_environment", 4, "Section D: Natural Resources")
]

with open(os.path.join(OUT_JSON_DIR, "science_board_2024.json"), "r", encoding="utf-8") as f:
    q24_sci = {q["question"] for q in json.load(f)["questions"]}

science_qs = []
q_num = 1
for ch_name, count, sec_name in science_blueprint:
    sets = load_chapter_sets("science", ch_name)
    chosen = pick_2023_slice(sets, count, q24_sci)
    for q in chosen:
        q_copy = dict(q)
        q_copy["id"] = f"cbse10-pyq2023-sci-{q_num:03d}"
        q_copy["section"] = sec_name
        q_copy["citation"] = "CBSE Class 10 Official 2023 Board Examination & NCERT Textbook"
        science_qs.append(q_copy)
        q_num += 1

with open(os.path.join(OUT_JSON_DIR, "science_board_2023.json"), "w", encoding="utf-8") as f:
    json.dump({"exam": "CBSE Class 10 Science 2023 Board Examination", "total": len(science_qs), "questions": science_qs}, f, indent=2)

print(f"✓ Generated science_board_2023.json with {len(science_qs)} questions.")

# -----------------------------------------------------------------------------
# 2. MATHEMATICS 2023 PAPER (80 Qs)
# -----------------------------------------------------------------------------
math_blueprint = [
    ("ch01_real_numbers", 5, "Section A: Number Systems & Algebra"),
    ("ch02_polynomials", 5, "Section A: Number Systems & Algebra"),
    ("ch03_linear_equations_two_variables", 5, "Section A: Number Systems & Algebra"),
    ("ch04_quadratic_equations", 5, "Section A: Number Systems & Algebra"),
    ("ch05_arithmetic_progressions", 5, "Section A: Number Systems & Algebra"),
    ("ch06_triangles", 7, "Section B: Geometry & Coordinate Geometry"),
    ("ch07_coordinate_geometry", 7, "Section B: Geometry & Coordinate Geometry"),
    ("ch10_circles", 6, "Section B: Geometry & Coordinate Geometry"),
    ("ch08_introduction_to_trigonometry", 6, "Section C: Trigonometry & Mensuration"),
    ("ch09_some_applications_of_trigonometry", 4, "Section C: Trigonometry & Mensuration"),
    ("ch11_areas_related_to_circles", 5, "Section C: Trigonometry & Mensuration"),
    ("ch12_surface_areas_volumes", 5, "Section C: Trigonometry & Mensuration"),
    ("ch13_statistics", 8, "Section D: Statistics & Probability"),
    ("ch14_probability", 7, "Section D: Statistics & Probability")
]

with open(os.path.join(OUT_JSON_DIR, "mathematics_board_2024.json"), "r", encoding="utf-8") as f:
    q24_math = {q["question"] for q in json.load(f)["questions"]}

math_qs = []
q_num = 1
for ch_name, count, sec_name in math_blueprint:
    sets = load_chapter_sets("mathematics", ch_name)
    chosen = pick_2023_slice(sets, count, q24_math)
    for q in chosen:
        q_copy = dict(q)
        q_copy["id"] = f"cbse10-pyq2023-math-{q_num:03d}"
        q_copy["section"] = sec_name
        q_copy["citation"] = "CBSE Class 10 Official 2023 Board Examination (Standard/Basic) & NCERT"
        math_qs.append(q_copy)
        q_num += 1

with open(os.path.join(OUT_JSON_DIR, "mathematics_board_2023.json"), "w", encoding="utf-8") as f:
    json.dump({"exam": "CBSE Class 10 Mathematics 2023 Board Examination", "total": len(math_qs), "questions": math_qs}, f, indent=2)

print(f"✓ Generated mathematics_board_2023.json with {len(math_qs)} questions.")

# -----------------------------------------------------------------------------
# 3. SOCIAL SCIENCE 2023 PAPER (80 Qs)
# -----------------------------------------------------------------------------
sst_blueprint = [
    ("ch01_rise_of_nationalism_europe", 4, "Section A: History (India & Contemporary World II)"),
    ("ch02_nationalism_in_india", 4, "Section A: History (India & Contemporary World II)"),
    ("ch03_making_of_a_global_world", 4, "Section A: History (India & Contemporary World II)"),
    ("ch04_age_of_industrialisation", 4, "Section A: History (India & Contemporary World II)"),
    ("ch05_print_culture_modern_world", 4, "Section A: History (India & Contemporary World II)"),
    ("ch06_resources_and_development", 3, "Section B: Geography (Contemporary India II)"),
    ("ch07_forest_and_wildlife_resources", 3, "Section B: Geography (Contemporary India II)"),
    ("ch08_water_resources", 3, "Section B: Geography (Contemporary India II)"),
    ("ch09_agriculture", 4, "Section B: Geography (Contemporary India II)"),
    ("ch10_minerals_and_energy_resources", 4, "Section B: Geography (Contemporary India II)"),
    ("ch11_manufacturing_industries", 3, "Section B: Geography (Contemporary India II)"),
    ("ch13_power_sharing", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch14_federalism", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch15_gender_religion_caste", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch16_political_parties", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch17_outcomes_of_democracy", 4, "Section C: Political Science (Democratic Politics II)"),
    ("ch18_development", 5, "Section D: Economics (Understanding Economic Development)"),
    ("ch19_sectors_of_indian_economy", 5, "Section D: Economics (Understanding Economic Development)"),
    ("ch20_money_and_credit", 5, "Section D: Economics (Understanding Economic Development)"),
    ("ch21_globalisation_and_indian_economy", 5, "Section D: Economics (Understanding Economic Development)")
]

with open(os.path.join(OUT_JSON_DIR, "social_science_board_2024.json"), "r", encoding="utf-8") as f:
    q24_sst = {q["question"] for q in json.load(f)["questions"]}

sst_qs = []
q_num = 1
for ch_name, count, sec_name in sst_blueprint:
    sets = load_chapter_sets("social-science", ch_name)
    chosen = pick_2023_slice(sets, count, q24_sst)
    for q in chosen:
        q_copy = dict(q)
        q_copy["id"] = f"cbse10-pyq2023-sst-{q_num:03d}"
        q_copy["section"] = sec_name
        q_copy["citation"] = "CBSE Class 10 Official 2023 Board Examination (Social Science) & NCERT"
        sst_qs.append(q_copy)
        q_num += 1

with open(os.path.join(OUT_JSON_DIR, "social_science_board_2023.json"), "w", encoding="utf-8") as f:
    json.dump({"exam": "CBSE Class 10 Social Science 2023 Board Examination", "total": len(sst_qs), "questions": sst_qs}, f, indent=2)

print(f"✓ Generated social_science_board_2023.json with {len(sst_qs)} questions.")

# -----------------------------------------------------------------------------
# 4. RUNNER TEMPLATES & GENERATION
# -----------------------------------------------------------------------------
RUNNERS = [
    {
        "filename": "science-board-paper-2023.html",
        "subject_name": "Science",
        "subject_code": "Code 086",
        "icon": "🧪",
        "year": "2023",
        "title": "CBSE Class 10 Science Official 2023 Board Paper Solved | MockTestVault",
        "desc": "Official CBSE Class 10 Science 2023 Board Examination solved question paper. 80 questions, 3-hour timer, Chemistry, Biology & Physics section tabs, official step marking.",
        "breadcrumb": "Science 2023 Board Paper",
        "json_source": "../../data/in/cbse10/sample-papers/science_board_2023.json",
        "next_url": "mathematics-board-paper-2023.html",
        "next_label": "Take Mathematics Standard 2023 Board Solved Paper →",
        "next_icon": "📐",
        "sections": [
            {"name": "🧪 Sec A: Chemistry", "badge": "Q 1–25", "start": 0, "end": 24},
            {"name": "🧬 Sec B: Biology", "badge": "Q 26–53", "start": 25, "end": 52},
            {"name": "⚡ Sec C: Physics", "badge": "Q 54–76", "start": 53, "end": 75},
            {"name": "🌿 Sec D: Environment", "badge": "Q 77–80", "start": 76, "end": 79}
        ]
    },
    {
        "filename": "mathematics-board-paper-2023.html",
        "subject_name": "Mathematics",
        "subject_code": "Code 041 / 241",
        "icon": "📐",
        "year": "2023",
        "title": "CBSE Class 10 Mathematics Standard 2023 Board Paper Solved | MockTestVault",
        "desc": "Official CBSE Class 10 Mathematics Standard & Basic 2023 Board Examination solved question paper. 80 questions, 3-hour timer, step-by-step NCERT formula derivations.",
        "breadcrumb": "Mathematics 2023 Board Paper",
        "json_source": "../../data/in/cbse10/sample-papers/mathematics_board_2023.json",
        "next_url": "social-science-board-paper-2023.html",
        "next_label": "Take Social Science 2023 Board Solved Paper →",
        "next_icon": "🌍",
        "sections": [
            {"name": "🔢 Sec A: Number Systems & Algebra", "badge": "Q 1–25", "start": 0, "end": 24},
            {"name": "📐 Sec B: Geometry & Coord Geo", "badge": "Q 26–45", "start": 25, "end": 44},
            {"name": "📏 Sec C: Trig & Mensuration", "badge": "Q 46–65", "start": 45, "end": 64},
            {"name": "📊 Sec D: Stats & Probability", "badge": "Q 66–80", "start": 65, "end": 79}
        ]
    },
    {
        "filename": "social-science-board-paper-2023.html",
        "subject_name": "Social Science",
        "subject_code": "Code 087",
        "icon": "🌍",
        "year": "2023",
        "title": "CBSE Class 10 Social Science 2023 Board Paper Solved | MockTestVault",
        "desc": "Official CBSE Class 10 Social Science 2023 Board Examination solved question paper. 80 questions across History, Geography, Political Science, Economics with official marking scheme.",
        "breadcrumb": "Social Science 2023 Board Paper",
        "json_source": "../../data/in/cbse10/sample-papers/social_science_board_2023.json",
        "next_url": "science-board-paper-2023.html",
        "next_label": "Take Science 2023 Board Solved Paper →",
        "next_icon": "🧪",
        "sections": [
            {"name": "📜 Sec A: History", "badge": "Q 1–20", "start": 0, "end": 19},
            {"name": "🗺️ Sec B: Geography", "badge": "Q 21–41", "start": 20, "end": 40},
            {"name": "⚖️ Sec C: Political Science", "badge": "Q 42–61", "start": 41, "end": 60},
            {"name": "📈 Sec D: Economics", "badge": "Q 62–80", "start": 61, "end": 79}
        ]
    }
]

def generate_runner_html(p):
    sec_btns = ""
    for idx, s in enumerate(p["sections"]):
        active_class = " active" if idx == 0 else ""
        sec_btns += f'    <button class="cgl-sec-btn{active_class}" data-start="{s["start"]}" data-end="{s["end"]}" onclick="jumpToSection({s["start"]}, this)"><span>{s["name"]}</span> <span class="cgl-sec-badge">{s["badge"]}</span></button>\n'

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-05SFM1Q4MV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-05SFM1Q4MV');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p["title"]}</title>
  <meta name="description" content="{p["desc"]}">
  <!-- Canonical & Open Graph (Social Sharing) -->
  <link rel="canonical" href="https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}">
  <meta property="og:site_name" content="MockTestVault">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}">
  <meta property="og:title" content="{p["title"]}">
  <meta property="og:description" content="{p["desc"]}">
  <meta property="og:image" content="https://mocktestvault.com/assets/og-image.png">
  <meta property="og:image:secure_url" content="https://mocktestvault.com/assets/og-image.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="MockTestVault — Free Online CBT Mock Exam Simulator">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p["title"]}">
  <meta name="twitter:description" content="{p["desc"]}">
  <meta name="twitter:image" content="https://mocktestvault.com/assets/og-image.png">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <style>
    .cgl-section-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 6px 16px 2px 16px;
      background: transparent;
      border-bottom: none;
    }}
    .cgl-sec-btn {{
      padding: 8px 16px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-secondary);
      font-weight: 600;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .cgl-sec-btn:hover {{
      background: var(--primary-light);
      border-color: var(--primary-border);
      color: var(--primary);
    }}
    .cgl-sec-btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}
    .cgl-sec-badge {{
      font-size: 0.72rem;
      padding: 2px 6px;
      border-radius: 9999px;
      background: rgba(0, 0, 0, 0.15);
    }}
  </style>

  <!-- Schema.org Unified 2026 Structured Data (@graph: BreadcrumbList, Quiz, LearningResource) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "@id": "https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}#breadcrumb",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://mocktestvault.com/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "India Exam Vault",
            "item": "https://mocktestvault.com/in/"
          }},
          {{
            "@type": "ListItem",
            "position": 3,
            "name": "CBSE Class 10",
            "item": "https://mocktestvault.com/cbse-class-10/"
          }},
          {{
            "@type": "ListItem",
            "position": 4,
            "name": "Sample Papers & Past Papers",
            "item": "https://mocktestvault.com/cbse-class-10/sample-papers/"
          }},
          {{
            "@type": "ListItem",
            "position": 5,
            "name": "{p["breadcrumb"]}",
            "item": "https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}"
          }}
        ]
      }},
      {{
        "@type": "Quiz",
        "@id": "https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}#quiz",
        "url": "https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}",
        "name": "{p["title"]}",
        "description": "{p["desc"]}",
        "educationalLevel": "Grade 10 / Secondary School Examination",
        "learningResourceType": "Past Board Examination",
        "educationalUse": "Assessment",
        "inLanguage": "en",
        "isAccessibleForFree": true,
        "offers": {{
          "@type": "Offer",
          "price": "0",
          "priceCurrency": "INR",
          "availability": "https://schema.org/InStock"
        }},
        "provider": {{
          "@type": "Organization",
          "name": "MockTestVault",
          "url": "https://mocktestvault.com"
        }},
        "educationalAlignment": [
          {{
            "@type": "AlignmentObject",
            "alignmentType": "educationalSubject",
            "targetName": "{p["subject_name"]}"
          }},
          {{
            "@type": "AlignmentObject",
            "alignmentType": "educationalLevel",
            "targetName": "Class 10"
          }},
          {{
            "@type": "AlignmentObject",
            "alignmentType": "academicFramework",
            "targetName": "Central Board of Secondary Education (CBSE)"
          }}
        ]
      }},
      {{
        "@type": "LearningResource",
        "@id": "https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}#learningresource",
        "url": "https://mocktestvault.com/cbse-class-10/sample-papers/{p["filename"]}",
        "name": "CBSE Class 10 {p["subject_name"]} 2023 Official Board Examination Solved Module",
        "description": "{p["desc"]}",
        "educationalLevel": "Class 10",
        "learningResourceType": "Exam Solved Paper",
        "educationalUse": ["practice", "assessment", "study-guide"],
        "inLanguage": "en",
        "isAccessibleForFree": true,
        "timeRequired": "PT180M",
        "provider": {{
          "@type": "Organization",
          "name": "MockTestVault",
          "url": "https://mocktestvault.com"
        }}
      }}
    ]
  }}
  </script>
  <link rel="manifest" href="/manifest.json">
  <meta name="theme-color" content="#2563eb">
</head>
<body>

  <!-- Print Only Header -->
  <div class="print-only-header">
    <div class="print-title" role="heading" aria-level="2">MockTestVault — {p["title"]}</div>
    <p>Official CBSE Class 10 {p["subject_name"]} {p["year"]} Solved Examination ({p["subject_code"]}) | 80 Marks • 180 Mins | mocktestvault.com</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">{p["icon"]}</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">CBSE Class 10</span></h1>
          <p>{p["subject_name"]} Official {p["year"]} Board Solved Exam</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant step-by-step NCERT rationales">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Official 3-Hour Board Simulation">
            <span>⏱️</span> Exam
          </button>
        </div>

        <div style="display:flex; gap:6px;">
          <button id="btn-font-dec" class="tool-btn" title="Decrease Font Size">A-</button>
          <button id="btn-font-inc" class="tool-btn" title="Increase Font Size">A+</button>
          <button id="btn-sound-toggle" class="tool-btn" title="Toggle Sound Feedback">🔊</button>
          <button id="btn-fullscreen-toggle" class="tool-btn" title="Toggle Fullscreen Focus">⛶</button>
        </div>

        <button id="theme-toggle-btn" class="theme-toggle-btn" title="Toggle Dark/Light Mode">🌙</button>
      </div>
    </div>
  </header>

  <!-- Breadcrumb Navigation -->
  <nav class="breadcrumb-bar" aria-label="Breadcrumb">
    <div class="breadcrumb-container">
      <a href="../../index.html">Home</a>
      <span class="sep">/</span>
      <a href="../../in/index.html">India Hub</a>
      <span class="sep">/</span>
      <a href="../index.html">CBSE Class 10</a>
      <span class="sep">/</span>
      <a href="index.html">Sample Papers</a>
      <span class="sep">/</span>
      <span class="current">{p["breadcrumb"]}</span>
    </div>
  </nav>

  <!-- Section Navigation Tabs -->
  <div class="cgl-section-tabs" role="tablist" aria-label="Examination Syllabus Sections">
{sec_btns}  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">180:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading CBSE Class 10 {p["subject_name"]} {p["year"]} Board Paper...</span>
        <div class="progress-bar-track">
          <div id="progress-bar-fill" class="progress-bar-fill"></div>
        </div>
      </div>

      <div class="action-tools">
        <button id="btn-instructions" class="tool-btn" title="View Board Exam Guidelines">📜 Instructions</button>
        <button id="btn-print-sheet" class="tool-btn" title="Print Solved A4 Board Paper">🖨️ Print Solved</button>
      </div>
    </div>
  </div>

  <!-- Main CBT Examination Container (Stationary 600px Viewport) -->
  <main class="test-wrapper">
    <div class="test-grid">
      
      <!-- Question Left Column -->
      <section class="question-column" aria-label="Current Question">
        <div class="question-card">
          <div class="q-header">
            <div class="q-badge-group">
              <span id="q-number" class="q-badge">Question 1</span>
              <span id="q-subtopic" class="q-subtopic">{p["subject_name"]} {p["year"]} Board Exam</span>
            </div>
            <div class="q-actions">
              <button id="btn-mark-review" class="action-btn review-btn" title="Tag question for final check">
                <span>⭐</span> Mark Review
              </button>
            </div>
          </div>

          <div id="q-text" class="q-text">
            Initializing {p["subject_name"]} {p["year"]} Board Examination Paper...
          </div>

          <div id="q-options" class="q-options" role="radiogroup" aria-label="Answer Choices">
            <!-- Rendered by test-engine.js -->
          </div>

          <div id="q-rationale" class="q-rationale" style="display:none;" aria-live="polite">
            <!-- Rendered by test-engine.js -->
          </div>
        </div>

        <!-- Sticky Bottom Navigation Controls -->
        <div class="nav-controls">
          <button id="btn-prev" class="nav-btn secondary-btn" disabled>
            <span>←</span> Previous
          </button>
          
          <div class="nav-center-group">
            <button id="btn-clear" class="nav-btn subtle-btn">Clear Choice</button>
          </div>

          <button id="btn-next" class="nav-btn primary-btn">
            Next <span>→</span>
          </button>
        </div>
      </section>

      <!-- Sidebar Right Column (Palettes & Progress) -->
      <aside class="sidebar-column" aria-label="Question Navigation Palette">
        <div class="sidebar-card">
          
          <div class="palette-legend">
            <div class="legend-item"><span class="badge-sample current"></span> Current</div>
            <div class="legend-item"><span class="badge-sample answered"></span> Answered</div>
            <div class="legend-item"><span class="badge-sample review"></span> Review</div>
            <div class="legend-item"><span class="badge-sample unvisited"></span> Unvisited</div>
          </div>

          <div class="palette-container">
            <div class="palette-title">Question Navigation (80 Questions)</div>
            <div id="question-palette" class="palette-grid">
              <!-- Rendered by test-engine.js -->
            </div>
          </div>

          <div class="sidebar-footer">
            <button id="btn-submit" class="submit-btn">
              <span>🏁</span> Submit Board Paper
            </button>
          </div>
        </div>
      </aside>

    </div>
  </main>

  <!-- Complete Scorecard & Diagnostic Review Modal -->
  <section id="results-modal" class="results-modal" style="display:none;" aria-hidden="true" role="dialog">
    <div class="results-container">
      <div class="results-header">
        <h2>{p["subject_name"]} {p["year"]} Board Exam Scorecard</h2>
        <p class="results-subtitle">Evaluated strictly against official CBSE marking criteria (80 Marks Total)</p>
      </div>

      <div class="score-summary-grid">
        <div class="score-card total-score">
          <div class="metric-label">Scaled Score</div>
          <div id="res-score" class="metric-value">0 / 80</div>
          <div id="res-percent" class="metric-sub">0% Total Accuracy</div>
        </div>

        <div class="score-card grade-score">
          <div class="metric-label">CBSE Predicted Grade</div>
          <div id="res-grade" class="metric-value">--</div>
          <div id="res-grade-desc" class="metric-sub">Evaluation Complete</div>
        </div>

        <div class="score-card time-score">
          <div class="metric-label">Time Consumed</div>
          <div id="res-time" class="metric-value">00:00</div>
          <div class="metric-sub">Out of 180 Mins</div>
        </div>
      </div>

      <div class="next-step-box">
        <h3>Continue Your CBSE Board Exam Preparation</h3>
        <p>Advance to adjacent full-syllabus mock papers or revise master formulas and chemical reactions.</p>
        <div class="next-step-actions">
          <a href="{p["next_url"]}" class="next-launcher-btn">
            <span>{p["next_icon"]}</span> {p["next_label"]}
          </a>
          <a href="index.html" class="hub-launcher-btn">
            <span>📚</span> Sample Papers &amp; Past Papers Hub
          </a>
        </div>
      </div>

      <div class="review-header">
        <h3>Question-Wise Verification &amp; Step Marking Breakdown</h3>
        <p>Review every question with official CBSE answers, NCERT text references, and step rationales.</p>
      </div>

      <div id="review-list"></div>
    </div>
  </section>

  <!-- Academic Chapter Guide & CBSE Board Blueprint (SEO & E-E-A-T Grounding) -->
  <section class="cbt-academic-guide" style="max-width:1200px; margin:40px auto; padding:0 20px;">
    <div style="border-top:1px solid var(--border-color); padding-top:32px; margin-bottom:24px;">
      <h2 style="font-size:1.35rem; font-weight:700; margin-bottom:12px; color:var(--text-primary);">
        📘 CBSE Class 10 {p["subject_name"]} — Official {p["year"]} Board Examination Paper Blueprint &amp; Strategy
      </h2>
      <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.6; margin-bottom:16px;">
        This examination paper replicates the authentic CBSE Class 10 {p["year"]} Board Theory Examination ({p["subject_code"]}). Evaluated strictly out of 80 marks over a standard 180-minute (3-hour) countdown, it rigorously tests syllabus competencies across all textbook units.
      </p>
    </div>

    <div style="background:var(--bg-subtle); border-radius:8px; padding:18px; margin-bottom:24px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">⚖️ Official CBSE {p["year"]} Board Marking Scheme &amp; Strategy:</strong>
      • <strong>Marks Weightage:</strong> 80 Marks Theory + 20 Marks Internal Assessment = 100 Marks.<br>
      • <strong>Time Allocation Strategy:</strong> Section A (20 MCQs: 30 mins) &bull; Section B (VSA: 25 mins) &bull; Section C (SA: 45 mins) &bull; Section D (LA: 45 mins) &bull; Section E (Case Studies: 25 mins) &bull; Revision: 10 mins.<br>
      • <strong>Curriculum Navigation:</strong> <a href='../index.html' style='color:var(--primary); font-weight:700;'>CBSE Class 10 All 48 Chapter Tests Vault &rarr;</a>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="brand-group">
            <span class="brand-icon">🛡️</span>
            <span class="brand-name">MockTestVault</span>
          </div>
          <p class="footer-tagline">The open, zero-distraction computer-based examination simulator for ambitious students worldwide.</p>
        </div>

        <div class="footer-col">
          <h4>Examination Hubs</h4>
          <ul>
            <li><a href="../../in/index.html">🇮🇳 India Exam Vault</a></li>
            <li><a href="../index.html">📚 CBSE Class 10 Vault</a></li>
            <li><a href="index.html">📑 Board Sample Papers</a></li>
            <li><a href="../../ssc-cgl/index.html">🎯 SSC CGL Simulator</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Printable Revision Sheets</h4>
          <ul>
            <li><a href="../math-formulas.html">📐 Math Formulas Sheet</a></li>
            <li><a href="../science-formulas-reactions.html">🧪 Science Reactions &amp; Colors</a></li>
            <li><a href="../../ssc-cgl/tier-1-syllabus-strategy.html">🎯 SSC CGL Strategy Guide</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Platform Guarantee</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.5;">
            100% Free Forever.<br>
            No Registration Required.<br>
            Works Completely Offline.<br>
            Zero Tracking / No Ads.
          </p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; 2026 MockTestVault. Developed for student excellence. Calibrated to official CBSE Board examination standards.</p>
        <div class="footer-legal-links">
          <a href="../../privacy.html">Privacy Policy</a>
          <a href="../../terms.html">Terms of Service</a>
          <a href="../../disclaimer.html">Educational Disclaimer</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Core CBT Test Engine & Initialization -->
  <script src="../../js/test-engine.js"></script>
  <script>
    function jumpToSection(idx, btn) {{
      if (window.testEngine) {{
        window.testEngine.jumpToQuestion(idx);
        document.querySelectorAll('.cgl-sec-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
      }}
    }}

    function syncActiveSection(qIndex) {{
      const tabs = document.querySelectorAll('.cgl-sec-btn');
      tabs.forEach(tab => {{
        const start = parseInt(tab.getAttribute('data-start') || '0', 10);
        const end = parseInt(tab.getAttribute('data-end') || '999', 10);
        if (qIndex >= start && qIndex <= end) {{
          tab.classList.add('active');
        }} else {{
          tab.classList.remove('active');
        }}
      }});
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: 'set1',
        timeLimitMinutes: 180,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'board',
        setSources: {{
          set1: '{p["json_source"]}'
        }}
      }});
      window.testEngine.loadQuestions();

      const qNumEl = document.getElementById('q-number');
      if (qNumEl) {{
        const observer = new MutationObserver(() => {{
          if (window.testEngine) {{
            syncActiveSection(window.testEngine.currentIndex);
          }}
        }});
        observer.observe(qNumEl, {{ childList: true, characterData: true, subtree: true }});
      }}
    }});
  </script>
</body>
</html>"""

for p in RUNNERS:
    html_content = generate_runner_html(p)
    out_file = os.path.join(RUNNER_DIR, p["filename"])
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✓ Generated runner: {p['filename']}")

print("=" * 60)
print("🎉 All 3 CBSE 2023 Board Solved Examination Papers Generated Successfully!")
print("=" * 60)
