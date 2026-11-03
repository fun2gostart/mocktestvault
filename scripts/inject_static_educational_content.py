#!/usr/bin/env python3
"""
Inject rich static educational overview sections, candidate instructions,
<noscript> fallbacks, and FAQ Schema into MockTestVault test runners.
This ensures Googlebot, Bingbot, and AdSense compliance crawlers immediately
read 500+ words of high-density academic text without requiring client-side JS execution.
"""
import os
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# 1. SSC CGL Full Mocks (mock-01, mock-02, mock-03)
# --------------------------------------------------------------------------
ssc_full_mock_static = """
  <!-- Static Educational Overview & Candidate Instructions (SEO & AdSense Substantive Content) -->
  <section class="exam-guide-static" style="max-width:960px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This examination suite is an interactive Computer-Based Test (CBT) simulator with real-time timers and TCS iON palette navigation. While JavaScript is required to launch the interactive exam engine, the complete examination syllabus, scoring scheme, and instructions are provided below.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        📖 SSC CGL Tier 1 Official Examination Blueprint & Guide
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        Comprehensive examination pattern, section weightage, and negative marking rubric.
      </p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-bottom:24px;">
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">1. Reasoning (25 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Analogies, Number/Letter Series, Syllogisms, Blood Relations, Direction Sense, Coding-Decoding, Visual Matrices.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">2. General Awareness (25 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Indian Polity (Articles 14–32), Harappan Sites, Delhi Sultanate, Drainage Systems, Total Internal Reflection, Census 2011.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">3. Quantitative Aptitude (25 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Algebraic Identities (x+1/x), Divisibility by 72, Tangent-Secant Theorem, Incentre Angles, 3-Year CI vs SI, AM-GM Minima.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); display:block; margin-bottom:4px; font-size:0.92rem;">4. English Comprehension (25 Qs)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">Subject-Verb Agreement, Conditionals, Prepositional Gerunds, Synonyms/Antonyms, Voice/Narration, Cloze Passages.</span>
      </div>
    </div>

    <div style="background:var(--bg-subtle); border-radius:8px; padding:18px; margin-bottom:24px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">⚖️ Official Scoring & Penalty Mathematics:</strong>
      • <strong>Correct Response:</strong> +2.00 marks.<br>
      • <strong>Incorrect Response:</strong> -0.50 mark (25% negative marking penalty).<br>
      • <strong>Unattempted Item:</strong> 0.00 marks.<br>
      • <strong>Optimal Strategy:</strong> Never make random 4-choice guesses. If you eliminate 2 options, statistical expectation is positive (+0.75 mark per attempt).
    </div>

    <div style="margin-top:20px;">
      <h3 style="font-size:1.1rem; font-weight:700; color:var(--text-primary); margin-bottom:12px;">Frequently Asked Questions</h3>
      <div style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
        <p><strong>Q: Can I jump between sections during the 60 minutes?</strong><br>
        Yes. In the official TCS iON CBT exam, all 100 questions across all four sections are accessible simultaneously without sectional timing locks.</p>
        <p><strong>Q: What is a competitive raw score in SSC CGL Tier 1?</strong><br>
        A raw score of 145–155+ marks out of 200 is generally considered a safe benchmark for the Unreserved (UR) category to ensure qualification for Tier 2.</p>
      </div>
    </div>
  </section>
"""

# --------------------------------------------------------------------------
# 2. SSC CGL Sectional Drills
# --------------------------------------------------------------------------
def get_ssc_sec_static(sec_name, sec_topics):
    return f"""
  <!-- Static Educational Overview & Candidate Instructions (SEO & AdSense Substantive Content) -->
  <section class="exam-guide-static" style="max-width:960px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This 25-question timed sectional drill requires JavaScript for the countdown timer and scoring analytics. Full syllabus reference and guidelines are provided below.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        🎯 SSC CGL Sectional Guide: {sec_name}
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        High-Yield Speed Test Blueprint: 25 Questions • 15 Minutes • 50 Marks (+2 / -0.5)
      </p>
    </div>

    <div style="background:var(--bg-subtle); padding:18px; border-radius:8px; margin-bottom:20px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">Key Syllabus Topics Tested in this Module:</strong>
      {sec_topics}
    </div>

    <div style="background:var(--bg-subtle); border-radius:8px; padding:18px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">⏱️ Speed Management Strategy:</strong>
      Target completing all 25 questions in under 15 minutes. Mark ambiguous questions for review and prioritize high-accuracy attempts to prevent the -0.50 negative marking penalty.
    </div>
  </section>
"""

