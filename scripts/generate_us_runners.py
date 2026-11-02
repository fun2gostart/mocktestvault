#!/usr/bin/env python3
"""
Generates and updates all 24 US examination runner HTML pages (100 Questions per exam across 5 sets + 1 Random Mock runner):
- SAT Math Practice 01, 02, 03, 04, 05 + Random 20-Q Mock (100 Qs Pool)
- SAT Reading & Writing Practice 01, 02, 03, 04, 05 + Random 20-Q Mock (100 Qs Pool)
- AP Calculus AB Diagnostic 01, 02, 03, 04, 05 + Random 20-Q Mock (100 Qs Pool)
- AP Physics 1 Diagnostic 01, 02, 03, 04, 05 + Random 20-Q Mock (100 Qs Pool)

Total: 400 Questions across 24 Production Routes.
Uses the unified, battle-tested CBT test engine architecture.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_SAT_DIR = os.path.join(BASE_DIR, "us", "sat")
US_AP_DIR = os.path.join(BASE_DIR, "us", "ap")

os.makedirs(US_SAT_DIR, exist_ok=True)
os.makedirs(US_AP_DIR, exist_ok=True)

# ----------------------------------------------------------------------
# SAT Math Runners (5 Sets + 1 Random Mock Runner = 100 Questions Bank)
# ----------------------------------------------------------------------
SAT_MATH_RUNNERS = [
  {
    "filename": "math-practice-01.html",
    "set_key": "01",
    "title": "Digital SAT® Math Practice Test 01 (Core Diagnostic) | MockTestVault US",
    "desc": "Free official-style Digital SAT Math Practice Test 01 with instant step-by-step solutions, Algebra, Advanced Math, Geometry, Desmos formulas, and adaptive module timing.",
    "h1": "Digital SAT® Math Module 01",
    "print_title": "Digital SAT® Math Practice Test 01",
    "print_sub": "College Board Specification: Algebra, Advanced Math, Problem Solving, Geometry & Trigonometry | mocktestvault.com",
    "quiz_name": "Digital SAT® Math Module 01 Practice Test (Core Diagnostic)",
    "time_mins": 32,
    "next_url": "math-practice-02.html",
    "next_text": "<span>📊</span> Take Math Module 02 (Algebra & Functions) →",
    "score_label": "Est. SAT Math Section"
  },
  {
    "filename": "math-practice-02.html",
    "set_key": "02",
    "title": "Digital SAT® Math Practice Test 02 (Algebra & Functions) | MockTestVault US",
    "desc": "Free official-style Digital SAT Math Practice Test 02 focusing on Linear Equations, Systems, Inequalities, and Functional Modeling with College Board rationales.",
    "h1": "Digital SAT® Math Module 02",
    "print_title": "Digital SAT® Math Practice Test 02",
    "print_sub": "College Board Specification: Linear Equations, Systems, Inequalities, and Functional Modeling | mocktestvault.com",
    "quiz_name": "Digital SAT® Math Module 02 Practice Test (Algebra & Functions)",
    "time_mins": 32,
    "next_url": "math-practice-03.html",
    "next_text": "<span>📐</span> Take Math Module 03 (Advanced Math & Geom) →",
    "score_label": "Est. SAT Math Section"
  },
  {
    "filename": "math-practice-03.html",
    "set_key": "03",
    "title": "Digital SAT® Math Practice Test 03 (Advanced Math & Geometry) | MockTestVault US",
    "desc": "Free official-style Digital SAT Math Practice Test 03 targeting Quadratics, Higher-Degree Polynomials, Exponential Growth, Circles, and Right-Triangle Trigonometry.",
    "h1": "Digital SAT® Math Module 03",
    "print_title": "Digital SAT® Math Practice Test 03",
    "print_sub": "College Board Specification: Quadratics, Polynomials, Exponential Functions, and Trigonometry | mocktestvault.com",
    "quiz_name": "Digital SAT® Math Module 03 Practice Test (Advanced Math & Geometry)",
    "time_mins": 32,
    "next_url": "math-practice-04.html",
    "next_text": "<span>🎯</span> Take Math Module 04 (700-800 Benchmark) →",
    "score_label": "Est. SAT Math Section"
  },
  {
    "filename": "math-practice-04.html",
    "set_key": "04",
    "title": "Digital SAT® Math Practice Test 04 (700-800 Benchmark) | MockTestVault US",
    "desc": "Master high-difficulty 700-800 benchmark Digital SAT Math problems: multi-step algebraic modeling, circle-line intersections, trigonometry, and data distributions.",
    "h1": "Digital SAT® Math Module 04",
    "print_title": "Digital SAT® Math Practice Test 04",
    "print_sub": "College Board Specification: Hard Module 2 Adaptive Simulator (700-800 Score Benchmark) | mocktestvault.com",
    "quiz_name": "Digital SAT® Math Module 04 Practice Test (700-800 Score Benchmark)",
    "time_mins": 32,
    "next_url": "math-practice-05.html",
    "next_text": "<span>🏆</span> Take Math Module 05 (1600 Master Suite) →",
    "score_label": "Est. SAT Math Section"
  },
  {
    "filename": "math-practice-05.html",
    "set_key": "05",
    "title": "Digital SAT® Math Practice Test 05 (1600 Master Suite) | MockTestVault US",
    "desc": "The ultimate 1600 benchmark Digital SAT Math practice test: comprehensive Heart of Algebra, Problem Solving & Data Analysis, Passport to Advanced Math, and Geometry.",
    "h1": "Digital SAT® Math Module 05",
    "print_title": "Digital SAT® Math Practice Test 05",
    "print_sub": "College Board Specification: 1600 Benchmark Master Suite across all 4 Math Domains | mocktestvault.com",
    "quiz_name": "Digital SAT® Math Module 05 Practice Test (1600 Master Suite)",
    "time_mins": 32,
    "next_url": "math-practice-random.html",
    "next_text": "<span>🎲</span> Take Random 20-Q Mock Test →",
    "score_label": "Est. SAT Math Section"
  },
  {
    "filename": "math-practice-random.html",
    "set_key": "random",
    "title": "Digital SAT® Math Random Mock Exam (100-Question Dynamic Bank) | MockTestVault US",
    "desc": "Take a freshly randomized 20-question official-style Digital SAT Math mock exam drawn dynamically from our 100-question College Board aligned question vault.",
    "h1": "Digital SAT® Math Random 20-Q Mock",
    "print_title": "Digital SAT® Math Random Mock Exam",
    "print_sub": "College Board Specification: Dynamic 20-Question Shuffled Pool across all 4 Math Domains | mocktestvault.com",
    "quiz_name": "Digital SAT® Math Random Mock Exam (Dynamic 20-Question Shuffled Pool)",
    "time_mins": 32,
    "next_url": "math-practice-random.html",
    "next_text": "<span>🎲</span> Retake Fresh Random 20 Questions →",
    "score_label": "Est. SAT Math Section"
  }
]

# ----------------------------------------------------------------------
# SAT Reading & Writing Runners (5 Sets + 1 Random Mock Runner = 100 Questions Bank)
# ----------------------------------------------------------------------
SAT_READING_RUNNERS = [
  {
    "filename": "reading-practice-01.html",
    "set_key": "01",
    "title": "Digital SAT® Reading & Writing Practice Test 01 (Core Diagnostic) | MockTestVault US",
    "desc": "Free official Digital SAT Reading & Writing Diagnostic with passage questions, Craft & Structure, Information & Ideas, and Standard English Conventions.",
    "h1": "Digital SAT® Reading & Writing Module 01",
    "print_title": "Digital SAT® Reading & Writing Practice Test 01",
    "print_sub": "College Board Specification: Craft & Structure, Information & Ideas, Standard English Conventions | mocktestvault.com",
    "quiz_name": "Digital SAT® Reading & Writing Practice Test 01 (Core Diagnostic)",
    "time_mins": 32,
    "next_url": "reading-practice-02.html",
    "next_text": "<span>🔍</span> Take Reading Module 02 (Craft & Structure) →",
    "score_label": "Est. SAT RW Section"
  },
  {
    "filename": "reading-practice-02.html",
    "set_key": "02",
    "title": "Digital SAT® Reading & Writing Practice Test 02 (Craft & Structure) | MockTestVault US",
    "desc": "Target Words in Context, Text Structure, Author's Purpose, and Cross-Text Paired Passage Connections for Digital SAT Reading & Writing.",
    "h1": "Digital SAT® Reading & Writing Module 02",
    "print_title": "Digital SAT® Reading & Writing Practice Test 02",
    "print_sub": "College Board Specification: Craft & Structure, Vocabulary in Context, and Paired Texts | mocktestvault.com",
    "quiz_name": "Digital SAT® Reading & Writing Practice Test 02 (Craft & Structure)",
    "time_mins": 32,
    "next_url": "reading-practice-03.html",
    "next_text": "<span>📊</span> Take Reading Module 03 (Information & Ideas) →",
    "score_label": "Est. SAT RW Section"
  },
  {
    "filename": "reading-practice-03.html",
    "set_key": "03",
    "title": "Digital SAT® Reading & Writing Practice Test 03 (Information & Ideas) | MockTestVault US",
    "desc": "Practice Central Ideas, Textual Evidence, Quantitative Data Tables, and Logical Inferences for College Board Digital SAT Reading & Writing.",
    "h1": "Digital SAT® Reading & Writing Module 03",
    "print_title": "Digital SAT® Reading & Writing Practice Test 03",
    "print_sub": "College Board Specification: Central Ideas, Scientific/Historical Evidence, and Inferences | mocktestvault.com",
    "quiz_name": "Digital SAT® Reading & Writing Practice Test 03 (Information & Ideas)",
    "time_mins": 32,
    "next_url": "reading-practice-04.html",
    "next_text": "<span>✍️</span> Take Reading Module 04 (Advanced Conventions) →",
    "score_label": "Est. SAT RW Section"
  },
  {
    "filename": "reading-practice-04.html",
    "set_key": "04",
    "title": "Digital SAT® Reading & Writing Practice Test 04 (Advanced Conventions) | MockTestVault US",
    "desc": "Master Sentence Boundaries, Subject-Verb Agreement, Verb Tense, Modifier Placement, and Rhetorical Transitions for Digital SAT Reading & Writing.",
    "h1": "Digital SAT® Reading & Writing Module 04",
    "print_title": "Digital SAT® Reading & Writing Practice Test 04",
    "print_sub": "College Board Specification: Standard English Conventions, Boundaries, and Transitions | mocktestvault.com",
    "quiz_name": "Digital SAT® Reading & Writing Practice Test 04 (Advanced Conventions)",
    "time_mins": 32,
    "next_url": "reading-practice-05.html",
    "next_text": "<span>🎯</span> Take Reading Module 05 (High-Percentile Mastery) →",
    "score_label": "Est. SAT RW Section"
  },
  {
    "filename": "reading-practice-05.html",
    "set_key": "05",
    "title": "Digital SAT® Reading & Writing Practice Test 05 (Mastery Suite) | MockTestVault US",
    "desc": "High-percentile Digital SAT Reading & Writing practice test with dual passages, scientific data analysis, complex grammar, and rhetorical synthesis.",
    "h1": "Digital SAT® Reading & Writing Module 05",
    "print_title": "Digital SAT® Reading & Writing Practice Test 05",
    "print_sub": "College Board Specification: High-Percentile Comprehensive Mastery across all RW domains | mocktestvault.com",
    "quiz_name": "Digital SAT® Reading & Writing Practice Test 05 (Mastery Suite)",
    "time_mins": 32,
    "next_url": "reading-practice-random.html",
    "next_text": "<span>🎲</span> Take Random 20-Q Mock Test →",
    "score_label": "Est. SAT RW Section"
  },
  {
    "filename": "reading-practice-random.html",
    "set_key": "random",
    "title": "Digital SAT® Reading & Writing Random Mock Exam (100-Question Dynamic Bank) | MockTestVault US",
    "desc": "Take a freshly randomized 20-question Digital SAT Reading & Writing mock exam drawn dynamically from our 100-question College Board aligned question vault.",
    "h1": "Digital SAT® Reading & Writing Random 20-Q Mock",
    "print_title": "Digital SAT® Reading & Writing Random Mock Exam",
    "print_sub": "College Board Specification: Dynamic 20-Question Shuffled Pool across all RW domains | mocktestvault.com",
    "quiz_name": "Digital SAT® Reading & Writing Random Mock Exam (Dynamic 20-Question Shuffled Pool)",
    "time_mins": 32,
    "next_url": "reading-practice-random.html",
    "next_text": "<span>🎲</span> Retake Fresh Random 20 Questions →",
    "score_label": "Est. SAT RW Section"
  }
]

# ----------------------------------------------------------------------
# AP Calculus AB Runners (5 Sets + 1 Random Mock Runner = 100 Questions Bank)
# ----------------------------------------------------------------------
AP_CALC_RUNNERS = [
  {
    "filename": "calculus-ab-diagnostic-01.html",
    "set_key": "01",
    "title": "AP® Calculus AB Section I Diagnostic 01 (Limits & Fundamentals) | MockTestVault US",
    "desc": "Free timed AP Calculus AB diagnostic test 01 (20 Multiple Choice Questions) covering Limits, Continuity, Differentiation Rules, FTC, and Integration by Substitution.",
    "h1": "AP® Calculus AB Set 01 (Diagnostic)",
    "print_title": "AP® Calculus AB Practice Diagnostic 01",
    "print_sub": "Official College Board AP® CED Specification: Limits, Derivatives, Integration, and Differential Equations | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Section I Diagnostic 01",
    "time_mins": 45,
    "next_url": "calculus-ab-diagnostic-02.html",
    "next_text": "<span>📐</span> Take AP Calculus Set 02 (Derivatives & Differentiability) →"
  },
  {
    "filename": "calculus-ab-diagnostic-02.html",
    "set_key": "02",
    "title": "AP® Calculus AB Set 02 (Derivatives & Differentiability) | MockTestVault US",
    "desc": "Practice 20 official-style AP Calculus AB questions on Product, Quotient, Chain Rule, Implicit Differentiation, and Inverse Function Derivatives.",
    "h1": "AP® Calculus AB Set 02 (Derivatives)",
    "print_title": "AP® Calculus AB Practice Test 02",
    "print_sub": "Official College Board AP® CED Specification: Differentiation and Differentiability Rules | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Set 02 (Derivatives & Differentiability)",
    "time_mins": 45,
    "next_url": "calculus-ab-diagnostic-03.html",
    "next_text": "<span>📈</span> Take AP Calculus Set 03 (Applications of Derivatives) →"
  },
  {
    "filename": "calculus-ab-diagnostic-03.html",
    "set_key": "03",
    "title": "AP® Calculus AB Set 03 (Applications of Derivatives) | MockTestVault US",
    "desc": "Practice 20 AP Calculus AB questions on Related Rates, Mean Value Theorem, First & Second Derivative Tests, Concavity, Inflection Points, and Optimization.",
    "h1": "AP® Calculus AB Set 03 (Applications)",
    "print_title": "AP® Calculus AB Practice Test 03",
    "print_sub": "Official College Board AP® CED Specification: Analytical and Contextual Applications of Derivatives | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Set 03 (Applications of Derivatives)",
    "time_mins": 45,
    "next_url": "calculus-ab-diagnostic-04.html",
    "next_text": "<span>∫</span> Take AP Calculus Set 04 (Integration & Accumulation) →"
  },
  {
    "filename": "calculus-ab-diagnostic-04.html",
    "set_key": "04",
    "title": "AP® Calculus AB Set 04 (Integration & Accumulation) | MockTestVault US",
    "desc": "Practice 20 AP Calculus AB questions on Riemann Sums, Trapezoidal Rule, FTC Parts 1 & 2, U-Substitution, and Average Value of a Function.",
    "h1": "AP® Calculus AB Set 04 (Integration)",
    "print_title": "AP® Calculus AB Practice Test 04",
    "print_sub": "Official College Board AP® CED Specification: Integration and Accumulation of Change | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Set 04 (Integration & Accumulation)",
    "time_mins": 45,
    "next_url": "calculus-ab-diagnostic-05.html",
    "next_text": "<span>🔄</span> Take AP Calculus Set 05 (Diff Eq & Volumes) →"
  },
  {
    "filename": "calculus-ab-diagnostic-05.html",
    "set_key": "05",
    "title": "AP® Calculus AB Set 05 (Differential Equations & Volumes) | MockTestVault US",
    "desc": "Master 20 AP Calculus AB questions on Slope Fields, Separation of Variables, Area Between Curves, and Volumes by Disk, Washer, and Cross-Sections.",
    "h1": "AP® Calculus AB Set 05 (Diff Eq & Volumes)",
    "print_title": "AP® Calculus AB Practice Test 05",
    "print_sub": "Official College Board AP® CED Specification: Differential Equations and Applications of Integration | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Set 05 (Differential Equations & Volumes)",
    "time_mins": 45,
    "next_url": "calculus-ab-diagnostic-random.html",
    "next_text": "<span>🎲</span> Take Random 20-Q Mock Exam →"
  },
  {
    "filename": "calculus-ab-diagnostic-random.html",
    "set_key": "random",
    "title": "AP® Calculus AB Section I Random Mock Exam (100-Question Dynamic Bank) | MockTestVault US",
    "desc": "Free timed AP Calculus AB 20-question random mock exam drawn dynamically from all 5 official CED units in our 100-question diagnostic vault.",
    "h1": "AP® Calculus AB Random 20-Q Mock",
    "print_title": "AP® Calculus AB Random Mock Exam",
    "print_sub": "Official College Board AP® CED Specification: Dynamic 20-Question Shuffled Pool across all 5 CED Units | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Section I Random Mock Exam (Dynamic 20-Question Shuffled Pool)",
    "time_mins": 45,
    "next_url": "calculus-ab-diagnostic-random.html",
    "next_text": "<span>🎲</span> Retake Fresh Random 20 Questions →"
  }
]

# ----------------------------------------------------------------------
# AP Physics 1 Runners (5 Sets + 1 Random Mock Runner = 100 Questions Bank)
# ----------------------------------------------------------------------
AP_PHYSICS_RUNNERS = [
  {
    "filename": "physics-1-diagnostic-01.html",
    "set_key": "01",
    "title": "AP® Physics 1 Diagnostic 01 (Kinematics & Core Physics) | MockTestVault US",
    "desc": "Free timed AP Physics 1 diagnostic test (20 Multiple Choice Questions) covering Kinematics, Newton's Laws, Work & Energy, Momentum, Torque, and SHM.",
    "h1": "AP® Physics 1 Set 01 (Diagnostic)",
    "print_title": "AP® Physics 1: Algebra-Based Diagnostic Test 01",
    "print_sub": "Official College Board AP® CED Specification: Kinematics, Dynamics, Energy, Momentum, and Rotation | mocktestvault.com",
    "quiz_name": "AP® Physics 1: Algebra-Based Section I Diagnostic Test 01",
    "time_mins": 40,
    "next_url": "physics-1-diagnostic-02.html",
    "next_text": "<span>🧲</span> Take AP Physics Set 02 (Dynamics & Newton's Laws) →"
  },
  {
    "filename": "physics-1-diagnostic-02.html",
    "set_key": "02",
    "title": "AP® Physics 1 Set 02 (Dynamics & Newton's Laws of Motion) | MockTestVault US",
    "desc": "Practice 20 official AP Physics 1 questions on Free-Body Diagrams, Static & Kinetic Friction, Inclines, Atwood Machines, and Apparent Weight.",
    "h1": "AP® Physics 1 Set 02 (Dynamics)",
    "print_title": "AP® Physics 1 Practice Test 02",
    "print_sub": "Official College Board AP® CED Specification: Dynamics and Newton's Laws of Motion | mocktestvault.com",
    "quiz_name": "AP® Physics 1 Set 02 (Dynamics & Newton's Laws)",
    "time_mins": 40,
    "next_url": "physics-1-diagnostic-03.html",
    "next_text": "<span>🔄</span> Take AP Physics Set 03 (Circular Motion & Energy) →"
  },
  {
    "filename": "physics-1-diagnostic-03.html",
    "set_key": "03",
    "title": "AP® Physics 1 Set 03 (Circular Motion, Gravitation & Energy) | MockTestVault US",
    "desc": "Practice 20 AP Physics 1 questions on Centripetal Force, Universal Gravitation, Orbits, Work-Energy Theorem, and Mechanical Power.",
    "h1": "AP® Physics 1 Set 03 (Circular Motion & Energy)",
    "print_title": "AP® Physics 1 Practice Test 03",
    "print_sub": "Official College Board AP® CED Specification: Circular Motion, Gravitation, and Work-Energy | mocktestvault.com",
    "quiz_name": "AP® Physics 1 Set 03 (Circular Motion, Gravitation & Energy)",
    "time_mins": 40,
    "next_url": "physics-1-diagnostic-04.html",
    "next_text": "<span>💥</span> Take AP Physics Set 04 (Momentum & Collisions) →"
  },
  {
    "filename": "physics-1-diagnostic-04.html",
    "set_key": "04",
    "title": "AP® Physics 1 Set 04 (Momentum, Impulse & Collisions) | MockTestVault US",
    "desc": "Practice 20 AP Physics 1 questions on Impulse-Momentum Theorem, 1D & 2D Elastic and Inelastic Collisions, and Center of Mass Velocity.",
    "h1": "AP® Physics 1 Set 04 (Momentum & Collisions)",
    "print_title": "AP® Physics 1 Practice Test 04",
    "print_sub": "Official College Board AP® CED Specification: Linear Momentum, Impulse, and Collisions | mocktestvault.com",
    "quiz_name": "AP® Physics 1 Set 04 (Momentum & Collisions)",
    "time_mins": 40,
    "next_url": "physics-1-diagnostic-05.html",
    "next_text": "<span>🌀</span> Take AP Physics Set 05 (SHM & Rotational Dynamics) →"
  },
  {
    "filename": "physics-1-diagnostic-05.html",
    "set_key": "05",
    "title": "AP® Physics 1 Set 05 (SHM & Rotational Dynamics) | MockTestVault US",
    "desc": "Master 20 AP Physics 1 questions on Mass-Spring Oscillators, Simple Pendulums, Torque, Static Equilibrium, Rolling Without Slipping, and Angular Momentum.",
    "h1": "AP® Physics 1 Set 05 (SHM & Rotation)",
    "print_title": "AP® Physics 1 Practice Test 05",
    "print_sub": "Official College Board AP® CED Specification: Simple Harmonic Motion and Rotational Dynamics | mocktestvault.com",
    "quiz_name": "AP® Physics 1 Set 05 (SHM & Rotational Dynamics)",
    "time_mins": 40,
    "next_url": "physics-1-diagnostic-random.html",
    "next_text": "<span>🎲</span> Take Random 20-Q Mock Exam →"
  },
  {
    "filename": "physics-1-diagnostic-random.html",
    "set_key": "random",
    "title": "AP® Physics 1 Section I Random Mock Exam (100-Question Dynamic Bank) | MockTestVault US",
    "desc": "Free timed AP Physics 1 20-question random mock exam drawn dynamically from all CED units (Kinematics to Rotation) in our 100-question bank.",
    "h1": "AP® Physics 1 Random 20-Q Mock",
    "print_title": "AP® Physics 1 Random Mock Exam",
    "print_sub": "Official College Board AP® CED Specification: Dynamic 20-Question Shuffled Pool across all CED Units | mocktestvault.com",
    "quiz_name": "AP® Physics 1 Section I Random Mock Exam (Dynamic 20-Question Shuffled Pool)",
    "time_mins": 40,
    "next_url": "physics-1-diagnostic-random.html",
    "next_text": "<span>🎲</span> Retake Fresh Random 20 Questions →"
  }
]

def generate_sat_template(runner, category="math"):
    is_math = (category == "math")
    track_title = "Digital SAT® Math" if is_math else "Digital SAT® Reading & Writing"
    
    modules_math = [
      ("math-practice-01.html", "📐 Set 01 (Diagnostic)", "20 Qs • 32M", False),
      ("math-practice-02.html", "📊 Set 02 (Algebra)", "20 Qs • 32M", False),
      ("math-practice-03.html", "📐 Set 03 (Adv Math)", "20 Qs • 32M", False),
      ("math-practice-04.html", "🎯 Set 04 (700-800)", "20 Qs • 32M", False),
      ("math-practice-05.html", "🏆 Set 05 (1600 Master)", "20 Qs • 32M", False),
      ("math-practice-random.html", "🎲 Random 20-Q Mock", "Shuffled", True)
    ]
    
    modules_reading = [
      ("reading-practice-01.html", "📖 Set 01 (Diagnostic)", "20 Qs • 32M", False),
      ("reading-practice-02.html", "🔍 Set 02 (Craft/Struct)", "20 Qs • 32M", False),
      ("reading-practice-03.html", "📊 Set 03 (Info/Ideas)", "20 Qs • 32M", False),
      ("reading-practice-04.html", "✍️ Set 04 (Conventions)", "20 Qs • 32M", False),
      ("reading-practice-05.html", "🎯 Set 05 (Mastery)", "20 Qs • 32M", False),
      ("reading-practice-random.html", "🎲 Random 20-Q Mock", "Shuffled", True)
    ]
    
    modules = modules_math if is_math else modules_reading
    
    switcher_btns = []
    for fn, label, meta, is_random in modules:
        active_cls = " active" if fn == runner["filename"] else ""
        aria_sel = "true" if fn == runner["filename"] else "false"
        rand_cls = " random-btn" if is_random else ""
        data_set_attr = ' data-set="random"' if is_random else ''
        switcher_btns.append(f"""        <a href="{fn}" class="set-btn{rand_cls}{active_cls}" role="tab" aria-selected="{aria_sel}"{data_set_attr}>
          <span>{label}</span>
          <span class="set-badge-count">{meta}</span>
        </a>""")
    switcher_html = "\n".join(switcher_btns)

    initial_set = "random" if runner["set_key"] == "random" else f"set{int(runner['set_key'])}"
    prefix = "digital_sat_math" if is_math else "digital_sat_reading"

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{runner['title']}</title>
  <meta name="description" content="{runner['desc']}">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{runner['quiz_name']}",
    "description": "{runner['desc']}",
    "educationalLevel": "High School Grade 11-12",
    "learningResourceType": "Practice Quiz",
    "provider": {{
      "@type": "Organization",
      "name": "MockTestVault",
      "url": "https://mocktestvault.com"
    }}
  }}
  </script>
</head>
<body>

  <!-- Print Only Header -->
  <div class="print-only-header">
    <h1>MockTestVault US — {runner['print_title']}</h1>
    <p>{runner['print_sub']}</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">🇺🇸</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">Digital SAT®</span></h1>
          <p>US College Admissions Exam Simulator</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant answers and step-by-step College Board rationales">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Timed 32-min official Digital SAT simulation">
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
      <a href="../index.html">US Exam Vault</a>
      <span class="sep">/</span>
      <span class="current">{runner['h1']}</span>
    </div>
  </nav>

  <!-- Section Info Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">{track_title} Modules (100 Qs Pool):</span>
      <div class="set-btn-group" role="tablist">
{switcher_html}
      </div>
    </div>
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">{runner['time_mins']}:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading College Board questions...</span>
        <div class="progress-bar-track">
          <div id="progress-bar-fill" class="progress-bar-fill"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Split Layout -->
  <main class="test-layout" id="test-layout">
    
    <!-- Question Card -->
    <section class="question-card" id="question-card" aria-label="Active Test Question">
      <div class="meta-badges-row" id="q-badges">
        <span class="badge badge-chapter">{track_title}</span>
        <span class="badge badge-subtopic" id="q-subtopic-badge">Core Unit</span>
        <span class="badge badge-subtopic" id="q-diff-badge">Medium</span>
      </div>

      <div class="question-text-box">
        <div class="question-number" id="q-number">Question 1 of 20</div>
        <div class="question-title" id="q-title">Loading question...</div>
      </div>

      <!-- Interactive Options -->
      <div class="options-list" id="options-list" role="radiogroup" aria-label="Answer Options"></div>

      <!-- Explanation Box -->
      <div class="explanation-box" id="explanation-box" style="display:none;">
        <div class="explanation-header">
          <span>💡 College Board Answer Rationale & Formula Method</span>
          <span class="citation-tag" id="citation-tag">College Board Specification</span>
        </div>
        <p class="explanation-text" id="explanation-text"></p>
      </div>

      <!-- Action Buttons Row -->
      <div class="card-action-bar">
        <button id="btn-prev" class="nav-btn" disabled>
          <span>⬅️</span> Previous
        </button>

        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <button id="btn-review" class="nav-btn btn-review" title="Flag question to review later">
            <span>🚩</span> Mark for Review
          </button>
          <button id="btn-clear" class="nav-btn" title="Clear chosen answer option">
            <span>🧹</span> Clear Choice
          </button>
        </div>

        <div style="display:flex; gap:10px;">
          <button id="btn-next" class="nav-btn btn-primary">
            Next <span>➡️</span>
          </button>
          <button id="btn-submit" class="nav-btn btn-submit-test">
            Submit Test <span>🏁</span>
          </button>
        </div>
      </div>
    </section>

    <!-- CBT Question Palette -->
    <aside class="palette-card" aria-label="Question Navigation Grid">
      <div class="palette-title">
        <span>Question Palette</span>
        <span id="palette-summary" style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">0 / 20 Answered</span>
      </div>

      <div class="palette-grid" id="palette-grid">
        <!-- 1 to 20 dynamically populated -->
      </div>

      <div class="palette-legend">
        <div class="legend-item">
          <div class="legend-dot dot-answered"></div>
          <span>Answered (<strong id="count-answered">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-not-answered"></div>
          <span>Not Answered (<strong id="count-not-answered">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-reviewed"></div>
          <span>Marked Review (<strong id="count-reviewed">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-unvisited"></div>
          <span>Not Visited (<strong id="count-unvisited">20</strong>)</span>
        </div>
      </div>

      <div style="margin-top:18px;">
        <button id="btn-open-submit" class="nav-btn btn-submit-test" style="width:100%; justify-content:center;">
          <span>🏁</span> Submit Test & Scorecard
        </button>
      </div>
    </aside>

  </main>

  <!-- Scorecard View -->
  <section class="scorecard-view" id="scorecard-view" style="max-width:960px; margin:24px auto; padding:32px 24px;">
    <div class="score-hero" id="score-hero"></div>
    <div class="stats-grid" id="stats-grid"></div>

    <div class="scorecard-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin:24px 0;">
      <button id="btn-retake" class="nav-btn btn-primary">
        <span>🔄</span> Retake Test
      </button>
      <button id="btn-print" class="nav-btn">
        <span>🖨️</span> Print / PDF Sheet
      </button>
      <a href="{runner['next_url']}" class="nav-btn" style="text-decoration:none; background:var(--primary); color:#fff;">
        {runner['next_text']}
      </a>
    </div>

    <div id="mastery-container"></div>

    <div class="review-filter-bar" style="margin-top:28px;">
      <div class="filter-pills" role="tablist" style="display:flex; gap:8px; flex-wrap:wrap;">
        <button class="filter-pill active" data-filter="all" id="filter-all">All (<span id="filter-count-all">20</span>)</button>
        <button class="filter-pill filter-wrong" data-filter="wrong" id="filter-wrong">❌ Mistakes (<span id="filter-count-wrong">0</span>)</button>
        <button class="filter-pill filter-reviewed" data-filter="reviewed" id="filter-reviewed">🟣 Review (<span id="filter-count-reviewed">0</span>)</button>
        <button class="filter-pill filter-correct" data-filter="correct" id="filter-correct">✓ Correct (<span id="filter-count-correct">0</span>)</button>
      </div>
    </div>

    <div id="review-list"></div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <p><strong>MockTestVault.com</strong> — 100% Free Educational Practice & Standardized Exam Simulators.</p>
      <p style="font-size:0.75rem;">Distraction-Free Computer-Based Testing. Aligned with official College Board Digital SAT® standards. SAT® is a registered trademark of the College Board, which is not affiliated with this website.</p>
    </div>
  </footer>

  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: '{initial_set}',
        timeLimitMinutes: {runner['time_mins']},
        randomSampleSize: 20,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'sat',
        setSources: {{
          set1: '../../data/us/sat/{prefix}_set1.json',
          set2: '../../data/us/sat/{prefix}_set2.json',
          set3: '../../data/us/sat/{prefix}_set3.json',
          set4: '../../data/us/sat/{prefix}_set4.json',
          set5: '../../data/us/sat/{prefix}_set5.json'
        }}
      }});
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>"""
    return html

