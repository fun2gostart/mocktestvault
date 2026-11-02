#!/usr/bin/env python3
"""
CBSE Class 10 Full 80-Mark Mock Runners & Hub Generator
Generates:
1. cbse-class-10/sample-papers/science-board-mock-01.html
2. cbse-class-10/sample-papers/mathematics-board-mock-01.html
3. cbse-class-10/sample-papers/social-science-board-mock-01.html
4. cbse-class-10/sample-papers/index.html (Dedicated Hub)
"""

import os

RUNNER_DIR = os.path.join(os.path.dirname(__file__), "..", "cbse-class-10", "sample-papers")
os.makedirs(RUNNER_DIR, exist_ok=True)

papers = [
    {
        "filename": "science-board-mock-01.html",
        "subject_name": "Science",
        "subject_code": "Code 086",
        "icon": "🧪",
        "title": "CBSE Class 10 Science Official 80-Mark Board Mock Paper 01 | MockTestVault",
        "desc": "Free 80-question full-syllabus CBSE Class 10 Science Board Mock Paper with 3-hour timer, Chemistry, Biology & Physics section tabs, instant NCERT rationales, and printable PDF sheet.",
        "breadcrumb": "Science 80-Mark Mock 01",
        "json_source": "../../data/in/cbse10/sample-papers/science_board_mock01.json",
        "next_url": "mathematics-board-mock-01.html",
        "next_label": "Take Mathematics 80-Mark Mock Paper 01 →",
        "next_icon": "📐",
        "sections": [
            {"name": "🧪 Sec A: Chemistry", "badge": "Q 1–25", "start": 0, "end": 24},
            {"name": "🧬 Sec B: Biology", "badge": "Q 26–53", "start": 25, "end": 52},
            {"name": "⚡ Sec C: Physics", "badge": "Q 54–76", "start": 53, "end": 75},
            {"name": "🌿 Sec D: Environment", "badge": "Q 77–80", "start": 76, "end": 79}
        ]
    },
    {
        "filename": "mathematics-board-mock-01.html",
        "subject_name": "Mathematics",
        "subject_code": "Code 041 / 241",
        "icon": "📐",
        "title": "CBSE Class 10 Mathematics Standard & Basic 80-Mark Board Mock Paper 01 | MockTestVault",
        "desc": "Free 80-question full-syllabus CBSE Class 10 Math Board Mock Paper with 3-hour timer, Algebra, Geometry, Trigonometry & Statistics section tabs, and printable PDF sheet.",
        "breadcrumb": "Mathematics 80-Mark Mock 01",
        "json_source": "../../data/in/cbse10/sample-papers/mathematics_board_mock01.json",
        "next_url": "social-science-board-mock-01.html",
        "next_label": "Take Social Science 80-Mark Mock Paper 01 →",
        "next_icon": "🌍",
        "sections": [
            {"name": "🔢 Sec A: Number Systems & Algebra", "badge": "Q 1–25", "start": 0, "end": 24},
            {"name": "📐 Sec B: Geometry & Coord Geo", "badge": "Q 26–45", "start": 25, "end": 44},
            {"name": "📏 Sec C: Trig & Mensuration", "badge": "Q 46–65", "start": 45, "end": 64},
            {"name": "📊 Sec D: Stats & Probability", "badge": "Q 66–80", "start": 65, "end": 79}
        ]
    },
    {
        "filename": "social-science-board-mock-01.html",
        "subject_name": "Social Science",
        "subject_code": "Code 087",
        "icon": "🌍",
        "title": "CBSE Class 10 Social Science 80-Mark Board Mock Paper 01 | MockTestVault",
        "desc": "Free 80-question full-syllabus CBSE Class 10 Social Science Board Mock Paper with 3-hour timer, History, Geography, Civics & Economics section tabs, and printable PDF sheet.",
        "breadcrumb": "Social Science 80-Mark Mock 01",
        "json_source": "../../data/in/cbse10/sample-papers/social_science_board_mock01.json",
        "next_url": "science-board-mock-01.html",
        "next_label": "Take Science 80-Mark Mock Paper 01 →",
        "next_icon": "🧪",
        "sections": [
            {"name": "📜 Sec A: History", "badge": "Q 1–20", "start": 0, "end": 19},
            {"name": "🌍 Sec B: Geography", "badge": "Q 21–40", "start": 20, "end": 39},
            {"name": "⚖️ Sec C: Political Science", "badge": "Q 41–60", "start": 40, "end": 59},
            {"name": "📈 Sec D: Economics", "badge": "Q 61–80", "start": 60, "end": 79}
        ]
    }
]

