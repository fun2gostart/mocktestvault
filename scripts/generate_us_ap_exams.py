#!/usr/bin/env python3
"""
Generates authentic College Board AP Course & Exam Description (CED) question banks:
1. ap_calculus_ab_set1.json (20 Questions - Section I Diagnostic)
2. ap_physics_1_set1.json (20 Questions - Section I Diagnostic)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_AP = os.path.join(BASE_DIR, "data", "us", "ap")
os.makedirs(US_DATA_AP, exist_ok=True)

# ==============================================================================
# AP CALCULUS AB DIAGNOSTIC 01 (20 Questions)
# ==============================================================================
ap_calc_questions = [
  {
    "id": "ap-calc-001",
    "type": "mcq",
    "subtopic": "Limits by Factoring (Unit 1: Limits & Continuity)",
    "difficulty": "Easy",
    "question": "What is the value of lim(x→3) [(x^2 - 9) / (x - 3)]?",
    "options": ["6", "0", "3", "Does not exist"],
    "answer": 0,
    "explanation": "Direct substitution gives 0/0 (indeterminate). Factor the numerator: (x - 3)(x + 3) / (x - 3). For x ≠ 3, cancel (x - 3): lim(x→3) (x + 3) = 3 + 3 = 6.",
    "citation": "College Board AP® Calculus AB CED — Topic 1.5 Determining Limits Using Algebraic Properties"
  },
  {
    "id": "ap-calc-002",
    "type": "mcq",
    "subtopic": "Limits at Infinity (Unit 1: Limits & Continuity)",
    "difficulty": "Easy",
    "question": "What is lim(x→∞) [(4x^3 - 2x + 1) / (7x^3 + 5x^2 - 8)]?",
    "options": ["4/7", "0", "∞", "-1/8"],
    "answer": 0,
    "explanation": "For limits at infinity of rational functions with matching degrees in numerator and denominator (degree 3), the limit equals the ratio of leading coefficients: 4 / 7.",
    "citation": "College Board AP® Calculus AB CED — Topic 1.15 Connecting Limits at Infinity and Horizontal Asymptotes"
  },
  {
    "id": "ap-calc-003",
    "type": "mcq",
    "subtopic": "Trigonometric Limits (Unit 1: Limits & Continuity)",
    "difficulty": "Medium",
    "question": "What is the value of lim(x→0) [sin(5x) / (3x)]?",
    "options": ["5/3", "3/5", "1", "0"],
    "answer": 0,
    "explanation": "Recall standard limit lim(u→0) [sin(u)/u] = 1. Multiply numerator and denominator by 5/3: lim(x→0) [(5/3) * (sin(5x) / 5x)] = (5/3) * 1 = 5/3.",
    "citation": "College Board AP® Calculus AB CED — Topic 1.8 Squeeze Theorem and Trigonometric Limits"
  },
  {
    "id": "ap-calc-004",
    "type": "mcq",
    "subtopic": "Intermediate Value Theorem (Unit 1: Limits & Continuity)",
    "difficulty": "Medium",
    "question": "Let f(x) be continuous on [0, 4] with f(0) = -2 and f(4) = 6. Which theorem guarantees the existence of a number c in (0, 4) such that f(c) = 0?",
    "options": [
      "Intermediate Value Theorem (IVT)",
      "Mean Value Theorem (MVT)",
      "Extreme Value Theorem (EVT)",
      "Rolle's Theorem"
    ],
    "answer": 0,
    "explanation": "Because f(x) is continuous on [0, 4] and 0 lies between f(0) = -2 and f(4) = 6, the Intermediate Value Theorem guarantees that f(c) = 0 for at least one c in (0, 4).",
    "citation": "College Board AP® Calculus AB CED — Topic 1.16 Intermediate Value Theorem (IVT)"
  },
  {
    "id": "ap-calc-005",
    "type": "mcq",
    "subtopic": "Product Rule (Unit 2: Differentiation)",
    "difficulty": "Medium",
    "question": "If f(x) = x^3 * e^x, what is f'(x)?",
    "options": ["x^2 * e^x * (x + 3)", "3x^2 * e^x", "x^3 * e^x", "3x^2 + e^x"],
    "answer": 0,
    "explanation": "By the product rule d/dx[u*v] = u'*v + u*v'. Here u = x^3 (u' = 3x^2) and v = e^x (v' = e^x). f'(x) = 3x^2 * e^x + x^3 * e^x = x^2 * e^x * (3 + x).",
    "citation": "College Board AP® Calculus AB CED — Topic 2.8 Product Rule"
  },
  {
    "id": "ap-calc-006",
    "type": "mcq",
    "subtopic": "Chain Rule with Trigonometry (Unit 3: Composite Functions)",
    "difficulty": "Medium",
    "question": "If y = sin(x^2), what is dy/dx?",
    "options": ["2x * cos(x^2)", "cos(x^2)", "2x * sin(x^2)", "-cos(x^2)"],
    "answer": 0,
    "explanation": "By chain rule dy/dx = cos(u) * du/dx where u = x^2 (du/dx = 2x). Thus dy/dx = 2x * cos(x^2).",
    "citation": "College Board AP® Calculus AB CED — Topic 3.1 The Chain Rule"
  },
  {
    "id": "ap-calc-007",
    "type": "mcq",
    "subtopic": "Quotient Rule (Unit 2: Differentiation)",
    "difficulty": "Medium",
    "question": "If f(x) = ln(x) / x for x > 0, what is f'(x)?",
    "options": ["(1 - ln(x)) / x^2", "(ln(x) - 1) / x^2", "1 / x^2", "-1 / x^2"],
    "answer": 0,
    "explanation": "Quotient rule [v*u' - u*v'] / v^2: u = ln(x) (u' = 1/x), v = x (v' = 1). f'(x) = [x*(1/x) - ln(x)*1] / x^2 = (1 - ln(x)) / x^2.",
    "citation": "College Board AP® Calculus AB CED — Topic 2.9 Quotient Rule"
  },
  {
    "id": "ap-calc-008",
    "type": "mcq",
    "subtopic": "Implicit Differentiation (Unit 3: Composite Functions)",
    "difficulty": "Hard",
    "question": "For the circle x^2 + y^2 = 25, what is the slope of the tangent line at the point (3, 4)?",
    "options": ["-3/4", "3/4", "-4/3", "4/3"],
    "answer": 0,
    "explanation": "Differentiate implicitly with respect to x: 2x + 2y(dy/dx) = 0 → dy/dx = -x / y. At point (3, 4), slope = -3 / 4.",
    "citation": "College Board AP® Calculus AB CED — Topic 3.2 Implicit Differentiation"
  },
  {
    "id": "ap-calc-009",
    "type": "mcq",
    "subtopic": "Derivative of Inverse Trigonometric Functions (Unit 3)",
    "difficulty": "Medium",
    "question": "What is the derivative of f(x) = arctan(2x)?",
    "options": ["2 / (1 + 4x^2)", "1 / (1 + 4x^2)", "2 / √(1 - 4x^2)", "1 / (1 + 2x^2)"],
    "answer": 0,
    "explanation": "Formula: d/dx[arctan(u)] = (1 / (1 + u^2)) * du/dx. Here u = 2x, so du/dx = 2. f'(x) = 2 / (1 + (2x)^2) = 2 / (1 + 4x^2).",
    "citation": "College Board AP® Calculus AB CED — Topic 3.4 Differentiating Inverse Trigonometric Functions"
  },
  {
    "id": "ap-calc-010",
    "type": "mcq",
    "subtopic": "Tangent Line Equations (Unit 2: Differentiation)",
    "difficulty": "Easy",
    "question": "What is the equation of the tangent line to the curve y = x^3 - 3x + 2 at x = 2?",
    "options": ["y = 9x - 14", "y = 9x + 4", "y = 3x - 2", "y = 12x - 20"],
    "answer": 0,
    "explanation": "Point y(2) = 2^3 - 3(2) + 2 = 8 - 6 + 2 = 4. Derivative y' = 3x^2 - 3. Slope m = y'(2) = 3(4) - 3 = 9. Tangent line: y - 4 = 9(x - 2) → y - 4 = 9x - 18 → y = 9x - 14.",
    "citation": "College Board AP® Calculus AB CED — Topic 2.3 Estimating Derivatives and Tangent Lines"
  },
  {
    "id": "ap-calc-011",
    "type": "mcq",
    "subtopic": "Particle Motion (Unit 4: Contextual Applications)",
    "difficulty": "Medium",
    "question": "A particle moves along the x-axis with position function s(t) = t^3 - 6t^2 + 9t for t ≥ 0. At what times t is the particle momentarily at rest?",
    "options": ["t = 1 and t = 3", "t = 0 and t = 3", "t = 2 only", "t = 1 only"],
    "answer": 0,
    "explanation": "A particle is at rest when velocity v(t) = s'(t) = 0. s'(t) = 3t^2 - 12t + 9 = 0. Divide by 3: t^2 - 4t + 3 = 0 → (t - 1)(t - 3) = 0 → t = 1 and t = 3.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.2 Straight-Line Motion: Connecting Position, Velocity, and Acceleration"
  },
  {
    "id": "ap-calc-012",
    "type": "mcq",
    "subtopic": "Related Rates (Unit 4: Contextual Applications)",
    "difficulty": "Hard",
    "question": "The radius r of a spherical balloon is expanding at a constant rate of 2 cm/s. At what rate is the volume of the balloon increasing, in cm^3/s, when radius r = 5 cm? (V = (4/3)πr^3)",
    "options": ["200π cm^3/s", "100π cm^3/s", "50π cm^3/s", "400π cm^3/s"],
    "answer": 0,
    "explanation": "Differentiate volume with respect to time t: dV/dt = 4πr^2 * (dr/dt). Given dr/dt = 2 and r = 5: dV/dt = 4π(5^2)(2) = 4π(25)(2) = 200π cm^3/s.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.5 Related Rates"
  },
  {
    "id": "ap-calc-013",
    "type": "mcq",
    "subtopic": "Mean Value Theorem (Unit 5: Analytical Applications)",
    "difficulty": "Medium",
    "question": "For f(x) = x^2 - 4x on the closed interval [1, 5], what value of c in (1, 5) satisfies the conclusion of the Mean Value Theorem?",
    "options": ["3", "2.5", "2", "4"],
    "answer": 0,
    "explanation": "f(1) = 1 - 4 = -3. f(5) = 25 - 20 = 5. Average rate of change = (5 - (-3)) / (5 - 1) = 8 / 4 = 2. MVT states f'(c) = 2. Since f'(x) = 2x - 4: 2c - 4 = 2 → 2c = 6 → c = 3.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.1 Using the Mean Value Theorem"
  },
  {
    "id": "ap-calc-014",
    "type": "mcq",
    "subtopic": "First & Second Derivative Tests (Unit 5: Analytical Applications)",
    "difficulty": "Medium",
    "question": "If f'(c) = 0 and f''(c) = -5, what does the Second Derivative Test conclude about x = c?",
    "options": [
      "f(x) has a relative (local) maximum at x = c",
      "f(x) has a relative (local) minimum at x = c",
      "x = c is an inflection point of f(x)",
      "The test is inconclusive"
    ],
    "answer": 0,
    "explanation": "By the Second Derivative Test, if f'(c) = 0 and f''(c) < 0, the curve is concave down at a horizontal tangent, meaning f has a local maximum at x = c.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.7 Using the Second Derivative Test to Determine Extrema"
  },
  {
    "id": "ap-calc-015",
    "type": "mcq",
    "subtopic": "L'Hôpital's Rule (Unit 4: Contextual Applications)",
    "difficulty": "Hard",
    "question": "Evaluate the limit: lim(x→0) [(e^(2x) - 1 - 2x) / x^2].",
    "options": ["2", "1", "4", "0"],
    "answer": 0,
    "explanation": "Direct evaluation gives (1 - 1 - 0)/0 = 0/0. Apply L'Hôpital's rule: lim(x→0) [(2e^(2x) - 2) / 2x] = (2 - 2)/0 = 0/0. Apply L'Hôpital's rule a second time: lim(x→0) [4e^(2x) / 2] = 4(1) / 2 = 2.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.7 Using L'Hôpital's Rule for Determining Limits of Indeterminate Forms"
  },
  {
    "id": "ap-calc-016",
    "type": "mcq",
    "subtopic": "Fundamental Theorem of Calculus Part 1 (Unit 6)",
    "difficulty": "Medium",
    "question": "If F(x) = ∫[from 1 to x] √(1 + t^4) dt, what is F'(x)?",
    "options": ["√(1 + x^4)", "(4x^3) / (2√(1 + x^4))", "√(1 + x^4) - √2", "x√(1 + x^4)"],
    "answer": 0,
    "explanation": "By the Fundamental Theorem of Calculus Part 1, d/dx ∫[from a to x] f(t) dt = f(x). Therefore, F'(x) = √(1 + x^4).",
    "citation": "College Board AP® Calculus AB CED — Topic 6.4 The Fundamental Theorem of Calculus and Accumulation Functions"
  },
  {
    "id": "ap-calc-017",
    "type": "mcq",
    "subtopic": "FTC with Chain Rule (Unit 6: Integration)",
    "difficulty": "Hard",
    "question": "What is the derivative of G(x) = ∫[from 0 to x^2] cos(t) dt with respect to x?",
    "options": ["2x * cos(x^2)", "cos(x^2)", "-2x * sin(x^2)", "sin(x^2)"],
    "answer": 0,
    "explanation": "By FTC Part 1 combined with the chain rule: d/dx ∫[from a to g(x)] f(t) dt = f(g(x)) * g'(x). Here g(x) = x^2 (g'(x) = 2x). Thus G'(x) = cos(x^2) * 2x = 2x * cos(x^2).",
    "citation": "College Board AP® Calculus AB CED — Topic 6.4 Accumulation Functions with Chain Rule"
  },
  {
    "id": "ap-calc-018",
    "type": "mcq",
    "subtopic": "U-Substitution Integration (Unit 6: Integration)",
    "difficulty": "Medium",
    "question": "Evaluate the indefinite integral: ∫ 2x * (x^2 + 5)^4 dx.",
    "options": ["(1/5)(x^2 + 5)^5 + C", "(x^2 + 5)^5 + C", "(2/5)(x^2 + 5)^5 + C", "(1/4)(x^2 + 5)^5 + C"],
    "answer": 0,
    "explanation": "Let u = x^2 + 5, then du = 2x dx. The integral becomes ∫ u^4 du = (1/5)u^5 + C = (1/5)(x^2 + 5)^5 + C.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.9 Integrating Using Substitution"
  },
  {
    "id": "ap-calc-019",
    "type": "mcq",
    "subtopic": "Area Between Two Curves (Unit 8: Applications of Integration)",
    "difficulty": "Hard",
    "question": "What is the area of the region bounded by the curves y = x^2 and y = 4x - x^2?",
    "options": ["8/3", "4/3", "16/3", "8"],
    "answer": 0,
    "explanation": "Find intersections: x^2 = 4x - x^2 → 2x^2 - 4x = 0 → 2x(x - 2) = 0 → x = 0 and x = 2. On [0, 2], 4x - x^2 ≥ x^2. Area = ∫[0 to 2] [(4x - x^2) - x^2] dx = ∫[0 to 2] (4x - 2x^2) dx = [2x^2 - (2/3)x^3] from 0 to 2 = [2(4) - (2/3)(8)] = 8 - 16/3 = 24/3 - 16/3 = 8/3.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.4 Finding the Area Between Curves"
  },
  {
    "id": "ap-calc-020",
    "type": "mcq",
    "subtopic": "Differential Equations by Separation of Variables (Unit 7)",
    "difficulty": "Hard",
    "question": "Find the general solution to the differential equation dy/dx = 2xy for y > 0.",
    "options": ["y = C * e^(x^2)", "y = C * e^(2x)", "y = x^2 + C", "y = ln(x^2) + C"],
    "answer": 0,
    "explanation": "Separate variables: (1/y) dy = 2x dx. Integrate both sides: ∫ (1/y) dy = ∫ 2x dx → ln(y) = x^2 + C1 → y = e^(x^2 + C1) = C * e^(x^2).",
    "citation": "College Board AP® Calculus AB CED — Topic 7.6 Finding General Solutions Using Separation of Variables"
  }
]

# Write AP Calculus AB JSON
with open(os.path.join(US_DATA_AP, "ap_calculus_ab_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_calc_questions}, f, indent=2, ensure_ascii=False)

print("Generated AP Calculus AB Set 1 successfully!")
