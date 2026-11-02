#!/usr/bin/env python3
"""
Updates CBSE Class 10 Social Science HTML runners from ch11 to ch21
to include the standard 3-set switcher bar and setSources configuration.
"""

import os, re

HTML_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cbse-class-10", "social-science")

chapters = [
    "ch11_manufacturing_industries",
    "ch12_lifelines_of_national_economy",
    "ch13_power_sharing",
    "ch14_federalism",
    "ch15_gender_religion_caste",
    "ch16_political_parties",
    "ch17_outcomes_of_democracy",
    "ch18_development",
    "ch19_sectors_of_indian_economy",
    "ch20_money_and_credit",
    "ch21_globalisation_and_indian_economy"
]

NEW_SWITCHER = """  <!-- Multi-Set Selector Bar (60 Total Questions) -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">Test Sets (60 Qs):</span>
      <div class="set-btn-group" role="tablist">
        <button class="set-btn active" data-set="set1" id="set-btn-set1" role="tab" aria-selected="true">
          <span>Set 1: Board Foundation</span>
          <span class="set-badge-count">20 Qs</span>
        </button>
        <button class="set-btn" data-set="set2" id="set-btn-set2" role="tab" aria-selected="false">
          <span>Set 2: NCERT Exemplar & Applications</span>
          <span class="set-badge-count">20 Qs</span>
        </button>
        <button class="set-btn" data-set="set3" id="set-btn-set3" role="tab" aria-selected="false">
          <span>Set 3: Assertion-Reason & Case Studies</span>
          <span class="set-badge-count">20 Qs</span>
        </button>
      </div>
    </div>
  </div>"""

def get_new_script(slug):
    return f"""  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: 'set1',
        timeLimitMinutes: 20,
        setSources: {{
          set1: '../../data/in/cbse10/social-science/{slug}_set1.json',
          set2: '../../data/in/cbse10/social-science/{slug}_set2.json',
          set3: '../../data/in/cbse10/social-science/{slug}_set3.json'
        }}
      }});
    }});
  </script>"""

switcher_pattern = re.compile(r'<!-- Multi-Set Selector Bar.*?</div>\s*</div>\s*</div>', re.DOTALL)
script_pattern = re.compile(r'<script src="../../js/test-engine.js"></script>.*?<script>.*?</script>', re.DOTALL)

for slug in chapters:
    filepath = os.path.join(HTML_DIR, f"{slug}.html")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace switcher bar
    if switcher_pattern.search(content):
        content = switcher_pattern.sub(NEW_SWITCHER, content, count=1)
    else:
        print(f"Warning: switcher pattern not found in {slug}")

    # Replace script section
    new_script = get_new_script(slug)
    if script_pattern.search(content):
        content = script_pattern.sub(new_script, content, count=1)
    else:
        print(f"Warning: script pattern not found in {slug}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated HTML runner: {slug}.html")

print("All 11 Social Science HTML runners updated successfully!")
