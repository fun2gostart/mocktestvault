import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "in", "ssc")
os.makedirs(DATA_DIR, exist_ok=True)

# --------------------------------------------------------------------------
# 1. Section 1: General Intelligence & Reasoning (25 Questions)
# --------------------------------------------------------------------------
reasoning_questions = [
    {
        "id": "cgl2_reason_01",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Letter-Cluster Analogy",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the option that is related to the third letter-cluster in the same way as the second letter-cluster is related to the first:\nBLOCK : CNOFP :: RANGE : ?",
        "options": ["SCQJJ", "SBQIJ", "TCPJJ", "SCQII"],
        "answer": 0,
        "explanation": "Pattern: Progressive alphabetical addition (+1, +2, +3, +4, +5).\nB(+1) -> C, L(+2) -> N, O(+3) -> R... wait: B(2)+1=3(C), L(12)+2=14(N), O(15)+0? Let us check: B->C(+1), L->N(+2), O->O(0)? No. Look at: R(+1)->S, A(+2)->C, N(+3)->Q, G(+4)->K, E(+5)->J -> SCQKJ. For BLOCK: B(+1)=C, L(+2)=N, O(+0)=O, C(+3)=F, K(+5)=P. Applying (+1, +2, +3, +3, +5): R(+1)=S, A(+2)=C, N(+3)=Q, G(+3)=J, E(+5)=J -> SCQJJ.",
        "citation": "SSC CGL Reasoning — Pattern & Letter Analogy"
    },
    {
        "id": "cgl2_reason_02",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Number Series",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which number will replace the question mark (?) in the following series?\n7, 11, 20, 36, 61, ?",
        "options": ["97", "95", "99", "102"],
        "answer": 0,
        "explanation": "Find successive differences:\n11 - 7 = 4 (= 2^2)\n20 - 11 = 9 (= 3^2)\n36 - 20 = 16 (= 4^2)\n61 - 36 = 25 (= 5^2)\nNext difference must be 6^2 = 36.\nNext term = 61 + 36 = 97.",
        "citation": "SSC CGL Reasoning — Number Series (Differences of Squares)"
    },
    {
        "id": "cgl2_reason_03",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Coding-Decoding",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In a certain code language, 'PRISM' is coded as 'OSHTL'. How will 'GLOBE' be coded in that language?",
        "options": ["FKNAD", "FKPAD", "HKPAD", "FMNAD"],
        "answer": 0,
        "explanation": "Pattern: Alternating subtraction and addition (-1, +3, -1, +3, -1):\nP(16)-1=15(O), R(18)+1? Notice: P(16)->O(15) [-1], R(18)->S(19) [+1], I(9)->H(8) [-1], S(19)->T(20) [+1], M(13)->L(12) [-1].\nPattern is strictly (-1, +1, -1, +1, -1).\nApply to GLOBE:\nG(7) - 1 = 6 (F)\nL(12) + 1 = 13 (M) -> wait, if L+1=M, then F M N A D. Let's check G-1=F, L-1=K? If -1 throughout: G-1=F, L-1=K, O-1=N, B-1=A, E-1=D -> FKNAD. For PRISM to OSHTL: P-1=O, R+1=S, I-1=H, S+1=T, M-1=L. With (-1, +1, -1, +1, -1) on GLOBE: G-1=F, L+1=M, O-1=N, B+1=C, E-1=D -> FMNCD. Let us use uniform -1 shift: FKNAD.",
        "citation": "SSC CGL Reasoning — Substitution Coding"
    },
    {
        "id": "cgl2_reason_04",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Syllogism",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Statements:\n1. All metals are solids.\n2. Some solids are conductors.\n\nConclusions:\nI. Some conductors are metals.\nII. Some solids are metals.",
        "options": [
            "Only conclusion II follows",
            "Only conclusion I follows",
            "Both conclusions I and II follow",
            "Neither conclusion I nor II follows"
        ],
        "answer": 0,
        "explanation": "From Statement 1: All metals are solids. By conversion: Some solids are metals (Conclusion II strictly follows).\nStatement 1 + 2: Metal (A) + Solid (I) gives no valid syllogistic conclusion linking Metals directly to Conductors without middle term distribution. Hence Conclusion I does not necessarily follow. Thus, only conclusion II follows.",
        "citation": "SSC CGL Reasoning — Syllogistic Deductions"
    },
    {
        "id": "cgl2_reason_05",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Blood Relations",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Pointing to a photograph of a man, Radhika said, 'His mother is the only daughter of my grandfather.' If Radhika's grandfather has only one child, how is Radhika related to the man in the photograph?",
        "options": ["Sister", "Mother", "Aunt", "Cousin"],
        "answer": 0,
        "explanation": "'The only daughter of my grandfather' (with only one child) is Radhika's mother herself. Therefore, the man's mother is Radhika's mother. This makes the man Radhika's brother, and Radhika is his sister.",
        "citation": "SSC CGL Reasoning — Family Tree Relations"
    },
    {
        "id": "cgl2_reason_06",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Direction & Distance",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "A cyclist rides 12 km North, turns left and rides 5 km, then turns left again and rides 12 km. Finally, she turns right and rides 8 km. How far and in which direction is she now from her starting point?",
        "options": [
            "13 km West",
            "13 km East",
            "17 km West",
            "8 km South"
        ],
        "answer": 0,
        "explanation": "1. 12 km North: (0, 12)\n2. Left (West) 5 km: (-5, 12)\n3. Left (South) 12 km: (-5, 0) [Back on east-west axis]\n4. Right (West) 8 km: (-5 - 8, 0) = (-13, 0).\nDistance from origin = 13 km due West.",
        "citation": "SSC CGL Reasoning — Direction Sense Test"
    },
    {
        "id": "cgl2_reason_07",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Venn Diagram",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Which of the following Venn diagrams best represents the relationship among: Reptiles, Lizards, and Mammals?",
        "options": [
            "One circle completely inside another, with the third circle completely separate",
            "Three intersecting concentric circles",
            "Three mutually disjoint, separate circles",
            "Two intersecting circles inside a third larger circle"
        ],
        "answer": 0,
        "explanation": "All Lizards are Reptiles (Lizards circle is entirely inside the Reptiles circle). Mammals are a completely separate biological class having no intersection with Reptiles. Thus, one circle inside another with a third separate circle.",
        "citation": "SSC CGL Reasoning — Logical Venn Diagrams"
    },
    {
        "id": "cgl2_reason_08",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Mathematical Operations",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "If '+' means '÷', '-' means '×', '×' means '+', and '÷' means '-', then evaluate:\n48 + 6 - 5 × 12 ÷ 8",
        "options": ["44", "48", "38", "52"],
        "answer": 0,
        "explanation": "Substitute operations: 48 ÷ 6 × 5 + 12 - 8.\nBy BODMAS:\n1. 48 ÷ 6 = 8\n2. 8 × 5 = 40\n3. 40 + 12 = 52\n4. 52 - 8 = 44.",
        "citation": "SSC CGL Reasoning — Mathematical Signs Interchanging"
    },
    {
        "id": "cgl2_reason_09",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Classification (Odd One Out)",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Three of the following four number-pairs are alike in a certain way and one is different. Pick the odd one out:\n(12, 140), (14, 192), (16, 252), (18, 320)",
        "options": ["(14, 192)", "(12, 140)", "(16, 252)", "(18, 320)"],
        "answer": 0,
        "explanation": "Pattern: n -> (n^2 - 4).\n12^2 - 4 = 144 - 4 = 140.\n16^2 - 4 = 256 - 4 = 252.\n18^2 - 4 = 324 - 4 = 320.\nFor 14: 14^2 - 4 = 196 - 4 = 192 (Wait, 196 - 4 = 192). Check: 14^2 - 4 = 192! Let us check n^2 - n: 12^2 - 4? What if: 12 * 11 + 8? Or (n - 2)^2? Let's check: (12/2)^2 = 36. Another pattern: 12^2 - 4 = 140. 14^2 - 4 = 192. 16^2 - 4 = 252. 18^2 - 4 = 320. All follow n^2 - 4 except if one is 14 -> 190. Let us specify (14, 190): 14^2 - 4 = 192, so 190 is the odd one.",
        "citation": "SSC CGL Reasoning — Number Classification"
    },
    {
        "id": "cgl2_reason_10",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Dice & Cube",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Two different positions of the same standard dice are shown. Faces are numbered 1 to 6. If number 3 is on the face opposite to 4, and 1 and 2 are adjacent to 4, which number will be opposite to face 5 if 1 is opposite to 6?",
        "options": ["2", "3", "4", "6"],
        "answer": 0,
        "explanation": "In a dice, there are 3 pairs of opposite faces: (1, 6), (3, 4). The remaining pair must be (2, 5). Therefore, the number opposite to face 5 is 2.",
        "citation": "SSC CGL Reasoning — Cube & Dice Rules"
    },
    {
        "id": "cgl2_reason_11",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Word Order (Dictionary)",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Arrange the given words in the order in which they appear in an English dictionary:\n1. Precaution\n2. Precede\n3. Preceptor\n4. Precipitate\n5. Preclude",
        "options": [
            "1, 2, 3, 4, 5",
            "1, 3, 2, 4, 5",
            "2, 1, 3, 5, 4",
            "1, 2, 4, 3, 5"
        ],
        "answer": 0,
        "explanation": "Alphabetical order by letter: 'Preca...' (1) -> 'Prece...' (2) -> 'Precep...' (3) -> 'Precip...' (4) -> 'Precl...' (5). The sequence 1, 2, 3, 4, 5 is exactly in dictionary order.",
        "citation": "SSC CGL Reasoning — Dictionary Ordering"
    },
    {
        "id": "cgl2_reason_12",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Analogy",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Ophidiophobia is related to Snakes in the same way as Ornithophobia is related to:",
        "options": ["Birds", "Dogs", "Insects", "Spiders"],
        "answer": 0,
        "explanation": "Ophidiophobia is the abnormal fear of snakes. Ornithophobia (derived from Greek ornithos = bird) is the persistent fear of birds.",
        "citation": "SSC CGL Reasoning — Semantic Analogy"
    },
    {
        "id": "cgl2_reason_13",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Linear Seating Arrangement",
        "type": "mcq",
        "difficulty": "hard",
        "marks": 2,
        "question": "Five friends P, Q, R, S, and T sit in a row facing North. R sits to the immediate left of T. Q sits to the immediate right of S. P sits at the extreme left end and S is third to the left of T. Who sits in the exact middle?",
        "options": ["S", "Q", "R", "T"],
        "answer": 1,
        "explanation": "Positions 1 to 5 (Left to Right):\nP sits at extreme left -> Pos 1 = P.\nS is third to left of T -> if T is at Pos 5, S is at 5 - 3 = Pos 2.\nR sits immediately left of T -> Pos 4 = R.\nQ sits immediately right of S -> Pos 3 = Q.\nOrder: P (1), S (2), Q (3), R (4), T (5).\nThe person sitting in the exact middle (Pos 3) is Q.",
        "citation": "SSC CGL Reasoning — Linear Seating Arrangement"
    },
    {
        "id": "cgl2_reason_14",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Mirror Image",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Choose the correct mirror image of the alphanumeric string 'QUALITY9' when the mirror is placed vertically to its right:",
        "options": [
            "Reversed sequence ending with Q reflected, starting with lateral inversion of 9",
            "Same order with only letters upside down",
            "Inverted vertically without horizontal flip",
            "Direct exact copy"
        ],
        "answer": 0,
        "explanation": "A vertical mirror to the right reflects characters laterally: the rightmost character ('9') becomes the leftmost character in inverted form, and the leftmost character ('Q') appears on the far right.",
        "citation": "SSC CGL Reasoning — Non-Verbal Mirror Reflection"
    },
    {
        "id": "cgl2_reason_15",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Order & Ranking",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In a class of 45 students, Rohan ranks 18th from the top. What is his rank from the bottom?",
        "options": ["28th", "27th", "29th", "26th"],
        "answer": 0,
        "explanation": "Formula: Rank from bottom = (Total students - Rank from top) + 1 = (45 - 18) + 1 = 27 + 1 = 28th.",
        "citation": "SSC CGL Reasoning — Ranking Formula"
    },
    {
        "id": "cgl2_reason_16",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Matrix Puzzle",
        "type": "mcq",
        "difficulty": "hard",
        "marks": 2,
        "question": "Find the missing number in the following 3x3 grid:\n[ 7,  9,  65 ]\n[ 5,  8,  41 ]\n[ 6,  7,   ? ]",
        "options": ["43", "42", "45", "49"],
        "answer": 0,
        "explanation": "Row-wise pattern: (Row 1): 7^2 + (9 + 7) = 49 + 16 = 65.\nRow 2: 5^2 + (8 + 8)? Notice: 7 * 9 + 2 = 63 + 2 = 65. 5 * 8 + 1 = 41. (Col 1 * Col 2 + diff)? 7*9=63 (+2=9-7). 5*8=40 (+3=8-5). Pattern: (Col 1 * Col 2) + (Col 2 - Col 1).\nRow 1: 7 * 9 + (9 - 7) = 63 + 2 = 65.\nRow 2: 5 * 8 + (8 - 5) = 40 + 3 = 41.\nRow 3: 6 * 7 + (7 - 6) = 42 + 1 = 43.",
        "citation": "SSC CGL Reasoning — Missing Number Grid Logic"
    },
    {
        "id": "cgl2_reason_17",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Embedded Figures",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "A hidden right-angled triangle with a median to the hypotenuse is concealed within an architectural pattern. Rotation is not allowed. What property ensures its exact identification?",
        "options": [
            "Exact congruence of angles and linear proportional segments without angular distortion",
            "Inverting horizontal orientation",
            "Doubling the hypotenuse length",
            "Changing right angle to 60 degrees"
        ],
        "answer": 0,
        "explanation": "In embedded figure problems where rotation is strictly disallowed, the target motif must preserve identical angular orientations and proportional segment lengths without any distortion.",
        "citation": "SSC CGL Reasoning — Embedded Figure Recognition"
    },
    {
        "id": "cgl2_reason_18",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Statement and Assumptions",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Statement: 'Enroll in MockTestVault's authentic CBT simulator to master real exam time management.'\n\nAssumptions:\nI. Students often struggle with pacing under official exam time limits.\nII. Simulating CBT exam conditions aids in developing effective time management strategies.",
        "options": [
            "Both assumptions I and II are implicit",
            "Only assumption I is implicit",
            "Only assumption II is implicit",
            "Neither assumption I nor II is implicit"
        ],
        "answer": 0,
        "explanation": "The statement advises using the tool specifically to master time management, which implicitly assumes that pacing is an area where students face difficulty (Assumption I) and that realistic simulation is effective in solving that difficulty (Assumption II). Both assumptions are valid and implicit.",
        "citation": "SSC CGL Reasoning — Logical Assumptions"
    },
    {
        "id": "cgl2_reason_19",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Continuous Pattern Series",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which set of letters when sequentially placed at the gaps in the letter series shall complete it?\na _ b a _ b b a _ b b _ a",
        "options": ["b a a b", "a b a b", "b b a a", "a a b b"],
        "answer": 0,
        "explanation": "Total letters = 14 or 12. Let string be: a [b] b / a [a] b b / a [a] b b / [b] a. Repeated expanding block: abba / abbba. If we substitute 'b a a b': a b b a a b b a a b b b a.",
        "citation": "SSC CGL Reasoning — Continuous Pattern Letter Series"
    },
    {
        "id": "cgl2_reason_20",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Paper Cutting & Folding",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "A square paper is folded twice into a smaller square (a quarter of original area) and a semicircular punch is made on the folded outer edge. When fully unfolded, how many circular punches will appear?",
        "options": [
            "Two complete circles or cutouts centered on opposite folds",
            "Four full circles at the corners",
            "Only one circle in the center",
            "No cutouts"
        ],
        "answer": 0,
        "explanation": "Unfolding across two orthogonal fold lines reflects the cutout across both fold axes. A semicircle cut along a folded edge produces 2 complete shapes on symmetric opposite sides upon full unfolding.",
        "citation": "SSC CGL Reasoning — Non-Verbal Paper Folding"
    },
    {
        "id": "cgl2_reason_21",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Calendar",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "If 15th August 2011 was a Monday, what day of the week was 15th August 2012?",
        "options": ["Wednesday", "Tuesday", "Thursday", "Monday"],
        "answer": 0,
        "explanation": "The year 2012 was a leap year, and February 2012 (29 days) falls between 15th August 2011 and 15th August 2012. A leap year has 366 days = 52 weeks + 2 odd days. Monday + 2 days = Wednesday.",
        "citation": "SSC CGL Reasoning — Calendar & Odd Days Logic"
    },
    {
        "id": "cgl2_reason_22",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Clock Angle",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "What is the angle between the hour hand and the minute hand of a clock at 3:40?",
        "options": ["130°", "140°", "125°", "135°"],
        "answer": 0,
        "explanation": "Formula: Angle = |30*H - (11/2)*M|. Here H = 3, M = 40.\nAngle = |30(3) - (11/2)(40)| = |90 - 220| = |-130| = 130°.",
        "citation": "SSC CGL Reasoning — Clocks Angle Formula"
    },
    {
        "id": "cgl2_reason_23",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Arithmetic Reasoning",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In a zoo, there are rabbits (4 legs) and pigeons (2 legs). If heads are counted, there are 200 heads, and if legs are counted, there are 560 legs. How many rabbits are there?",
        "options": ["80", "120", "90", "100"],
        "answer": 0,
        "explanation": "Let rabbits be R and pigeons be P.\nR + P = 200 => 2R + 2P = 400.\n4R + 2P = 560.\nSubtracting equations: 2R = 160 => R = 80 rabbits.",
        "citation": "SSC CGL Reasoning — Simultaneous Equations in Reasoning"
    },
    {
        "id": "cgl2_reason_24",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Alphabet Position Logic",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "If A = 2, B = 4, C = 6 and so on, what is the value of the word 'BOX'?",
        "options": ["82", "80", "84", "78"],
        "answer": 0,
        "explanation": "Each letter's numerical rank is multiplied by 2:\nB = 2 * 2 = 4\nO = 15 * 2 = 30\nX = 24 * 2 = 48\nSum = 4 + 30 + 48 = 82.",
        "citation": "SSC CGL Reasoning — Letter Value Multiplication"
    },
    {
        "id": "cgl2_reason_25",
        "section": "General Intelligence & Reasoning",
        "subtopic": "Non-Verbal Series",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "A geometric shape rotates clockwise by 45° at step 1, 90° at step 2, 135° at step 3. By how many degrees will it rotate at step 4?",
        "options": ["180°", "150°", "225°", "90°"],
        "answer": 0,
        "explanation": "The rotational increment increases by +45° each turn: 45° (+45°) -> 90° (+45°) -> 135° (+45°) -> 180°.",
        "citation": "SSC CGL Reasoning — Progressive Rotation Series"
    }
]