def generate_ap_template(runner, exam_type="calc"):
    is_calc = (exam_type == "calc")
    course_name = "AP® Calculus AB" if is_calc else "AP® Physics 1"
    
    tabs_calc = [
      ("calculus-ab-diagnostic-01.html", "Set 01 (Limits/Diag)", "20 Qs", False),
      ("calculus-ab-diagnostic-02.html", "Set 02 (Derivatives)", "20 Qs", False),
      ("calculus-ab-diagnostic-03.html", "Set 03 (Applications)", "20 Qs", False),
      ("calculus-ab-diagnostic-04.html", "Set 04 (Integration)", "20 Qs", False),
      ("calculus-ab-diagnostic-05.html", "Set 05 (DiffEq/Vols)", "20 Qs", False),
      ("calculus-ab-diagnostic-random.html", "🎲 Random 20-Q Mock", "Shuffled", True)
    ]
    
    tabs_phys = [
      ("physics-1-diagnostic-01.html", "Set 01 (Kinematics)", "20 Qs", False),
      ("physics-1-diagnostic-02.html", "Set 02 (Dynamics)", "20 Qs", False),
      ("physics-1-diagnostic-03.html", "Set 03 (Circ/Energy)", "20 Qs", False),
      ("physics-1-diagnostic-04.html", "Set 04 (Momentum)", "20 Qs", False),
      ("physics-1-diagnostic-05.html", "Set 05 (Rotation/SHM)", "20 Qs", False),
      ("physics-1-diagnostic-random.html", "🎲 Random 20-Q Mock", "Shuffled", True)
    ]
    
    tabs = tabs_calc if is_calc else tabs_phys
    
    switcher_btns = []
    for fn, label, meta, is_random in tabs:
        active_cls = " active" if fn == runner["filename"] else ""
        aria_sel = "true" if fn == runner["filename"] else "false"
        rand_cls = " random-btn" if is_random else ""
        data_set_attr = ' data-set="random"' if is_random else ''
        switcher_btns.append(f"""        <a href="{fn}" class="set-btn{rand_cls}{active_cls}" role="tab" aria-selected="{aria_sel}"{data_set_attr}>
          <span>{label}</span>
          <span class="set-badge-count">{meta}</span>
        </a>""")
    switcher_html = "\n".join(switcher_btns)

    initial_set = "random" if runner["set_key"] == "random" else f"set{int(runner['set_key'])}"
    prefix = "ap_calculus_ab" if is_calc else "ap_physics_1"

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{runner['title']}</title>
  <meta name="description" content="{runner['desc']}">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{runner['quiz_name']}",
    "description": "{runner['desc']}",
    "educationalLevel": "High School Grade 10-12 / College Credit",
    "learningResourceType": "Diagnostic Quiz",
    "provider": {{
      "@type": "Organization",
      "name": "MockTestVault",
      "url": "https://mocktestvault.com"
    }}
  }}
  </script>
