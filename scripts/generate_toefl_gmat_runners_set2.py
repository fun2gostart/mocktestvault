#!/usr/bin/env python3
"""
Creates:
1. mocktestvault.com/global/toefl/reading-practice-02.html
2. mocktestvault.com/global/gmat/focus-diagnostic-02.html
And synchronizes switcher bars and setSources in:
3. mocktestvault.com/global/toefl/reading-practice-01.html
4. mocktestvault.com/global/gmat/focus-diagnostic-01.html
"""

import os, re

BASE_DIR = '/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com'

# ==============================================================================
# 1. TOEFL RUNNERS
# ==============================================================================

def make_toefl_switcher(active_file):
    return f'''  <!-- Multi-Set Selector Bar (40 Total Questions) -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">TOEFL® iBT Track (40 Qs):</span>
      <div class="set-btn-group" role="tablist">
        <a href="reading-practice-01.html" class="set-btn{' active' if active_file == 'drill01' else ''}" role="tab" aria-selected="{'true' if active_file == 'drill01' else 'false'}">
          <span>📖 Drill 01 (Paleoclimate/Cuneiform)</span>
          <span class="set-badge-count">20 Qs • 35M</span>
        </a>
        <a href="reading-practice-02.html" class="set-btn{' active' if active_file == 'drill02' else ''}" role="tab" aria-selected="{'true' if active_file == 'drill02' else 'false'}">
          <span>🌊 Drill 02 (Corals/Working Memory)</span>
          <span class="set-badge-count">20 Qs • 35M</span>
        </a>
      </div>
    </div>
  </div>'''

toefl_sources_block = '''setSources: {
          set1: '../../data/global/toefl/toefl_reading_set1.json',
          set2: '../../data/global/toefl/toefl_reading_set2.json'
        }'''

# Update reading-practice-01.html
p_toefl01 = os.path.join(BASE_DIR, 'global/toefl/reading-practice-01.html')
with open(p_toefl01, 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'  <!-- Multi-Set Selector Bar -->.*?</div>\s*</div>\s*</div>', make_toefl_switcher('drill01'), c, flags=re.DOTALL)
c = re.sub(r'setSources:\s*\{[^}]+\}', toefl_sources_block, c)

with open(p_toefl01, 'w', encoding='utf-8') as f:
    f.write(c)

# Create reading-practice-02.html based on reading-practice-01.html
c02 = c.replace(
    'reading-practice-01.html',
    'reading-practice-02.html'
).replace(
    'Reading Diagnostic Test 01',
    'Reading Diagnostic Test 02'
).replace(
    'Reading Drill 01',
    'Reading Drill 02'
).replace(
    'Paleoclimatology ice cores, early Mesopotamian cuneiform',
    'Coral reef biomineralization, neural working memory circuits'
).replace(
    'covering Paleoclimatology and the Origins of Cuneiform',
    'covering Coral Biomineralization & Acidification and Neural Working Memory Architecture'
).replace(
    make_toefl_switcher('drill01'),
    make_toefl_switcher('drill02')
).replace(
    "initialSet: 'set1',",
    "initialSet: 'set2',"
)

p_toefl02 = os.path.join(BASE_DIR, 'global/toefl/reading-practice-02.html')
with open(p_toefl02, 'w', encoding='utf-8') as f:
    f.write(c02)

print("Created and synchronized TOEFL reading runners!")

# ==============================================================================
# 2. GMAT FOCUS RUNNERS
# ==============================================================================

def make_gmat_switcher(active_file):
    return f'''  <!-- Multi-Set Selector Bar (40 Total Questions) -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">GMAT® Focus Suites (40 Qs):</span>
      <div class="set-btn-group" role="tablist">
        <a href="focus-diagnostic-01.html" class="set-btn{' active' if active_file == 'diag01' else ''}" role="tab" aria-selected="{'true' if active_file == 'diag01' else 'false'}">
          <span>📊 Diagnostic 01 (SaaS/Sufficiency/Sets)</span>
          <span class="set-badge-count">20 Qs • 45M</span>
        </a>
        <a href="focus-diagnostic-02.html" class="set-btn{' active' if active_file == 'diag02' else ''}" role="tab" aria-selected="{'true' if active_file == 'diag02' else 'false'}">
          <span>📊 Diagnostic 02 (Infra/SAFE/Permutations)</span>
          <span class="set-badge-count">20 Qs • 45M</span>
        </a>
      </div>
    </div>
  </div>'''

gmat_sources_block = '''setSources: {
          set1: '../../data/global/gmat/gmat_focus_set1.json',
          set2: '../../data/global/gmat/gmat_focus_set2.json'
        }'''

# Update focus-diagnostic-01.html
p_gmat01 = os.path.join(BASE_DIR, 'global/gmat/focus-diagnostic-01.html')
with open(p_gmat01, 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'  <!-- Multi-Set Selector Bar -->.*?</div>\s*</div>\s*</div>', make_gmat_switcher('diag01'), c, flags=re.DOTALL)
c = re.sub(r'setSources:\s*\{[^}]+\}', gmat_sources_block, c)

with open(p_gmat01, 'w', encoding='utf-8') as f:
    f.write(c)

# Create focus-diagnostic-02.html
c_gmat02 = c.replace(
    'focus-diagnostic-01.html',
    'focus-diagnostic-02.html'
).replace(
    'Diagnostic Test 01',
    'Diagnostic Test 02'
).replace(
    'Diagnostic Drill 01',
    'Diagnostic Drill 02'
).replace(
    'Table Analysis, Multi-Source Reasoning, Graphical Interpretation, Data Sufficiency',
    'Data Center Analytics, SAFE Term Sheets, Prime Triplets, Permutations, and Dilutions'
).replace(
    make_gmat_switcher('diag01'),
    make_gmat_switcher('diag02')
).replace(
    "initialSet: 'set1',",
    "initialSet: 'set2',"
)

p_gmat02 = os.path.join(BASE_DIR, 'global/gmat/focus-diagnostic-02.html')
with open(p_gmat02, 'w', encoding='utf-8') as f:
    f.write(c_gmat02)

print("Created and synchronized GMAT Focus runners!")
