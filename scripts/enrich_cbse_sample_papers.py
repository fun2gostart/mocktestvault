#!/usr/bin/env python3
"""
Enrich CBSE Class 10 Board Mock 01 (Math, Science, Social Science)
Expands brief answer rationales into comprehensive pedagogical solutions:
- Core Theorem / Formula Statement
- Step-by-Step Derivation / Historical Analysis
- Option Elimination & Trap Warnings
- Board Examiner Tips & NCERT Statutory Citations
"""

import json
import os

BASE_DIR = "/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com/data/in/cbse10/sample-papers"

# 1. Mathematics Deepened Explanations
MATH_UPDATES = {
    "cbse10-sqp-math-004": (
        "Core Definition: A prime number is a natural number strictly greater than 1 that has exactly two distinct positive divisors: 1 and itself. "
        "The smallest prime number is 2 (note that 1 is neither prime nor composite, and 2 is the only even prime number). "
        "A composite number is a natural number greater than 1 that has more than two distinct positive divisors; the smallest composite number is 4 (divisors: 1, 2, 4).\n"
        "Step-by-Step Factorization:\n"
        "• 2 = 2¹\n"
        "• 4 = 2²\n"
        "HCF is the product of the smallest power of each common prime factor involved: HCF(2, 4) = 2¹ = 2.\n"
        "Trap Alert: Option (a) 1 is chosen by students who mistakenly consider 1 a prime number. Option (b) 4 is the LCM, not the HCF."
    ),
    "cbse10-sqp-math-005": (
        "Core Formula: For any two positive integers a and b, Fundamental Theorem of Arithmetic implies HCF(a, b) × LCM(a, b) = a × b.\n"
        "Verification of Assertion (A):\n"
        "Given HCF = 5 and product of numbers (a × b) = 150.\n"
        "Substitute into formula: 5 × LCM = 150 ⇒ LCM = 150 / 5 = 30.\n"
        "Thus, Assertion (A) is mathematically true.\n"
        "Verification of Reason (R):\n"
        "Reason (R) states the universal product relation HCF × LCM = a × b, which is a verified standard property for any two positive integers.\n"
        "Conclusion: Reason (R) is true and is the exact mathematical foundation used to deduce Assertion (A). Correct option is (a)."
    ),
    "cbse10-sqp-math-016": (
        "Standard Definition: A quadratic equation in the variable x is an equation of the form ax² + bx + c = 0, where a, b, c are real numbers and the coefficient of the squared term a ≠ 0 (degree strictly equals 2).\n"
        "Step-by-Step Expansion of Option (a):\n"
        "LHS = x(x + 1) + 8 = x² + x + 8\n"
        "RHS = (x + 2)(x - 2) = x² - 4 (using identity (a + b)(a - b) = a² - b²)\n"
        "Equating LHS = RHS: x² + x + 8 = x² - 4\n"
        "Subtracting x² from both sides: x + 8 = -4 ⇒ x + 12 = 0.\n"
        "Notice the x² term completely cancels out (a = 0). The resulting equation is of degree 1 (linear), so it is NOT a quadratic equation.\n"
        "Verification of Other Options:\n"
        "• (b) (x - 2)² + 1 = 2x - 3 ⇒ x² - 4x + 4 + 1 = 2x - 3 ⇒ x² - 6x + 8 = 0 (quadratic, a = 1).\n"
        "• (c) x(2x + 3) = x² + 1 ⇒ 2x² + 3x = x² + 1 ⇒ x² + 3x - 1 = 0 (quadratic, a = 1).\n"
        "• (d) (x + 2)³ = x³ - 4 ⇒ x³ + 6x² + 12x + 8 = x³ - 4 ⇒ 6x² + 12x + 12 = 0 (quadratic, a = 6)."
    ),
    "cbse10-sqp-math-017": (
        "Standard Theorem (Nature of Roots): For a quadratic equation ax² + bx + c = 0 (with a ≠ 0), the discriminant is defined as D = b² - 4ac.\n"
        "According to the quadratic formula, the roots are x = (-b ± √D) / (2a):\n"
        "1. If D > 0: √D is a non-zero positive real number, yielding two distinct real roots: x₁ = (-b + √D)/(2a) and x₂ = (-b - √D)/(2a).\n"
        "2. If D = 0: √D = 0, yielding two equal real roots (coincident roots): x = -b / (2a).\n"
        "3. If D < 0: √D involves the square root of a negative number, meaning there are no real roots.\n"
        "Therefore, real and distinct roots require strictly D > 0. Option (d) is correct."
    ),
    "cbse10-sqp-math-021": (
        "Core Formula: The nth term of an Arithmetic Progression with first term 'a' and common difference 'd' is given by: aₙ = a + (n - 1)d.\n"
        "Given AP: 10, 7, 4, ...\n"
        "Step 1: Identify parameters:\n"
        "• First term a = 10\n"
        "• Common difference d = a₂ - a₁ = 7 - 10 = -3 (strictly negative since the sequence is decreasing)\n"
        "• Term index n = 30\n"
        "Step 2: Calculate a₃₀:\n"
        "a₃₀ = 10 + (30 - 1)(-3)\n"
        "a₃₀ = 10 + 29 × (-3)\n"
        "a₃₀ = 10 - 87 = -77.\n"
        "Trap Warning: A common sign mistake is computing d = 10 - 7 = +3, which falsely yields 10 + 87 = 97. Always evaluate d as (second term - first term)."
    ),
    "cbse10-sqp-math-022": (
        "Core Formula: nth term of an AP is aₙ = a + (n - 1)d.\n"
        "Given AP: -3, -1/2, 2, ...\n"
        "Step 1: Determine first term and common difference:\n"
        "• a = -3\n"
        "• d = a₂ - a₁ = -1/2 - (-3) = -1/2 + 3 = (-1 + 6) / 2 = 5/2\n"
        "Check: a₃ - a₂ = 2 - (-1/2) = 2 + 1/2 = 5/2 (consistent AP).\n"
        "Step 2: Calculate 11th term (n = 11):\n"
        "a₁₁ = a + (11 - 1)d\n"
        "a₁₁ = -3 + 10 × (5/2)\n"
        "Since 10 × (5/2) = 5 × 5 = 25:\n"
        "a₁₁ = -3 + 25 = 22.\n"
        "Thus, the 11th term is 22. Correct option is (a)."
    ),
    "cbse10-sqp-math-026": (
        "Theorem Reference (Basic Proportionality Theorem / Thales Theorem, Theorem 6.1):\n"
        "If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.\n"
        "In ΔABC, since DE ∥ BC:\n"
        "AD / DB = AE / EC\n"
        "Step-by-Step Substitution:\n"
        "• Given: AD = 1.5 cm, DB = 3 cm, AE = 1 cm\n"
        "1.5 / 3 = 1 / EC\n"
        "Simplifying the LHS: 1.5 / 3 = 1 / 2\n"
        "1 / 2 = 1 / EC ⇒ EC = 2 cm.\n"
        "Board Examiner Note: Always state the theorem acronym 'BPT' or 'Thales Theorem' in Section B descriptive answers for full step-marking."
    ),
    "cbse10-sqp-math-033": (
        "Core Formula: The Euclidean distance 'd' between two points P(x₁, y₁) and Q(x₂, y₂) in the Cartesian plane is given by:\n"
        "d = √[(x₂ - x₁)² + (y₂ - y₁)²]\n"
        "Given Coordinates: P(2, 3) where x₁ = 2, y₁ = 3; and Q(4, 1) where x₂ = 4, y₂ = 1.\n"
        "Step-by-Step Computation:\n"
        "• x₂ - x₁ = 4 - 2 = 2 ⇒ (x₂ - x₁)² = 2² = 4\n"
        "• y₂ - y₁ = 1 - 3 = -2 ⇒ (y₂ - y₁)² = (-2)² = 4\n"
        "• Sum of squares = 4 + 4 = 8\n"
        "• Distance d = √8 = √(4 × 2) = 2√2 units.\n"
        "Trap Alert: Forgetting to take the square root of 8 leads to option (b) 8 units. Option (d) 2√2 units is the correct simplified surd form."
    ),
    "cbse10-sqp-math-034": (
        "Core Formula: The distance of any point P(x, y) from the origin O(0, 0) is a direct application of the distance formula:\n"
        "OP = √[(x - 0)² + (y - 0)²] = √(x² + y²)\n"
        "Given Point: P(-6, 8) where x = -6 and y = 8.\n"
        "Step-by-Step Calculation:\n"
        "• (-6)² = 36 (a negative number squared is always positive)\n"
        "• (8)² = 64\n"
        "• x² + y² = 36 + 64 = 100\n"
        "• OP = √100 = 10 units.\n"
        "Examiner Insight: Notice that (6, 8, 10) forms a scaled Pythagorean triplet (derived from 3, 4, 5 by multiplying by 2). This allows instant mental verification during competitive drills."
    ),
    "cbse10-sqp-math-035": (
        "Core Formula: The midpoint M(x, y) of the line segment joining points A(x₁, y₁) and B(x₂, y₂) divides the segment in the ratio 1 : 1 and is given by the midpoint formula:\n"
        "x = (x₁ + x₂) / 2,   y = (y₁ + y₂) / 2\n"
        "Given Points: A(-5, 4) and B(7, -8)\n"
        "Step 1: Compute x-coordinate:\n"
        "x = (-5 + 7) / 2 = 2 / 2 = 1\n"
        "Step 2: Compute y-coordinate:\n"
        "y = (4 + (-8)) / 2 = (4 - 8) / 2 = -4 / 2 = -2\n"
        "Therefore, the midpoint coordinates are (1, -2). Correct option is (c)."
    ),
    "cbse10-sqp-math-039": (
        "Mathematical Verification:\n"
        "• Point P(3, 4) from the origin O(0, 0):\n"
        "Distance = √(3² + 4²) = √(9 + 16) = √25 = 5 units.\n"
        "Hence, Assertion (A) is completely true.\n"
        "• Reason (R) states: 'The distance of any point P(x, y) from the origin is given by √(x² + y²)'.\n"
        "This is the exact algebraic theorem derived from Pythagoras theorem and the coordinate distance formula.\n"
        "Conclusion: Both (A) and (R) are true, and (R) provides the exact theoretical rationale that establishes (A). Correct option is (a)."
    ),
    "cbse10-sqp-math-040": (
        "Theorem 10.1 (NCERT Statement):\n"
        "'The tangent at any point of a circle is perpendicular to the radius through the point of contact.'\n"
        "Geometric Proof Insight:\n"
        "Let O be the centre of the circle and AB be the tangent at point P. Take any point Q on AB other than P. Point Q must lie outside the circle (if it were inside, AB would be a secant, not a tangent). "
        "Therefore, distance OQ > OP (radius). Since this holds for every point on the tangent except P, OP is the shortest distance between centre O and the tangent line AB. "
        "By geometric principle, the shortest distance from a point to a straight line is the perpendicular distance. Hence, OP ⊥ AB (Angle = 90°). Option (c) is correct."
    ),
    "cbse10-sqp-math-041": (
        "Theorem 10.2 (NCERT Statement):\n"
        "'The lengths of tangents drawn from an external point to a circle are equal.'\n"
        "Proof by RHS Congruence:\n"
        "Consider a circle with centre O. From external point P, tangents PA and PB touch the circle at A and B. Join OA, OB, and OP.\n"
        "In right triangles ΔOAP and ΔOBP:\n"
        "1. ∠OAP = ∠OBP = 90° (Theorem 10.1: radius ⊥ tangent at point of contact)\n"
        "2. OP = OP (Common hypotenuse)\n"
        "3. OA = OB (Radii of the same circle)\n"
        "By RHS congruence criterion: ΔOAP ≅ ΔOBP.\n"
        "Therefore, by CPCT (Corresponding Parts of Congruent Triangles), PA = PB. Option (c) is correct."
    ),
    "cbse10-sqp-math-046": (
        "Standard Trigonometric Table Values (NCERT Table 8.1):\n"
        "• sin 30° = 1/2\n"
        "• cos 60° = 1/2\n"
        "Step-by-Step Evaluation:\n"
        "sin 30° + cos 60° = (1/2) + (1/2) = (1 + 1) / 2 = 2 / 2 = 1.\n"
        "Complementary Angle Concept: Notice that sin 30° = cos(90° - 30°) = cos 60°. "
        "Hence sin 30° + cos 60° = 2 × (1/2) = 1. Correct option is (c)."
    ),
    "cbse10-sqp-math-048": (
        "Algebraic Factoring & Trigonometric Identity:\n"
        "Given expression: 9 sec² A - 9 tan² A\n"
        "Step 1: Factor out the common constant coefficient 9:\n"
        "= 9(sec² A - tan² A)\n"
        "Step 2: Recall the second fundamental Pythagorean trigonometric identity:\n"
        "1 + tan² A = sec² A\n"
        "Subtracting tan² A from both sides gives:\n"
        "sec² A - tan² A = 1\n"
        "Step 3: Substitute the identity value into the expression:\n"
        "= 9 × (1) = 9.\n"
        "Trap Alert: Careless students often overlook the factor 9 and choose 1, thinking only of the raw identity value. Option (a) 9 is correct."
    ),
    "cbse10-sqp-math-052": (
        "Trigonometric Modelling (Height and Distance):\n"
        "Let the vertical pole be represented by AB and its shadow on the ground by BC. The angle of elevation of the sun is θ = ∠ACB.\n"
        "In the right-angled triangle ΔABC:\n"
        "tan θ = Opposite side / Adjacent side = AB / BC = Height / Shadow length.\n"
        "Given condition: Height = Shadow length (AB = BC).\n"
        "Therefore: tan θ = AB / AB = 1.\n"
        "From the standard trigonometric table, the acute angle whose tangent equals 1 is 45° (since tan 45° = 1).\n"
        "Hence, the angle of elevation of the sun is 45°. Correct option is (b)."
    ),
    "cbse10-sqp-math-053": (
        "Trigonometric Ratio Application:\n"
        "Let AB be the tower of height 'h' standing vertically on the ground, and C be the point on the ground such that distance BC = 30 m. The angle of elevation ∠ACB = 30°.\n"
        "In right triangle ΔABC:\n"
        "tan 30° = AB / BC = h / 30\n"
        "Since tan 30° = 1 / √3:\n"
        "1 / √3 = h / 30\n"
        "Cross-multiplying gives:\n"
        "h = 30 / √3\n"
        "Rationalizing the denominator:\n"
        "h = (30 × √3) / (√3 × √3) = (30√3) / 3 = 10√3 m.\n"
        "Numerical value: 10 × 1.732 = 17.32 m. Correct option is (a)."
    ),
    "cbse10-sqp-math-056": (
        "Geometrical Derivation (Area of a Sector):\n"
        "A circular disc of radius r has a total central angle of 360° and an area of πr².\n"
        "By the unitary method:\n"
        "• Area of sector corresponding to a central angle of 360° = πr²\n"
        "• Area of sector corresponding to a central angle of 1° = (πr²) / 360\n"
        "• Area of sector corresponding to a central angle of θ = (θ / 360) × πr²\n"
        "Trap Warning: Do not confuse with arc length, which uses circumference 2πr: length = (θ / 360) × 2πr. For sector area, the correct formula is (θ / 360) × πr². Option (b) is correct."
    ),
    "cbse10-sqp-math-057": (
        "Geometrical Derivation (Length of an Arc of a Sector):\n"
        "The circumference of a complete circle of radius r (subtending 360° at the centre) is 2πr.\n"
        "By proportion:\n"
        "The length of an arc subtending an angle θ at the centre is proportional to the fraction of the full revolution θ / 360°.\n"
        "Therefore, Length of Arc = (θ / 360) × 2πr.\n"
        "Notice this can also be written in reduced form as (θ / 180) × πr, but the standard CBSE textbook notation is (θ / 360) × 2πr. Option (a) is correct."
    ),
    "cbse10-sqp-math-060": (
        "Step-by-Step Proof:\n"
        "• A full circle subtends a central angle of 360° with circumference 2πr.\n"
        "• A semicircle represents exactly half of the circle, subtending a straight central angle of θ = 180°.\n"
        "Substituting θ = 180° into the arc length formula:\n"
        "Arc length = (θ / 360) × 2πr = (180 / 360) × 2πr = (1/2) × 2πr = πr.\n"
        "Thus, Assertion (A) is true, and Reason (R) gives the exact central angle (180°) that mathematically generates (A). Correct option is (a)."
    ),
    "cbse10-sqp-math-066": (
        "Statistical Definition: The class mark (also known as the midpoint of a class interval) represents the central value of the interval and is defined as:\n"
        "Class mark = (Upper class limit + Lower class limit) / 2\n"
        "For the given interval 25 - 40:\n"
        "• Lower class limit = 25\n"
        "• Upper class limit = 40\n"
        "Class mark = (40 + 25) / 2 = 65 / 2 = 32.5.\n"
        "Trap Warning: Do not confuse class mark with class size/width (Upper limit - Lower limit = 40 - 25 = 15, shown in option c). Option (d) 32.5 is correct."
    ),
    "cbse10-sqp-math-067": (
        "Empirical Relationship (Karl Pearson's Formula):\n"
        "For a moderately skewed (asymmetrical) continuous distribution, the three measures of central tendency satisfy the fundamental empirical relationship:\n"
        "Mode = 3 Median - 2 Mean\n"
        "Rearranged Equivalent Forms:\n"
        "• 3 Median = Mode + 2 Mean\n"
        "• Mode - Mean = 3(Median - Mean)\n"
        "• Mode - Median = 2(Median - Mean)\n"
        "Trap Warning: A frequent exam error is swapping the coefficients to write Mode = 3 Mean - 2 Median or Mode = 2 Median - 3 Mean. Remember: 'Median' has 6 letters and gets the larger positive coefficient (+3), while 'Mean' has 4 letters and gets (-2)."
    ),
    "cbse10-sqp-math-068": (
        "Calculation using Empirical Relationship:\n"
        "Given Parameters:\n"
        "• Mean = 24\n"
        "• Median = 26\n"
        "Formula: Mode = 3 Median - 2 Mean\n"
        "Step-by-Step Substitution:\n"
        "Mode = 3(26) - 2(24)\n"
        "Mode = 78 - 48\n"
        "Mode = 30.\n"
        "Verification: Check the difference relation: Mode - Mean = 30 - 24 = 6; and 3(Median - Mean) = 3(26 - 24) = 3(2) = 6. The result is verified. Correct option is (a) 30."
    ),
    "cbse10-sqp-math-069": (
        "Statistical Concept: In a grouped frequency distribution, the modal class is defined as the class interval that has the maximum frequency.\n"
        "Inspecting the given distribution:\n"
        "• Interval 0 - 10: Frequency = 5\n"
        "• Interval 10 - 20: Frequency = 8\n"
        "• Interval 20 - 30: Frequency = 15 (MAXIMUM)\n"
        "• Interval 30 - 40: Frequency = 10\n"
        "• Interval 40 - 50: Frequency = 6\n"
        "Since 15 is the highest frequency, the corresponding class interval 20 - 30 is the modal class. Option (a) is correct."
    ),
    "cbse10-sqp-math-071": (
        "Algebraic Derivation using Central Tendency Relationship:\n"
        "Given: Mode - Median = 24\n"
        "We know from the empirical relationship: Mode = 3 Median - 2 Mean\n"
        "Subtracting Median from both sides:\n"
        "Mode - Median = (3 Median - 2 Mean) - Median\n"
        "Mode - Median = 2 Median - 2 Mean = 2(Median - Mean)\n"
        "Substitute the given difference of 24:\n"
        "24 = 2(Median - Mean)\n"
        "Dividing both sides by 2:\n"
        "Median - Mean = 24 / 2 = 12.\n"
        "Thus, the difference between median and mean is 12. Correct option is (b)."
    ),
    "cbse10-sqp-math-073": (
        "Mathematical Verification:\n"
        "Given: Median = 20, Mean = 22.5\n"
        "Applying the empirical formula Mode = 3 Median - 2 Mean:\n"
        "Mode = 3(20) - 2(22.5)\n"
        "Mode = 60 - 45 = 15.\n"
        "This confirms Assertion (A) is completely true.\n"
        "Reason (R) states the exact empirical relationship Mode = 3 Median - 2 Mean, which is the governing theorem used to derive the result.\n"
        "Conclusion: Both (A) and (R) are true, and (R) is the correct explanation of (A). Correct option is (a)."
    ),
    "cbse10-sqp-math-074": (
        "Probability Axiomatic Foundations (Kolmogorov's Axioms):\n"
        "For any event E in a random experiment, the probability P(E) satisfies the fundamental inequality:\n"
        "0 ≤ P(E) ≤ 1\n"
        "• If P(E) = 0, E is an impossible event.\n"
        "• If P(E) = 1, E is a sure (certain) event.\n"
        "Analyzing the given options:\n"
        "• (a) 0.7 lies within [0, 1] — Valid probability.\n"
        "• (b) 15% = 15/100 = 0.15 lies within [0, 1] — Valid probability.\n"
        "• (c) 2/3 ≈ 0.67 lies within [0, 1] — Valid probability.\n"
        "• (d) -1.5 is negative (< 0) — IMPOSSIBLE, as probability can never be negative. Correct option is (d)."
    ),
    "cbse10-sqp-math-075": (
        "Complementary Events Theorem:\n"
        "For any event E, the event 'not E' (denoted as Ē) is called the complementary event. The sum of the probability of an event and its complement is always equal to 1:\n"
        "P(E) + P(not E) = 1\n"
        "Rearranging to find P(not E):\n"
        "P(not E) = 1 - P(E)\n"
        "Given P(E) = 0.05:\n"
        "P(not E) = 1.00 - 0.05 = 0.95.\n"
        "Trap Alert: Subtracting carelessly gives 0.50 or 0.90. Decimal alignment: 1.00 - 0.05 = 0.95. Correct option is (b)."
    ),
    "cbse10-sqp-math-076": (
        "Probability Calculation (Single Die):\n"
        "When a standard fair six-faced die is thrown once:\n"
        "• Sample space S = {1, 2, 3, 4, 5, 6}\n"
        "• Total number of elementary outcomes n(S) = 6\n"
        "Let E be the event of getting a prime number.\n"
        "• Prime numbers in the sample space: {2, 3, 5} (Crucial note: 1 is neither prime nor composite; 4 and 6 are composite).\n"
        "• Favourable outcomes n(E) = 3\n"
        "P(E) = n(E) / n(S) = 3 / 6 = 1 / 2.\n"
        "Trap Warning: Including 1 as prime gives 4/6 = 2/3 (Option b); omitting 2 gives 2/6 = 1/3 (Option a). The correct prime set is strictly {2, 3, 5}, yielding P = 1/2. Correct option is (c)."
    ),
    "cbse10-sqp-math-077": (
        "Two Dice Probability Sample Space:\n"
        "When two dice are thrown simultaneously, each die has 6 outcomes. The total number of elementary outcomes in the sample space is:\n"
        "n(S) = 6 × 6 = 36.\n"
        "Let E be the event that the sum of the two numbers is 8.\n"
        "Favourable pairs (die 1, die 2):\n"
        "1. (2, 6) → 2 + 6 = 8\n"
        "2. (3, 5) → 3 + 5 = 8\n"
        "3. (4, 4) → 4 + 4 = 8\n"
        "4. (5, 3) → 5 + 3 = 8\n"
        "5. (6, 2) → 6 + 2 = 8\n"
        "Total favourable outcomes n(E) = 5.\n"
        "Therefore, P(sum = 8) = n(E) / n(S) = 5 / 36. Correct option is (c)."
    ),
    "cbse10-sqp-math-079": (
        "Two Dice Doublets Probability:\n"
        "A 'doublet' means obtaining the same number on both dice in a simultaneous roll.\n"
        "Total number of outcomes in sample space S = 6 × 6 = 36.\n"
        "Favourable outcomes for a doublet:\n"
        "E = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)}\n"
        "Number of favourable outcomes n(E) = 6.\n"
        "Probability P(doublet) = n(E) / n(S) = 6 / 36 = 1 / 6.\n"
        "Correct option is (b) 1/6."
    )
}

