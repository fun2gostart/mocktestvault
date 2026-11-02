#!/usr/bin/env python3
"""
Generates AP Calculus AB Sets 03, 04, and 05 (60 Questions total):
- ap_calculus_ab_set3.json (Unit 4 & 5: Applications of Derivatives)
- ap_calculus_ab_set4.json (Unit 6: Integration and Accumulation of Change)
- ap_calculus_ab_set5.json (Unit 7 & 8: Differential Equations and Applications of Integration)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_AP = os.path.join(BASE_DIR, "data", "us", "ap")
os.makedirs(US_DATA_AP, exist_ok=True)

# ==============================================================================
# SET 03: APPLICATIONS OF DERIVATIVES (20 Questions - Units 4 & 5)
# ==============================================================================
ap_calc_set3 = [
  {
    "id": "ap-calc-041",
    "type": "mcq",
    "subtopic": "Related Rates: Expanding Circle Area (Unit 4)",
    "difficulty": "Medium",
    "question": "The radius of a circular oil slick is expanding at a constant rate of 3 meters per hour. At what rate, in square meters per hour, is the area of the slick increasing when the radius is 10 meters?",
    "options": ["60π m^2/hr", "30π m^2/hr", "90π m^2/hr", "20π m^2/hr"],
    "answer": 0,
    "explanation": "Area A = πr^2. Differentiate with respect to time t: dA/dt = 2πr * (dr/dt). Given dr/dt = 3 m/hr and r = 10 m: dA/dt = 2π(10)(3) = 60π m^2/hr.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.5 Solving Related Rates Problems"
  },
  {
    "id": "ap-calc-042",
    "type": "mcq",
    "subtopic": "Related Rates: Sliding Ladder (Unit 4)",
    "difficulty": "Hard",
    "question": "A 13-foot ladder leans against a vertical wall. The base of the ladder slides away from the wall at a rate of 2 ft/sec. How fast is the top of the ladder sliding down the wall when the base is 5 feet from the wall?",
    "options": ["-5/6 ft/sec", "-6/5 ft/sec", "-2 ft/sec", "-5/12 ft/sec"],
    "answer": 0,
    "explanation": "By Pythagorean theorem: x^2 + y^2 = 13^2 = 169. When x = 5, y = √(169 - 25) = √144 = 12. Differentiate with respect to t: 2x(dx/dt) + 2y(dy/dt) = 0 → dy/dt = -x(dx/dt) / y. With x = 5, dx/dt = 2, y = 12: dy/dt = -5(2)/12 = -10/12 = -5/6 ft/sec.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.5 Solving Related Rates Problems"
  },
  {
    "id": "ap-calc-043",
    "type": "mcq",
    "subtopic": "Mean Value Theorem (Unit 5)",
    "difficulty": "Medium",
    "question": "The function f(x) = x^3 - 3x satisfies the hypotheses of the Mean Value Theorem on the interval [0, 3]. What is the value of c in (0, 3) that satisfies the conclusion of the theorem?",
    "options": ["√3", "1.5", "1", "2"],
    "answer": 0,
    "explanation": "MVT states f'(c) = [f(b) - f(a)] / (b - a). Here f(3) = 27 - 9 = 18 and f(0) = 0. Average rate of change = (18 - 0) / (3 - 0) = 6. Set f'(c) = 3c^2 - 3 = 6 → 3c^2 = 9 → c^2 = 3 → c = √3 (since √3 ≈ 1.732 is in (0, 3)).",
    "citation": "College Board AP® Calculus AB CED — Topic 5.1 Using the Mean Value Theorem"
  },
  {
    "id": "ap-calc-044",
    "type": "mcq",
    "subtopic": "Rolle's Theorem (Unit 5)",
    "difficulty": "Medium",
    "question": "For f(x) = x^2 - 6x + 8 on the interval [2, 4], at what value of c does f'(c) = 0, as guaranteed by Rolle's Theorem?",
    "options": ["3", "2.5", "3.5", "0"],
    "answer": 0,
    "explanation": "Check hypotheses: f is continuous on [2, 4], differentiable on (2, 4), and f(2) = 4 - 12 + 8 = 0 = f(4) = 16 - 24 + 8 = 0. f'(x) = 2x - 6 = 0 → 2x = 6 → c = 3 ∈ (2, 4).",
    "citation": "College Board AP® Calculus AB CED — Topic 5.1 Rolle's Theorem"
  },
  {
    "id": "ap-calc-045",
    "type": "mcq",
    "subtopic": "Extreme Value Theorem on Closed Interval (Unit 5)",
    "difficulty": "Medium",
    "question": "What is the absolute maximum value of f(x) = 2x^3 - 3x^2 - 12x + 1 on the closed interval [-2, 3]?",
    "options": ["8", "1", "-8", "-19"],
    "answer": 0,
    "explanation": "Critical points: f'(x) = 6x^2 - 6x - 12 = 6(x^2 - x - 2) = 6(x - 2)(x + 1) = 0 → x = 2 and x = -1. Test candidates: Endpoints and critical points: f(-2) = 2(-8) - 3(4) - 12(-2) + 1 = -16 - 12 + 24 + 1 = -3; f(-1) = 2(-1) - 3(1) - 12(-1) + 1 = -2 - 3 + 12 + 1 = 8; f(2) = 2(8) - 3(4) - 12(2) + 1 = 16 - 12 - 24 + 1 = -19; f(3) = 2(27) - 3(9) - 12(3) + 1 = 54 - 27 - 36 + 1 = -8. Absolute maximum is 8 (at x = -1).",
    "citation": "College Board AP® Calculus AB CED — Topic 5.2 Extreme Value Theorem and Candidates Test"
  },
  {
    "id": "ap-calc-046",
    "type": "mcq",
    "subtopic": "First Derivative Test for Local Extrema (Unit 5)",
    "difficulty": "Easy",
    "question": "The derivative of a function f is given by f'(x) = (x - 1)^2 * (x + 3). At which value of x does f have a relative minimum?",
    "options": ["x = -3", "x = 1", "x = 3", "f has no relative minimum"],
    "answer": 0,
    "explanation": "Critical points are x = 1 and x = -3. For x < -3: (x-1)^2 is (+), (x+3) is (-) → f' < 0. For -3 < x < 1: (x-1)^2 is (+), (x+3) is (+) → f' > 0. For x > 1: f' > 0. Since f' changes from negative to positive at x = -3, f has a relative minimum at x = -3. At x = 1, f' does not change sign (no extremum).",
    "citation": "College Board AP® Calculus AB CED — Topic 5.4 Using the First Derivative Test to Determine Extrema"
  },
  {
    "id": "ap-calc-047",
    "type": "mcq",
    "subtopic": "Points of Inflection and Concavity (Unit 5)",
    "difficulty": "Medium",
    "question": "At what x-coordinate does the graph of y = x^4 - 6x^2 + 5 have a point of inflection?",
    "options": ["x = 1 and x = -1", "x = √3 and x = -√3", "x = 0 only", "x = 2 and x = -2"],
    "answer": 0,
    "explanation": "First derivative: y' = 4x^3 - 12x. Second derivative: y'' = 12x^2 - 12 = 12(x^2 - 1) = 12(x - 1)(x + 1). Set y'' = 0 → x = ±1. For x < -1, y'' > 0 (concave up). For -1 < x < 1, y'' < 0 (concave down). For x > 1, y'' > 0 (concave up). Because the concavity changes at both x = -1 and x = 1, both are inflection points.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.6 Determining Concavity and Points of Inflection"
  },
  {
    "id": "ap-calc-048",
    "type": "mcq",
    "subtopic": "Second Derivative Test for Local Extrema (Unit 5)",
    "difficulty": "Easy",
    "question": "Suppose f is a function with f'(4) = 0 and f''(4) = -5. What conclusion can be drawn about the graph of f at x = 4?",
    "options": [
      "f has a relative maximum at x = 4",
      "f has a relative minimum at x = 4",
      "f has a point of inflection at x = 4",
      "No conclusion can be drawn"
    ],
    "answer": 0,
    "explanation": "By the Second Derivative Test: if f'(c) = 0 and f''(c) < 0, the curve has a horizontal tangent and is concave down at c, indicating a relative maximum at c.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.7 Using the Second Derivative Test to Determine Extrema"
  },
  {
    "id": "ap-calc-049",
    "type": "mcq",
    "subtopic": "Straight-Line Particle Motion: Speeding Up (Unit 4)",
    "difficulty": "Hard",
    "question": "The position of a particle moving along the x-axis is s(t) = t^3 - 6t^2 + 9t for t ≥ 0. On which interval of t is the particle's speed increasing?",
    "options": ["(1, 2) and (3, ∞)", "(0, 1) and (2, 3)", "(1, 3)", "(0, 2)"],
    "answer": 0,
    "explanation": "Speed is increasing when velocity v(t) and acceleration a(t) have the same sign. Velocity v(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3). a(t) = 6t - 12 = 6(t - 2). Signs: On (0, 1): v > 0, a < 0 (different sign). On (1, 2): v < 0, a < 0 (both negative → speeding up). On (2, 3): v < 0, a > 0 (different sign). On (3, ∞): v > 0, a > 0 (both positive → speeding up). Thus speed increases on (1, 2) and (3, ∞).",
    "citation": "College Board AP® Calculus AB CED — Topic 4.2 Straight-Line Motion: Connecting Position, Velocity, and Acceleration"
  },
  {
    "id": "ap-calc-050",
    "type": "mcq",
    "subtopic": "Optimization: Maximum Rectangular Area (Unit 5)",
    "difficulty": "Medium",
    "question": "A farmer has 120 meters of fencing to enclose a rectangular pen with one side bordering a straight river (requiring no fencing on that side). What is the maximum area that can be enclosed?",
    "options": ["1,800 m^2", "1,200 m^2", "900 m^2", "2,400 m^2"],
    "answer": 0,
    "explanation": "Let width perpendicular to river be x and length along river be y. Fencing: 2x + y = 120 → y = 120 - 2x. Area A(x) = x * y = x(120 - 2x) = 120x - 2x^2. Set A'(x) = 120 - 4x = 0 → x = 30 m. Length y = 120 - 60 = 60 m. Max Area = 30 * 60 = 1,800 m^2.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.11 Solving Optimization Problems"
  },
  {
    "id": "ap-calc-051",
    "type": "mcq",
    "subtopic": "L'Hôpital's Rule with Transcendental Functions (Unit 4)",
    "difficulty": "Medium",
    "question": "What is the value of lim(x→0) [(e^(2x) - 1 - 2x) / x^2]?",
    "options": ["2", "1", "4", "0"],
    "answer": 0,
    "explanation": "Evaluating at x = 0 gives (1 - 1 - 0) / 0 = 0/0 (indeterminate). Apply L'Hôpital's rule: lim(x→0) [2e^(2x) - 2] / (2x) = 0/0. Apply L'Hôpital's rule a second time: lim(x→0) [4e^(2x)] / 2 = 4(1) / 2 = 2.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.7 Using L'Hôpital's Rule for Determining Limits of Indeterminate Forms"
  },
  {
    "id": "ap-calc-052",
    "type": "mcq",
    "subtopic": "Connecting Graph of f' to Features of f (Unit 5)",
    "difficulty": "Hard",
    "question": "If the graph of f' is an inverted parabola that intersects the x-axis at x = -2 and x = 4, which of the following is true about f?",
    "options": [
      "f is concave down on (-∞, 1) and concave up on (1, ∞)",
      "f has a relative maximum at x = 4 and a relative minimum at x = -2",
      "f has a relative minimum at x = 4 and a relative maximum at x = -2",
      "f is increasing on (-∞, -2) and decreasing on (-2, 4)"
    ],
    "answer": 1,
    "explanation": "For an inverted parabola with roots -2 and 4: f' < 0 for x < -2, f' > 0 for -2 < x < 4, and f' < 0 for x > 4. At x = -2, f' changes from (-) to (+) → relative minimum at x = -2. At x = 4, f' changes from (+) to (-) → relative maximum at x = 4. Option 1 states this accurately.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.8 Sketching Graphs of Functions and Their Derivatives"
  },
  {
    "id": "ap-calc-053",
    "type": "mcq",
    "subtopic": "Related Rates: Conical Tank (Unit 4)",
    "difficulty": "Hard",
    "question": "Water is poured into an inverted right circular cone of base radius 4 m and height 8 m at a rate of 2 m^3/min. At what rate is the water level rising when the water depth is 4 m?",
    "options": ["1 / (2π) m/min", "1 / π m/min", "2 / π m/min", "1 / (4π) m/min"],
    "answer": 0,
    "explanation": "By similar triangles, r / h = 4 / 8 = 1/2 → r = h/2. Volume V = (1/3)πr^2 * h = (1/3)π(h/2)^2 * h = (π/12)h^3. Differentiate with respect to t: dV/dt = (π/4)h^2 * (dh/dt). Given dV/dt = 2 and h = 4: 2 = (π/4)(16) * (dh/dt) → 2 = 4π * (dh/dt) → dh/dt = 2 / (4π) = 1 / (2π) m/min.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.5 Solving Related Rates Problems"
  },
  {
    "id": "ap-calc-054",
    "type": "mcq",
    "subtopic": "Optimization: Minimum Surface Area Box (Unit 5)",
    "difficulty": "Hard",
    "question": "An open-top rectangular box with a square base has a fixed volume of 32 cubic inches. What dimensions of the base minimize the total surface area?",
    "options": ["4 in by 4 in", "2 in by 2 in", "8 in by 8 in", "√32 in by √32 in"],
    "answer": 0,
    "explanation": "Let side of square base be x and height be h. Volume V = x^2 * h = 32 → h = 32 / x^2. Surface area S = x^2 + 4xh = x^2 + 4x(32/x^2) = x^2 + 128/x. Differentiate: S'(x) = 2x - 128/x^2 = 0 → 2x^3 = 128 → x^3 = 64 → x = 4 inches.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.11 Solving Optimization Problems"
  },
  {
    "id": "ap-calc-055",
    "type": "mcq",
    "subtopic": "Total Distance Traveled by Particle (Unit 4)",
    "difficulty": "Hard",
    "question": "A particle moves along a straight line with velocity v(t) = 2t - 4 m/s on the time interval [0, 4]. What is the total distance traveled by the particle?",
    "options": ["8 meters", "0 meters", "4 meters", "12 meters"],
    "answer": 0,
    "explanation": "Total distance is ∫[0 to 4] |v(t)| dt. v(t) = 0 at t = 2. On [0, 2], v(t) ≤ 0: distance = |∫[0 to 2] (2t - 4) dt| = |[t^2 - 4t]_0^2| = |4 - 8| = 4 m. On [2, 4], v(t) ≥ 0: distance = ∫[2 to 4] (2t - 4) dt = [t^2 - 4t]_2^4 = (16 - 16) - (4 - 8) = 4 m. Total distance = 4 + 4 = 8 meters. (Displacement is 0 m).",
    "citation": "College Board AP® Calculus AB CED — Topic 4.2 Straight-Line Motion: Connecting Position, Velocity, and Acceleration"
  },
  {
    "id": "ap-calc-056",
    "type": "mcq",
    "subtopic": "L'Hôpital's Rule with Logarithms (Unit 4)",
    "difficulty": "Medium",
    "question": "What is the value of lim(x→1) [ln(x) / (x^2 - 1)]?",
    "options": ["1/2", "1", "0", "Does not exist"],
    "answer": 0,
    "explanation": "Direct substitution gives ln(1) / (1 - 1) = 0/0. Apply L'Hôpital's rule: derivative of numerator is 1/x; derivative of denominator is 2x. lim(x→1) [(1/x) / (2x)] = 1 / (2*1) = 1/2.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.7 Using L'Hôpital's Rule for Indeterminate Forms"
  },
  {
    "id": "ap-calc-057",
    "type": "mcq",
    "subtopic": "Related Rates: Moving Shadow (Unit 4)",
    "difficulty": "Hard",
    "question": "A person 6 feet tall walks away from a 15-foot lamppost at a speed of 5 ft/s. At what rate is the length of the person's shadow increasing?",
    "options": ["10/3 ft/s", "5/2 ft/s", "15/4 ft/s", "5 ft/s"],
    "answer": 0,
    "explanation": "Let x be distance from post and s be length of shadow. By similar triangles: 15 / (x + s) = 6 / s → 15s = 6x + 6s → 9s = 6x → s = (2/3)x. Differentiate: ds/dt = (2/3)(dx/dt) = (2/3)(5) = 10/3 ft/s.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.5 Solving Related Rates Problems"
  },
  {
    "id": "ap-calc-058",
    "type": "mcq",
    "subtopic": "Concavity and Point of Inflection Criteria (Unit 5)",
    "difficulty": "Medium",
    "question": "If f''(c) = 0, which condition guarantees that (c, f(c)) is a point of inflection?",
    "options": [
      "f''(x) changes sign from positive to negative or negative to positive at x = c",
      "f'(c) = 0",
      "f''(x) > 0 for all x > c",
      "f(x) has a horizontal tangent at x = c"
    ],
    "answer": 0,
    "explanation": "A point of inflection is defined as a point where the concavity of the graph changes. Having f''(c) = 0 is a necessary condition for a twice-differentiable function, but an inflection point occurs if and only if f'' changes sign across x = c.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.6 Determining Concavity and Points of Inflection"
  },
  {
    "id": "ap-calc-059",
    "type": "mcq",
    "subtopic": "Rate of Change of Volume of a Sphere (Unit 4)",
    "difficulty": "Easy",
    "question": "The volume of a sphere is expanding. If the radius is 5 cm and is increasing at a rate of 2 cm/s, how fast is the volume increasing?",
    "options": ["200π cm^3/s", "100π cm^3/s", "50π cm^3/s", "400π cm^3/s"],
    "answer": 0,
    "explanation": "Volume V = (4/3)πr^3. dV/dt = 4πr^2 * (dr/dt). With r = 5 and dr/dt = 2: dV/dt = 4π(25)(2) = 200π cm^3/s.",
    "citation": "College Board AP® Calculus AB CED — Topic 4.5 Solving Related Rates Problems"
  },
  {
    "id": "ap-calc-060",
    "type": "mcq",
    "subtopic": "Critical Numbers vs Local Extrema (Unit 5)",
    "difficulty": "Medium",
    "question": "Which of the following functions has a critical number at x = 0 that is neither a local maximum nor a local minimum?",
    "options": ["f(x) = x^3", "f(x) = x^2", "f(x) = -x^2", "f(x) = |x|"],
    "answer": 0,
    "explanation": "For f(x) = x^3, f'(x) = 3x^2. f'(0) = 0 (so x = 0 is a critical point). However, f'(x) > 0 for both x < 0 and x > 0. Since f' does not change sign, x = 0 is a point of inflection with a horizontal tangent, not an extremum.",
    "citation": "College Board AP® Calculus AB CED — Topic 5.4 First Derivative Test"
  }
]

# Write AP Calc Set 3
with open(os.path.join(US_DATA_AP, "ap_calculus_ab_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_calc_set3}, f, indent=2, ensure_ascii=False)
print("Generated ap_calculus_ab_set3.json (20 Qs)!")

# ==============================================================================
# SET 04: INTEGRATION & ACCUMULATION OF CHANGE (20 Questions - Unit 6)
# ==============================================================================
ap_calc_set4 = [
  {
    "id": "ap-calc-061",
    "type": "mcq",
    "subtopic": "Trapezoidal Rule Approximation (Unit 6)",
    "difficulty": "Medium",
    "question": "Approximate ∫[0 to 4] x^2 dx using the trapezoidal rule with 4 subintervals of equal width.",
    "options": ["22", "21.33", "20", "24"],
    "answer": 0,
    "explanation": "Subinterval width Δx = (4 - 0) / 4 = 1. Grid points: 0, 1, 2, 3, 4. Function values: f(0)=0, f(1)=1, f(2)=4, f(3)=9, f(4)=16. Trapezoidal sum = (Δx/2) * [f(0) + 2f(1) + 2f(2) + 2f(3) + f(4)] = (1/2) * [0 + 2(1) + 2(4) + 2(9) + 16] = (1/2) * [0 + 2 + 8 + 18 + 16] = (1/2) * 44 = 22.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.2 Approximating Areas with Riemann Sums and Trapezoidal Rule"
  },
  {
    "id": "ap-calc-062",
    "type": "mcq",
    "subtopic": "Average Value of a Function (Unit 6)",
    "difficulty": "Medium",
    "question": "What is the average value of the function f(x) = 3x^2 - 4x on the interval [1, 4]?",
    "options": ["11", "33", "7", "15"],
    "answer": 0,
    "explanation": "Average value formula: f_avg = (1 / (b - a)) * ∫[a to b] f(x) dx. Here b - a = 4 - 1 = 3. ∫[1 to 4] (3x^2 - 4x) dx = [x^3 - 2x^2]_1^4 = (64 - 32) - (1 - 2) = 32 - (-1) = 33. Average value = 33 / 3 = 11.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.5 Finding the Average Value of a Function on an Interval"
  },
  {
    "id": "ap-calc-063",
    "type": "mcq",
    "subtopic": "Properties of Definite Integrals (Unit 6)",
    "difficulty": "Easy",
    "question": "If ∫[1 to 5] f(x) dx = 12 and ∫[1 to 3] f(x) dx = 4, what is the value of ∫[3 to 5] (2f(x) - 3) dx?",
    "options": ["10", "16", "8", "13"],
    "answer": 0,
    "explanation": "∫[3 to 5] f(x) dx = ∫[1 to 5] f(x) dx - ∫[1 to 3] f(x) dx = 12 - 4 = 8. Now evaluate ∫[3 to 5] (2f(x) - 3) dx = 2 * ∫[3 to 5] f(x) dx - ∫[3 to 5] 3 dx = 2(8) - 3(5 - 3) = 16 - 6 = 10.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.6 Properties of Definite Integrals"
  },
  {
    "id": "ap-calc-064",
    "type": "mcq",
    "subtopic": "FTC Part 1 with Upper and Lower Bounds (Unit 6)",
    "difficulty": "Hard",
    "question": "If F(x) = ∫[x to 2x] (3t + 1) dt, what is F'(x)?",
    "options": ["9x + 1", "6x + 2", "3x", "12x + 1"],
    "answer": 0,
    "explanation": "Split the integral: F(x) = ∫[0 to 2x] (3t + 1) dt - ∫[0 to x] (3t + 1) dt. Differentiate with respect to x using FTC Part 1 and chain rule: F'(x) = [3(2x) + 1] * (2) - [3(x) + 1] * (1) = (6x + 1)(2) - (3x + 1) = 12x + 2 - 3x - 1 = 9x + 1.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.4 Fundamental Theorem of Calculus Part 1"
  },
  {
    "id": "ap-calc-065",
    "type": "mcq",
    "subtopic": "Definite Integral by U-Substitution (Unit 6)",
    "difficulty": "Medium",
    "question": "Evaluate the definite integral: ∫[0 to 1] x * e^(x^2) dx.",
    "options": ["(e - 1) / 2", "e - 1", "(e + 1) / 2", "e / 2"],
    "answer": 0,
    "explanation": "Let u = x^2, then du = 2x dx → x dx = du/2. When x = 0, u = 0; when x = 1, u = 1. Integral becomes (1/2) * ∫[0 to 1] e^u du = (1/2)[e^u]_0^1 = (1/2)(e^1 - e^0) = (e - 1) / 2.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.9 Integrating Using Substitution"
  },
  {
    "id": "ap-calc-066",
    "type": "mcq",
    "subtopic": "Indefinite Integral with Trigonometry (Unit 6)",
    "difficulty": "Medium",
    "question": "Evaluate: ∫ sec^2(3x) dx.",
    "options": ["(1/3) * tan(3x) + C", "3 * tan(3x) + C", "tan(3x) + C", "(1/3) * sec^3(3x) + C"],
    "answer": 0,
    "explanation": "Let u = 3x, du = 3 dx. ∫ sec^2(3x) dx = (1/3) ∫ sec^2(u) du = (1/3) * tan(u) + C = (1/3) * tan(3x) + C.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.8 Indefinite Integrals of Basic Functions"
  },
  {
    "id": "ap-calc-067",
    "type": "mcq",
    "subtopic": "Integrals Resulting in Inverse Trig Functions (Unit 6)",
    "difficulty": "Hard",
    "question": "What is the value of ∫[0 to 2] [1 / (4 + x^2)] dx?",
    "options": ["π / 8", "π / 4", "π / 2", "1 / 4"],
    "answer": 0,
    "explanation": "Standard integral form: ∫ [1 / (a^2 + x^2)] dx = (1/a) * arctan(x/a) + C. Here a = 2. Value = [(1/2) * arctan(x/2)]_0^2 = (1/2) * [arctan(1) - arctan(0)] = (1/2) * (π/4 - 0) = π / 8.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.10 Integrating Functions Using Long Division or Completing the Square"
  },
  {
    "id": "ap-calc-068",
    "type": "mcq",
    "subtopic": "U-Substitution with Algebraic Adjustments (Unit 6)",
    "difficulty": "Hard",
    "question": "Evaluate the indefinite integral: ∫ x * √(x - 1) dx.",
    "options": [
      "(2/5)(x - 1)^(5/2) + (2/3)(x - 1)^(3/2) + C",
      "(2/5)(x - 1)^(5/2) - (2/3)(x - 1)^(3/2) + C",
      "(1/2)x^2 * (2/3)(x - 1)^(3/2) + C",
      "(2/3)(x - 1)^(3/2) + C"
    ],
    "answer": 0,
    "explanation": "Let u = x - 1 → x = u + 1 and dx = du. The integral becomes ∫ (u + 1) * u^(1/2) du = ∫ (u^(3/2) + u^(1/2)) du = (2/5)u^(5/2) + (2/3)u^(3/2) + C = (2/5)(x - 1)^(5/2) + (2/3)(x - 1)^(3/2) + C.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.9 Integrating Using Substitution"
  },
  {
    "id": "ap-calc-069",
    "type": "mcq",
    "subtopic": "Definite Integral of Odd and Even Functions (Unit 6)",
    "difficulty": "Easy",
    "question": "What is the value of ∫[-π to π] [x^3 * cos(x) + 5] dx?",
    "options": ["10π", "0", "5π", "20π"],
    "answer": 0,
    "explanation": "Break into two integrals: ∫[-π to π] x^3 * cos(x) dx + ∫[-π to π] 5 dx. The function g(x) = x^3 * cos(x) is odd (since (-x)^3 * cos(-x) = -x^3 * cos(x)). The integral of any odd continuous function over a symmetric interval [-a, a] is strictly 0. ∫[-π to π] 5 dx = 5 * [π - (-π)] = 5 * 2π = 10π. Total = 0 + 10π = 10π.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.6 Properties of Definite Integrals and Symmetry"
  },
  {
    "id": "ap-calc-070",
    "type": "mcq",
    "subtopic": "Left vs Right Riemann Sum Error (Unit 6)",
    "difficulty": "Medium",
    "question": "If f(x) is a strictly increasing, continuous function on [a, b], which of the following is true regarding Riemann sum approximations of ∫[a to b] f(x) dx?",
    "options": [
      "The Left Riemann Sum is an underestimate, and the Right Riemann Sum is an overestimate",
      "The Left Riemann Sum is an overestimate, and the Right Riemann Sum is an underestimate",
      "Both Left and Right sums are overestimates",
      "Both Left and Right sums are underestimates"
    ],
    "answer": 0,
    "explanation": "For any strictly increasing function, the function value at the left endpoint of every subinterval is the minimum value on that subinterval (producing an underestimate), while the right endpoint is the maximum value (producing an overestimate).",
    "citation": "College Board AP® Calculus AB CED — Topic 6.2 Riemann Sums and Monotonic Functions"
  },
  {
    "id": "ap-calc-071",
    "type": "mcq",
    "subtopic": "Net Change Theorem (Unit 6)",
    "difficulty": "Medium",
    "question": "A reservoir contains 500 gallons of water at t = 0. Water flows into the reservoir at a rate of r(t) = 100 * e^(-0.2t) gallons per hour. How much water is in the reservoir at t = 5 hours?",
    "options": [
      "500 + 500(1 - e^-1) gallons",
      "500 + 100(1 - e^-1) gallons",
      "500 - 500e^-1 gallons",
      "1,000 gallons"
    ],
    "answer": 0,
    "explanation": "Total water at t = 5: W(5) = W(0) + ∫[0 to 5] r(t) dt = 500 + ∫[0 to 5] 100 * e^(-0.2t) dt. Antiderivative is 100 / (-0.2) * e^(-0.2t) = -500 * e^(-0.2t). Evaluate from 0 to 5: -500(e^-1 - e^0) = 500(1 - e^-1). Total = 500 + 500(1 - e^-1) gallons.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.3 The Fundamental Theorem of Calculus and Accumulation Functions"
  },
  {
    "id": "ap-calc-072",
    "type": "mcq",
    "subtopic": "Midpoint Riemann Sum (Unit 6)",
    "difficulty": "Medium",
    "question": "Use a Midpoint Riemann Sum with n = 2 subintervals of equal width to approximate ∫[0 to 4] (x^3 + 1) dx.",
    "options": ["34", "68", "17", "28"],
    "answer": 0,
    "explanation": "Interval [0, 4] with n = 2 gives Δx = 2. Subintervals are [0, 2] and [2, 4]. Midpoints are m1 = 1 and m2 = 3. Function values: f(1) = 1^3 + 1 = 2; f(3) = 3^3 + 1 = 28. Midpoint sum = Δx * [f(m1) + f(m2)] = 2 * (2 + 28) = 2 * 30 = 60? Wait! Let's re-calculate: 2 * (2 + 28) = 60. Wait, let's make options: ['68', '60', '34', '72']. Wait, 2 * (2 + 28) = 60. Let's make options: ['60', '68', '34', '72'].",
    "options": ["60", "68", "34", "72"],
    "answer": 0,
    "explanation": "Interval [0, 4] with n = 2 has subinterval width Δx = 2. Subintervals: [0, 2] with midpoint 1; [2, 4] with midpoint 3. f(1) = 1 + 1 = 2. f(3) = 27 + 1 = 28. Midpoint sum = 2 * (2 + 28) = 2 * 30 = 60.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.2 Midpoint Riemann Sums"
  },
  {
    "id": "ap-calc-073",
    "type": "mcq",
    "subtopic": "Integral of 1/x (Unit 6)",
    "difficulty": "Easy",
    "question": "What is the value of ∫[1 to e^3] (1 / x) dx?",
    "options": ["3", "e^3 - 1", "ln(3)", "1/3"],
    "answer": 0,
    "explanation": "Antiderivative of 1/x is ln|x|. Evaluated from 1 to e^3: ln(e^3) - ln(1) = 3 - 0 = 3.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.8 Indefinite Integrals of Basic Functions"
  },
  {
    "id": "ap-calc-074",
    "type": "mcq",
    "subtopic": "Integration with Negative Powers (Unit 6)",
    "difficulty": "Easy",
    "question": "Evaluate: ∫ (3/x^2 - 4/x^3) dx.",
    "options": ["-3/x + 2/x^2 + C", "3/x - 2/x^2 + C", "-3/x - 2/x^2 + C", "-6/x^3 + 12/x^4 + C"],
    "answer": 0,
    "explanation": "Rewrite with negative exponents: ∫ (3x^(-2) - 4x^(-3)) dx = 3(x^(-1)/-1) - 4(x^(-2)/-2) + C = -3/x + 2/x^2 + C.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.8 Indefinite Integrals of Basic Functions"
  },
  {
    "id": "ap-calc-075",
    "type": "mcq",
    "subtopic": "Accumulation Function Derivative (Unit 6)",
    "difficulty": "Medium",
    "question": "If g(x) = ∫[2 to x] √(t^3 + 1) dt, what is the value of g'(2)?",
    "options": ["3", "0", "9", "Undefined"],
    "answer": 0,
    "explanation": "By FTC Part 1, g'(x) = √(x^3 + 1). Evaluating at x = 2 gives g'(2) = √(2^3 + 1) = √(8 + 1) = √9 = 3.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.4 Accumulation Functions"
  },
  {
    "id": "ap-calc-076",
    "type": "mcq",
    "subtopic": "Definite Integral of Absolute Value (Unit 6)",
    "difficulty": "Medium",
    "question": "What is the value of ∫[-2 to 3] |x| dx?",
    "options": ["13/2", "5/2", "5", "13"],
    "answer": 0,
    "explanation": "Split the integral at x = 0: ∫[-2 to 0] (-x) dx + ∫[0 to 3] (x) dx = [-x^2/2]_{-2}^0 + [x^2/2]_0^3 = (0 - (-4/2)) + (9/2 - 0) = 2 + 9/2 = 4/2 + 9/2 = 13/2.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.6 Properties of Definite Integrals and Piecewise Integrals"
  },
  {
    "id": "ap-calc-077",
    "type": "mcq",
    "subtopic": "U-Substitution with Trig Composition (Unit 6)",
    "difficulty": "Medium",
    "question": "Evaluate: ∫ cos(x) * sin^4(x) dx.",
    "options": ["(1/5) * sin^5(x) + C", "(1/5) * cos^5(x) + C", "-(1/5) * sin^5(x) + C", "sin^5(x) + C"],
    "answer": 0,
    "explanation": "Let u = sin(x), then du = cos(x) dx. The integral becomes ∫ u^4 du = (1/5)u^5 + C = (1/5) * sin^5(x) + C.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.9 Integrating Using Substitution"
  },
  {
    "id": "ap-calc-078",
    "type": "mcq",
    "subtopic": "Interpreting Integral from a Graph (Unit 6)",
    "difficulty": "Medium",
    "question": "The graph of f consists of a semicircle of radius 2 centered at (2, 0) above the x-axis on [0, 4] and a triangle with vertices (4, 0), (6, -3), and (8, 0) below the x-axis. What is ∫[0 to 8] f(x) dx?",
    "options": ["2π - 6", "4π - 6", "2π - 12", "4π - 12"],
    "answer": 0,
    "explanation": "Area above x-axis on [0, 4]: semicircle of radius r = 2 has area (1/2)πr^2 = (1/2)π(4) = 2π. Area below x-axis on [4, 8]: triangle has base = 8 - 4 = 4 and height = 3, area = (1/2)(4)(3) = 6. Since it is below the x-axis, its integral is -6. Total ∫[0 to 8] f(x) dx = 2π - 6.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.6 Definite Integrals as Geometric Area"
  },
  {
    "id": "ap-calc-079",
    "type": "mcq",
    "subtopic": "FTC Part 2 with Given Derivative (Unit 6)",
    "difficulty": "Easy",
    "question": "If f'(x) is continuous on [1, 5] with f(1) = 7 and f(5) = 19, what is ∫[1 to 5] f'(x) dx?",
    "options": ["12", "26", "6", "19"],
    "answer": 0,
    "explanation": "By the Fundamental Theorem of Calculus Part 2: ∫[a to b] f'(x) dx = f(b) - f(a). Here f(5) - f(1) = 19 - 7 = 12.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.7 Fundamental Theorem of Calculus Part 2"
  },
  {
    "id": "ap-calc-080",
    "type": "mcq",
    "subtopic": "Integral with Radical in Denominator (Unit 6)",
    "difficulty": "Medium",
    "question": "Evaluate the definite integral: ∫[0 to 3] [x / √(x^2 + 16)] dx.",
    "options": ["1", "5", "4", "2"],
    "answer": 0,
    "explanation": "Let u = x^2 + 16, du = 2x dx → x dx = du/2. When x = 0, u = 16; when x = 3, u = 25. The integral becomes (1/2) ∫[16 to 25] u^(-1/2) du = (1/2) * [2u^(1/2)]_16^25 = [√u]_16^25 = √25 - √16 = 5 - 4 = 1.",
    "citation": "College Board AP® Calculus AB CED — Topic 6.9 Integrating Using Substitution"
  }
]

# Write AP Calc Set 4
with open(os.path.join(US_DATA_AP, "ap_calculus_ab_set4.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_calc_set4}, f, indent=2, ensure_ascii=False)
print("Generated ap_calculus_ab_set4.json (20 Qs)!")

# ==============================================================================
# SET 05: DIFFERENTIAL EQUATIONS & APPLICATIONS OF INTEGRATION (20 Questions - Units 7 & 8)
# ==============================================================================
ap_calc_set5 = [
  {
    "id": "ap-calc-081",
    "type": "mcq",
    "subtopic": "Slope Fields Matching (Unit 7)",
    "difficulty": "Medium",
    "question": "Which differential equation has a slope field where all tangent segments along the y-axis (where x = 0) are horizontal?",
    "options": ["dy/dx = x * y", "dy/dx = y / x", "dy/dx = x + y", "dy/dx = y - x"],
    "answer": 0,
    "explanation": "Along the y-axis, x = 0. Tangent segments are horizontal when dy/dx = 0. For dy/dx = x * y, when x = 0, dy/dx = 0 * y = 0 for all y.",
    "citation": "College Board AP® Calculus AB CED — Topic 7.3 Sketching and Interpreting Slope Fields"
  },
  {
    "id": "ap-calc-082",
    "type": "mcq",
    "subtopic": "Separation of Variables with Initial Condition (Unit 7)",
    "difficulty": "Hard",
    "question": "Find the particular solution to the differential equation dy/dx = (3x^2) / y for y > 0, given the initial condition y(0) = 4.",
    "options": ["y = √(2x^3 + 16)", "y = x^3 + 4", "y = √(x^3 + 16)", "y = 2x^3 + 16"],
    "answer": 0,
    "explanation": "Separate variables: y dy = 3x^2 dx. Integrate both sides: ∫ y dy = ∫ 3x^2 dx → y^2 / 2 = x^3 + C → y^2 = 2x^3 + 2C. Use y(0) = 4: 4^2 = 2(0) + 2C → 16 = 2C. Thus y^2 = 2x^3 + 16 → y = √(2x^3 + 16) (since y > 0).",
    "citation": "College Board AP® Calculus AB CED — Topic 7.7 Particular Solutions Using Initial Conditions"
  },
  {
    "id": "ap-calc-083",
    "type": "mcq",
    "subtopic": "Exponential Growth and Decay (Unit 7)",
    "difficulty": "Medium",
    "question": "The rate of growth of a bacteria population P(t) is directly proportional to its population: dP/dt = kP. If the initial population is 200 and the population doubles every 3 hours, what is the value of k?",
    "options": ["ln(2) / 3", "3 * ln(2)", "ln(3) / 2", "2 / 3"],
    "answer": 0,
    "explanation": "The solution to dP/dt = kP is P(t) = P0 * e^(kt). Given P(3) = 2 * P0: P0 * e^(3k) = 2 * P0 → e^(3k) = 2 → 3k = ln(2) → k = ln(2) / 3.",
    "citation": "College Board AP® Calculus AB CED — Topic 7.8 Exponential Models with Differential Equations"
  },
  {
    "id": "ap-calc-084",
    "type": "mcq",
    "subtopic": "Area Between Two Curves (Unit 8)",
    "difficulty": "Medium",
    "question": "What is the area of the region in the first quadrant bounded by the curves y = √x and y = x^2?",
    "options": ["1/3", "2/3", "1/6", "1"],
    "answer": 0,
    "explanation": "Find intersections: √x = x^2 → x = x^4 → x(x^3 - 1) = 0 → x = 0 and x = 1. On [0, 1], √x ≥ x^2. Area = ∫[0 to 1] (x^(1/2) - x^2) dx = [(2/3)x^(3/2) - (1/3)x^3]_0^1 = (2/3 - 1/3) = 1/3.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.4 Finding the Area Between Curves Expressed as Functions of x"
  },
  {
    "id": "ap-calc-085",
    "type": "mcq",
    "subtopic": "Area Between Curves Integrating with Respect to y (Unit 8)",
    "difficulty": "Hard",
    "question": "What is the area of the region bounded by x = y^2 - 2 and x = y?",
    "options": ["9/2", "7/2", "9/4", "3"],
    "answer": 0,
    "explanation": "Set curves equal to find y-limits: y^2 - 2 = y → y^2 - y - 2 = 0 → (y - 2)(y + 1) = 0 → y = -1 and y = 2. On [-1, 2], the right curve is x = y and the left curve is x = y^2 - 2. Area = ∫[-1 to 2] [y - (y^2 - 2)] dy = ∫[-1 to 2] (y - y^2 + 2) dy = [y^2/2 - y^3/3 + 2y]_{-1}^2 = (2 - 8/3 + 4) - (1/2 + 1/3 - 2) = (6 - 8/3) - (-3/2 + 1/3) = (10/3) - (-7/6) = 20/6 + 7/6 = 27/6 = 9/2.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.5 Finding the Area Between Curves Expressed as Functions of y"
  },
  {
    "id": "ap-calc-086",
    "type": "mcq",
    "subtopic": "Volume of Solid: Disk Method (Unit 8)",
    "difficulty": "Medium",
    "question": "The region bounded by y = 2x, y = 0, and x = 3 is revolved around the x-axis. What is the volume of the resulting solid?",
    "options": ["36π", "18π", "54π", "12π"],
    "answer": 0,
    "explanation": "Disk method formula: V = π ∫[a to b] [f(x)]^2 dx. V = π ∫[0 to 3] (2x)^2 dx = π ∫[0 to 3] 4x^2 dx = π [4x^3 / 3]_0^3 = π [4(27) / 3] = π(36) = 36π.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.9 Volume with Disc Method: Revolving Around the x- or y-Axis"
  },
  {
    "id": "ap-calc-087",
    "type": "mcq",
    "subtopic": "Volume of Solid: Washer Method (Unit 8)",
    "difficulty": "Hard",
    "question": "The region bounded by y = x and y = x^2 is revolved around the x-axis. What is the volume of the generated solid?",
    "options": ["2π / 15", "π / 15", "2π / 5", "π / 3"],
    "answer": 0,
    "explanation": "Intersections are at x = 0 and x = 1. On [0, 1], outer radius R(x) = x, inner radius r(x) = x^2. Washer formula: V = π ∫[0 to 1] ([R(x)]^2 - [r(x)]^2) dx = π ∫[0 to 1] (x^2 - x^4) dx = π [x^3/3 - x^5/5]_0^1 = π (1/3 - 1/5) = π (2/15) = 2π / 15.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.11 Volume with Washer Method: Revolving Around the x- or y-Axis"
  },
  {
    "id": "ap-calc-088",
    "type": "mcq",
    "subtopic": "Volume of Solid with Square Cross-Sections (Unit 8)",
    "difficulty": "Hard",
    "question": "The base of a solid is the region bounded by y = 4 - x^2 and the x-axis. Cross-sections perpendicular to the x-axis are squares. What is the volume of the solid?",
    "options": ["512 / 15", "256 / 15", "128 / 5", "64 / 3"],
    "answer": 0,
    "explanation": "Base extends from x = -2 to x = 2 (where 4 - x^2 = 0). The side length of each square cross-section is s(x) = y = 4 - x^2. Area of cross-section A(x) = s^2 = (4 - x^2)^2 = 16 - 8x^2 + x^4. Volume V = ∫[-2 to 2] (16 - 8x^2 + x^4) dx = 2 * ∫[0 to 2] (16 - 8x^2 + x^4) dx = 2 * [16x - (8/3)x^3 + x^5/5]_0^2 = 2 * [32 - 64/3 + 32/5] = 2 * 32 * [1 - 2/3 + 1/5] = 64 * [15/15 - 10/15 + 3/15] = 64 * (8/15) = 512 / 15.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.7 Volumes with Cross Sections: Squares and Rectangles"
  },
  {
    "id": "ap-calc-089",
    "type": "mcq",
    "subtopic": "Volume with Semicircular Cross-Sections (Unit 8)",
    "difficulty": "Hard",
    "question": "The base of a solid is bounded by y = sin(x) and the x-axis on [0, π]. Each cross-section perpendicular to the x-axis is a semicircle with diameter lying in the base. What is the volume of the solid?",
    "options": ["π^2 / 16", "π^2 / 8", "π / 8", "π^2 / 4"],
    "answer": 0,
    "explanation": "Diameter of semicircle d = sin(x) → radius r = (1/2)sin(x). Area of semicircle cross-section A(x) = (1/2)πr^2 = (1/2)π[(1/2)sin(x)]^2 = (π/8)sin^2(x). Recall ∫[0 to π] sin^2(x) dx = π/2. Volume = (π/8) * (π/2) = π^2 / 16.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.8 Volumes with Cross Sections: Triangles and Semicircles"
  },
  {
    "id": "ap-calc-090",
    "type": "mcq",
    "subtopic": "Separation of Variables with Natural Log Solution (Unit 7)",
    "difficulty": "Medium",
    "question": "What is the general solution to dy/dx = 4x * (y - 1) for y > 1?",
    "options": ["y = 1 + C * e^(2x^2)", "y = C * e^(4x) + 1", "y = 2x^2 + C", "y = 1 + e^(4x^2)"],
    "answer": 0,
    "explanation": "Separate variables: [1 / (y - 1)] dy = 4x dx. Integrate: ln(y - 1) = 2x^2 + C1 → y - 1 = e^(2x^2 + C1) = C * e^(2x^2) → y = 1 + C * e^(2x^2).",
    "citation": "College Board AP® Calculus AB CED — Topic 7.6 Finding General Solutions Using Separation of Variables"
  },
  {
    "id": "ap-calc-091",
    "type": "mcq",
    "subtopic": "Revolution Around a Non-Axis Line (Unit 8)",
    "difficulty": "Hard",
    "question": "The region bounded by y = √x, y = 0, and x = 4 is revolved around the vertical line x = 4. Which integral expression gives the volume using horizontal disks?",
    "options": [
      "π ∫[0 to 2] (4 - y^2)^2 dy",
      "π ∫[0 to 4] (4 - √x)^2 dx",
      "π ∫[0 to 2] (16 - y^4) dy",
      "2π ∫[0 to 2] (4 - y^2) dy"
    ],
    "answer": 0,
    "explanation": "In terms of y, curve is x = y^2, y ranges from 0 to √4 = 2. Revolved around the vertical line x = 4, horizontal disks have radius R(y) = 4 - x = 4 - y^2. Volume = π ∫[0 to 2] [R(y)]^2 dy = π ∫[0 to 2] (4 - y^2)^2 dy.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.12 Volume with Washer Method: Revolving Around Other Axes"
  },
  {
    "id": "ap-calc-092",
    "type": "mcq",
    "subtopic": "Verifying Solutions to Differential Equations (Unit 7)",
    "difficulty": "Easy",
    "question": "Which of the following functions is a solution to the differential equation y'' + 9y = 0?",
    "options": ["y = 4 * cos(3x)", "y = e^(3x)", "y = 3 * sin(9x)", "y = 9 * cos(x)"],
    "answer": 0,
    "explanation": "For y = 4*cos(3x): y' = -12*sin(3x) and y'' = -36*cos(3x). Substitute into equation: -36*cos(3x) + 9(4*cos(3x)) = -36*cos(3x) + 36*cos(3x) = 0.",
    "citation": "College Board AP® Calculus AB CED — Topic 7.2 Verifying Solutions for Differential Equations"
  },
  {
    "id": "ap-calc-093",
    "type": "mcq",
    "subtopic": "Newton's Law of Cooling Model (Unit 7)",
    "difficulty": "Medium",
    "question": "Newton's Law of Cooling states that the rate of change of temperature T(t) of an object is proportional to the difference between T(t) and the ambient temperature T_m. Which differential equation represents this law for a positive constant k?",
    "options": ["dT/dt = -k(T - T_m)", "dT/dt = k(T + T_m)", "dT/dt = -k * T * T_m", "dT/dt = -k / (T - T_m)"],
    "answer": 0,
    "explanation": "Newton's Law of Cooling states dT/dt = -k(T - T_m) where k > 0, ensuring that an object hotter than ambient (T > T_m) has a negative rate of temperature change (cools down).",
    "citation": "College Board AP® Calculus AB CED — Topic 7.8 Exponential Models with Differential Equations"
  },
  {
    "id": "ap-calc-094",
    "type": "mcq",
    "subtopic": "Washer Method Around Horizontal Line (Unit 8)",
    "difficulty": "Hard",
    "question": "The region bounded by y = x^2 and y = 4 is revolved around the line y = 4. What is the volume of the resulting solid?",
    "options": ["256π / 15", "128π / 15", "64π / 5", "512π / 15"],
    "answer": 0,
    "explanation": "Intersections with y = 4 are x = -2 and x = 2. Revolved around y = 4, disks are formed with radius R(x) = 4 - y = 4 - x^2. Disk formula: V = π ∫[-2 to 2] (4 - x^2)^2 dx = 2π ∫[0 to 2] (16 - 8x^2 + x^4) dx = 2π [16x - 8x^3/3 + x^5/5]_0^2 = 2π [32 - 64/3 + 32/5] = 2π * (128/15) = 256π / 15.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.10 Volume with Disc Method: Revolving Around Other Axes"
  },
  {
    "id": "ap-calc-095",
    "type": "mcq",
    "subtopic": "Interpreting Slope Field Equilibrium Solutions (Unit 7)",
    "difficulty": "Medium",
    "question": "Given the autonomous differential equation dy/dx = (y - 3)(y + 2), what are the equilibrium solutions?",
    "options": ["y = 3 and y = -2", "y = -3 and y = 2", "y = 0 only", "x = 3 and x = -2"],
    "answer": 0,
    "explanation": "Equilibrium solutions occur when dy/dx = 0 for all x (constant horizontal solution curves). Setting (y - 3)(y + 2) = 0 gives y = 3 and y = -2.",
    "citation": "College Board AP® Calculus AB CED — Topic 7.3 Slope Fields and Equilibrium Solutions"
  },
  {
    "id": "ap-calc-096",
    "type": "mcq",
    "subtopic": "Area Enclosed by Three Curves (Unit 8)",
    "difficulty": "Hard",
    "question": "What is the area of the region bounded by y = e^x, y = e^(-x), and the vertical line x = 1?",
    "options": ["e + 1/e - 2", "e - 1/e", "e + 1/e", "2e - 2"],
    "answer": 0,
    "explanation": "The curves intersect at x = 0 (where e^0 = e^-0 = 1). On [0, 1], e^x ≥ e^(-x). Area = ∫[0 to 1] (e^x - e^(-x)) dx = [e^x + e^(-x)]_0^1 = (e^1 + e^-1) - (e^0 + e^0) = e + 1/e - (1 + 1) = e + 1/e - 2.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.4 Area Between Curves"
  },
  {
    "id": "ap-calc-097",
    "type": "mcq",
    "subtopic": "Separation of Variables with Trig (Unit 7)",
    "difficulty": "Hard",
    "question": "Solve the initial value problem dy/dx = cos(x) / (2y) with y(0) = 2 for y > 0.",
    "options": ["y = √(sin(x) + 4)", "y = sin(x) + 2", "y = √(2*sin(x) + 4)", "y = cos(x) + 1"],
    "answer": 0,
    "explanation": "Separate variables: 2y dy = cos(x) dx. Integrate: y^2 = sin(x) + C. Use y(0) = 2: 2^2 = sin(0) + C → 4 = 0 + C → C = 4. Thus y^2 = sin(x) + 4 → y = √(sin(x) + 4).",
    "citation": "College Board AP® Calculus AB CED — Topic 7.7 Particular Solutions to Differential Equations"
  },
  {
    "id": "ap-calc-098",
    "type": "mcq",
    "subtopic": "Volume with Equilateral Triangle Cross-Sections (Unit 8)",
    "difficulty": "Hard",
    "question": "The base of a solid is bounded by y = 2 - x^2 and the line y = 0. Cross-sections perpendicular to the y-axis are equilateral triangles. If side length of an equilateral triangle is s, its area is (√3/4)s^2. What integral gives the volume?",
    "options": [
      "(√3/4) ∫[0 to 2] (2 * √(2 - y))^2 dy",
      "(√3/4) ∫[0 to 2] (2 - y)^2 dy",
      "(√3/2) ∫[0 to √2] (2 - x^2)^2 dx",
      "√3 ∫[0 to 2] (2 - y) dy"
    ],
    "answer": 0,
    "explanation": "Cross-sections are perpendicular to the y-axis, so integrate with respect to y from y = 0 to y = 2. Bounding curve is x^2 = 2 - y → x = ±√(2 - y). Side length s is the horizontal distance between branches: s = 2*√(2 - y). Area A(y) = (√3/4)s^2 = (√3/4)[2*√(2 - y)]^2. Volume = (√3/4) ∫[0 to 2] (2 * √(2 - y))^2 dy.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.8 Volumes with Cross Sections: Triangles"
  },
  {
    "id": "ap-calc-099",
    "type": "mcq",
    "subtopic": "Initial Value Problem with Inverse Tangent (Unit 7)",
    "difficulty": "Hard",
    "question": "Find the solution to dy/dx = (1 + y^2) with y(0) = 1.",
    "options": ["y = tan(x + π/4)", "y = tan(x) + 1", "y = arctan(x + 1)", "y = e^x"],
    "answer": 0,
    "explanation": "Separate variables: [1 / (1 + y^2)] dy = dx. Integrate: arctan(y) = x + C. Use y(0) = 1: arctan(1) = 0 + C → C = π/4. Therefore arctan(y) = x + π/4 → y = tan(x + π/4).",
    "citation": "College Board AP® Calculus AB CED — Topic 7.7 Particular Solutions to Differential Equations"
  },
  {
    "id": "ap-calc-100",
    "type": "mcq",
    "subtopic": "Area Under Curve in Context (Unit 8)",
    "difficulty": "Medium",
    "question": "The power consumption of a research lab, in kilowatts, is modeled by P(t) = 80 + 20 * sin(πt / 12) for 0 ≤ t ≤ 24 hours. What is the total electrical energy consumed by the lab, in kilowatt-hours, over the 24-hour day?",
    "options": ["1,920 kWh", "1,920 + 240/π kWh", "2,400 kWh", "960 kWh"],
    "answer": 0,
    "explanation": "Total energy is E = ∫[0 to 24] P(t) dt = ∫[0 to 24] [80 + 20 * sin(πt / 12)] dt = [80t - 20 * (12/π) * cos(πt / 12)]_0^24 = (80*24 - (240/π)*cos(2π)) - (0 - (240/π)*cos(0)) = 1920 - (240/π)(1) + (240/π)(1) = 1,920 kWh.",
    "citation": "College Board AP® Calculus AB CED — Topic 8.1 Finding the Average Value and Net Accumulation of Change"
  }
]

# Write AP Calc Set 5
with open(os.path.join(US_DATA_AP, "ap_calculus_ab_set5.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ap_calc_set5}, f, indent=2, ensure_ascii=False)
print("Generated ap_calculus_ab_set5.json (20 Qs)!")
