#!/usr/bin/env python3
"""
MockTestVault — Complete CBSE Class 10 Curriculum Builder
Generates verified question banks and test runners for all 48 chapters across Science, Math, and Social Science.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Template for Chapter Test Runner HTML
def generate_html_runner(subject_name, subject_slug, ch_num, ch_title, ch_slug, json_rel_path):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Class 10 CBSE {subject_name} Chapter {ch_num}: {ch_title} MCQ Mock Test | MockTestVault</title>
  <meta name="description" content="Free chapter-wise CBSE Class 10 {subject_name} {ch_title} MCQ practice test with assertion-reasoning, timer, instant NCERT explanations, and printable revision PDF sheet.">
  
  <link rel="stylesheet" href="../../css/test-engine.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "CBSE Class 10 {subject_name} Chapter {ch_num}: {ch_title} MCQ Test",
    "educationalLevel": "Grade 10",
    "learningResourceType": "Practice Quiz",
    "about": {{
      "@type": "Thing",
      "name": "{ch_title}"
    }},
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
    <h1>MockTestVault — CBSE Class 10 {subject_name} Chapter {ch_num} Revision Sheet</h1>
    <p>Topic: {ch_title} (NCERT Solutions & Conceptual Review) | mocktestvault.com</p>
  </div>

  <!-- Site Navigation Header -->
  <header class="site-header">
    <div class="header-container">
      <a href="../../index.html" class="brand-link">
        <div class="brand-logo">🛡️</div>
        <div class="brand-text">
          <h1>MockTestVault <span class="vault-pill">CBSE Class 10</span></h1>
          <p>Official Curriculum Exam Simulator</p>
        </div>
      </a>

      <div class="header-controls">
        <!-- Practice Mode vs Exam Mode Toggle -->
        <div class="mode-pill-group" role="group" aria-label="Test Mode Selection">
          <button id="mode-practice-btn" class="mode-btn" title="Practice Mode: Instant answers and step-by-step NCERT explanations">
            <span>🎓</span> Practice
          </button>
          <button id="mode-exam-btn" class="mode-btn active" title="Exam Mode: Timed 20-min official simulation with final scorecard">
            <span>⏱️</span> Exam
          </button>
        </div>

        <!-- Utility Toolbar -->
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
      <a href="../index.html">CBSE Class 10</a>
      <span class="sep">/</span>
      <a href="../index.html#block-{subject_slug}">{subject_name}</a>
      <span class="sep">/</span>
      <span class="current">Ch {ch_num}: {ch_title}</span>
    </div>
  </nav>

  <!-- Multi-Set Selector Bar -->
  <div class="set-switcher-bar">
    <div class="set-switcher-container">
      <span class="set-label">Test Sets (Chapter {ch_num}):</span>
      <div class="set-btn-group" role="tablist">
        <button class="set-btn active" data-set="set1" id="set-btn-set1" role="tab" aria-selected="true">
          <span>Set 1: Board Mock Test</span>
          <span class="set-badge-count">Live</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Exam Live Status Bar -->
  <div id="exam-status-bar" class="exam-status-bar">
    <div class="status-container">
      <div id="timer-box" class="timer-box">
        <span>⏱️</span>
        <span id="timer-display">20:00</span>
      </div>

      <div class="progress-info">
        <span id="progress-text" class="progress-text">Loading questions...</span>
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
      <div class="meta-badges-row" id="q-badges"></div>

      <div class="question-text-box">
        <div class="question-number" id="q-number">Question 1</div>
        <div class="question-title" id="q-title">Loading question...</div>
      </div>

      <!-- Interactive Options -->
      <div class="options-list" id="options-list" role="radiogroup"></div>

      <!-- NCERT Explanation Box -->
      <div class="explanation-box" id="explanation-box">
        <div class="explanation-header">
          <span>✓ NCERT Conceptual Explanation</span>
          <span class="citation-tag" id="citation-tag">NCERT Official Syllabus</span>
        </div>
        <p class="explanation-text" id="explanation-text"></p>
      </div>

      <!-- Action Buttons Row -->
      <div class="card-action-bar">
        <button id="btn-prev" class="nav-btn" disabled>
          <span>⬅️</span> Previous
        </button>

        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <button id="btn-review" class="nav-btn btn-review">
            <span>☆</span> Mark for Review
          </button>
          <button id="btn-clear" class="nav-btn" title="Clear selection for this question">
            <span>🧹</span> Clear Response
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
        <span style="font-size:0.75rem; color:var(--text-muted); font-weight:normal;">Board Simulator</span>
      </div>

      <div class="palette-grid" id="palette-grid"></div>

      <!-- TCS iON Official 5-State Status Legend -->
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
          <span>Marked for Review (<strong id="count-reviewed">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-answered-reviewed"></div>
          <span>Ans & Marked for Review (<strong id="count-ans-reviewed">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-unvisited"></div>
          <span>Not Visited (<strong id="count-unvisited">0</strong>)</span>
        </div>
        <div class="legend-item">
          <div class="legend-dot dot-current"></div>
          <span>Current Active Question</span>
        </div>
      </div>
    </aside>

  </main>

  <!-- Scorecard View -->
  <section class="scorecard-view" id="scorecard-view" style="max-width:960px; margin:24px auto; padding:32px 24px;">
    <div class="score-hero" id="score-hero"></div>
    <div class="stats-grid" id="stats-grid"></div>

    <div class="scorecard-actions">
      <button id="btn-retake" class="nav-btn btn-primary">
        <span>🔄</span> Retake Test
      </button>
      <button id="btn-print" class="nav-btn">
        <span>🖨️</span> Download / Print Revision PDF
      </button>
    </div>

    <!-- Subtopic Mastery Progress Breakdown -->
    <div id="mastery-container"></div>

    <!-- Review Filters Bar -->
    <div class="review-filters-bar">
      <h3 class="review-list-title" style="margin-bottom:0;">Detailed Solution Review</h3>
      <div class="review-filter-group" role="tablist">
        <button class="filter-pill active" data-filter="all" id="filter-all">
          All (<span id="filter-count-all">0</span>)
        </button>
        <button class="filter-pill filter-wrong" data-filter="wrong" id="filter-wrong">
          ❌ Mistakes (<span id="filter-count-wrong">0</span>)
        </button>
        <button class="filter-pill filter-reviewed" data-filter="reviewed" id="filter-reviewed">
          🟣 Review (<span id="filter-count-reviewed">0</span>)
        </button>
        <button class="filter-pill filter-correct" data-filter="correct" id="filter-correct">
          ✓ Correct (<span id="filter-count-correct">0</span>)
        </button>
      </div>
    </div>

    <!-- Full Review List -->
    <div id="review-list"></div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <p><strong>MockTestVault.com</strong> — 100% Free Educational Practice & Board Exam Simulators.</p>
      <p style="font-size:0.75rem;">100% Free & Distraction-Free. Aligned with official NCERT Class 10 {subject_name} standards.</p>
    </div>
  </footer>

  <script src="../../js/test-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      window.testEngine = new MockTestEngine({{
        initialSet: 'set1',
        timeLimitMinutes: 20
      }});
      window.testEngine.setSources = {{
        set1: '../../{json_rel_path}'
      }};
      window.testEngine.dataSource = window.testEngine.setSources.set1;
      window.testEngine.loadQuestions();
    }});
  </script>
</body>
</html>
"""

print("Runner template defined.")

# -------------------------------------------------------------------------
# SCIENCE CURRICULUM CHAPTER DEFINITIONS & QUESTION VAULTS
# -------------------------------------------------------------------------