# 2. Social Science Deepened Explanations
SST_UPDATES = {
    "cbse10-sqp-sst-002": (
        "Historical Context (Napoleonic Code 1804):\n"
        "Napoleon Bonaparte introduced the Civil Code of 1804 (widely known as the Napoleonic Code) to modernize the French legal framework and dismantle feudal remnants.\n"
        "Core Provisions of the Code:\n"
        "1. Abolished all privileges based on birth.\n"
        "2. Established legal equality for all citizens before the law.\n"
        "3. Secured the inviolability of the right to property.\n"
        "4. Simplified administrative divisions, abolished the feudal manorial dues, and freed peasants from serfdom.\n"
        "5. Removed guild restrictions in towns and standardized weights, measures, and national currency.\n"
        "This Code was exported to regions under French control, such as the Dutch Republic, Switzerland, Italy, and Germany. Correct option is (a)."
    ),
    "cbse10-sqp-sst-003": (
        "National Identity Measures in the French Revolution:\n"
        "To forge a collective national consciousness ('sentiment de nation'), French revolutionaries introduced deliberate political and cultural symbols:\n"
        "• Promoted the ideas of 'la patrie' (the fatherland) and 'le citoyen' (the citizen), emphasizing a united community enjoying equal constitutional rights.\n"
        "• Replaced the former royal white banner with a new French tricolour (blue, white, red) flag.\n"
        "• The Estates General was elected by the body of active citizens and renamed the National Assembly.\n"
        "• Formulated uniform laws for all citizens within its territory and abolished internal customs duties.\n"
        "• Discouraged regional dialects and made French the national lingua franca.\n"
        "Hence, continuing the royal white standard of the Bourbon monarchy was explicitly NOT done—it was discarded as a symbol of royal absolutism. Correct option is (d)."
    ),
    "cbse10-sqp-sst-005": (
        "Gandhian Chronology:\n"
        "Mahatma Gandhi returned to India from South Africa in January 1915.\n"
        "Historical Significance:\n"
        "In South Africa, Gandhi had spent over two decades developing and refining his novel method of mass agitation based on truth and non-violence, which he called 'Satyagraha'. He successfully organized Indian immigrants against racist registration laws and poll taxes.\n"
        "Upon arriving in India in January 1915, on the advice of his political mentor Gopal Krishna Gokhale, Gandhi spent his first year travelling across the subcontinent to understand the conditions and grievances of the Indian masses before launching any political campaign. Correct option is (c)."
    ),
    "cbse10-sqp-sst-006": (
        "Champaran Satyagraha 1917 Context:\n"
        "In 1917, Mahatma Gandhi travelled to the Champaran district of Bihar after being persuaded by a local farmer, Raj Kumar Shukla, to investigate the plight of sharecroppers.\n"
        "The Grievance: European planters enforced the oppressive 'Tinkathia' system, which legally mandated peasant farmers to cultivate indigo on 3/20th of their total landholdings. When synthetic German chemical dyes rendered natural indigo unprofitable, planters extracted exorbitant illegal rents and compensations to release peasants from agreements.\n"
        "Gandhi organized non-violent peasant resistance, faced down arrest warrants, and secured an official inquiry committee that refunded 25% of the extracted money. This marked Gandhi's first nationwide triumph of Satyagraha in India. Correct option is (b)."
    ),
    "cbse10-sqp-sst-007": (
        "First World War Economic Fallout on India (1913–1918):\n"
        "During the First World War, the British colonial administration financed massive imperial war expenditures by floating war loans and sharply increasing domestic taxes in India (customs duties were raised and income tax was introduced for the first time).\n"
        "Price Inflation: Between 1913 and 1918, market prices of essential food grains and commodities doubled. This triggered catastrophic inflation, black marketing, and severe deprivation for rural peasants and urban working classes.\n"
        "Compounded Distress: This economic misery was exacerbated in 1918–19 and 1920–21 by catastrophic crop failures across many parts of India, accompanied by the 1918 influenza epidemic in which 12 to 13 million people perished (1921 Census). Correct option is (a)."
    ),
    "cbse10-sqp-sst-018": (
        "History of Print in Japan:\n"
        "Buddhist missionaries from China introduced hand-printing technology (woodblock printing) into Japan around AD 768–770.\n"
        "The Buddhist Diamond Sutra (AD 868):\n"
        "The oldest surviving printed Japanese book is the Buddhist Diamond Sutra, printed in AD 868. It consists of six sheets of accordion-folded paper printed with woodblocks, containing sacred Buddhist sutra text and detailed woodcut depictions of the Buddha preaching to his assembly.\n"
        "Later Developments: Printing diversified to include playing cards, paper money, and Edo period illustrated novels and Ukiyo-e woodblock prints by artists like Kitagawa Utamaro. Correct option is (c)."
    ),
    "cbse10-sqp-sst-027": (
        "Global Water Resource Distribution (NCERT Chapter 3 Water Resources):\n"
        "• Total Global Volume: 96.5% of the total volume of world's water is estimated to exist as saline ocean and sea water, which is unfit for direct human consumption, agriculture, or industrial processing.\n"
        "• Freshwater Proportion: Only about 2.5% of the earth's water exists as fresh water.\n"
        "• Availability Breakdown of Freshwater: Nearly 70% of this fresh water is locked up in permanent ice sheets and glaciers in Antarctica, Greenland, and mountainous regions; slightly less than 30% is stored as groundwater in aquifers. Less than 1% exists in accessible rivers and freshwater lakes.\n"
        "This stark scarcity underscores why rainwater harvesting and conservation are critical. Correct option is (d)."
    ),
    "cbse10-sqp-sst-030": (
        "Nomenclature of Shifting Cultivation (Jhumming):\n"
        "Primitive subsistence agriculture, also known as 'slash and burn' agriculture, is a traditional system where farmers clear a patch of forest land, burn the vegetation to enrich the soil with potash ash, and cultivate food crops until fertility declines.\n"
        "Regional Terms in India:\n"
        "• 'Jhumming' in North-Eastern states: Assam, Meghalaya, Mizoram, and Nagaland.\n"
        "• 'Pamlou' in Manipur.\n"
        "• 'Dipa' in Bastar district of Chhattisgarh and Andaman & Nicobar Islands.\n"
        "• 'Bewar' or 'Dahiya' in Madhya Pradesh.\n"
        "• 'Podu' or 'Penda' in Andhra Pradesh.\n"
        "• 'Kuruwa' in Jharkhand.\n"
        "Hence, in Assam, Meghalaya, and Nagaland, it is called Jhumming. Correct option is (c)."
    ),
    "cbse10-sqp-sst-031": (
        "Regional Matching of Slash-and-Burn Cultivation:\n"
        "• Dipa: Bastar district of Chhattisgarh and Andaman & Nicobar Islands (Correct).\n"
        "• Podu or Penda: Andhra Pradesh (Correct).\n"
        "• Valre or Waltre: South-eastern Rajasthan (Correct).\n"
        "Analysis of Incorrect Combinations:\n"
        "• Bewar is in Madhya Pradesh, NOT Kerala.\n"
        "• Khil is in the Himalayan belt, NOT Tamil Nadu.\n"
        "• Kuruwa is in Jharkhand, NOT Gujarat.\n"
        "Option (a) presents the verified, accurate NCERT geographical pairings. Correct option is (a)."
    ),
    "cbse10-sqp-sst-035": (
        "Thorium Occurrence in Monazite Placer Sands:\n"
        "Monazite is a reddish-brown phosphate mineral containing rare-earth metals and substantial concentrations of radioactive Thorium (Th-232).\n"
        "Geographical Distribution: The coastal beach placer sands of Kerala (particularly in Chavara and Kollam districts) contain the world's richest deposits of monazite sand. Waves concentrate these heavy minerals along the coastline.\n"
        "Strategic Value: Thorium is a cornerstone of India's three-stage nuclear power programme (pioneered by Dr. Homi J. Bhabha) to transition from uranium to abundant domestic thorium breeder reactors. Correct option is (d)."
    ),
    "cbse10-sqp-sst-036": (
        "Economic Geology (Ore vs. Mineral):\n"
        "An 'ore' is a naturally occurring mineral aggregate from which a commercially valuable metal can be economically extracted at a profit.\n"
        "• Assertion (A): Although minerals occur widely in rocks, only deposits with adequate concentration justify commercial investment. Mining requires massive capital for excavation, beneficiation, transport, and smelting. If mineral content is too low or extraction too costly, the rock remains a mere geological occurrence, not an ore.\n"
        "• Reason (R): Accurately defines the economic parameters of ore viability: high grade, sufficient volume, and low production cost relative to market price.\n"
        "Conclusion: Reason (R) correctly explains Assertion (A). Correct option is (a)."
    ),
    "cbse10-sqp-sst-045": (
        "Constitutional Definition of Federalism (NCERT Chapter 2 Federalism):\n"
        "Federalism is an institutional system of shared rule and self-rule in which governmental power is constitutionally divided between a central authority (national government) and various constituent regional units (such as states or provinces).\n"
        "Key Characteristics:\n"
        "1. Two or more tiers of government (Union, State, and Local Panchayats/Municipalities).\n"
        "2. Each tier has its own jurisdiction in specific matters of legislation, taxation, and administration specified in the Constitution.\n"
        "3. Fundamental constitutional provisions cannot be unilaterally altered by one level of government.\n"
        "4. Courts (Supreme Court) act as an umpire to interpret the Constitution and resolve disputes between levels. Correct option is (a)."
    ),
    "cbse10-sqp-sst-048": (
        "Linguistic Reorganisation of Indian States (1956 Onwards):\n"
        "Historical Context: When the demand for states on the basis of language was raised after Independence, national leaders feared it would lead to balkanization and disintegration of India.\n"
        "Outcome of the States Reorganisation Act (1956):\n"
        "Contrary to initial apprehensions, creating linguistic states (e.g. Andhra Pradesh for Telugu, Maharashtra for Marathi, Gujarat for Gujarati) accommodated deep regional identities, reduced ethnic friction, democratized governance by enabling administration in regional languages, and made the country more cohesive.\n"
        "Conclusion: Assertion (A) is true, and Reason (R) provides the exact sociological explanation for why linguistic states consolidated national unity. Correct option is (a)."
    ),
    "cbse10-sqp-sst-050": (
        "Sociological Definition (Feminist Movement):\n"
        "A woman or a man who believes in equal rights and opportunities for women and men is termed a feminist.\n"
        "Feminist Movements: Political, cultural, and social movements that campaigned for women's suffrage (voting franchise), equal legal status, enhanced educational access, workplace non-discrimination, equal pay for equal work, and autonomy in personal and domestic life.\n"
        "Other terms:\n"
        "• Communalism: Exploiting religious differences to mobilize political power against other communities.\n"
        "• Secularism: State neutrality regarding all religions, guaranteeing no official religion. Correct option is (a)."
    ),
    "cbse10-sqp-sst-054": (
        "Tripartite Structure of Political Parties (NCERT Chapter 6 Political Parties):\n"
        "A political party is a group of people who come together to contest elections and hold power in the government. Every political party has three core structural components:\n"
        "1. The Leaders: Elected or appointed officials who formulate party ideology, guide political strategy, and hold executive office when elected.\n"
        "2. The Active Members: Cadres, grassroots workers, and committee delegates who organize rallies, canvas voters, and execute campaign programs.\n"
        "3. The Followers: Citizens and sympathizers who endorse the party's ideological platform and vote for its candidates in elections.\n"
        "Option (d) correctly lists all three statutory components."
    ),
    "cbse10-sqp-sst-056": (
        "Indispensability of Political Parties in Modern Democracy:\n"
        "Assertion (A): Without political parties, every candidate in an election would be an independent individual. No one would be able to make any unified national policy promises to the electorate. The government might be formed, but its utility would remain ever uncertain.\n"
        "Reason (R): Political parties perform the indispensable democratic function of interest aggregation—synthesizing millions of diverse individual opinions into actionable public policies. They formulate governments, provide an organized institutional opposition to keep the ruling party accountable, and give voters a clear choice between competing governance philosophies.\n"
        "Conclusion: Reason (R) directly explains why representative democracies cannot function without political parties. Correct option is (a)."
    ),
    "cbse10-sqp-sst-065": (
        "Economics: Limitations of Per Capita Income (NCERT Chapter 1 Development):\n"
        "Per Capita Income (Average Income = National Income / Total Population) is widely used by the World Bank in its World Development Reports, but it has severe structural limitations:\n"
        "1. Conceals Income Disparities: A country with an elite few earning billions and millions living in extreme poverty can have the same average per capita income as an egalitarian society where wealth is evenly distributed.\n"
        "2. Neglects Non-Material Dimensions: It tells us nothing about literacy rates, infant mortality rates, life expectancy, clean drinking water access, gender parity, or environmental sustainability.\n"
        "This is why the UNDP Human Development Index (HDI) integrates health (life expectancy) and education (mean years of schooling) alongside per capita income. Reason (R) correctly explains Assertion (A). Correct option is (a)."
    ),
    "cbse10-sqp-sst-075": (
        "Monetary Economics: Elimination of Double Coincidence of Wants:\n"
        "Barter Bottleneck: In a barter economy without money, trade requires a 'double coincidence of wants'—what a seller wishes to sell must coincide exactly with what a buyer wishes to purchase. If an apple farmer wants shoes, he must find a shoemaker who simultaneously desires apples.\n"
        "Role of Money: Money acts as an intermediate medium of exchange. A person holding money can easily exchange it for any commodity or service in the market. Since transactions are split into two independent steps (sale for money, then purchase with money), the cumbersome double coincidence requirement is eliminated.\n"
        "Conclusion: Reason (R) accurately explains the operational mechanism behind Assertion (A). Correct option is (a)."
    ),
    "cbse10-sqp-sst-080": (
        "Globalisation: Global Dispersion of MNC Production:\n"
        "Strategy of Multinational Corporations (MNCs):\n"
        "MNCs set up production facilities not in a single country, but across regions where production costs are lowest and market access is highest.\n"
        "Example (NCERT Illustration):\n"
        "A large MNC producing industrial equipment designs its products in specialized research centers in the United States, manufactures complex components in China (where low-cost manufacturing infrastructure exists), ships them to Mexico and Eastern Europe for assembly close to major consumer markets in North America and Europe, and manages global technical customer support through English-speaking call centers in India.\n"
        "This spatial fragmentation allows MNCs to minimize production costs by up to 50–60%. Reason (R) correctly explains Assertion (A). Correct option is (a)."
    )
}