</head>
<body>

  <!-- Print Only Header -->
  <div class="print-only-header">
    <h1>MockTestVault US — {runner['print_title']}</h1>
    <p>{runner['print_sub']}</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">🇺🇸</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">{course_name}</span></h1>
          <p>Advanced Placement Examination Simulator (100 Questions Vault)</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant step-by-step rationales & formulas">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Official {runner['time_mins']}-minute AP Section I simulation">
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
      <a href="../index.html">US Exam Vault</a>
      <span class="sep">/</span>
      <span class="current">{runner['h1']}</span>
    </div>
  </nav>

  <!-- Section Info Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">{course_name} 100-Question Modules:</span>
      <div class="set-btn-group" role="tablist">
{switcher_html}
      </div>
    </div>
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">{runner['time_mins']}:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading official AP CED questions...</span>
        <div class="progress-bar-track">
          <div id="progress-bar-fill" class="progress-bar-fill"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Split Layout -->
  <main class="test-layout" id="test-layout">
    
    <!-- Question Card -->
    <section class="question-card" id="question-card" aria-label="Active Test Question">
      <div class="meta-badges-row" id="q-badges">
        <span class="badge badge-chapter">{course_name}</span>
        <span class="badge badge-subtopic" id="q-subtopic-badge">CED Core Unit</span>
        <span class="badge badge-subtopic" id="q-diff-badge">Medium</span>
      </div>

      <div class="question-text-box">
        <div class="question-number" id="q-number">Question 1 of 20</div>
        <div class="question-title" id="q-title">Loading question...</div>
      </div>

      <!-- Interactive Options -->
      <div class="options-list" id="options-list" role="radiogroup" aria-label="Answer Options"></div>

      <!-- Explanation Box -->
      <div class="explanation-box" id="explanation-box" style="display:none;">
        <div class="explanation-header">
          <span>💡 College Board Answer Rationale & Formula Method</span>
          <span class="citation-tag" id="citation-tag">College Board Specification</span>
        </div>
        <p class="explanation-text" id="explanation-text"></p>
      </div>

      <!-- Action Buttons Row -->
      <div class="card-action-bar">
        <button id="btn-prev" class="nav-btn" disabled>
          <span>⬅️</span> Previous
        </button>

        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <button id="btn-review" class="nav-btn btn-review" title="Flag question to review later">
            <span>🚩</span> Mark for Review
          </button>
          <button id="btn-clear" class="nav-btn" title="Clear chosen answer option">
            <span>🧹</span> Clear Choice
          </button>
        </div>

        <div style="display:flex; gap:10px;">
          <button id="btn-next" class="nav-btn btn-primary">
            Next <span>➡️</span>
          </button>
          <button id="btn-submit" class="nav-btn btn-submit-test">
            Submit Test <span>🏁</span>
          </button>
        </div>
      </div>
    </section>

    <!-- CBT Question Palette -->
    <aside class="palette-card" aria-label="Question Navigation Grid">
      <div class="palette-title">
        <span>Question Palette</span>
        <span id="palette-summary" style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">0 / 20 Answered</span>
      </div>

      <div class="palette-grid" id="palette-grid">
        <!-- 1 to 20 dynamically populated -->
      </div>

      <div class="palette-legend">
        <div class="legend-item">
          <div class="legend-dot dot-answered"></div>
          <span>Answered (<strong id="count-answered">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-not-answered"></div>
          <span>Not Answered (<strong id="count-not-answered">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-reviewed"></div>
          <span>Marked Review (<strong id="count-reviewed">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-unvisited"></div>
          <span>Not Visited (<strong id="count-unvisited">20</strong>)</span>
        </div>
      </div>

      <div style="margin-top:18px;">
        <button id="btn-open-submit" class="nav-btn btn-submit-test" style="width:100%; justify-content:center;">
          <span>🏁</span> Submit Test & Scorecard
        </button>
      </div>
    </aside>

  </main>

  <!-- Scorecard View -->
  <section class="scorecard-view" id="scorecard-view" style="max-width:960px; margin:24px auto; padding:32px 24px;">
    <div class="score-hero" id="score-hero"></div>
    <div class="stats-grid" id="stats-grid"></div>

    <div class="scorecard-actions" style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap; margin:24px 0;">
      <button id="btn-retake" class="nav-btn btn-primary">
        <span>🔄</span> Retake Test
      </button>
      <button id="btn-print" class="nav-btn">
        <span>🖨️</span> Print / PDF Sheet
      </button>
      <a href="{runner['next_url']}" class="nav-btn" style="text-decoration:none; background:var(--primary); color:#fff;">
        {runner['next_text']}
      </a>
    </div>

    <div id="mastery-container"></div>

    <div class="review-filter-bar" style="margin-top:28px;">
      <div class="filter-pills" role="tablist" style="display:flex; gap:8px; flex-wrap:wrap;">
        <button class="filter-pill active" data-filter="all" id="filter-all">All (<span id="filter-count-all">20</span>)</button>
        <button class="filter-pill filter-wrong" data-filter="wrong" id="filter-wrong">❌ Mistakes (<span id="filter-count-wrong">0</span>)</button>
        <button class="filter-pill filter-reviewed" data-filter="reviewed" id="filter-reviewed">🟣 Review (<span id="filter-count-reviewed">0</span>)</button>
        <button class="filter-pill filter-correct" data-filter="correct" id="filter-correct">✓ Correct (<span id="filter-count-correct">0</span>)</button>
      </div>
    </div>

    <div id="review-list"></div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <p><strong>MockTestVault.com</strong> — 100% Free Educational Practice & Standardized Exam Simulators.</p>
      <p style="font-size:0.75rem;">Distraction-Free Computer-Based Testing. Aligned with official College Board AP® Course and Exam Description (CED) standards. AP® is a registered trademark of the College Board, which is not affiliated with this website.</p>
    </div>
  </footer>

  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: '{initial_set}',
        timeLimitMinutes: {runner['time_mins']},
        randomSampleSize: 20,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'ap',
        setSources: {{
          set1: '../../data/us/ap/{prefix}_set1.json',
          set2: '../../data/us/ap/{prefix}_set2.json',
          set3: '../../data/us/ap/{prefix}_set3.json',
          set4: '../../data/us/ap/{prefix}_set4.json',
          set5: '../../data/us/ap/{prefix}_set5.json'
        }}
      }});
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>"""
    return html

# Generate SAT Math Runners (5 Sets + 1 Random)
for r in SAT_MATH_RUNNERS:
    target_path = os.path.join(US_SAT_DIR, r["filename"])
    content = generate_sat_template(r, category="math")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/sat/{r['filename']}")

# Generate SAT Reading Runners (5 Sets + 1 Random)
for r in SAT_READING_RUNNERS:
    target_path = os.path.join(US_SAT_DIR, r["filename"])
    content = generate_sat_template(r, category="reading")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/sat/{r['filename']}")

# Generate AP Calc Runners (5 Sets + 1 Random)
for r in AP_CALC_RUNNERS:
    target_path = os.path.join(US_AP_DIR, r["filename"])
    content = generate_ap_template(r, exam_type="calc")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/ap/{r['filename']}")

# Generate AP Physics Runners (5 Sets + 1 Random)
for r in AP_PHYSICS_RUNNERS:
    target_path = os.path.join(US_AP_DIR, r["filename"])
    content = generate_ap_template(r, exam_type="phys")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/ap/{r['filename']}")
