#!/usr/bin/env python3
"""
MockTestVault — Master CBSE Class 10 Curriculum Generator (All 48 Chapters)
Generates complete, verified JSON question banks and HTML test runners for:
- Science: 13 Chapters (Chemistry, Biology, Physics)
- Mathematics: 14 Chapters (Number Systems, Algebra, Geometry, Trigonometry, Mensuration, Statistics & Probability)
- Social Science: 21 Chapters (History, Geography, Civics, Economics)

100% Distraction-Free, Authentic CBT Interface, NCERT Grounded, TCS iON 5-State Palette.
"""

import os
import sys
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(SCRIPT_DIR)

import build_full_class10 as bfc
import sst_data as sst

# Directories setup
DATA_BASE = os.path.join(VAULT_DIR, "data", "in", "cbse10")
PAGES_BASE = os.path.join(VAULT_DIR, "cbse-class-10")

DIRS_TO_CREATE = [
    os.path.join(DATA_BASE, "science"),
    os.path.join(DATA_BASE, "mathematics"),
    os.path.join(DATA_BASE, "social-science"),
    os.path.join(PAGES_BASE, "science"),
    os.path.join(PAGES_BASE, "mathematics"),
    os.path.join(PAGES_BASE, "social-science")
]

for d in DIRS_TO_CREATE:
    os.makedirs(d, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. PREPARE ALL 48 CHAPTER DATA OBJECTS
# -----------------------------------------------------------------------------

# --- SCIENCE (13 Chapters) ---
science_chapters = []
for ch in bfc.SCIENCE_CHAPTERS:
    ch_copy = dict(ch)
    # Check if pre-existing rich set exists for ch01, ch02, ch03
    if ch_copy["slug"] == "ch01_chemical_reactions":
        src = os.path.join(DATA_BASE, "science_ch01_chemical_reactions_set1.json")
        if os.path.exists(src):
            with open(src) as f:
                ch_copy["questions"] = json.load(f)
    elif ch_copy["slug"] == "ch02_acids_bases_salts":
        src = os.path.join(DATA_BASE, "science_ch02_acids_bases_salts_set1.json")
        if os.path.exists(src):
            with open(src) as f:
                ch_copy["questions"] = json.load(f)
    elif ch_copy["slug"] == "ch03_metals_non_metals":
        src = os.path.join(DATA_BASE, "science_ch03_metals_non_metals_set1.json")
        if os.path.exists(src):
            with open(src) as f:
                ch_copy["questions"] = json.load(f)
    
    ch_copy["subject"] = "Science"
    ch_copy["subject_slug"] = "science"
    ch_copy["code"] = "086"
    science_chapters.append(ch_copy)

# --- MATHEMATICS (14 Chapters) ---
math_chapters = []
for ch in bfc.MATH_CHAPTERS:
    ch_copy = dict(ch)
    if ch_copy["slug"] == "ch01_real_numbers":
        src = os.path.join(DATA_BASE, "math_ch01_real_numbers_set1.json")
        if os.path.exists(src):
            with open(src) as f:
                ch_copy["questions"] = json.load(f)
    
    ch_copy["subject"] = "Mathematics"
    ch_copy["subject_slug"] = "mathematics"
    ch_copy["code"] = "041"
    math_chapters.append(ch_copy)

# --- SOCIAL SCIENCE (21 Chapters) ---
sst_chapters = []
for ch in sst.SST_CHAPTERS:
    ch_copy = dict(ch)
    ch_copy["subject"] = "Social Science"
    ch_copy["subject_slug"] = "social-science"
    ch_copy["code"] = "087"
    sst_chapters.append(ch_copy)

ALL_SUBJECTS = [
    {"name": "Science", "slug": "science", "code": "086", "chapters": science_chapters},
    {"name": "Mathematics", "slug": "mathematics", "code": "041", "chapters": math_chapters},
    {"name": "Social Science", "slug": "social-science", "code": "087", "chapters": sst_chapters}
]

# -----------------------------------------------------------------------------
# 2. GENERATE JSON QUESTION VAULTS & HTML TEST RUNNERS
# -----------------------------------------------------------------------------

total_questions_generated = 0
total_chapters_generated = 0

for subj in ALL_SUBJECTS:
    sub_name = subj["name"]
    sub_slug = subj["slug"]
    
    for ch in subj["chapters"]:
        ch_slug = ch["slug"]
        ch_num = ch["num"]
        ch_title = ch["title"]
        questions = ch["questions"]
        
        # 1. Write JSON file
        json_filename = f"{ch_slug}.json"
        json_abs_path = os.path.join(DATA_BASE, sub_slug, json_filename)
        json_rel_path = f"data/in/cbse10/{sub_slug}/{json_filename}"
        
        with open(json_abs_path, "w", encoding="utf-8") as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
            
        total_questions_generated += len(questions)
        
        # 2. Write HTML Runner file
        html_filename = f"{ch_slug}.html"
        html_abs_path = os.path.join(PAGES_BASE, sub_slug, html_filename)
        
        html_content = bfc.generate_html_runner(
            subject_name=sub_name,
            subject_slug=sub_slug,
            ch_num=ch_num,
            ch_title=ch_title,
            ch_slug=ch_slug,
            json_rel_path=json_rel_path
        )
        
        with open(html_abs_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        total_chapters_generated += 1

print(f"Generated {total_chapters_generated} chapter test runners and question vaults.")
print(f"Total verified questions across all vaults: {total_questions_generated}")

# -----------------------------------------------------------------------------
# 3. BUILD THE COMPREHENSIVE CBSE CLASS 10 DASHBOARD (index.html)
# -----------------------------------------------------------------------------

def build_dashboard_html():
    def render_cards(chapter_list, sub_slug):
        cards = []
        for ch in chapter_list:
            slug = ch["slug"]
            num = ch["num"]
            title = ch["title"]
            sub_tag = ch.get("sub", "")
            marks = ch.get("marks", "Board Exam")
            desc = ch.get("desc", "")
            q_count = len(ch["questions"])
            tags = f"{sub_slug} {sub_tag.lower()} {title.lower()} {desc.lower()} ch{num} chapter{num}"
            
            card_html = f"""        <a href="{sub_slug}/{slug}.html" class="chapter-card" data-tags="{tags}">
          <div class="card-top-meta">
            <span class="card-sub-tag">{sub_tag}</span>
            <span class="card-weightage">{marks}</span>
          </div>
          <h3 class="card-title">Chapter {num}: {title}</h3>
          <p class="card-desc">{desc}</p>
          <div class="card-footer">
            <span>{q_count} Questions (Live)</span>
            <span>Start Practice →</span>
          </div>
        </a>"""
            cards.append(card_html)
        return "\n\n".join(cards)

    science_cards = render_cards(science_chapters, "science")
    math_cards = render_cards(math_chapters, "mathematics")
    sst_cards = render_cards(sst_chapters, "social-science")

    total_chapters = len(science_chapters) + len(math_chapters) + len(sst_chapters)

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CBSE Class 10 Mock Tests 2026 — Chapter-wise MCQ Practice & Board Exam Simulator | MockTestVault</title>
  <meta name="description" content="Free chapter-wise CBSE Class 10 MCQ mock tests for Science (13 chapters), Mathematics (14 chapters), and Social Science (21 chapters). 100% NCERT aligned with TCS iON 5-state palette, instant explanations, and printable revision sheets.">

  <link rel="stylesheet" href="../css/test-engine.css">

  <style>
    .curriculum-hero {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #f8fafc;
      padding: 48px 24px;
      text-align: center;
      border-bottom: 1px solid var(--border-color);
    }}
    .curriculum-hero h1 {{
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
      color: #ffffff;
    }}
    .curriculum-hero p {{
      font-size: 1.05rem;
      color: #cbd5e1;
      max-width: 760px;
      margin: 0 auto 24px auto;
      line-height: 1.6;
    }}
    .subject-pill-tabs {{
      display: flex;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 24px;
    }}
    .subject-pill {{
      padding: 10px 22px;
      border-radius: 9999px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #f8fafc;
      font-weight: 600;
      font-size: 0.92rem;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .subject-pill:hover,
    .subject-pill.active {{
      background: var(--primary);
      border-color: var(--primary);
      color: white;
      transform: translateY(-2px);
      box-shadow: 0 4px 14px rgba(26, 115, 232, 0.3);
    }}
    .search-filter-box {{
      max-width: 600px;
      margin: 28px auto 0 auto;
      position: relative;
    }}
    .search-filter-box input {{
      width: 100%;
      padding: 14px 20px 14px 46px;
      border-radius: 12px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      background: rgba(255, 255, 255, 0.07);
      color: #ffffff;
      font-size: 1rem;
      outline: none;
      backdrop-filter: blur(8px);
      transition: border-color 0.2s;
    }}
    .search-filter-box input:focus {{
      border-color: var(--primary);
      background: rgba(255, 255, 255, 0.12);
    }}
    .search-filter-box input::placeholder {{
      color: #94a3b8;
    }}
    .search-filter-box span.search-icon {{
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.1rem;
      color: #94a3b8;
    }}
    .catalog-main {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 40px 24px 80px 24px;
    }}
    .subject-block {{
      margin-bottom: 56px;
    }}
    .subject-block-title {{
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--text-color);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--border-color);
    }}
    .chapter-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 20px;
    }}
    .chapter-card {{
      background: var(--bg-surface);
      border: 1.5px solid var(--border-color);
      border-radius: 14px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
      text-decoration: none;
      color: inherit;
    }}
    .chapter-card:hover {{
      border-color: var(--primary);
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }}
    .card-top-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .card-sub-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--bg-body);
      color: var(--text-muted);
      border: 1px solid var(--border-color);
    }}
    .card-weightage {{
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--primary);
    }}
    .card-title {{
      font-size: 1.08rem;
      font-weight: 700;
      color: var(--text-color);
      margin-bottom: 8px;
      line-height: 1.4;
    }}
    .card-desc {{
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 16px;
      flex-grow: 1;
    }}
    .card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
      color: var(--primary);
      font-weight: 600;
      padding-top: 12px;
      border-top: 1px dashed var(--border-color);
    }}
    .hidden-card {{
      display: none !important;
    }}
  </style>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Course",
    "name": "CBSE Class 10 Full Chapter-wise MCQ Practice Catalog",
    "description": "Complete chapter-wise practice tests for Class 10 Science, Mathematics, and Social Science aligned with NCERT syllabus.",
    "provider": {{
      "@type": "Organization",
      "name": "MockTestVault",
      "url": "https://mocktestvault.com"
    }}
  }}
  </script>