SCIENCE_CHAPTERS = [
  {
    "slug": "ch01_chemical_reactions",
    "num": 1,
    "title": "Chemical Reactions and Equations",
    "sub": "Chemistry",
    "marks": "6–7 Marks",
    "desc": "Balancing equations, combination, decomposition, displacement, double displacement, redox, corrosion, and rancidity.",
    "questions": [] # Already generated in set1, set2, set3
  },
  {
    "slug": "ch02_acids_bases_salts",
    "num": 2,
    "title": "Acids, Bases and Salts",
    "sub": "Chemistry",
    "marks": "7–8 Marks",
    "desc": "pH scale, indicators, neutralization, chlor-alkali process, bleaching powder, baking soda, washing soda & POP.",
    "questions": [] # Already generated in set1
  },
  {
    "slug": "ch03_metals_non_metals",
    "num": 3,
    "title": "Metals and Non-metals",
    "sub": "Chemistry",
    "marks": "6–7 Marks",
    "desc": "Physical & chemical properties, reactivity series, formation & properties of ionic compounds, and metallurgy.",
    "questions": [] # Already generated in set1
  },
  {
    "slug": "ch04_carbon_compounds",
    "num": 4,
    "title": "Carbon and its Compounds",
    "sub": "Chemistry",
    "marks": "7–8 Marks",
    "desc": "Covalent bonding, versatile nature of carbon, homologous series, functional groups, ethanol, ethanoic acid, and soaps.",
    "questions": [
      {
        "id": "cbse10-sci-ch04-s1-001",
        "type": "mcq",
        "subtopic": "Covalent Bonding",
        "difficulty": "Easy",
        "question": "Carbon forms covalent bonds rather than ionic bonds because forming C⁴⁺ or C⁴⁻ ions is energetically unfavorable. Which properties are characteristic of covalent carbon compounds?",
        "options": [
          "High melting points and conduct electricity in solid state",
          "Low melting/boiling points and are poor conductors of electricity",
          "High electrical conductivity in molten state",
          "Soluble exclusively in inorganic polar solvents"
        ],
        "answer": 1,
        "explanation": "Covalent compounds share electrons between atoms, so no free ions or charged particles are present, making them poor conductors of electricity. Their intermolecular forces are relatively weak, leading to low melting and boiling points.",
        "citation": "NCERT Class 10 Science, Chapter 4, Section 4.1"
      },
      {
        "id": "cbse10-sci-ch04-s1-002",
        "type": "mcq",
        "subtopic": "Allotropes of Carbon",
        "difficulty": "Easy",
        "question": "Which allotrope of carbon consists of carbon atoms arranged in layers of hexagonal arrays held by weak van der Waals forces, making it soft, slippery, and a good conductor of electricity?",
        "options": [
          "Diamond",
          "Graphite",
          "Buckminsterfullerene (C-60)",
          "Carbon nanotube"
        ],
        "answer": 1,
        "explanation": "In graphite, each carbon atom is bonded to three other carbons in the same plane giving a hexagonal array. One valence electron remains delocalized, allowing graphite to conduct electricity. The slippery layers make it an effective solid lubricant.",
        "citation": "NCERT Class 10 Science, Chapter 4, Section 4.1.1 (Allotropes Box)"
      },
      {
        "id": "cbse10-sci-ch04-s1-003",
        "type": "mcq",
        "subtopic": "Homologous Series",
        "difficulty": "Medium",
        "question": "In a homologous series of organic compounds, two successive members differ in their molecular formula and molecular mass respectively by:",
        "options": [
          "-CH₃ and 15 u",
          "-CH₂- and 14 u",
          "-CH- and 13 u",
          "-C₂H₄ and 28 u"
        ],
        "answer": 1,
        "explanation": "Consecutive members of any homologous series (e.g. CH₄ and C₂H₆, or CH₃OH and C₂H₅OH) differ by one carbon atom and two hydrogen atoms (-CH₂- unit). Carbon mass = 12 u, 2×H = 2 u; total mass difference is 14 u.",
        "citation": "NCERT Class 10 Science, Chapter 4, Section 4.2.2"
      },
      {
        "id": "cbse10-sci-ch04-s1-004",
        "type": "mcq",
        "subtopic": "Soaps & Detergents",
        "difficulty": "Hard",
        "question": "What is the structural orientation of a soap molecule during micelle formation when dissolved in water?",
        "options": [
          "Hydrophobic ionic head towards oil; hydrophilic hydrocarbon tail towards water",
          "Hydrophobic hydrocarbon tail dissolves in oil/dirt; hydrophilic ionic head faces outward in water",
          "Both ends dissolve completely inside the oil droplet",
          "Both ends face outward towards water molecules"
        ],
        "answer": 1,
        "explanation": "A soap molecule has two ends: a long non-polar hydrocarbon tail that is hydrophobic (water-repelling) and dissolves in oily dirt, and an ionic end (COO⁻Na⁺) that is hydrophilic (water-attracting). In water, they form radial spherical clusters called micelles.",
        "citation": "NCERT Class 10 Science, Chapter 4, Section 4.5 (Soaps and Detergents)"
      },
      {
        "id": "cbse10-sci-ch04-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): Vegetable oils containing unsaturated fatty acids are generally recommended for healthy cooking over animal fats.\nReason (R): Unsaturated hydrocarbons undergo addition reactions with hydrogen in the presence of nickel catalyst to form saturated fats.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 1,
        "explanation": "Vegetable oils contain long unsaturated carbon chains and are considered heart-healthy, whereas saturated animal fats can raise cholesterol. The industrial hydrogenation of oils using nickel is also chemically true, but does not explain the biological nutritional benefit.",
        "citation": "NCERT Class 10 Science, Chapter 4, Section 4.3.3"
      }
    ]
  },
  {
    "slug": "ch05_life_processes",
    "num": 5,
    "title": "Life Processes",
    "sub": "Biology",
    "marks": "8–9 Marks",
    "desc": "Autotrophic & heterotrophic nutrition, cellular respiration, human heart double circulation, and nephron excretion.",
    "questions": [
      {
        "id": "cbse10-sci-ch05-s1-001",
        "type": "mcq",
        "subtopic": "Photosynthesis",
        "difficulty": "Easy",
        "question": "During the process of photosynthesis in green plants, which of the following events does NOT take place?",
        "options": [
          "Absorption of light energy by chlorophyll",
          "Conversion of light energy into chemical energy and splitting of water molecules into hydrogen and oxygen",
          "Oxidation of carbon dioxide to form carbohydrates",
          "Reduction of carbon dioxide to form carbohydrates"
        ],
        "answer": 2,
        "explanation": "Photosynthesis involves the REDUCTION (not oxidation) of carbon dioxide to carbohydrates by the addition of hydrogen from water. The three key steps are: light absorption by chlorophyll, photolysis of water, and reduction of CO₂ to glucose.",
        "citation": "NCERT Class 10 Science, Chapter 5, Section 5.2.1"
      },
      {
        "id": "cbse10-sci-ch05-s1-002",
        "type": "mcq",
        "subtopic": "Respiration Pathways",
        "difficulty": "Medium",
        "question": "When energy is required rapidly during intense muscular exercise in humans, pyruvate is converted into which compound in muscle cells, causing muscle fatigue and cramps?",
        "options": [
          "Ethanol + Carbon dioxide + Energy",
          "Lactic acid + Energy",
          "Carbon dioxide + Water + Energy",
          "Glucose + Pyruvate"
        ],
        "answer": 1,
        "explanation": "When there is a lack of oxygen in human muscle cells, pyruvate undergoes anaerobic breakdown into a 3-carbon compound called lactic acid. The buildup of lactic acid causes muscle cramps.",
        "citation": "NCERT Class 10 Science, Chapter 5, Section 5.3 (Breakdown of Glucose Diagram)"
      },
      {
        "id": "cbse10-sci-ch05-s1-003",
        "type": "mcq",
        "subtopic": "Human Heart & Circulation",
        "difficulty": "Hard",
        "question": "In the human circulatory system, which blood vessel carries freshly oxygenated blood from the lungs directly into the left atrium of the heart?",
        "options": [
          "Pulmonary artery",
          "Pulmonary vein",
          "Vena cava",
          "Aorta"
        ],
        "answer": 1,
        "explanation": "The pulmonary veins are the only veins in the human body that carry oxygenated blood; they transport blood from the lungs into the left atrium. The pulmonary artery carries deoxygenated blood from the right ventricle to the lungs.",
        "citation": "NCERT Class 10 Science, Chapter 5, Section 5.4.1"
      },
      {
        "id": "cbse10-sci-ch05-s1-004",
        "type": "mcq",
        "subtopic": "Excretion in Humans",
        "difficulty": "Medium",
        "question": "What is the basic functional filtration unit of the human kidney, and where does initial ultrafiltration of blood take place?",
        "options": [
          "Alveoli; Bronchioles",
          "Nephron; Glomerulus enclosed in Bowman's capsule",
          "Neuron; Synapse",
          "Villi; Small intestine"
        ],
        "answer": 1,
        "explanation": "The basic filtration unit of the kidney is the nephron. High-pressure capillary filtration occurs in the glomerulus, a tuft of capillaries sitting inside the cup-shaped Bowman's capsule.",
        "citation": "NCERT Class 10 Science, Chapter 5, Section 5.5.1"
      },
      {
        "id": "cbse10-sci-ch05-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The inner lining of the small intestine possesses millions of microscopic finger-like projections called villi.\nReason (R): Villi vastly increase the surface area available for the rapid absorption of digested food nutrients.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Villi multiply the absorptive surface area of the ileum several hundredfold. They are richly supplied with blood vessels that take absorbed food to every cell of the body. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 5, Section 5.2.3"
      }
    ]
  },
  {
    "slug": "ch06_control_coordination",
    "num": 6,
    "title": "Control and Coordination",
    "sub": "Biology",
    "marks": "5–6 Marks",
    "desc": "Human brain, reflex action, peripheral nervous system, plant tropic movements, and endocrine glands.",
    "questions": [
      {
        "id": "cbse10-sci-ch06-s1-001",
        "type": "mcq",
        "subtopic": "Nervous System",
        "difficulty": "Easy",
        "question": "In a neuron, electrical impulses travel through which sequence of anatomical structures?",
        "options": [
          "Dendrite → Cell body (cyton) → Axon → Axonal nerve ending",
          "Axon → Cell body → Dendrite → Synapse",
          "Cell body → Dendrite → Axon → Nucleus",
          "Nerve ending → Axon → Cell body → Dendrite"
        ],
        "answer": 0,
        "explanation": "Information is acquired at the dendritic tip, sets off an electrical impulse that travels through the cell body, then along the axon to its terminal end. At the synapse, electrical signals trigger chemical neurotransmitter release.",
        "citation": "NCERT Class 10 Science, Chapter 6, Section 6.1.1"
      },
      {
        "id": "cbse10-sci-ch06-s1-002",
        "type": "mcq",
        "subtopic": "Brain Anatomy",
        "difficulty": "Medium",
        "question": "Which specific region of the human brain is responsible for maintaining posture, equilibrium, and precision of voluntary muscle actions like riding a bicycle?",
        "options": [
          "Cerebrum in the forebrain",
          "Cerebellum in the hindbrain",
          "Medulla in the hindbrain",
          "Hypothalamus"
        ],
        "answer": 1,
        "explanation": "The cerebellum (part of the hindbrain) coordinates voluntary movements, posture, balance, and fine motor precision (e.g. walking a straight line, picking up a pen).",
        "citation": "NCERT Class 10 Science, Chapter 6, Section 6.1.3"
      },
      {
        "id": "cbse10-sci-ch06-s1-003",
        "type": "mcq",
        "subtopic": "Plant Hormones",
        "difficulty": "Easy",
        "question": "Which plant hormone promotes rapid cell division and is found in high concentrations in areas of active cell growth such as fruits and seeds?",
        "options": [
          "Auxin",
          "Gibberellin",
          "Cytokinin",
          "Abscisic acid"
        ],
        "answer": 2,
        "explanation": "Cytokinins naturally promote cytokinesis (cell division) and are present in greatest concentration in fast-growing plant tissues such as developing seeds and ripening fruits.",
        "citation": "NCERT Class 10 Science, Chapter 6, Section 6.2.2"
      },
      {
        "id": "cbse10-sci-ch06-s1-004",
        "type": "mcq",
        "subtopic": "Endocrine Glands",
        "difficulty": "Easy",
        "question": "Deficiency of dietary iodine in drinking water and food leads to swelling of the thyroid gland in the neck, causing which disease?",
        "options": [
          "Diabetes mellitus",
          "Goitre",
          "Dwarfism",
          "Acromegaly"
        ],
        "answer": 1,
        "explanation": "Iodine is essential for the thyroid gland to synthesize the hormone thyroxin, which regulates carbohydrate, protein, and fat metabolism. Lack of iodine leads to goitre, characterized by an enlarged, swollen neck.",
        "citation": "NCERT Class 10 Science, Chapter 6, Section 6.3"
      },
      {
        "id": "cbse10-sci-ch06-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): Tendrils of pea plants coil around a support fence whenever they come in physical contact with it.\nReason (R): Auxin diffuses towards the side of the tendril that is in direct contact with the support, accelerating its growth.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true.",
          "Both (A) and (R) are false."
        ],
        "answer": 1,
        "explanation": "Assertion (A) is TRUE: Tendrils circle supports (thigmotropism). Reason (R) is FALSE: Auxin moves AWAY from the side of contact towards the side facing away from the support, stimulating faster cell elongation on the outside, causing it to bend and coil.",
        "citation": "NCERT Class 10 Science, Chapter 6, Section 6.2.1"
      }
    ]
  },
  {
    "slug": "ch07_how_organisms_reproduce",
    "num": 7,
    "title": "How do Organisms Reproduce?",
    "sub": "Biology",
    "marks": "6–7 Marks",
    "desc": "Asexual modes, sexual reproduction in plants, human reproductive anatomy, and contraception.",
    "questions": [
      {
        "id": "cbse10-sci-ch07-s1-001",
        "type": "mcq",
        "subtopic": "Asexual Reproduction",
        "difficulty": "Easy",
        "question": "In Bryophyllum, vegetative propagation naturally occurs through buds produced along the margins of which organ?",
        "options": [
          "Stem nodes",
          "Notches in leaf margins",
          "Fibrous roots",
          "Flower petals"
        ],
        "answer": 1,
        "explanation": "The leaves of Bryophyllum produce adventitious buds in the notches along their leaf margins. When these leaves fall on moist soil, the buds develop into independent new plantlets.",
        "citation": "NCERT Class 10 Science, Chapter 7, Section 7.2.5"
      },
      {
        "id": "cbse10-sci-ch07-s1-002",
        "type": "mcq",
        "subtopic": "Reproduction in Plants",
        "difficulty": "Medium",
        "question": "In a flowering plant, which parts develop into the seed and fruit respectively after double fertilization?",
        "options": [
          "Ovule develops into seed; Ovary develops into fruit",
          "Ovary develops into seed; Ovule develops into fruit",
          "Stamen develops into seed; Carpel develops into fruit",
          "Pollen grain develops into seed; Petal develops into fruit"
        ],
        "answer": 0,
        "explanation": "Following fertilization, the zygote divides to form an embryo within the ovule, which develops a tough coat and becomes the seed. The surrounding ovary grows rapidly and ripens to form the protective fruit.",
        "citation": "NCERT Class 10 Science, Chapter 7, Section 7.3.1"
      },
      {
        "id": "cbse10-sci-ch07-s1-003",
        "type": "mcq",
        "subtopic": "Human Reproductive Anatomy",
        "difficulty": "Medium",
        "question": "Why are the human testes located outside the abdominal cavity within a pouch of skin called the scrotum?",
        "options": [
          "To provide mechanical flexibility during walking",
          "Spermatogenesis requires a temperature 2 to 2.5°C lower than standard internal body temperature",
          "To allow direct oxygenation from atmospheric air",
          "To store mature sperm cells indefinitely"
        ],
        "answer": 1,
        "explanation": "Formation of viable sperm cells requires a temperature 2–2.5°C lower than normal body temperature (37°C). The external scrotum regulates this optimal cooler environment.",
        "citation": "NCERT Class 10 Science, Chapter 7, Section 7.3.2"
      },
      {
        "id": "cbse10-sci-ch07-s1-004",
        "type": "mcq",
        "subtopic": "Contraceptive Methods",
        "difficulty": "Easy",
        "question": "Which of the following birth control methods provides reliable dual protection by preventing both unwanted pregnancy and the transmission of sexually transmitted infections (STIs/STDs)?",
        "options": [
          "Copper-T (IUCD) inserted into uterus",
          "Oral contraceptive hormonal pills",
          "Barrier methods like condoms",
          "Surgical vasectomy / tubectomy"
        ],
        "answer": 2,
        "explanation": "Condoms are physical barrier contraceptives that prevent direct mucosal fluid contact, thereby offering dual protection against both fertilization and sexually transmitted infections (HIV, gonorrhea, syphilis).",
        "citation": "NCERT Class 10 Science, Chapter 7, Section 7.4"
      },
      {
        "id": "cbse10-sci-ch07-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): Surgical blocking of the vas deferens in males (vasectomy) prevents pregnancy.\nReason (R): Vasectomy prevents the production of sperm cells in the testes.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true.",
          "Both (A) and (R) are false."
        ],
        "answer": 1,
        "explanation": "Assertion (A) is TRUE: Vasectomy is a permanent contraceptive method. Reason (R) is FALSE: Testes CONTINUE to produce sperm, but the blocked vas deferens prevents sperm from entering the ejaculated semen.",
        "citation": "NCERT Class 10 Science, Chapter 7, Section 7.4"
      }
    ]
  },
  {
    "slug": "ch08_heredity",
    "num": 8,
    "title": "Heredity",
    "sub": "Biology",
    "marks": "5–6 Marks",
    "desc": "Mendelian genetics, monohybrid/dihybrid cross ratios, and chromosome sex determination.",
    "questions": [
      {
        "id": "cbse10-sci-ch08-s1-001",
        "type": "mcq",
        "subtopic": "Mendelian Genetics",
        "difficulty": "Easy",
        "question": "In a classical Mendelian monohybrid cross between a homozygous pure tall pea plant (TT) and a homozygous pure short plant (tt), what is the phenotypic ratio obtained in the F2 generation?",
        "options": [
          "1 Tall : 1 Short",
          "3 Tall : 1 Short",
          "9 Tall : 3 Short : 3 Wrinkled : 1 Round",
          "All Tall (100%)"
        ],
        "answer": 1,
        "explanation": "F1 generation (Tt) self-pollinates (Tt × Tt). The resulting F2 offspring are TT (Tall), Tt (Tall), Tt (Tall), and tt (Short), yielding a phenotypic ratio of 3 Tall : 1 Short (genotypic ratio 1 : 2 : 1).",
        "citation": "NCERT Class 10 Science, Chapter 8, Section 8.2"
      },
      {
        "id": "cbse10-sci-ch08-s1-002",
        "type": "mcq",
        "subtopic": "Sex Determination",
        "difficulty": "Easy",
        "question": "In human beings, how is the biological sex of a newborn child genetically determined?",
        "options": [
          "Entirely by the mother's X chromosome",
          "By whether the father's fertilizing sperm cell carries an X or a Y chromosome",
          "By the ambient temperature during incubation",
          "By the nutritional health of the placenta"
        ],
        "answer": 1,
        "explanation": "Females produce eggs containing only X chromosomes (22 + X). Males produce two types of sperms in equal 50:50 ratio: (22 + X) and (22 + Y). Fertilization by an X-sperm gives a female child (XX), and by a Y-sperm gives a male child (XY).",
        "citation": "NCERT Class 10 Science, Chapter 8, Section 8.2.4"
      },
      {
        "id": "cbse10-sci-ch08-s1-003",
        "type": "mcq",
        "subtopic": "Dihybrid Cross",
        "difficulty": "Medium",
        "question": "In a dihybrid cross between pea plants with Round Yellow seeds (RRYY) and Wrinkled Green seeds (rryy), what is the phenotypic ratio in the F2 generation?",
        "options": [
          "3 : 1",
          "9 : 3 : 3 : 1",
          "1 : 2 : 1",
          "1 : 1 : 1 : 1"
        ],
        "answer": 1,
        "explanation": "Mendel's Law of Independent Assortment shows that seed shape and seed color segregate independently, producing 9 Round Yellow : 3 Round Green : 3 Wrinkled Yellow : 1 Wrinkled Green.",
        "citation": "NCERT Class 10 Science, Chapter 8, Section 8.2.3"
      },
      {
        "id": "cbse10-sci-ch08-s1-004",
        "type": "mcq",
        "subtopic": "Chromosomes",
        "difficulty": "Easy",
        "question": "How many total chromosomes and how many pairs of autosomes are present in the somatic cells of a normal human being?",
        "options": [
          "23 chromosomes; 11 pairs autosomes",
          "46 chromosomes (23 pairs); 22 pairs autosomes",
          "48 chromosomes; 24 pairs autosomes",
          "44 chromosomes; 21 pairs autosomes"
        ],
        "answer": 1,
        "explanation": "Human cells have 46 chromosomes (23 pairs). Of these, 22 pairs are autosomes (identical in males and females), and 1 pair is sex chromosomes (XX in females, XY in males).",
        "citation": "NCERT Class 10 Science, Chapter 8, Section 8.2.4"
      },
      {
        "id": "cbse10-sci-ch08-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): A cross between a pure tall plant (TT) and a pure dwarf plant (tt) produces only tall plants in the F1 generation.\nReason (R): The allele for tallness (T) is dominant over the recessive allele for dwarfness (t).",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "According to Mendel's Law of Dominance, when two contrasting alleles are brought together, only the dominant trait expresses in the phenotype of the F1 hybrid (Tt), while the recessive trait remains masked. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 8, Section 8.2"
      }
    ]
  },
  {
    "slug": "ch09_light_reflection_refraction",
    "num": 9,
    "title": "Light – Reflection and Refraction",
    "sub": "Physics",
    "marks": "8–9 Marks",
    "desc": "Spherical mirrors, mirror formula, refractive index, Snell's law, lenses, and optical power.",
    "questions": [
      {
        "id": "cbse10-sci-ch09-s1-001",
        "type": "mcq",
        "subtopic": "Spherical Mirrors",
        "difficulty": "Easy",
        "question": "A concave mirror produces a virtual, erect, and magnified image only when the object is placed at which specific position?",
        "options": [
          "At the Centre of Curvature (C)",
          "Between Focus (F) and Centre of Curvature (C)",
          "Between the Pole (P) and Principal Focus (F)",
          "At infinity"
        ],
        "answer": 2,
        "explanation": "In all other positions, a concave mirror forms real, inverted images. Only when an object is held close between the Pole (P) and Focus (F) does it form an erect, magnified, virtual image behind the mirror (used by dentists and in shaving mirrors).",
        "citation": "NCERT Class 10 Science, Chapter 9, Section 9.2.2 (Table 9.1)"
      },
      {
        "id": "cbse10-sci-ch09-s1-002",
        "type": "mcq",
        "subtopic": "Convex Mirrors",
        "difficulty": "Easy",
        "question": "Why are convex mirrors universally preferred as rear-view (wing) mirrors in automobiles?",
        "options": [
          "They produce magnified real images of distant vehicles",
          "They always produce an erect, diminished image and provide a much wider field of view because they curve outwards",
          "They invert images to alert the driver",
          "They focus headlight beams into parallel rays"
        ],
        "answer": 1,
        "explanation": "Convex mirrors always form erect, diminished virtual images regardless of object distance, and their outward curvature provides a significantly wider field of view than a flat plane mirror.",
        "citation": "NCERT Class 10 Science, Chapter 9, Section 9.2.3"
      },
      {
        "id": "cbse10-sci-ch09-s1-003",
        "type": "mcq",
        "subtopic": "Refractive Index",
        "difficulty": "Medium",
        "question": "The absolute refractive index of diamond is 2.42. What does this physical constant signify regarding the speed of light in diamond compared to a vacuum?",
        "options": [
          "Light travels 2.42 times faster in diamond than in vacuum",
          "The speed of light in diamond is (1 / 2.42) times the speed of light in vacuum",
          "Light cannot pass through diamond",
          "The angle of incidence inside diamond is always 2.42 radians"
        ],
        "answer": 1,
        "explanation": "Refractive index n = c / v. Therefore, v = c / 2.42. Light travels 2.42 times slower in diamond than in vacuum, giving diamond immense optical density and high light-bending capability.",
        "citation": "NCERT Class 10 Science, Chapter 9, Section 9.3.2"
      },
      {
        "id": "cbse10-sci-ch09-s1-004",
        "type": "mcq",
        "subtopic": "Power of a Lens",
        "difficulty": "Medium",
        "question": "An optometrist prescribes a corrective eyeglass lens of power -2.5 D. What is the type and focal length of this lens?",
        "options": [
          "Convex lens of focal length +40 cm",
          "Concave lens of focal length -40 cm",
          "Concave lens of focal length -25 cm",
          "Convex lens of focal length +25 cm"
        ],
        "answer": 1,
        "explanation": "P = 1 / f(in m) ⇒ f = 1 / P = 1 / (-2.5) = -0.4 m = -40 cm. A negative power and negative focal length correspond to a diverging (concave) lens used to correct myopia.",
        "citation": "NCERT Class 10 Science, Chapter 9, Section 9.3.8"
      },
      {
        "id": "cbse10-sci-ch09-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The magnification produced by a convex mirror is always positive and less than 1.\nReason (R): A convex mirror always forms a virtual, erect, and diminished image regardless of object position.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Magnification m = h' / h. For a virtual and erect image, h' is positive, so m is positive. Because the image is diminished (h' < h), the magnitude of m is strictly less than 1. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 9, Section 9.2.4"
      }
    ]
  },
  {
    "slug": "ch10_human_eye_colourful_world",
    "num": 10,
    "title": "The Human Eye and the Colourful World",
    "sub": "Physics",
    "marks": "4–5 Marks",
    "desc": "Vision defects (myopia, hypermetropia), prism dispersion, atmospheric refraction, and scattering.",
    "questions": [
      {
        "id": "cbse10-sci-ch10-s1-001",
        "type": "mcq",
        "subtopic": "Defects of Vision",
        "difficulty": "Easy",
        "question": "A student sitting on the back bench cannot read the blackboard clearly, but can easily read their textbook. Which vision defect does the student have, and which corrective lens is needed?",
        "options": [
          "Hypermetropia; corrected by a convex lens",
          "Myopia (near-sightedness); corrected by a concave lens of suitable focal length",
          "Presbyopia; corrected by a bifocal lens",
          "Cataract; corrected by surgery only"
        ],
        "answer": 1,
        "explanation": "Myopic individuals can see nearby objects distinctly but cannot see distant objects clearly. The image of distant objects forms in front of the retina. A diverging (concave) lens assists by diverging incoming rays onto the retina.",
        "citation": "NCERT Class 10 Science, Chapter 10, Section 10.2"
      },
      {
        "id": "cbse10-sci-ch10-s1-002",
        "type": "mcq",
        "subtopic": "Prism Dispersion",
        "difficulty": "Easy",
        "question": "When a narrow beam of white light passes through a triangular glass prism, which component colour deviates the least, and which deviates the most?",
        "options": [
          "Red deviates the most; Violet deviates the least",
          "Red deviates the least; Violet deviates the most",
          "Yellow deviates the most; Green deviates the least",
          "All colours undergo identical deviation"
        ],
        "answer": 1,
        "explanation": "Red light has the longest wavelength in the visible spectrum and travels fastest in glass, deviating the least. Violet light has the shortest wavelength and travels slowest, suffering the maximum angular deviation.",
        "citation": "NCERT Class 10 Science, Chapter 10, Section 10.3"
      },
      {
        "id": "cbse10-sci-ch10-s1-003",
        "type": "mcq",
        "subtopic": "Atmospheric Refraction",
        "difficulty": "Medium",
        "question": "The apparent twinkling of stars at night and the phenomenon of advanced sunrise (2 minutes early) are primarily caused by:",
        "options": [
          "Periodic internal reflections within interstellar dust",
          "Continuous atmospheric refraction of starlight through layers of air with fluctuating optical densities",
          "Dispersion of light by water droplets in clouds",
          "Gravitational lensing by the Moon"
        ],
        "answer": 1,
        "explanation": "Earth's atmosphere has layers of fluctuating temperature and air density, causing continuous refractive index variations. Starlight undergoes continuous refraction, making its apparent position fluctuate and twinkle.",
        "citation": "NCERT Class 10 Science, Chapter 10, Section 10.4"
      },
      {
        "id": "cbse10-sci-ch10-s1-004",
        "type": "mcq",
        "subtopic": "Scattering of Light",
        "difficulty": "Easy",
        "question": "Danger signal lights mounted at the top of tall buildings and railway signals are always painted red because:",
        "options": [
          "Red light is absorbed completely by water vapor",
          "Red has the longest wavelength and is scattered the least by smoke and fog particles",
          "Red travels much faster than all other colours in air",
          "Red light reflects off the ground creating shadows"
        ],
        "answer": 1,
        "explanation": "According to Rayleigh scattering, intensity of scattered light is inversely proportional to the fourth power of wavelength (I ∝ 1/λ⁴). Red light has the longest visible wavelength, undergoes minimal scattering, and remains visible over the greatest distance through smoke or fog.",
        "citation": "NCERT Class 10 Science, Chapter 10, Section 10.5"
      },
      {
        "id": "cbse10-sci-ch10-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): To an astronaut flying in outer space, the sky appears black instead of blue.\nReason (R): In outer space, there is no atmosphere to scatter incoming sunlight.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "The blue color of the sky on Earth is caused by Rayleigh scattering of sunlight by gas molecules in the atmosphere. In outer space (a vacuum), there is no atmosphere to scatter light, so no scattered rays enter the eyes, rendering the sky black. Reason explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 10, Section 10.5"
      }
    ]
  },
  {
    "slug": "ch11_electricity",
    "num": 11,
    "title": "Electricity",
    "sub": "Physics",
    "marks": "7–8 Marks",
    "desc": "Ohm's law, resistivity, series vs parallel circuits, Joule heating, and electric power.",
    "questions": [
      {
        "id": "cbse10-sci-ch11-s1-001",
        "type": "mcq",
        "subtopic": "Resistance & Resistivity",
        "difficulty": "Medium",
        "question": "A cylindrical metal wire of resistance R is stretched uniformly until its length is doubled. What will be the new resistance of the stretched wire?",
        "options": [
          "2 R",
          "4 R",
          "R / 2",
          "R / 4"
        ],
        "answer": 1,
        "explanation": "When stretched to double length (L' = 2L), its volume (V = A × L) remains constant, so the cross-sectional area halves (A' = A/2). New resistance R' = ρ (L' / A') = ρ (2L / (A/2)) = 4 × (ρL / A) = 4R.",
        "citation": "NCERT Class 10 Science, Chapter 11, Section 11.3 (Example 11.6)"
      },
      {
        "id": "cbse10-sci-ch11-s1-002",
        "type": "mcq",
        "subtopic": "Parallel vs Series Circuits",
        "difficulty": "Easy",
        "question": "Why are domestic household lighting circuits connected in parallel rather than in series?",
        "options": [
          "In parallel, if one electrical appliance fails, all other appliances continue working normally",
          "Series circuits have zero electrical resistance",
          "Parallel circuits require high voltage fuses on every appliance",
          "To force identical electrical current through appliances of varying power ratings"
        ],
        "answer": 0,
        "explanation": "In a parallel circuit: (1) each appliance receives full supply voltage (220 V), (2) appliances can be switched on/off independently, and (3) if one bulb fuses, the other parallel branches remain unbroken.",
        "citation": "NCERT Class 10 Science, Chapter 11, Section 11.5"
      },
      {
        "id": "cbse10-sci-ch11-s1-003",
        "type": "mcq",
        "subtopic": "Joule's Heating Effect",
        "difficulty": "Medium",
        "question": "According to Joule's law of heating, the heat produced in a resistor is directly proportional to:",
        "options": [
          "The square of the electric current (I²)",
          "The square root of resistance (√R)",
          "Inversely proportional to time (1/t)",
          "Inversely proportional to potential difference"
        ],
        "answer": 0,
        "explanation": "H = I²Rt. Heat generated in a conductor is directly proportional to: (1) square of current (I²), (2) resistance (R), and (3) time of current flow (t).",
        "citation": "NCERT Class 10 Science, Chapter 11, Section 11.6"
      },
      {
        "id": "cbse10-sci-ch11-s1-004",
        "type": "mcq",
        "subtopic": "Commercial Energy Unit",
        "difficulty": "Easy",
        "question": "What is the commercial unit of electrical energy, and how many Joules does 1 unit (1 kWh) equal?",
        "options": [
          "1 kWh = 3.6 × 10⁵ J",
          "1 kWh = 3.6 × 10⁶ J",
          "1 kWh = 1.0 × 10³ J",
          "1 kWh = 3.6 × 10³ J"
        ],
        "answer": 1,
        "explanation": "1 kWh = 1 kW × 1 hour = 1000 W × 3600 seconds = 3,600,000 Joules = 3.6 × 10⁶ J.",
        "citation": "NCERT Class 10 Science, Chapter 11, Section 11.7"
      },
      {
        "id": "cbse10-sci-ch11-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): An electric fuse wire is made of a lead-tin alloy having a low melting point.\nReason (R): When an excessive electric current flows during a short-circuit, Joule heating melts the fuse wire, breaking the circuit.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "A fuse is a safety device designed to melt quickly when current exceeds safe amperage limits, protecting expensive domestic appliances from fires. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 11, Section 11.6.1"
      }
    ]
  },
  {
    "slug": "ch12_magnetic_effects_electric_current",
    "num": 12,
    "title": "Magnetic Effects of Electric Current",
    "sub": "Physics",
    "marks": "6–7 Marks",
    "desc": "Magnetic field lines, solenoid, Fleming's rules, motor principle, and domestic safety circuits.",
    "questions": [
      {
        "id": "cbse10-sci-ch12-s1-001",
        "type": "mcq",
        "subtopic": "Magnetic Field Lines",
        "difficulty": "Easy",
        "question": "Why do two magnetic field lines never cross or intersect each other?",
        "options": [
          "They carry identical magnetic electric charges that repel",
          "At the intersection point, a compass needle would point simultaneously in two different directions, which is physically impossible",
          "Field lines exist only inside solid iron magnets",
          "Field lines always form discontinuous straight line segments"
        ],
        "answer": 1,
        "explanation": "The tangent to a magnetic field line shows field direction. If two lines intersected, a compass placed at that intersection would point in two different directions at once, which is an impossibility.",
        "citation": "NCERT Class 10 Science, Chapter 12, Section 12.1"
      },
      {
        "id": "cbse10-sci-ch12-s1-002",
        "type": "mcq",
        "subtopic": "Solenoid",
        "difficulty": "Medium",
        "question": "What is the nature of the magnetic field inside a long current-carrying cylindrical solenoid?",
        "options": [
          "Zero at the center and maximum at the ends",
          "Decreases rapidly towards the axis",
          "Uniform and represented by parallel, equidistant straight lines",
          "Circular concentric loops around each wire"
        ],
        "answer": 2,
        "explanation": "The field lines inside a current-carrying solenoid are parallel straight lines. This indicates that the magnetic field is uniform (identical in magnitude and direction) at all internal points.",
        "citation": "NCERT Class 10 Science, Chapter 12, Section 12.2.3"
      },
      {
        "id": "cbse10-sci-ch12-s1-003",
        "type": "mcq",
        "subtopic": "Fleming's Left-Hand Rule",
        "difficulty": "Easy",
        "question": "According to Fleming's left-hand rule, which fingers indicate the direction of Magnetic Field, Current, and Force (motion) respectively?",
        "options": [
          "Forefinger: Field; Middle finger: Current; Thumb: Force / Motion",
          "Thumb: Field; Forefinger: Current; Middle finger: Motion",
          "Middle finger: Field; Thumb: Current; Forefinger: Motion",
          "Forefinger: Motion; Middle finger: Field; Thumb: Current"
        ],
        "answer": 0,
        "explanation": "Stretch the thumb, forefinger, and middle finger of the left hand mutually perpendicular. Forefinger represents Field, center/middle finger represents Current, and Thumb points along Force/Motion.",
        "citation": "NCERT Class 10 Science, Chapter 12, Section 12.3"
      },
      {
        "id": "cbse10-sci-ch12-s1-004",
        "type": "mcq",
        "subtopic": "Domestic Electric Circuits",
        "difficulty": "Easy",
        "question": "What are the standard potential difference and frequency of domestic alternating current (AC) electricity supplied in India?",
        "options": [
          "110 V at 60 Hz",
          "220 V at 50 Hz",
          "440 V at 50 Hz",
          "220 V at 100 Hz"
        ],
        "answer": 1,
        "explanation": "In India, domestic household electricity has a potential difference of 220 V between the live wire and neutral wire, with a frequency of 50 Hz (direction of current reverses every 1/100 second).",
        "citation": "NCERT Class 10 Science, Chapter 12, Section 12.4"
      },
      {
        "id": "cbse10-sci-ch12-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): Metallic body electrical appliances (like electric press, refrigerator) are connected to an earth wire.\nReason (R): The earth wire provides a low-resistance conducting path for leakage current directly to the ground, preventing fatal electric shocks.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "The green earth wire connects appliance metallic frames to a metal plate buried deep in the ground. If insulation fails and live wire touches the metal casing, current flows safely to ground without shocking the user. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 12, Section 12.4"
      }
    ]
  },
  {
    "slug": "ch13_our_environment",
    "num": 13,
    "title": "Our Environment",
    "sub": "Biology",
    "marks": "4–5 Marks",
    "desc": "Trophic levels, 10% energy law, biological magnification, and ozone layer protection.",
    "questions": [
      {
        "id": "cbse10-sci-ch13-s1-001",
        "type": "mcq",
        "subtopic": "10% Energy Transfer Law",
        "difficulty": "Easy",
        "question": "If 10,000 Joules of solar energy is captured by green plants (producers) in a terrestrial ecosystem, how much energy will be transferred to a secondary consumer (carnivore)?",
        "options": [
          "1,000 J",
          "100 J",
          "10 J",
          "1 J"
        ],
        "answer": 1,
        "explanation": "Producers have 10,000 J. Primary consumers (herbivores) receive 10% = 1,000 J. Secondary consumers (carnivores) receive 10% of 1,000 J = 100 J.",
        "citation": "NCERT Class 10 Science, Chapter 13, Section 13.1.1"
      },
      {
        "id": "cbse10-sci-ch13-s1-002",
        "type": "mcq",
        "subtopic": "Biological Magnification",
        "difficulty": "Medium",
        "question": "Which organism in an aquatic food chain (Phytoplankton → Zooplankton → Small fish → Large bird / Human) accumulates the HIGHEST concentration of toxic non-biodegradable pesticide (DDT)?",
        "options": [
          "Phytoplankton (producers)",
          "Zooplankton (primary consumers)",
          "Small fish (secondary consumers)",
          "Large predatory bird or Human (top consumer)"
        ],
        "answer": 3,
        "explanation": "Biological magnification is the progressive increase in concentration of non-biodegradable chemicals at each successive trophic level. As humans or apex predatory birds occupy the top of the food chain, maximum accumulation occurs in their tissues.",
        "citation": "NCERT Class 10 Science, Chapter 13, Section 13.1.1"
      },
      {
        "id": "cbse10-sci-ch13-s1-003",
        "type": "mcq",
        "subtopic": "Ozone Layer",
        "difficulty": "Easy",
        "question": "What is the primary ecological hazard caused by the depletion of the stratospheric ozone layer by chlorofluorocarbons (CFCs)?",
        "options": [
          "Depletion of atmospheric carbon dioxide needed for crops",
          "Increased penetration of ultraviolet (UV-B) radiation, causing skin cancers, cataracts, and immune damage in humans",
          "Sudden drop in ocean water levels",
          "Immediate extinction of freshwater algae"
        ],
        "answer": 1,
        "explanation": "Ozone (O₃) filters high-energy solar UV radiation. Depletion of this protective shield exposes biological systems to harmful UV-B rays, causing skin cancers, cataracts, and damage to terrestrial/marine organisms.",
        "citation": "NCERT Class 10 Science, Chapter 13, Section 13.2.1"
      },
      {
        "id": "cbse10-sci-ch13-s1-004",
        "type": "mcq",
        "subtopic": "Waste Management",
        "difficulty": "Easy",
        "question": "Which of the following waste materials is completely BIODEGRADABLE?",
        "options": [
          "Plastic water bottles and polythene shopping bags",
          "Fruit peels, tea leaves, and cattle dung cakes",
          "Aluminium beverage cans",
          "DDT pesticide powder"
        ],
        "answer": 1,
        "explanation": "Substances broken down into harmless organic compounds by microbial saprophytes (bacteria and fungi) are biodegradable (fruit peels, paper, vegetable refuse). Plastics, glass, and heavy metals are non-biodegradable.",
        "citation": "NCERT Class 10 Science, Chapter 13, Section 13.2.2"
      },
      {
        "id": "cbse10-sci-ch13-s1-005",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): Food chains in nature rarely consist of more than four to five trophic levels.\nReason (R): According to the 10% law, the energy available decreases sharply at each step, leaving insufficient energy to sustain higher trophic levels.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Since 90% of energy is lost as heat at each trophic level, very little usable energy remains after 4 or 5 levels to support another population of organisms. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Science, Chapter 13, Section 13.1.1"
      }
    ]
  }
]