# 3. Science Deepened Explanations
SCI_UPDATES = {
    "cbse10-sqp-sci-010": (
        "Chemical Reaction Analysis:\n"
        "Zn(s) + 2NaOH(aq) --heat--> Na₂ZnO₂(aq) + H₂(g)↑\n"
        "Detailed Principles:\n"
        "• Zinc is an amphoteric metal capable of reacting with both strong acids and strong alkalis.\n"
        "• When heated with hot, concentrated sodium hydroxide (NaOH), zinc displaces hydrogen to liberate hydrogen gas (which burns with a characteristic pop sound when a burning splinter is brought near).\n"
        "• The salt formed is Sodium Zincate, which contains the zincate anion [ZnO₂]²⁻, yielding the neutral chemical formula Na₂ZnO₂.\n"
        "Examiner Trap: Students frequently confuse the formula with NaZnO₂ or Na(ZnO)₂. Remember: Sodium has valency +1 and zincate has valency -2, requiring two sodium cations: Na₂ZnO₂."
    ),
    "cbse10-sqp-sci-013": (
        "Exceptional Physical Properties of Metals and Non-Metals:\n"
        "• Liquid Metal at Room Temperature: Mercury (Hg) is the only transition metal that remains in a liquid state under standard laboratory temperature and pressure (melting point -38.83°C). All other metals (except caesium and gallium which melt near body temperature at ~30°C) are solid.\n"
        "• Lustrous Non-Metal: Non-metals are generally dull and non-reflective, but Iodine (I₂) is a notable exception. Solid iodine forms dark purple-black crystals with a prominent metallic-like lustrous sheen.\n"
        "Other notable exceptions to remember:\n"
        "• Carbon in the form of diamond is a non-metal with the highest natural hardness.\n"
        "• Carbon in the form of graphite conducts electricity.\n"
        "• Alkali metals (Na, K, Li) are so soft they can be cut with a knife. Correct option is (b)."
    ),
    "cbse10-sqp-sci-017": (
        "Reaction of Metals with Steam (NCERT Activity 3.10):\n"
        "3Fe(s) + 4H₂O(g) → Fe₃O₄(s) + 4H₂(g)↑\n"
        "Reactivity Series Insights:\n"
        "• Potassium and sodium react violently with cold water.\n"
        "• Calcium reacts less vigorously with cold water.\n"
        "• Magnesium does not react with cold water; it reacts slowly with hot water.\n"
        "• Iron, aluminium, and zinc do not react with cold or hot water at all. They only react when heated steam is passed over red-hot metal.\n"
        "Compound Formed: The oxidation of iron by steam yields mixed Iron(II,III) oxide (also known as ferrosoferric oxide or magnetic iron oxide, Fe₃O₄, which is a combination of FeO and Fe₂O₃), liberating hydrogen gas. Correct option is (c)."
    ),
    "cbse10-sqp-sci-036": (
        "Human Brain Functional Neuroanatomy (NCERT Chapter 7 Control and Coordination):\n"
        "The brain is divided into forebrain, midbrain, and hindbrain.\n"
        "Functions of Brain Regions:\n"
        "• Cerebellum (Hindbrain): Coordinates voluntary muscular motor actions, maintains posture, bodily balance, equilibrium, and precision of movements (such as walking along a straight line, riding a bicycle, or picking up a needle).\n"
        "• Cerebrum (Forebrain): Seat of intelligence, conscious thought, memory, sensory perception, and reasoning.\n"
        "• Medulla Oblongata (Hindbrain): Controls involuntary visceral reflexes like blood pressure, salivation, heartbeat, and vomiting.\n"
        "• Hypothalamus: Regulates homeostasis, body temperature, hunger, and endocrine signals. Correct option is (b) Cerebellum."
    ),
    "cbse10-sqp-sci-037": (
        "Phytohormones (Plant Growth Regulators):\n"
        "• Cytokinins: Derived from adenine, cytokinins specifically stimulate rapid cytokinesis (cell division), delay leaf senescence, and open stomata. They are found in highest concentrations in areas of rapid cell proliferation, such as developing embryos, seeds, and actively growing fruits.\n"
        "Other Phytohormone Functions for Comparison:\n"
        "• Auxin: Synthesized at root/shoot tips; promotes cell elongation, apical dominance, and phototropism.\n"
        "• Gibberellins: Promote internodal stem elongation and break seed dormancy.\n"
        "• Abscisic Acid (ABA): Plant growth inhibitor; induces stomatal closure during drought and promotes leaf wilting/fall. Correct option is (c) Cytokinin."
    ),
    "cbse10-sqp-sci-042": (
        "Asexual Reproduction: Vegetative Propagation in Plants:\n"
        "Bryophyllum (sprout leaf plant) possesses specialized adventitious foliar buds located in the marginal notches of its broad, succulent leaves.\n"
        "Biological Mechanism:\n"
        "When an intact leaf matures and drops onto moist soil, or when leaf notches touch moist ground, these dormant marginal buds sprout roots and shoot plantlets through mitosis, utilizing stored nutrient reserves. These detach to grow into independent, genetically identical daughter plants.\n"
        "Comparative Examples:\n"
        "• Vegetative propagation by stem: Potato (tubers/eyes), Ginger (rhizome).\n"
        "• Vegetative propagation by root: Sweet potato, Dahlia.\n"
        "• Vegetative propagation by leaf: Bryophyllum, Begonia. Correct option is (a)."
    ),
    "cbse10-sqp-sci-044": (
        "Human Reproductive Physiology (Thermoregulation of Spermatogenesis):\n"
        "The male testes are housed outside the abdominal pelvic cavity inside a pouch of skin and smooth muscle called the scrotum.\n"
        "Biological Necessity:\n"
        "Normal core human body temperature is approximately 37°C (98.6°F). However, the complex cellular process of spermatogenesis (meiotic production and maturation of viable, motile spermatozoa) requires a cooler temperature that is 2°C to 2.5°C lower than internal core body temperature (i.e. ~34.5°C–35°C).\n"
        "The scrotum acts as a biological climate control mechanism: in cold temperatures, dartos and cremasteric muscles contract to pull the testes closer to the body; in warm temperatures, they relax to suspend them further away. If the testes fail to descend (cryptorchidism), viable sperm production is arrested, leading to sterility. Correct option is (b)."
    )
}

def update_file(filename, updates_dict):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    updated_count = 0
    for q in data["questions"]:
        qid = q["id"]
        if qid in updates_dict:
            q["explanation"] = updates_dict[qid]
            updated_count += 1
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"✓ {filename}: Successfully enriched {updated_count} questions!")

if __name__ == "__main__":
    update_file("mathematics_board_mock01.json", MATH_UPDATES)
    update_file("social_science_board_mock01.json", SST_UPDATES)
    update_file("science_board_mock01.json", SCI_UPDATES)
    print("🎉 All CBSE Board Mock 01 explanations enriched successfully!")