runner_template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <style>
    .cgl-section-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 10px 16px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-color);
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

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{title_clean}",
    "description": "{desc}",
    "educationalLevel": "Grade 10 / Secondary School Examination",
    "learningResourceType": "Full Mock Exam",
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
    <h1>MockTestVault — CBSE Class 10 {subject_name} Official 80-Mark Board Mock Paper 01</h1>
    <p>Full Syllabus 80-Question Solved Examination ({subject_code}) | 80 Marks • 180 Mins | mocktestvault.com</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">{icon}</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">CBSE Class 10</span></h1>
          <p>{subject_name} Full 80-Mark Board Exam Simulator</p>
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
      <a href="../../in/index.html">India Exam Vault</a>
      <span class="sep">/</span>
      <a href="../index.html">CBSE Class 10</a>
      <span class="sep">/</span>
      <a href="index.html">Sample Papers</a>
      <span class="sep">/</span>
      <span class="current">{breadcrumb}</span>
    </div>
  </nav>

  <!-- Section Tabs Bar -->
  <div class="cgl-section-tabs" role="tablist" aria-label="Examination Syllabus Sections">
{section_buttons_html}
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">180:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading CBSE Class 10 {subject_name} Paper...</span>
        <div class="progress-bar-track">
          <div id="progress-bar-fill" class="progress-bar-fill"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Split Layout -->
  <main class="test-layout" id="test-layout">
    
    <!-- Question Card -->
    <section class="question-card" id="question-card" aria-label="Active Board Question">
      <div class="meta-badges-row" id="q-badges">
        <span class="badge badge-chapter">CBSE Class 10 {subject_name}</span>
        <span class="badge badge-subtopic" id="q-subtopic-badge">Board Syllabus</span>
        <span class="badge badge-subtopic" id="q-diff-badge">Standard</span>
      </div>

      <div class="question-text-box">
        <div class="question-number" id="q-number">Question 1 of 80</div>
        <div class="question-title" id="q-title">Loading question...</div>
      </div>

      <!-- Interactive Options -->
      <div class="options-list" id="options-list" role="radiogroup" aria-label="Answer Options"></div>

      <!-- Explanation Box -->
      <div class="explanation-box" id="explanation-box" style="display:none;">
        <div class="explanation-header">
          <span>💡 NCERT Step-by-Step Conceptual Rationale</span>
          <span class="citation-tag" id="citation-tag">Official NCERT Class 10 Textbook</span>
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
        <span>Question Palette (80 Questions)</span>
        <span id="palette-summary" style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">0 / 80 Answered</span>
      </div>

      <div class="palette-grid" id="palette-grid">
        <!-- 1 to 80 dynamically populated -->
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
          <span>Not Visited (<strong id="count-unvisited">80</strong>)</span>
        </div>
      </div>

      <div style="margin-top:18px;">
        <button id="btn-open-submit" class="nav-btn btn-submit-test" style="width:100%; justify-content:center;">
          <span>🏁</span> Submit Test & View Scorecard
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
        <span>🔄</span> Retake Examination
      </button>
      <button id="btn-print" class="nav-btn">
        <span>🖨️</span> Print / PDF Revision Sheet
      </button>
      <a href="{next_url}" class="nav-btn" style="text-decoration:none; background:var(--primary); color:#fff;">
        <span>{next_icon}</span> {next_label}
      </a>
      <a href="index.html" class="nav-btn" style="text-decoration:none;">
        <span>📚</span> View All 80-Mark Sample Papers
      </a>
    </div>

    <div id="mastery-container"></div>

    <div class="review-filter-bar" style="margin-top:28px;">
      <div class="filter-pills" role="tablist" style="display:flex; gap:8px; flex-wrap:wrap;">
        <button class="filter-pill active" data-filter="all" id="filter-all">All (<span id="filter-count-all">80</span>)</button>
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
      <p><strong>MockTestVault.com</strong> — 100% Free Educational Practice & Board Exam Simulators.</p>
      <p style="font-size:0.75rem;">100% Free & Distraction-Free. Aligned with official Central Board of Secondary Education (CBSE) Class 10 Examination specifications.</p>
    </div>
  </footer>

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
          set1: '{json_source}'
        }}
      }});
      window.testEngine.loadQuestions();

      // Automatically keep the active section tab synchronized
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
</html>
"""

for p in papers:
    sec_html_lines = []
    for idx, sec in enumerate(p["sections"]):
        active_cls = " active" if idx == 0 else ""
        sec_html_lines.append(
            f'    <button class="cgl-sec-btn{active_cls}" data-start="{sec["start"]}" data-end="{sec["end"]}" onclick="jumpToSection({sec["start"]}, this)">'
            f'<span>{sec["name"]}</span> <span class="cgl-sec-badge">{sec["badge"]}</span></button>'
        )
    section_buttons_html = "\n".join(sec_html_lines)
    title_clean = p["title"].split("|")[0].strip()
    
    rendered = runner_template.format(
        title=p["title"],
        title_clean=title_clean,
        desc=p["desc"],
        subject_name=p["subject_name"],
        subject_code=p["subject_code"],
        icon=p["icon"],
        breadcrumb=p["breadcrumb"],
        json_source=p["json_source"],
        next_url=p["next_url"],
        next_label=p["next_label"],
        next_icon=p["next_icon"],
        section_buttons_html=section_buttons_html
    )
    
    out_file = os.path.join(RUNNER_DIR, p["filename"])
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"Generated {p['filename']}")

# =========================================================================
# 4. DEDICATED HUB PAGE: cbse-class-10/sample-papers/index.html
# =========================================================================
hub_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 10 Full 80-Mark Sample Question Papers (SQP) 2025–2026 | MockTestVault</title>
  <meta name="description" content="Free official-pattern CBSE Class 10 Full 80-Mark Board Mock Papers for Science, Mathematics, and Social Science. 3-hour timed CBT simulator with section tabs, instant NCERT solutions, and printable PDF sheets.">
  <link rel="canonical" href="https://mocktestvault.com/cbse-class-10/sample-papers/">

  <link rel="stylesheet" href="../../css/homepage.css">

  <style>
    .sqp-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 24px;
      margin-top: 32px;
    }
    .sqp-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 28px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }
    .sqp-card:hover {
      border-color: var(--primary);
      transform: translateY(-4px);
      box-shadow: var(--shadow-xl);
    }
    .sqp-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }
    .sqp-icon {
      font-size: 2rem;
    }
    .sqp-status {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--accent-emerald);
      background: var(--accent-emerald-light);
      padding: 4px 10px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .sqp-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-primary);
      margin-bottom: 8px;
    }
    .sqp-code {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      margin-bottom: 12px;
    }
    .sqp-desc {
      font-size: 0.88rem;
      color: var(--text-secondary);
      line-height: 1.6;
      margin-bottom: 20px;
      flex-grow: 1;
    }
    .sqp-meta-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      background: var(--bg-subtle);
      padding: 12px;
      border-radius: var(--radius-sm);
      margin-bottom: 20px;
      font-size: 0.8rem;
    }
    .sqp-meta-item {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--text-secondary);
      font-weight: 600;
    }
    .sqp-actions {
      display: flex;
      gap: 10px;
    }
    .sqp-launch-btn {
      flex: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      background: var(--primary);
      color: #ffffff;
      padding: 12px 18px;
      border-radius: var(--radius-md);
      font-weight: 700;
      text-decoration: none;
      transition: background 0.2s ease;
    }
    .sqp-launch-btn:hover {
      background: var(--primary-hover);
    }
  </style>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "MockTestVault CBSE Class 10 Sample Question Papers",
    "url": "https://mocktestvault.com/cbse-class-10/sample-papers/",
    "description": "Full-syllabus 80-mark Computer-Based Testing simulators for CBSE Class 10 Board examinations across Science, Mathematics, and Social Science.",
    "educationalLevel": "Grade 10 / Secondary School",
    "areaServed": "India"
  }
  </script>
</head>
<body>

  <!-- Site Navigation Header -->
  <header class="global-nav">
    <div class="home-container">
      <div class="nav-wrapper">
        <a href="../../index.html" class="brand-group" aria-label="MockTestVault Home">
          <div class="brand-icon">🛡️</div>
          <div class="brand-title">
            <span>MockTestVault</span>
            <span class="brand-badge">CBSE Board Vault</span>
          </div>
        </a>

        <!-- Region Switcher Navigation -->
        <nav class="nav-links" aria-label="Regional Portals">
          <div class="region-switcher" style="display:flex; gap:6px; background:var(--bg-subtle); padding:4px; border-radius:var(--radius-full); border:1px solid var(--border-color);">
            <a href="../../in/index.html" class="nav-link active" style="background:var(--primary); color:#ffffff; padding:6px 14px; border-radius:var(--radius-full); font-weight:700; text-decoration:none;">🇮🇳 India</a>
            <a href="../../us/index.html" class="nav-link" style="color:var(--text-secondary); padding:6px 14px; border-radius:var(--radius-full); font-weight:600; text-decoration:none;">🇺🇸 United States</a>
            <a href="../../global/index.html" class="nav-link" style="color:var(--text-secondary); padding:6px 14px; border-radius:var(--radius-full); font-weight:600; text-decoration:none;">🌐 Global Tests</a>
          </div>
        </nav>

        <div class="nav-actions">
          <button id="theme-toggle-btn" class="theme-btn" title="Toggle Dark/Light Mode" aria-label="Toggle theme">🌙</button>
          <a href="../index.html" class="cta-header-btn">
            <span>📚 48-Ch Catalog</span>
          </a>
        </div>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="home-container">
      <div class="hero-grid">
        
        <div class="hero-content">
          <div class="hero-badge">
            <span class="hero-badge-dot"></span>
            <span>Official CBSE Board Pattern • 80 Marks • 3-Hour Countdown</span>
          </div>

          <h1 class="hero-title">
            CBSE Class 10 <span class="gradient-text">Full 80-Mark</span> Board Exam Simulators.
          </h1>

          <p class="hero-subtitle">
            Experience realistic 3-hour Board Examination simulations calibrated to official CBSE Class 10 sample question paper blueprints. Features section-wise jump tabs, instant NCERT rationales, 5-state question palettes, and zero paywalls.
          </p>

          <div class="hero-actions">
            <a href="science-board-mock-01.html" class="btn-primary-hero">
              <span>🧪 Launch Science 80M Paper</span>
            </a>
            <a href="mathematics-board-mock-01.html" class="btn-secondary-hero">
              <span>📐 Mathematics 80M Paper</span>
            </a>
          </div>

          <!-- Feature Bullets -->
          <div style="display:flex; flex-wrap:wrap; gap:16px; margin-top:28px; font-size:0.88rem; color:var(--text-secondary);">
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="color:var(--accent-emerald); font-weight:900;">✓</span>
              <span>Full 80-Mark Theory Blueprint</span>
            </div>
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="color:var(--accent-emerald); font-weight:900;">✓</span>
              <span>180-Minute (3-Hour) Exam Countdown</span>
            </div>
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="color:var(--accent-emerald); font-weight:900;">✓</span>
              <span>Printable Offline A4 Solved Papers</span>
            </div>
          </div>
        </div>

        <!-- Hero Teaser Card -->
        <div class="hero-teaser-card" style="background:var(--bg-card); border:1px solid var(--border-color); border-radius:var(--radius-lg); padding:28px; box-shadow:var(--shadow-xl);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
            <span style="font-size:0.75rem; font-weight:800; text-transform:uppercase; letter-spacing:0.05em; color:var(--primary); background:var(--primary-light); padding:4px 10px; border-radius:var(--radius-full);">
              Board Blueprint Calibration
            </span>
            <span style="font-size:0.8rem; color:var(--text-muted); font-weight:600;">Code 086 / 041 / 087</span>
          </div>

          <h3 style="font-size:1.15rem; font-weight:800; color:var(--text-primary); margin-bottom:14px;">
            Official Section-Wise Weightage Breakdown
          </h3>

          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:0.85rem; color:var(--text-secondary);">
            <li style="display:flex; align-items:center; justify-content:space-between; padding:8px 12px; background:var(--bg-subtle); border-radius:var(--radius-sm);">
              <span><strong>🧪 Science (Code 086):</strong> Chem (25) + Bio (28) + Phy (23) + Env (4)</span>
              <span style="color:var(--primary); font-weight:700;">80 Qs / 80M</span>
            </li>
            <li style="display:flex; align-items:center; justify-content:space-between; padding:8px 12px; background:var(--bg-subtle); border-radius:var(--radius-sm);">
              <span><strong>📐 Mathematics (Code 041):</strong> Algebra (25) + Geo (20) + Trig (20) + Stats (15)</span>
              <span style="color:var(--primary); font-weight:700;">80 Qs / 80M</span>
            </li>
            <li style="display:flex; align-items:center; justify-content:space-between; padding:8px 12px; background:var(--bg-subtle); border-radius:var(--radius-sm);">
              <span><strong>🌍 Social Science (Code 087):</strong> Hist (20) + Geo (20) + Civics (20) + Eco (20)</span>
              <span style="color:var(--primary); font-weight:700;">80 Qs / 80M</span>
            </li>
          </ul>

          <div style="margin-top:20px; font-size:0.8rem; color:var(--text-muted); line-height:1.5;">
            💡 <em>Tip: Each test can also be used in Practice Mode with instant step-by-step NCERT rationales and formula derivations.</em>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- SQP Catalog Grid -->
  <section class="section-block" style="padding: 40px 0 80px 0;">
    <div class="home-container">
      <div class="section-head">
        <span class="section-pill">Full Syllabus Board Simulators</span>
        <h2 class="section-title">Select Your 80-Mark Sample Question Paper</h2>
        <p class="section-desc">
          Complete syllabus coverage matching CBSE Board examination blueprints with sectional jump tabs and NCERT citations.
        </p>
      </div>

      <div class="sqp-grid">

        <!-- Card 1: Science -->
        <article class="sqp-card">
          <div>
            <div class="sqp-top">
              <div class="sqp-icon">🧪</div>
              <span class="sqp-status">🟢 Live • Full 80M Paper</span>
            </div>
            <div class="sqp-code">Subject Code 086 • Theory Paper</div>
            <h3 class="sqp-title">Class 10 Science — 80-Mark Board Mock 01</h3>
            <p class="sqp-desc">
              Comprehensive 80-question test covering all 13 NCERT chapters across Chemistry, Biology, Physics, and Natural Resources. Features instant formula derivations and reaction equations.
            </p>
            <div class="sqp-meta-grid">
              <div class="sqp-meta-item"><span>📝</span> 80 Questions</div>
              <div class="sqp-meta-item"><span>🎯</span> 80 Marks</div>
              <div class="sqp-meta-item"><span>⏱️</span> 180 Minutes (3 Hrs)</div>
              <div class="sqp-meta-item"><span>📑</span> 4 Section Tabs</div>
            </div>
          </div>
          <div class="sqp-actions">
            <a href="science-board-mock-01.html" class="sqp-launch-btn"><span>🚀 Start Science Paper</span></a>
          </div>
        </article>

        <!-- Card 2: Mathematics -->
        <article class="sqp-card">
          <div>
            <div class="sqp-top">
              <div class="sqp-icon">📐</div>
              <span class="sqp-status">🟢 Live • Full 80M Paper</span>
            </div>
            <div class="sqp-code">Subject Code 041 / 241 • Standard & Basic</div>
            <h3 class="sqp-title">Class 10 Mathematics — 80-Mark Board Mock 01</h3>
            <p class="sqp-desc">
              Comprehensive 80-question test covering all 14 NCERT chapters across Number Systems, Algebra, Geometry, Trigonometry, Mensuration, Statistics, and Probability.
            </p>
            <div class="sqp-meta-grid">
              <div class="sqp-meta-item"><span>📝</span> 80 Questions</div>
              <div class="sqp-meta-item"><span>🎯</span> 80 Marks</div>
              <div class="sqp-meta-item"><span>⏱️</span> 180 Minutes (3 Hrs)</div>
              <div class="sqp-meta-item"><span>📑</span> 4 Section Tabs</div>
            </div>
          </div>
          <div class="sqp-actions">
            <a href="mathematics-board-mock-01.html" class="sqp-launch-btn"><span>🚀 Start Mathematics Paper</span></a>
          </div>
        </article>

        <!-- Card 3: Social Science -->
        <article class="sqp-card">
          <div>
            <div class="sqp-top">
              <div class="sqp-icon">🌍</div>
              <span class="sqp-status">🟢 Live • Full 80M Paper</span>
            </div>
            <div class="sqp-code">Subject Code 087 • All 4 Disciplines</div>
            <h3 class="sqp-title">Class 10 Social Science — 80-Mark Board Mock 01</h3>
            <p class="sqp-desc">
              Comprehensive 80-question test covering all 21 NCERT chapters across History, Geography, Political Science, and Economics with statutory textbook page citations.
            </p>
            <div class="sqp-meta-grid">
              <div class="sqp-meta-item"><span>📝</span> 80 Questions</div>
              <div class="sqp-meta-item"><span>🎯</span> 80 Marks</div>
              <div class="sqp-meta-item"><span>⏱️</span> 180 Minutes (3 Hrs)</div>
              <div class="sqp-meta-item"><span>📑</span> 4 Section Tabs</div>
            </div>
          </div>
          <div class="sqp-actions">
            <a href="social-science-board-mock-01.html" class="sqp-launch-btn"><span>🚀 Start Social Science Paper</span></a>
          </div>
        </article>

      </div>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer" style="background:var(--bg-surface); border-top:1px solid var(--border-color); padding:40px 0; margin-top:60px;">
    <div class="home-container" style="display:flex; flex-direction:column; align-items:center; text-align:center; gap:12px;">
      <p style="margin:0; font-size:0.9rem; color:var(--text-secondary);">
        <strong>MockTestVault.com</strong> — 100% Free Educational Practice & Board Exam Simulators.
      </p>
      <p style="margin:0; font-size:0.78rem; color:var(--text-muted); max-width:680px;">
        Distraction-Free Computer-Based Testing. Aligned with official Central Board of Secondary Education (CBSE) syllabus specifications. CBSE® is a registered trademark of the Central Board of Secondary Education.
      </p>
      <div style="display:flex; gap:16px; font-size:0.8rem; margin-top:8px;">
        <a href="../../about.html" style="color:var(--text-secondary); text-decoration:none;">About</a>
        <a href="../../privacy.html" style="color:var(--text-secondary); text-decoration:none;">Privacy Policy</a>
        <a href="../../terms.html" style="color:var(--text-secondary); text-decoration:none;">Terms of Service</a>
        <a href="../../disclaimer.html" style="color:var(--text-secondary); text-decoration:none;">Disclaimer</a>
        <a href="../../contact.html" style="color:var(--text-secondary); text-decoration:none;">Contact Desk</a>
      </div>
    </div>
  </footer>

</body>
</html>
"""

hub_file = os.path.join(RUNNER_DIR, "index.html")
with open(hub_file, "w", encoding="utf-8") as f:
    f.write(hub_html)
print("Generated sample-papers/index.html")

print("✓ All CBSE Class 10 Full 80-Mark Mock Runners and Hub generated successfully!")