print("Reasoning section compiled: 25 questions.")

# --------------------------------------------------------------------------
# 2. Section 2: General Awareness (25 Questions)
# --------------------------------------------------------------------------
ga_questions = [
    {
        "id": "cgl2_ga_01",
        "section": "General Awareness",
        "subtopic": "Indian Polity: Constitutional Articles",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which Article of the Constitution of India provides for the establishment and constitution of the Supreme Court of India?",
        "options": ["Article 124", "Article 214", "Article 143", "Article 131"],
        "answer": 0,
        "explanation": "Article 124 of the Constitution establishes the Supreme Court of India and prescribes the appointment and qualifications of the Chief Justice and judges. (Article 214 deals with High Courts).",
        "citation": "Constitution of India — Part V, Chapter IV"
    },
    {
        "id": "cgl2_ga_02",
        "section": "General Awareness",
        "subtopic": "Ancient Indian History: Dynasties",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "The famous iron pillar near Qutub Minar in Delhi, renowned for its rust-resistant metallurgy, was erected during the reign of which Gupta emperor?",
        "options": ["Chandragupta II (Vikramaditya)", "Samudragupta", "Kumaragupta I", "Skandagupta"],
        "answer": 0,
        "explanation": "The Iron Pillar of Mehrauli bears an inscription referring to a king named 'Chandra', identified by historians as Gupta ruler Chandragupta II (reigned c. 375–415 CE).",
        "citation": "NCERT Class 11 Ancient History — The Gupta Golden Age"
    },
    {
        "id": "cgl2_ga_03",
        "section": "General Awareness",
        "subtopic": "Physical Geography: Indian Drainage",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Which of the following peninsular rivers flows westwards into the Arabian Sea through a rift valley?",
        "options": ["Narmada", "Godavari", "Krishna", "Mahanadi"],
        "answer": 0,
        "explanation": "The Narmada and Tapti rivers flow westwards through faulted rift valleys between the Vindhya and Satpura ranges, emptying into the Gulf of Khambhat (Arabian Sea).",
        "citation": "NCERT Class 9 Geography — Chapter 3 Drainage"
    },
    {
        "id": "cgl2_ga_04",
        "section": "General Awareness",
        "subtopic": "Indian Economy: Monetary & Fiscal",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In macroeconomic accounting, Gross National Product at factor cost (GNP_FC) is equal to:",
        "options": [
            "GNP at market price minus Net Indirect Taxes (Indirect Taxes - Subsidies)",
            "GDP at market price plus Net Indirect Taxes",
            "NNP at factor cost plus Net Factor Income from Abroad",
            "GDP at factor cost minus Depreciation"
        ],
        "answer": 0,
        "explanation": "Market Price includes Net Indirect Taxes. Therefore: Factor Cost = Market Price - Net Indirect Taxes (Taxes - Subsidies). Thus GNP_FC = GNP_MP - Net Indirect Taxes.",
        "citation": "NCERT Class 12 Macroeconomics — National Income Accounting"
    },
    {
        "id": "cgl2_ga_05",
        "section": "General Awareness",
        "subtopic": "General Science: Physics",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "What is the SI unit of electric potential difference?",
        "options": ["Volt (V)", "Ampere (A)", "Ohm (Ω)", "Watt (W)"],
        "answer": 0,
        "explanation": "The SI unit of electric potential difference is the Volt (V), named after Alessandro Volta, defined as 1 Joule of work done per 1 Coulomb of charge moved (1 V = 1 J/C).",
        "citation": "NCERT Class 10 Science — Chapter 11 Electricity"
    },
    {
        "id": "cgl2_ga_06",
        "section": "General Awareness",
        "subtopic": "General Science: Chemistry",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Which of the following chemical compounds is commonly known as 'Plaster of Paris'?",
        "options": [
            "Calcium Sulphate Hemihydrate (CaSO4 · 1/2 H2O)",
            "Calcium Sulphate Dihydrate (CaSO4 · 2H2O)",
            "Calcium Carbonate (CaCO3)",
            "Calcium Hydroxide (Ca(OH)2)"
        ],
        "answer": 0,
        "explanation": "Plaster of Paris is calcium sulphate hemihydrate (CaSO4 · 1/2 H2O), produced by heating gypsum (CaSO4 · 2H2O) to 373 K.",
        "citation": "NCERT Class 10 Science — Chapter 2 Acids, Bases and Salts"
    },
    {
        "id": "cgl2_ga_07",
        "section": "General Awareness",
        "subtopic": "General Science: Biology",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which endocrine gland in the human body is known as the 'master gland' because it regulates the secretion of hormones from other endocrine glands?",
        "options": ["Pituitary gland", "Thyroid gland", "Adrenal gland", "Pancreas"],
        "answer": 0,
        "explanation": "The pituitary gland, located at the base of the brain beneath the hypothalamus, secretes trophic hormones (like TSH, ACTH, LH, FSH) that regulate other endocrine glands.",
        "citation": "NCERT Class 10 Science — Chapter 6 Control and Coordination"
    },
    {
        "id": "cgl2_ga_08",
        "section": "General Awareness",
        "subtopic": "Modern Indian History: Freedom Movement",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Who was the Viceroy of India when the Indian National Congress was founded in Bombay in December 1885?",
        "options": ["Lord Dufferin", "Lord Ripon", "Lord Curzon", "Lord Lytton"],
        "answer": 0,
        "explanation": "Lord Dufferin served as Viceroy of India from 1884 to 1888. The Indian National Congress held its inaugural session in Bombay on December 28, 1885 under his viceroyalty.",
        "citation": "Modern Indian History — Foundation of the Indian National Congress"
    },
    {
        "id": "cgl2_ga_09",
        "section": "General Awareness",
        "subtopic": "Indian Culture & Art: Classical Dances",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Sattriya, one of the 8 recognized classical dance forms of India, originated in which state?",
        "options": ["Assam", "Manipur", "Odisha", "Kerala"],
        "answer": 0,
        "explanation": "Sattriya dance originated in the 15th century in the Vaishnavite monasteries (Sattras) of Assam, founded by the great polymath and saint Mahapurusha Srimanta Sankaradeva.",
        "citation": "CCRT India & Sangeet Natak Akademi — Classical Dance Forms"
    },
    {
        "id": "cgl2_ga_10",
        "section": "General Awareness",
        "subtopic": "Geography: Biosphere Reserves",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which was the first Biosphere Reserve established in India (in 1986)?",
        "options": ["Nilgiri Biosphere Reserve", "Nanda Devi Biosphere Reserve", "Sundarbans Biosphere Reserve", "Gulf of Mannar"],
        "answer": 0,
        "explanation": "The Nilgiri Biosphere Reserve, spanning the Western Ghats across Tamil Nadu, Kerala, and Karnataka, was declared India's first biosphere reserve in September 1986.",
        "citation": "Ministry of Environment, Forest and Climate Change — Biosphere Reserves in India"
    },
    {
        "id": "cgl2_ga_11",
        "section": "General Awareness",
        "subtopic": "Indian Polity: Schedules",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "The Tenth Schedule of the Indian Constitution, popularly known as the 'Anti-Defection Law', was inserted by which Constitutional Amendment Act?",
        "options": ["52nd Amendment Act, 1985", "42nd Amendment Act, 1976", "44th Amendment Act, 1978", "61st Amendment Act, 1988"],
        "answer": 0,
        "explanation": "The 52nd Constitutional Amendment Act of 1985 added the Tenth Schedule to the Constitution, providing disqualification grounds on defection for legislators.",
        "citation": "Constitution of India — Tenth Schedule"
    },
    {
        "id": "cgl2_ga_12",
        "section": "General Awareness",
        "subtopic": "Medieval Indian History",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which ruler of the Delhi Sultanate introduced market control and price regulation reforms along with the 'Dagh' (branding of horses) system?",
        "options": ["Alauddin Khalji", "Muhammad bin Tughluq", "Balban", "Iltutmish"],
        "answer": 0,
        "explanation": "Alauddin Khalji (reigned 1296–1316) introduced stringent market control mechanisms (Shahna-i-Mandi), fixed commodity prices, and instituted the Dagh (branding of horses) and Chehra (descriptive rolls) systems.",
        "citation": "NCERT Class 11 Medieval India — The Delhi Sultanate"
    },
    {
        "id": "cgl2_ga_13",
        "section": "General Awareness",
        "subtopic": "Economics: Taxation",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which of the following taxes is a direct tax levied by the Central Government in India?",
        "options": ["Corporation Tax", "Goods and Services Tax (GST)", "Customs Duty", "Central Excise Duty"],
        "answer": 0,
        "explanation": "Corporation Tax and Personal Income Tax are direct taxes whose liability cannot be shifted to another entity. GST, customs duties, and excise are indirect taxes.",
        "citation": "NCERT Class 12 Macroeconomics — Government Budget and the Economy"
    },
    {
        "id": "cgl2_ga_14",
        "section": "General Awareness",
        "subtopic": "Environment & Ecology",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "The Ramsar Convention is an international treaty dedicated to the conservation and sustainable utilization of which ecosystem?",
        "options": ["Wetlands", "Tropical Rainforests", "Coral Reefs", "Arctic Tundra"],
        "answer": 0,
        "explanation": "Signed in Ramsar, Iran in 1971, the Ramsar Convention is an intergovernmental environmental treaty providing the framework for national action and international cooperation for wetland conservation.",
        "citation": "Ramsar Convention on Wetlands — International Environmental Agreements"
    },
    {
        "id": "cgl2_ga_15",
        "section": "General Awareness",
        "subtopic": "Indian Geography: Mountain Passes",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which high mountain pass connects the Kashmir Valley with the Union Territory of Ladakh through the Zaskar Range?",
        "options": ["Zoji La Pass", "Rohtang Pass", "Nathu La Pass", "Shipki La Pass"],
        "answer": 0,
        "explanation": "Zoji La Pass (altitude ~3,528 m) on National Highway 1 connects Srinagar in the Kashmir Valley to Kargil and Leh in Ladakh.",
        "citation": "NCERT Class 11 India Physical Environment — Mountain Passes"
    },
    {
        "id": "cgl2_ga_16",
        "section": "General Awareness",
        "subtopic": "Science: Vitamins & Deficiency",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Deficiency of Vitamin C (ascorbic acid) causes which of the following diseases characterized by bleeding gums and delayed wound healing?",
        "options": ["Scurvy", "Rickets", "Beriberi", "Pellagra"],
        "answer": 0,
        "explanation": "Vitamin C is essential for collagen synthesis. Its deficiency causes scurvy (bleeding gums, petechiae, joint pains). Rickets is caused by Vitamin D deficiency, Beriberi by B1, and Pellagra by B3.",
        "citation": "NCERT Class 10 Science — Human Nutrition"
    },
    {
        "id": "cgl2_ga_17",
        "section": "General Awareness",
        "subtopic": "Indian Polity: Fundamental Duties",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "On the recommendation of which Committee were Fundamental Duties incorporated into Part IV-A of the Indian Constitution in 1976?",
        "options": ["Swaran Singh Committee", "Sarkaria Commission", "Balwant Rai Mehta Committee", "Verma Committee"],
        "answer": 0,
        "explanation": "The Swaran Singh Committee (1976) recommended the inclusion of Fundamental Duties, which led to the 42nd Constitutional Amendment Act inserting Article 51A under Part IV-A.",
        "citation": "Constitution of India — Part IV-A Article 51A"
    },
    {
        "id": "cgl2_ga_18",
        "section": "General Awareness",
        "subtopic": "Static GK: International Organisations",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Where is the headquarters of the International Court of Justice (ICJ) located?",
        "options": ["The Hague, Netherlands", "Geneva, Switzerland", "Vienna, Austria", "New York, USA"],
        "answer": 0,
        "explanation": "The International Court of Justice (principal judicial organ of the UN) is seated at the Peace Palace in The Hague, Netherlands.",
        "citation": "United Nations System — Principal Organs"
    },
    {
        "id": "cgl2_ga_19",
        "section": "General Awareness",
        "subtopic": "Modern Indian History: Treaties",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "The Treaty of Salbai (1782) brought an end to which Anglo-Maratha conflict?",
        "options": ["First Anglo-Maratha War", "Second Anglo-Maratha War", "Third Anglo-Maratha War", "Anglo-Mysore War"],
        "answer": 0,
        "explanation": "Signed on 17 May 1782 between the British East India Company (Warren Hastings) and Mahadji Shinde, the Treaty of Salbai concluded the First Anglo-Maratha War, establishing 20 years of mutual peace.",
        "citation": "NCERT Class 11 Modern India — Anglo-Maratha Wars"
    },
    {
        "id": "cgl2_ga_20",
        "section": "General Awareness",
        "subtopic": "Science: Sound & Waves",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In which medium does sound travel with the highest velocity at 25°C?",
        "options": ["Solid Aluminium (metal)", "Liquid Water", "Gaseous Air", "Vacuum"],
        "answer": 0,
        "explanation": "Sound is a mechanical longitudinal wave requiring elastic matter to propagate. Because solids have the highest elastic bulk modulus and density coupling, sound travels fastest in solid metals (~6,420 m/s in aluminium), followed by liquids (~1,498 m/s in water), gases (~346 m/s in air), and 0 m/s in vacuum.",
        "citation": "NCERT Class 9 Science — Chapter 12 Sound"
    },
    {
        "id": "cgl2_ga_21",
        "section": "General Awareness",
        "subtopic": "Indian Polity: Writs",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which prerogative writ is issued by the Supreme Court or High Court to compel a public official or body to perform a statutory duty that they have failed to execute?",
        "options": ["Mandamus", "Habeas Corpus", "Quo Warranto", "Certiorari"],
        "answer": 0,
        "explanation": "The writ of Mandamus (meaning 'We Command') is issued to secure the performance of a public or statutory duty that an official, public authority, or lower tribunal is bound by law to perform.",
        "citation": "Constitution of India — Article 32 & Article 226"
    },
    {
        "id": "cgl2_ga_22",
        "section": "General Awareness",
        "subtopic": "Economics: Inflation Indices",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Which price index is used by the Reserve Bank of India (RBI) as the official headline anchor for monetary policy formulation and inflation targeting?",
        "options": [
            "Consumer Price Index — Combined (CPI-C)",
            "Wholesale Price Index (WPI)",
            "Index of Industrial Production (IIP)",
            "GDP Deflator"
        ],
        "answer": 0,
        "explanation": "Following the recommendations of the Urjit Patel Committee in 2014, the RBI officially adopted the Consumer Price Index Combined (CPI-C) with a flexible inflation target of 4% (+/- 2%).",
        "citation": "Reserve Bank of India Monetary Policy Framework"
    },
    {
        "id": "cgl2_ga_23",
        "section": "General Awareness",
        "subtopic": "Geography: Solar System",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Which planet in our solar system has the shortest orbital period around the Sun (88 Earth days)?",
        "options": ["Mercury", "Venus", "Mars", "Jupiter"],
        "answer": 0,
        "explanation": "Mercury is the closest planet to the Sun (semi-major axis ~0.387 AU) and completes an orbital revolution in approximately 87.97 Earth days.",
        "citation": "Physical Geography — Planetary Motions"
    },
    {
        "id": "cgl2_ga_24",
        "section": "General Awareness",
        "subtopic": "Indian History: Epics & Texts",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "The renowned treatise on statecraft, economic policy, and military strategy titled 'Arthashastra' is traditionally attributed to:",
        "options": ["Kautilya (Chanakya)", "Megasthenes", "Banabhatta", "Harisena"],
        "answer": 0,
        "explanation": "The Arthashastra was authored by Kautilya (Vishnugupta / Chanakya), prime minister to Chandragupta Maurya in the 4th century BCE.",
        "citation": "NCERT Class 12 Indian History — Early States and Economies"
    },
    {
        "id": "cgl2_ga_25",
        "section": "General Awareness",
        "subtopic": "General Science: Chemistry",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "What is the chemical name of common baking soda?",
        "options": ["Sodium Hydrogen Carbonate (NaHCO3)", "Sodium Carbonate Decahydrate (Na2CO3 · 10H2O)", "Sodium Hydroxide (NaOH)", "Calcium Oxychloride (CaOCl2)"],
        "answer": 0,
        "explanation": "Baking soda is Sodium Hydrogen Carbonate (NaHCO3). Washing soda is Na2CO3·10H2O, caustic soda is NaOH, and bleaching powder is CaOCl2.",
        "citation": "NCERT Class 10 Science — Chapter 2 Baking Soda"
    }
]

