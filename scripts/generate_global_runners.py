import os

os.makedirs('mocktestvault.com/global/ielts', exist_ok=True)
os.makedirs('mocktestvault.com/global/gre', exist_ok=True)

# -------------------------------------------------------------
# 1. IELTS RUNNERS (Drill 01, Drill 02, Drill 03, Random Mock)
# -------------------------------------------------------------
ielts_modules = [
    {
        "filename": "reading-practice-01.html",
        "set_key": "1",
        "title": "IELTS® Academic Reading Practice Test 01: Biophilic Cities & Marine Acoustics | MockTestVault",
        "quiz_name": "IELTS® Academic Reading Practice Test 01",
        "desc": "Timed Cambridge-style IELTS Academic Reading practice drill featuring True/False/Not Given, Heading Matching, Summary Completion, and Lexical Resource targeting Band 7.5 to 9.0.",
        "badge_title": "Drill 01 (Biophilic Architecture & Acoustics)",
        "active_idx": 1
    },
    {
        "filename": "reading-practice-02.html",
        "set_key": "2",
        "title": "IELTS® Academic Reading Practice Test 02: Early Agriculture & Deep-Sea Minerals | MockTestVault",
        "quiz_name": "IELTS® Academic Reading Practice Test 02",
        "desc": "Official-style IELTS Academic Reading practice test featuring Fertile Crescent agriculture, polymetallic seabed nodules, and neuroplasticity in bilinguals.",
        "badge_title": "Drill 02 (Agriculture, Ocean Minerals & Cognition)",
        "active_idx": 2
    },
    {
        "filename": "reading-practice-03.html",
        "set_key": "3",
        "title": "IELTS® Academic Reading Practice Test 03: Cryptography, Cryosphere & Biomimetics | MockTestVault",
        "quiz_name": "IELTS® Academic Reading Practice Test 03",
        "desc": "High-percentile IELTS Academic Reading practice test featuring the Voynich Manuscript, polar albedo feedback mechanisms, and gecko dry adhesion biomimetics.",
        "badge_title": "Drill 03 (Voynich, Cryosphere & Biomimetics)",
        "active_idx": 3
    },
    {
        "filename": "reading-practice-random.html",
        "set_key": "random",
        "title": "IELTS® Academic Reading Dynamic Shuffled 20-Q Mock Test | MockTestVault",
        "quiz_name": "IELTS® Academic Reading Dynamic Shuffled Mock Test",
        "desc": "Take a freshly randomized 20-question IELTS Academic Reading mock test drawn dynamically from our 60-question verified question pool. Retake anytime for new questions.",
        "badge_title": "Random 20-Q Shuffled Mock",
        "active_idx": 4
    }
]

ielts_switcher_items = [
    ("reading-practice-01.html", "📖 Drill 01 (Architecture/Acoustics)", "20 Qs • 25M", False),
    ("reading-practice-02.html", "🌾 Drill 02 (Agriculture/Seabed/Neuro)", "20 Qs • 25M", False),
    ("reading-practice-03.html", "📜 Drill 03 (Voynich/Cryosphere/Biomim)", "20 Qs • 25M", False),
    ("reading-practice-random.html", "🎲 Random 20-Q Mock", "Shuffled", True)
]