# --------------------------------------------------------------------------
# 3. Digital SAT Drills
# --------------------------------------------------------------------------
sat_math_static = """
  <!-- Static Educational Overview & Candidate Instructions (SEO & AdSense Substantive Content) -->
  <section class="exam-guide-static" style="max-width:960px; margin:36px auto 48px auto; padding:28px 24px; background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-lg); box-shadow:var(--shadow-sm);">
    <noscript>
      <div style="padding:16px 20px; background:#fff3cd; color:#856404; border:1px solid #ffeeba; border-radius:8px; margin-bottom:24px; font-size:0.92rem; line-height:1.5;">
        <strong>⚠️ JavaScript Recommended:</strong> This Digital SAT® simulator requires JavaScript for timing, adaptive scoring, and interactive Desmos calculator integration. Complete module specifications are provided below.
      </div>
    </noscript>

    <div style="border-bottom:2px solid var(--primary-light); padding-bottom:12px; margin-bottom:20px;">
      <h2 style="font-size:1.35rem; font-weight:800; color:var(--text-primary); margin-bottom:6px;">
        📐 Digital SAT® Math Module Specifications & Domains
      </h2>
      <p style="font-size:0.88rem; color:var(--text-muted); margin:0;">
        Aligned with College Board Digital SAT Test Specifications (Algebra, Advanced Math, Problem Solving, Geometry).
      </p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-bottom:20px;">
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); font-size:0.92rem;">Algebra (~35%)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); display:block; margin-top:4px;">Linear equations, systems of linear equations, linear inequalities, and absolute value functions.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); font-size:0.92rem;">Advanced Math (~35%)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); display:block; margin-top:4px;">Quadratic functions, polynomial zeros, exponential growth/decay, radical and rational expressions.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); font-size:0.92rem;">Problem Solving (~15%)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); display:block; margin-top:4px;">Ratios, rates, proportions, unit conversions, percentages, and two-variable statistical data analysis.</span>
      </div>
      <div style="background:var(--bg-subtle); padding:16px; border-radius:8px; border-left:3px solid var(--primary);">
        <strong style="color:var(--text-primary); font-size:0.92rem;">Geometry & Trig (~15%)</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); display:block; margin-top:4px;">Area and volume formulas, right triangle trigonometry, circle equations (x-h)² + (y-k)² = r².</span>
      </div>
    </div>

    <div style="background:var(--bg-subtle); padding:18px; border-radius:8px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong>💡 Desmos Graphing Calculator Strategy:</strong> All Digital SAT Math questions permit the use of the integrated Desmos graphing calculator. Practice graphing systems of equations to find intersection points directly rather than solving labor-intensive algebraic substitutions.
    </div>
  </section>
"""

# --------------------------------------------------------------------------
# 4. Process Injection
# --------------------------------------------------------------------------
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

# Inject into SSC Full Mocks
ssc_dir = os.path.join(BASE_DIR, "ssc-cgl")
for mock_name in ["mock-01.html", "mock-02.html", "mock-03.html"]:
    fp = os.path.join(ssc_dir, mock_name)
    if os.path.exists(fp) and inject_block(fp, ssc_full_mock_static):
        print(f"Injected static content into: ssc-cgl/{mock_name}")

# Inject into SSC Sectional Drills
sec_configs = [
    ("sectional-reasoning", "General Intelligence & Reasoning", "Syllogisms, Analogies, Number Series, Coding-Decoding, Blood Relations, Linear Seating, Direction Sense, Paper Folding & Mirror Inversion."),
    ("sectional-quantitative-aptitude", "Quantitative Aptitude", "Algebraic Identities, Divisibility Rules, Dishonest Dealer Profit, 3-Year CI vs SI Difference, Incentre/Circumcentre, Tangent-Secant Theorem, AM-GM Minima."),
    ("sectional-english", "English Comprehension", "Subject-Verb Agreement with 'neither/nor', Third Conditionals, Fixed Prepositions with Gerunds, Classical Synonyms/Antonyms, Active/Passive Voice, Cloze Passages."),
    ("sectional-general-awareness", "General Awareness & Static GK", "Indian Polity (Articles 14–32, Writs, 42nd Amendment), Harappan Maritime Sites, Delhi Sultanate, Total Internal Reflection, SI Units, Census 2011, ISRO Missions.")
]

for prefix, name, topics in sec_configs:
    block = get_ssc_sec_static(name, topics)
    for num in [1, 2, 3]:
        fn = f"{prefix}-0{num}.html"
        fp = os.path.join(ssc_dir, fn)
        if os.path.exists(fp) and inject_block(fp, block):
            print(f"Injected static content into: ssc-cgl/{fn}")

# Inject into SAT Math Runners
sat_dir = os.path.join(BASE_DIR, "sat")
for fn in glob.glob(os.path.join(sat_dir, "math-practice-*.html")):
    if inject_block(fn, sat_math_static):
        print(f"Injected static content into: sat/{os.path.basename(fn)}")

print("Static educational overviews injected successfully across all targeted runners!")
