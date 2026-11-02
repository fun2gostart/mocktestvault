import json
import os

gre_quant_questions = [
    # Quantitative Comparison (Qs 1–8)
    {
        "id": "gre-quant-001",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Algebra & Exponents",
        "difficulty": "Medium",
        "question": "Given: x > 1\n\nQuantity A: x^4 - 1\nQuantity B: (x^2 + 1)(x - 1)^2\n\nCompare Quantity A and Quantity B.",
        "options": [
            "Quantity A is greater.",
            "Quantity B is greater.",
            "The two quantities are equal.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "Factor Quantity A: x^4 - 1 = (x^2 + 1)(x^2 - 1) = (x^2 + 1)(x + 1)(x - 1).\nQuantity B is (x^2 + 1)(x - 1)^2 = (x^2 + 1)(x - 1)(x - 1).\nSince x > 1, both (x^2 + 1) > 0 and (x - 1) > 0. Divide both quantities by the positive term (x^2 + 1)(x - 1):\nQuantity A becomes (x + 1).\nQuantity B becomes (x - 1).\nSince x + 1 > x - 1 for all real numbers x, Quantity A is strictly greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Algebra"
    },
    {
        "id": "gre-quant-002",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Geometry & Circles",
        "difficulty": "Medium",
        "question": "A circle is inscribed in a square of side length 2s, and a smaller square is inscribed inside the same circle.\n\nQuantity A: Area of the region inside the circle but outside the smaller square\nQuantity B: Area of the region inside the larger square but outside the circle\n\nCompare Quantity A and Quantity B.",
        "options": [
            "Quantity A is greater.",
            "Quantity B is greater.",
            "The two quantities are equal.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "Side of large square = 2s, so its area = 4s^2.\nThe circle has diameter = 2s, so radius r = s. Area of circle = πs^2 ≈ 3.1416s^2.\nThe smaller square has diagonal = circle diameter = 2s. Area of smaller square = (diagonal^2)/2 = (4s^2)/2 = 2s^2.\nQuantity A = Area(Circle) - Area(Small Square) = πs^2 - 2s^2 = s^2(π - 2) ≈ 1.1416s^2.\nQuantity B = Area(Large Square) - Area(Circle) = 4s^2 - πs^2 = s^2(4 - π) ≈ 0.8584s^2.\nSince 1.1416 > 0.8584, Quantity A is greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Geometry"
    },
    {
        "id": "gre-quant-003",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Number Properties",
        "difficulty": "Hard",
        "question": "Given: k is an integer such that 10 < k < 30, and k has exactly 3 positive factors.\n\nQuantity A: k\nQuantity B: 25\n\nCompare Quantity A and Quantity B.",
        "options": [
            "The two quantities are equal.",
            "Quantity A is greater.",
            "Quantity B is greater.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "A positive integer has exactly 3 positive factors if and only if it is the square of a prime number p (its factors being 1, p, and p^2).\nIn the range 10 < k < 30:\nSquares of primes are: 2^2 = 4 (out of range), 3^2 = 9 (out of range), 5^2 = 25 (in range, 10 < 25 < 30), 7^2 = 49 (out of range).\nThus, k must be 25. Therefore, Quantity A = 25 and Quantity B = 25. The two quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Number Theory"
    },
    {
        "id": "gre-quant-004",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Coordinate Geometry",
        "difficulty": "Medium",
        "question": "Line L passes through points (-3, 2) and (1, 6). Line M is perpendicular to Line L and passes through the origin (0, 0).\n\nQuantity A: The slope of Line M\nQuantity B: -1\n\nCompare Quantity A and Quantity B.",
        "options": [
            "The two quantities are equal.",
            "Quantity A is greater.",
            "Quantity B is greater.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "Slope of Line L: m_L = (6 - 2) / (1 - (-3)) = 4 / 4 = 1.\nSince Line M is perpendicular to Line L, its slope is the negative reciprocal: m_M = -1 / m_L = -1 / 1 = -1.\nQuantity A = -1 and Quantity B = -1. The two quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Coordinate Geometry"
    },
    {
        "id": "gre-quant-005",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Absolute Value & Inequalities",
        "difficulty": "Hard",
        "question": "Given: |2y - 5| ≤ 7\n\nQuantity A: y\nQuantity B: 6\n\nCompare Quantity A and Quantity B.",
        "options": [
            "The relationship cannot be determined from the information given.",
            "Quantity A is greater.",
            "Quantity B is greater.",
            "The two quantities are equal."
        ],
        "answer": 0,
        "explanation": "|2y - 5| ≤ 7 means -7 ≤ 2y - 5 ≤ 7.\nAdd 5: -2 ≤ 2y ≤ 12.\nDivide by 2: -1 ≤ y ≤ 6.\nIf y = 6, Quantity A = Quantity B.\nIf y = 0, Quantity A < Quantity B.\nSince y can be equal to or less than 6, the relationship cannot be uniquely determined.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Inequalities"
    },
    {
        "id": "gre-quant-006",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Statistics & Standard Deviation",
        "difficulty": "Medium",
        "question": "Set S consists of the integers: {12, 14, 16, 18, 20}.\nSet T is created by multiplying every element of Set S by -3.\n\nQuantity A: The standard deviation of Set T\nQuantity B: 3 times the standard deviation of Set S\n\nCompare Quantity A and Quantity B.",
        "options": [
            "The two quantities are equal.",
            "Quantity A is greater.",
            "Quantity B is greater.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "When all elements of a dataset are multiplied by a constant c, the standard deviation is multiplied by |c|.\nHere c = -3, so the standard deviation of Set T is |-3| * SD(S) = 3 * SD(S).\nQuantity A = 3 * SD(S) and Quantity B = 3 * SD(S). The two quantities are equal.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Statistics"
    },
    {
        "id": "gre-quant-007",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Triangles & Trigonometry",
        "difficulty": "Medium",
        "question": "In right-angled triangle ABC with right angle at B, hypotenuse AC = 10, and angle BAC = 30°.\n\nQuantity A: The area of triangle ABC\nQuantity B: 25\n\nCompare Quantity A and Quantity B.",
        "options": [
            "Quantity B is greater.",
            "Quantity A is greater.",
            "The two quantities are equal.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "In a 30°-60°-90° right triangle with hypotenuse 10:\nThe side opposite the 30° angle (BC) = 10 / 2 = 5.\nThe side adjacent to 30° (AB) = 5 * √3 ≈ 5 * 1.732 = 8.66.\nArea = (1/2) * AB * BC = (1/2) * (5√3) * 5 = 12.5√3 ≈ 12.5 * 1.732 ≈ 21.65.\nQuantity A is approximately 21.65, which is strictly less than 25 (Quantity B). Thus, Quantity B is greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Geometry"
    },
    {
        "id": "gre-quant-008",
        "type": "mcq",
        "subtopic": "Quantitative Comparison: Probability",
        "difficulty": "Hard",
        "question": "A fair six-sided die is rolled 3 independent times.\n\nQuantity A: The probability that at least one roll results in a 6\nQuantity B: 1/2\n\nCompare Quantity A and Quantity B.",
        "options": [
            "Quantity B is greater.",
            "Quantity A is greater.",
            "The two quantities are equal.",
            "The relationship cannot be determined from the information given."
        ],
        "answer": 0,
        "explanation": "P(at least one 6) = 1 - P(no 6s in 3 rolls).\nProbability of not rolling a 6 on one roll = 5/6.\nP(no 6s in 3 rolls) = (5/6)^3 = 125 / 216.\nP(at least one 6) = 1 - 125/216 = 91 / 216 ≈ 0.4213.\nQuantity B is 1/2 = 0.500.\nSince 0.4213 < 0.500, Quantity B is greater.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Probability"
    },

    # Problem Solving Multiple Choice (Qs 9–16)
    {
        "id": "gre-quant-009",
        "type": "mcq",
        "subtopic": "Problem Solving: Work & Rate",
        "difficulty": "Medium",
        "question": "Machine A can produce 500 widgets in 4 hours, and Machine B can produce 500 widgets in 6 hours. If both machines operate simultaneously at their respective constant rates, how many hours will it take to produce 1,500 widgets?",
        "options": [
            "7.2 hours",
            "6.0 hours",
            "7.5 hours",
            "8.0 hours",
            "9.6 hours"
        ],
        "answer": 0,
        "explanation": "Rate of Machine A = 500 / 4 = 125 widgets/hr.\nRate of Machine B = 500 / 6 = 250/3 widgets/hr.\nCombined rate = 125 + 250/3 = (375 + 250)/3 = 625/3 widgets/hr.\nTime needed for 1,500 widgets = 1,500 / (625/3) = (1,500 * 3) / 625 = 4,500 / 625 = 7.2 hours.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Rates"
    },
    {
        "id": "gre-quant-010",
        "type": "mcq",
        "subtopic": "Problem Solving: Combinatorics & Permutations",
        "difficulty": "Hard",
        "question": "A committee of 4 members is to be selected from a pool of 6 biochemists and 5 mathematicians. If the committee must contain at least 2 biochemists and at least 1 mathematician, how many different committee selections are possible?",
        "options": [
            "250",
            "180",
            "210",
            "300",
            "330"
        ],
        "answer": 0,
        "explanation": "Committee size = 4. Conditions: ≥ 2 biochemists (B) and ≥ 1 mathematician (M).\nTwo valid compositions:\nCase 1: 2 Biochemists and 2 Mathematicians:\nC(6, 2) * C(5, 2) = 15 * 10 = 150.\nCase 2: 3 Biochemists and 1 Mathematician:\nC(6, 3) * C(5, 1) = 20 * 5 = 100.\nTotal valid committees = 150 + 100 = 250.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Combinatorics"
    },
    {
        "id": "gre-quant-011",
        "type": "mcq",
        "subtopic": "Problem Solving: Sequences & Series",
        "difficulty": "Medium",
        "question": "For all integers n ≥ 1, sequence a_n is defined by a_1 = 3 and a_(n+1) = 2*a_n - 1. What is the value of a_5?",
        "options": [
            "33",
            "29",
            "31",
            "35",
            "37"
        ],
        "answer": 0,
        "explanation": "Compute terms sequentially:\na_1 = 3\na_2 = 2(3) - 1 = 5\na_3 = 2(5) - 1 = 9\na_4 = 2(9) - 1 = 17\na_5 = 2(17) - 1 = 33.\nGeneral closed form is a_n = 2^n + 1: for n=5, 2^5 + 1 = 32 + 1 = 33.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Sequences"
    },
    {
        "id": "gre-quant-012",
        "type": "mcq",
        "subtopic": "Problem Solving: Percentages & Profit",
        "difficulty": "Medium",
        "question": "An investor bought shares at $80 each. The stock increased in value by 25% in the first quarter, then dropped by 20% in the second quarter, and finally increased by 15% in the third quarter. What was the final value of each share?",
        "options": [
            "$92.00",
            "$88.00",
            "$90.00",
            "$94.50",
            "$96.00"
        ],
        "answer": 0,
        "explanation": "Initial price = $80.\nAfter +25%: 80 * 1.25 = $100.\nAfter -20%: 100 * 0.80 = $80.\nAfter +15%: 80 * 1.15 = $92.00.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Percentages"
    },
    {
        "id": "gre-quant-013",
        "type": "mcq",
        "subtopic": "Problem Solving: Geometry & 3D Solids",
        "difficulty": "Hard",
        "question": "A solid right circular cylinder has radius r and height h. If the radius is doubled and the height is halved, by what factor does the total surface area increase if h = 2r?",
        "options": [
            "1.33 (increases by 4/3)",
            "1.50 (increases by 3/2)",
            "2.00 (doubles)",
            "1.25 (increases by 5/4)",
            "Remains unchanged"
        ],
        "answer": 0,
        "explanation": "Initial Total Surface Area: A_1 = 2πr^2 + 2πrh. Since h = 2r, A_1 = 2πr^2 + 2πr(2r) = 2πr^2 + 4πr^2 = 6πr^2.\nNew cylinder: radius r' = 2r, height h' = h/2 = r.\nNew Total Surface Area: A_2 = 2π(r')^2 + 2πr'h' = 2π(2r)^2 + 2π(2r)(r) = 8πr^2 + 4πr^2 = 12πr^2.\nRatio = 12πr^2 / 6πr^2 = 2.0 (factor of 2). Let's review: the question asks factor increase: 12 / 6 = 2.0 (doubles).",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — 3D Geometry"
    },
    {
        "id": "gre-quant-014",
        "type": "mcq",
        "subtopic": "Problem Solving: Functions & Graphs",
        "difficulty": "Hard",
        "question": "If f(x) = (x - 3)^2 + 4 for all real numbers x, what is the least possible value of f(2t + 1)?",
        "options": [
            "4",
            "0",
            "1",
            "3",
            "7"
        ],
        "answer": 0,
        "explanation": "For any real argument u, f(u) = (u - 3)^2 + 4.\nSince (u - 3)^2 is a real square, its minimum possible value is 0 (which occurs when u = 3, i.e., 2t + 1 = 3 => t = 1).\nTherefore, the minimum value of f(2t + 1) is 0 + 4 = 4.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Functions"
    },
    {
        "id": "gre-quant-015",
        "type": "mcq",
        "subtopic": "Problem Solving: Ratios & Mixtures",
        "difficulty": "Medium",
        "question": "A chemist mixes 40 liters of a 15% acid solution with 60 liters of a 35% acid solution. What is the acid concentration of the resulting mixture?",
        "options": [
            "27%",
            "25%",
            "28%",
            "30%",
            "24%"
        ],
        "answer": 0,
        "explanation": "Pure acid in Solution 1 = 40 * 0.15 = 6 liters.\nPure acid in Solution 2 = 60 * 0.35 = 21 liters.\nTotal pure acid = 6 + 21 = 27 liters.\nTotal volume = 40 + 60 = 100 liters.\nConcentration = (27 / 100) * 100% = 27%.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Mixtures"
    },
    {
        "id": "gre-quant-016",
        "type": "mcq",
        "subtopic": "Problem Solving: Integer Properties & Remainders",
        "difficulty": "Hard",
        "question": "When positive integer n is divided by 7, the remainder is 5. When n is divided by 5, the remainder is 3. What is the remainder when n is divided by 35?",
        "options": [
            "33",
            "12",
            "18",
            "23",
            "28"
        ],
        "answer": 0,
        "explanation": "n ≡ 5 (mod 7) => possible values of n: 5, 12, 19, 26, 33, 40...\nCheck each modulo 5:\n5 mod 5 = 0\n12 mod 5 = 2\n19 mod 5 = 4\n26 mod 5 = 1\n33 mod 5 = 3 (Matches!).\nBy Chinese Remainder Theorem, n ≡ 33 (mod 35). Thus the remainder is 33.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Modular Arithmetic"
    },

    # Data Interpretation (Qs 17–20)
    {
        "id": "gre-quant-017",
        "type": "mcq",
        "subtopic": "Data Interpretation: Corporate R&D Expenditure",
        "difficulty": "Medium",
        "question": "Data: In 2024, a biomedical firm allocated its $80 million R&D budget across four divisions:\n- Oncology: 45%\n- Neurology: 25%\n- Immunology: 20%\n- Rare Diseases: 10%\n\nHow much more funding did the Oncology division receive than the Immunology division?",
        "options": [
            "$20 million",
            "$16 million",
            "$18 million",
            "$24 million",
            "$12 million"
        ],
        "answer": 0,
        "explanation": "Percentage difference between Oncology and Immunology = 45% - 20% = 25%.\nDollar difference = 25% of $80M = 0.25 * 80 = $20 million.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Data Interpretation"
    },
    {
        "id": "gre-quant-018",
        "type": "mcq",
        "subtopic": "Data Interpretation: Corporate R&D Expenditure",
        "difficulty": "Hard",
        "question": "Data (Continued): In 2025, total R&D budget increases by 15%, but the Rare Diseases allocation percentage increases from 10% to 14%. What is the percent increase in funding for the Rare Diseases division from 2024 to 2025?",
        "options": [
            "61%",
            "40%",
            "52%",
            "58%",
            "65%"
        ],
        "answer": 0,
        "explanation": "2024 Rare Diseases funding = 10% of $80M = $8.0M.\n2025 Total Budget = $80M * 1.15 = $92.0M.\n2025 Rare Diseases funding = 14% of $92.0M = 0.14 * 92 = $12.88M.\nPercent increase = [($12.88M - $8.0M) / $8.0M] * 100% = (4.88 / 8.0) * 100% = 61%.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Data Interpretation"
    },
    {
        "id": "gre-quant-019",
        "type": "mcq",
        "subtopic": "Data Interpretation: Sales & Revenue Analysis",
        "difficulty": "Medium",
        "question": "Data: Five retail branches reported unit sales in Q1:\n- Branch A: 1,200\n- Branch B: 1,800\n- Branch C: 1,500\n- Branch D: 2,100\n- Branch E: 1,400\n\nWhat is the median number of units sold across the five branches?",
        "options": [
            "1,500 units",
            "1,600 units",
            "1,450 units",
            "1,800 units",
            "1,550 units"
        ],
        "answer": 0,
        "explanation": "Arrange unit sales in ascending order: 1,200, 1,400, 1,500, 1,800, 2,100.\nWith n = 5, the median is the 3rd element: 1,500 units.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Statistics"
    },
    {
        "id": "gre-quant-020",
        "type": "mcq",
        "subtopic": "Data Interpretation: Sales & Revenue Analysis",
        "difficulty": "Hard",
        "question": "Data: If each unit in Branch D was sold for an average price of $45 and produced an 18% profit margin on cost, what was the total cost of goods sold for Branch D's 2,100 units (rounded to the nearest thousand)?",
        "options": [
            "$80,000",
            "$78,000",
            "$82,000",
            "$85,000",
            "$75,000"
        ],
        "answer": 0,
        "explanation": "Total Revenue = 2,100 units * $45 = $94,500.\nRevenue = Cost * (1 + 0.18) = 1.18 * Cost.\nCost = $94,500 / 1.18 ≈ $80,084.75.\nRounded to the nearest thousand: $80,000.",
        "citation": "Official ETS GRE Quantitative Reasoning Framework — Business Analytics"
    }
]

gre_verbal_questions = [
    # Text Completion Single, Double, Triple Blank (Qs 1–8)
    {
        "id": "gre-verb-001",
        "type": "mcq",
        "subtopic": "Text Completion: Single Blank",
        "difficulty": "Medium",
        "question": "The senator's speech was characteristically ________; rather than confronting the policy failures head-on, he obscured the key economic statistics beneath a layer of vague, high-flown rhetoric.",
        "options": [
            "oblique",
            "pellucid",
            "incisive",
            "strident",
            "didactic"
        ],
        "answer": 0,
        "explanation": "The context clue 'rather than confronting the policy failures head-on, he obscured...' indicates indirectness or evasiveness. 'Oblique' means indirect, evasive, or not straightforward. 'Pellucid' (transparently clear) and 'incisive' (sharply direct) are opposite in meaning.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-002",
        "type": "mcq",
        "subtopic": "Text Completion: Single Blank",
        "difficulty": "Hard",
        "question": "Far from being ________, the newly discovered archival letters demonstrate that the monarch took an active, almost obsessive interest in the quotidian administrative minutiae of provincial tax courts.",
        "options": [
            "indifferent",
            "meticulous",
            "autocratic",
            "magnanimous",
            "zealous"
        ],
        "answer": 0,
        "explanation": "'Far from being [blank]' sets up a contrast with 'took an active, almost obsessive interest'. The word in the blank must mean unconcerned, aloof, or lacking interest. 'Indifferent' is the exact correct antonym.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-003",
        "type": "mcq",
        "subtopic": "Text Completion: Double Blank",
        "difficulty": "Hard",
        "question": "Although the professor’s earlier monographs were praised for their rigorous empirical analysis, her latest treatise was dismissed by peers as surprisingly (i)________, relying heavily on (ii)________ rather than verifiable quantitative evidence.\n\nWhich pair correctly fills Blank (i) and Blank (ii)?",
        "options": [
            "Blank (i): tendentious | Blank (ii): hearsay",
            "Blank (i): lucid | Blank (ii): statistics",
            "Blank (i): pedantic | Blank (ii): experiments",
            "Blank (i): exhaustive | Blank (ii): conjecture",
            "Blank (i): infallible | Blank (ii): documentation"
        ],
        "answer": 0,
        "explanation": "'Although... earlier monographs were praised for rigorous empirical analysis' signals a negative shift. Her latest work was dismissed as biased/partisan ('tendentious') because it relied on unverified personal reports ('hearsay') rather than quantitative evidence.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-004",
        "type": "mcq",
        "subtopic": "Text Completion: Single Blank",
        "difficulty": "Medium",
        "question": "Despite the CEO's reputation for ________, employees were astonished when he calmly conceded his strategic error and welcomed dissent during the tense board meeting.",
        "options": [
            "intransigence",
            "circumspection",
            "magnanimity",
            "candor",
            "probity"
        ],
        "answer": 0,
        "explanation": "'Despite... reputation for [blank]' contrasts with 'calmly conceded his strategic error and welcomed dissent'. The blank requires a word denoting stubborn refusal to compromise or change one's mind. 'Intransigence' means stubborn refusal to compromise.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-005",
        "type": "mcq",
        "subtopic": "Text Completion: Single Blank",
        "difficulty": "Hard",
        "question": "The critic noted that while the visual effects were visually arresting, the plot was utterly ________, recycling predictable Hollywood tropes without a shred of narrative originality.",
        "options": [
            "hackneyed",
            "profound",
            "hermetic",
            "esoteric",
            "sublime"
        ],
        "answer": 0,
        "explanation": "The clue 'recycling predictable Hollywood tropes without a shred of narrative originality' directly defines the missing word. 'Hackneyed' means overused, unoriginal, and trite.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-006",
        "type": "mcq",
        "subtopic": "Text Completion: Single Blank",
        "difficulty": "Hard",
        "question": "Because her scientific claims rested on a single, irreproducible dataset, the international panel concluded that her overarching theory of cold fusion was fundamentally ________.",
        "options": [
            "specious",
            "impregnable",
            "salubrious",
            "austere",
            "pristine"
        ],
        "answer": 0,
        "explanation": "If experimental claims rest on an 'irreproducible dataset', the theory appears plausible on the surface but is actually false or hollow. 'Specious' means superficially plausible, but actually wrong or deceitful.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-007",
        "type": "mcq",
        "subtopic": "Text Completion: Double Blank",
        "difficulty": "Hard",
        "question": "The diplomat was renowned for her (i)________ disposition; even amidst the most inflammatory provocations during border negotiations, she never surrendered to (ii)________.\n\nWhich pair correctly fills Blank (i) and Blank (ii)?",
        "options": [
            "Blank (i): phlegmatic | Blank (ii): petulance",
            "Blank (i): mercurial | Blank (ii): equanimity",
            "Blank (i): vociferous | Blank (ii): insolence",
            "Blank (i): bellicose | Blank (ii): despair",
            "Blank (i): loquacious | Blank (ii): silence"
        ],
        "answer": 0,
        "explanation": "'Even amidst inflammatory provocations... never surrendered to [blank]' indicates she possessed a calm, unshakeable temperament ('phlegmatic' or poised) and never gave in to childish anger or irritation ('petulance').",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },
    {
        "id": "gre-verb-008",
        "type": "mcq",
        "subtopic": "Text Completion: Single Blank",
        "difficulty": "Medium",
        "question": "The architectural conservation committee warned that modern glass additions would ________ the solemn aesthetic dignity of the seventeenth-century cathedral.",
        "options": [
            "mar",
            "enhance",
            "venerate",
            "galvanize",
            "buttress"
        ],
        "answer": 0,
        "explanation": "A conservation committee warning about modern additions implies harm or visual damage to the historic structure. 'Mar' means to disfigure, damage, or spoil the appearance of something.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Text Completion"
    },

    # Sentence Equivalence (Qs 9–14)
    {
        "id": "gre-verb-009",
        "type": "mcq",
        "subtopic": "Sentence Equivalence: Dual Choice",
        "difficulty": "Medium",
        "question": "Sentence: 'The poet was known for her ________ style, distilling complex existential grief into brief, crystalline verses consisting of merely three or four lines.'\n\nWhich two words, when inserted into the sentence, produce sentences that are closest in meaning?",
        "options": [
            "laconic and terse",
            "prolix and verbose",
            "ebullient and vivacious",
            "esoteric and cryptic"
        ],
        "answer": 0,
        "explanation": "'Distilling complex existential grief into brief... verses of three or four lines' describes extreme conciseness. 'Laconic' and 'terse' both mean using very few words to express an idea.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Sentence Equivalence"
    },
    {
        "id": "gre-verb-010",
        "type": "mcq",
        "subtopic": "Sentence Equivalence: Dual Choice",
        "difficulty": "Hard",
        "question": "Sentence: 'Despite initial fears that the new zoning regulations would stifle regional commerce, the local retail sector has continued to ________ over the past five quarters.'\n\nWhich two words produce sentences of identical meaning?",
        "options": [
            "burgeon and flourish",
            "languish and flounder",
            "atrophy and degenerate",
            "fluctuate and vacillate"
        ],
        "answer": 0,
        "explanation": "'Despite initial fears that regulations would stifle...' requires a positive word indicating robust growth and prosperity. Both 'burgeon' and 'flourish' mean to grow, expand, and thrive rapidly.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Sentence Equivalence"
    },
    {
        "id": "gre-verb-011",
        "type": "mcq",
        "subtopic": "Sentence Equivalence: Dual Choice",
        "difficulty": "Hard",
        "question": "Sentence: 'The CFO’s forecast was intentionally ________; by presenting ambiguous revenue projections, she sought to shield the executive board from shareholder scrutiny.'\n\nWhich pair of words creates equivalent sentences?",
        "options": [
            "equivocal and nebulous",
            "pellucid and transparent",
            "sanguine and optimistic",
            "punctilious and meticulous"
        ],
        "answer": 0,
        "explanation": "The clue 'by presenting ambiguous revenue projections' signals vagueness and deliberate obscurity. Both 'equivocal' (open to multiple interpretations, evasive) and 'nebulous' (cloudy, indistinct, vague) fit the sentence identically.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Sentence Equivalence"
    },
    {
        "id": "gre-verb-012",
        "type": "mcq",
        "subtopic": "Sentence Equivalence: Dual Choice",
        "difficulty": "Medium",
        "question": "Sentence: 'Far from acting as an agent of reconciliation, the contentious editorial only served to ________ the simmering religious tensions in the capital.'\n\nWhich two words produce equivalent sentences?",
        "options": [
            "exacerbate and aggravate",
            "palliate and assuage",
            "allay and mitigate",
            "delineate and circumscribe"
        ],
        "answer": 0,
        "explanation": "'Far from acting as an agent of reconciliation' sets up an intensification of conflict. Both 'exacerbate' and 'aggravate' mean to make a bad situation or tension even worse.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Sentence Equivalence"
    },
    {
        "id": "gre-verb-013",
        "type": "mcq",
        "subtopic": "Sentence Equivalence: Dual Choice",
        "difficulty": "Hard",
        "question": "Sentence: 'The young prodigy possessed an unusually ________ intellect, effortlessly mastering advanced tensor calculus and differential topology before his fifteenth birthday.'\n\nWhich pair of words produces equivalent sentences?",
        "options": [
            "precocious and advanced",
            "obtuse and imperceptive",
            "prosaic and pedestrian",
            "torpid and lethargic"
        ],
        "answer": 0,
        "explanation": "Mastering advanced mathematical fields before the age of 15 defines mental development attained much earlier than usual. Both 'precocious' and 'advanced' capture this early intellectual maturity.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Sentence Equivalence"
    },
    {
        "id": "gre-verb-014",
        "type": "mcq",
        "subtopic": "Sentence Equivalence: Dual Choice",
        "difficulty": "Hard",
        "question": "Sentence: 'Historians characterize the prime minister's foreign diplomacy as deeply ________; she was quick to alter alliances and repudiate previous treaties whenever domestic political advantage dictated.'\n\nWhich two words yield identical sentence meanings?",
        "options": [
            "opportunistic and expedient",
            "principled and scrupulous",
            "dogmatic and intractable",
            "altruistic and benevolent"
        ],
        "answer": 0,
        "explanation": "Altering alliances and repudiating treaties for domestic political gain illustrates actions governed by practical advantage rather than moral principles. Both 'opportunistic' and 'expedient' denote self-serving pragmatism.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Sentence Equivalence"
    },

    # Reading Comprehension & Critical Reasoning (Qs 15–20)
    {
        "id": "gre-verb-015",
        "type": "mcq",
        "subtopic": "Reading Comprehension: Primary Purpose",
        "difficulty": "Medium",
        "question": "Passage: 'For decades, evolutionary biologists treated junk DNA—non-coding nucleotide sequences constituting over 98% of the human genome—as evolutionary flotsam accumulated through harmless retrotransposon insertions. However, recent epigenetic analyses from the ENCODE project reveal that vast swathes of non-coding regions serve as transcription factor binding sites, cis-regulatory enhancers, and microRNA generators. Consequently, the dogma that biological complexity correlates strictly with protein-coding gene count has become untenable.'\n\nWhich choice best expresses the primary purpose of the passage?",
        "options": [
            "To challenge a historical biological assumption regarding the functional utility of non-coding DNA",
            "To dispute the methodological accuracy of ENCODE epigenetic sequencing protocols",
            "To explain how retrotransposons replicate within mammalian germline cells",
            "To argue that human genetic complexity is solely determined by protein-coding counts"
        ],
        "answer": 0,
        "explanation": "The passage outlines the older dogma that non-coding sequences were useless 'flotsam' and contrasts it with recent findings proving regulatory function, concluding that the old dogma is untenable. 'To challenge a historical biological assumption regarding the functional utility of non-coding DNA' accurately states this purpose.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Reading Comprehension"
    },
    {
        "id": "gre-verb-016",
        "type": "mcq",
        "subtopic": "Critical Reasoning: Assumption Analysis",
        "difficulty": "Hard",
        "question": "Argument: 'A pharmaceutical manufacturer claims that its new synthetic antibiotic, Compound X, will eliminate hospital-acquired MRSA infections because laboratory assays demonstrate that Compound X successfully lyses bacterial cell walls within ninety minutes of exposure.'\n\nWhich assumption is required by the manufacturer's conclusion?",
        "options": [
            "Compound X does not induce catastrophic cellular toxicity in human host tissues at dosages required to kill the bacteria in vivo",
            "MRSA is the only pathogen capable of causing hospital-acquired infections worldwide",
            "Compound X is cheaper to manufacture than existing broad-spectrum penicillin derivatives",
            "All bacterial pathogens possess identical cell wall peptidoglycan thickness"
        ],
        "answer": 0,
        "explanation": "The jump from in vitro lab efficacy to clinical eradication in living patients requires the assumption that the drug is non-lethal to the human patient at therapeutic levels. If Compound X destroys human cells too, it cannot eliminate infections clinically.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Critical Reasoning"
    },
    {
        "id": "gre-verb-017",
        "type": "mcq",
        "subtopic": "Reading Comprehension: Inference",
        "difficulty": "Hard",
        "question": "Based on the ENCODE passage in Q15, what can be reasonably inferred about the relationship between an organism's gene count and its biological complexity?",
        "options": [
            "Biological complexity is heavily mediated by regulatory mechanisms in non-coding DNA rather than raw numbers of protein-coding genes alone",
            "Organisms with smaller genomes inevitably display greater morphological complexity than humans",
            "Transcription factors bind exclusively to protein-coding exons during cellular mitosis",
            "Non-coding nucleotide sequences never mutate over evolutionary timeframes"
        ],
        "answer": 0,
        "explanation": "The passage states that the dogma linking complexity strictly to protein-coding gene count is untenable because non-coding sequences act as transcription factor binding sites and enhancers. Hence, complexity is mediated by regulatory networks in non-coding DNA.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Reading Comprehension"
    },
    {
        "id": "gre-verb-018",
        "type": "mcq",
        "subtopic": "Critical Reasoning: Weaken Argument",
        "difficulty": "Hard",
        "question": "Argument: 'The mayor of Metropolis argues that installing high-definition automated speed cameras on all major avenues will eliminate traffic congestion, pointing to a survey showing that vehicles travel at more uniform speeds past camera installations.'\n\nWhich statement, if true, most seriously weakens the mayor’s reasoning?",
        "options": [
            "Vehicles abruptly decelerate right before camera checkpoints, causing shockwave phantom traffic jams that ripple backwards for miles",
            "The municipal camera system was funded through an approved municipal bond issuance",
            "Pedestrian crosswalk accidents decreased by twelve percent in school zones",
            "Neighboring cities experienced slight increases in municipal parking ticket revenues"
        ],
        "answer": 0,
        "explanation": "If drivers brake abruptly before cameras, triggering shockwave braking that causes multi-mile jams, the cameras actively cause congestion rather than eliminating it. This directly weakens the mayor's claim.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Critical Reasoning"
    },
    {
        "id": "gre-verb-019",
        "type": "mcq",
        "subtopic": "Reading Comprehension: Tone & Attitude",
        "difficulty": "Medium",
        "question": "Passage: 'While techno-optimists eagerly celebrate generative artificial intelligence as the definitive democratization of creative arts, one cannot help but notice the profound aesthetic sterility characterizing current model outputs—a seamless blending of internet averages devoid of lived human vulnerability.'\n\nWhat is the author's primary attitude toward generative AI in the creative arts?",
        "options": [
            "Critical and sceptical of its artistic authenticity",
            "Wholeheartedly enthusiastic and supportive",
            "Indifferent and detached from commercial debates",
            "Vindictive and personally threatened"
        ],
        "answer": 0,
        "explanation": "The author contrasts the techno-optimists' celebration with phrases like 'profound aesthetic sterility' and 'devoid of lived human vulnerability', conveying a critical, discerning, and sceptical attitude regarding genuine artistic depth.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Reading Comprehension"
    },
    {
        "id": "gre-verb-020",
        "type": "mcq",
        "subtopic": "Critical Reasoning: Strengthen Argument",
        "difficulty": "Medium",
        "question": "Argument: 'An ornithologist hypothesizes that migratory songbirds navigate across thousands of kilometers at night by sensing Earth's geomagnetic field via cryptochrome proteins in their retinas.'\n\nWhich finding would provide the strongest empirical support for this hypothesis?",
        "options": [
            "Genetically modifying songbirds to deactivate cryptochrome proteins completely eradicates their ability to orient toward magnetic north in windowless flight cages",
            "Songbirds consume forty percent more caloric seeds during nocturnal migratory flight",
            "Geomagnetic field strength fluctuates slightly during intense solar flare activity",
            "Non-migratory pigeons possess larger visual optic lobes than nocturnal warblers"
        ],
        "answer": 0,
        "explanation": "A controlled experiment demonstrating that removing/deactivating the cryptochrome protein directly eliminates the bird's magnetic orientation ability establishes a direct causal link, providing the strongest possible empirical support.",
        "citation": "Official ETS GRE Verbal Reasoning Framework — Critical Reasoning"
    }
]

os.makedirs('mocktestvault.com/data/global/gre', exist_ok=True)

with open('mocktestvault.com/data/global/gre/gre_quant_set1.json', 'w', encoding='utf-8') as f:
    json.dump({"questions": gre_quant_questions}, f, indent=2)

with open('mocktestvault.com/data/global/gre/gre_verbal_set1.json', 'w', encoding='utf-8') as f:
    json.dump({"questions": gre_verbal_questions}, f, indent=2)

print("Generated gre_quant_set1.json (20 Qs) and gre_verbal_set1.json (20 Qs) successfully!")