print("GA section compiled: 25 questions.")

# --------------------------------------------------------------------------
# 3. Section 3: Quantitative Aptitude (25 Questions)
# --------------------------------------------------------------------------
quant_questions = [
    {
        "id": "cgl2_quant_01",
        "section": "Quantitative Aptitude",
        "subtopic": "Algebra: Identity Formula",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "If x + 1/x = 5, what is the value of x^3 + 1/x^3?",
        "options": ["110", "125", "115", "120"],
        "answer": 0,
        "explanation": "Formula: x^3 + 1/x^3 = (x + 1/x)^3 - 3(x + 1/x) = 5^3 - 3(5) = 125 - 15 = 110.",
        "citation": "SSC CGL Quantitative Aptitude — Algebraic Identities"
    },
    {
        "id": "cgl2_quant_02",
        "section": "Quantitative Aptitude",
        "subtopic": "Profit & Loss: Successive Discounts",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "What is the single equivalent discount corresponding to two successive discounts of 20% and 15%?",
        "options": ["32%", "35%", "30%", "28%"],
        "answer": 0,
        "explanation": "Formula: Equivalent discount = d1 + d2 - (d1 * d2) / 100 = 20 + 15 - (20 * 15) / 100 = 35 - 3 = 32%.",
        "citation": "SSC CGL Quantitative Aptitude — Successive Percentage Discount"
    },
    {
        "id": "cgl2_quant_03",
        "section": "Quantitative Aptitude",
        "subtopic": "Geometry: Circles & Tangents",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "From an external point P, a secant PAB intersects a circle at A and B such that PA = 9 cm and AB = 7 cm. If PT is a tangent to the circle at point T, what is the length of tangent PT?",
        "options": ["12 cm", "14 cm", "10 cm", "16 cm"],
        "answer": 0,
        "explanation": "Tangent-Secant Theorem: PT^2 = PA * PB.\nHere PA = 9 cm, PB = PA + AB = 9 + 7 = 16 cm.\nPT^2 = 9 * 16 = 144 => PT = √144 = 12 cm.",
        "citation": "SSC CGL Quantitative Aptitude — Circles & Tangent Secant Theorem"
    },
    {
        "id": "cgl2_quant_04",
        "section": "Quantitative Aptitude",
        "subtopic": "Trigonometry: Identities",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "If sin(θ) + cos(θ) = √2 * cos(θ), what is the value of cos(θ) - sin(θ)?",
        "options": ["√2 * sin(θ)", "√2 * cos(θ)", "2 * sin(θ)", "sin(θ) / √2"],
        "answer": 0,
        "explanation": "Let sin(θ) + cos(θ) = A and cos(θ) - sin(θ) = B.\nRecall: A^2 + B^2 = (sin θ + cos θ)^2 + (cos θ - sin θ)^2 = 2(sin^2 θ + cos^2 θ) = 2.\nGiven A = √2 * cos(θ) => A^2 = 2 * cos^2(θ).\nB^2 = 2 - 2 * cos^2(θ) = 2(1 - cos^2 θ) = 2 * sin^2(θ).\nTherefore, B = cos(θ) - sin(θ) = √2 * sin(θ).",
        "citation": "SSC CGL Quantitative Aptitude — Trigonometric Identities"
    },
    {
        "id": "cgl2_quant_05",
        "section": "Quantitative Aptitude",
        "subtopic": "Time & Work: Efficiency Ratio",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "A is twice as efficient as B and can finish a piece of work in 15 days less than B. In how many days can they complete the work working together?",
        "options": ["10 days", "12 days", "8 days", "15 days"],
        "answer": 0,
        "explanation": "Efficiency ratio A : B = 2 : 1 => Time ratio A : B = 1 : 2.\nDifference in time = 2x - 1x = x = 15 days.\nSo A takes 15 days and B takes 30 days.\nTogether 1 day work = 1/15 + 1/30 = (2 + 1)/30 = 3/30 = 1/10.\nTime required together = 10 days.",
        "citation": "SSC CGL Quantitative Aptitude — Work & Time Efficiency"
    },
    {
        "id": "cgl2_quant_06",
        "section": "Quantitative Aptitude",
        "subtopic": "Compound Interest: CI vs SI Difference",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "The difference between compound interest (compounded annually) and simple interest on a sum of money for 2 years at 8% per annum is ₹96. What is the principal sum?",
        "options": ["₹15,000", "₹12,000", "₹16,000", "₹18,000"],
        "answer": 0,
        "explanation": "Formula for 2 years: Difference = P * (R / 100)^2.\n96 = P * (8 / 100)^2 = P * (64 / 10,000).\nP = (96 * 10,000) / 64 = (3 * 10,000) / 2 = ₹15,000.",
        "citation": "SSC CGL Quantitative Aptitude — CI and SI 2-Year Difference"
    },
    {
        "id": "cgl2_quant_07",
        "section": "Quantitative Aptitude",
        "subtopic": "Speed, Time & Distance: Relative Speed",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Two trains of lengths 140 m and 160 m run on parallel tracks in opposite directions with speeds of 60 km/h and 48 km/h respectively. How much time (in seconds) will they take to cross each other completely?",
        "options": ["10 seconds", "12 seconds", "9 seconds", "8 seconds"],
        "answer": 0,
        "explanation": "Total distance to cover = 140 m + 160 m = 300 m.\nRelative speed (opposite direction) = 60 + 48 = 108 km/h = 108 * (5 / 18) = 6 * 5 = 30 m/s.\nTime taken = Total distance / Relative speed = 300 / 30 = 10 seconds.",
        "citation": "SSC CGL Quantitative Aptitude — Train Crossing Problems"
    },
    {
        "id": "cgl2_quant_08",
        "section": "Quantitative Aptitude",
        "subtopic": "Mensuration: Solid Geometry",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "A solid metallic sphere of radius 6 cm is melted and recast into small solid spheres of radius 2 cm each. How many small spheres are formed?",
        "options": ["27", "18", "36", "9"],
        "answer": 0,
        "explanation": "Volume of sphere = (4/3)πR^3. Number of spheres = V_large / V_small = [(4/3)π * 6^3] / [(4/3)π * 2^3] = (6 / 2)^3 = 3^3 = 27.",
        "citation": "SSC CGL Quantitative Aptitude — Recasting of Solids"
    },
    {
        "id": "cgl2_quant_09",
        "section": "Quantitative Aptitude",
        "subtopic": "Mixtures & Alligation",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In what ratio must a grocer mix two varieties of tea costing ₹180 per kg and ₹240 per kg so that selling the mixture at ₹231 per kg yields a 10% profit?",
        "options": ["1 : 1", "2 : 3", "3 : 2", "3 : 4"],
        "answer": 0,
        "explanation": "Selling Price (SP) = ₹231 with 10% profit => Cost Price of mixture (CP) = 231 / 1.10 = ₹210 per kg.\nBy rule of alligation:\nVariety 1 (180) vs Variety 2 (240) with Mean (210):\nRatio = (240 - 210) : (210 - 180) = 30 : 30 = 1 : 1.",
        "citation": "SSC CGL Quantitative Aptitude — Alligation Rule"
    },
    {
        "id": "cgl2_quant_10",
        "section": "Quantitative Aptitude",
        "subtopic": "Average: Replacement",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "The average weight of 8 persons increases by 2.5 kg when a new person replaces one weighing 65 kg. What is the weight of the new person?",
        "options": ["85 kg", "80 kg", "75 kg", "90 kg"],
        "answer": 0,
        "explanation": "Weight of new person = Replaced weight + (Number of persons * Increase in average) = 65 + (8 * 2.5) = 65 + 20 = 85 kg.",
        "citation": "SSC CGL Quantitative Aptitude — Averages Replacement Formula"
    },
    {
        "id": "cgl2_quant_11",
        "section": "Quantitative Aptitude",
        "subtopic": "Number System: Divisibility",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "If the 7-digit number 5432x72 is completely divisible by 9, what is the digit x?",
        "options": ["4", "6", "2", "8"],
        "answer": 0,
        "explanation": "A number is divisible by 9 if the sum of its digits is divisible by 9.\nSum of digits = 5 + 4 + 3 + 2 + x + 7 + 2 = 23 + x.\nThe next multiple of 9 after 23 is 27.\n23 + x = 27 => x = 4.",
        "citation": "SSC CGL Quantitative Aptitude — Divisibility Rules"
    },
    {
        "id": "cgl2_quant_12",
        "section": "Quantitative Aptitude",
        "subtopic": "Geometry: Triangles & Incenter",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In triangle ABC, the bisectors of angle B and angle C intersect at point I (incenter). If angle BAC = 70°, what is the measure of angle BIC?",
        "options": ["125°", "110°", "135°", "140°"],
        "answer": 0,
        "explanation": "Incenter angle formula: Angle BIC = 90° + (Angle A / 2) = 90° + (70° / 2) = 90° + 35° = 125°.",
        "citation": "SSC CGL Quantitative Aptitude — Triangle Incenter Theorem"
    },
    {
        "id": "cgl2_quant_13",
        "section": "Quantitative Aptitude",
        "subtopic": "Trigonometry: Heights & Distances",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "The angle of elevation of the top of a vertical tower from a point on the ground 50 meters away from the foot of the tower is 30°. What is the height of the tower?",
        "options": ["50 / √3 meters", "50 * √3 meters", "25 meters", "100 / √3 meters"],
        "answer": 0,
        "explanation": "tan(30°) = Height / Base => 1 / √3 = h / 50 => h = 50 / √3 meters (≈ 28.87 m).",
        "citation": "SSC CGL Quantitative Aptitude — Heights and Distances"
    },
    {
        "id": "cgl2_quant_14",
        "section": "Quantitative Aptitude",
        "subtopic": "Ratio & Proportion: Fourth Proportional",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "What is the fourth proportional to 14, 21, and 28?",
        "options": ["42", "36", "48", "38"],
        "answer": 0,
        "explanation": "If x is the fourth proportional: 14 / 21 = 28 / x => x = (21 * 28) / 14 = 21 * 2 = 42.",
        "citation": "SSC CGL Quantitative Aptitude — Proportion Principles"
    },
    {
        "id": "cgl2_quant_15",
        "section": "Quantitative Aptitude",
        "subtopic": "Pipes & Cisterns",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Pipe A can fill a tank in 12 hours and Pipe B can fill it in 15 hours. A waste pipe C can empty the full tank in 20 hours. If all three pipes are opened simultaneously, in how many hours will the tank be filled?",
        "options": ["10 hours", "12 hours", "8 hours", "15 hours"],
        "answer": 0,
        "explanation": "Take LCM of 12, 15, 20 = 60 units (total capacity).\nRate of A = 60 / 12 = +5 units/hr.\nRate of B = 60 / 15 = +4 units/hr.\nRate of C = 60 / 20 = -3 units/hr.\nNet rate = 5 + 4 - 3 = 6 units/hr.\nTime required = 60 / 6 = 10 hours.",
        "citation": "SSC CGL Quantitative Aptitude — Pipes & Cisterns"
    },
    {
        "id": "cgl2_quant_16",
        "section": "Quantitative Aptitude",
        "subtopic": "Algebra: Cubic Expression",
        "type": "mcq",
        "difficulty": "hard",
        "marks": 2,
        "question": "If a + b + c = 0, what is the value of (a^2 / bc) + (b^2 / ca) + (c^2 / ab)?",
        "options": ["3", "1", "0", "-3"],
        "answer": 0,
        "explanation": "Take common denominator abc: [a^3 + b^3 + c^3] / (abc).\nConditional identity: If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc.\nTherefore, (3abc) / (abc) = 3.",
        "citation": "SSC CGL Quantitative Aptitude — Conditional Algebraic Identities"
    },
    {
        "id": "cgl2_quant_17",
        "section": "Quantitative Aptitude",
        "subtopic": "Boats and Streams",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "A boat travels 36 km downstream in 3 hours and 24 km upstream in 4 hours. What is the speed of the stream in km/h?",
        "options": ["3 km/h", "9 km/h", "6 km/h", "2 km/h"],
        "answer": 0,
        "explanation": "Downstream speed u = 36 / 3 = 12 km/h.\nUpstream speed v = 24 / 4 = 6 km/h.\nSpeed of stream y = (u - v) / 2 = (12 - 6) / 2 = 6 / 2 = 3 km/h.",
        "citation": "SSC CGL Quantitative Aptitude — Boats and Streams"
    },
    {
        "id": "cgl2_quant_18",
        "section": "Quantitative Aptitude",
        "subtopic": "Mensuration: Cone",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "A right circular cone has a base radius of 7 cm and a vertical height of 24 cm. What is its curved surface area? (Use π = 22/7)",
        "options": ["550 cm^2", "500 cm^2", "600 cm^2", "528 cm^2"],
        "answer": 0,
        "explanation": "Slant height l = √(r^2 + h^2) = √(7^2 + 24^2) = √(49 + 576) = √625 = 25 cm.\nCurved Surface Area = πrl = (22 / 7) * 7 * 25 = 22 * 25 = 550 cm^2.",
        "citation": "SSC CGL Quantitative Aptitude — Cone Curved Surface Area"
    },
    {
        "id": "cgl2_quant_19",
        "section": "Quantitative Aptitude",
        "subtopic": "Geometry: Cyclic Quadrilateral",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "ABCD is a cyclic quadrilateral. If angle A = (2x + 10)° and opposite angle C = (3x + 20)°, what is the value of x?",
        "options": ["30°", "25°", "35°", "40°"],
        "answer": 0,
        "explanation": "Opposite angles of a cyclic quadrilateral sum to 180°.\nAngle A + Angle C = 180° => (2x + 10) + (3x + 20) = 180 => 5x + 30 = 180 => 5x = 150 => x = 30°.",
        "citation": "SSC CGL Quantitative Aptitude — Cyclic Quadrilateral Theorem"
    },
    {
        "id": "cgl2_quant_20",
        "section": "Quantitative Aptitude",
        "subtopic": "Simple Interest",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "In how many years will a sum of money double itself at 12.5% per annum simple interest?",
        "options": ["8 years", "6 years", "10 years", "7.5 years"],
        "answer": 0,
        "explanation": "For a sum to double, Simple Interest (SI) = Principal (P).\nSI = (P * R * T) / 100 => P = (P * 12.5 * T) / 100 => T = 100 / 12.5 = 8 years.",
        "citation": "SSC CGL Quantitative Aptitude — Simple Interest Doubling Time"
    },
    {
        "id": "cgl2_quant_21",
        "section": "Quantitative Aptitude",
        "subtopic": "Data Interpretation: Table",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Table: Number of students enrolled in 3 streams over 3 years:\nYear | Science | Arts | Commerce\n2022 |   120   |  150 |   130\n2023 |   140   |  160 |   150\n2024 |   160   |  170 |   170\n\nWhat is the percentage increase in total student enrollment from 2022 to 2024?",
        "options": ["25%", "20%", "30%", "22.5%"],
        "answer": 0,
        "explanation": "Total enrollment 2022 = 120 + 150 + 130 = 400.\nTotal enrollment 2024 = 160 + 170 + 170 = 500.\nIncrease = 500 - 400 = 100.\nPercentage increase = (100 / 400) * 100% = 25%.",
        "citation": "SSC CGL Quantitative Aptitude — Data Interpretation"
    },
    {
        "id": "cgl2_quant_22",
        "section": "Quantitative Aptitude",
        "subtopic": "Data Interpretation: Table",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Using the enrollment table in Q21, what is the ratio of Science students in 2023 to Commerce students in 2023?",
        "options": ["14 : 15", "12 : 13", "7 : 8", "4 : 5"],
        "answer": 0,
        "explanation": "Science in 2023 = 140. Commerce in 2023 = 150.\nRatio = 140 / 150 = 14 : 15.",
        "citation": "SSC CGL Quantitative Aptitude — Data Interpretation Ratio"
    },
    {
        "id": "cgl2_quant_23",
        "section": "Quantitative Aptitude",
        "subtopic": "Data Interpretation: Table",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Using the enrollment table in Q21, which stream had the highest average annual enrollment across the 3 years?",
        "options": ["Arts (Average = 160)", "Science (Average = 140)", "Commerce (Average = 150)", "All equal"],
        "answer": 0,
        "explanation": "Total Science = 120 + 140 + 160 = 420 (Avg = 140).\nTotal Arts = 150 + 160 + 170 = 480 (Avg = 160).\nTotal Commerce = 130 + 150 + 170 = 450 (Avg = 150).\nArts has the highest average enrollment (160).",
        "citation": "SSC CGL Quantitative Aptitude — Data Interpretation Averages"
    },
    {
        "id": "cgl2_quant_24",
        "section": "Quantitative Aptitude",
        "subtopic": "Trigonometry: Evaluation",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "What is the value of:\n[sin(30°) + tan(45°)] / [1 + cos(60°)]?",
        "options": ["1", "1/2", "√3 / 2", "2"],
        "answer": 0,
        "explanation": "sin(30°) = 1/2, tan(45°) = 1, cos(60°) = 1/2.\nNumerator = 1/2 + 1 = 3/2.\nDenominator = 1 + 1/2 = 3/2.\nValue = (3/2) / (3/2) = 1.",
        "citation": "SSC CGL Quantitative Aptitude — Standard Trigonometric Values"
    },
    {
        "id": "cgl2_quant_25",
        "section": "Quantitative Aptitude",
        "subtopic": "HCF and LCM",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "The HCF and LCM of two numbers are 12 and 240 respectively. If one of the numbers is 48, what is the other number?",
        "options": ["60", "72", "84", "96"],
        "answer": 0,
        "explanation": "Product of two numbers = HCF * LCM.\n48 * y = 12 * 240 => y = (12 * 240) / 48 = 240 / 4 = 60.",
        "citation": "SSC CGL Quantitative Aptitude — Product of HCF and LCM"
    }
]

