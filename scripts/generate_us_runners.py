#!/usr/bin/env python3
"""
Generates and updates all 10 US examination runner HTML pages:
- SAT Math Practice 01, 02, 03, 04
- SAT Reading & Writing Practice 01, 02, 03, 04
- AP Calculus AB Diagnostic 01
- AP Physics 1 Diagnostic 01

Maintains 100% adherence to:
- Test Engine architecture (../../css/test-engine.css, ../../js/test-engine.js)
- JSON-LD Quiz Schema markup
- 4-module tab navigation in SAT runners
- Multi-exam tab navigation in AP runners
- Interlinked next-test scorecard CTA funnels
- Distraction-Free exam engine policy (Zero Ads claims purged)
- Canonical breadcrumbs & College Board citations
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_SAT_DIR = os.path.join(BASE_DIR, "us", "sat")
US_AP_DIR = os.path.join(BASE_DIR, "us", "ap")

os.makedirs(US_SAT_DIR, exist_ok=True)
os.makedirs(US_AP_DIR, exist_ok=True)

# ----------------------------------------------------------------------
# SAT Math Runner Configurations
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
    "json_path": "../../data/us/sat/digital_sat_math_set1.json",
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
    "json_path": "../../data/us/sat/digital_sat_math_set2.json",
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
    "json_path": "../../data/us/sat/digital_sat_math_set3.json",
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
    "json_path": "../../data/us/sat/digital_sat_math_set4.json",
    "time_mins": 32,
    "next_url": "reading-practice-01.html",
    "next_text": "<span>📖</span> Take Reading & Writing Module 01 →",
    "score_label": "Est. SAT Math Section"
  }
]

# ----------------------------------------------------------------------
# SAT Reading & Writing Runner Configurations
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
    "json_path": "../../data/us/sat/digital_sat_reading_set1.json",
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
    "json_path": "../../data/us/sat/digital_sat_reading_set2.json",
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
    "json_path": "../../data/us/sat/digital_sat_reading_set3.json",
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
    "json_path": "../../data/us/sat/digital_sat_reading_set4.json",
    "time_mins": 32,
    "next_url": "../ap/calculus-ab-diagnostic-01.html",
    "next_text": "<span>∫</span> Try AP® Calculus AB Diagnostic Test →",
    "score_label": "Est. SAT RW Section"
  }
]

# ----------------------------------------------------------------------
# AP Exam Runner Configurations
# ----------------------------------------------------------------------
AP_RUNNERS = [
  {
    "filename": "calculus-ab-diagnostic-01.html",
    "set_key": "01",
    "title": "AP® Calculus AB Diagnostic Practice Test 01 | MockTestVault US",
    "desc": "Free timed AP Calculus AB diagnostic test (20 Multiple Choice Questions) covering Limits, Continuity, Differentiation Rules, FTC, and Integration by Substitution.",
    "h1": "AP® Calculus AB Diagnostic 01",
    "print_title": "AP® Calculus AB Practice Diagnostic Test 01",
    "print_sub": "Official College Board AP® CED Specification: Limits, Derivatives, Integration, and Differential Equations | mocktestvault.com",
    "quiz_name": "AP® Calculus AB Section I Diagnostic Practice Test 01",
    "json_path": "../../data/us/ap/ap_calculus_ab_set1.json",
    "time_mins": 45,
    "next_url": "physics-1-diagnostic-01.html",
    "next_text": "<span>⚡</span> Take AP® Physics 1 Diagnostic Test →",
    "score_label": "AP Scaled Score Projection",
    "course_name": "AP® Calculus AB",
    "icon": "∫"
  },
  {
    "filename": "physics-1-diagnostic-01.html",
    "set_key": "01",
    "title": "AP® Physics 1: Algebra-Based Diagnostic Test 01 | MockTestVault US",
    "desc": "Free timed AP Physics 1 diagnostic test (20 Multiple Choice Questions) covering Kinematics, Newton's Laws, Work & Energy, Momentum, Torque, and SHM.",
    "h1": "AP® Physics 1 Diagnostic 01",
    "print_title": "AP® Physics 1: Algebra-Based Diagnostic Test 01",
    "print_sub": "Official College Board AP® CED Specification: Kinematics, Dynamics, Energy, Momentum, and Rotation | mocktestvault.com",
    "quiz_name": "AP® Physics 1: Algebra-Based Section I Diagnostic Test 01",
    "json_path": "../../data/us/ap/ap_physics_1_set1.json",
    "time_mins": 40,
    "next_url": "../sat/math-practice-01.html",
    "next_text": "<span>📐</span> Practice Digital SAT® Math Modules →",
    "score_label": "AP Scaled Score Projection",
    "course_name": "AP® Physics 1",
    "icon": "⚡"
  }
]

def generate_sat_template(runner, category="math"):
    is_math = (category == "math")
    track_title = "Digital SAT® Math" if is_math else "Digital SAT® Reading & Writing"
    
    modules_math = [
      ("math-practice-01.html", "📐 Math Module 01 (Core Diagnostic)"),
      ("math-practice-02.html", "📊 Math Module 02 (Algebra & Functions)"),
      ("math-practice-03.html", "📐 Math Module 03 (Advanced Math & Geom)"),
      ("math-practice-04.html", "🎯 Math Module 04 (700-800 Benchmark)")
    ]
    
    modules_reading = [
      ("reading-practice-01.html", "📖 Reading Module 01 (Core Diagnostic)"),
      ("reading-practice-02.html", "🔍 Reading Module 02 (Craft & Structure)"),
      ("reading-practice-03.html", "📊 Reading Module 03 (Information & Ideas)"),
      ("reading-practice-04.html", "✍️ Reading Module 04 (Advanced Conventions)")
    ]
    
    modules = modules_math if is_math else modules_reading
    
    # Build switcher buttons
    switcher_btns = []
    for fn, label in modules:
        active_cls = " active" if fn == runner["filename"] else ""
        aria_sel = "true" if fn == runner["filename"] else "false"
        switcher_btns.append(f"""        <a href="{fn}" class="set-btn{active_cls}" role="tab" aria-selected="{aria_sel}">
          <span>{label}</span>
          <span class="set-badge-count">20 Qs • 32 Mins</span>
        </a>""")
    switcher_html = "\n".join(switcher_btns)

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
      <span class="set-label">{track_title} Modules:</span>
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

  <!-- Main Test Layout -->
  <main class="test-layout" id="test-layout">
    
    <!-- Left Column: Question Area -->
    <section class="question-column">
      <div class="question-card" id="question-card">
        <div class="q-header">
          <span class="q-number-badge" id="q-number-badge">Question 1</span>
          <div class="q-meta-group">
            <span class="q-badge" id="q-subtopic-badge">Standard Topic</span>
            <span class="q-badge" id="q-diff-badge">Medium</span>
          </div>
        </div>

        <div class="q-body" id="q-body">
          <p id="q-text">Loading question text...</p>
        </div>

        <div class="options-group" id="options-group" role="radiogroup" aria-label="Answer Options">
          <!-- Dynamically populated options A, B, C, D -->
        </div>

        <!-- Practice Mode Explanation Box -->
        <div class="explanation-box" id="explanation-box" style="display: none;">
          <div class="exp-title">
            <span>💡</span> College Board Answer Rationale & Formula Method:
          </div>
          <div class="exp-body" id="exp-text"></div>
          <div class="exp-citation" id="exp-citation"></div>
        </div>

        <!-- Question Card Action Controls -->
        <div class="q-actions-bar">
          <div class="action-left">
            <button id="btn-review" class="btn-action btn-review" title="Flag this question to review later">
              <span>🚩</span> Mark for Review
            </button>
            <button id="btn-clear" class="btn-action btn-clear" title="Clear chosen answer option">
              Clear Choice
            </button>
          </div>

          <div class="action-right">
            <button id="btn-prev" class="btn-nav btn-prev" disabled>
              ← Previous
            </button>
            <button id="btn-next" class="btn-nav btn-next">
              Next Question →
            </button>
            <button id="btn-submit" class="btn-nav btn-submit" style="display:none;">
              Finish Module
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Right Column: Navigation Palette & Overview -->
    <aside class="palette-column" aria-label="Question Navigation Palette">
      <div class="palette-card">
        <div class="palette-header">
          <h3>Question Palette</h3>
          <span class="palette-count" id="palette-summary">0 / 20 Answered</span>
        </div>

        <!-- Official Status Legend -->
        <div class="palette-legend">
          <div class="legend-item"><span class="legend-dot dot-not-visited"></span> Not Visited</div>
          <div class="legend-item"><span class="legend-dot dot-not-answered"></span> Unanswered</div>
          <div class="legend-item"><span class="legend-dot dot-answered"></span> Answered</div>
          <div class="legend-item"><span class="legend-dot dot-review"></span> Marked Review</div>
        </div>

        <!-- Grid of Question Buttons -->
        <div class="palette-grid" id="palette-grid">
          <!-- 1 to 20 dynamically populated -->
        </div>

        <div class="palette-footer">
          <button id="btn-open-submit" class="btn-palette-submit">
            <span>🏁</span> Submit Test & Scorecard
          </button>
        </div>
      </div>
    </aside>

  </main>

  <!-- Comprehensive Scorecard View (Shown on Submission) -->
  <section id="scorecard-view" class="scorecard-view" style="display: none;">
    <div class="scorecard-hero">
      <div class="scorecard-badge">{runner['h1']} Performance Summary</div>
      <h2 id="scorecard-greeting">Test Complete!</h2>
      <p id="scorecard-subtext">Here is your detailed breakdown according to College Board SAT scoring benchmarks.</p>

      <div class="score-tiles-grid">
        <div class="score-tile">
          <div class="tile-label">Raw Score</div>
          <div class="tile-val" id="score-raw">0 / 20</div>
        </div>
        <div class="score-tile">
          <div class="tile-label">Accuracy</div>
          <div class="tile-val" id="score-pct">0%</div>
        </div>
        <div class="score-tile">
          <div class="tile-label">{runner['score_label']}</div>
          <div class="tile-val" id="score-sat-scale">680 - 750</div>
        </div>
        <div class="score-tile">
          <div class="tile-label">Time Elapsed</div>
          <div class="tile-val" id="score-time">00:00</div>
        </div>
      </div>

      <div class="scorecard-actions">
        <button id="btn-retake" class="btn-scorecard btn-retake">
          <span>🔄</span> Retake Test
        </button>
        <button id="btn-print-sheet" class="btn-scorecard btn-print">
          <span>🖨️</span> Print Revision Sheet (PDF)
        </button>
        <a href="{runner['next_url']}" class="btn-scorecard btn-next-ch">
          {runner['next_text']}
        </a>
      </div>
    </div>

    <!-- Review Section with Filter Pills -->
    <div class="scorecard-filter-bar">
      <h3>Detailed Solution Review</h3>
      <div class="filter-pills-group" role="tablist">
        <button class="filter-pill active" data-filter="all" id="filter-all">
          All (<span id="filter-count-all">20</span>)
        </button>
        <button class="filter-pill filter-incorrect" data-filter="incorrect" id="filter-incorrect">
          ✗ Incorrect (<span id="filter-count-incorrect">0</span>)
        </button>
        <button class="filter-pill filter-unanswered" data-filter="unanswered" id="filter-unanswered">
          ⚪ Unanswered (<span id="filter-count-unanswered">0</span>)
        </button>
        <button class="filter-pill filter-reviewed" data-filter="reviewed" id="filter-reviewed">
          🟣 Review (<span id="filter-count-reviewed">0</span>)
        </button>
        <button class="filter-pill filter-correct" data-filter="correct" id="filter-correct">
          ✓ Correct (<span id="filter-count-correct">0</span>)
        </button>
      </div>
    </div>

    <!-- Full Review List -->
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
        initialSet: 'set1',
        timeLimitMinutes: {runner['time_mins']},
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'sat',
        setSources: {{
          set1: '{runner['json_path']}'
        }}
      }});
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>"""
    return html

