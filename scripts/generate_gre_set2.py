import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRE_DIR = os.path.join(BASE_DIR, "data", "global", "gre")
os.makedirs(GRE_DIR, exist_ok=True)

standard_qc_options = [
    "Quantity A is greater.",
    "Quantity B is greater.",
    "The two quantities are equal.",
    "The relationship cannot be determined from the information given."
]

gre_quant_set2_questions = [
    # QC 1: Arithmetic & Exponents
    {
        "id": "gre-quant-021",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Exponents & Bases",
        "difficulty": "Medium",
        "question": "Quantity A: 2^60\nQuantity B: 3^40\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 1,
        "explanation": "Express both quantities using the common exponent GCD(60, 40) = 20:\nQuantity A = 2^60 = (2^3)^20 = 8^20.\nQuantity B = 3^40 = (3^2)^20 = 9^20.\nSince 9 > 8 and 20 > 0, 9^20 > 8^20. Therefore, Quantity B is greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Exponent Comparison"
    },
    # QC 2: Geometry & Triangles
    {
        "id": "gre-quant-022",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Triangle Inequality",
        "difficulty": "Medium",
        "question": "A triangle has side lengths 7, 11, and x, where x is an integer.\n\nQuantity A: The number of possible values of x\nQuantity B: 13\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 2,
        "explanation": "By the Triangle Inequality Theorem, for sides a, b, c: |a - b| < c < a + b.\nHere: |11 - 7| < x < 11 + 7 => 4 < x < 18.\nSince x is an integer, x can take values: 5, 6, 7, ..., 17.\nNumber of integer values = 17 - 5 + 1 = 13.\nQuantity A = 13 and Quantity B = 13. The two quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Triangle Inequality"
    },
    # QC 3: Algebra & Factorials
    {
        "id": "gre-quant-023",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Factorials",
        "difficulty": "Easy",
        "question": "Quantity A: (15! / 13!) - (14! / 13!)\nQuantity B: 14^2\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 2,
        "explanation": "Simplify Quantity A:\n15! / 13! = 15 * 14 = 210.\n14! / 13! = 14.\nQuantity A = 210 - 14 = 196.\nQuantity B = 14^2 = 196.\nBoth quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Factorials"
    },
    # QC 4: Coordinate Geometry
    {
        "id": "gre-quant-024",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Midpoint & Distance",
        "difficulty": "Medium",
        "question": "Points P(-4, 6) and Q(6, -2) lie on the xy-plane.\n\nQuantity A: Distance from the midpoint of PQ to the origin (0, 0)\nQuantity B: √5\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 2,
        "explanation": "Midpoint M = ((-4 + 6)/2, (6 + (-2))/2) = (2/2, 4/2) = (1, 2).\nDistance from origin to M = √(1^2 + 2^2) = √(1 + 4) = √5.\nQuantity A = √5 and Quantity B = √5. The two quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Coordinate Geometry"
    },
    # QC 5: Rates & Work
    {
        "id": "gre-quant-025",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Work Rates",
        "difficulty": "Medium",
        "question": "Pump X fills a reservoir in 6 hours. Pump Y fills the same reservoir in 4 hours.\n\nQuantity A: The time taken to fill the reservoir with both pumps working together\nQuantity B: 2.5 hours\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 1,
        "explanation": "Combined rate = 1/6 + 1/4 = (2 + 3)/12 = 5/12 of the reservoir per hour.\nTime taken = 12 / 5 = 2.4 hours.\nQuantity A = 2.4 hours.\nQuantity B = 2.5 hours.\nSince 2.5 > 2.4, Quantity B is greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Rates"
    },
    # QC 6: Statistics: Mean vs Median
    {
        "id": "gre-quant-026",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Skewed Distributions",
        "difficulty": "Medium",
        "question": "A list of 7 distinct positive integers has median 20 and a single extreme outlier equal to 1,000.\n\nQuantity A: The mean of the 7 integers\nQuantity B: The median of the 7 integers\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 0,
        "explanation": "The sum of the 7 integers is at least: 1 + 2 + 3 + 20 + 21 + 22 + 1000 = 1,069.\nMean ≥ 1,069 / 7 ≈ 152.7.\nQuantity A (Mean) > 150.\nQuantity B (Median) = 20.\nTherefore, Quantity A is strictly greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Statistics Mean vs Median"
    },
    # QC 7: Circles & Secants
    {
        "id": "gre-quant-027",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Circle Chords",
        "difficulty": "Easy",
        "question": "A circle has diameter d = 20 cm. Chord AB has length 16 cm.\n\nQuantity A: The distance from the center of the circle to chord AB\nQuantity B: 6 cm\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 2,
        "explanation": "Radius r = d / 2 = 10 cm.\nThe perpendicular from the center bisects the chord into two 8 cm segments.\nBy the Pythagorean theorem: distance^2 + 8^2 = 10^2 => distance^2 = 100 - 64 = 36 => distance = 6 cm.\nQuantity A = 6 cm and Quantity B = 6 cm. Both quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Circle Chords"
    },
    # QC 8: Inequalities & Unknowns
    {
        "id": "gre-quant-028",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Non-linear Inequalities",
        "difficulty": "Hard",
        "question": "Given: a * b < 0 and a + b > 0\n\nQuantity A: |a|\nQuantity B: |b|\n\nCompare Quantity A and Quantity B.",
        "options": list(standard_qc_options),
        "answer": 3,
        "explanation": "a * b < 0 implies one variable is positive and the other is negative.\na + b > 0 implies the positive variable has a strictly greater absolute value than the negative variable.\nHowever, we are not told which variable (a or b) is the positive one!\nIf a = 5 and b = -2: a + b = 3 > 0, |a| = 5, |b| = 2 => Quantity A > Quantity B.\nIf a = -2 and b = 5: a + b = 3 > 0, |a| = 2, |b| = 5 => Quantity B > Quantity A.\nTherefore, the relationship cannot be determined.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Inequalities & Absolute Values"
    },
    # Q9–Q16: Problem Solving Multiple Choice (5 options)
    {
        "id": "gre-quant-029",
        "type": "mcq",
        "subtopic": "Combinatorics: Circular Permutations",
        "difficulty": "Medium",
        "question": "In how many distinct ways can 6 dignitaries be seated around a circular conference table?",
        "options": ["120", "720", "24", "60", "360"],
        "answer": 0,
        "explanation": "Circular permutation formula for n distinct objects is (n - 1)!.\nHere n = 6 => (6 - 1)! = 5! = 5 * 4 * 3 * 2 * 1 = 120 distinct seating arrangements.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Permutations"
    },
    {
        "id": "gre-quant-030",
        "type": "mcq",
        "subtopic": "Probability: Independent Events",
        "difficulty": "Medium",
        "question": "A basket contains 5 green apples and 7 red apples. Two apples are drawn at random without replacement. What is the probability that both apples drawn are green?",
        "options": ["5/33", "25/144", "5/12", "1/6", "7/33"],
        "answer": 0,
        "explanation": "Total apples = 5 + 7 = 12.\nP(1st green) = 5/12.\nP(2nd green | 1st green) = 4/11.\nP(both green) = (5/12) * (4/11) = 20 / 132 = 5 / 33.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Probability Without Replacement"
    },
    {
        "id": "gre-quant-031",
        "type": "mcq",
        "subtopic": "Percentages: Net Profit Margin",
        "difficulty": "Medium",
        "question": "A merchant purchases goods for $600. He marks them up by 50% above cost and subsequently offers a discount of 20% on the marked price. What is the merchant's net profit in dollars?",
        "options": ["$120", "$150", "$100", "$180", "$90"],
        "answer": 0,
        "explanation": "Cost Price (CP) = $600.\nMarked Price (MP) = 600 * 1.50 = $900.\nSelling Price (SP) = 900 * (1 - 0.20) = 900 * 0.80 = $720.\nNet Profit = SP - CP = $720 - $600 = $120.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Profit and Loss"
    },
    {
        "id": "gre-quant-032",
        "type": "mcq",
        "subtopic": "Geometry: 3D Rectangular Prism",
        "difficulty": "Hard",
        "question": "A rectangular storage room has dimensions 12 feet by 9 feet by 8 feet. What is the length of the longest rigid steel pole that can fit entirely inside the room?",
        "options": ["17 feet", "15 feet", "20 feet", "18 feet", "19 feet"],
        "answer": 0,
        "explanation": "The longest segment is the space diagonal d = √(l^2 + w^2 + h^2).\nd = √(12^2 + 9^2 + 8^2) = √(144 + 81 + 64) = √289 = 17 feet.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — 3D Geometry Space Diagonal"
    },
    {
        "id": "gre-quant-033",
        "type": "mcq",
        "subtopic": "Number Theory: Prime Factorization",
        "difficulty": "Medium",
        "question": "What is the total number of distinct positive divisors (factors) of the integer 360?",
        "options": ["24", "18", "16", "30", "12"],
        "answer": 0,
        "explanation": "Prime factorize 360: 360 = 36 * 10 = (2^2 * 3^2) * (2 * 5) = 2^3 * 3^2 * 5^1.\nFormula for number of divisors = (e1 + 1)(e2 + 1)(e3 + 1) = (3 + 1)(2 + 1)(1 + 1) = 4 * 3 * 2 = 24 positive divisors.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Divisors Count"
    },
    {
        "id": "gre-quant-034",
        "type": "mcq",
        "subtopic": "Sequences: Geometric Progression",
        "difficulty": "Medium",
        "question": "In a geometric sequence of positive terms, the 2nd term is 12 and the 5th term is 96. What is the first term of the sequence?",
        "options": ["6", "3", "4", "8", "2"],
        "answer": 0,
        "explanation": "General term: a_n = a_1 * r^(n - 1).\na_2 = a_1 * r = 12.\na_5 = a_1 * r^4 = 96.\nDivide a_5 by a_2: r^3 = 96 / 12 = 8 => r = 2.\nSince a_1 * 2 = 12 => a_1 = 6.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Geometric Sequences"
    },
    {
        "id": "gre-quant-035",
        "type": "mcq",
        "subtopic": "Functions & Transformations",
        "difficulty": "Hard",
        "question": "If g(x) = (2x - 3) / (x + 4) for all real x ≠ -4, what is the value of x for which g(x) = 5?",
        "options": ["-23/3", "-17/3", "-7", "17/3", "23/3"],
        "answer": 0,
        "explanation": "Set equation: (2x - 3) / (x + 4) = 5.\nCross-multiply: 2x - 3 = 5(x + 4) = 5x + 20.\nRearrange: 2x - 5x = 20 + 3 => -3x = 23 => x = -23/3.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Rational Functions"
    },
    {
        "id": "gre-quant-036",
        "type": "mcq",
        "subtopic": "Speed & Average Speed",
        "difficulty": "Medium",
        "question": "A motorist drives 60 miles from City A to City B at an average speed of 30 mph, and returns along the same route from City B to City A at 60 mph. What was the average speed for the entire round trip?",
        "options": ["40 mph", "45 mph", "42 mph", "48 mph", "50 mph"],
        "answer": 0,
        "explanation": "Average speed = Total Distance / Total Time.\nTotal Distance = 60 + 60 = 120 miles.\nTime going = 60 / 30 = 2 hours.\nTime returning = 60 / 60 = 1 hour.\nTotal Time = 2 + 1 = 3 hours.\nAverage speed = 120 / 3 = 40 mph.\n(Harmonic mean formula: 2 * v1 * v2 / (v1 + v2) = 2 * 30 * 60 / 90 = 40 mph).",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Harmonic Average Speed"
    },
    # Q17–Q20: Data Interpretation Set
    {
        "id": "gre-quant-037",
        "type": "mcq",
        "subtopic": "Data Interpretation: Clean Energy Output",
        "difficulty": "Easy",
        "question": "Data: In 2024, a municipal utility produced 500 gigawatt-hours (GWh) of clean power:\n- Wind: 40%\n- Solar: 35%\n- Hydroelectric: 15%\n- Biomass: 10%\n\nHow many GWh were generated by Wind and Solar combined?",
        "options": ["375 GWh", "350 GWh", "400 GWh", "325 GWh", "300 GWh"],
        "answer": 0,
        "explanation": "Combined percentage for Wind + Solar = 40% + 35% = 75%.\nTotal GWh = 75% of 500 GWh = 0.75 * 500 = 375 GWh.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Data Interpretation"
    },
    {
        "id": "gre-quant-038",
        "type": "mcq",
        "subtopic": "Data Interpretation: Clean Energy Output",
        "difficulty": "Medium",
        "question": "Using the 2024 energy data in Q37, if Hydroelectric power generation was sold at $60 per megawatt-hour (MWh), what was the total revenue generated from Hydroelectric power? (Note: 1 GWh = 1,000 MWh)",
        "options": ["$4.5 million", "$3.0 million", "$6.0 million", "$7.5 million", "$9.0 million"],
        "answer": 0,
        "explanation": "Hydroelectric generation = 15% of 500 GWh = 75 GWh.\nConvert to MWh: 75 GWh * 1,000 MWh/GWh = 75,000 MWh.\nTotal Revenue = 75,000 MWh * $60/MWh = $4,500,000 = $4.5 million.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Unit Conversions in Data Interpretation"
    },
    {
        "id": "gre-quant-039",
        "type": "mcq",
        "subtopic": "Data Interpretation: Clean Energy Output",
        "difficulty": "Medium",
        "question": "Using the data in Q37, in 2025 Solar output increases by 20% while Wind output decreases by 10%. What is the ratio of Solar generation to Wind generation in 2025?",
        "options": ["7 : 6", "6 : 7", "1 : 1", "4 : 3", "5 : 4"],
        "answer": 0,
        "explanation": "Initial 2024 generation:\nSolar = 35% of 500 = 175 GWh.\nWind = 40% of 500 = 200 GWh.\n2025 generation:\nSolar = 175 * 1.20 = 210 GWh.\nWind = 200 * 0.90 = 180 GWh.\nRatio = 210 / 180 = 21 / 18 = 7 : 6.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Proportional Changes"
    },
    {
        "id": "gre-quant-040",
        "type": "mcq",
        "subtopic": "Data Interpretation: Clean Energy Output",
        "difficulty": "Hard",
        "question": "Using the data in Q37, what is the degree measure of the central angle representing Biomass in a circular pie chart of 2024 generation?",
        "options": ["36°", "40°", "30°", "45°", "25°"],
        "answer": 0,
        "explanation": "Biomass accounts for 10% of the total generation.\nA complete circle is 360°.\nCentral angle = 10% of 360° = 0.10 * 360° = 36°.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Circular Sector Graphs"
    }
]

with open(os.path.join(GRE_DIR, "gre_quant_set2.json"), "w") as f:
    json.dump({"test_id": "gre_quant_set2", "title": "GRE® Quantitative Reasoning Diagnostic Drill 02", "total_questions": 20, "duration_minutes": 35, "questions": gre_quant_set2_questions}, f, indent=2)

print("gre_quant_set2.json created successfully!")