# -------------------------------------------------------------------------
# MATHEMATICS CURRICULUM DEFINITIONS & QUESTION VAULTS
# -------------------------------------------------------------------------

MATH_CHAPTERS = [
  {
    "slug": "ch01_real_numbers",
    "num": 1,
    "title": "Real Numbers",
    "sub": "Number Systems",
    "marks": "6 Marks",
    "desc": "Fundamental Theorem of Arithmetic, proving irrationality of √2, √3, √5, HCF and LCM relations.",
    "questions": [
      {
        "id": "cbse10-math-ch01-s1-001",
        "type": "mcq",
        "subtopic": "Fundamental Theorem of Arithmetic",
        "difficulty": "Easy",
        "question": "According to the Fundamental Theorem of Arithmetic, every composite number can be expressed as a product of primes uniquely, apart from:",
        "options": ["The magnitude of the primes", "The order in which prime factors occur", "The number of digits", "The sign of factors"],
        "answer": 1,
        "explanation": "Every composite number can be uniquely factored into primes, except for the order in which the factors appear.",
        "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.2"
      },
      {
        "id": "cbse10-math-ch01-s1-002",
        "type": "mcq",
        "subtopic": "HCF and LCM Relation",
        "difficulty": "Easy",
        "question": "If HCF(306, 657) = 9, what is LCM(306, 657)?",
        "options": ["22338", "21338", "22336", "23338"],
        "answer": 0,
        "explanation": "LCM = (a × b) / HCF = (306 × 657) / 9 = 34 × 657 = 22,338.",
        "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.2 (Exercise 1.2 Q4)"
      },
      {
        "id": "cbse10-math-ch01-s1-003",
        "type": "mcq",
        "subtopic": "Irrational Numbers",
        "difficulty": "Medium",
        "question": "Given that √3 is an irrational number, which of the following is an irrational number?",
        "options": ["5 + 2√3", "(√3 - 2)(√3 + 2)", "(√3)²", "√12 / √3"],
        "answer": 0,
        "explanation": "The sum of a non-zero rational number (5) and an irrational number (2√3) is always irrational. Options B, C, D evaluate to -1, 3, and 2 respectively (rational integers).",
        "citation": "NCERT Class 10 Mathematics, Chapter 1, Theorem 1.3"
      },
      {
        "id": "cbse10-math-ch01-s1-004",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The number 4ⁿ can never end with the digit 0 for any natural number n.\nReason (R): The prime factorisation of 4ⁿ is (2²)ⁿ = 2²ⁿ, which does not contain the prime factor 5.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "For any number to end in 0, its prime factorisation must contain both 2 and 5 (10 = 2 × 5). Since 4ⁿ has only 2 as its prime factor, it can never end with 0. Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.2"
      }
    ]
  },
  {
    "slug": "ch02_polynomials",
    "num": 2,
    "title": "Polynomials",
    "sub": "Algebra",
    "marks": "4 Marks",
    "desc": "Zeroes of quadratic polynomials, relationship between coefficients and zeroes, and graphical interpretations.",
    "questions": [
      {
        "id": "cbse10-math-ch02-s1-001",
        "type": "mcq",
        "subtopic": "Zeroes of Quadratic Polynomial",
        "difficulty": "Easy",
        "question": "If α and β are the zeroes of the quadratic polynomial p(x) = ax² + bx + c (a ≠ 0), what are the sum and product of zeroes?",
        "options": [
          "α + β = -b/a;  αβ = c/a",
          "α + β = b/a;   αβ = -c/a",
          "α + β = c/a;   αβ = b/a",
          "α + β = -c/a;  αβ = -b/a"
        ],
        "answer": 0,
        "explanation": "For any quadratic polynomial ax² + bx + c: Sum of zeroes (α + β) = -(coefficient of x) / (coefficient of x²) = -b/a; Product of zeroes (αβ) = constant term / (coefficient of x²) = c/a.",
        "citation": "NCERT Class 10 Mathematics, Chapter 2, Section 2.2"
      },
      {
        "id": "cbse10-math-ch02-s1-002",
        "type": "mcq",
        "subtopic": "Formation of Quadratic Polynomial",
        "difficulty": "Medium",
        "question": "What is the quadratic polynomial whose sum of zeroes is -3 and product of zeroes is 2?",
        "options": [
          "x² - 3x + 2",
          "x² + 3x + 2",
          "x² - 3x - 2",
          "x² + 3x - 2"
        ],
        "answer": 1,
        "explanation": "p(x) = k [x² - (Sum of zeroes)x + (Product of zeroes)] = k [x² - (-3)x + 2] = x² + 3x + 2.",
        "citation": "NCERT Class 10 Mathematics, Chapter 2, Section 2.2"
      },
      {
        "id": "cbse10-math-ch02-s1-003",
        "type": "mcq",
        "subtopic": "Geometric Meaning of Zeroes",
        "difficulty": "Easy",
        "question": "The number of real zeroes of a polynomial y = p(x) is equal to the number of points where the graph of y = p(x) intersects which axis?",
        "options": ["The x-axis", "The y-axis", "Both x and y axes", "The origin only"],
        "answer": 0,
        "explanation": "The zeroes of y = p(x) are precisely the x-coordinates of the points where the curve intersects the x-axis (where y = 0).",
        "citation": "NCERT Class 10 Mathematics, Chapter 2, Section 2.1"
      },
      {
        "id": "cbse10-math-ch02-s1-004",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The polynomial p(x) = x² + 4x + 5 has no real zeroes.\nReason (R): For p(x) = ax² + bx + c, if discriminant D = b² - 4ac < 0, the parabola does not cut the x-axis.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Here a=1, b=4, c=5. D = b² - 4ac = 16 - 20 = -4 < 0. When D < 0, there are no real zeroes. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 2, Section 2.1"
      }
    ]
  },
  {
    "slug": "ch03_linear_equations_two_variables",
    "num": 3,
    "title": "Pair of Linear Equations in Two Variables",
    "sub": "Algebra",
    "marks": "6 Marks",
    "desc": "Graphical and algebraic consistency conditions (a1/a2 ratios), substitution, and elimination methods.",
    "questions": [
      {
        "id": "cbse10-math-ch03-s1-001",
        "type": "mcq",
        "subtopic": "Consistency Conditions",
        "difficulty": "Easy",
        "question": "If the pair of linear equations a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 satisfies a₁/a₂ = b₁/b₂ ≠ c₁/c₂, what is the geometric nature of the lines and the number of solutions?",
        "options": [
          "Intersecting lines with unique solution",
          "Parallel lines with no solution (inconsistent)",
          "Coincident lines with infinitely many solutions (dependent consistent)",
          "Perpendicular lines with two solutions"
        ],
        "answer": 1,
        "explanation": "When a₁/a₂ = b₁/b₂ ≠ c₁/c₂, the lines are parallel and never meet, meaning the system has no solution and is inconsistent.",
        "citation": "NCERT Class 10 Mathematics, Chapter 3, Section 3.2 (Table 3.1)"
      },
      {
        "id": "cbse10-math-ch03-s1-002",
        "type": "mcq",
        "subtopic": "Infinite Solutions",
        "difficulty": "Medium",
        "question": "For what value of 'k' will the equations x + 2y - 3 = 0 and 5x + ky + 7 = 0 have NO solution?",
        "options": ["k = 10", "k = -10", "k = 5", "k = 15"],
        "answer": 0,
        "explanation": "For no solution: a₁/a₂ = b₁/b₂ ≠ c₁/c₂ ⇒ 1/5 = 2/k ⇒ k = 10. (And 2/10 ≠ -3/7, which holds).",
        "citation": "NCERT Class 10 Mathematics, Chapter 3, Section 3.2"
      },
      {
        "id": "cbse10-math-ch03-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The pair of equations 2x + 3y = 7 and 4x + 6y = 14 represents coincident lines.\nReason (R): If a₁/a₂ = b₁/b₂ = c₁/c₂, the pair of linear equations has infinitely many solutions.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Here 2/4 = 3/6 = 7/14 = 1/2. Because all three ratios are equal, the lines coincide and have infinite solutions. Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 3, Section 3.2"
      }
    ]
  },
  {
    "slug": "ch04_quadratic_equations",
    "num": 4,
    "title": "Quadratic Equations",
    "sub": "Algebra",
    "marks": "6–8 Marks",
    "desc": "Standard form, roots by factorisation & quadratic formula, and discriminant nature of roots.",
    "questions": [
      {
        "id": "cbse10-math-ch04-s1-001",
        "type": "mcq",
        "subtopic": "Nature of Roots",
        "difficulty": "Easy",
        "question": "For a quadratic equation ax² + bx + c = 0 (a ≠ 0), the roots are real and EQUAL if the discriminant D = b² - 4ac is:",
        "options": ["D > 0", "D = 0", "D < 0", "D ≤ -1"],
        "answer": 1,
        "explanation": "Roots are given by x = (-b ± √D) / 2a. If D = 0, both roots equal -b / 2a (two equal real roots).",
        "citation": "NCERT Class 10 Mathematics, Chapter 4, Section 4.4"
      },
      {
        "id": "cbse10-math-ch04-s1-002",
        "type": "mcq",
        "subtopic": "Discriminant Calculation",
        "difficulty": "Medium",
        "question": "If the quadratic equation 2x² - kx + 2 = 0 has two equal real roots, what are the possible values of k?",
        "options": ["k = ±4", "k = ±2", "k = ±8", "k = ±16"],
        "answer": 0,
        "explanation": "For equal roots, D = 0 ⇒ b² - 4ac = 0 ⇒ (-k)² - 4(2)(2) = 0 ⇒ k² - 16 = 0 ⇒ k² = 16 ⇒ k = ±4.",
        "citation": "NCERT Class 10 Mathematics, Chapter 4, Section 4.4 (Exercise 4.4 Q2)"
      },
      {
        "id": "cbse10-math-ch04-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The equation (x + 1)² = 2(x - 3) is a quadratic equation.\nReason (R): Any equation of the form ax² + bx + c = 0 with real coefficients and a ≠ 0 is a quadratic equation.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Expanding: x² + 2x + 1 = 2x - 6 ⇒ x² + 7 = 0. Here degree is 2 and a = 1 ≠ 0, making it a valid quadratic equation. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 4, Section 4.1"
      }
    ]
  },
  {
    "slug": "ch05_arithmetic_progressions",
    "num": 5,
    "title": "Arithmetic Progressions (AP)",
    "sub": "Algebra",
    "marks": "5–6 Marks",
    "desc": "nth term derivation [an = a + (n-1)d], sum of first n terms [Sn = n/2(2a+(n-1)d)], and word problems.",
    "questions": [
      {
        "id": "cbse10-math-ch05-s1-001",
        "type": "mcq",
        "subtopic": "nth Term of an AP",
        "difficulty": "Easy",
        "question": "What is the 30th term of the arithmetic progression 10, 7, 4, ...?",
        "options": ["97", "77", "-77", "-87"],
        "answer": 2,
        "explanation": "Here first term a = 10, common difference d = 7 - 10 = -3. a₃₀ = a + (30 - 1)d = 10 + 29(-3) = 10 - 87 = -77.",
        "citation": "NCERT Class 10 Mathematics, Chapter 5, Section 5.2"
      },
      {
        "id": "cbse10-math-ch05-s1-002",
        "type": "mcq",
        "subtopic": "Sum of n Terms",
        "difficulty": "Medium",
        "question": "What is the sum of the first 20 terms of the AP: 1, 4, 7, 10, ...?",
        "options": ["590", "600", "580", "610"],
        "answer": 0,
        "explanation": "a = 1, d = 3, n = 20. S₂₀ = (n/2) [2a + (n-1)d] = (20/2) [2(1) + 19(3)] = 10 [2 + 57] = 10 × 59 = 590.",
        "citation": "NCERT Class 10 Mathematics, Chapter 5, Section 5.3"
      },
      {
        "id": "cbse10-math-ch05-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The common difference 'd' of an AP can be positive, negative, or zero.\nReason (R): In an AP, each term is obtained by adding a fixed number 'd' to the preceding term.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "d can be positive (increasing AP), negative (decreasing AP), or zero (constant AP like 5, 5, 5...). Both statements are true and Reason defines Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 5, Section 5.1"
      }
    ]
  },
  {
    "slug": "ch06_triangles",
    "num": 6,
    "title": "Triangles",
    "sub": "Geometry",
    "marks": "8–9 Marks",
    "desc": "Basic Proportionality Theorem (Thales Theorem) and similarity criteria (AAA, SSS, SAS).",
    "questions": [
      {
        "id": "cbse10-math-ch06-s1-001",
        "type": "mcq",
        "subtopic": "Basic Proportionality Theorem (BPT)",
        "difficulty": "Medium",
        "question": "In a ΔABC, DE is drawn parallel to BC intersecting AB at D and AC at E. If AD = 1.5 cm, DB = 3 cm, and AE = 1 cm, what is the length of EC?",
        "options": ["2 cm", "2.5 cm", "3 cm", "1.5 cm"],
        "answer": 0,
        "explanation": "By BPT (Thales Theorem): AD / DB = AE / EC ⇒ 1.5 / 3 = 1 / EC ⇒ 1/2 = 1 / EC ⇒ EC = 2 cm.",
        "citation": "NCERT Class 10 Mathematics, Chapter 6, Section 6.2 (Theorem 6.1)"
      },
      {
        "id": "cbse10-math-ch06-s1-002",
        "type": "mcq",
        "subtopic": "Similarity Criteria",
        "difficulty": "Easy",
        "question": "Two triangles are similar if their corresponding angles are equal and their corresponding sides are:",
        "options": ["Equal in length", "In the same ratio (proportional)", "Perpendicular", "Parallel"],
        "answer": 1,
        "explanation": "Two polygons/triangles with the same number of sides are similar if: (1) corresponding angles are equal, and (2) corresponding sides are in the same ratio (proportional).",
        "citation": "NCERT Class 10 Mathematics, Chapter 6, Section 6.1"
      },
      {
        "id": "cbse10-math-ch06-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): All congruent triangles are similar, but all similar triangles need not be congruent.\nReason (R): Congruent triangles have corresponding sides in the ratio 1 : 1, satisfying similarity.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Congruence requires equal shapes and equal sizes (ratio 1:1). Similarity requires equal shapes (proportional sides). Hence all congruent figures are similar. Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 6, Section 6.1"
      }
    ]
  },
  {
    "slug": "ch07_coordinate_geometry",
    "num": 7,
    "title": "Coordinate Geometry",
    "sub": "Coordinate Geometry",
    "marks": "6 Marks",
    "desc": "Distance formula between two points, section formula (internal division), and midpoint applications.",
    "questions": [
      {
        "id": "cbse10-math-ch07-s1-001",
        "type": "mcq",
        "subtopic": "Distance Formula",
        "difficulty": "Easy",
        "question": "What is the straight-line distance between the points P(2, 3) and Q(4, 1)?",
        "options": ["2√2 units", "4 units", "8 units", "2 units"],
        "answer": 0,
        "explanation": "d = √[(x₂ - x₁)² + (y₂ - y₁)²] = √[(4 - 2)² + (1 - 3)²] = √[2² + (-2)²] = √[4 + 4] = √8 = 2√2 units.",
        "citation": "NCERT Class 10 Mathematics, Chapter 7, Section 7.2"
      },
      {
        "id": "cbse10-math-ch07-s1-002",
        "type": "mcq",
        "subtopic": "Midpoint Formula",
        "difficulty": "Easy",
        "question": "What are the coordinates of the midpoint of the line segment joining points A(-5, 4) and B(7, -8)?",
        "options": ["(1, -2)", "(2, -4)", "(-1, 2)", "(6, -6)"],
        "answer": 0,
        "explanation": "Midpoint M = [(x₁ + x₂)/2, (y₁ + y₂)/2] = [(-5 + 7)/2, (4 - 8)/2] = [2/2, -4/2] = (1, -2).",
        "citation": "NCERT Class 10 Mathematics, Chapter 7, Section 7.3"
      },
      {
        "id": "cbse10-math-ch07-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The distance of the point P(3, 4) from the origin O(0, 0) is 5 units.\nReason (R): The distance of any point P(x, y) from the origin is given by √(x² + y²).",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Distance from origin = √(3² + 4²) = √(9 + 16) = √25 = 5. Reason is the exact formula that verifies Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 7, Section 7.2"
      }
    ]
  },
  {
    "slug": "ch08_introduction_to_trigonometry",
    "num": 8,
    "title": "Introduction to Trigonometry",
    "sub": "Trigonometry",
    "marks": "8 Marks",
    "desc": "Trigonometric ratios of acute angles, standard angles (0°, 30°, 45°, 60°, 90°), and identities [sin²θ+cos²θ=1].",
    "questions": [
      {
        "id": "cbse10-math-ch08-s1-001",
        "type": "mcq",
        "subtopic": "Trigonometric Values",
        "difficulty": "Easy",
        "question": "What is the numerical value of (sin 30° + cos 60°)?",
        "options": ["1", "1/2", "√3", "0"],
        "answer": 0,
        "explanation": "sin 30° = 1/2 and cos 60° = 1/2. Therefore, sin 30° + cos 60° = 1/2 + 1/2 = 1.",
        "citation": "NCERT Class 10 Mathematics, Chapter 8, Section 8.3 (Table 8.1)"
      },
      {
        "id": "cbse10-math-ch08-s1-002",
        "type": "mcq",
        "subtopic": "Trigonometric Identities",
        "difficulty": "Medium",
        "question": "Which of the following fundamental trigonometric identities is mathematically correct for all 0° ≤ θ < 90°?",
        "options": [
          "1 + tan²θ = sec²θ",
          "1 + cot²θ = sec²θ",
          "sin²θ - cos²θ = 1",
          "tan²θ - 1 = sec²θ"
        ],
        "answer": 0,
        "explanation": "The three fundamental Pythagorean identities are: (1) sin²θ + cos²θ = 1, (2) 1 + tan²θ = sec²θ, and (3) 1 + cot²θ = cosec²θ.",
        "citation": "NCERT Class 10 Mathematics, Chapter 8, Section 8.4"
      },
      {
        "id": "cbse10-math-ch08-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The value of sin θ increases as θ increases from 0° to 90°.\nReason (R): In a right triangle, as acute angle θ grows larger, the opposite side (perpendicular) increases relative to the hypotenuse.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "sin 0° = 0, sin 30° = 0.5, sin 45° = 1/√2 ≈ 0.707, sin 60° = √3/2 ≈ 0.866, sin 90° = 1. Sin θ strictly increases from 0 to 1 as angle opens. Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 8, Section 8.3"
      }
    ]
  },
  {
    "slug": "ch09_some_applications_of_trigonometry",
    "num": 9,
    "title": "Some Applications of Trigonometry",
    "sub": "Trigonometry",
    "marks": "4 Marks",
    "desc": "Angle of elevation, angle of depression, and multi-point height and distance word problems.",
    "questions": [
      {
        "id": "cbse10-math-ch09-s1-001",
        "type": "mcq",
        "subtopic": "Angle of Elevation",
        "difficulty": "Easy",
        "question": "A vertical pole stands on level ground. If the height of the pole is equal to the length of its shadow, what is the angle of elevation of the sun?",
        "options": ["30°", "45°", "60°", "90°"],
        "answer": 1,
        "explanation": "Let height = h and shadow = s. tan θ = h / s. Given h = s, tan θ = 1. Since tan 45° = 1, θ = 45°.",
        "citation": "NCERT Class 10 Mathematics, Chapter 9, Section 9.1"
      },
      {
        "id": "cbse10-math-ch09-s1-002",
        "type": "mcq",
        "subtopic": "Heights & Distances",
        "difficulty": "Medium",
        "question": "From a point on the ground 30 m away from the foot of a tower, the angle of elevation of the top of the tower is 30°. What is the height of the tower?",
        "options": ["10√3 m", "30√3 m", "15 m", "20√3 m"],
        "answer": 0,
        "explanation": "tan 30° = Height / 30 ⇒ 1 / √3 = h / 30 ⇒ h = 30 / √3 = 10√3 m.",
        "citation": "NCERT Class 10 Mathematics, Chapter 9, Section 9.1 (Exercise 9.1 Q4)"
      },
      {
        "id": "cbse10-math-ch09-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The angle of elevation of an object viewed is always equal to the angle of depression of the observer from that object.\nReason (R): The line of sight forms alternate interior angles between two parallel horizontal lines.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "The horizontal line from the observer's eye is parallel to the ground horizontal line. The line of sight acts as a transversal, making angle of elevation = angle of depression (alternate interior angles). Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 9, Section 9.1"
      }
    ]
  },
  {
    "slug": "ch10_circles",
    "num": 10,
    "title": "Circles",
    "sub": "Geometry",
    "marks": "6 Marks",
    "desc": "Tangent at any point is perpendicular to radius, and lengths of tangents from external points are equal.",
    "questions": [
      {
        "id": "cbse10-math-ch10-s1-001",
        "type": "mcq",
        "subtopic": "Tangent Properties",
        "difficulty": "Easy",
        "question": "The tangent at any point of a circle is always perpendicular to which geometric line segment through the point of contact?",
        "options": ["The chord", "The radius", "The diameter extended outside", "The secant line"],
        "answer": 1,
        "explanation": "Theorem 10.1: The tangent at any point of a circle is perpendicular to the radius through the point of contact (Angle between radius and tangent = 90°).",
        "citation": "NCERT Class 10 Mathematics, Chapter 10, Theorem 10.1"
      },
      {
        "id": "cbse10-math-ch10-s1-002",
        "type": "mcq",
        "subtopic": "External Tangents",
        "difficulty": "Easy",
        "question": "From an external point P, tangents PA and PB are drawn to a circle. What is the relation between the lengths of PA and PB?",
        "options": ["PA = PB", "PA > PB", "PA + PB = Radius", "PA = 2 PB"],
        "answer": 0,
        "explanation": "Theorem 10.2: The lengths of tangents drawn from an external point to a circle are equal (PA = PB).",
        "citation": "NCERT Class 10 Mathematics, Chapter 10, Theorem 10.2"
      },
      {
        "id": "cbse10-math-ch10-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): From a point lying inside a circle, exactly two tangents can be drawn to the circle.\nReason (R): A tangent to a circle touches the circle at exactly one point.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true.",
          "Both (A) and (R) are false."
        ],
        "answer": 2,
        "explanation": "Assertion (A) is completely FALSE: From a point inside a circle, NO tangent can be drawn (all lines cut as secants). Two tangents can be drawn only from an EXTERNAL point. Reason (R) is TRUE: Tangent touches at exactly one point.",
        "citation": "NCERT Class 10 Mathematics, Chapter 10, Section 10.2"
      }
    ]
  },
  {
    "slug": "ch11_areas_related_to_circles",
    "num": 11,
    "title": "Areas Related to Circles",
    "sub": "Mensuration",
    "marks": "4 Marks",
    "desc": "Area of sector of a circle, length of an arc, area of segment of a circle.",
    "questions": [
      {
        "id": "cbse10-math-ch11-s1-001",
        "type": "mcq",
        "subtopic": "Sector Area",
        "difficulty": "Easy",
        "question": "What is the formula for the area of a sector of angle θ of a circle with radius r?",
        "options": [
          "(θ / 360°) × πr²",
          "(θ / 180°) × πr²",
          "(θ / 360°) × 2πr",
          "(θ / 720°) × 2πr²"
        ],
        "answer": 0,
        "explanation": "Area of a sector of angle θ = (θ / 360°) × πr². Length of corresponding arc = (θ / 360°) × 2πr.",
        "citation": "NCERT Class 10 Mathematics, Chapter 11, Section 11.2"
      },
      {
        "id": "cbse10-math-ch11-s1-002",
        "type": "mcq",
        "subtopic": "Clock Problem",
        "difficulty": "Medium",
        "question": "The minute hand of a clock is 14 cm long. What is the area swept by the minute hand in 5 minutes? (Use π = 22/7)",
        "options": ["154 / 3 cm²", "154 cm²", "77 / 3 cm²", "308 / 3 cm²"],
        "answer": 0,
        "explanation": "In 60 mins, minute hand sweeps 360°. In 5 mins, angle θ = (360° / 60) × 5 = 30°. Area = (30/360) × (22/7) × 14 × 14 = (1/12) × 22 × 2 × 14 = (1/12) × 616 = 154 / 3 cm² ≈ 51.33 cm².",
        "citation": "NCERT Class 10 Mathematics, Chapter 11, Section 11.2 (Exercise 11.1 Q2)"
      },
      {
        "id": "cbse10-math-ch11-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): The length of the arc of a semicircle of radius r is πr.\nReason (R): The angle subtended by a semicircle at the center is 180°.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Arc length = (θ / 360°) × 2πr = (180° / 360°) × 2πr = (1/2) × 2πr = πr. Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 11, Section 11.2"
      }
    ]
  },
  {
    "slug": "ch12_surface_areas_volumes",
    "num": 12,
    "title": "Surface Areas and Volumes",
    "sub": "Mensuration",
    "marks": "6 Marks",
    "desc": "Surface areas and volumes of combinations of solids (cubes, cuboids, spheres, hemispheres, right circular cylinders/cones).",
    "questions": [
      {
        "id": "cbse10-math-ch12-s1-001",
        "type": "mcq",
        "subtopic": "Combination of Solids",
        "difficulty": "Medium",
        "question": "A solid toy is in the form of a hemisphere surmounted by a right circular cone of the same radius r. If the height of the cone is h, what is the total volume of the solid toy?",
        "options": [
          "(1/3) πr² (h + 2r)",
          "(2/3) πr² (h + r)",
          "πr² (h + 2r)",
          "(1/3) πr³ (h + 2)"
        ],
        "answer": 0,
        "explanation": "Total Volume = Volume of Cone + Volume of Hemisphere = (1/3)πr²h + (2/3)πr³ = (1/3)πr² (h + 2r).",
        "citation": "NCERT Class 10 Mathematics, Chapter 12, Section 12.2"
      },
      {
        "id": "cbse10-math-ch12-s1-002",
        "type": "mcq",
        "subtopic": "Sphere & Cylinder",
        "difficulty": "Medium",
        "question": "A solid metallic sphere of radius 3 cm is melted and recast into a cylinder of radius 2 cm. What is the height of the cylinder?",
        "options": ["9 cm", "4.5 cm", "6 cm", "12 cm"],
        "answer": 0,
        "explanation": "Volume of sphere = Volume of cylinder ⇒ (4/3)π R³ = π r² h ⇒ (4/3) × 27 = 4 × h ⇒ 36 = 4h ⇒ h = 9 cm.",
        "citation": "NCERT Class 10 Mathematics, Chapter 12, Section 12.3"
      },
      {
        "id": "cbse10-math-ch12-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): When a solid cylinder is reshaped into a wire, its total volume remains invariant.\nReason (R): Reshaping changes surface area, but the amount of matter (volume) is conserved.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "Melting or recasting solids into different shapes conserves volume (Volume of new solid = Volume of original solid). Reason explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 12, Section 12.3"
      }
    ]
  },
  {
    "slug": "ch13_statistics",
    "num": 13,
    "title": "Statistics",
    "sub": "Statistics & Probability",
    "marks": "7 Marks",
    "desc": "Mean, median, and mode of grouped data, assumed mean method, and empirical relation.",
    "questions": [
      {
        "id": "cbse10-math-ch13-s1-001",
        "type": "mcq",
        "subtopic": "Empirical Relationship",
        "difficulty": "Easy",
        "question": "What is the standard empirical relationship between the three measures of central tendency for a moderately skewed distribution?",
        "options": [
          "3 Median = Mode + 2 Mean",
          "3 Mode = Median + 2 Mean",
          "Mode = 3 Mean - 2 Median",
          "Mean = 3 Median - 2 Mode"
        ],
        "answer": 0,
        "explanation": "The standard empirical formula connecting the three central tendencies is: 3 Median = Mode + 2 Mean (or Mode = 3 Median - 2 Mean).",
        "citation": "NCERT Class 10 Mathematics, Chapter 13, Section 13.4"
      },
      {
        "id": "cbse10-math-ch13-s1-002",
        "type": "mcq",
        "subtopic": "Modal Class",
        "difficulty": "Easy",
        "question": "In a frequency distribution of grouped data, what is the 'modal class'?",
        "options": [
          "The class interval with the minimum frequency",
          "The class interval with the highest (maximum) frequency",
          "The middle class interval regardless of frequency",
          "The first class interval of the dataset"
        ],
        "answer": 1,
        "explanation": "Mode is the value that appears with the highest frequency. In grouped data, the class interval having the highest frequency is termed the modal class.",
        "citation": "NCERT Class 10 Mathematics, Chapter 13, Section 13.3"
      },
      {
        "id": "cbse10-math-ch13-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): If the mode of a given dataset is 24 and the mean is 24, then its median is also 24.\nReason (R): 3 Median = Mode + 2 Mean for any moderately symmetric distribution.",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "3 Median = 24 + 2(24) = 24 + 48 = 72 ⇒ Median = 72 / 3 = 24. For a perfectly symmetric distribution, Mean = Median = Mode. Reason correctly explains Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 13, Section 13.4"
      }
    ]
  },
  {
    "slug": "ch14_probability",
    "num": 14,
    "title": "Probability",
    "sub": "Statistics & Probability",
    "marks": "4 Marks",
    "desc": "Classical probability definition, simple events, coin tosses, fair dice rolls, and 52-card deck problems.",
    "questions": [
      {
        "id": "cbse10-math-ch14-s1-001",
        "type": "mcq",
        "subtopic": "Range of Probability",
        "difficulty": "Easy",
        "question": "For any random event E, the probability P(E) satisfies which mandatory inequality?",
        "options": [
          "0 ≤ P(E) ≤ 1",
          "-1 ≤ P(E) ≤ 1",
          "0 < P(E) < 1",
          "1 ≤ P(E) ≤ 100"
        ],
        "answer": 0,
        "explanation": "The probability of an impossible event is 0, and the probability of a sure (certain) event is 1. The probability of any event always lies within the inclusive range: 0 ≤ P(E) ≤ 1. It can never be negative or exceed 1.",
        "citation": "NCERT Class 10 Mathematics, Chapter 14, Section 14.1"
      },
      {
        "id": "cbse10-math-ch14-s1-002",
        "type": "mcq",
        "subtopic": "Cards Probability",
        "difficulty": "Medium",
        "question": "A card is drawn at random from a well-shuffled standard deck of 52 playing cards. What is the probability of drawing a red face card?",
        "options": ["3 / 26", "3 / 13", "1 / 2", "6 / 13"],
        "answer": 0,
        "explanation": "Total cards = 52. Face cards are Jacks, Queens, and Kings (3 per suit). Red suits are Hearts (3) and Diamonds (3), giving a total of 6 red face cards. Probability = 6 / 52 = 3 / 26.",
        "citation": "NCERT Class 10 Mathematics, Chapter 14, Section 14.1 (Exercise 14.1 Q14)"
      },
      {
        "id": "cbse10-math-ch14-s1-003",
        "type": "assertion_reasoning",
        "subtopic": "Assertion & Reasoning",
        "difficulty": "Board Standard",
        "question": "Assertion (A): If P(E) = 0.05, then the probability of 'not E', P(Ē), is 0.95.\nReason (R): For any event E, P(E) + P(Ē) = 1 (complementary events).",
        "options": [
          "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
          "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
          "(A) is true, but (R) is false.",
          "(A) is false, but (R) is true."
        ],
        "answer": 0,
        "explanation": "P(Ē) = 1 - P(E) = 1 - 0.05 = 0.95. Reason is the fundamental complementary event rule that directly verifies Assertion.",
        "citation": "NCERT Class 10 Mathematics, Chapter 14, Section 14.1"
      }
    ]
  }
]

print("Math chapters array defined.")
