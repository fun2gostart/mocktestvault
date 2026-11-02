#!/usr/bin/env python3
"""
Generates Digital SAT Set 05 Question Banks to bring Digital SAT to 100 Questions each:
1. data/us/sat/digital_sat_math_set5.json (20 Questions - 1600 Benchmark Master Module)
2. data/us/sat/digital_sat_reading_set5.json (20 Questions - High Percentile Comprehensive Module)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_SAT = os.path.join(BASE_DIR, "data", "us", "sat")
os.makedirs(US_DATA_SAT, exist_ok=True)

# ==============================================================================
# DIGITAL SAT MATH SET 05 (20 Questions - 1600 Benchmark Master Module)
# ==============================================================================
sat_math_set5 = [
  {
    "id": "sat-m-501",
    "type": "mcq",
    "subtopic": "Heart of Algebra: Absolute Value Equations",
    "difficulty": "Medium",
    "question": "What is the sum of the solutions to the equation |3x - 7| = 14?",
    "options": ["14/3", "7/3", "0", "28/3"],
    "answer": 0,
    "explanation": "Break into two cases: Case 1: 3x - 7 = 14 → 3x = 21 → x = 7. Case 2: 3x - 7 = -14 → 3x = -7 → x = -7/3. Sum of solutions = 7 + (-7/3) = 21/3 - 7/3 = 14/3. Shortcut: for |ax - b| = c, the sum of roots is 2b/a = 2(7)/3 = 14/3.",
    "citation": "College Board Digital SAT® Math Specifications — Heart of Algebra: Absolute Value Equations"
  },
  {
    "id": "sat-m-502",
    "type": "mcq",
    "subtopic": "Heart of Algebra: Linear Inequality Word Problem",
    "difficulty": "Medium",
    "question": "A catering company charges a base setup fee of $120 plus $18.50 per guest for dinner. If an event planner has a budget of at most $750, what is the maximum number of guests that can be invited?",
    "options": ["34", "35", "33", "40"],
    "answer": 0,
    "explanation": "Set up the inequality: 120 + 18.50g ≤ 750. Subtract 120: 18.50g ≤ 630. Divide by 18.50: g ≤ 630 / 18.50 ≈ 34.054. Since the number of guests must be a whole number, the maximum number is 34.",
    "citation": "College Board Digital SAT® Math Specifications — Heart of Algebra: Linear Inequalities in One Variable"
  },
  {
    "id": "sat-m-503",
    "type": "mcq",
    "subtopic": "Heart of Algebra: Perpendicular Lines",
    "difficulty": "Medium",
    "question": "In the xy-plane, line k passes through the points (2, -3) and (6, 5). Line m is perpendicular to line k. What is the slope of line m?",
    "options": ["-1/2", "2", "-2", "1/2"],
    "answer": 0,
    "explanation": "Slope of line k: m_k = (5 - (-3)) / (6 - 2) = 8 / 4 = 2. Perpendicular lines have negative reciprocal slopes: m_m = -1 / m_k = -1/2.",
    "citation": "College Board Digital SAT® Math Specifications — Heart of Algebra: Linear Equations and Slope Properties"
  },
  {
    "id": "sat-m-504",
    "type": "mcq",
    "subtopic": "Heart of Algebra: Parallel Line Systems with No Solution",
    "difficulty": "Hard",
    "question": "The system of equations below has no solution: \n4x - 6y = 15 \n6x + ky = 22 \nWhat is the value of the constant k?",
    "options": ["-9", "9", "-4", "6"],
    "answer": 0,
    "explanation": "A linear system has no solution if the lines are parallel (matching slopes but different y-intercepts). For a1*x + b1*y = c1 and a2*x + b2*y = c2 to be parallel: a1/a2 = b1/b2 → 4/6 = -6/k. Cross-multiply: 4k = -36 → k = -9. Check constant ratio: 4/6 ≠ 15/22, confirming no solution.",
    "citation": "College Board Digital SAT® Math Specifications — Heart of Algebra: Systems of Linear Equations"
  },
  {
    "id": "sat-m-505",
    "type": "mcq",
    "subtopic": "Heart of Algebra: Interpreting Intercepts",
    "difficulty": "Easy",
    "question": "The function C(m) = 45 + 0.20m models the monthly telephone bill C, in dollars, for m text messages sent. What does the value 45 represent in this model?",
    "options": [
      "The flat monthly subscription fee regardless of texts sent",
      "The fee charged per individual text message sent",
      "The maximum monthly bill allowed by the carrier",
      "The total number of text messages included in the plan"
    ],
    "answer": 0,
    "explanation": "In the linear function C(m) = 45 + 0.20m, 45 is the y-intercept (C(0) = 45), representing the fixed initial fee incurred when m = 0 text messages are sent.",
    "citation": "College Board Digital SAT® Math Specifications — Heart of Algebra: Linear Function Interpretations"
  },
  {
    "id": "sat-m-506",
    "type": "mcq",
    "subtopic": "Problem Solving: Percent Change & Successive Discounts",
    "difficulty": "Medium",
    "question": "A retail jacket originally priced at $160 is discounted by 25% during a weekend sale. A shopper uses a coupon for an additional 10% off the discounted price. What is the final price of the jacket before tax?",
    "options": ["$108", "$104", "$112", "$120"],
    "answer": 0,
    "explanation": "Discount of 25% means paying 75%: 160 * 0.75 = $120. An additional 10% discount on $120 means paying 90%: 120 * 0.90 = $108. (Note: discounts do not simply add to 35%).",
    "citation": "College Board Digital SAT® Math Specifications — Problem Solving: Percentages and Multi-Step Models"
  },
  {
    "id": "sat-m-507",
    "type": "mcq",
    "subtopic": "Problem Solving: Unit Conversion & Rate",
    "difficulty": "Medium",
    "question": "A water pump fills a cistern at a rate of 15 gallons per minute. If 1 gallon is approximately 3.785 liters, approximately how many liters does the pump deliver in 2.5 hours?",
    "options": ["8,516 liters", "3,407 liters", "5,678 liters", "14,194 liters"],
    "answer": 0,
    "explanation": "Calculate total minutes: 2.5 hours * 60 minutes/hour = 150 minutes. Total gallons = 150 min * 15 gal/min = 2,250 gallons. Convert to liters: 2,250 gallons * 3.785 L/gal = 8,516.25 liters ≈ 8,516 liters.",
    "citation": "College Board Digital SAT® Math Specifications — Problem Solving: Rates, Proportions, and Unit Conversions"
  },
  {
    "id": "sat-m-508",
    "type": "mcq",
    "subtopic": "Problem Solving: Two-Way Frequency Table Probability",
    "difficulty": "Medium",
    "question": "A survey of 200 high school students found that 120 students study Spanish, 50 study French, and 30 study both languages. If a student is selected at random from those who study Spanish, what is the probability that this student also studies French?",
    "options": ["1/4", "3/20", "3/5", "1/6"],
    "answer": 0,
    "explanation": "This is conditional probability P(French | Spanish). The conditioning group is students who study Spanish (120 students). Of these, 30 study both languages. P = 30 / 120 = 1/4 (or 0.25).",
    "citation": "College Board Digital SAT® Math Specifications — Problem Solving: Conditional Probability and Two-Way Tables"
  },
  {
    "id": "sat-m-509",
    "type": "mcq",
    "subtopic": "Problem Solving: Mean, Median, and Outliers",
    "difficulty": "Hard",
    "question": "A dataset contains 9 distinct test scores with a mean of 82 and a median of 84. If a 10th student scores 98 and is added to the dataset, which of the following statements must be true?",
    "options": [
      "The mean of the dataset will increase",
      "The median of the dataset will decrease",
      "The standard deviation of the dataset will decrease",
      "The range of the dataset will remain unchanged"
    ],
    "answer": 0,
    "explanation": "Since the new score (98) is greater than the existing mean (82), the new mean = (9 * 82 + 98) / 10 = (738 + 98) / 10 = 83.6 > 82. Adding an observation strictly greater than the mean always increases the mean.",
    "citation": "College Board Digital SAT® Math Specifications — Problem Solving: Center, Spread, and Shape of Distributions"
  },
  {
    "id": "sat-m-510",
    "type": "mcq",
    "subtopic": "Problem Solving: Scatterplots and Line of Best Fit",
    "difficulty": "Medium",
    "question": "A line of best fit for a dataset relating advertising budget x (thousands of dollars) to sales revenue y (thousands of dollars) is y = 3.4x + 18.5. For an advertising budget of $20,000, the actual sales revenue was $91,000. What is the residual for this data point?",
    "options": ["$4.5 thousand", "-$4.5 thousand", "$5.5 thousand", "$86.5 thousand"],
    "answer": 0,
    "explanation": "Residual = Actual y - Predicted y. Note units are in thousands, so x = 20, actual y = 91. Predicted y = 3.4(20) + 18.5 = 68 + 18.5 = 86.5. Residual = 91 - 86.5 = +4.5 (or $4,500).",
    "citation": "College Board Digital SAT® Math Specifications — Problem Solving: Linear Regression and Residuals"
  },
  {
    "id": "sat-m-511",
    "type": "mcq",
    "subtopic": "Passport to Advanced Math: Quadratic Discriminant",
    "difficulty": "Medium",
    "question": "For what value of c does the quadratic equation 3x^2 - 12x + c = 0 have exactly one real solution?",
    "options": ["12", "6", "18", "4"],
    "answer": 0,
    "explanation": "A quadratic ax^2 + bx + c = 0 has exactly one real solution (a double root) when discriminant Δ = b^2 - 4ac = 0. Here a = 3, b = -12: (-12)^2 - 4(3)(c) = 0 → 144 - 12c = 0 → 12c = 144 → c = 12.",
    "citation": "College Board Digital SAT® Math Specifications — Passport to Advanced Math: Quadratic Equations and Discriminants"
  },
  {
    "id": "sat-m-512",
    "type": "mcq",
    "subtopic": "Passport to Advanced Math: Vertex Form Transformation",
    "difficulty": "Medium",
    "question": "The parabola f(x) = x^2 - 8x + 19 is graphed in the xy-plane. What are the coordinates of its vertex?",
    "options": ["(4, 3)", "(-4, 3)", "(4, 19)", "(8, 3)"],
    "answer": 0,
    "explanation": "Complete the square or use h = -b / (2a): h = -(-8) / (2*1) = 4. Substitute x = 4: f(4) = (4)^2 - 8(4) + 19 = 16 - 32 + 19 = 3. Thus, the vertex is (4, 3).",
    "citation": "College Board Digital SAT® Math Specifications — Passport to Advanced Math: Quadratic Vertex Forms"
  },
  {
    "id": "sat-m-513",
    "type": "mcq",
    "subtopic": "Passport to Advanced Math: Rational Expression Simplification",
    "difficulty": "Hard",
    "question": "Which of the following expressions is equivalent to (x^2 - 25) / (2x^2 - 7x - 15) for all x where the expression is defined?",
    "options": ["(x + 5) / (2x + 3)", "(x - 5) / (2x - 3)", "(x + 5) / (2x - 5)", "(x - 5) / (2x + 5)"],
    "answer": 0,
    "explanation": "Factor numerator: (x - 5)(x + 5). Factor denominator: find two numbers that multiply to 2*(-15) = -30 and sum to -7: -10 and +3. Rewrite 2x^2 - 10x + 3x - 15 = 2x(x - 5) + 3(x - 5) = (2x + 3)(x - 5). Cancel (x - 5): (x + 5) / (2x + 3).",
    "citation": "College Board Digital SAT® Math Specifications — Passport to Advanced Math: Rational Expressions"
  },
  {
    "id": "sat-m-514",
    "type": "mcq",
    "subtopic": "Passport to Advanced Math: Exponential Decay Half-Life",
    "difficulty": "Hard",
    "question": "A radioactive isotope has a half-life of 8 days. An initial sample contains 320 grams of the isotope. Which function models the remaining mass M(t), in grams, after t days?",
    "options": [
      "M(t) = 320 * (1/2)^(t/8)",
      "M(t) = 320 * (1/2)^(8t)",
      "M(t) = 320 * (8)^(t/2)",
      "M(t) = 320 - (1/2)^(t/8)"
    ],
    "answer": 0,
    "explanation": "Standard half-life model is M(t) = M0 * (1/2)^(t / T_half). With initial mass M0 = 320 and half-life T_half = 8 days, M(t) = 320 * (1/2)^(t/8).",
    "citation": "College Board Digital SAT® Math Specifications — Passport to Advanced Math: Exponential Growth and Decay"
  },
  {
    "id": "sat-m-515",
    "type": "mcq",
    "subtopic": "Passport to Advanced Math: Radical Equation with Extraneous Roots",
    "difficulty": "Hard",
    "question": "What is the solution set of the equation √(2x + 15) = x?",
    "options": ["{5}", "{-3, 5}", "{-3}", "No real solutions"],
    "answer": 0,
    "explanation": "Square both sides: 2x + 15 = x^2 → x^2 - 2x - 15 = 0 → (x - 5)(x + 3) = 0 → candidate roots x = 5 and x = -3. Test x = 5: √(2(5) + 15) = √25 = 5 (valid). Test x = -3: √(2(-3) + 15) = √9 = 3 ≠ -3 (extraneous). Therefore, only {5} is a valid solution.",
    "citation": "College Board Digital SAT® Math Specifications — Passport to Advanced Math: Radical and Polynomial Operations"
  },
  {
    "id": "sat-m-516",
    "type": "mcq",
    "subtopic": "Additional Topics: Circle Equation and Radius",
    "difficulty": "Medium",
    "question": "In the xy-plane, the equation of a circle is x^2 + y^2 - 10x + 6y = 47. What is the radius of the circle?",
    "options": ["9", "81", "√47", "7"],
    "answer": 0,
    "explanation": "Complete the square for x and y: (x^2 - 10x + 25) + (y^2 + 6y + 9) = 47 + 25 + 9. (x - 5)^2 + (y + 3)^2 = 81. Since r^2 = 81, the radius r = √81 = 9.",
    "citation": "College Board Digital SAT® Math Specifications — Additional Topics: Circle Equations in the Coordinate Plane"
  },
  {
    "id": "sat-m-517",
    "type": "mcq",
    "subtopic": "Additional Topics: Right Triangle Trigonometric Identity",
    "difficulty": "Medium",
    "question": "In right triangle ABC, angle C is 90°. If sin(A) = 7/25, what is the value of cos(B)?",
    "options": ["7/25", "24/25", "25/7", "24/7"],
    "answer": 0,
    "explanation": "In a right triangle where C = 90°, angles A and B are complementary (A + B = 90°). By the co-function identity, sin(A) = cos(90° - A) = cos(B). Thus, cos(B) = 7/25.",
    "citation": "College Board Digital SAT® Math Specifications — Additional Topics: Right Triangle Trigonometry"
  },
  {
    "id": "sat-m-518",
    "type": "mcq",
    "subtopic": "Additional Topics: Arc Length of a Circle",
    "difficulty": "Hard",
    "question": "A circle has a radius of 12 cm. What is the length of an arc intercepted by a central angle of 75°?",
    "options": ["5π cm", "10π cm", "2.5π cm", "15π cm"],
    "answer": 0,
    "explanation": "Arc length s = 2πr * (θ / 360°). With r = 12 and θ = 75°: s = 2π(12) * (75/360) = 24π * (5/24) = 5π cm.",
    "citation": "College Board Digital SAT® Math Specifications — Additional Topics: Radians and Sector Arc Lengths"
  },
  {
    "id": "sat-m-519",
    "type": "mcq",
    "subtopic": "Additional Topics: Complex Numbers",
    "difficulty": "Medium",
    "question": "If i = √(-1), which of the following is equivalent to (4 + 3i)(2 - 5i)?",
    "options": ["23 - 14i", "8 - 14i", "23 + 14i", "-7 - 14i"],
    "answer": 0,
    "explanation": "Expand using FOIL: 4(2) + 4(-5i) + 3i(2) + 3i(-5i) = 8 - 20i + 6i - 15(i^2). Since i^2 = -1, -15(i^2) = +15. Combine real and imaginary terms: (8 + 15) + (-20i + 6i) = 23 - 14i.",
    "citation": "College Board Digital SAT® Math Specifications — Additional Topics: Complex Number Arithmetic"
  },
  {
    "id": "sat-m-520",
    "type": "mcq",
    "subtopic": "Additional Topics: Similar Triangle Ratios",
    "difficulty": "Hard",
    "question": "Triangle PQR is similar to triangle STU, where vertices P, Q, and R correspond to S, T, and U, respectively. The length of PQ is 15 cm and the length of ST is 25 cm. If the area of triangle PQR is 54 cm^2, what is the area of triangle STU?",
    "options": ["150 cm^2", "90 cm^2", "125 cm^2", "180 cm^2"],
    "answer": 0,
    "explanation": "Scale factor k of side lengths is ST / PQ = 25 / 15 = 5/3. The ratio of areas of similar geometric figures is the square of the linear scale factor: Area_STU / Area_PQR = (5/3)^2 = 25/9. Area_STU = 54 * (25/9) = 6 * 25 = 150 cm^2.",
    "citation": "College Board Digital SAT® Math Specifications — Additional Topics: Geometric Proportions and Similar Figures"
  }
]

# ==============================================================================
# DIGITAL SAT READING & WRITING SET 05 (20 Questions - High-Percentile Comprehensive)
# ==============================================================================
sat_reading_set5 = [
  {
    "id": "sat-rw-501",
    "type": "mcq",
    "subtopic": "Craft & Structure: Words in Context",
    "difficulty": "Medium",
    "question": "Text:\nEcologists long assumed that microbial biodiversity in extreme alpine tundra was uniform across elevations. However, recent soil sequencing revealed that microclimates create highly _______ microbial niches, resulting in stark biological variations over distances of merely a few meters.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["heterogeneous", "immutable", "ephemeral", "quiescent"],
    "answer": 0,
    "explanation": "'Heterogeneous' means diverse in character or content. The passage contrasts the previous belief of 'uniform' microbial biodiversity with 'stark biological variations,' requiring a word meaning varied or diverse.",
    "citation": "College Board Digital SAT® Reading & Writing — Craft & Structure: Words in Context"
  },
  {
    "id": "sat-rw-502",
    "type": "mcq",
    "subtopic": "Craft & Structure: Words in Context",
    "difficulty": "Hard",
    "question": "Text:\nWhile early architectural theorists praised modern concrete facades for their austere purity, subsequent urban critics condemned such surfaces as cold and forbidding, claiming they _______ pedestrian warmth and discouraged civic engagement.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["stifled", "bolstered", "heralded", "reconciled"],
    "answer": 0,
    "explanation": "The context describes critics viewing concrete as 'cold and forbidding' and discouraging civic engagement. 'Stifled' (suppressed, smothered, or held back) logically describes how these surfaces diminished pedestrian warmth.",
    "citation": "College Board Digital SAT® Reading & Writing — Craft & Structure: Words in Context"
  },
  {
    "id": "sat-rw-503",
    "type": "mcq",
    "subtopic": "Craft & Structure: Text Structure & Purpose",
    "difficulty": "Hard",
    "question": "Text:\nIn classical economic theory, consumers are presumed to act as rational utility-maximizers possessing comprehensive market knowledge. Behavioral economists, however, have documented persistent cognitive biases, such as loss aversion and anchoring, which cause systematic deviations from theoretical optimization.\n\nWhich choice best describes the primary function of the second sentence?",
    "options": [
      "It introduces empirical counter-evidence that challenges a foundational premise described in the first sentence.",
      "It provides concrete examples that corroborate the theoretical framework outlined in the first sentence.",
      "It proposes an irreconcilable philosophical conflict between two historical economic schools.",
      "It outlines a methodological compromise capable of synthesizing both approaches."
    ],
    "answer": 0,
    "explanation": "The first sentence presents the classical economic assumption of rational consumers. The second sentence uses 'however' to introduce behavioral economics findings (cognitive biases, loss aversion) that systematically challenge and contradict this classical model.",
    "citation": "College Board Digital SAT® Reading & Writing — Craft & Structure: Text Structure and Purpose"
  },
  {
    "id": "sat-rw-504",
    "type": "mcq",
    "subtopic": "Craft & Structure: Cross-Text Paired Connections",
    "difficulty": "Hard",
    "question": "Text 1:\nAstrophysicist Dr. Vance argues that lunar dust presents the single greatest technical obstacle to establishing permanent human settlements on the Moon. Its abrasive, electrostatically charged particles erode spacesuit joints and damage optical sensors.\n\nText 2:\nDr. Nguyen acknowledges that lunar regolith poses mechanical challenges, but points out that recent advances in passive electrostatic shielding and self-cleaning ceramic nanocoatings have effectively neutralized particulate infiltration in simulated vacuum testing.\n\nBased on the texts, how would Dr. Nguyen (Text 2) most likely respond to Dr. Vance's perspective (Text 1)?",
    "options": [
      "By asserting that technological innovations are actively solving the abrasive particle hazards highlighted by Dr. Vance.",
      "By denying that lunar regolith particles possess electrostatic charges or abrasive qualities.",
      "By suggesting that optical sensors are unnecessary for long-term lunar habitats.",
      "By claiming that radiation presents a far more severe settlement danger than surface regolith."
    ],
    "answer": 0,
    "explanation": "Text 1 claims lunar dust is the greatest obstacle due to its abrasiveness. Text 2 agrees with the mechanical challenge, but points to successful electrostatic shielding and nanocoatings in vacuum tests that neutralize particulate infiltration.",
    "citation": "College Board Digital SAT® Reading & Writing — Craft & Structure: Cross-Text Connections"
  },
  {
    "id": "sat-rw-505",
    "type": "mcq",
    "subtopic": "Information & Ideas: Central Ideas",
    "difficulty": "Medium",
    "question": "Text:\nWhen trees undergo severe drought stress, tiny air bubbles form inside their xylem conduits—a destructive phenomenon known as cavitation. If cavitation spreads unchecked throughout the vascular network, the plant loses its hydraulic conductance and perishes. Certain desert shrubs, however, possess narrow xylem vessels with reinforced cell walls that resist high negative pressures, allowing them to sustain fluid transport under hyper-arid conditions.\n\nWhich choice best expresses the main idea of the text?",
    "options": [
      "Specialized anatomical adaptations in xylem vessel structure enable certain arid-adapted plants to survive hydraulic cavitation caused by drought.",
      "Cavitation is an inevitable environmental disaster that uniformly threatens all terrestrial vegetation during dry periods.",
      "Desert vegetation survives primarily by eliminating vascular water transport during seasonal periods of extreme heat.",
      "Air bubble formation in xylem conduits enhances nutrient absorption in hyper-arid botanical ecosystems."
    ],
    "answer": 0,
    "explanation": "The passage outlines the danger of cavitation (air bubbles breaking water transport) and highlights how desert shrubs survive through narrow xylem vessels with reinforced cell walls that maintain fluid transport under extreme tension.",
    "citation": "College Board Digital SAT® Reading & Writing — Information & Ideas: Central Ideas and Details"
  },
  {
    "id": "sat-rw-506",
    "type": "mcq",
    "subtopic": "Information & Ideas: Command of Textual Evidence",
    "difficulty": "Hard",
    "question": "Text:\nIn a study of avian foraging behavior, researcher Elena Ruiz hypothesized that urban crows have adapted their tool-use techniques to exploit artificial food containers discarded by humans, exhibiting higher novel problem-solving rates than their rural counterparts.\n\nWhich finding, if true, would most directly support Ruiz's hypothesis?",
    "options": [
      "Urban crows successfully unlatched synthetic container prototypes in 72% of trials, whereas rural crows only succeeded in 19% of trials under identical conditions.",
      "Urban crows and rural crows exhibited nearly identical completion times when foraging for naturally occurring beetle larvae in soil.",
      "Rural crows possessed larger body sizes and longer beak dimensions than urban crows.",
      "Urban crows produced more vocal warning alarms in the presence of domestic predators than rural crows."
    ],
    "answer": 0,
    "explanation": "Ruiz's hypothesis is specifically that urban crows exhibit higher novel problem-solving rates with artificial food containers compared to rural crows. Showing 72% success for urban crows vs 19% for rural crows directly validates this hypothesis.",
    "citation": "College Board Digital SAT® Reading & Writing — Information & Ideas: Command of Textual Evidence"
  },
  {
    "id": "sat-rw-507",
    "type": "mcq",
    "subtopic": "Information & Ideas: Command of Quantitative Evidence",
    "difficulty": "Medium",
    "question": "Data Summary:\nAnnual Carbon Sequestration by Ecosystem Type (Metric Tons per Hectare):\n- Mangrove Forests: 10.2\n- Seagrass Meadows: 8.4\n- Temperate Deciduous Forests: 3.1\n- Boreal Coniferous Forests: 1.5\n\nA marine conservation analyst claims that coastal marine wetland habitats capture atmospheric carbon at rates significantly greater than major terrestrial forest biomes.\n\nWhich choice best describes how the data in the summary support the analyst's claim?",
    "options": [
      "Mangrove forests and seagrass meadows sequester over double the carbon per hectare of temperate deciduous and boreal forests.",
      "Boreal coniferous forests sequester more carbon per hectare than temperate deciduous forests.",
      "Seagrass meadows sequester less carbon than any other habitat evaluated in the survey.",
      "Terrestrial forest biomes capture the majority of global atmospheric carbon emissions."
    ],
    "answer": 0,
    "explanation": "Marine coastal wetlands (mangroves at 10.2 and seagrass at 8.4) sequester 10.2 and 8.4 MT/ha, which is more than double temperate forests (3.1) and boreal forests (1.5), directly substantiating the claim.",
    "citation": "College Board Digital SAT® Reading & Writing — Information & Ideas: Command of Quantitative Evidence"
  },
  {
    "id": "sat-rw-508",
    "type": "mcq",
    "subtopic": "Information & Ideas: Inferences",
    "difficulty": "Hard",
    "question": "Text:\nMicrobial fuel cells (MFCs) generate electricity by using bacteria to oxidize organic compounds in wastewater. However, conventional MFC anodes made of bare carbon cloth suffer from low electron transfer efficiency due to poor biocompatibility with bacterial biofilms. When chemical engineers functionalized carbon cloth anodes with graphene oxide nanoparticles, biofilm adhesion increased threefold and electrical power output increased by 240%.\n\nIt can reasonably be inferred from the text that _______.",
    "options": [
      "improving the biochemical interface between the anode and bacterial colonies is critical to increasing power generation in MFCs",
      "graphene oxide nanoparticles actively eradicate bacteria in contaminated wastewater systems",
      "bare carbon cloth remains the most cost-effective substrate for commercial industrial wastewater treatment",
      "microbial fuel cells will completely replace fossil fuel electrical power generation within the next decade"
    ],
    "answer": 0,
    "explanation": "The text explains that poor biocompatibility between the anode and bacteria hindered electron transfer, and that enhancing biofilm adhesion via graphene oxide boosted power output by 240%. Therefore, improving this interface is critical to electrical power output.",
    "citation": "College Board Digital SAT® Reading & Writing — Information & Ideas: Inferences"
  },
  {
    "id": "sat-rw-509",
    "type": "mcq",
    "subtopic": "Standard English Conventions: Sentence Boundaries",
    "difficulty": "Hard",
    "question": "Text:\nIn 1910, geneticist Thomas Hunt Morgan discovered a white-eyed male fruit fly among thousands of red-eyed _______ this landmark observation provided the first empirical proof that specific genes reside on specific chromosomes.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["specimens; and", "specimens, and", "specimens, this", "specimens this"],
    "answer": 1,
    "explanation": "Both clauses are independent clauses ('In 1910, geneticist Thomas Hunt Morgan discovered...' and 'this landmark observation provided...'). Connecting two independent clauses requires a comma with a coordinating conjunction (', and') or a semicolon alone. 'specimens, and' correctly coordinates the two clauses.",
    "citation": "College Board Digital SAT® Reading & Writing — Standard English Conventions: Boundaries"
  },
  {
    "id": "sat-rw-510",
    "type": "mcq",
    "subtopic": "Standard English Conventions: Punctuation with Nonessential Clauses",
    "difficulty": "Medium",
    "question": "Text:\nDr. Chien-Shiung Wu _______ a pioneering nuclear physicist nicknamed 'the First Lady of Physics' _______ conducted the Wu experiment in 1956, disproving the conservation of parity in weak nuclear interactions.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      "—a pioneering nuclear physicist nicknamed 'the First Lady of Physics'—",
      "—a pioneering nuclear physicist nicknamed 'the First Lady of Physics',",
      ", a pioneering nuclear physicist nicknamed 'the First Lady of Physics'—",
      ": a pioneering nuclear physicist nicknamed 'the First Lady of Physics':"
    ],
    "answer": 0,
    "explanation": "The appositive phrase ('a pioneering nuclear physicist nicknamed...') is a nonessential modifier. Nonessential parenthetical elements must be set off with matching punctuation marks on both sides (two commas, two parentheses, or two em-dashes). Option 0 uses matching em-dashes.",
    "citation": "College Board Digital SAT® Reading & Writing — Standard English Conventions: Punctuation"
  },
  {
    "id": "sat-rw-511",
    "type": "mcq",
    "subtopic": "Standard English Conventions: Subject-Verb Agreement",
    "difficulty": "Medium",
    "question": "Text:\nThe discovery of hydrothermal vent ecosystems along oceanic spreading ridges _______ marine biologists to reconsider the thermodynamic limits of multicellular life.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["has prompted", "have prompted", "are prompting", "were prompting"],
    "answer": 0,
    "explanation": "The subject of the sentence is the singular noun phrase 'The discovery' (not 'vent ecosystems' or 'spreading ridges', which are objects of prepositions). A singular subject takes a singular verb: 'has prompted'.",
    "citation": "College Board Digital SAT® Reading & Writing — Standard English Conventions: Agreement"
  },
  {
    "id": "sat-rw-512",
    "type": "mcq",
    "subtopic": "Standard English Conventions: Modifier Placement",
    "difficulty": "Hard",
    "question": "Text:\nHaving synthesized thousands of astronomical spectra using deep neural networks, _______.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      "the computational research team identified forty previously undetected exoplanet candidates",
      "forty previously undetected exoplanet candidates were identified by the computational research team",
      "the identification of forty previously undetected exoplanet candidates astonished astronomers",
      "astronomers were astonished by forty previously undetected exoplanet candidates"
    ],
    "answer": 0,
    "explanation": "The introductory participial phrase 'Having synthesized thousands of astronomical spectra...' must logically modify the subject immediately following the comma. The entity that synthesized the spectra is 'the computational research team' (not the exoplanets or the identification).",
    "citation": "College Board Digital SAT® Reading & Writing — Standard English Conventions: Modifier Placement"
  },
  {
    "id": "sat-rw-513",
    "type": "mcq",
    "subtopic": "Standard English Conventions: Verb Tense & Aspect",
    "difficulty": "Medium",
    "question": "Text:\nBy the time the James Webb Space Telescope reached its Sun-Earth L2 Lagrange point in January 2022, engineers _______ over two decades designing and testing its segmented beryllium mirrors.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["had spent", "have spent", "will spend", "spend"],
    "answer": 0,
    "explanation": "The time marker 'By the time... [past action in 2022]' indicates an action completed prior to another past event. This past-before-past relationship requires the past perfect tense ('had spent').",
    "citation": "College Board Digital SAT® Reading & Writing — Standard English Conventions: Verb Tense"
  },
  {
    "id": "sat-rw-514",
    "type": "mcq",
    "subtopic": "Standard English Conventions: Colons",
    "difficulty": "Medium",
    "question": "Text:\nArchitect Zaha Hadid utilized fluid parametric curves to evoke the natural dynamics of water _______ undulating waves, converging currents, and cascading streams.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [":", ";", ",", "—and"],
    "answer": 0,
    "explanation": "A colon is used after an independent clause ('Architect Zaha Hadid utilized fluid parametric curves to evoke the natural dynamics of water') to introduce an illustrative list or elaboration ('undulating waves, converging currents...').",
    "citation": "College Board Digital SAT® Reading & Writing — Standard English Conventions: Punctuation"
  },
  {
    "id": "sat-rw-515",
    "type": "mcq",
    "subtopic": "Expression of Ideas: Transitions",
    "difficulty": "Medium",
    "question": "Text:\nCommercial passenger aircraft wings are intentionally engineered with substantial structural flexibility to safely absorb turbulence. _______, when encountering severe thermal downdrafts, the wingtips of a Boeing 787 can flex upward by nearly twenty feet without structural failure.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["For instance", "In contrast", "Nevertheless", "Meanwhile"],
    "answer": 0,
    "explanation": "The first sentence introduces the general principle that wings are engineered with flexibility. The second sentence provides a specific, concrete example of this principle in action (the Boeing 787 flexing 20 feet). 'For instance' correctly signals an illustrative example.",
    "citation": "College Board Digital SAT® Reading & Writing — Expression of Ideas: Transitions"
  },
  {
    "id": "sat-rw-516",
    "type": "mcq",
    "subtopic": "Expression of Ideas: Transitions",
    "difficulty": "Hard",
    "question": "Text:\nAdvocates of active optical camouflage cite its potential to render terrestrial military vehicles virtually undetectable to enemy spotters. _______, maintaining the immense power supply and thermal dissipation systems required by light-emitting panels remains a formidable engineering bottleneck in field environments.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["However", "Furthermore", "Accordingly", "Similarly"],
    "answer": 0,
    "explanation": "The first sentence outlines the promising capability of active optical camouflage. The second sentence introduces a major drawback/obstacle (power supply and thermal dissipation bottlenecks). 'However' correctly signals this contrast.",
    "citation": "College Board Digital SAT® Reading & Writing — Expression of Ideas: Transitions"
  },
  {
    "id": "sat-rw-517",
    "type": "mcq",
    "subtopic": "Expression of Ideas: Transitions",
    "difficulty": "Medium",
    "question": "Text:\nIn arid soils, mycorrhizal fungal networks establish symbiotic relationships with plant roots, transporting phosphorus in exchange for plant-synthesized carbohydrates. _______, the microscopic fungal hyphae bind fine soil particles together, significantly reducing wind erosion.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["Additionally", "Consequently", "Rather", "Otherwise"],
    "answer": 0,
    "explanation": "The first sentence explains one benefit of mycorrhizal fungi (nutrient transport). The second sentence provides a second, additive ecological benefit (soil particle binding and erosion prevention). 'Additionally' correctly marks the addition of a complementary point.",
    "citation": "College Board Digital SAT® Reading & Writing — Expression of Ideas: Transitions"
  },
  {
    "id": "sat-rw-518",
    "type": "mcq",
    "subtopic": "Expression of Ideas: Rhetorical Synthesis",
    "difficulty": "Hard",
    "question": "Notes:\n- The Svalbard Global Seed Vault is located on the Norwegian island of Spitsbergen.\n- It was established in 2008 as a long-term backup repository for the world's crop diversity.\n- It is buried 120 meters inside a sandstone mountain surrounded by permafrost.\n- The facility maintains an ambient temperature of -18°C, preserving seeds for centuries even during a power outage.\n\nThe student wants to emphasize the facility's geological and climatic security features. Which choice most effectively uses relevant information from the notes to accomplish this goal?",
    "options": [
      "Buried 120 meters inside a permafrost-encased sandstone mountain, the Svalbard Global Seed Vault naturally preserves seeds at -18°C even in the event of power loss.",
      "Established in 2008 on the Norwegian island of Spitsbergen, the Svalbard Global Seed Vault backs up the world's crop diversity.",
      "The Svalbard Global Seed Vault, located in Norway, was created in 2008 to protect global agriculture.",
      "Preserving crop diversity is critical for global agriculture, as shown by the Svalbard Global Seed Vault."
    ],
    "answer": 0,
    "explanation": "The goal is specifically to emphasize geological and climatic security features. Option 0 directly highlights being buried 120 meters inside a permafrost mountain and maintaining -18°C without power.",
    "citation": "College Board Digital SAT® Reading & Writing — Expression of Ideas: Rhetorical Synthesis"
  },
  {
    "id": "sat-rw-519",
    "type": "mcq",
    "subtopic": "Expression of Ideas: Rhetorical Synthesis",
    "difficulty": "Hard",
    "question": "Notes:\n- The Voynich manuscript is an illustrated codex hand-written in an unknown writing system.\n- Carbon dating by the University of Arizona determined the vellum was created between 1404 and 1438.\n- Despite cryptanalytic efforts by World War II codebreakers and modern supercomputers, the text remains un-deciphered.\n\nThe student wants to emphasize the persistent mystery of the manuscript despite extensive historical and modern analysis. Which choice most effectively uses relevant information from the notes to accomplish this goal?",
    "options": [
      "Although carbon-dated to the early 15th century and examined by both World War II codebreakers and supercomputers, the Voynich manuscript remains completely un-deciphered.",
      "The Voynich manuscript is an illustrated 15th-century codex inscribed in an unknown writing system on animal vellum.",
      "Scientists at the University of Arizona used carbon dating to estimate that the Voynich manuscript was created between 1404 and 1438.",
      "World War II codebreakers analyzed historical illustrated manuscripts including the Voynich codex."
    ],
    "answer": 0,
    "explanation": "Option 0 directly contrasts the thorough historical analysis (World War II codebreakers) and modern analysis (supercomputers) with its lingering status ('remains completely un-deciphered').",
    "citation": "College Board Digital SAT® Reading & Writing — Expression of Ideas: Rhetorical Synthesis"
  },
  {
    "id": "sat-rw-520",
    "type": "mcq",
    "subtopic": "Craft & Structure: Words in Context",
    "difficulty": "Hard",
    "question": "Text:\nRather than displaying the unyielding, dogmatic certainty common among early political manifestos, the philosopher's treatise was remarkably _______, openly conceding gaps in its empirical data and inviting collaborative revision.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["modest", "trenchant", "imperious", "pugnacious"],
    "answer": 0,
    "explanation": "The text contrasts 'unyielding, dogmatic certainty' with a treatise that 'openly conceded gaps in its empirical data and invited collaborative revision.' The word 'modest' (unassuming, moderate, humble in estimation of oneself) fits this context perfectly.",
    "citation": "College Board Digital SAT® Reading & Writing — Craft & Structure: Words in Context"
  }
]

# Write SAT Math Set 5
with open(os.path.join(US_DATA_SAT, "digital_sat_math_set5.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_math_set5}, f, indent=2, ensure_ascii=False)
print("Generated digital_sat_math_set5.json successfully (20 Qs)!")

# Write SAT Reading Set 5
with open(os.path.join(US_DATA_SAT, "digital_sat_reading_set5.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_reading_set5}, f, indent=2, ensure_ascii=False)
print("Generated digital_sat_reading_set5.json successfully (20 Qs)!")
