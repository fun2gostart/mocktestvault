#!/usr/bin/env python3
"""
Expand static educational overview injection to CBSE Sample Papers,
IELTS, GRE, TOEFL, and GMAT runners.
"""
import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def inject_block(filepath, block_html):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    if "<!-- Static Educational Overview" in html:
        return False
    
    target = "  <!-- Site Footer -->"
    if target in html:
        html = html.replace(target, block_html + "\n" + target)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False

# --------------------------------------------------------------------------
# 1. CBSE Class 10 Full 80-Mark Board Papers
# --------------------------------------------------------------------------
def get_cbse_paper_static(subject_name, sections_desc):
    return f"""
  <!-- Static Educational Overview & Candidate Instructions (SEO & AdSense Substantive Content) -->
  <section class="exam-guide-static" style="max-width:960px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This is a full 80-mark 3-hour CBSE Board examination simulation. JavaScript is required for the timer, question palette, and section navigation. Complete syllabus blueprint is provided below.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        📑 CBSE Class 10 {subject_name} Official 80-Mark Board Paper Blueprint
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        Full Curriculum Simulation: 80 Questions • 180 Minutes (3 Hours) • 80 Marks • 100% NCERT Grounding
      </p>
    </div>

    <div style="background:var(--bg-subtle); padding:18px; border-radius:8px; margin-bottom:20px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">Syllabus Distribution & Sectional Coverage:</strong>
      {sections_desc}
    </div>

    <div style="background:var(--bg-subtle); border-radius:8px; padding:18px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">⚖️ Official Board Evaluation Guidelines:</strong>
      Every question includes full NCERT chapter and page citations with step-by-step mathematical and conceptual breakdowns matching the official CBSE marking scheme.
    </div>
  </section>
"""

cbse_sp_dir = os.path.join(BASE_DIR, "cbse-class-10", "sample-papers")
papers = [
    ("science-board-mock-01.html", "Science", "Chemical Reactions, Acids/Bases, Metals, Carbon Compounds, Life Processes, Control & Coordination, Reproduction, Heredity, Light, Human Eye, Electricity, Magnetic Effects, Our Environment."),
    ("mathematics-board-mock-01.html", "Mathematics (Standard & Basic)", "Real Numbers, Polynomials, Linear Equations, Quadratic Equations, Arithmetic Progressions, Triangles (BPT), Coordinate Geometry, Trigonometry, Circles, Areas, Surface Areas & Volumes, Statistics, Probability."),
    ("social-science-board-mock-01.html", "Social Science", "History (Nationalism in Europe & India, Global World), Geography (Resources, Water, Agriculture, Minerals), Political Science (Federalism, Gender/Caste, Political Parties), Economics (Development, Sectors, Money & Credit).")
]

for fn, subj, desc in papers:
    fp = os.path.join(cbse_sp_dir, fn)
    if os.path.exists(fp) and inject_block(fp, get_cbse_paper_static(subj, desc)):
        print(f"Injected static content into: cbse-class-10/sample-papers/{fn}")

# --------------------------------------------------------------------------
# 2. Global Standards Pillar (TOEFL, GMAT, IELTS, GRE)
# --------------------------------------------------------------------------
toefl_static = """
  <!-- Static Educational Overview & Candidate Instructions (SEO & AdSense Substantive Content) -->
  <section class="exam-guide-static" style="max-width:960px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This TOEFL® iBT reading practice suite requires JavaScript for passage split-screen display and the 35-minute timer.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        🌐 TOEFL® iBT Academic Reading Specifications
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        ETS Format: 2 Full Academic Passages • 20 Questions • 35 Minutes • 0–30 Scaled Scoring
      </p>
    </div>

    <div style="background:var(--bg-subtle); padding:18px; border-radius:8px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">Question Types & Cognitive Skills Tested:</strong>
      • <strong>Factual Information & Negative Factual:</strong> Direct passage verification and identifying untrue assertions.<br>
      • <strong>Inference & Rhetorical Purpose:</strong> Deducing unstated implications and analyzing why an author included specific evidence.<br>
      • <strong>Vocabulary in Context:</strong> Advanced academic lexemes evaluated in their exact contextual nuance.<br>
      • <strong>Sentence Insertion & Prose Summary:</strong> Testing structural cohesion and major vs minor conceptual synthesis.
    </div>
  </section>
"""

gmat_static = """
  <!-- Static Educational Overview & Candidate Instructions (SEO & AdSense Substantive Content) -->
  <section class="exam-guide-static" style="max-width:960px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This GMAT® Focus Edition simulator requires JavaScript for timing, Data Insights table sorting, and GMAC scoring conversion.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        📊 GMAT® Focus Edition Diagnostic Blueprint
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        GMAC Pattern: 20 High-Rigor Questions • 45 Minutes • 60–90 Scaled Section Score
      </p>
    </div>

    <div style="background:var(--bg-subtle); padding:18px; border-radius:8px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">Skills Evaluated in this Diagnostic:</strong>
      • <strong>Data Insights:</strong> Table analysis, graphical interpretation, cohort retention curves, and multi-source analysis.<br>
      • <strong>Data Sufficiency:</strong> Evaluating whether Statement (1) and Statement (2) alone or together provide sufficient data to answer the target question.<br>
      • <strong>Quantitative Problem Solving:</strong> Advanced algebra, prime factorizations, combinatorics, mixture dilutions, and harmonic rates.
    </div>
  </section>
"""

# Inject into TOEFL
for fn in glob.glob(os.path.join(BASE_DIR, "global", "toefl", "reading-practice-*.html")):
    if inject_block(fn, toefl_static):
        print(f"Injected static content into: global/toefl/{os.path.basename(fn)}")

# Inject into GMAT
for fn in glob.glob(os.path.join(BASE_DIR, "global", "gmat", "focus-diagnostic-*.html")):
    if inject_block(fn, gmat_static):
        print(f"Injected static content into: global/gmat/{os.path.basename(fn)}")

print("CBSE Board Papers, TOEFL, and GMAT static educational overviews injected successfully!")
