#!/usr/bin/env python3
"""
Polishes and standardizes all runner pages for GRE, IELTS, and SSC CGL:
- Synchronizes switcher bars across GRE (Quant 01/02, Verbal 01/02)
- Synchronizes switcher bars and setSources across IELTS (Drill 01, 02, 03, 04, Random)
- Adds canonical URLs and switcher bars across SSC CGL (Full Mocks 01/02, Sectionals 01/02)
"""

import os, re

BASE_DIR = '/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com'

# ==============================================================================
# 1. GRE SUITES
# ==============================================================================

def make_gre_switcher(active_file):
    return f'''  <!-- Multi-Set Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">GRE® General Suites:</span>
      <div class="set-btn-group" role="tablist">
        <a href="quantitative-reasoning-01.html" class="set-btn{' active' if active_file == 'quant01' else ''}" role="tab" aria-selected="{'true' if active_file == 'quant01' else 'false'}">
          <span>📐 Quant Diagnostic 01</span>
          <span class="set-badge-count">20 Qs • 35M</span>
        </a>
        <a href="quantitative-reasoning-02.html" class="set-btn{' active' if active_file == 'quant02' else ''}" role="tab" aria-selected="{'true' if active_file == 'quant02' else 'false'}">
          <span>📐 Quant Diagnostic 02</span>
          <span class="set-badge-count">20 Qs • 35M</span>
        </a>
        <a href="verbal-reasoning-01.html" class="set-btn{' active' if active_file == 'verbal01' else ''}" role="tab" aria-selected="{'true' if active_file == 'verbal01' else 'false'}">
          <span>🧠 Verbal Diagnostic 01</span>
          <span class="set-badge-count">20 Qs • 30M</span>
        </a>
        <a href="verbal-reasoning-02.html" class="set-btn{' active' if active_file == 'verbal02' else ''}" role="tab" aria-selected="{'true' if active_file == 'verbal02' else 'false'}">
          <span>🧠 Verbal Diagnostic 02</span>
          <span class="set-badge-count">20 Qs • 30M</span>
        </a>
      </div>
    </div>
  </div>'''

