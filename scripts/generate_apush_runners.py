#!/usr/bin/env python3
"""
AP® U.S. History (APUSH) Runner HTML Generator
Generates the 6 production runners for the US Pillar:
- us/ap/us-history-diagnostic-01.html
- us/ap/us-history-diagnostic-02.html
- us/ap/us-history-diagnostic-03.html
- us/ap/us-history-diagnostic-04.html
- us/ap/us-history-diagnostic-05.html
- us/ap/us-history-diagnostic-random.html
"""

import os

RUNNER_DIR = os.path.join(os.path.dirname(__file__), "..", "us", "ap")
os.makedirs(RUNNER_DIR, exist_ok=True)

modules = [
    {
        "filename": "us-history-diagnostic-01.html",
        "set_key": "set1",
        "title": "AP® U.S. History Diagnostic 01 (Periods 1 & 2: 1491–1754) | MockTestVault US",
        "desc": "Free timed AP U.S. History diagnostic test 01 (20 Multiple Choice Questions) covering Pre-Columbian societies, Columbian Exchange, and European colonization.",
        "badge_text": "AP® U.S. History Set 01 (1491–1754)",
        "print_sub": "Official College Board AP® CED Specification: Periods 1 & 2 (1491–1754) | mocktestvault.com",
        "breadcrumb": "AP® U.S. History Set 01 (1491–1754)",
        "next_url": "us-history-diagnostic-02.html",
        "next_label": "Take AP U.S. History Set 02 (1754–1848) →",
        "next_icon": "📜"
    },
    {
        "filename": "us-history-diagnostic-02.html",
        "set_key": "set2",
        "title": "AP® U.S. History Diagnostic 02 (Periods 3 & 4: 1754–1848) | MockTestVault US",
        "desc": "Free timed AP U.S. History diagnostic test 02 (20 Multiple Choice Questions) covering the American Revolution, Constitution, Early Republic, and Market Revolution.",
        "badge_text": "AP® U.S. History Set 02 (1754–1848)",
        "print_sub": "Official College Board AP® CED Specification: Periods 3 & 4 (1754–1848) | mocktestvault.com",
        "breadcrumb": "AP® U.S. History Set 02 (1754–1848)",
        "next_url": "us-history-diagnostic-03.html",
        "next_label": "Take AP U.S. History Set 03 (1844–1898) →",
        "next_icon": "⚔️"
    },
    {
        "filename": "us-history-diagnostic-03.html",
        "set_key": "set3",
        "title": "AP® U.S. History Diagnostic 03 (Periods 5 & 6: 1844–1898) | MockTestVault US",
        "desc": "Free timed AP U.S. History diagnostic test 03 (20 Multiple Choice Questions) covering Manifest Destiny, Civil War, Reconstruction, and Gilded Age Industrialization.",
        "badge_text": "AP® U.S. History Set 03 (1844–1898)",
        "print_sub": "Official College Board AP® CED Specification: Periods 5 & 6 (1844–1898) | mocktestvault.com",
        "breadcrumb": "AP® U.S. History Set 03 (1844–1898)",
        "next_url": "us-history-diagnostic-04.html",
        "next_label": "Take AP U.S. History Set 04 (1890–1980) →",
        "next_icon": "⛓️"
    },
    {
        "filename": "us-history-diagnostic-04.html",
        "set_key": "set4",
        "title": "AP® U.S. History Diagnostic 04 (Periods 7 & 8: 1890–1980) | MockTestVault US",
        "desc": "Free timed AP U.S. History diagnostic test 04 (20 Multiple Choice Questions) covering Imperialism, WWI, New Deal, WWII, Cold War, and Civil Rights Movement.",
        "badge_text": "AP® U.S. History Set 04 (1890–1980)",
        "print_sub": "Official College Board AP® CED Specification: Periods 7 & 8 (1890–1980) | mocktestvault.com",
        "breadcrumb": "AP® U.S. History Set 04 (1890–1980)",
        "next_url": "us-history-diagnostic-05.html",
        "next_label": "Take AP U.S. History Set 05 (1980–Present) →",
        "next_icon": "🏭"
    },
    {
        "filename": "us-history-diagnostic-05.html",
        "set_key": "set5",
        "title": "AP® U.S. History Diagnostic 05 (Period 9 & Thematic Review: 1980–Present) | MockTestVault US",
        "desc": "Free timed AP U.S. History diagnostic test 05 (20 Multiple Choice Questions) covering Reagan Revolution, Post-Cold War, 21st Century, and Thematic Synthesis.",
        "badge_text": "AP® U.S. History Set 05 (1980–Present)",
        "print_sub": "Official College Board AP® CED Specification: Period 9 & Thematic Review (1980–Present) | mocktestvault.com",
        "breadcrumb": "AP® U.S. History Set 05 (1980–Present)",
        "next_url": "us-history-diagnostic-random.html",
        "next_label": "Take Dynamic Random 20-Q Mock →",
        "next_icon": "🎲"
    },
    {
        "filename": "us-history-diagnostic-random.html",
        "set_key": "random",
        "title": "AP® U.S. History Dynamic Random Mock Test (Periods 1–9) | MockTestVault US",
        "desc": "Free timed AP U.S. History dynamic random mock test. Samples 20 randomized stimulus-based questions across all 9 historical periods (1491–Present) from our 100-question pool.",
        "badge_text": "AP® U.S. History 🎲 Random Shuffled Mock",
        "print_sub": "Official College Board AP® CED Specification: Dynamic Random 20-Q Mock (Periods 1–9) | mocktestvault.com",
        "breadcrumb": "AP® U.S. History 🎲 Random Mock",
        "next_url": "us-history-diagnostic-01.html",
        "next_label": "Start Over: Take AP U.S. History Set 01 →",
        "next_icon": "📜"
    }
]

