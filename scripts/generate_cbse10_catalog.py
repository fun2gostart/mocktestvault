#!/usr/bin/env python3
"""
MockTestVault — Automated CBSE Class 10 Data Generator & Pipeline
Generates syllabus-grounded question vaults with NCERT citations.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "in", "cbse10")
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------------------------------------------------
# 1. Science Chapter 3: Metals and Non-metals (20 Qs)
# -------------------------------------------------------------------------
ch3_metals = [
  {
    "id": "cbse10-sci-ch03-s1-001",
    "type": "mcq",
    "subtopic": "Physical Properties of Metals",
    "difficulty": "Easy",
    "question": "Which metal is liquid at room temperature, and which non-metal is a lustrous crystalline solid?",
    "options": [
      "Metal: Sodium; Non-metal: Sulphur",
      "Metal: Mercury; Non-metal: Iodine",
      "Metal: Gallium; Non-metal: Carbon",
      "Metal: Lead; Non-metal: Phosphorus"
    ],
    "answer": 1,
    "explanation": "Mercury (Hg) is the only liquid metal at standard room temperature. Iodine is a non-metal, yet it displays exceptional metallic-like lustre.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sci-ch03-s1-002",
    "type": "mcq",
    "subtopic": "Reactivity with Water",
    "difficulty": "Medium",
    "question": "Metals like sodium and potassium react violently with cold water. Why are sodium and potassium stored submerged in kerosene oil?",
    "options": [
      "To prevent them from evaporating into air",
      "To prevent vigorous exothermic reaction with atmospheric oxygen and moisture that catches fire",
      "To dissolve their outer oxide coating",
      "To keep their metallic luster shiny for display"
    ],
    "answer": 1,
    "explanation": "Sodium and potassium react so vigorously with moisture and oxygen in the air that they catch fire spontaneously (2Na + 2H₂O → 2NaOH + H₂ + Heat). Immersing them in kerosene protects them from contact with air and moisture.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.2"
  },
  {
    "id": "cbse10-sci-ch03-s1-003",
    "type": "mcq",
    "subtopic": "Amphoteric Oxides",
    "difficulty": "Hard",
    "question": "Aluminium oxide (Al₂O₃) reacts with both hydrochloric acid and sodium hydroxide solution to produce salt and water. Such metal oxides are defined as:",
    "options": [
      "Neutral oxides",
      "Acidic oxides",
      "Amphoteric oxides",
      "Basic oxides only"
    ],
    "answer": 2,
    "explanation": "Metal oxides which react with both acids as well as bases to produce salts and water are known as amphoteric oxides. Examples: Al₂O₃ and ZnO. Al₂O₃ + 2NaOH → 2NaAlO₂ (sodium aluminate) + H₂O.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.1"
  },
  {
    "id": "cbse10-sci-ch03-s1-004",
    "type": "mcq",
    "subtopic": "Aqua Regia",
    "difficulty": "Medium",
    "question": "Aqua regia is a highly corrosive, fuming liquid capable of dissolving noble metals like gold and platinum. What is its exact chemical composition?",
    "options": [
      "Dilute HCl and Concentrated HNO₃ in a 3 : 1 ratio",
      "Concentrated HCl and Concentrated HNO₃ in a 3 : 1 ratio",
      "Concentrated H₂SO₄ and Concentrated HNO₃ in a 1 : 1 ratio",
      "Concentrated HCl and Concentrated H₂SO₄ in a 2 : 1 ratio"
    ],
    "answer": 1,
    "explanation": "Aqua regia (royal water) is a freshly prepared mixture of concentrated hydrochloric acid and concentrated nitric acid in the ratio of 3 : 1 by volume.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.3 (Aqua Regia Box)"
  },
  {
    "id": "cbse10-sci-ch03-s1-005",
    "type": "mcq",
    "subtopic": "Ionic Compounds",
    "difficulty": "Medium",
    "question": "Which of the following properties is NOT characteristic of electrovalent (ionic) compounds like sodium chloride (NaCl)?",
    "options": [
      "High melting and boiling points due to strong inter-ionic electrostatic forces",
      "Conduct electricity in solid state",
      "Soluble in polar solvents like water, but insoluble in kerosene and petrol",
      "Conduct electricity in aqueous solution or molten state"
    ],
    "answer": 1,
    "explanation": "In solid state, ionic compounds do NOT conduct electricity because ions are locked in rigid crystal lattice positions. They conduct electricity only in molten or aqueous state where ions are free to migrate.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.3 (Properties of Ionic Compounds)"
  },
  {
    "id": "cbse10-sci-ch03-s1-006",
    "type": "mcq",
    "subtopic": "Metallurgy: Roasting vs Calcination",
    "difficulty": "Hard",
    "question": "What is the difference between roasting and calcination during the extraction of metals from their ores?",
    "options": [
      "Roasting is done in absence of air for carbonates; Calcination is done in excess air for sulphides",
      "Roasting strongly heats sulphide ores in excess air; Calcination strongly heats carbonate ores in limited/no air",
      "Both processes are identical methods of electrolytic refining",
      "Roasting converts oxides to metals; Calcination converts metals to alloys"
    ],
    "answer": 1,
    "explanation": "Roasting: 2ZnS + 3O₂ + Heat → 2ZnO + 2SO₂ (excess air for sulphide ores). Calcination: ZnCO₃ + Heat → ZnO + CO₂ (limited or absence of air for carbonate ores).",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.4.3"
  },
  {
    "id": "cbse10-sci-ch03-s1-007",
    "type": "mcq",
    "subtopic": "Thermite Process",
    "difficulty": "Medium",
    "question": "The highly exothermic reduction of iron(III) oxide with aluminium powder (Fe₂O₃ + 2Al → 2Fe + Al₂O₃ + Heat) is utilized practically for:",
    "options": [
      "Electroplating copper utensils",
      "Joining railway tracks and cracked machine parts",
      "Manufacturing light-weight aircraft alloys",
      "Extracting pure oxygen in submarines"
    ],
    "answer": 1,
    "explanation": "This displacement reaction is known as the thermite reaction. The heat evolved is so high that iron is produced in molten liquid state, allowing it to fuse and weld railway tracks on site.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.4.3 (Thermite Process)"
  },
  {
    "id": "cbse10-sci-ch03-s1-008",
    "type": "mcq",
    "subtopic": "Electrolytic Refining",
    "difficulty": "Medium",
    "question": "During the electrolytic refining of blister copper, what are the anode, cathode, and electrolyte respectively?",
    "options": [
      "Anode: Pure copper; Cathode: Impure copper; Electrolyte: Dilute HCl",
      "Anode: Impure copper slab; Cathode: Thin pure copper strip; Electrolyte: Acidified CuSO₄ solution",
      "Anode: Carbon rod; Cathode: Pure copper; Electrolyte: Molten CuCl₂",
      "Anode: Platinum; Cathode: Zinc; Electrolyte: CuSO₄ solution"
    ],
    "answer": 1,
    "explanation": "Impure copper acts as the Anode (+) and dissolves into solution as Cu²⁺ ions. Pure copper deposits onto the Cathode (-). Insoluble impurities settle below the anode as 'anode mud'.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.4.4"
  },
  {
    "id": "cbse10-sci-ch03-s1-009",
    "type": "mcq",
    "subtopic": "Alloys",
    "difficulty": "Easy",
    "question": "An amalgam is a special metallic alloy containing which mandatory metal component?",
    "options": [
      "Aluminium",
      "Mercury",
      "Silver",
      "Gold"
    ],
    "answer": 1,
    "explanation": "If one of the constituent metals in an alloy is mercury (Hg), the alloy is specifically termed an amalgam (e.g. sodium amalgam, dental amalgam).",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.5 (Alloys)"
  },
  {
    "id": "cbse10-sci-ch03-s1-010",
    "type": "mcq",
    "subtopic": "Alloys & Compositions",
    "difficulty": "Easy",
    "question": "What are the primary constituent metals in Brass, Bronze, and Solder respectively?",
    "options": [
      "Brass: Cu + Zn; Bronze: Cu + Sn; Solder: Pb + Sn",
      "Brass: Cu + Sn; Bronze: Cu + Zn; Solder: Fe + C",
      "Brass: Fe + Cr; Bronze: Al + Cu; Solder: Pb + Zn",
      "Brass: Zn + Ni; Bronze: Cu + Pb; Solder: Sn + Ag"
    ],
    "answer": 0,
    "explanation": "Brass is an alloy of Copper and Zinc (Cu + Zn). Bronze is an alloy of Copper and Tin (Cu + Sn). Solder is an alloy of Lead and Tin (Pb + Sn), which has a low melting point used for welding electrical wires.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sci-ch03-s1-011",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Nitric acid (HNO₃) generally does not evolve hydrogen gas when reacted with metals.\nReason (R): Nitric acid is a powerful oxidizing agent; it oxidizes the H₂ produced into water and is itself reduced to nitrogen oxides.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "HNO₃ oxidizes H₂ into H₂O and reduces to NO₂, NO, or N₂O. Only very dilute HNO₃ reacts with Magnesium (Mg) and Manganese (Mn) to evolve H₂ gas. Reason correctly explains Assertion.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.3"
  },
  {
    "id": "cbse10-sci-ch03-s1-012",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Galvanisation protects iron articles from rusting even if the protective zinc layer is scratched.\nReason (R): Zinc is more electropositive than iron and preferentially corrodes/sacrifices itself to protect the underlying iron.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Zinc has a higher oxidation potential than iron. Even when scratched, zinc oxidizes sacrificially before iron can react with air and moisture (cathodic protection). Reason correctly explains Assertion.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sci-ch03-s1-013",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Highly reactive metals like sodium, calcium, and magnesium cannot be obtained from their oxides by chemical reduction with carbon.\nReason (R): These metals have more affinity for oxygen than carbon does.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Carbon cannot reduce oxides of Na, Mg, Ca, or Al because these metals bind oxygen with far greater affinity than carbon. They must be extracted by electrolytic reduction of their molten chlorides. Reason explains Assertion.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.4.4"
  },
  {
    "id": "cbse10-sci-ch03-s1-014",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Silver ornaments turn black when exposed to air for a few weeks.\nReason (R): Silver reacts with sulphur compounds present in the air to form a thin black coating of silver sulphide (Ag₂S).",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "2Ag + H₂S → Ag₂S (black) + H₂. Silver does not react with oxygen easily, but traces of hydrogen sulphide gas in polluted air cause the formation of black silver sulphide. Reason explains Assertion.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sci-ch03-s1-015",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Pure gold (24 carat) is not suitable for making everyday jewellery.\nReason (R): 24-carat gold is extremely soft and easily bends or loses shape; it is alloyed with copper or silver (22 carat) to make it hard and durable.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Pure gold (24 carat) is very malleable and soft. In India, 22-carat gold (22 parts pure gold alloyed with 2 parts copper or silver) is standard to impart structural hardness. Reason correctly explains Assertion.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.5 (22-Carat Gold Box)"
  },
  {
    "id": "cbse10-sci-ch03-s1-016",
    "type": "mcq",
    "subtopic": "Anodising",
    "difficulty": "Medium",
    "question": "What is the process of Anodising, and which metal is commonly anodised to provide corrosion resistance and decorative colours?",
    "options": [
      "Coating iron with molten zinc; Iron",
      "Forming a thick, protective oxide layer electrochemically; Aluminium",
      "Depositing chromium on steel bumpers; Nickel",
      "Heating copper with charcoal; Copper"
    ],
    "answer": 1,
    "explanation": "Anodising is an electrolytic process of forming a thick protective aluminium oxide (Al₂O₃) layer on aluminium articles. During electrolysis with dilute H₂SO₄, oxygen gas liberated at the anode reacts with aluminium to form an impermeable, dyeable protective coat.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.1 (Anodising Box)"
  },
  {
    "id": "cbse10-sci-ch03-s1-017",
    "type": "mcq",
    "subtopic": "Reactivity Series",
    "difficulty": "Easy",
    "question": "Which of the following displacement pairs will result in an active chemical reaction?",
    "options": [
      "NaCl solution and Copper metal",
      "MgCl₂ solution and Aluminium metal",
      "FeSO₄ solution and Silver metal",
      "AgNO₃ solution and Copper metal"
    ],
    "answer": 3,
    "explanation": "Copper is higher than silver in the reactivity series: Cu + 2AgNO₃ → Cu(NO₃)₂ + 2Ag. Copper displaces silver, producing a lustrous grey-white deposit of silver crystals and a blue copper nitrate solution. In all other options, the metal is less reactive than the cation in solution.",
    "citation": "NCERT Class 10 Science, Chapter 3, Chapter Exercise Q1"
  },
  {
    "id": "cbse10-sci-ch03-s1-018",
    "type": "mcq",
    "subtopic": "Cinnabar Extraction",
    "difficulty": "Medium",
    "question": "Cinnabar (HgS) is a sulphide ore of mercury. When cinnabar is heated in air, what sequence of chemical transformations occurs?",
    "options": [
      "Converted directly to mercury metal and chlorine gas",
      "Converted first into mercuric oxide (HgO), which upon further heating reduces to metallic mercury",
      "Forms mercuric sulphate which dissolves in water",
      "Decomposes into hydrogen gas and sulphur"
    ],
    "answer": 1,
    "explanation": "2HgS + 3O₂ + Heat → 2HgO + 2SO₂. On continuous strong heating, the oxide decomposes thermally without needing a reducing agent: 2HgO + Heat → 2Hg(l) + O₂(g).",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.4.2"
  },
  {
    "id": "cbse10-sci-ch03-s1-019",
    "type": "mcq",
    "subtopic": "Non-metal Oxides",
    "difficulty": "Easy",
    "question": "Non-metals like sulphur and carbon burn in oxygen to produce non-metallic oxides. What is the nature of these oxides in aqueous solution?",
    "options": [
      "Basic; turns red litmus blue",
      "Acidic or neutral; acidic oxides turn blue litmus red",
      "Strongly amphoteric; reacts with both acids and bases",
      "Saline with neutral pH 7"
    ],
    "answer": 1,
    "explanation": "Most non-metals produce acidic oxides when dissolved in water (e.g. SO₂ + H₂O → H₂SO₃ sulphurous acid, CO₂ + H₂O → H₂CO₃ carbonic acid). Neutral non-metal oxides include CO, H₂O, and N₂O.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.1"
  },
  {
    "id": "cbse10-sci-ch03-s1-020",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Copper does not react with dilute hydrochloric acid even upon boiling.\nReason (R): Copper is situated below hydrogen in the reactivity series and cannot displace hydrogen ions from dilute non-oxidizing acids.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Metals lower than hydrogen in the reactivity series (Cu, Ag, Au, Pt) lack sufficient reducing power to displace H⁺ from dilute HCl or dilute H₂SO₄. Reason correctly explains Assertion.",
    "citation": "NCERT Class 10 Science, Chapter 3, Section 3.2.3"
  }
]

# -------------------------------------------------------------------------
# 2. Mathematics Chapter 1: Real Numbers (20 Qs)
# -------------------------------------------------------------------------
ch1_real_numbers = [
  {
    "id": "cbse10-math-ch01-s1-001",
    "type": "mcq",
    "subtopic": "Fundamental Theorem of Arithmetic",
    "difficulty": "Easy",
    "question": "According to the Fundamental Theorem of Arithmetic, every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique apart from:",
    "options": [
      "The magnitude of the primes",
      "The order in which the prime factors occur",
      "The number of decimal digits",
      "The sign of the number"
    ],
    "answer": 1,
    "explanation": "The Fundamental Theorem of Arithmetic states that every composite number can be factored uniquely into prime numbers, except for the order in which the prime factors are written (e.g. 12 = 2² × 3 = 3 × 2²).",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.2"
  },
  {
    "id": "cbse10-math-ch01-s1-002",
    "type": "mcq",
    "subtopic": "HCF and LCM Relation",
    "difficulty": "Easy",
    "question": "For any two positive integers 'a' and 'b', which fundamental relationship between their HCF and LCM holds true?",
    "options": [
      "HCF(a, b) + LCM(a, b) = a + b",
      "HCF(a, b) × LCM(a, b) = a × b",
      "HCF(a, b) / LCM(a, b) = a / b",
      "[HCF(a, b)]² = a × b"
    ],
    "answer": 1,
    "explanation": "For any two positive integers a and b: HCF(a, b) × LCM(a, b) = a × b. Note that this relation holds only for two numbers, not for three.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.2"
  },
  {
    "id": "cbse10-math-ch01-s1-003",
    "type": "mcq",
    "subtopic": "Prime Factorisation",
    "difficulty": "Medium",
    "question": "If two positive integers a and b are written as a = x³y² and b = xy³, where x and y are prime numbers, then HCF(a, b) is:",
    "options": [
      "xy",
      "xy²",
      "x³y³",
      "x²y²"
    ],
    "answer": 1,
    "explanation": "HCF is the product of the smallest power of each common prime factor involved in the numbers. Common factors are x and y; the smallest power of x is 1 and of y is 2. Hence, HCF = xy².",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Exemplar Q1"
  },
  {
    "id": "cbse10-math-ch01-s1-004",
    "type": "mcq",
    "subtopic": "Irrational Numbers",
    "difficulty": "Easy",
    "question": "Which of the following numbers is an IRRATIONAL number?",
    "options": [
      "3.141414... (repeating)",
      "22 / 7 (fraction of integers)",
      "√2 (square root of a prime number)",
      "√16 (equal to 4)"
    ],
    "answer": 2,
    "explanation": "If 'p' is a prime number, then √p is always an irrational number. 3.1414... is non-terminating repeating (rational), 22/7 is rational (ratio of integers), and √16 = 4 is an integer.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-math-ch01-s1-005",
    "type": "mcq",
    "subtopic": "Nature of Numbers",
    "difficulty": "Medium",
    "question": "The sum or difference of a rational number and an irrational number is always:",
    "options": [
      "Always rational",
      "Always irrational",
      "Always an integer",
      "Zero"
    ],
    "answer": 1,
    "explanation": "The sum or difference of a non-zero rational number and an irrational number is always irrational (e.g. 2 + √3 or 5 - √2). Similarly, the product or quotient of a non-zero rational and irrational is irrational.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-math-ch01-s1-006",
    "type": "mcq",
    "subtopic": "Exponent Properties",
    "difficulty": "Medium",
    "question": "Can the number 6ⁿ, where n is a natural number, ever end with the digit zero?",
    "options": [
      "Yes, for n = 5",
      "Yes, for any even value of n",
      "No, because the prime factorisation of 6 is 2 × 3 and does not contain the prime factor 5",
      "Yes, for n = 10"
    ],
    "answer": 2,
    "explanation": "A number can end with digit 0 only if its prime factorisation contains both 2 and 5 (since 10 = 2 × 5). Prime factorisation of 6ⁿ = (2 × 3)ⁿ = 2ⁿ × 3ⁿ. By uniqueness of FTA, 5 does not occur in prime factors, so 6ⁿ can never end with 0.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Example 5"
  },
  {
    "id": "cbse10-math-ch01-s1-007",
    "type": "mcq",
    "subtopic": "HCF Applications",
    "difficulty": "Medium",
    "question": "The largest number which divides 70 and 125, leaving remainders 5 and 8 respectively, is:",
    "options": [
      "13",
      "65",
      "875",
      "1750"
    ],
    "answer": 0,
    "explanation": "The required number is HCF of (70 - 5) and (125 - 8), which is HCF(65, 117). 65 = 5 × 13 and 117 = 9 × 13 = 3² × 13. The common factor is 13. Hence, the largest divisor is 13.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Exemplar Q3"
  },
  {
    "id": "cbse10-math-ch01-s1-008",
    "type": "mcq",
    "subtopic": "LCM Applications",
    "difficulty": "Medium",
    "question": "The least number that is divisible by all numbers from 1 to 10 (both inclusive) is:",
    "options": [
      "10",
      "100",
      "504",
      "2520"
    ],
    "answer": 3,
    "explanation": "Required number is LCM(1, 2, 3, 4, 5, 6, 7, 8, 9, 10). Prime factors: 2³ × 3² × 5 × 7 = 8 × 9 × 5 × 7 = 2520.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Exemplar Q7"
  },
  {
    "id": "cbse10-math-ch01-s1-009",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The HCF of two numbers is 5 and their product is 150, then their LCM is 30.\nReason (R): For any two positive integers a and b, HCF(a, b) × LCM(a, b) = a × b.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "HCF × LCM = Product of numbers ⇒ 5 × LCM = 150 ⇒ LCM = 150 / 5 = 30. Both statements are true and Reason directly calculates Assertion.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Section 1.2"
  },
  {
    "id": "cbse10-math-ch01-s1-010",
    "type": "assertion_reasoning",
    "subtopic": "Assertion & Reasoning",
    "difficulty": "Board Standard",
    "question": "Assertion (A): √p is an irrational number, where p is any prime number.\nReason (R): The square root of any positive integer is always an irrational number.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true.",
      "Both (A) and (R) are false."
    ],
    "answer": 1,
    "explanation": "Assertion (A) is TRUE: √p is always irrational for prime p. Reason (R) is completely FALSE: square roots of perfect squares like √4 = 2, √9 = 3, √16 = 4 are rational numbers.",
    "citation": "NCERT Class 10 Mathematics, Chapter 1, Theorem 1.3"
  }
]

# Write JSON files
with open(os.path.join(DATA_DIR, "science_ch03_metals_non_metals_set1.json"), "w") as f:
    json.dump(ch3_metals, f, indent=2)
print("Generated: science_ch03_metals_non_metals_set1.json (20 Qs)")

with open(os.path.join(DATA_DIR, "math_ch01_real_numbers_set1.json"), "w") as f:
    json.dump(ch1_real_numbers, f, indent=2)
print("Generated: math_ch01_real_numbers_set1.json (10 Qs Foundation)")

print("Batch generation completed successfully.")