def generate_ap_template(runner):
    ap_tabs = [
      ("calculus-ab-diagnostic-01.html", "📐 AP® Calculus AB Diagnostic 01", "20 Qs • 45 Mins"),
      ("physics-1-diagnostic-01.html", "⚡ AP® Physics 1 Diagnostic 01", "20 Qs • 40 Mins")
    ]
    
    switcher_btns = []
    for fn, label, meta in ap_tabs:
        active_cls = " active" if fn == runner["filename"] else ""
        aria_sel = "true" if fn == runner["filename"] else "false"
        switcher_btns.append(f"""        <a href="{fn}" class="set-btn{active_cls}" role="tab" aria-selected="{aria_sel}">
          <span>{label}</span>
          <span class="set-badge-count">{meta}</span>
        </a>""")
    switcher_html = "\n".join(switcher_btns)

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
          <h1>MockTestVault <span class="vault-pill">{runner['course_name']}</span></h1>
          <p>Advanced Placement Examination Simulator</p>
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
      <span class="set-label">College Board AP Track:</span>
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

  <!-- Main Test Layout -->
  <main class="test-layout" id="test-layout">
    
    <!-- Left Column: Question Area -->
    <section class="question-column">
      <div class="question-card" id="question-card">
        <div class="q-header">
          <span class="q-number-badge" id="q-number-badge">Question 1</span>
          <div class="q-meta-group">
            <span class="q-badge" id="q-subtopic-badge">CED Core Unit</span>
            <span class="q-badge" id="q-diff-badge">Medium</span>
          </div>
        </div>

        <div class="q-body" id="q-body">
          <p id="q-text">Loading question text...</p>
        </div>

        <div class="options-group" id="options-group" role="radiogroup" aria-label="Answer Options">
          <!-- Dynamically populated options A, B, C, D -->
        </div>

        <!-- Practice Mode Explanation Box -->
        <div class="explanation-box" id="explanation-box" style="display: none;">
          <div class="exp-title">
            <span>💡</span> College Board Answer Rationale & Formula Method:
          </div>
          <div class="exp-body" id="exp-text"></div>
          <div class="exp-citation" id="exp-citation"></div>
        </div>

        <!-- Question Card Action Controls -->
        <div class="q-actions-bar">
          <div class="action-left">
            <button id="btn-review" class="btn-action btn-review" title="Flag this question to review later">
              <span>🚩</span> Mark for Review
            </button>
            <button id="btn-clear" class="btn-action btn-clear" title="Clear chosen answer option">
              Clear Choice
            </button>
          </div>

          <div class="action-right">
            <button id="btn-prev" class="btn-nav btn-prev" disabled>
              ← Previous
            </button>
            <button id="btn-next" class="btn-nav btn-next">
              Next Question →
            </button>
            <button id="btn-submit" class="btn-nav btn-submit" style="display:none;">
              Finish Exam
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Right Column: Navigation Palette & Overview -->
    <aside class="palette-column" aria-label="Question Navigation Palette">
      <div class="palette-card">
        <div class="palette-header">
          <h3>Question Palette</h3>
          <span class="palette-count" id="palette-summary">0 / 20 Answered</span>
        </div>

        <!-- Official Status Legend -->
        <div class="palette-legend">
          <div class="legend-item"><span class="legend-dot dot-not-visited"></span> Not Visited</div>
          <div class="legend-item"><span class="legend-dot dot-not-answered"></span> Unanswered</div>
          <div class="legend-item"><span class="legend-dot dot-answered"></span> Answered</div>
          <div class="legend-item"><span class="legend-dot dot-review"></span> Marked Review</div>
        </div>

        <!-- Grid of Question Buttons -->
        <div class="palette-grid" id="palette-grid">
          <!-- 1 to 20 dynamically populated -->
        </div>

        <div class="palette-footer">
          <button id="btn-open-submit" class="btn-palette-submit">
            <span>🏁</span> Submit Test & Scorecard
          </button>
        </div>
      </div>
    </aside>

  </main>

  <!-- Comprehensive Scorecard View (Shown on Submission) -->
  <section id="scorecard-view" class="scorecard-view" style="display: none;">
    <div class="scorecard-hero">
      <div class="scorecard-badge">{runner['h1']} Performance Summary</div>
      <h2 id="scorecard-greeting">Diagnostic Complete!</h2>
      <p id="scorecard-subtext">Here is your detailed breakdown according to College Board AP scoring benchmarks.</p>

      <div class="score-tiles-grid">
        <div class="score-tile">
          <div class="tile-label">Raw Score</div>
          <div class="tile-val" id="score-raw">0 / 20</div>
        </div>
        <div class="score-tile">
          <div class="tile-label">Accuracy</div>
          <div class="tile-val" id="score-pct">0%</div>
        </div>
        <div class="score-tile">
          <div class="tile-label">Projected AP Score</div>
          <div class="tile-val" id="score-sat-scale">Score 5 (Top Tier)</div>
        </div>
        <div class="score-tile">
          <div class="tile-label">Time Elapsed</div>
          <div class="tile-val" id="score-time">00:00</div>
        </div>
      </div>

      <div class="scorecard-actions">
        <button id="btn-retake" class="btn-scorecard btn-retake">
          <span>🔄</span> Retake Test
        </button>
        <button id="btn-print-sheet" class="btn-scorecard btn-print">
          <span>🖨️</span> Print Revision Sheet (PDF)
        </button>
        <a href="{runner['next_url']}" class="btn-scorecard btn-next-ch">
          {runner['next_text']}
        </a>
      </div>
    </div>

    <!-- Review Section with Filter Pills -->
    <div class="scorecard-filter-bar">
      <h3>Detailed Solution Review</h3>
      <div class="filter-pills-group" role="tablist">
        <button class="filter-pill active" data-filter="all" id="filter-all">
          All (<span id="filter-count-all">20</span>)
        </button>
        <button class="filter-pill filter-incorrect" data-filter="incorrect" id="filter-incorrect">
          ✗ Incorrect (<span id="filter-count-incorrect">0</span>)
        </button>
        <button class="filter-pill filter-unanswered" data-filter="unanswered" id="filter-unanswered">
          ⚪ Unanswered (<span id="filter-count-unanswered">0</span>)
        </button>
        <button class="filter-pill filter-reviewed" data-filter="reviewed" id="filter-reviewed">
          🟣 Review (<span id="filter-count-reviewed">0</span>)
        </button>
        <button class="filter-pill filter-correct" data-filter="correct" id="filter-correct">
          ✓ Correct (<span id="filter-count-correct">0</span>)
        </button>
      </div>
    </div>

    <!-- Full Review List -->
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
        initialSet: 'set1',
        timeLimitMinutes: {runner['time_mins']},
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'board',
        setSources: {{
          set1: '{runner['json_path']}'
        }}
      }});
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>"""
    return html

# Generate SAT Math Runners
for r in SAT_MATH_RUNNERS:
    target_path = os.path.join(US_SAT_DIR, r["filename"])
    content = generate_sat_template(r, category="math")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/sat/{r['filename']}")

# Generate SAT Reading Runners
for r in SAT_READING_RUNNERS:
    target_path = os.path.join(US_SAT_DIR, r["filename"])
    content = generate_sat_template(r, category="reading")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/sat/{r['filename']}")

# Generate AP Runners
for r in AP_RUNNERS:
    target_path = os.path.join(US_AP_DIR, r["filename"])
    content = generate_ap_template(r)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated: us/ap/{r['filename']}")

print("All 10 US examination runners generated/updated successfully!")