def render_ielts_runner(cfg):
    switcher_btns = []
    for fn, label, meta, is_rand in ielts_switcher_items:
        is_active = (fn == cfg["filename"])
        active_cls = " active" if is_active else ""
        rand_cls = " random-btn" if is_rand else ""
        data_set_attr = ' data-set="random"' if is_rand else ''
        aria_sel = "true" if is_active else "false"
        switcher_btns.append(f"""        <a href="{fn}" class="set-btn{rand_cls}{active_cls}" role="tab" aria-selected="{aria_sel}"{data_set_attr}>
          <span>{label}</span>
          <span class="set-badge-count">{meta}</span>
        </a>""")
    switcher_html = "\n".join(switcher_btns)

    initial_set = "random" if cfg["set_key"] == "random" else f"set{cfg['set_key']}"

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cfg['title']}</title>
  <meta name="description" content="{cfg['desc']}">
  <link rel="canonical" href="https://mocktestvault.com/global/ielts/{cfg['filename']}">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{cfg['quiz_name']}",
    "description": "{cfg['desc']}",
    "educationalLevel": "International English Proficiency (CEFR C1/C2)",
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
    <h1>MockTestVault Global — {cfg['quiz_name']}</h1>
    <p>International Standard: True/False/Not Given, Heading Matching, Lexical Resource | mocktestvault.com</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">🌐</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">IELTS® Academic</span></h1>
          <p>Global English & International Standards</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant Band 9 text justifications and vocabulary breakdown">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Timed 25-min authentic IELTS simulation">
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
      <a href="../index.html">Global Exam Vault</a>
      <span class="sep">/</span>
      <span class="current">{cfg['badge_title']}</span>
    </div>
  </nav>

  <!-- Multi-Set Selector Bar (60 Total Questions) -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">IELTS Academic Track (60 Qs):</span>
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
        <span id="timer-display">25:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading IELTS academic passages...</span>
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
        <span class="badge badge-chapter">IELTS® Academic</span>
        <span class="badge badge-subtopic" id="q-subtopic-badge">Academic Reading</span>
        <span class="badge badge-subtopic" id="q-diff-badge">Band 7.5+</span>
      </div>

      <div class="question-text-box">
        <div class="question-number" id="q-number">Question 1</div>
        <div class="question-title" id="q-title">Loading passage and question text...</div>
      </div>

      <!-- Interactive Options -->
      <div class="options-list" id="options-list" role="radiogroup"></div>

      <!-- Band 9 Justification Box -->
      <div class="explanation-box" id="explanation-box" style="display:none;">
        <div class="explanation-header">
          <span>💡 Band 9 Reading Justification & Lexical Analysis:</span>
          <span class="citation-tag" id="citation-tag">Cambridge IELTS Framework</span>
        </div>
        <div class="explanation-text" id="explanation-text"></div>
      </div>

      <!-- Navigation & Response Controls -->
      <div class="card-action-bar">
        <div class="action-left">
          <button id="btn-review" class="nav-btn btn-review">
            <span>🚩</span> Mark for Review
          </button>
          <button id="btn-clear" class="nav-btn btn-clear">
            Clear Choice
          </button>
        </div>

        <div class="action-right">
          <button id="btn-prev" class="nav-btn btn-secondary">
            ← Previous
          </button>
          <button id="btn-next" class="nav-btn btn-primary">
            Next Question →
          </button>
          <button id="btn-submit" class="nav-btn btn-submit-test" style="display:none;">
            <span>🏁</span> Submit Test
          </button>
        </div>
      </div>
    </section>

    <!-- Right Column: Interactive CBT Palette -->
    <aside class="palette-card" aria-label="Question Navigator">
      <div class="palette-header">
        <h3>Question Palette</h3>
        <span class="palette-counter" id="palette-summary">20 Questions</span>
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
          <span>🏁</span> Submit Drill & Scorecard
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
      <p style="font-size:0.75rem;">100% Free & Distraction-Free. Aligned with official Cambridge IELTS® standards. IELTS® is a registered trademark of the University of Cambridge, the British Council, and IDP Education Australia, which are not affiliated with this website.</p>
    </div>
  </footer>

  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: '{initial_set}',
        timeLimitMinutes: 25,
        randomSampleSize: 20,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'ielts',
        setSources: {{
          set1: '../../data/global/ielts/ielts_reading_set1.json',
          set2: '../../data/global/ielts/ielts_reading_set2.json',
          set3: '../../data/global/ielts/ielts_reading_set3.json'
        }}
      }});
    }});
  </script>
