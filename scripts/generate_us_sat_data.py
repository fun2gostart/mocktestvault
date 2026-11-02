#!/usr/bin/env python3
"""
Generates authentic Digital SAT question sets for the US Portal:
1. digital_sat_math_set1.json (20 Questions)
2. digital_sat_reading_set1.json (20 Questions)
Aligned with official College Board Digital SAT Specifications.
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_DIR = os.path.join(BASE_DIR, "data", "us", "sat")
os.makedirs(US_DATA_DIR, exist_ok=True)

# =============================================================================
# DIGITAL SAT MATH MODULE 1 & 2 (20 Questions)
# Domains: Algebra, Advanced Math, Problem-Solving & Data Analysis, Geometry & Trig
# =============================================================================

sat_math_questions = [
  {
    "id": "sat-math-001",
    "type": "mcq",
    "subtopic": "Linear Equations in One Variable (Algebra)",
    "difficulty": "Easy",
    "question": "If 4(x - 3) + 7 = 3x - 1, what is the value of x?",
    "options": ["4", "6", "8", "-4"],
    "answer": 0,
    "explanation": "Expand the left side: 4x - 12 + 7 = 3x - 1 -> 4x - 5 = 3x - 1. Subtract 3x from both sides: x - 5 = -1. Add 5 to both sides: x = 4.",
    "citation": "College Board Digital SAT Math Specification — Heart of Algebra"
  },
  {
    "id": "sat-math-002",
    "type": "mcq",
    "subtopic": "Linear Functions & Slope-Intercept Form (Algebra)",
    "difficulty": "Easy",
    "question": "A line in the xy-plane passes through the points (2, 5) and (6, 17). What is the y-intercept of the line?",
    "options": ["(0, -1)", "(0, 1)", "(0, 3)", "(0, -3)"],
    "answer": 0,
    "explanation": "Slope m = (17 - 5) / (6 - 2) = 12 / 4 = 3. Using point-slope form with (2, 5): y - 5 = 3(x - 2) -> y = 3x - 6 + 5 -> y = 3x - 1. The y-intercept is (0, -1).",
    "citation": "College Board Digital SAT Math Specification — Linear Functions"
  },
  {
    "id": "sat-math-003",
    "type": "mcq",
    "subtopic": "Systems of Linear Equations (Algebra)",
    "difficulty": "Medium",
    "question": "Consider the system of equations:\n2x + 3y = 13\n5x - y = 7\nWhat is the value of x + y?",
    "options": ["5", "3", "7", "9"],
    "answer": 0,
    "explanation": "From the second equation, y = 5x - 7. Substitute into the first equation: 2x + 3(5x - 7) = 13 -> 2x + 15x - 21 = 13 -> 17x = 34 -> x = 2. Then y = 5(2) - 7 = 3. Therefore, x + y = 2 + 3 = 5.",
    "citation": "College Board Digital SAT Math Specification — Systems of Linear Equations"
  },
  {
    "id": "sat-math-004",
    "type": "mcq",
    "subtopic": "Equivalent Expressions & Exponents (Advanced Math)",
    "difficulty": "Medium",
    "question": "For all positive values of x, which of the following is equivalent to (x^(3/4)) * (x^(1/2))?",
    "options": ["x^(5/4)", "x^(3/8)", "x^(7/4)", "x^(2/3)"],
    "answer": 0,
    "explanation": "When multiplying terms with the same base, add their exponents: 3/4 + 1/2 = 3/4 + 2/4 = 5/4. Hence, x^(3/4) * x^(1/2) = x^(5/4).",
    "citation": "College Board Digital SAT Math Specification — Exponents and Radicals"
  },
  {
    "id": "sat-math-005",
    "type": "mcq",
    "subtopic": "Quadratic Equations & Roots (Advanced Math)",
    "difficulty": "Medium",
    "question": "If x^2 - 8x + k = 0 has exactly one distinct real solution, what is the value of k?",
    "options": ["16", "64", "8", "-16"],
    "answer": 0,
    "explanation": "A quadratic ax^2 + bx + c = 0 has exactly one distinct real solution when its discriminant b^2 - 4ac = 0. Here a = 1, b = -8, c = k. Thus (-8)^2 - 4(1)(k) = 0 -> 64 - 4k = 0 -> 4k = 64 -> k = 16.",
    "citation": "College Board Digital SAT Math Specification — Passport to Advanced Math"
  },
  {
    "id": "sat-math-006",
    "type": "mcq",
    "subtopic": "Vertex Form of a Parabola (Advanced Math)",
    "difficulty": "Hard",
    "question": "The function f(x) = 2(x - 3)^2 - 8 is graphed in the xy-plane. Which of the following is true?",
    "options": [
      "The minimum value of f(x) is -8, and it occurs at x = 3",
      "The maximum value of f(x) is -8, and it occurs at x = 3",
      "The minimum value of f(x) is 3, and it occurs at x = -8",
      "The line of symmetry is y = 3"
    ],
    "answer": 0,
    "explanation": "In vertex form f(x) = a(x - h)^2 + k, the vertex is (h, k) = (3, -8). Since a = 2 > 0, the parabola opens upward, meaning the vertex is the absolute minimum point: minimum value is -8 at x = 3.",
    "citation": "College Board Digital SAT Math Specification — Quadratic Functions"
  },
  {
    "id": "sat-math-007",
    "type": "mcq",
    "subtopic": "Percentages & Ratios (Problem Solving)",
    "difficulty": "Easy",
    "question": "The original price of a laptop was $800. The price was discounted by 20%, and then an additional 10% coupon was applied to the discounted price. What was the final purchase price before tax?",
    "options": ["$576", "$560", "$600", "$640"],
    "answer": 0,
    "explanation": "First discount of 20%: $800 * (1 - 0.20) = $800 * 0.80 = $640. Second discount of 10%: $640 * (1 - 0.10) = $640 * 0.90 = $576. Note that sequential percentage discounts are multiplicative, not additive.",
    "citation": "College Board Digital SAT Math Specification — Problem Solving & Data Analysis"
  },
  {
    "id": "sat-math-008",
    "type": "mcq",
    "subtopic": "Unit Conversion & Rates (Problem Solving)",
    "difficulty": "Medium",
    "question": "A high-speed train travels at a constant speed of 180 miles per hour. How many feet does the train travel in 1 second? (1 mile = 5,280 feet)",
    "options": ["264 feet", "300 feet", "180 feet", "528 feet"],
    "answer": 0,
    "explanation": "Speed = 180 miles / 1 hour = (180 * 5,280 feet) / (3,600 seconds) = 950,400 / 3,600 = 264 feet per second.",
    "citation": "College Board Digital SAT Math Specification — Rates and Proportions"
  },
  {
    "id": "sat-math-009",
    "type": "mcq",
    "subtopic": "Scatterplots & Line of Best Fit (Data Analysis)",
    "difficulty": "Medium",
    "question": "A line of best fit for a scatterplot relating weekly study hours (x) to final exam scores (y) is given by the equation y = 2.4x + 58. According to this model, what is the predicted score for a student who studies 15 hours per week?",
    "options": ["94", "88", "90", "92"],
    "answer": 0,
    "explanation": "Substitute x = 15 into the line of best fit: y = 2.4(15) + 58 = 36 + 58 = 94.",
    "citation": "College Board Digital SAT Math Specification — Two-Variable Data"
  },
  {
    "id": "sat-math-010",
    "type": "mcq",
    "subtopic": "Standard Deviation & Spread (Data Analysis)",
    "difficulty": "Hard",
    "question": "Dataset A contains the numbers {10, 10, 10, 10, 10}. Dataset B contains the numbers {8, 9, 10, 11, 12}. Which statement correctly compares their standard deviations?",
    "options": [
      "The standard deviation of Dataset A is 0, which is less than the standard deviation of Dataset B",
      "Both datasets have identical standard deviations because their means are both 10",
      "The standard deviation of Dataset A is greater than Dataset B",
      "Standard deviation cannot be determined without knowing the sample variance"
    ],
    "answer": 0,
    "explanation": "Standard deviation measures the spread of data points from the mean. In Dataset A, all values are equal to the mean (10), so spread is 0. In Dataset B, values vary from 8 to 12, so standard deviation is greater than 0.",
    "citation": "College Board Digital SAT Math Specification — One-Variable Statistics"
  },
  {
    "id": "sat-math-011",
    "type": "mcq",
    "subtopic": "Right Triangle Trigonometry (Geometry)",
    "difficulty": "Easy",
    "question": "In right triangle ABC, angle C is 90 degrees and sin(A) = 3/5. What is the value of cos(B)?",
    "options": ["3/5", "4/5", "5/3", "4/3"],
    "answer": 0,
    "explanation": "In any right triangle where C = 90°, angles A and B are complementary (A + B = 90°). By the cofunction identity, sin(A) = cos(90° - A) = cos(B). Since sin(A) = 3/5, cos(B) = 3/5.",
    "citation": "College Board Digital SAT Math Specification — Trigonometry & Complementary Angles"
  },
  {
    "id": "sat-math-012",
    "type": "mcq",
    "subtopic": "Circle Equation in Standard Form (Geometry)",
    "difficulty": "Hard",
    "question": "In the xy-plane, the graph of x^2 + y^2 - 6x + 8y = 11 is a circle. What is the radius of this circle?",
    "options": ["6", "11", "36", "5"],
    "answer": 0,
    "explanation": "Complete the square: (x^2 - 6x + 9) + (y^2 + 8y + 16) = 11 + 9 + 16 -> (x - 3)^2 + (y + 4)^2 = 36. In standard form (x - h)^2 + (y - k)^2 = r^2, r^2 = 36, so radius r = 6.",
    "citation": "College Board Digital SAT Math Specification — Circles in the Coordinate Plane"
  },
  {
    "id": "sat-math-013",
    "type": "mcq",
    "subtopic": "Exponential Growth Functions (Advanced Math)",
    "difficulty": "Medium",
    "question": "A colony of bacteria begins with an initial population of 500 and doubles every 3 hours. Which function P(t) models the population after t hours?",
    "options": [
      "P(t) = 500 * (2)^(t/3)",
      "P(t) = 500 * (3)^(t/2)",
      "P(t) = 500 + 2t/3",
      "P(t) = 500 * (2)^(3t)"
    ],
    "answer": 0,
    "explanation": "The standard exponential growth model is P(t) = P_0 * (growth factor)^(t / doubling period). Here P_0 = 500, growth factor = 2, and period = 3 hours, giving P(t) = 500 * (2)^(t/3).",
    "citation": "College Board Digital SAT Math Specification — Non-linear Functions"
  },
  {
    "id": "sat-math-014",
    "type": "mcq",
    "subtopic": "Arc Length & Radians (Geometry)",
    "difficulty": "Medium",
    "question": "A circle with radius 12 cm has a central angle measuring (5*pi/6) radians. What is the length of the intercepted arc?",
    "options": ["10*pi cm", "5*pi cm", "12*pi cm", "20*pi cm"],
    "answer": 0,
    "explanation": "Arc length s = r * theta (when theta is in radians). Here r = 12 cm and theta = 5*pi/6. Thus s = 12 * (5*pi / 6) = 2 * 5*pi = 10*pi cm.",
    "citation": "College Board Digital SAT Math Specification — Radians and Arc Length"
  },
  {
    "id": "sat-math-015",
    "type": "mcq",
    "subtopic": "Rational Equations (Advanced Math)",
    "difficulty": "Hard",
    "question": "What is the positive solution to the equation (3 / (x - 1)) + (2 / (x + 1)) = 1?",
    "options": ["4", "3", "2", "5"],
    "answer": 0,
    "explanation": "Multiply both sides by (x - 1)(x + 1) = x^2 - 1: 3(x + 1) + 2(x - 1) = x^2 - 1 -> 3x + 3 + 2x - 2 = x^2 - 1 -> 5x + 1 = x^2 - 1 -> x^2 - 5x - 2 = 0. Wait, check: if x = 4: 3/3 + 2/5 = 1 + 0.4 != 1. Let us solve x^2 - 5x - 2 = 0 or adjust equation: 3/(x-1) + 2/(x+1) = 1. If x=4, 3/3 + 2/5. If equation is 3/(x+1) + 2/(x-1) = 1 -> 3(x-1)+2(x+1)=x^2-1 -> 5x - 1 = x^2 - 1 -> x^2 - 5x = 0 -> x(x - 5) = 0 -> x = 5 (or if 2/(x-1) + 3/(x+1) = 1). For x=4: (6/(x-1)) - (2/(x+1)) = 1? Let's check x=4 in 2/(x-2) + 1/(x-1): Let's make: If (4 / (x + 2)) + (3 / (x - 2)) = 1 -> 4(x - 2) + 3(x + 2) = x^2 - 4 -> 7x - 2 = x^2 - 4 -> x^2 - 7x - 2 = 0. Or simpler: (2 / x) + (3 / 2x) = 7/8 -> (4 + 3)/(2x) = 7/2x = 7/8 -> 2x = 8 -> x = 4.",
    "question": "If (2 / x) + (3 / (2x)) = 7/8, what is the value of x?",
    "options": ["4", "2", "6", "8"],
    "answer": 0,
    "explanation": "Find common denominator on the left: (4 / 2x) + (3 / 2x) = 7 / 2x. Set equal to 7/8: 7 / 2x = 7 / 8. Cross-multiplying: 7(8) = 7(2x) -> 56 = 14x -> x = 4.",
    "citation": "College Board Digital SAT Math Specification — Rational Expressions"
  },
  {
    "id": "sat-math-016",
    "type": "mcq",
    "subtopic": "Linear Inequalities in Two Variables (Algebra)",
    "difficulty": "Medium",
    "question": "Which of the following points (x, y) lies in the solution set of the system of inequalities y > 2x - 4 and y < -x + 3?",
    "options": ["(0, 1)", "(2, 5)", "(4, -2)", "(-1, -7)"],
    "answer": 0,
    "explanation": "Test point (0, 1): For inequality 1: 1 > 2(0) - 4 -> 1 > -4 (True). For inequality 2: 1 < -(0) + 3 -> 1 < 3 (True). Both inequalities are satisfied, so (0, 1) lies in the solution set.",
    "citation": "College Board Digital SAT Math Specification — Systems of Inequalities"
  },
  {
    "id": "sat-math-017",
    "type": "mcq",
    "subtopic": "Volume & Dimensional Geometry (Geometry)",
    "difficulty": "Medium",
    "question": "A right circular cylinder has a radius of 4 inches and a height of 9 inches. What is the volume of the cylinder in terms of pi?",
    "options": ["144*pi cubic inches", "72*pi cubic inches", "36*pi cubic inches", "288*pi cubic inches"],
    "answer": 0,
    "explanation": "Volume of a cylinder V = pi * r^2 * h. Here r = 4 and h = 9: V = pi * (4^2) * 9 = pi * 16 * 9 = 144*pi cubic inches.",
    "citation": "College Board Digital SAT Math Specification — 3D Geometry and Volume"
  },
  {
    "id": "sat-math-018",
    "type": "mcq",
    "subtopic": "Conditional Probability (Data Analysis)",
    "difficulty": "Hard",
    "question": "In a survey of 100 high school students, 60 participate in athletics, 40 participate in music, and 20 participate in both. If a student who participates in athletics is selected at random, what is the probability that this student also participates in music?",
    "options": ["1/3", "1/2", "1/5", "2/3"],
    "answer": 0,
    "explanation": "This is conditional probability P(Music | Athletics) = P(Athletics and Music) / P(Athletics) = 20 / 60 = 1/3.",
    "citation": "College Board Digital SAT Math Specification — Probability & Relative Frequencies"
  },
  {
    "id": "sat-math-019",
    "type": "mcq",
    "subtopic": "Complex Polynomial Factors (Advanced Math)",
    "difficulty": "Hard",
    "question": "If (x - 2) is a factor of the polynomial P(x) = x^3 - 3x^2 + kx - 6, what is the value of k?",
    "options": ["5", "2", "-5", "3"],
    "answer": 0,
    "explanation": "By the Factor Theorem, if (x - 2) is a factor, then P(2) = 0. P(2) = (2)^3 - 3(2)^2 + k(2) - 6 = 8 - 12 + 2k - 6 = -10 + 2k = 0 -> 2k = 10 -> k = 5.",
    "citation": "College Board Digital SAT Math Specification — Remainder and Factor Theorems"
  },
  {
    "id": "sat-math-020",
    "type": "mcq",
    "subtopic": "Nonlinear Systems of Equations (Advanced Math)",
    "difficulty": "Hard",
    "question": "At how many points do the graphs of y = x^2 - 4x + 3 and y = 2x - 6 intersect in the xy-plane?",
    "options": [
      "Exactly 1 point (the line is tangent to the parabola)",
      "Exactly 2 distinct points",
      "0 points (they do not intersect)",
      "Infinitely many points"
    ],
    "answer": 0,
    "explanation": "Set the equations equal: x^2 - 4x + 3 = 2x - 6 -> x^2 - 6x + 9 = 0 -> (x - 3)^2 = 0 -> x = 3. Since there is exactly one real root, the line intersects the parabola at exactly one tangent point: (3, 0).",
    "citation": "College Board Digital SAT Math Specification — Nonlinear Systems"
  }
]

# =============================================================================
# DIGITAL SAT READING & WRITING MODULE 1 & 2 (20 Questions)
# Domains: Craft & Structure, Information & Ideas, Standard English Conventions, Expression of Ideas
# =============================================================================

sat_reading_questions = [
  {
    "id": "sat-rw-001",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Medium",
    "question": "Botanists studying the resurrection fern (*Pleopeltis polypodioides*) noted that during extended droughts, the plant loses up to 95% of its water content and appears dead. However, upon exposure to rain, its metabolic activities are quickly _______, returning the fronds to vibrant green within hours.",
    "options": ["resumed", "terminated", "concealed", "relinquished"],
    "answer": 0,
    "explanation": "'Resumed' means started again after a pause. The context explains that the plant appears dead during drought but springs back to life when rain arrives, so its metabolic activities are restarted or resumed.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-002",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Hard",
    "question": "The architectural critic lauded the new public library for its _______ design; by seamlessly integrating quiet subterranean reading rooms with expansive, sunlit glass atriums, the structure harmonized two seemingly antithetical spatial philosophies.",
    "options": ["judicious", "superfluous", "monotonous", "dogmatic"],
    "answer": 0,
    "explanation": "'Judicious' means showing good judgment, discernment, or wisdom. Harmonizing two opposite spatial philosophies effectively requires thoughtful and prudent design. 'Superfluous' (unnecessary), 'monotonous' (boring), and 'dogmatic' (rigid) contradict the positive praise.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-003",
    "type": "mcq",
    "subtopic": "Text Structure & Purpose (Craft & Structure)",
    "difficulty": "Medium",
    "question": "Microbiologists historically classified deep-sea hydrothermal vents as biological deserts due to the absence of solar radiation. However, the 1977 discovery of diverse vent ecosystems powered by chemosynthetic bacteria overturned this orthodoxy, demonstrating that life can thrive entirely independently of sunlight.\n\nWhich choice best describes the main purpose of the text?",
    "options": [
      "To describe how a scientific discovery challenged and revised a prevailing assumption",
      "To argue that hydrothermal vents contain more biodiversity than terrestrial rainforests",
      "To criticize early microbiologists for failing to conduct deep-sea submersible expeditions",
      "To explain the chemical equations governing bacterial chemosynthesis"
    ],
    "answer": 0,
    "explanation": "The text begins with an old belief (vents as biological deserts) and shows how a discovery (1977 chemosynthetic ecosystems) overturned that view. Thus, the purpose is to describe how a discovery revised an established assumption.",
    "citation": "College Board Digital SAT Reading & Writing — Text Structure and Purpose"
  },
  {
    "id": "sat-rw-004",
    "type": "mcq",
    "subtopic": "Cross-Text Connections (Craft & Structure)",
    "difficulty": "Hard",
    "question": "**Text 1**: Urban economist Dr. Aris Thorne argues that municipal subsidies for sports stadiums are a squandering of civic funds. Independent econometric analyses consistently show that stadium construction produces negligible long-term gains in local employment or retail sales.\n\n**Text 2**: Urban planner Elena Rostova counters that evaluating stadiums solely through direct tax revenues misses their catalytic role. A landmark arena revitalizes derelict downtown waterfronts, attracting private hospitality investment and fostering civic pride that conventional economic models fail to quantify.\n\nBased on the texts, how would Rostova (Text 2) most likely respond to Thorne's reliance on econometric analyses in Text 1?",
    "options": [
      "By asserting that Thorne's metrics are overly narrow because they disregard broader social and qualitative revitalization benefits",
      "By arguing that Thorne manipulated the econometric data to fit a biased anti-sports ideology",
      "By agreeing that sports stadiums generate zero financial impact on hotel or restaurant revenues",
      "By suggesting that private developers should pay 100% of municipal stadium bonds"
    ],
    "answer": 0,
    "explanation": "Rostova argues that looking solely at direct revenues 'misses their catalytic role' and qualitative benefits like downtown revitalization and civic pride. Therefore, she would view Thorne's econometric data as too narrow in scope.",
    "citation": "College Board Digital SAT Reading & Writing — Cross-Text Connections"
  },
  {
    "id": "sat-rw-005",
    "type": "mcq",
    "subtopic": "Central Ideas & Details (Information & Ideas)",
    "difficulty": "Medium",
    "question": "Unlike mammalian teeth, which are fixed in number and cannot regenerate once adult dentition is established, elasmobranchs (sharks and rays) possess polyphyodont dentition. Their teeth develop in multiple conveyor-belt rows inside the jaw cartilage. As functional outer teeth wear down or break while hunting prey, new replacement teeth rotate forward, allowing a single shark to cycle through tens of thousands of teeth in its lifespan.\n\nAccording to the text, what is the primary functional advantage of a shark's polyphyodont dentition?",
    "options": [
      "It ensures continuous replacement of damaged or worn teeth throughout the animal's lifetime",
      "It allows sharks to grind mineral corals into digestible calcium supplements",
      "It prevents jaw cartilage from expanding during deep predatory dives",
      "It enables sharks to survive long periods without capturing food"
    ],
    "answer": 0,
    "explanation": "The text directly states that as teeth wear down or break, replacement teeth rotate forward, giving the shark a continuous supply of fresh, sharp teeth throughout its life.",
    "citation": "College Board Digital SAT Reading & Writing — Central Ideas and Details"
  },
  {
    "id": "sat-rw-006",
    "type": "mcq",
    "subtopic": "Command of Evidence: Textual (Information & Ideas)",
    "difficulty": "Hard",
    "question": "Historians researching the 14th-century West African Mali Empire often emphasize its immense wealth and active integration into trans-Saharan commerce. Which quotation from a primary historical source would best support this historical claim?",
    "options": [
      "Ibn Battuta recorded that Emperor Mansa Musa's pilgrimage caravan carried so much gold bullion through Cairo that the market value of gold in Egypt remained depressed for over twelve years.",
      "Leo Africanus noted that the savannah grasslands of the Sahel experienced recurrent seasonal droughts that reduced sorghum harvests.",
      "A merchant log recorded that camel caravans journeyed for forty days across the sand dunes between salt mines.",
      "An oral griot epic recounted legendary genealogical songs celebrating ancestral hunters of the Niger River basin."
    ],
    "answer": 0,
    "explanation": "The claim is that the Mali Empire possessed immense wealth and active international trade integration. Ibn Battuta's documentation of Mansa Musa's gold disrupting the Egyptian currency market directly provides compelling textual proof.",
    "citation": "College Board Digital SAT Reading & Writing — Command of Evidence (Textual)"
  },
  {
    "id": "sat-rw-007",
    "type": "mcq",
    "subtopic": "Command of Evidence: Quantitative (Information & Ideas)",
    "difficulty": "Medium",
    "question": "Researchers tested five organic polymers for packaging tensile strength. Polymer A withstands 45 MPa of stress; Polymer B withstands 62 MPa; Polymer C withstands 38 MPa; Polymer D withstands 85 MPa; and Polymer E withstands 51 MPa.\n\nWhich statement is most accurately supported by the quantitative data?",
    "options": [
      "Polymer D possesses higher tensile strength than any other polymer tested in the study",
      "Polymer C is capable of enduring more mechanical stress than Polymer B",
      "Polymer A and Polymer E exhibit identical mechanical resistance to tearing",
      "All five polymers withstand tensile stress exceeding 100 MPa"
    ],
    "answer": 0,
    "explanation": "At 85 MPa, Polymer D is higher than 45, 62, 38, and 51, making it unambiguously the highest among all tested materials.",
    "citation": "College Board Digital SAT Reading & Writing — Command of Evidence (Quantitative)"
  },
  {
    "id": "sat-rw-008",
    "type": "mcq",
    "subtopic": "Inferences (Information & Ideas)",
    "difficulty": "Hard",
    "question": "In astronomical spectroscopy, planetary atmospheres that contain methane alongside high levels of ozone or molecular oxygen present a chemical disequilibrium. Because photochemical reactions naturally break down methane rapidly in an oxygenated environment, methane must be constantly replenished by a continuous surface source. If geological processes like volcanism are ruled out by isotopic analysis, researchers infer that _______.\n\nWhich choice most logically completes the text?",
    "options": [
      "Active biological organisms may be actively generating methane on the planet's surface",
      "The planet must have completely lost its gravitational atmosphere billions of years ago",
      "The host star has ceased all thermonuclear fusion of hydrogen into helium",
      "Oxygen cannot support any complex organic chemical reactions in space"
    ],
    "answer": 0,
    "explanation": "If methane is being broken down quickly but continuously replenished, and non-biological geological causes are ruled out, the logical inference is that biological life (methanogenic organisms) is producing the gas.",
    "citation": "College Board Digital SAT Reading & Writing — Inferences"
  },
  {
    "id": "sat-rw-009",
    "type": "mcq",
    "subtopic": "Subject-Verb Agreement (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "The complex array of optical sensors and thermal cameras mounted on the Mars rover _______ designed to operate in sub-zero atmospheric conditions.",
    "options": ["is", "are", "were", "have been"],
    "answer": 0,
    "explanation": "The grammatical subject is 'The complex array' (singular collective noun phrase). The prepositional phrase 'of optical sensors and thermal cameras' does not change the subject number. Therefore, the singular verb 'is' is correct.",
    "citation": "College Board Digital SAT Reading & Writing — Subject-Verb Agreement"
  },
  {
    "id": "sat-rw-010",
    "type": "mcq",
    "subtopic": "Punctuation & Sentence Boundaries (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "During the Renaissance, botanist Leonhart Fuchs illustrated plants with unprecedented scientific _______ his meticulously engraved woodcuts served as foundational anatomical references for generations of European apothecaries.",
    "options": ["accuracy; and", "accuracy;", "accuracy", "accuracy, but"],
    "answer": 1,
    "explanation": "The text consists of two independent clauses: Clause 1 ends at 'accuracy', and Clause 2 begins with 'his meticulously engraved woodcuts'. A semicolon cleanly separates two related independent clauses without creating a comma splice or run-on sentence.",
    "citation": "College Board Digital SAT Reading & Writing — Boundaries and Semicolons"
  },
  {
    "id": "sat-rw-011",
    "type": "mcq",
    "subtopic": "Modifier Placement (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "Peering through the powerful electron microscope, _______.\n\nWhich choice completes the sentence so that it conforms to the conventions of Standard English?",
    "options": [
      "the intricate crystalline lattice of the synthetic diamond was analyzed by the materials scientist",
      "the materials scientist analyzed the intricate crystalline lattice of the synthetic diamond",
      "the synthetic diamond's crystalline lattice became clearly visible to researchers",
      "an intricate crystalline lattice could be observed by the lab team"
    ],
    "answer": 1,
    "explanation": "The introductory participial phrase 'Peering through the powerful electron microscope' must logically modify the subject that immediately follows the comma. A crystalline lattice or diamond cannot peer through a microscope; only 'the materials scientist' can peer through it.",
    "citation": "College Board Digital SAT Reading & Writing — Dangling Modifiers"
  },
  {
    "id": "sat-rw-012",
    "type": "mcq",
    "subtopic": "Pronoun-Antecedent Agreement (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "Each of the migratory songbirds returning to the boreal forest in spring establishes _______ own nesting territory along the riverbank.",
    "options": ["its", "their", "they're", "it's"],
    "answer": 0,
    "explanation": "'Each' is a singular indefinite pronoun requiring a singular possessive pronoun. Since songbirds are animals of non-specified gender, the singular possessive pronoun 'its' is grammatically correct ('it's' is a contraction for 'it is').",
    "citation": "College Board Digital SAT Reading & Writing — Pronoun Agreement"
  },
  {
    "id": "sat-rw-013",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Easy",
    "question": "Solar panels generate peak electrical output during the sunniest afternoon hours. _______, peak consumer residential demand for electricity typically surges between 6:00 PM and 9:00 PM when people return home from work.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["However", "Furthermore", "Consequently", "In other words"],
    "answer": 0,
    "explanation": "The first sentence notes when generation peaks (afternoon), while the second notes when demand peaks (evening). This is a contrast between supply timing and demand timing, requiring the adversative transition 'However'.",
    "citation": "College Board Digital SAT Reading & Writing — Logical Transitions"
  },
  {
    "id": "sat-rw-014",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "Graphene consists of a single layer of carbon atoms arranged in a hexagonal honeycomb lattice. This ultrathin atomic arrangement gives the material exceptional electrical conductivity and mechanical tensile strength. _______, researchers are testing graphene coatings to build lighter, longer-lasting aircraft wings.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["Accordingly", "Nevertheless", "In contrast", "Conversely"],
    "answer": 0,
    "explanation": "The aircraft wing applications are a direct consequence and practical application of graphene's exceptional strength and conductivity. 'Accordingly' (meaning 'as a result' or 'therefore') expresses this cause-and-effect link.",
    "citation": "College Board Digital SAT Reading & Writing — Logical Transitions"
  },
  {
    "id": "sat-rw-015",
    "type": "mcq",
    "subtopic": "Rhetorical Synthesis (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "While researching an essay on civil rights icon Bayard Rustin, a student took the following notes:\n- Bayard Rustin was an African American leader in social movements for civil rights, socialism, and nonviolence.\n- He was the chief organizer of the historic 1963 March on Washington for Jobs and Freedom.\n- He mentored Dr. Martin Luther King Jr. in the philosophy of nonviolent civil disobedience.\n- Because he was an openly gay man in the mid-20th century, Rustin was often relegated to background roles by political contemporaries.\n\nThe student wants to emphasize Rustin's pivotal influence on the civil rights movement despite facing discrimination. Which choice most effectively uses the relevant information?",
    "options": [
      "Although political contemporaries often marginalized Bayard Rustin due to his sexual orientation, he profoundly shaped the civil rights movement by mentoring Martin Luther King Jr. and organizing the 1963 March on Washington.",
      "Bayard Rustin was an advocate for socialism, civil rights, and nonviolence who organized the March on Washington in 1963.",
      "Martin Luther King Jr. learned the philosophical principles of nonviolence from Bayard Rustin during the civil rights era.",
      "Rustin was an openly gay African American leader in the mid-20th century who worked alongside prominent activists."
    ],
    "answer": 0,
    "explanation": "Choice A directly achieves both goals: it highlights his pivotal influence (mentoring MLK, organizing the March on Washington) and acknowledges the discrimination he faced (marginalized due to sexual orientation).",
    "citation": "College Board Digital SAT Reading & Writing — Rhetorical Synthesis"
  },
  {
    "id": "sat-rw-016",
    "type": "mcq",
    "subtopic": "Parallel Structure (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "The city council's urban sustainability initiative focuses on expanding bike corridors, _______ municipal buildings, and installing public electric vehicle chargers.",
    "options": ["weatherizing", "to weatherize", "it weatherizes", "weatherization of"],
    "answer": 0,
    "explanation": "Items in a list must maintain parallel grammatical form. Here we have gerund phrases: 'expanding bike corridors', 'weatherizing municipal buildings', and 'installing public electric vehicle chargers'.",
    "citation": "College Board Digital SAT Reading & Writing — Parallelism"
  },
  {
    "id": "sat-rw-017",
    "type": "mcq",
    "subtopic": "Nonessential Clauses & Commas (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "Dr. Chien-Shiung Wu _______ a pioneering nuclear physicist who disproved the theoretical Law of Conservation of Parity, earned the nickname 'the First Lady of Physics'.",
    "options": [
      ", a pioneering nuclear physicist who disproved the theoretical Law of Conservation of Parity,",
      "a pioneering nuclear physicist who disproved the theoretical Law of Conservation of Parity",
      ", a pioneering nuclear physicist who disproved the theoretical Law of Conservation of Parity",
      "a pioneering nuclear physicist who disproved the theoretical Law of Conservation of Parity,"
    ],
    "answer": 0,
    "explanation": "The phrase 'a pioneering nuclear physicist who disproved the theoretical Law of Conservation of Parity' is a nonessential appositive providing extra detail about Dr. Chien-Shiung Wu. Nonessential appositives must be enclosed by paired commas.",
    "citation": "College Board Digital SAT Reading & Writing — Appositives and Commas"
  },
  {
    "id": "sat-rw-018",
    "type": "mcq",
    "subtopic": "Verb Tense Consistency (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "By the time the James Webb Space Telescope reached its orbital destination at Lagrange point 2 in early 2022, engineers _______ over two decades designing and testing its folding gold-coated mirrors.",
    "options": ["had spent", "have spent", "will spend", "spend"],
    "answer": 0,
    "explanation": "The past perfect tense ('had spent') is required because the action of designing and testing occurred and was completed prior to another past milestone ('reached its destination in 2022').",
    "citation": "College Board Digital SAT Reading & Writing — Verb Tense and Aspect"
  },
  {
    "id": "sat-rw-019",
    "type": "mcq",
    "subtopic": "Rhetorical Synthesis (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "While researching bioluminescence, a student noted:\n- Bioluminescence is the biochemical production of light by living organisms.\n- Firefly luciferase catalyzes the oxidation of luciferin in the presence of ATP and oxygen, releasing photons.\n- Deep-sea anglerfish use bioluminescent bacteria inside an esca (lure) to attract prey in the bathypelagic zone.\n\nThe student wants to provide a specific example of how bioluminescence is utilized for predation. Which choice most effectively accomplishes this goal?",
    "options": [
      "The deep-sea anglerfish utilizes bioluminescent bacteria housed within its esca lure to entice unsuspecting prey in the pitch-black ocean depths.",
      "Bioluminescence is caused by the chemical interaction of luciferin, luciferase, ATP, and oxygen.",
      "Living organisms generate biological light through a biochemical reaction producing photons.",
      "Both terrestrial fireflies and deep-sea marine animals exhibit luminous biological traits."
    ],
    "answer": 0,
    "explanation": "Choice A provides the precise example requested: how the anglerfish uses its glowing esca lure to catch prey in the deep sea.",
    "citation": "College Board Digital SAT Reading & Writing — Rhetorical Synthesis"
  },
  {
    "id": "sat-rw-020",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Hard",
    "question": "Early film archivists stored motion picture master reels on cellulose nitrate stock, unaware that the chemical compound naturally degrades into an auto-combustible acidic powder. _______, modern audiovisual preservationists must transfer surviving silent films onto non-flammable polyester safety film inside sub-zero climate vaults.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["As a consequence", "Similarly", "Conversely", "Meanwhile"],
    "answer": 0,
    "explanation": "The hazard of nitrate decomposition directly causes the modern requirement to transfer films onto polyester film in climate-controlled vaults. 'As a consequence' correctly articulates this cause-and-effect relationship.",
    "citation": "College Board Digital SAT Reading & Writing — Logical Transitions"
  }
]

# Write out JSON files
with open(os.path.join(US_DATA_DIR, "digital_sat_math_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_math_questions}, f, indent=2, ensure_ascii=False)

with open(os.path.join(US_DATA_DIR, "digital_sat_reading_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_reading_questions}, f, indent=2, ensure_ascii=False)

print("Generated Digital SAT Math (20 Qs) and Reading & Writing (20 Qs) successfully!")
