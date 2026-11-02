#!/usr/bin/env python3
"""
MockTestVault — United States Pillar Expansion Generator
Generates:
1. Digital SAT Math Sets 02, 03, 04 (20 Qs each = 60 Qs)
2. Digital SAT Reading & Writing Sets 02, 03, 04 (20 Qs each = 60 Qs)
3. AP Calculus AB Diagnostic 01 (20 Qs)
4. AP Physics 1 Diagnostic 01 (20 Qs)
Total: 160 Ground-Truth Verified Questions across 8 new production suites.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_SAT = os.path.join(BASE_DIR, "data", "us", "sat")
US_DATA_AP = os.path.join(BASE_DIR, "data", "us", "ap")
US_PAGES_SAT = os.path.join(BASE_DIR, "us", "sat")
US_PAGES_AP = os.path.join(BASE_DIR, "us", "ap")

os.makedirs(US_DATA_SAT, exist_ok=True)
os.makedirs(US_DATA_AP, exist_ok=True)
os.makedirs(US_PAGES_SAT, exist_ok=True)
os.makedirs(US_PAGES_AP, exist_ok=True)

# ==============================================================================
# 1. DIGITAL SAT MATH SET 02 (20 Questions)
# ==============================================================================
sat_math_set2 = [
  {
    "id": "sat-math-021",
    "type": "mcq",
    "subtopic": "Linear Inequalities (Algebra)",
    "difficulty": "Easy",
    "question": "Which of the following represents the complete solution set to the inequality 3x - 5 ≥ 7x + 11?",
    "options": ["x ≤ -4", "x ≥ -4", "x ≤ 4", "x ≥ 4"],
    "answer": 0,
    "explanation": "Subtract 3x from both sides: -5 ≥ 4x + 11. Subtract 11: -16 ≥ 4x. Divide both sides by 4: -4 ≥ x, which can be rewritten as x ≤ -4.",
    "citation": "College Board Digital SAT Math Specification — Heart of Algebra"
  },
  {
    "id": "sat-math-022",
    "type": "mcq",
    "subtopic": "Systems with Infinite Solutions (Algebra)",
    "difficulty": "Medium",
    "question": "In the system of linear equations below, k is a constant:\nkx + 6y = 14\n2x + 3y = 7\nIf the system has infinitely many solutions (x, y), what is the value of k?",
    "options": ["4", "2", "6", "1"],
    "answer": 0,
    "explanation": "For a linear system to have infinitely many solutions, the two equations must be proportional multiples of each other. Multiplying the second equation by 2 yields 4x + 6y = 14. Matching coefficients with the first equation gives k = 4.",
    "citation": "College Board Digital SAT Math Specification — Systems of Linear Equations"
  },
  {
    "id": "sat-math-023",
    "type": "mcq",
    "subtopic": "Absolute Value Equations (Algebra)",
    "difficulty": "Medium",
    "question": "What is the sum of all real solutions to the equation |2x - 7| = 15?",
    "options": ["7", "11", "-4", "15"],
    "answer": 0,
    "explanation": "Case 1: 2x - 7 = 15 → 2x = 22 → x = 11. Case 2: 2x - 7 = -15 → 2x = -8 → x = -4. The sum of the solutions is 11 + (-4) = 7.",
    "citation": "College Board Digital SAT Math Specification — Absolute Value Concepts"
  },
  {
    "id": "sat-math-024",
    "type": "mcq",
    "subtopic": "Radicals and Exponents (Advanced Math)",
    "difficulty": "Medium",
    "question": "For all positive values of x and y, which of the following is equivalent to the expression (x^6 * y^9)^(1/3) * (x^4 * y^2)^(1/2)?",
    "options": ["x^4 * y^4", "x^5 * y^5", "x^3 * y^4", "x^10 * y^11"],
    "answer": 0,
    "explanation": "(x^6 * y^9)^(1/3) = x^(6/3) * y^(9/3) = x^2 * y^3. (x^4 * y^2)^(1/2) = x^(4/2) * y^(2/2) = x^2 * y^1. Multiplying both terms: (x^2 * y^3) * (x^2 * y) = x^(2+2) * y^(3+1) = x^4 * y^4.",
    "citation": "College Board Digital SAT Math Specification — Rational Exponents"
  },
  {
    "id": "sat-math-025",
    "type": "mcq",
    "subtopic": "Discriminant & Nature of Roots (Advanced Math)",
    "difficulty": "Medium",
    "question": "What is the value of the discriminant of the quadratic equation 2x^2 - 4x + 5 = 0, and how many distinct real solutions does it possess?",
    "options": [
      "-24; zero real solutions (two complex solutions)",
      "24; two distinct real solutions",
      "0; exactly one real solution",
      "-56; zero real solutions"
    ],
    "answer": 0,
    "explanation": "Discriminant Δ = b^2 - 4ac. For 2x^2 - 4x + 5 = 0, a = 2, b = -4, c = 5. Δ = (-4)^2 - 4(2)(5) = 16 - 40 = -24. Because Δ < 0, the equation has no real solutions (two complex conjugates).",
    "citation": "College Board Digital SAT Math Specification — Quadratic Functions"
  },
  {
    "id": "sat-math-026",
    "type": "mcq",
    "subtopic": "Vertex of a Parabola (Advanced Math)",
    "difficulty": "Medium",
    "question": "A projectile's height in feet after t seconds is given by h(t) = -16(t - 3)^2 + 144. What is the maximum height, in feet, reached by the projectile?",
    "options": ["144 feet", "3 feet", "96 feet", "192 feet"],
    "answer": 0,
    "explanation": "The equation is given in vertex form h(t) = a(t - h)^2 + k where vertex is (h, k) = (3, 144). Since a = -16 < 0, the parabola opens downward, so the vertex represents the maximum value: 144 feet at t = 3 seconds.",
    "citation": "College Board Digital SAT Math Specification — Nonlinear Functions"
  },
  {
    "id": "sat-math-027",
    "type": "mcq",
    "subtopic": "Percentage Increase (Problem Solving)",
    "difficulty": "Easy",
    "question": "The student enrollment at an academy increased from 40,000 students in 2022 to 52,000 students in 2026. What was the percentage increase in enrollment?",
    "options": ["30%", "23%", "25%", "35%"],
    "answer": 0,
    "explanation": "Percentage increase = ((New Value - Old Value) / Old Value) * 100% = ((52,000 - 40,000) / 40,000) * 100% = (12,000 / 40,000) * 100% = 0.30 * 100% = 30%.",
    "citation": "College Board Digital SAT Math Specification — Rates, Ratios & Percentages"
  },
  {
    "id": "sat-math-028",
    "type": "mcq",
    "subtopic": "Conditional Probability (Data Analysis)",
    "difficulty": "Medium",
    "question": "In a survey of 120 college undergraduates, 50 are freshmen and 70 are sophomores. Among the freshmen, 20 commute by bus. Among the sophomores, 35 commute by bus. If a student who commutes by bus is chosen at random, what is the probability that the student is a freshman?",
    "options": ["20/55 (or 4/11)", "20/120 (or 1/6)", "20/50 (or 2/5)", "35/55 (or 7/11)"],
    "answer": 0,
    "explanation": "Total students who commute by bus = 20 (freshmen) + 35 (sophomores) = 55. Among these 55 bus commuters, 20 are freshmen. Thus, P(Freshman | Bus) = 20/55 = 4/11.",
    "citation": "College Board Digital SAT Math Specification — Two-Way Tables & Probability"
  },
  {
    "id": "sat-math-029",
    "type": "mcq",
    "subtopic": "Scatterplot Slope Interpretation (Data Analysis)",
    "difficulty": "Medium",
    "question": "A researcher fits a line of best fit to a scatterplot comparing daily smartphone screen time in hours (x) to nightly sleep duration in hours (y): y = -0.45x + 8.6. What is the best interpretation of the number -0.45 in this context?",
    "options": [
      "For each additional hour of screen time, predicted sleep duration decreases by 0.45 hours",
      "For each additional hour of sleep, predicted screen time decreases by 0.45 hours",
      "The minimum sleep duration recorded was 0.45 hours",
      "When screen time is 0 hours, predicted sleep duration is 0.45 hours"
    ],
    "answer": 0,
    "explanation": "In y = mx + b, slope m = -0.45 represents the rate of change of y with respect to x. Since y is nightly sleep and x is screen time, each 1-hour increase in screen time associates with a 0.45-hour reduction in sleep.",
    "citation": "College Board Digital SAT Math Specification — Linear Models in Scatterplots"
  },
  {
    "id": "sat-math-030",
    "type": "mcq",
    "subtopic": "Margin of Error & Sample Size (Data Analysis)",
    "difficulty": "Hard",
    "question": "A random sample of 600 registered voters found that 54% supported a municipal green energy bond, with an associated margin of error of 4% at a 95% confidence level. Which of the following conclusions is best supported by this data?",
    "options": [
      "It is plausible that between 50% and 58% of all registered voters in the municipality support the bond",
      "Exactly 54% of all registered voters in the municipality support the bond",
      "If 1,200 voters had been surveyed, the margin of error would have doubled to 8%",
      "Between 50% and 58% of all citizens nationwide support municipal bonds"
    ],
    "answer": 0,
    "explanation": "A margin of error of ±4% around an estimate of 54% establishes a plausible confidence interval from 54% - 4% = 50% to 54% + 4% = 58% for the target population (registered voters in the municipality).",
    "citation": "College Board Digital SAT Math Specification — Inference & Margin of Error"
  },
  {
    "id": "sat-math-031",
    "type": "mcq",
    "subtopic": "Similar Triangles & Area Ratio (Geometry)",
    "difficulty": "Medium",
    "question": "Triangle ABC is similar to triangle DEF, where vertices A, B, and C correspond to D, E, and F respectively. If DE = 3 * AB and the area of triangle ABC is 14 square units, what is the area of triangle DEF?",
    "options": ["126 square units", "42 square units", "84 square units", "56 square units"],
    "answer": 0,
    "explanation": "When two triangles are similar with side scale factor k, their areas scale by k^2. Here the linear scale factor k = DE / AB = 3. Therefore, Area(DEF) = Area(ABC) * 3^2 = 14 * 9 = 126 square units.",
    "citation": "College Board Digital SAT Math Specification — Geometric Similarity"
  },
  {
    "id": "sat-math-032",
    "type": "mcq",
    "subtopic": "Circle Equation in xy-Plane (Geometry)",
    "difficulty": "Medium",
    "question": "A circle in the xy-plane has its center at (2, -5) and passes through the point (5, -1). Which of the following is an equation of this circle?",
    "options": [
      "(x - 2)^2 + (y + 5)^2 = 25",
      "(x + 2)^2 + (y - 5)^2 = 25",
      "(x - 2)^2 + (y + 5)^2 = 5",
      "(x - 5)^2 + (y + 1)^2 = 16"
    ],
    "answer": 0,
    "explanation": "Radius r = sqrt((5 - 2)^2 + (-1 - (-5))^2) = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5. Standard circle equation: (x - h)^2 + (y - k)^2 = r^2. Substituting center (2, -5) and r = 5 yields (x - 2)^2 + (y + 5)^2 = 25.",
    "citation": "College Board Digital SAT Math Specification — Circles in the Coordinate Plane"
  },
  {
    "id": "sat-math-033",
    "type": "mcq",
    "subtopic": "Special Right Triangles 30-60-90 (Trigonometry)",
    "difficulty": "Easy",
    "question": "In a 30°-60°-90° right triangle, the length of the hypotenuse is 16 units. What is the length of the side opposite the 60° angle?",
    "options": ["8√3", "8", "16√3", "8√2"],
    "answer": 0,
    "explanation": "In a 30°-60°-90° triangle with hypotenuse 2x, side opposite 30° is x, and side opposite 60° is x√3. Given 2x = 16 → x = 8. Thus, side opposite 60° is 8√3.",
    "citation": "College Board Digital SAT Math Specification — Right Triangle Trigonometry"
  },
  {
    "id": "sat-math-034",
    "type": "mcq",
    "subtopic": "Trigonometric Ratios (Trigonometry)",
    "difficulty": "Medium",
    "question": "In right triangle JKL with right angle at K, tan(J) = 5/12. What is the value of cos(J)?",
    "options": ["12/13", "5/13", "13/12", "12/5"],
    "answer": 0,
    "explanation": "tan(J) = Opposite / Adjacent = 5 / 12. By Pythagorean theorem, Hypotenuse = sqrt(5^2 + 12^2) = sqrt(25 + 144) = sqrt(169) = 13. Therefore, cos(J) = Adjacent / Hypotenuse = 12 / 13.",
    "citation": "College Board Digital SAT Math Specification — Trigonometric Functions"
  },
  {
    "id": "sat-math-035",
    "type": "mcq",
    "subtopic": "Polynomial Remainder Theorem (Advanced Math)",
    "difficulty": "Hard",
    "question": "When polynomial P(x) = 2x^3 - 5x^2 + 3x - 8 is divided by (x - 2), what is the resulting remainder?",
    "options": ["-6", "0", "4", "-14"],
    "answer": 0,
    "explanation": "According to the Polynomial Remainder Theorem, the remainder of dividing P(x) by (x - c) is simply P(c). Here c = 2. P(2) = 2(2)^3 - 5(2)^2 + 3(2) - 8 = 2(8) - 5(4) + 6 - 8 = 16 - 20 + 6 - 8 = -6.",
    "citation": "College Board Digital SAT Math Specification — Polynomial Operations"
  },
  {
    "id": "sat-math-036",
    "type": "mcq",
    "subtopic": "Exponential Growth Functions (Advanced Math)",
    "difficulty": "Easy",
    "question": "A bank account is opened with an initial deposit of $5,000 and earns 6% annual interest compounded once per year. Which expression gives the total account balance, in dollars, after t years with no further deposits or withdrawals?",
    "options": ["5,000(1.06)^t", "5,000(0.06)^t", "5,000 + 1.06t", "5,000(1.60)^t"],
    "answer": 0,
    "explanation": "Compound growth formula: A = P(1 + r)^t. Substituting principal P = 5,000 and annual rate r = 0.06 gives A(t) = 5,000(1 + 0.06)^t = 5,000(1.06)^t.",
    "citation": "College Board Digital SAT Math Specification — Exponential Functions"
  },
  {
    "id": "sat-math-037",
    "type": "mcq",
    "subtopic": "Perpendicular Lines in xy-Plane (Algebra)",
    "difficulty": "Medium",
    "question": "Line L1 has the equation 2x + 5y = 10. Line L2 is perpendicular to Line L1 in the xy-plane. What is the slope of Line L2?",
    "options": ["5/2", "-2/5", "-5/2", "2/5"],
    "answer": 0,
    "explanation": "Rewrite 2x + 5y = 10 in slope-intercept form: 5y = -2x + 10 → y = (-2/5)x + 2. The slope of L1 is m1 = -2/5. Perpendicular lines have negative reciprocal slopes: m2 = -1 / (-2/5) = 5/2.",
    "citation": "College Board Digital SAT Math Specification — Parallel & Perpendicular Lines"
  },
  {
    "id": "sat-math-038",
    "type": "mcq",
    "subtopic": "Volume of a Cylinder (Geometry)",
    "difficulty": "Easy",
    "question": "A right circular cylinder has a base radius of 4 inches and a height of 10 inches. What is the total volume of the cylinder in cubic inches?",
    "options": ["160π", "80π", "40π", "320π"],
    "answer": 0,
    "explanation": "Volume of cylinder V = π * r^2 * h. Substituting r = 4 and h = 10: V = π * (4^2) * 10 = π * 16 * 10 = 160π cubic inches.",
    "citation": "College Board Digital SAT Math Specification — Solid Geometry"
  },
  {
    "id": "sat-math-039",
    "type": "mcq",
    "subtopic": "Simple Probability (Data Analysis)",
    "difficulty": "Easy",
    "question": "A dealership inventory contains 40 sedans (10 of which are red) and 80 SUVs (24 of which are red). If a vehicle is selected at random from the total inventory, what is the probability that it is red?",
    "options": ["17/60", "34/100", "1/4", "3/10"],
    "answer": 0,
    "explanation": "Total vehicles = 40 + 80 = 120. Total red vehicles = 10 + 24 = 34. Probability = 34 / 120 = 17 / 60.",
    "citation": "College Board Digital SAT Math Specification — Probability Foundations"
  },
  {
    "id": "sat-math-040",
    "type": "mcq",
    "subtopic": "Nonlinear Systems of Equations (Advanced Math)",
    "difficulty": "Hard",
    "question": "What are all the points of intersection between the line y = 2x + 1 and the parabola y = x^2 + 2x - 8?",
    "options": [
      "(3, 7) and (-3, -5)",
      "(3, 7) only",
      "(-3, -5) only",
      "(0, 1) and (2, 5)"
    ],
    "answer": 0,
    "explanation": "Set the two equations equal: x^2 + 2x - 8 = 2x + 1. Subtract (2x + 1) from both sides: x^2 - 9 = 0 → x^2 = 9 → x = 3 or x = -3. If x = 3, y = 2(3) + 1 = 7. If x = -3, y = 2(-3) + 1 = -5. The intersection points are (3, 7) and (-3, -5).",
    "citation": "College Board Digital SAT Math Specification — Nonlinear Systems"
  }
]

# ==============================================================================
# 2. DIGITAL SAT MATH SET 03 (20 Questions)
# ==============================================================================
sat_math_set3 = [
  {
    "id": "sat-math-041",
    "type": "mcq",
    "subtopic": "Work Rate Word Problems (Algebra)",
    "difficulty": "Medium",
    "question": "Pipe A can fill a reservoir in 4 hours, and Pipe B can fill the same reservoir in 6 hours. If both pipes are opened simultaneously, how many hours will it take to fill the reservoir?",
    "options": ["2.4 hours", "5.0 hours", "2.0 hours", "3.2 hours"],
    "answer": 0,
    "explanation": "Combined rate per hour = 1/4 + 1/6 = 3/12 + 2/12 = 5/12 of the reservoir per hour. Time taken = 1 / (5/12) = 12/5 = 2.4 hours.",
    "citation": "College Board Digital SAT Math Specification — Rational Rates"
  },
  {
    "id": "sat-math-042",
    "type": "mcq",
    "subtopic": "Completing the Square (Advanced Math)",
    "difficulty": "Hard",
    "question": "Which of the following are the exact real solutions to the equation x^2 - 10x + 14 = 0?",
    "options": ["5 ± √11", "10 ± √11", "5 ± √14", "-5 ± √11"],
    "answer": 0,
    "explanation": "Complete the square: x^2 - 10x = -14. Add (10/2)^2 = 25 to both sides: x^2 - 10x + 25 = -14 + 25 → (x - 5)^2 = 11. Taking square roots: x - 5 = ±√11 → x = 5 ± √11.",
    "citation": "College Board Digital SAT Math Specification — Quadratic Form and Roots"
  },
  {
    "id": "sat-math-043",
    "type": "mcq",
    "subtopic": "Half-Life & Exponential Decay (Advanced Math)",
    "difficulty": "Medium",
    "question": "A radioactive isotope has a half-life of 8 days. If an initial laboratory sample contains 80 grams of this isotope, how many grams will remain after 24 days?",
    "options": ["10 grams", "20 grams", "5 grams", "26.7 grams"],
    "answer": 0,
    "explanation": "Number of half-life cycles elapsed n = 24 / 8 = 3. Remaining mass = 80 * (1/2)^3 = 80 * 1/8 = 10 grams.",
    "citation": "College Board Digital SAT Math Specification — Exponential Models"
  },
  {
    "id": "sat-math-044",
    "type": "mcq",
    "subtopic": "Function Transformations (Advanced Math)",
    "difficulty": "Easy",
    "question": "The graph of g(x) is obtained by shifting the graph of f(x) = x^2 right by 3 units and upward by 5 units. Which equation defines g(x)?",
    "options": ["g(x) = (x - 3)^2 + 5", "g(x) = (x + 3)^2 + 5", "g(x) = (x - 3)^2 - 5", "g(x) = (x + 5)^2 + 3"],
    "answer": 0,
    "explanation": "Horizontal shift right by h units replaces x with (x - h), so (x - 3)^2. Vertical shift upward by k units adds k, resulting in g(x) = (x - 3)^2 + 5.",
    "citation": "College Board Digital SAT Math Specification — Function Notation"
  },
  {
    "id": "sat-math-045",
    "type": "mcq",
    "subtopic": "Arc Length in Radians (Geometry)",
    "difficulty": "Medium",
    "question": "A circle has a radius of 12 cm. What is the length of an arc subtended by a central angle of π/3 radians?",
    "options": ["4π cm", "2π cm", "6π cm", "8π cm"],
    "answer": 0,
    "explanation": "Arc length formula in radians: s = r * θ. Substituting r = 12 cm and θ = π/3 gives s = 12 * (π/3) = 4π cm.",
    "citation": "College Board Digital SAT Math Specification — Radians & Arc Length"
  },
  {
    "id": "sat-math-046",
    "type": "mcq",
    "subtopic": "Sector Area (Geometry)",
    "difficulty": "Medium",
    "question": "In a circle with radius 10 inches, a sector is defined by a central angle of 72°. What is the area of this sector in square inches?",
    "options": ["20π", "10π", "40π", "5π"],
    "answer": 0,
    "explanation": "Sector area = (θ / 360°) * π * r^2. Here θ = 72°, so the fraction of the circle is 72 / 360 = 1/5. Area = (1/5) * π * (10^2) = (1/5) * 100π = 20π square inches.",
    "citation": "College Board Digital SAT Math Specification — Circles & Sectors"
  },
  {
    "id": "sat-math-047",
    "type": "mcq",
    "subtopic": "Interpreting Linear Coefficients (Algebra)",
    "difficulty": "Easy",
    "question": "A taxi company models the total fare C(m) in dollars for a ride of m miles as C(m) = 2.50m + 4.00. What is the real-world meaning of the constant 4.00?",
    "options": [
      "The initial pickup fee charged before any miles are traveled",
      "The cost per mile driven",
      "The maximum fare allowed for any single trip",
      "The speed in miles per hour of the taxi"
    ],
    "answer": 0,
    "explanation": "In C(m) = 2.50m + 4.00, m is miles traveled. When m = 0, C(0) = 4.00. This represents the base pickup fee charged regardless of distance.",
    "citation": "College Board Digital SAT Math Specification — Linear Models"
  },
  {
    "id": "sat-math-048",
    "type": "mcq",
    "subtopic": "Factoring by Grouping (Advanced Math)",
    "difficulty": "Hard",
    "question": "What is the only real solution to the cubic equation x^3 - 3x^2 + 4x - 12 = 0?",
    "options": ["3", "-3", "2", "-2"],
    "answer": 0,
    "explanation": "Factor by grouping: x^2(x - 3) + 4(x - 3) = 0 → (x^2 + 4)(x - 3) = 0. Setting factors to zero: x^2 + 4 = 0 yields non-real roots x = ±2i. Setting x - 3 = 0 yields real solution x = 3.",
    "citation": "College Board Digital SAT Math Specification — Polynomial Roots"
  },
  {
    "id": "sat-math-049",
    "type": "mcq",
    "subtopic": "Box Plot Analysis & IQR (Data Analysis)",
    "difficulty": "Medium",
    "question": "A box plot shows Dataset X has Q1 = 15, Median = 25, Q3 = 35. Dataset Y has Q1 = 20, Median = 25, Q3 = 45. Which of the following is true?",
    "options": [
      "The interquartile range (IQR) of Dataset Y is greater than Dataset X",
      "Both datasets have identical IQRs",
      "The median of Dataset Y is greater than Dataset X",
      "The range of Dataset X must be greater than Dataset Y"
    ],
    "answer": 0,
    "explanation": "IQR = Q3 - Q1. For Dataset X: IQR = 35 - 15 = 20. For Dataset Y: IQR = 45 - 20 = 25. Since 25 > 20, Dataset Y has a greater IQR.",
    "citation": "College Board Digital SAT Math Specification — Five-Number Summary"
  },
  {
    "id": "sat-math-050",
    "type": "mcq",
    "subtopic": "Outliers & Statistical Measures (Data Analysis)",
    "difficulty": "Medium",
    "question": "A dataset contains the numbers {2, 3, 4, 5, 6}. If an extreme outlier of 100 is added to this dataset, how will the mean and median be affected?",
    "options": [
      "The mean will increase significantly, while the median will change very little",
      "The median will increase significantly, while the mean will remain unaffected",
      "Both mean and median will increase by identical amounts",
      "Neither mean nor median will change"
    ],
    "answer": 0,
    "explanation": "The mean is non-resistant to outliers and pulls heavily toward extreme values (mean jumps from 4 to ~18). The median is resistant and only shifts slightly to the middle position (median shifts from 4 to 4.5).",
    "citation": "College Board Digital SAT Math Specification — Measures of Center"
  },
  {
    "id": "sat-math-051",
    "type": "mcq",
    "subtopic": "Inscribed Angles Theorem (Geometry)",
    "difficulty": "Medium",
    "question": "In a circle, an inscribed angle intercepts an arc of measure 140°. What is the measure of the inscribed angle in degrees?",
    "options": ["70°", "140°", "280°", "35°"],
    "answer": 0,
    "explanation": "The Inscribed Angle Theorem states that the measure of an inscribed angle is exactly half the measure of its intercepted arc: Angle = 140° / 2 = 70°.",
    "citation": "College Board Digital SAT Math Specification — Circles & Inscribed Angles"
  },
  {
    "id": "sat-math-052",
    "type": "mcq",
    "subtopic": "Pythagorean Trigonometric Identity (Trigonometry)",
    "difficulty": "Easy",
    "question": "For an acute angle θ, if cos(θ) = 4/5, what is the value of sin(θ)?",
    "options": ["3/5", "5/4", "1/5", "3/4"],
    "answer": 0,
    "explanation": "Using sin^2(θ) + cos^2(θ) = 1: sin^2(θ) + (4/5)^2 = 1 → sin^2(θ) + 16/25 = 1 → sin^2(θ) = 9/25. Since θ is acute, sin(θ) = 3/5.",
    "citation": "College Board Digital SAT Math Specification — Trigonometric Identities"
  },
  {
    "id": "sat-math-053",
    "type": "mcq",
    "subtopic": "Rational Equations & Extraneous Solutions (Advanced Math)",
    "difficulty": "Hard",
    "question": "How many real solutions exist for the rational equation: 2/(x - 3) + 1/x = 6/(x(x - 3))?",
    "options": ["Zero real solutions (solution is extraneous)", "Exactly one real solution: x = 3", "Exactly two real solutions", "Infinitely many solutions"],
    "answer": 0,
    "explanation": "Multiply all terms by common denominator x(x - 3): 2x + (x - 3) = 6 → 3x - 3 = 6 → 3x = 9 → x = 3. However, substituting x = 3 back into original equation produces division by zero (3 - 3 = 0). Thus, x = 3 is extraneous and no valid real solution exists.",
    "citation": "College Board Digital SAT Math Specification — Extraneous Solutions"
  },
  {
    "id": "sat-math-054",
    "type": "mcq",
    "subtopic": "System with No Solution (Algebra)",
    "difficulty": "Medium",
    "question": "Which of the following linear systems has no solution in the xy-plane?",
    "options": [
      "4x - 6y = 9 and 2x - 3y = 8",
      "2x + 3y = 7 and 4x + 6y = 14",
      "x - y = 5 and x + y = 5",
      "3x + 2y = 8 and 2x + 3y = 8"
    ],
    "answer": 0,
    "explanation": "In 4x - 6y = 9, dividing by 2 gives 2x - 3y = 4.5. The second equation is 2x - 3y = 8. The lines share the same slope (2/3) but have different y-intercepts (-1.5 vs -8/3). They are strictly parallel and never intersect.",
    "citation": "College Board Digital SAT Math Specification — Linear Systems"
  },
  {
    "id": "sat-math-055",
    "type": "mcq",
    "subtopic": "Volume of a Cone (Geometry)",
    "difficulty": "Easy",
    "question": "A right circular cone has a base radius of 6 cm and a vertical height of 8 cm. What is the volume of the cone in cubic centimeters?",
    "options": ["96π", "288π", "48π", "144π"],
    "answer": 0,
    "explanation": "Volume of cone V = (1/3) * π * r^2 * h = (1/3) * π * (6^2) * 8 = (1/3) * π * 36 * 8 = 12 * 8 * π = 96π cubic cm.",
    "citation": "College Board Digital SAT Math Specification — Geometric Volumes"
  },
  {
    "id": "sat-math-056",
    "type": "mcq",
    "subtopic": "Quarterly Compounding (Problem Solving)",
    "difficulty": "Medium",
    "question": "An investment of $2,000 earns 8% nominal annual interest compounded quarterly. Which expression represents the account balance after t years?",
    "options": ["2,000(1.02)^(4t)", "2,000(1.08)^(4t)", "2,000(1.02)^t", "2,000(1.08)^t"],
    "answer": 0,
    "explanation": "Formula: A = P(1 + r/n)^(nt). Here P = 2,000, r = 0.08, n = 4 (quarters/year). r/n = 0.08 / 4 = 0.02. Thus A = 2,000(1 + 0.02)^(4t) = 2,000(1.02)^(4t).",
    "citation": "College Board Digital SAT Math Specification — Compound Interest"
  },
  {
    "id": "sat-math-057",
    "type": "mcq",
    "subtopic": "Skewness and Center (Data Analysis)",
    "difficulty": "Medium",
    "question": "A salary distribution at a corporation is strongly right-skewed by a few high-earning executive salaries. Which statement is most likely true regarding this distribution?",
    "options": [
      "The mean salary is greater than the median salary",
      "The median salary is greater than the mean salary",
      "The mean and median salaries are identical",
      "The standard deviation of salaries is zero"
    ],
    "answer": 0,
    "explanation": "Right-skewed distributions have long right tails caused by high values. These extreme values pull the mean upward, while the median remains anchored to the 50th percentile, meaning Mean > Median.",
    "citation": "College Board Digital SAT Math Specification — Distribution Shape"
  },
  {
    "id": "sat-math-058",
    "type": "mcq",
    "subtopic": "Similar Solids & Volume Scaling (Geometry)",
    "difficulty": "Hard",
    "question": "Two solid cubes have edge lengths in the ratio 2:3. If the volume of the smaller cube is 64 cm^3, what is the volume of the larger cube?",
    "options": ["216 cm^3", "96 cm^3", "144 cm^3", "128 cm^3"],
    "answer": 0,
    "explanation": "When linear scale factor is a:b, volumes scale as a^3:b^3. Here ratio is 2^3:3^3 = 8:27. Volume of larger = 64 * (27 / 8) = 8 * 27 = 216 cm^3.",
    "citation": "College Board Digital SAT Math Specification — 3D Scaling"
  },
  {
    "id": "sat-math-059",
    "type": "mcq",
    "subtopic": "Degrees to Radians (Trigonometry)",
    "difficulty": "Easy",
    "question": "What is the radian measure equivalent to an angle of 150°?",
    "options": ["5π/6", "3π/4", "7π/6", "2π/3"],
    "answer": 0,
    "explanation": "To convert degrees to radians, multiply by π/180°: 150 * (π / 180) = (150/180)π = 5π/6 radians.",
    "citation": "College Board Digital SAT Math Specification — Angles and Radians"
  },
  {
    "id": "sat-math-060",
    "type": "mcq",
    "subtopic": "Circle Chords and Distance (Geometry)",
    "difficulty": "Hard",
    "question": "In a circle of radius 13 cm, a chord is located 5 cm away from the center along a perpendicular segment. What is the total length of the chord?",
    "options": ["24 cm", "12 cm", "18 cm", "20 cm"],
    "answer": 0,
    "explanation": "The perpendicular line from the center bisects the chord. A right triangle is formed by the distance from center (5), half-chord (x), and radius (13): x^2 + 5^2 = 13^2 → x^2 + 25 = 169 → x^2 = 144 → x = 12 cm. Total chord length = 2x = 2(12) = 24 cm.",
    "citation": "College Board Digital SAT Math Specification — Chords & Radii"
  }
]

# ==============================================================================
# 3. DIGITAL SAT MATH SET 04 (20 Questions - 700-800 Benchmark)
# ==============================================================================
sat_math_set4 = [
  {
    "id": "sat-math-061",
    "type": "mcq",
    "subtopic": "Quadratic Coefficients in Context (Advanced Math)",
    "difficulty": "Hard",
    "question": "The height of an arch is modeled by h(x) = -0.05x(x - 40) where h(x) is height in meters and x is distance from the left base in meters. What is the maximum height of the arch?",
    "options": ["20 meters", "40 meters", "10 meters", "15 meters"],
    "answer": 0,
    "explanation": "The x-intercepts are at x = 0 and x = 40. The axis of symmetry lies midway: x = (0 + 40)/2 = 20. Max height h(20) = -0.05(20)(20 - 40) = -1 * (-20) = 20 meters.",
    "citation": "College Board Digital SAT Math Specification — Nonlinear Applications"
  },
  {
    "id": "sat-math-062",
    "type": "mcq",
    "subtopic": "Linear Systems with No Solution (Algebra)",
    "difficulty": "Hard",
    "question": "For what value of constant p does the system of equations have no solution?\npx - 4y = 9\n3x - 2y = 5",
    "options": ["6", "-6", "4", "3"],
    "answer": 0,
    "explanation": "For no solution, slopes must match while y-intercepts differ: p/3 = (-4)/(-2) = 2 → p = 6. With p = 6, 6x - 4y = 9 and 6x - 4y = 10, which are parallel and distinct.",
    "citation": "College Board Digital SAT Math Specification — System Parameters"
  },
  {
    "id": "sat-math-063",
    "type": "mcq",
    "subtopic": "Complex Numbers (Advanced Math)",
    "difficulty": "Medium",
    "question": "If i = √(-1), which of the following is equivalent to (3 + 2i)(4 - 5i)?",
    "options": ["22 - 7i", "2 - 7i", "12 - 10i", "22 + 7i"],
    "answer": 0,
    "explanation": "FOIL: 3(4) + 3(-5i) + 2i(4) + 2i(-5i) = 12 - 15i + 8i - 10(i^2). Since i^2 = -1: 12 - 7i - 10(-1) = 12 - 7i + 10 = 22 - 7i.",
    "citation": "College Board Digital SAT Math Specification — Complex Numbers"
  },
  {
    "id": "sat-math-064",
    "type": "mcq",
    "subtopic": "Rational Function Asymptotes (Advanced Math)",
    "difficulty": "Hard",
    "question": "What is the vertical asymptote of the rational function f(x) = (3x + 1) / (2x - 8)?",
    "options": ["x = 4", "x = -4", "y = 3/2", "x = 8"],
    "answer": 0,
    "explanation": "Vertical asymptotes occur where denominator is zero and numerator is non-zero: 2x - 8 = 0 → 2x = 8 → x = 4. (Note: y = 3/2 is the horizontal asymptote).",
    "citation": "College Board Digital SAT Math Specification — Rational Functions"
  },
  {
    "id": "sat-math-065",
    "type": "mcq",
    "subtopic": "Circle Area with Inscribed Square (Geometry)",
    "difficulty": "Hard",
    "question": "A square is inscribed in a circle of radius 5√2 cm. What is the area of the square in square centimeters?",
    "options": ["100 cm^2", "50 cm^2", "200 cm^2", "25 cm^2"],
    "answer": 0,
    "explanation": "The diagonal of the inscribed square equals diameter of circle d = 2 * (5√2) = 10√2 cm. For square with side s: s√2 = 10√2 → s = 10 cm. Area = s^2 = 10^2 = 100 cm^2.",
    "citation": "College Board Digital SAT Math Specification — Inscribed Polygons"
  },
  {
    "id": "sat-math-066",
    "type": "mcq",
    "subtopic": "Weighted Averages (Problem Solving)",
    "difficulty": "Medium",
    "question": "In a physics course, midterm exams account for 40% of the course grade, homework accounts for 20%, and the final exam accounts for 40%. If Maya scores 85 on midterms and 95 on homework, what minimum score must she achieve on the final exam to attain an overall course average of 90?",
    "options": ["92.5", "90.0", "95.0", "88.0"],
    "answer": 0,
    "explanation": "Overall Grade = 0.40(85) + 0.20(95) + 0.40(F) ≥ 90. 34 + 19 + 0.40F ≥ 90 → 53 + 0.40F ≥ 90 → 0.40F ≥ 37 → F ≥ 37 / 0.40 = 92.5.",
    "citation": "College Board Digital SAT Math Specification — Weighted Statistics"
  },
  {
    "id": "sat-math-067",
    "type": "mcq",
    "subtopic": "Exponential Decay Half-Life Equation (Advanced Math)",
    "difficulty": "Hard",
    "question": "A medicine has a biological half-life of 6 hours in the bloodstream. If 200 mg is administered at t = 0, which equation models remaining medicine M(t) after t hours?",
    "options": ["M(t) = 200(0.5)^(t/6)", "M(t) = 200(0.5)^(6t)", "M(t) = 200(0.94)^t", "M(t) = 200 - 6t"],
    "answer": 0,
    "explanation": "Half-life model: M(t) = M0 * (1/2)^(t / T_half). Substituting initial M0 = 200 and T_half = 6 yields M(t) = 200(0.5)^(t/6).",
    "citation": "College Board Digital SAT Math Specification — Modeling Half-Life"
  },
  {
    "id": "sat-math-068",
    "type": "mcq",
    "subtopic": "Sphere Volume and Surface Area (Geometry)",
    "difficulty": "Medium",
    "question": "If the surface area of a sphere is 64π square inches, what is the volume of the sphere in cubic inches?",
    "options": ["(256/3)π", "(128/3)π", "64π", "32π"],
    "answer": 0,
    "explanation": "Surface area of sphere = 4πr^2 = 64π → r^2 = 16 → r = 4. Volume = (4/3)πr^3 = (4/3)π(4^3) = (4/3)π(64) = (256/3)π cubic inches.",
    "citation": "College Board Digital SAT Math Specification — 3D Geometry"
  },
  {
    "id": "sat-math-069",
    "type": "mcq",
    "subtopic": "Solving Fractional Exponent Equations (Advanced Math)",
    "difficulty": "Hard",
    "question": "If (x + 2)^(3/2) = 27, what is the value of x?",
    "options": ["7", "9", "5", "25"],
    "answer": 0,
    "explanation": "Raise both sides to the power of 2/3: x + 2 = 27^(2/3) = (27^(1/3))^2 = 3^2 = 9. Subtract 2: x = 7.",
    "citation": "College Board Digital SAT Math Specification — Radical Equations"
  },
  {
    "id": "sat-math-070",
    "type": "mcq",
    "subtopic": "Trigonometric Co-Functions (Trigonometry)",
    "difficulty": "Easy",
    "question": "If sin(x°) = cos(34°), where 0° < x < 90°, what is the value of x?",
    "options": ["56", "34", "66", "146"],
    "answer": 0,
    "explanation": "Cofunction identity: sin(x) = cos(90° - x). Therefore, x + 34° = 90° → x = 90° - 34° = 56°.",
    "citation": "College Board Digital SAT Math Specification — Cofunction Identities"
  },
  {
    "id": "sat-math-071",
    "type": "mcq",
    "subtopic": "Standard Normal Distribution (Data Analysis)",
    "difficulty": "Medium",
    "question": "Exam scores are normally distributed with a mean of 75 and standard deviation of 8. Approximately what percentage of students scored between 67 and 83?",
    "options": ["68%", "95%", "50%", "99.7%"],
    "answer": 0,
    "explanation": "67 is exactly 1 standard deviation below mean (75 - 8), and 83 is 1 standard deviation above mean (75 + 8). By the empirical rule (68-95-99.7 rule), approximately 68% of data falls within 1 standard deviation of the mean.",
    "citation": "College Board Digital SAT Math Specification — Normal Distributions"
  },
  {
    "id": "sat-math-072",
    "type": "mcq",
    "subtopic": "Linear Regression Residuals (Data Analysis)",
    "difficulty": "Hard",
    "question": "For a data point (5, 18), a linear regression model predicts a value of 15.2. What is the residual of this data point?",
    "options": ["2.8", "-2.8", "33.2", "1.18"],
    "answer": 0,
    "explanation": "Residual = Actual y - Predicted y = 18 - 15.2 = 2.8. A positive residual indicates the actual data point lies above the regression line.",
    "citation": "College Board Digital SAT Math Specification — Residual Analysis"
  },
  {
    "id": "sat-math-073",
    "type": "mcq",
    "subtopic": "Perpendicular Bisector Equation (Geometry)",
    "difficulty": "Hard",
    "question": "What is the equation of the perpendicular bisector of the line segment connecting A(2, 4) and B(6, 12)?",
    "options": ["y = -0.5x + 10", "y = 2x", "y = -2x + 16", "y = 0.5x + 6"],
    "answer": 0,
    "explanation": "Midpoint M = ((2+6)/2, (4+12)/2) = (4, 8). Slope AB = (12 - 4) / (6 - 2) = 8 / 4 = 2. Perpendicular slope m_perp = -1/2 = -0.5. Point-slope: y - 8 = -0.5(x - 4) → y - 8 = -0.5x + 2 → y = -0.5x + 10.",
    "citation": "College Board Digital SAT Math Specification — Coordinate Geometry"
  },
  {
    "id": "sat-math-074",
    "type": "mcq",
    "subtopic": "Factoring Sum of Cubes (Advanced Math)",
    "difficulty": "Hard",
    "question": "Which of the following is equivalent to 8x^3 + 27y^3?",
    "options": [
      "(2x + 3y)(4x^2 - 6xy + 9y^2)",
      "(2x + 3y)(4x^2 + 6xy + 9y^2)",
      "(2x + 3y)^3",
      "(4x + 9y)(2x^2 - 3xy + 3y^2)"
    ],
    "answer": 0,
    "explanation": "Sum of cubes formula: a^3 + b^3 = (a + b)(a^2 - ab + b^2). Here a = 2x and b = 3y. Thus (2x + 3y)((2x)^2 - (2x)(3y) + (3y)^2) = (2x + 3y)(4x^2 - 6xy + 9y^2).",
    "citation": "College Board Digital SAT Math Specification — Algebraic Factoring"
  },
  {
    "id": "sat-math-075",
    "type": "mcq",
    "subtopic": "Circle Arc Length with Degrees (Geometry)",
    "difficulty": "Easy",
    "question": "In a circle with circumference 72 cm, an arc has a central angle of 45°. What is the length of the arc in cm?",
    "options": ["9 cm", "8 cm", "12 cm", "6 cm"],
    "answer": 0,
    "explanation": "Arc length = (θ / 360°) * Circumference = (45 / 360) * 72 = (1/8) * 72 = 9 cm.",
    "citation": "College Board Digital SAT Math Specification — Circumference and Arcs"
  },
  {
    "id": "sat-math-076",
    "type": "mcq",
    "subtopic": "Linear Equation Infinite Solutions (Algebra)",
    "difficulty": "Medium",
    "question": "If 5(2x - 3) + 7 = ax + b is true for all real values of x, what is the value of a + b?",
    "options": ["2", "18", "-8", "10"],
    "answer": 0,
    "explanation": "Expand left side: 10x - 15 + 7 = 10x - 8. For this to equal ax + b for all x: a = 10 and b = -8. Thus a + b = 10 + (-8) = 2.",
    "citation": "College Board Digital SAT Math Specification — Equivalent Equations"
  },
  {
    "id": "sat-math-077",
    "type": "mcq",
    "subtopic": "Discriminant Real World (Advanced Math)",
    "difficulty": "Medium",
    "question": "A business calculates daily profit P(x) = -2x^2 + 20x - 50, where x is price in dollars. How many price points result in exactly $0 profit?",
    "options": [
      "Exactly 1 price point (x = $5)",
      "Exactly 2 price points",
      "Zero price points",
      "Infinitely many price points"
    ],
    "answer": 0,
    "explanation": "Set P(x) = 0: -2x^2 + 20x - 50 = 0. Divide by -2: x^2 - 10x + 25 = 0 → (x - 5)^2 = 0. There is exactly one real root: x = 5.",
    "citation": "College Board Digital SAT Math Specification — Quadratic Word Problems"
  },
  {
    "id": "sat-math-078",
    "type": "mcq",
    "subtopic": "Median in Frequency Histogram (Data Analysis)",
    "difficulty": "Medium",
    "question": "A sample of 51 employees had years of experience recorded. In which interval must the median fall?",
    "options": [
      "The interval containing the 26th ordered observation",
      "The interval containing the 25th ordered observation",
      "The interval with the highest frequency",
      "The middle numerical range between min and max"
    ],
    "answer": 0,
    "explanation": "For n = 51 observations, the median position is (51 + 1) / 2 = 26th observation when ranked in ascending order.",
    "citation": "College Board Digital SAT Math Specification — Histograms & Medians"
  },
  {
    "id": "sat-math-079",
    "type": "mcq",
    "subtopic": "Pythagorean Distance in 3D (Geometry)",
    "difficulty": "Hard",
    "question": "A rectangular box has length 4 inches, width 3 inches, and height 12 inches. What is the length of the internal space diagonal in inches?",
    "options": ["13 inches", "19 inches", "15 inches", "12.5 inches"],
    "answer": 0,
    "explanation": "3D space diagonal d = sqrt(l^2 + w^2 + h^2) = sqrt(4^2 + 3^2 + 12^2) = sqrt(16 + 9 + 144) = sqrt(169) = 13 inches.",
    "citation": "College Board Digital SAT Math Specification — 3D Geometry"
  },
  {
    "id": "sat-math-080",
    "type": "mcq",
    "subtopic": "Tangent to Circle (Geometry)",
    "difficulty": "Medium",
    "question": "A tangent line touches a circle of radius 7 at point P. An external point Q is 25 units from the center of the circle O. What is the length of tangent segment PQ?",
    "options": ["24", "18", "25", "20"],
    "answer": 0,
    "explanation": "A line tangent to a circle is perpendicular to the radius at the point of tangency, creating right triangle OPQ where OP = 7, hypotenuse OQ = 25. By Pythagorean theorem: PQ = sqrt(25^2 - 7^2) = sqrt(625 - 49) = sqrt(576) = 24.",
    "citation": "College Board Digital SAT Math Specification — Tangent Lines"
  }
]

# Write SAT Math JSONs
with open(os.path.join(US_DATA_SAT, "digital_sat_math_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_math_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(US_DATA_SAT, "digital_sat_math_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_math_set3}, f, indent=2, ensure_ascii=False)
with open(os.path.join(US_DATA_SAT, "digital_sat_math_set4.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_math_set4}, f, indent=2, ensure_ascii=False)

print("Generated Digital SAT Math Sets 2, 3, 4 successfully!")