# Update GRE Quant 01
p_quant01 = os.path.join(BASE_DIR, 'global/gre/quantitative-reasoning-01.html')
with open(p_quant01, 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(r'  <!-- Multi-Set Selector Bar -->\s*<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_gre_switcher('quant01'), c, flags=re.DOTALL)
c = c.replace(
    "setSources: {\n          set1: '../../data/global/gre/gre_quant_set1.json'\n        }",
    "setSources: {\n          set1: '../../data/global/gre/gre_quant_set1.json',\n          set2: '../../data/global/gre/gre_quant_set2.json'\n        }"
)
with open(p_quant01, 'w', encoding='utf-8') as f:
    f.write(c)

# Update GRE Quant 02
p_quant02 = os.path.join(BASE_DIR, 'global/gre/quantitative-reasoning-02.html')
with open(p_quant02, 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(r'  <!-- Multi-Set Selector Bar -->\s*<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_gre_switcher('quant02'), c, flags=re.DOTALL)
c = c.replace(
    "initialSet: 'set1',",
    "initialSet: 'set2',"
).replace(
    "setSources: {\n          set1: '../../data/global/gre/gre_quant_set2.json'\n        }",
    "setSources: {\n          set1: '../../data/global/gre/gre_quant_set1.json',\n          set2: '../../data/global/gre/gre_quant_set2.json'\n        }"
)
with open(p_quant02, 'w', encoding='utf-8') as f:
    f.write(c)

# Update GRE Verbal 01
p_verb01 = os.path.join(BASE_DIR, 'global/gre/verbal-reasoning-01.html')
with open(p_verb01, 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(r'  <!-- Multi-Set Selector Bar -->\s*<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_gre_switcher('verbal01'), c, flags=re.DOTALL)
c = c.replace(
    "setSources: {\n          set1: '../../data/global/gre/gre_verbal_set1.json'\n        }",
    "setSources: {\n          set1: '../../data/global/gre/gre_verbal_set1.json',\n          set2: '../../data/global/gre/gre_verbal_set2.json'\n        }"
)
with open(p_verb01, 'w', encoding='utf-8') as f:
    f.write(c)

# Update GRE Verbal 02
p_verb02 = os.path.join(BASE_DIR, 'global/gre/verbal-reasoning-02.html')
with open(p_verb02, 'r', encoding='utf-8') as f:
    c = f.read()
c = re.sub(r'  <!-- Multi-Set Selector Bar -->\s*<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_gre_switcher('verbal02'), c, flags=re.DOTALL)
c = c.replace(
    "initialSet: 'set1',",
    "initialSet: 'set2',"
).replace(
    "setSources: {\n          set1: '../../data/global/gre/gre_verbal_set2.json'\n        }",
    "setSources: {\n          set1: '../../data/global/gre/gre_verbal_set1.json',\n          set2: '../../data/global/gre/gre_verbal_set2.json'\n        }"
)
with open(p_verb02, 'w', encoding='utf-8') as f:
    f.write(c)

print("Synchronized all 4 GRE runner pages!")

# ==============================================================================
# 2. IELTS SUITES
# ==============================================================================

def make_ielts_switcher(active_file):
    return f'''  <!-- Multi-Set Selector Bar (80 Total Questions) -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">IELTS Academic Track (80 Qs):</span>
      <div class="set-btn-group" role="tablist">
        <a href="reading-practice-01.html" class="set-btn{' active' if active_file == 'drill01' else ''}" role="tab" aria-selected="{'true' if active_file == 'drill01' else 'false'}">
          <span>📖 Drill 01 (Architecture/Acoustics)</span>
          <span class="set-badge-count">20 Qs • 25M</span>
        </a>
        <a href="reading-practice-02.html" class="set-btn{' active' if active_file == 'drill02' else ''}" role="tab" aria-selected="{'true' if active_file == 'drill02' else 'false'}">
          <span>🌾 Drill 02 (Agriculture/Seabed/Neuro)</span>
          <span class="set-badge-count">20 Qs • 25M</span>
        </a>
        <a href="reading-practice-03.html" class="set-btn{' active' if active_file == 'drill03' else ''}" role="tab" aria-selected="{'true' if active_file == 'drill03' else 'false'}">
          <span>📜 Drill 03 (Voynich/Cryosphere/Biomim)</span>
          <span class="set-badge-count">20 Qs • 25M</span>
        </a>
        <a href="reading-practice-04.html" class="set-btn{' active' if active_file == 'drill04' else ''}" role="tab" aria-selected="{'true' if active_file == 'drill04' else 'false'}">
          <span>🌋 Drill 04 (Vents/Mycorrhizae/Acoustics)</span>
          <span class="set-badge-count">20 Qs • 25M</span>
        </a>
        <a href="reading-practice-random.html" class="set-btn random-btn{' active' if active_file == 'random' else ''}" role="tab" aria-selected="{'true' if active_file == 'random' else 'false'}" data-set="random">
          <span>🎲 Random 20-Q Mock</span>
          <span class="set-badge-count">Shuffled</span>
        </a>
      </div>
    </div>
  </div>'''

ielts_set_sources_block = '''setSources: {
          set1: '../../data/global/ielts/ielts_reading_set1.json',
          set2: '../../data/global/ielts/ielts_reading_set2.json',
          set3: '../../data/global/ielts/ielts_reading_set3.json',
          set4: '../../data/global/ielts/ielts_reading_set4.json'
        }'''

for fname, key in [
    ('reading-practice-01.html', 'drill01'),
    ('reading-practice-02.html', 'drill02'),
    ('reading-practice-03.html', 'drill03'),
    ('reading-practice-04.html', 'drill04'),
    ('reading-practice-random.html', 'random')
]:
    fpath = os.path.join(BASE_DIR, 'global/ielts', fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'  <!-- Multi-Set Selector Bar.*?<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', make_ielts_switcher(key), c, flags=re.DOTALL)
    c = re.sub(r'setSources:\s*\{[^}]+\}', ielts_set_sources_block, c)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Synchronized all 5 IELTS runner pages!")

# ==============================================================================
# 3. SSC CGL RUNNER PAGES
# ==============================================================================

def make_ssc_mock_switcher(active_num):
    return f'''  <!-- Multi-Mock Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">Full Length Mocks:</span>
      <div class="set-btn-group" role="tablist">
        <a href="mock-01.html" class="set-btn{' active' if active_num == 1 else ''}" role="tab" aria-selected="{'true' if active_num == 1 else 'false'}">
          <span>🛡️ Full Mock 01</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
        <a href="mock-02.html" class="set-btn{' active' if active_num == 2 else ''}" role="tab" aria-selected="{'true' if active_num == 2 else 'false'}">
          <span>🛡️ Full Mock 02</span>
          <span class="set-badge-count">100 Qs • 60M</span>
        </a>
      </div>
    </div>
  </div>'''

for num in [1, 2]:
    fpath = os.path.join(BASE_DIR, f'ssc-cgl/mock-0{num}.html')
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    # Add canonical if missing
    canonical_tag = f'<link rel="canonical" href="https://mocktestvault.com/ssc-cgl/mock-0{num}.html">'
    if 'rel="canonical"' not in c:
        c = c.replace('<link rel="stylesheet"', f'{canonical_tag}\n\n  <link rel="stylesheet"')
    
    # Insert switcher bar before section tabs if not already present
    if '<!-- Multi-Mock Selector Bar -->' not in c:
        c = c.replace('  <!-- Section Quick Jump Toolbar', f'{make_ssc_mock_switcher(num)}\n\n  <!-- Section Quick Jump Toolbar')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Updated SSC CGL mock-01.html and mock-02.html!")

# Update Sectional Runners
sectionals = [
    ('reasoning', 'Reasoning Drills', '🧠 Speed Drill', '15M'),
    ('quantitative-aptitude', 'Quant Drills', '📐 Speed Drill', '20M'),
    ('general-awareness', 'General Awareness Drills', '🌍 Speed Drill', '10M'),
    ('english', 'English Drills', '📖 Speed Drill', '12M')
]

for sec_key, sec_label, sec_icon_prefix, sec_time in sectionals:
    for num in [1, 2]:
        fpath = os.path.join(BASE_DIR, f'ssc-cgl/sectional-{sec_key}-0{num}.html')
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        canonical_tag = f'<link rel="canonical" href="https://mocktestvault.com/ssc-cgl/sectional-{sec_key}-0{num}.html">'
        if 'rel="canonical"' not in c:
            c = c.replace('<link rel="stylesheet"', f'{canonical_tag}\n\n  <link rel="stylesheet"')
        
        switcher = f'''  <!-- Sectional Multi-Set Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">{sec_label}:</span>
      <div class="set-btn-group" role="tablist">
        <a href="sectional-{sec_key}-01.html" class="set-btn{' active' if num == 1 else ''}" role="tab" aria-selected="{'true' if num == 1 else 'false'}">
          <span>{sec_icon_prefix} 01</span>
          <span class="set-badge-count">25 Qs • {sec_time}</span>
        </a>
        <a href="sectional-{sec_key}-02.html" class="set-btn{' active' if num == 2 else ''}" role="tab" aria-selected="{'true' if num == 2 else 'false'}">
          <span>{sec_icon_prefix} 02</span>
          <span class="set-badge-count">25 Qs • {sec_time}</span>
        </a>
      </div>
    </div>
  </div>'''
        c = re.sub(r'  <!-- Section Info Bar -->\s*<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', switcher, c, flags=re.DOTALL)
        c = re.sub(r'  <!-- Sectional Multi-Set Bar -->\s*<div class="set-switcher-bar">.*?</div>\s*</div>\s*</div>', switcher, c, flags=re.DOTALL)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)

print("Updated all 8 SSC CGL sectional runner pages!")