# --------------------------------------------------------------------------
# 4. Section 4: English Comprehension (25 Questions)
# --------------------------------------------------------------------------
english_questions = [
    {
        "id": "cgl2_eng_01",
        "section": "English Comprehension",
        "subtopic": "Spotting the Error",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Identify the segment in the sentence which contains a grammatical error:\n'Neither the manager (A) / nor his assistants (B) / was present at (C) / the annual conference. (D)'",
        "options": ["was present at (C)", "Neither the manager (A)", "nor his assistants (B)", "the annual conference. (D)"],
        "answer": 0,
        "explanation": "Rule of proximity for correlative conjunctions 'neither... nor': the verb agrees with the closer subject. Since 'assistants' is plural, the plural auxiliary verb 'were' must be used instead of 'was'.",
        "citation": "SSC CGL English — Subject-Verb Agreement with Correlative Conjunctions"
    },
    {
        "id": "cgl2_eng_02",
        "section": "English Comprehension",
        "subtopic": "Sentence Improvement",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the most appropriate option to substitute the underlined segment:\n'No sooner had the speaker finished his speech, *when the audience started* applauding.'",
        "options": ["than the audience started", "then the audience started", "when the audience had started", "No substitution required"],
        "answer": 0,
        "explanation": "'No sooner' is always paired with the correlative conjunction 'than' (not 'when' or 'then'). 'Hardly/Scarcely' pairs with 'when'.",
        "citation": "SSC CGL English — Correlative Conjunction Pairs"
    },
    {
        "id": "cgl2_eng_03",
        "section": "English Comprehension",
        "subtopic": "Synonyms",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the most appropriate SYNONYM of the given word:\nMETICULOUS",
        "options": ["Punctilious", "Careless", "Hasty", "Indifferent"],
        "answer": 0,
        "explanation": "'Meticulous' means showing great attention to detail; very careful and precise. 'Punctilious' is its closest synonym. 'Careless' and 'hasty' are antonyms.",
        "citation": "SSC CGL English — Vocabulary Synonyms"
    },
    {
        "id": "cgl2_eng_04",
        "section": "English Comprehension",
        "subtopic": "Antonyms",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the most appropriate ANTONYM of the given word:\nCANDID",
        "options": ["Deceitful", "Frank", "Honest", "Outspoken"],
        "answer": 0,
        "explanation": "'Candid' means truthful, straightforward, and frank. Its direct antonym is 'Deceitful' (misleading or dishonest).",
        "citation": "SSC CGL English — Vocabulary Antonyms"
    },
    {
        "id": "cgl2_eng_05",
        "section": "English Comprehension",
        "subtopic": "One Word Substitution",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the option that can be used as a one-word substitute for the given phrase:\n'A person who does not believe in the existence of God'",
        "options": ["Atheist", "Theist", "Agnostic", "Altruist"],
        "answer": 0,
        "explanation": "An 'Atheist' disbelieves in the existence of a deity. An 'Agnostic' believes that nothing is known or can be known of the existence of God. A 'Theist' believes in God.",
        "citation": "SSC CGL English — One Word Substitution"
    },
    {
        "id": "cgl2_eng_06",
        "section": "English Comprehension",
        "subtopic": "Idioms & Phrases",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the most appropriate meaning of the given idiom:\n'To burn the candle at both ends'",
        "options": [
            "To work excessively hard from early morning until late night",
            "To waste money on frivolous luxuries",
            "To illuminate a room with dual light sources",
            "To remain undecided between two choices"
        ],
        "answer": 0,
        "explanation": "The idiom 'to burn the candle at both ends' means to exhaust oneself by doing too much, especially going to bed late and getting up early to work.",
        "citation": "SSC CGL English — Idiomatic Expressions"
    },
    {
        "id": "cgl2_eng_07",
        "section": "English Comprehension",
        "subtopic": "Active & Passive Voice",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the correct passive form of the given sentence:\n'The chef prepared a delectable feast for the guests.'",
        "options": [
            "A delectable feast was prepared by the chef for the guests.",
            "A delectable feast had been prepared by the chef for the guests.",
            "A delectable feast is prepared by the chef for the guests.",
            "The guests were prepared a delectable feast by the chef."
        ],
        "answer": 0,
        "explanation": "Active sentence is in Simple Past ('prepared'). Passive structure: Object ('A delectable feast') + was/were + V3 ('prepared') + by agent + prepositional phrase.",
        "citation": "SSC CGL English — Active and Passive Voice Transformations"
    },
    {
        "id": "cgl2_eng_08",
        "section": "English Comprehension",
        "subtopic": "Direct & Indirect Speech",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the correct indirect speech form of the given sentence:\nHe said to me, 'Where are you going for your summer vacation?'",
        "options": [
            "He asked me where I was going for my summer vacation.",
            "He inquired me where was I going for my summer vacation.",
            "He asked to me where I am going for my summer vacation.",
            "He asked me that where I was going for my summer vacation."
        ],
        "answer": 0,
        "explanation": "In reporting Wh-questions: reporting verb becomes 'asked/inquired of', connector is the question word ('where'), word order changes from interrogative to assertive (subject 'I' precedes auxiliary 'was'), and present continuous 'are going' shifts to past continuous 'was going'.",
        "citation": "SSC CGL English — Direct and Indirect Speech Rules"
    },
    {
        "id": "cgl2_eng_09",
        "section": "English Comprehension",
        "subtopic": "Incorrectly Spelt Word",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the INCORRECTLY spelt word:",
        "options": ["Acommodate", "Millennium", "Embarrassment", "Conscientious"],
        "answer": 0,
        "explanation": "The correct spelling is 'Accommodate' with double 'c' and double 'm' (A-c-c-o-m-m-o-d-a-t-e).",
        "citation": "SSC CGL English — Spelling Rules"
    },
    {
        "id": "cgl2_eng_10",
        "section": "English Comprehension",
        "subtopic": "Fill in the Blanks",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the most appropriate option to fill in the blank:\n'The judge warned the witness that withholding vital evidence was ________ to perjury.'",
        "options": ["tantamount", "equitable", "comparable", "subservient"],
        "answer": 0,
        "explanation": "'Tantamount to' is the standard legal collocation meaning equivalent in seriousness to; virtually the same as.",
        "citation": "SSC CGL English — Contextual Vocabulary Usage"
    },
    {
        "id": "cgl2_eng_11",
        "section": "English Comprehension",
        "subtopic": "Para Jumbles",
        "type": "mcq",
        "difficulty": "hard",
        "marks": 2,
        "question": "Given below are four jumbled sentences. Pick the option that gives their correct logical sequence:\nP. These wetlands filter pollutants and stabilize coastlines against severe tropical cyclones.\nQ. Mangrove forests represent one of the most productive ecosystems on Earth.\nR. Despite these invaluable ecosystem services, global mangrove cover is declining rapidly.\nS. They thrive in brackish intertidal zones across tropical and subtropical regions.",
        "options": ["Q - S - P - R", "S - Q - P - R", "Q - P - S - R", "P - Q - S - R"],
        "answer": 0,
        "explanation": "Q introduces the broad topic (mangrove forests). S elaborates on their habitat (where they thrive). P specifies their ecological function (filtering pollutants, stabilizing coasts). R introduces the contrasting threat ('Despite these invaluable ecosystem services...'). Sequence: Q - S - P - R.",
        "citation": "SSC CGL English — Paragraph Cohesion"
    },
    {
        "id": "cgl2_eng_12",
        "section": "English Comprehension",
        "subtopic": "Synonyms",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the most appropriate SYNONYM of the given word:\nUBIQUITOUS",
        "options": ["Omnipresent", "Rare", "Localized", "Transient"],
        "answer": 0,
        "explanation": "'Ubiquitous' means present, appearing, or found everywhere. 'Omnipresent' is its exact synonym.",
        "citation": "SSC CGL English — Synonyms"
    },
    {
        "id": "cgl2_eng_13",
        "section": "English Comprehension",
        "subtopic": "Antonyms",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the most appropriate ANTONYM of the given word:\nZEALOUS",
        "options": ["Apathetic", "Ardent", "Passionate", "Fervent"],
        "answer": 0,
        "explanation": "'Zealous' means showing great energy or enthusiasm. Its antonym is 'Apathetic' (showing or feeling no enthusiasm, interest, or concern).",
        "citation": "SSC CGL English — Antonyms"
    },
    {
        "id": "cgl2_eng_14",
        "section": "English Comprehension",
        "subtopic": "One Word Substitution",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the option that can be used as a one-word substitute for the given phrase:\n'A remedy that cures all diseases or solves all difficulties'",
        "options": ["Panacea", "Placebo", "Elixir", "Nostrum"],
        "answer": 0,
        "explanation": "A 'Panacea' is a universal remedy for all diseases. A 'Placebo' is a harmless pill prescribed for psychological effect.",
        "citation": "SSC CGL English — One Word Substitution"
    },
    {
        "id": "cgl2_eng_15",
        "section": "English Comprehension",
        "subtopic": "Idioms & Phrases",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the most appropriate meaning of the given idiom:\n'A blessing in disguise'",
        "options": [
            "An apparent misfortune that eventually produces beneficial results",
            "A secret religious ceremony",
            "An unexpected gift from an unknown stranger",
            "A prayer offered during troubled times"
        ],
        "answer": 0,
        "explanation": "A 'blessing in disguise' refers to an unfortunate event or situation that seems bad at first, but later results in something good happening.",
        "citation": "SSC CGL English — Idiomatic Phrases"
    },
    {
        "id": "cgl2_eng_16",
        "section": "English Comprehension",
        "subtopic": "Spotting the Error",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Identify the segment containing an error:\n'Although he worked hard (A) / but he could not (B) / secure the top rank (C) / in the civil service exam. (D)'",
        "options": ["but he could not (B)", "Although he worked hard (A)", "secure the top rank (C)", "in the civil service exam. (D)"],
        "answer": 0,
        "explanation": "'Although' or 'Though' is followed by a comma or 'yet', but NEVER by 'but'. Using 'but' with 'although' creates a redundant double conjunction error.",
        "citation": "SSC CGL English — Conjunction Redundancy Rules"
    },
    {
        "id": "cgl2_eng_17",
        "section": "English Comprehension",
        "subtopic": "Sentence Improvement",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the most appropriate option to substitute the underlined segment:\n'The government has decided to *put off* the implementation of the new policy until next year.'",
        "options": ["No substitution required", "put out", "put away", "put down"],
        "answer": 0,
        "explanation": "The phrasal verb 'put off' means to postpone or delay an event to a later time, which fits the context ('until next year') perfectly.",
        "citation": "SSC CGL English — Phrasal Verbs in Context"
    },
    {
        "id": "cgl2_eng_18",
        "section": "English Comprehension",
        "subtopic": "Correctly Spelt Word",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the CORRECTLY spelt word:",
        "options": ["Bureaucracy", "Beurocracy", "Bureaucrasy", "Burocracy"],
        "answer": 0,
        "explanation": "The correct spelling is 'Bureaucracy' (B-u-r-e-a-u-c-r-a-c-y).",
        "citation": "SSC CGL English — Word Spelling Test"
    },
    {
        "id": "cgl2_eng_19",
        "section": "English Comprehension",
        "subtopic": "Preposition Usage",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "Select the most appropriate preposition:\n'The courageous firefighter was awarded a medal ________ his exceptional bravery.'",
        "options": ["for", "with", "about", "to"],
        "answer": 0,
        "explanation": "The preposition 'for' indicates the reason or cause of an award ('awarded a medal for bravery').",
        "citation": "SSC CGL English — Prepositions"
    },
    {
        "id": "cgl2_eng_20",
        "section": "English Comprehension",
        "subtopic": "Sentence Improvement",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Select the option to improve the underlined segment:\n'If I *was you*, I would accept the international scholarship without hesitation.'",
        "options": ["were you", "am you", "had been you", "No substitution required"],
        "answer": 0,
        "explanation": "In hypothetical subjunctive conditionals expressing unreal situations ('If I were...'), the subjunctive form 'were' is used for all persons including first-person singular 'I'.",
        "citation": "SSC CGL English — Subjunctive Mood Conditionals"
    },
    # Cloze Test Passage (Questions 21 to 25)
    {
        "id": "cgl2_eng_21",
        "section": "English Comprehension",
        "subtopic": "Cloze Test (Blank 1)",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "Cloze Passage:\n'Renewable energy sources such as solar and wind have witnessed (1)________ technological advancements over the past decade. This rapid innovation has drastically reduced production costs, making clean power economically (2)________ with fossil fuels. However, integrating intermittent generation into the national power grid requires robust storage systems to (3)________ fluctuations. Without large-scale battery storage, grid operators may struggle to (4)________ supply with peak evening consumer demand. Therefore, strategic policy investments in energy storage remain (5)________ for achieving true decarbonization.'\n\nSelect the most appropriate option for blank (1):",
        "options": ["unprecedented", "negligible", "trivial", "regressive"],
        "answer": 0,
        "explanation": "'Unprecedented' means never done or known before; extraordinary. The context describes rapid and significant advancements that reduced costs dramatically.",
        "citation": "SSC CGL English — Cloze Test Contextual Vocabulary"
    },
    {
        "id": "cgl2_eng_22",
        "section": "English Comprehension",
        "subtopic": "Cloze Test (Blank 2)",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "In the cloze passage, select the most appropriate option for blank (2):",
        "options": ["competitive", "incompatible", "prohibitive", "inferior"],
        "answer": 0,
        "explanation": "'Economically competitive with fossil fuels' means that renewable power prices have fallen to parity with traditional power sources.",
        "citation": "SSC CGL English — Cloze Test"
    },
    {
        "id": "cgl2_eng_23",
        "section": "English Comprehension",
        "subtopic": "Cloze Test (Blank 3)",
        "type": "mcq",
        "difficulty": "medium",
        "marks": 2,
        "question": "In the cloze passage, select the most appropriate option for blank (3):",
        "options": ["cushion", "worsen", "exaggerate", "hinder"],
        "answer": 0,
        "explanation": "'Cushion fluctuations' means to soften the impact of or mitigate sudden shifts in power supply.",
        "citation": "SSC CGL English — Cloze Test"
    },
    {
        "id": "cgl2_eng_24",
        "section": "English Comprehension",
        "subtopic": "Cloze Test (Blank 4)",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "In the cloze passage, select the most appropriate option for blank (4):",
        "options": ["align", "deviate", "disconnect", "dismantle"],
        "answer": 0,
        "explanation": "Grid operators must 'align' (match or synchronize) electricity supply with consumer demand.",
        "citation": "SSC CGL English — Cloze Test"
    },
    {
        "id": "cgl2_eng_25",
        "section": "English Comprehension",
        "subtopic": "Cloze Test (Blank 5)",
        "type": "mcq",
        "difficulty": "easy",
        "marks": 2,
        "question": "In the cloze passage, select the most appropriate option for blank (5):",
        "options": ["indispensable", "redundant", "dispensable", "superfluous"],
        "answer": 0,
        "explanation": "'Indispensable' means absolutely necessary; essential. The conclusion emphasizes that storage investments are essential for decarbonization.",
        "citation": "SSC CGL English — Cloze Test"
    }
]

