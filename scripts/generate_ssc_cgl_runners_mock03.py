#!/usr/bin/env python3
"""
Generate SSC CGL Mock 03 HTML runners and update multi-mock switcher bars.
Runners created:
  - ssc-cgl/mock-03.html
  - ssc-cgl/sectional-reasoning-03.html
  - ssc-cgl/sectional-quantitative-aptitude-03.html
  - ssc-cgl/sectional-english-03.html
  - ssc-cgl/sectional-general-awareness-03.html
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SSC_DIR = os.path.join(BASE_DIR, "ssc-cgl")

# --------------------------------------------------------------------------
# 1. Full Mock 03 Runner
# --------------------------------------------------------------------------
with open(os.path.join(SSC_DIR, "mock-02.html"), "r", encoding="utf-8") as f:
    mock2_html = f.read()

# Build 3-mock switcher bar
mock_switcher_3 = """  <!-- Multi-Mock Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">Full Length Mocks:</span>
      <div class="set-btn-group" role="tablist">
        <a href="mock-01.html" class="set-btn" role="tab" aria-selected="false">
          <span>🛡️ Full Mock 01</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
        <a href="mock-02.html" class="set-btn" role="tab" aria-selected="false">
          <span>🛡️ Full Mock 02</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
        <a href="mock-03.html" class="set-btn active" role="tab" aria-selected="true">
          <span>🛡️ Full Mock 03</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
      </div>
    </div>
  </div>"""

# Generate mock-03.html
mock3_html = mock2_html
mock3_html = mock3_html.replace("Mock Test 02", "Mock Test 03")
mock3_html = mock3_html.replace("mock-02.html", "mock-03.html")
mock3_html = mock3_html.replace("cgl_tier1_mock02_full.json", "cgl_tier1_mock03_full.json")
# Replace switcher bar
mock3_html = re.sub(r'<!-- Multi-Mock Selector Bar -->.*?</div>\s*</div>\s*</div>', mock_switcher_3, mock3_html, flags=re.DOTALL)

with open(os.path.join(SSC_DIR, "mock-03.html"), "w", encoding="utf-8") as f:
    f.write(mock3_html)
print("Created: ssc-cgl/mock-03.html")

# Update mock-01.html and mock-02.html switcher bars
def update_full_mock_switcher(filename, active_mock):
    filepath = os.path.join(SSC_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    switcher = f"""  <!-- Multi-Mock Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">Full Length Mocks:</span>
      <div class="set-btn-group" role="tablist">
        <a href="mock-01.html" class="set-btn{' active' if active_mock == 1 else ''}" role="tab" aria-selected="{'true' if active_mock == 1 else 'false'}">
          <span>🛡️ Full Mock 01</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
        <a href="mock-02.html" class="set-btn{' active' if active_mock == 2 else ''}" role="tab" aria-selected="{'true' if active_mock == 2 else 'false'}">
          <span>🛡️ Full Mock 02</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
        <a href="mock-03.html" class="set-btn{' active' if active_mock == 3 else ''}" role="tab" aria-selected="{'true' if active_mock == 3 else 'false'}">
          <span>🛡️ Full Mock 03</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
      </div>
    </div>
  </div>"""
    
    content = re.sub(r'<!-- Multi-Mock Selector Bar -->.*?</div>\s*</div>\s*</div>', switcher, content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated switcher bar in: ssc-cgl/{filename}")

update_full_mock_switcher("mock-01.html", 1)
update_full_mock_switcher("mock-02.html", 2)

# --------------------------------------------------------------------------
# 2. Sectional Drills (Reasoning, Quant, English, GA)
# --------------------------------------------------------------------------
sections_info = [
    {
        "id": "reasoning",
        "file_prefix": "sectional-reasoning",
        "label": "Reasoning Drills",
        "badge_icon": "🧠",
        "name": "General Intelligence & Reasoning",
        "json_key": "reasoning"
    },
    {
        "id": "quant",
        "file_prefix": "sectional-quantitative-aptitude",
        "label": "Quant Drills",
        "badge_icon": "📐",
        "name": "Quantitative Aptitude",
        "json_key": "quant"
    },
    {
        "id": "english",
        "file_prefix": "sectional-english",
        "label": "English Drills",
        "badge_icon": "📖",
        "name": "English Comprehension",
        "json_key": "english"
    },
    {
        "id": "ga",
        "file_prefix": "sectional-general-awareness",
        "label": "General Awareness Drills",
        "badge_icon": "🌍",
        "name": "General Awareness",
        "json_key": "ga"
    }
]

for sec in sections_info:
    prefix = sec["file_prefix"]
    f2_path = os.path.join(SSC_DIR, f"{prefix}-02.html")
    with open(f2_path, "r", encoding="utf-8") as f:
        sec2_html = f.read()

    # Build 3-drill switcher bar
    def make_sec_switcher(active_drill):
        return f"""  <!-- Multi-Set Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">{sec['label']}:</span>
      <div class="set-btn-group" role="tablist">
        <a href="{prefix}-01.html" class="set-btn{' active' if active_drill == 1 else ''}" role="tab" aria-selected="{'true' if active_drill == 1 else 'false'}">
          <span>{sec['badge_icon']} Speed Drill 01</span>
          <span class="set-badge-count">25 Qs • 15M</span>
        </a>
        <a href="{prefix}-02.html" class="set-btn{' active' if active_drill == 2 else ''}" role="tab" aria-selected="{'true' if active_drill == 2 else 'false'}">
          <span>{sec['badge_icon']} Speed Drill 02</span>
          <span class="set-badge-count">25 Qs • 15M</span>
        </a>
        <a href="{prefix}-03.html" class="set-btn{' active' if active_drill == 3 else ''}" role="tab" aria-selected="{'true' if active_drill == 3 else 'false'}">
          <span>{sec['badge_icon']} Speed Drill 03</span>
          <span class="set-badge-count">25 Qs • 15M</span>
        </a>
      </div>
    </div>
  </div>"""

    # Generate 03.html
    sec3_html = sec2_html
    sec3_html = sec3_html.replace("Test 02", "Test 03")
    sec3_html = sec3_html.replace("Drill 02", "Drill 03")
    sec3_html = sec3_html.replace(f"{prefix}-02.html", f"{prefix}-03.html")
    sec3_html = sec3_html.replace(f"cgl_tier1_mock02_{sec['json_key']}.json", f"cgl_tier1_mock03_{sec['json_key']}.json")
    sec3_html = re.sub(r'<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_sec_switcher(3), sec3_html, flags=re.DOTALL)

    f3_path = os.path.join(SSC_DIR, f"{prefix}-03.html")
    with open(f3_path, "w", encoding="utf-8") as f:
        f.write(sec3_html)
    print(f"Created: ssc-cgl/{prefix}-03.html")

    # Update 01.html and 02.html switchers
    for d_num in [1, 2]:
        fn = f"{prefix}-0{d_num}.html"
        fp = os.path.join(SSC_DIR, fn)
        with open(fp, "r", encoding="utf-8") as f:
            c = f.read()
        c = re.sub(r'<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_sec_switcher(d_num), c, flags=re.DOTALL)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated switcher bar in: ssc-cgl/{fn}")

print("All 5 SSC CGL Mock 03 runners created and switcher bars updated!")