</body>
</html>"""

for mod in ielts_modules:
    path = os.path.join('mocktestvault.com/global/ielts', mod['filename'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(render_ielts_runner(mod))
    print(f"Generated IELTS runner: {path}")


# -------------------------------------------------------------
# 2. GRE RUNNERS (Quant Diagnostic 01 & Verbal Diagnostic 01)
# -------------------------------------------------------------
gre_suites = [
    {
        "filename": "quantitative-reasoning-01.html",
        "title": "GRE® Quantitative Reasoning Diagnostic Drill 01 (20 Questions) | MockTestVault",
        "quiz_name": "GRE® Quantitative Reasoning Diagnostic Test 01",
        "desc": "Official-style GRE Quantitative Reasoning timed diagnostic featuring Quantitative Comparison, Problem Solving, Data Interpretation, and 130–170 scaled scoring.",
        "badge_title": "Quantitative Reasoning Drill 01",
        "track": "Quantitative Reasoning",
        "time_mins": 35,
        "json_source": "../../data/global/gre/gre_quant_set1.json",
        "meta_label": "20 Qs • 35 Mins • 130-170 Scale"
    },
    {
        "filename": "verbal-reasoning-01.html",
        "title": "GRE® Verbal Reasoning Diagnostic Drill 01 (20 Questions) | MockTestVault",
        "quiz_name": "GRE® Verbal Reasoning Diagnostic Test 01",
        "desc": "Official-style GRE Verbal Reasoning timed diagnostic featuring Text Completion, Sentence Equivalence, Reading Comprehension, and 130–170 scaled scoring.",
        "badge_title": "Verbal Reasoning Drill 01",
        "track": "Verbal Reasoning",
        "time_mins": 30,
        "json_source": "../../data/global/gre/gre_verbal_set1.json",
        "meta_label": "20 Qs • 30 Mins • 130-170 Scale"
    }
]

def render_gre_runner(suite):
    is_quant = "quantitative" in suite["filename"]
    quant_active = " active" if is_quant else ""
    quant_sel = "true" if is_quant else "false"
    verb_active = " active" if not is_quant else ""
    verb_sel = "true" if not is_quant else "false"

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{suite['title']}</title>
  <meta name="description" content="{suite['desc']}">
  <link rel="canonical" href="https://mocktestvault.com/global/gre/{suite['filename']}">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{suite['quiz_name']}",
    "description": "{suite['desc']}",
    "educationalLevel": "Higher Education & Graduate Admissions (ETS GRE)",
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
    <h1>MockTestVault Global — {suite['quiz_name']}</h1>
    <p>ETS GRE® General Test Standard: Quantitative Comparison, Text Completion & Etymology | mocktestvault.com</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">🏛️</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">GRE® General</span></h1>
          <p>Graduate Admissions Standardized Simulator</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant official explanations and formula/etymology analysis">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Timed {suite['time_mins']}-min authentic GRE simulation">
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
      <a href="../index.html">Global Exam Vault</a>
      <span class="sep">/</span>
      <span class="current">{suite['badge_title']}</span>
    </div>
  </nav>

  <!-- Multi-Set Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">GRE® General Suites:</span>
      <div class="set-btn-group" role="tablist">
        <a href="quantitative-reasoning-01.html" class="set-btn{quant_active}" role="tab" aria-selected="{quant_sel}">
          <span>📐 Quant Diagnostic 01</span>
          <span class="set-badge-count">20 Qs • 35M</span>
        </a>
        <a href="verbal-reasoning-01.html" class="set-btn{verb_active}" role="tab" aria-selected="{verb_sel}">
          <span>🧠 Verbal Diagnostic 01</span>
          <span class="set-badge-count">20 Qs • 30M</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">{suite['time_mins']}:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading GRE diagnostic questions...</span>
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
        <span class="badge badge-chapter">ETS GRE® General</span>
        <span class="badge badge-subtopic" id="q-subtopic-badge">{suite['track']}</span>
        <span class="badge badge-subtopic" id="q-diff-badge">Graduate Level</span>
      </div>

      <div class="question-text-box">
        <div class="question-number" id="q-number">Question 1</div>
        <div class="question-title" id="q-title">Loading question...</div>
      </div>

      <!-- Interactive Options -->
      <div class="options-list" id="options-list" role="radiogroup"></div>

      <!-- Solution Explanation Box -->
      <div class="explanation-box" id="explanation-box" style="display:none;">
        <div class="explanation-header">
          <span>💡 Official GRE Detailed Solution & Rationale:</span>
          <span class="citation-tag" id="citation-tag">ETS GRE Framework</span>
        </div>
        <div class="explanation-text" id="explanation-text"></div>
      </div>

      <!-- Navigation Controls -->
      <div class="card-action-bar">
        <div class="action-left">
          <button id="btn-review" class="nav-btn btn-review">
            <span>🚩</span> Mark for Review
          </button>
          <button id="btn-clear" class="nav-btn btn-clear">
            Clear Choice
          </button>
        </div>

        <div class="action-right">
          <button id="btn-prev" class="nav-btn btn-secondary">
            ← Previous
          </button>
          <button id="btn-next" class="nav-btn btn-primary">
            Next Question →
          </button>
          <button id="btn-submit" class="nav-btn btn-submit-test" style="display:none;">
            <span>🏁</span> Submit Test
          </button>
        </div>
      </div>
    </section>

    <!-- Right Column: Interactive CBT Palette -->
    <aside class="palette-card" aria-label="Question Navigator">
      <div class="palette-header">
        <h3>Question Palette</h3>
        <span class="palette-counter" id="palette-summary">20 Questions</span>
      </div>

      <div class="palette-grid" id="palette-grid"></div>

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
          <span>🏁</span> Submit Diagnostic & Scorecard
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
      <p style="font-size:0.75rem;">100% Free & Distraction-Free. Aligned with official Educational Testing Service (ETS) GRE® standards. GRE® is a registered trademark of ETS, which is not affiliated with this website.</p>
    </div>
  </footer>

  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: 'set1',
        timeLimitMinutes: {suite['time_mins']},
        randomSampleSize: 20,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'gre',
        setSources: {{
          set1: '{suite['json_source']}'
        }}
      }});
    }});
  </script>
</body>
</html>"""

for suite in gre_suites:
    path = os.path.join('mocktestvault.com/global/gre', suite['filename'])
    with open(path, 'w', encoding='utf-8') as f:
        f.write(render_gre_runner(suite))
    print(f"Generated GRE runner: {path}")

print("All Global Pillar runners generated successfully!")