set_links = [
    ("us-history-diagnostic-01.html", "set1", "Set 01 (1491–1754)", "20 Qs"),
    ("us-history-diagnostic-02.html", "set2", "Set 02 (1754–1848)", "20 Qs"),
    ("us-history-diagnostic-03.html", "set3", "Set 03 (1844–1898)", "20 Qs"),
    ("us-history-diagnostic-04.html", "set4", "Set 04 (1890–1980)", "20 Qs"),
    ("us-history-diagnostic-05.html", "set5", "Set 05 (1980–Pres)", "20 Qs"),
]

def render_switcher(active_key):
    lines = []
    lines.append('      <span class="set-label">AP® U.S. History 100-Question Modules:</span>')
    lines.append('      <div class="set-btn-group" role="tablist">')
    for href, key, name, badge in set_links:
        is_active = (key == active_key)
        cls = "set-btn active" if is_active else "set-btn"
        sel = "true" if is_active else "false"
        lines.append(f'        <a href="{href}" class="{cls}" role="tab" aria-selected="{sel}">')
        lines.append(f'          <span>{name}</span>')
        lines.append(f'          <span class="set-badge-count">{badge}</span>')
        lines.append('        </a>')
    
    # Random button
    is_rand_active = (active_key == "random")
    rand_cls = "set-btn random-btn active" if is_rand_active else "set-btn random-btn"
    rand_sel = "true" if is_rand_active else "false"
    lines.append(f'        <a href="us-history-diagnostic-random.html" class="{rand_cls}" role="tab" aria-selected="{rand_sel}" data-set="random">')
    lines.append('          <span>🎲 Random 20-Q Mock</span>')
    lines.append('          <span class="set-badge-count">Shuffled</span>')
    lines.append('        </a>')
    lines.append('      </div>')
    return "\n".join(lines)

template = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">

  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{title_clean}",
    "description": "{desc}",
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
    <h1>MockTestVault US — {badge_text}</h1>
    <p>{print_sub}</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">🇺🇸</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">AP® U.S. History</span></h1>
          <p>Advanced Placement Examination Simulator (100 Questions Vault)</p>
        </div>
      </a>

      <div class="header-controls">
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant step-by-step rationales & citations">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Official 45-minute AP Section I simulation">
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
      <span class="current">{breadcrumb}</span>
    </div>
  </nav>

  <!-- Section Info Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
{switcher_html}
    </div>
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">45:00</span>
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
        <span class="badge badge-chapter">AP® U.S. History</span>
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
          <span>💡 College Board Historical Analysis & Rationale</span>
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
      <a href="{next_url}" class="nav-btn" style="text-decoration:none; background:var(--primary); color:#fff;">
        <span>{next_icon}</span> {next_label}
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
        initialSet: '{set_key}',
        timeLimitMinutes: 45,
        randomSampleSize: 20,
        markingScheme: {{ correct: 1, wrong: 0 }},
        examType: 'ap',
        setSources: {{
          set1: '../../data/us/ap/ap_us_history_set1.json',
          set2: '../../data/us/ap/ap_us_history_set2.json',
          set3: '../../data/us/ap/ap_us_history_set3.json',
          set4: '../../data/us/ap/ap_us_history_set4.json',
          set5: '../../data/us/ap/ap_us_history_set5.json'
        }}
      }});
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>
"""

for mod in modules:
    switcher_html = render_switcher(mod["set_key"])
    title_clean = mod["title"].split("|")[0].strip()
    rendered = template.format(
        title=mod["title"],
        title_clean=title_clean,
        desc=mod["desc"],
        badge_text=mod["badge_text"],
        print_sub=mod["print_sub"],
        breadcrumb=mod["breadcrumb"],
        switcher_html=switcher_html,
        next_url=mod["next_url"],
        next_icon=mod["next_icon"],
        next_label=mod["next_label"],
        set_key=mod["set_key"]
    )
    filepath = os.path.join(RUNNER_DIR, mod["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"Generated {mod['filename']}")

print("All 6 AP US History runners created successfully!")