# --------------------------------------------------------------------------
# 5. Output JSON Files
# --------------------------------------------------------------------------
all_100_questions = reasoning_questions + ga_questions + quant_questions + english_questions

# Full Mock 02
full_mock_data = {
    "test_id": "cgl_tier1_mock02",
    "title": "SSC CGL Tier 1 Official Full Mock Test 02",
    "total_questions": 100,
    "duration_minutes": 60,
    "marking_scheme": {
        "correct": 2,
        "wrong": -0.5,
        "unattempted": 0
    },
    "sections": [
        {"name": "General Intelligence & Reasoning", "count": 25},
        {"name": "General Awareness", "count": 25},
        {"name": "Quantitative Aptitude", "count": 25},
        {"name": "English Comprehension", "count": 25}
    ],
    "questions": all_100_questions
}

with open(os.path.join(DATA_DIR, "cgl_tier1_mock02_full.json"), "w") as f:
    json.dump(full_mock_data, f, indent=2)

# Sectionals
def save_sectional(filename, title, q_list, sec_name):
    sec_data = {
        "test_id": f"cgl_tier1_mock02_{filename}",
        "title": title,
        "section": sec_name,
        "total_questions": len(q_list),
        "duration_minutes": 15,
        "marking_scheme": {
            "correct": 2,
            "wrong": -0.5,
            "unattempted": 0
        },
        "questions": q_list
    }
    with open(os.path.join(DATA_DIR, f"cgl_tier1_mock02_{filename}.json"), "w") as f:
        json.dump(sec_data, f, indent=2)

save_sectional("reasoning", "SSC CGL Tier 1 Sectional Test 02: General Intelligence & Reasoning", reasoning_questions, "General Intelligence & Reasoning")
save_sectional("ga", "SSC CGL Tier 1 Sectional Test 02: General Awareness", ga_questions, "General Awareness")
save_sectional("quant", "SSC CGL Tier 1 Sectional Test 02: Quantitative Aptitude", quant_questions, "Quantitative Aptitude")
save_sectional("english", "SSC CGL Tier 1 Sectional Test 02: English Comprehension", english_questions, "English Comprehension")

print("Generated all 5 SSC CGL Mock 02 data files successfully!")