</head>
<body>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../index.html" class="brand-link">
        <div class="brand-logo">🛡️</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">CBSE 10</span></h1>
          <p>Official Curriculum Exam Simulator</p>
        </div>
      </a>

      <div class="header-controls">
        <a href="../index.html" class="nav-btn" style="padding:6px 14px; font-size:0.82rem;">
          <span>🏠</span> Home
        </a>
        <button id="theme-toggle-btn" class="theme-toggle-btn" title="Toggle Dark/Light Mode">🌙</button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="curriculum-hero">
    <h1>CBSE Class 10 Board Exam Practice Vault</h1>
    <p>Comprehensive chapter-wise mock tests covering all 48 chapters of the official CBSE Class 10 curriculum. Practice under real-time exam conditions with instant NCERT explanations and TCS iON 5-state tracking.</p>

    <div class="search-filter-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="chapter-search" placeholder="Search by chapter name (e.g. Chemical, Trigonometry, Nationalism, Metals)..." autocomplete="off">
    </div>

    <div class="subject-pill-tabs">
      <a href="#all" class="subject-pill active" data-subject="all">All Chapters ({total_chapters})</a>
      <a href="#block-science" class="subject-pill" data-subject="science">🧪 Science ({len(science_chapters)})</a>
      <a href="#block-mathematics" class="subject-pill" data-subject="mathematics">📐 Mathematics ({len(math_chapters)})</a>
      <a href="#block-social-science" class="subject-pill" data-subject="social-science">🌍 Social Science ({len(sst_chapters)})</a>
    </div>
  </section>

  <!-- Main Catalog Grid -->
  <main class="catalog-main">

    <!-- 1. SCIENCE SECTION (13 Chapters) -->
    <section class="subject-block" id="block-science">
      <h2 class="subject-block-title">
        <span>🧪</span> Class 10 Science (Code 086) — 13 Chapters Complete
      </h2>
      <div class="chapter-grid">
{science_cards}
      </div>
    </section>

    <!-- 2. MATHEMATICS SECTION (14 Chapters) -->
    <section class="subject-block" id="block-mathematics">
      <h2 class="subject-block-title">
        <span>📐</span> Class 10 Mathematics (Code 041 / 241) — 14 Chapters Complete
      </h2>
      <div class="chapter-grid">
{math_cards}
      </div>
    </section>

    <!-- 3. SOCIAL SCIENCE SECTION (21 Chapters) -->
    <section class="subject-block" id="block-social-science">
      <h2 class="subject-block-title">
        <span>🌍</span> Class 10 Social Science (Code 087) — 21 Chapters Complete (History, Geography, Civics, Economics)
      </h2>
      <div class="chapter-grid">
{sst_cards}
      </div>
    </section>

  </main>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <p><strong>MockTestVault.com</strong> — 100% Free Educational Practice & Board Exam Simulators.</p>
      <p style="font-size:0.75rem;">100% Free & Distraction-Free. Aligned with official NCERT CBSE Class 10 standards.</p>
    </div>
  </footer>

  <script>
    // Live Search & Tab Filtering
    const searchInput = document.getElementById('chapter-search');
    const cards = document.querySelectorAll('.chapter-card');
    const tabs = document.querySelectorAll('.subject-pill');
    const subjectBlocks = document.querySelectorAll('.subject-block');

    function filterCatalog() {{
      const query = searchInput.value.toLowerCase().trim();
      const activeTab = document.querySelector('.subject-pill.active')?.dataset.subject || 'all';

      cards.forEach(card => {{
        const tags = (card.dataset.tags || '').toLowerCase();
        const matchesQuery = !query || tags.includes(query);
        const matchesTab = activeTab === 'all' || tags.includes(activeTab);

        if (matchesQuery && matchesTab) {{
          card.classList.remove('hidden-card');
        }} else {{
          card.classList.add('hidden-card');
        }}
      }});

      // Hide empty subject sections
      subjectBlocks.forEach(block => {{
        const visibleCards = block.querySelectorAll('.chapter-card:not(.hidden-card)');
        block.style.display = visibleCards.length > 0 ? 'block' : 'none';
      }});
    }}

    searchInput.addEventListener('input', filterCatalog);

    tabs.forEach(tab => {{
      tab.addEventListener('click', (e) => {{
        e.preventDefault();
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        filterCatalog();
      }});
    }});

    // Theme Toggle
    const themeBtn = document.getElementById('theme-toggle-btn');
    themeBtn.addEventListener('click', () => {{
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('mtv_theme', next);
      themeBtn.textContent = next === 'dark' ? '☀️' : '🌙';
    }});

    const savedTheme = localStorage.getItem('mtv_theme');
    if (savedTheme) {{
      document.documentElement.setAttribute('data-theme', savedTheme);
      themeBtn.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
    }}
  </script>

</body>
</html>
"""

dashboard_html = build_dashboard_html()
dashboard_path = os.path.join(PAGES_BASE, "index.html")
with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(dashboard_html)

print(f"Updated CBSE Class 10 Dashboard at {dashboard_path} with all {total_chapters_generated} chapter links.")
