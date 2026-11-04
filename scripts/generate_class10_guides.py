#!/usr/bin/env python3
"""
Generate and inject curriculum-accurate static Academic Guides into all 48 CBSE Class 10 chapter test pages.
Solves two-wave JavaScript indexing by embedding 350-500 words of static, crawlable HTML text per page.
"""

import os
import re

ROOT = "/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com/cbse-class-10"

# Guide database for all 48 chapters
CHAPTER_GUIDES = {
    # -------------------------------------------------------------------------
    # SCIENCE (13 Chapters)
    # -------------------------------------------------------------------------
    "science/ch01_chemical_reactions.html": {
        "title": "Chapter 1: Chemical Reactions and Equations",
        "subject": "Science (Chemistry)",
        "weightage": "6–7 Marks",
        "overview": "Chemical Reactions and Equations establishes the foundation of Class 10 Chemistry. The CBSE Class 10 Board exam frequently tests balancing chemical equations, state symbols, exothermic vs endothermic reactions, the five primary reaction typologies, and practical color shifts.",
        "cards": [
            ("⚡ Chemical Equation Balancing", "Adheres to the Law of Conservation of Mass. Always balance atoms of metals first, then non-metals, and finally hydrogen and oxygen. Include state symbols (s, l, g, aq)."),
            ("🔄 Decomposition Typologies", "Thermal (FeSO4 heating yields reddish-brown Fe2O3 and pungent SO2/SO3 gases), Electrolytic (water electrolysis 2:1 H2:O2 volume ratio), and Photolytic (AgCl turning grey in sunlight)."),
            ("🧪 Precipitation & Double Displacement", "Aqueous exchange of ions forming insoluble precipitates: BaCl2 + Na2SO4 forms insoluble white BaSO4; Pb(NO3)2 + KI forms bright yellow PbI2 precipitate."),
            ("🛡️ Redox & Corrosion Mechanisms", "Oxidation involves electron loss or oxygen gain; reduction involves electron gain or hydrogen gain. Rusting requires both air and moisture (4Fe + 3O2 + 2xH2O -> 2Fe2O3.xH2O).")
        ],
        "strategy": "Never forget to write physical state symbols (s, l, g, aq) in chemical equations. In displacement reactions, always verify reactivity order using the reactivity series.",
        "link": "<a href='../science-formulas-reactions.html' style='color:var(--primary); font-weight:700;'>Science All Reactions, Colors &amp; Formulas Sheet →</a>"
    },
    "science/ch02_acids_bases_salts.html": {
        "title": "Chapter 2: Acids, Bases and Salts",
        "subject": "Science (Chemistry)",
        "weightage": "7–8 Marks",
        "overview": "Focuses on Arrhenius and Brønsted-Lowry conceptual models of acids and bases, the universal pH scale, indicator transitions, and the industrial synthesis of commercial salts from sodium chloride via the Chlor-Alkali process.",
        "cards": [
            ("🎨 Indicators & Color Scales", "Litmus (Acid=Red, Base=Blue), Phenolphthalein (Acid=Colorless, Base=Pink), Methyl Orange (Acid=Red, Base=Yellow). Olfactory indicators (onion, vanilla) lose scent in basic media."),
            ("⚡ Acid-Base Reactions", "Acid + Active Metal -> Salt + H2 gas (pop sound test). Acid + Metal Carbonate -> Salt + H2O + CO2 gas (turns lime water milky due to CaCO3 precipitate)."),
            ("📊 pH Scale & Everyday Significance", "pH = -log[H+]. pH < 7 acidic, pH = 7 neutral, pH > 7 basic. Living organisms survive in narrow range (7.0–7.8). Acid rain (pH < 5.6), tooth decay begins below pH 5.5."),
            ("🏭 Chlor-Alkali Industrial Suite", "Electrolysis of brine (2NaCl + 2H2O -> 2NaOH + Cl2 + H2). Yields Caustic Soda (NaOH), Bleaching Powder (CaOCl2), Baking Soda (NaHCO3), Washing Soda (Na2CO3.10H2O), and Plaster of Paris (CaSO4.1/2H2O).")
        ],
        "strategy": "Memorize the chemical names and formulas of all 5 commercial salts. Note that Plaster of Paris must be stored in moisture-proof containers to prevent hydration back to Gypsum.",
        "link": "<a href='../science-formulas-reactions.html#salts' style='color:var(--primary); font-weight:700;'>Industrial Salts &amp; POP Chemical Equations →</a>"
    },
    "science/ch03_metals_non_metals.html": {
        "title": "Chapter 3: Metals and Non-Metals",
        "subject": "Science (Chemistry)",
        "weightage": "6–7 Marks",
        "overview": "Details physical and chemical properties of metals and non-metals, ionic bond formation, the reactivity series, and industrial metallurgical processes for extracting metals from their mineral ores.",
        "cards": [
            ("⚡ Reactivity Series & Properties", "K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au. Highly reactive metals (K, Na) react vigorously with cold water; Mg reacts with hot water; Fe, Al react with steam."),
            ("🔬 Amphoteric Oxides", "Metal oxides that react with both acids and bases to yield salt and water: Al2O3 + 6HCl -> 2AlCl3 + 3H2O and Al2O3 + 2NaOH -> 2NaAlO2 + H2O (Sodium aluminate)."),
            ("💎 Ionic Bonding & Lattices", "Formed by complete transfer of valence electrons from metal to non-metal. Characteristics: high melting/boiling points, crystalline solids, soluble in water, conduct electricity in molten/aqueous state."),
            ("⛏️ Metallurgical Extraction", "Roasting (sulfide ores heated in excess air: 2ZnS + 3O2 -> 2ZnO + 2SO2), Calcination (carbonate ores in limited air: ZnCO3 -> ZnO + CO2), and Thermit welding (Fe2O3 + 2Al -> 2Fe + Al2O3).")
        ],
        "strategy": "In metallurgy questions, differentiate clearly between Roasting (sulfides, excess O2) and Calcination (carbonates, limited air). Never confuse ionic lattice solubility.",
        "link": "<a href='../science-formulas-reactions.html#ch3' style='color:var(--primary); font-weight:700;'>Metals, Non-Metals &amp; Metallurgy Sheet →</a>"
    },
    "science/ch04_carbon_compounds.html": {
        "title": "Chapter 4: Carbon and Its Compounds",
        "subject": "Science (Chemistry)",
        "weightage": "7–8 Marks",
        "overview": "Explores the versatile tetravalent nature of carbon, catenation, covalent bonding, homologous series, IUPAC nomenclature, and vital organic reactions including combustion, oxidation, addition, esterification, and saponification.",
        "cards": [
            ("🔗 Catenation & Tetravalency", "Carbon forms 4 covalent bonds sharing electrons to achieve stable octet. High C-C bond energy enables long chains, branched structures, and rings (catenation)."),
            ("📐 Homologous Series & Groups", "Alkanes (CnH2n+2), Alkenes (CnH2n), Alkynes (CnH2n-2). Successive members differ by -CH2- unit (14u mass). Functional groups: -OH (alcohol), -CHO (aldehyde), >C=O (ketone), -COOH (acid)."),
            ("🔥 Key Organic Reactions", "Combustion (CH4 + 2O2 -> CO2 + 2H2O), Oxidation of ethanol to ethanoic acid via alkaline KMnO4, Addition (hydrogenation of oils using Ni), Substitution (CH4 + Cl2 under sunlight)."),
            ("🧼 Esterification & Soaps", "Ethanoic acid + Ethanol -> Ethyl ethanoate (fruity ester). Saponification: alkaline hydrolysis of ester yields soap (sodium carboxylate) and glycerol. Micelle cleaning mechanism.")
        ],
        "strategy": "Always draw full structural formulas when naming isomers. For esterification, mention concentrated H2SO4 as dehydrating catalyst. For micelle action, explain hydrophilic ionic head vs hydrophobic hydrocarbon tail.",
        "link": "<a href='../science-formulas-reactions.html#ch4' style='color:var(--primary); font-weight:700;'>Carbon Reaction Mechanisms &amp; Equations →</a>"
    },
    "science/ch05_life_processes.html": {
        "title": "Chapter 5: Life Processes",
        "subject": "Science (Biology)",
        "weightage": "8–9 Marks",
        "overview": "Comprehensive coverage of vital physiological processes across autotrophic and heterotrophic nutrition, cellular respiration, human double circulation, plant vascular transport (xylem/phloem), and renal excretion.",
        "cards": [
            ("🌿 Photosynthesis & Nutrition", "6CO2 + 12H2O -> C6H12O6 + 6O2 + 6H2O in presence of chlorophyll and sunlight. Site: Chloroplast thylakoids and stroma. Stomatal opening regulated by turgid guard cells."),
            ("🫁 Respiration & ATP Pathways", "Glycolysis in cytoplasm converts glucose to pyruvate. Aerobic respiration in mitochondria yields 36-38 ATP; anaerobic fermentation yields ethanol + CO2 (yeast) or lactic acid (muscle fatigue)."),
            ("❤️ Double Circulation System", "Heart pumps deoxygenated blood to lungs (pulmonary circuit) and oxygenated blood to body tissues (systemic circuit). Prevents mixing of oxygenated and deoxygenated blood for high metabolic efficiency."),
            ("🩺 Nephron Excretion & Filtration", "Bowman's capsule filters blood under pressure (ultrafiltration). Selective reabsorption of glucose, amino acids, and water occurs along the renal tubule, concentrating urea into urine.")
        ],
        "strategy": "Practice labeling the human heart (valves, septum, aorta) and nephron (glomerulus, Bowman's capsule, Henle's loop). Remember that xylem transports water/minerals unidirectionally, while phloem translocates sucrose bidirectionally.",
        "link": "<a href='ch06_control_coordination.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Control and Coordination Mock →</a>"
    },
    "science/ch06_control_coordination.html": {
        "title": "Chapter 6: Control and Coordination",
        "subject": "Science (Biology)",
        "weightage": "5–6 Marks",
        "overview": "Covers neural coordination in animals, neuron anatomy, electrical impulse transmission across synapses, reflex arcs, human brain divisions, and chemical coordination via plant phytohormones and animal endocrine glands.",
        "cards": [
            ("🧠 Neuron & Reflex Arc", "Dendrite receives stimulus -> Cyton -> Axon -> Synapse (neurotransmitter release). Reflex arc pathway: Receptor -> Sensory neuron -> Relay neuron (spinal cord) -> Motor neuron -> Effector muscle."),
            ("🏛️ Human Brain Anatomy", "Forebrain (Cerebrum: thought, memory, voluntary actions), Midbrain (visual/auditory reflexes), Hindbrain (Cerebellum: posture/balance; Medulla: involuntary vomiting/BP; Pons: respiration rate)."),
            ("🌱 Plant Tropisms & Hormones", "Phototropism, Geotropism, Hydrotropism, Thigmotropism. Auxin promotes cell elongation towards light; Gibberellins promote stem growth; Cytokinins stimulate cell division; Abscisic acid (ABA) causes wilting."),
            ("💉 Endocrine System & Feedback", "Pituitary (Growth hormone), Thyroid (Thyroxine requires iodine), Pancreas (Insulin lowers blood glucose), Adrenals (Adrenaline fight-or-flight). Regulated by negative feedback loops.")
        ],
        "strategy": "Clearly distinguish between voluntary actions (cerebrum), involuntary actions (medulla), and reflex actions (spinal cord). Remember that auxins accumulate on the shaded side of stems.",
        "link": "<a href='ch07_how_organisms_reproduce.html' style='color:var(--primary); font-weight:700;'>Next Chapter: How Do Organisms Reproduce Mock →</a>"
    },
    "science/ch07_how_organisms_reproduce.html": {
        "title": "Chapter 7: How Do Organisms Reproduce?",
        "subject": "Science (Biology)",
        "weightage": "6–7 Marks",
        "overview": "Details modes of asexual reproduction (fission, budding, spore formation, vegetative propagation) and sexual reproduction in flowering plants (pollination, double fertilization) and humans (gametogenesis, menstrual cycle, contraception).",
        "cards": [
            ("🔬 Asexual Reproduction Modes", "Binary fission (Amoeba), Multiple fission (Plasmodium), Budding (Hydra/yeast), Fragmentation (Spirogyra), Regeneration (Planaria), Spore formation (Rhizopus)."),
            ("🌸 Angiosperm Double Fertilization", "Pollen grain lands on stigma -> pollen tube grows down style to ovule -> Syngamy (male gamete + egg -> 2n zygote) + Triple fusion (male gamete + 2 polar nuclei -> 3n endosperm)."),
            ("👨‍👩‍👧 Human Reproductive Systems", "Male: Testes (sperm + testosterone, scrotum 2-2.5°C below core temp), Vas deferens, Prostate/Seminal vesicles. Female: Ovaries (oocytes + estrogen), Fallopian tubes (site of fertilization), Uterus."),
            ("🛡️ Menstrual Cycle & Contraception", "28-day cycle with ovulation around day 14. Contraceptive methods: Barrier (condoms prevent STDs), Chemical (oral pills), IUDs (Copper-T), and Surgical (Vasectomy/Tubectomy).")
        ],
        "strategy": "Labeling diagrams of the female reproductive system and flower anatomy are guaranteed high-mark questions. Remember that fertilization occurs in the ampulla/fallopian tube.",
        "link": "<a href='ch08_heredity.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Heredity &amp; Genetics Mock →</a>"
    },
    "science/ch08_heredity.html": {
        "title": "Chapter 8: Heredity",
        "subject": "Science (Biology)",
        "weightage": "5–6 Marks",
        "overview": "Explores transmission of genetic traits from parents to offspring, Gregor Mendel's classic experiments on garden peas (Pisum sativum), laws of segregation and independent assortment, and chromosomal sex determination in humans.",
        "cards": [
            ("🌱 Mendel's Monohybrid Cross", "Cross of pure tall (TT) and dwarf (tt) plants yields 100% tall (Tt) in F1. Selfing F1 gives F2 phenotypic ratio 3 Tall : 1 Dwarf (3:1) and genotypic ratio 1 TT : 2 Tt : 1 tt (1:2:1)."),
            ("🌿 Mendel's Dihybrid Cross", "Cross of round yellow (RRYY) and wrinkled green (rryy) seeds yields F1 RrYy. F2 generation displays 9:3:3:1 phenotypic ratio, demonstrating Law of Independent Assortment."),
            ("🧬 Dominant vs Recessive Alleles", "Dominant allele expresses itself in both homozygous (TT) and heterozygous (Tt) states; recessive allele expresses only in homozygous condition (tt)."),
            ("👶 Sex Determination in Humans", "Females possess homomorphic XX chromosomes (produce only X ova); males possess heteromorphic XY chromosomes (produce 50% X and 50% Y sperm). Father's sperm determines child's sex.")
        ],
        "strategy": "Always show complete Punnett squares when solving genetics problems. Emphasize that all human ova carry X chromosomes, so male sperm strictly determines zygote gender.",
        "link": "<a href='ch09_light_reflection_refraction.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Light Reflection &amp; Refraction Mock →</a>"
    },
    "science/ch09_light_reflection_refraction.html": {
        "title": "Chapter 9: Light – Reflection and Refraction",
        "subject": "Science (Physics)",
        "weightage": "7–8 Marks",
        "overview": "Rigorous treatment of geometric optics: laws of reflection, spherical mirrors (concave/convex), mirror formula, Snell's law of refraction, absolute refractive index, spherical lenses, lens formula, and lens power calculations.",
        "cards": [
            ("🪞 Spherical Mirror Formulas", "Mirror formula: 1/f = 1/v + 1/u. Linear magnification: m = hi / ho = -v / u. Concave mirror focal length f is negative (-); convex mirror focal length f is positive (+)."),
            ("📐 Ray Diagrams & Convex Applications", "Concave mirror forms real inverted images for objects beyond F, and virtual erect magnified image when object is between P and F. Convex mirrors always form virtual erect diminished images (rear-view mirrors)."),
            ("🔍 Snell's Law & Refractive Index", "Snell's Law: n21 = sin i / sin r = v1 / v2. Absolute refractive index n = c / v. Light bends toward the normal when entering an optically denser medium, slowing down in speed."),
            ("🔬 Lens Formula & Dioptres", "Lens formula: 1/f = 1/v - 1/u. Magnification: m = hi / ho = +v / u. Power of a lens: P = 1 / f(in meters). Convex lens has +P; concave lens has -P. Unit: Dioptre (D).")
        ],
        "strategy": "Always write Cartesian sign conventions explicitly (u is always negative). Remember that magnification for mirrors is -v/u, but for lenses it is +v/u. Convert focal length to meters before calculating power P = 1/f.",
        "link": "<a href='../science-formulas-reactions.html#optics' style='color:var(--primary); font-weight:700;'>Optics Formulas &amp; Sign Conventions Sheet →</a>"
    },
    "science/ch10_human_eye_colourful_world.html": {
        "title": "Chapter 10: The Human Eye and the Colourful World",
        "subject": "Science (Physics)",
        "weightage": "5–6 Marks",
        "overview": "Anatomy of the human eye, power of accommodation, common refractive vision defects (myopia, hypermetropia, presbyopia) with optical lens corrections, prism refraction, dispersion, and atmospheric scattering phenomena.",
        "cards": [
            ("👁️ Eye Anatomy & Accommodation", "Ciliary muscles adjust crystalline lens curvature to focus near and distant objects (accommodation). Normal near point = 25 cm (least distance of distinct vision); far point = infinity."),
            ("👓 Vision Defects & Lens Corrections", "Myopia (nearsightedness): image forms in front of retina, corrected by concave lens. Hypermetropia (farsightedness): image forms behind retina, corrected by convex lens. Presbyopia: bifocal lenses."),
            ("🌈 Prism Dispersion & Rainbow", "Triangular glass prism splits white light into spectrum (VIBGYOR) because different wavelengths travel at different speeds in glass (red deviates least, violet deviates most). Rainbow involves refraction, dispersion, and internal reflection."),
            ("✨ Atmospheric Refraction & Tyndall Effect", "Twinkling of stars and advanced sunrise/delayed sunset (by ~2 mins) result from continuous atmospheric refraction. Blue sky color and reddish sunset result from Rayleigh scattering (I ∝ 1/λ⁴).")
        ],
        "strategy": "Draw clear ray diagrams showing corrected vision defects with the corrective lens placed in front of the eye. State that atmospheric scattering intensity is inversely proportional to the fourth power of wavelength.",
        "link": "<a href='ch11_electricity.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Electricity Theory &amp; Numericals Mock →</a>"
    },
    "science/ch11_electricity.html": {
        "title": "Chapter 11: Electricity",
        "subject": "Science (Physics)",
        "weightage": "7–8 Marks",
        "overview": "Fundamental physics of electric charge, potential difference, Ohm's law, electrical resistance and material resistivity, series and parallel circuit analysis, Joule's heating effect, and electrical power calculations.",
        "cards": [
            ("⚡ Charge, Current & Potential", "Current I = Q / t = ne / t (Amperes). Potential difference V = W / Q (Volts). Ohm's Law: V = IR at constant temperature, yielding a linear V-I slope representing resistance R."),
            ("📏 Resistance & Material Resistivity", "R = ρ (l / A). Resistivity ρ (in Ω·m) depends solely on material and temperature. Stretching a wire to double its length quarters area, quadrupling resistance (R' = 4R)."),
            ("🔌 Resistor Networks (Series vs Parallel)", "Series: Rs = R1 + R2 + R3 (same current I throughout). Parallel: 1/Rp = 1/R1 + 1/R2 + 1/R3 (same voltage V across all branches, equivalent resistance is lower than smallest individual resistor)."),
            ("🔥 Joule's Heating & Electric Power", "Heat H = I²Rt = VIt = (V²/R)t (Joules). Power P = VI = I²R = V²/R (Watts). Commercial electrical unit: 1 kWh = 3.6 × 10⁶ Joules = 1 Board of Trade Unit.")
        ],
        "strategy": "In parallel combination numericals, double-check reciprocal addition. For household circuits, remember that domestic appliances are always connected in parallel so each operates at 220V independently.",
        "link": "<a href='../science-formulas-reactions.html#electricity' style='color:var(--primary); font-weight:700;'>Electricity Formulas &amp; Joule's Laws Sheet →</a>"
    },
    "science/ch12_magnetic_effects_electric_current.html": {
        "title": "Chapter 12: Magnetic Effects of Electric Current",
        "subject": "Science (Physics)",
        "weightage": "6–7 Marks",
        "overview": "Oersted's discovery, magnetic field lines and their properties, magnetic field due to straight conductor, circular loop, and solenoid, Fleming's Left-Hand Rule, electric motor principles, and domestic electrical circuit safety.",
        "cards": [
            ("🧲 Magnetic Field Lines & Properties", "Continuous closed loops emerging from North pole and entering South pole externally; run South to North inside. Field line density indicates strength; two field lines never cross each other."),
            ("👍 Right-Hand Thumb & Solenoid Rules", "Thumb points in current direction, curled fingers give magnetic field direction. A long cylindrical coil of insulated copper wire (solenoid) produces a uniform internal magnetic field like a bar magnet (B = μ₀nI)."),
            ("✋ Fleming's Left-Hand Rule & Force", "Forefinger = Magnetic Field, Middle finger = Current, Thumb = Force/Motion. A current-carrying conductor experiences maximum force F = BIL when perpendicular to the magnetic field (electric motor)."),
            ("🔌 Domestic Electric Circuits", "220 V AC at 50 Hz. Live wire (brown/red, 220V), Neutral wire (blue/black, 0V), Earth wire (green/yellow, safety ground). Fuse wire has low melting point to prevent short-circuit and overloading hazards.")
        ],
        "strategy": "Never draw intersecting magnetic field lines. For Fleming's Left-Hand Rule, clearly label the 3 fingers: Field (Forefinger), Current (Center finger), Motion/Thrust (Thumb).",
        "link": "<a href='ch13_our_environment.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Our Environment Ecosystem Mock →</a>"
    },
    "science/ch13_our_environment.html": {
        "title": "Chapter 13: Our Environment",
        "subject": "Science (Biology / Ecology)",
        "weightage": "4–5 Marks",
        "overview": "Ecosystem components (biotic and abiotic), food chains, food webs, trophic levels, Lindeman's 10% energy transfer law, biological magnification of pesticides, and environmental challenges including ozone layer depletion and waste management.",
        "cards": [
            ("🌿 Ecosystem & Trophic Levels", "Producers (autotrophs) -> Primary consumers (herbivores) -> Secondary consumers (carnivores) -> Tertiary consumers (apex predators). Energy flow in an ecosystem is strictly unidirectional."),
            ("🔟 Lindeman's 10% Energy Transfer Law", "Only ~10% of chemical energy stored in organic matter at one trophic level is transferred to the next higher level; 90% is lost as metabolic heat. Limits food chain length to 3-4 steps."),
            ("⚠️ Biological Magnification", "Progressive accumulation of non-biodegradable pesticides (e.g. DDT) in increasing concentrations along successive trophic levels, reaching maximum concentration in top consumers (humans)."),
            ("🛡️ Ozone Depletion & Waste Management", "Stratospheric ozone (O3) absorbs solar UV-B radiation. Chlorofluorocarbons (CFCs) release chlorine radicals that catalytically destroy ozone molecules. 1987 Montreal Protocol froze CFC production.")
        ],
        "strategy": "Explain why food chains are limited to 3 or 4 trophic levels using the 10% law. Emphasize that biodegradable waste can be broken down by microbial decomposers, unlike non-biodegradable plastics.",
        "link": "<a href='../index.html' style='color:var(--primary); font-weight:700;'>Class 10 Portal Home — 48 Chapter Catalog →</a>"
    },

    # -------------------------------------------------------------------------
    # MATHEMATICS (14 Chapters)
    # -------------------------------------------------------------------------
    "mathematics/ch01_real_numbers.html": {
        "title": "Chapter 1: Real Numbers",
        "subject": "Mathematics (Number Systems)",
        "weightage": "6 Marks",
        "overview": "Sets up the statutory CBSE Class 10 Number Systems unit. Covers the Fundamental Theorem of Arithmetic, unique prime factorization of composite numbers, proofs of irrationality, and the relationship between HCF and LCM.",
        "cards": [
            ("🔢 Fundamental Theorem of Arithmetic", "Every composite number can be uniquely expressed (factorized) as a product of prime powers, apart from the order in which the prime factors occur. Essential for finding HCF and LCM."),
            ("📐 HCF & LCM Product Relation", "For any two positive integers a and b: HCF(a, b) × LCM(a, b) = a × b. Note: This identity holds strictly for 2 numbers and does NOT generally hold for three or more numbers."),
            ("🛡️ Proof of Irrationality by Contradiction", "Classic board proofs that √2, √3, √5, and expressions like 3 + 2√5 are irrational numbers. Uses theorem: if prime p divides a², then p divides a for positive integer a."),
            ("⚙️ Coprime Integers & Fraction Simplification", "In proofs of irrationality, assuming √p = a/b where a and b are coprime integers (HCF = 1) leads to a contradiction that both share a common factor p.")
        ],
        "strategy": "The proof that √2 or √3 is irrational is a guaranteed 3-mark board question. Memorize the exact contrapositive steps: assume rationality as a/b (coprime), square both sides, and show common divisibility.",
        "link": "<a href='../math-formulas.html#ch1' style='color:var(--primary); font-weight:700;'>Mathematics Master Formula Sheet &amp; Identities →</a>"
    },
    "mathematics/ch02_polynomials.html": {
        "title": "Chapter 2: Polynomials",
        "subject": "Mathematics (Algebra)",
        "weightage": "4–5 Marks",
        "overview": "Covers linear, quadratic, and cubic polynomials, geometrical significance of zeroes from Cartesian graphs, and the algebraic relationship between the coefficients and roots of a quadratic polynomial.",
        "cards": [
            ("📈 Geometrical Meaning of Zeroes", "The zeroes of polynomial p(x) are the exact x-coordinates of the points where the graph y = p(x) intersects the horizontal x-axis. A degree-n polynomial has at most n real zeroes."),
            ("📐 Quadratic Roots & Coefficients", "For quadratic polynomial ax² + bx + c = 0 with zeroes α and β: Sum of zeroes: α + β = -b / a. Product of zeroes: αβ = c / a."),
            ("✏️ Constructing Quadratic Polynomials", "Given sum S = (α + β) and product P = αβ, the corresponding family of quadratic polynomials is given by: k [ x² - (α + β)x + αβ ] where k is any non-zero real constant."),
            ("🔄 Higher Symmetric Root Identities", "Frequently tested algebraic expansions: α² + β² = (α + β)² - 2αβ; 1/α + 1/β = (α + β)/(αβ); and α³ + β³ = (α + β)³ - 3αβ(α + β).")
        ],
        "strategy": "When asked to find a quadratic polynomial, always include the non-zero arbitrary real constant k in front: k[x² - Sx + P]. Do not omit k in formal board solutions.",
        "link": "<a href='ch03_linear_equations_two_variables.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Linear Equations Mock →</a>"
    },
    "mathematics/ch03_linear_equations_two_variables.html": {
        "title": "Chapter 3: Pair of Linear Equations in Two Variables",
        "subject": "Mathematics (Algebra)",
        "weightage": "6–7 Marks",
        "overview": "Analysis of simultaneous linear equations a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 using graphical methods, algebraic consistency conditions, substitution, and elimination techniques.",
        "cards": [
            ("🎯 Unique Solution (Intersecting Lines)", "Condition: a₁/a₂ ≠ b₁/b₂. The system is consistent with exactly one unique point of intersection (x, y) satisfying both equations simultaneously."),
            ("♾️ Infinitely Many Solutions (Coincident Lines)", "Condition: a₁/a₂ = b₁/b₂ = c₁/c₂. The system is consistent and dependent, representing identical overlapping straight lines with infinite solution pairs."),
            ("🚫 No Solution (Parallel Lines)", "Condition: a₁/a₂ = b₁/b₂ ≠ c₁/c₂. The system is inconsistent, representing two strictly parallel non-intersecting lines with zero common points."),
            ("🛠️ Algebraic Solution Techniques", "Substitution method (express y in terms of x and substitute into second equation) and Elimination method (multiply equations by constants to cancel one variable).")
        ],
        "strategy": "Always convert both equations to standard form ax + by + c = 0 before comparing ratio fractions. When solving word problems (upstream/downstream, speed/distance), state let statements clearly.",
        "link": "<a href='ch04_quadratic_equations.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Quadratic Equations Mock →</a>"
    },
    "mathematics/ch04_quadratic_equations.html": {
        "title": "Chapter 4: Quadratic Equations",
        "subject": "Mathematics (Algebra)",
        "weightage": "6–8 Marks",
        "overview": "Standard form ax² + bx + c = 0 (a ≠ 0), factorization by middle-term splitting, the quadratic formula (Shreedharacharya's rule), discriminant D = b² - 4ac, nature of roots, and real-world word problems.",
        "cards": [
            ("📐 Standard Quadratic Formula", "Roots are given by: x = [ -b ± √(b² - 4ac) ] / (2a). Solves any quadratic equation when factorization is difficult or involves surds."),
            ("⚖️ Discriminant & Nature of Roots", "D = b² - 4ac. If D > 0: two distinct real roots. If D = 0: two equal real roots (x = -b/2a). If D < 0: no real roots (imaginary conjugate roots)."),
            ("✂️ Factorization by Middle-Term Splitting", "To factorize ax² + bx + c, find two numbers p and q such that p + q = b and pq = ac. Rewrite bx as px + qx and group common binomial factors."),
            ("🚤 Real-World Modeling Problems", "Speed, distance, time problems (speed of stream upstream = u - v, downstream = u + v) and pipe flow problems (work rate = 1/x tank filled per hour).")
        ],
        "strategy": "For word problems, reject negative values of x if the physical variable represents length, age, or speed, but always justify the rejection explicitly.",
        "link": "<a href='ch05_arithmetic_progressions.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Arithmetic Progressions Mock →</a>"
    },
    "mathematics/ch05_arithmetic_progressions.html": {
        "title": "Chapter 5: Arithmetic Progressions",
        "subject": "Mathematics (Algebra)",
        "weightage": "6–7 Marks",
        "overview": "Sequences of numbers where difference between consecutive terms is constant (common difference d). Covers nth term derivation, sum of first n terms, selection of terms, and practical case studies.",
        "cards": [
            ("🔢 General Form & nth Term", "First term a, common difference d = aₖ₊₁ - aₖ. The nth term is given by: aₙ = a + (n - 1)d. Term from end: aₙ' = l - (n - 1)d where l is last term."),
            ("➕ Sum of First n Terms (Sₙ)", "Sum formula: Sₙ = (n/2) [ 2a + (n - 1)d ] or Sₙ = (n/2) [ a + l ]. Key relation: nth term aₙ = Sₙ - Sₙ₋₁."),
            ("🎲 Selection of Terms Shortcut", "For 3 terms in AP: choose (a - d), a, (a + d) [sum = 3a]. For 4 terms in AP: choose (a - 3d), (a - d), (a + d), (a + 3d) with common difference 2d."),
            ("🌟 Sum of First n Natural Numbers", "Special summation: 1 + 2 + 3 + ... + n = n(n + 1) / 2. Useful in rapid arithmetic calculations and multiple-choice questions.")
        ],
        "strategy": "If given Sₙ, compute aₙ using aₙ = Sₙ - Sₙ₋₁. In word problems, remember that number of terms n must strictly be a positive integer (natural number).",
        "link": "<a href='ch06_triangles.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Triangles &amp; Similarity Mock →</a>"
    },
    "mathematics/ch06_triangles.html": {
        "title": "Chapter 6: Triangles",
        "subject": "Mathematics (Geometry)",
        "weightage": "8–10 Marks",
        "overview": "Similarity of geometric figures, Thales Theorem (Basic Proportionality Theorem - BPT) and its converse, criteria for similarity of triangles (AAA, SSS, SAS), and multi-step geometric proofs.",
        "cards": [
            ("📐 Basic Proportionality Theorem (BPT)", "If a line is drawn parallel to one side of a triangle intersecting other two sides, it divides them in the same ratio: AD/DB = AE/EC in ΔABC with DE || BC."),
            ("🔄 Converse of BPT", "If a line divides any two sides of a triangle in the same ratio, then the line must be strictly parallel to the third side."),
            ("👥 Criteria for Triangle Similarity", "AAA (Angle-Angle-Angle or AA criterion), SSS (Side-Side-Side proportional sides), SAS (Two sides proportional and included angle equal: AB/DE = AC/DF and ∠A = ∠D)."),
            ("📏 Properties of Similar Triangles", "If ΔABC ~ ΔDEF, then corresponding angles are equal (∠A=∠D, ∠B=∠E, ∠C=∠F) and corresponding sides, perimeters, medians, and altitudes are in identical ratios.")
        ],
        "strategy": "The statement and proof of Basic Proportionality Theorem (Thales) is a classic 5-mark board question. Always write Given, To Prove, Construction, and Proof with reasons for every step.",
        "link": "<a href='ch07_coordinate_geometry.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Coordinate Geometry Mock →</a>"
    },
    "mathematics/ch07_coordinate_geometry.html": {
        "title": "Chapter 7: Coordinate Geometry",
        "subject": "Mathematics (Coordinate Geometry)",
        "weightage": "6 Marks",
        "overview": "Cartesian coordinate geometry on 2D planes: distance formula, distance from origin, collinearity tests, section formula for internal division of line segments, and midpoint coordinates.",
        "cards": [
            ("📏 Distance Formula", "Distance between P(x₁, y₁) and Q(x₂, y₂): d = √[ (x₂ - x₁)² + (y₂ - y₁)² ]. Distance of point P(x, y) from origin O(0, 0) is simply √(x² + y²)."),
            ("⚖️ Collinearity Test", "Three points A, B, C are collinear if the sum of lengths of any two segments equals the third segment (e.g. AB + BC = AC)."),
            ("✂️ Section Formula (Internal Division)", "Coordinates of point P dividing line segment AB in ratio m₁:m₂: P = [ (m₁x₂ + m₂x₁)/(m₁ + m₂), (m₁y₂ + m₂y₁)/(m₁ + m₂) ]. Shortcut ratio: use k:1."),
            ("📍 Midpoint & Centroid Coordinates", "Midpoint M of AB: M = [ (x₁ + x₂)/2, (y₁ + y₂)/2 ]. Centroid of triangle ABC: G = [ (x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3 ].")
        ],
        "strategy": "When asked to find the ratio in which a point or axis divides a segment, always assume the ratio to be k:1 instead of m:n to solve with a single unknown variable.",
        "link": "<a href='ch08_introduction_to_trigonometry.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Introduction to Trigonometry Mock →</a>"
    },
    "mathematics/ch08_introduction_to_trigonometry.html": {
        "title": "Chapter 8: Introduction to Trigonometry",
        "subject": "Mathematics (Trigonometry)",
        "weightage": "8–9 Marks",
        "overview": "Trigonometric ratios of acute angles in right-angled triangles, values of ratios for standard angles (0°, 30°, 45°, 60°, 90°), reciprocal and quotient relations, and fundamental Pythagorean trigonometric identities.",
        "cards": [
            ("📐 Trigonometric Ratios (SOH CAH TOA)", "sin θ = Opp/Hyp, cos θ = Adj/Hyp, tan θ = Opp/Adj. Reciprocals: cosec θ = 1/sin θ, sec θ = 1/cos θ, cot θ = 1/tan θ. Quotient: tan θ = sin θ / cos θ."),
            ("📊 Standard Angle Table Values", "sin 0°=0, 30°=1/2, 45°=1/√2, 60°=√3/2, 90°=1. cos values reverse sin values (cos 0°=1, 60°=1/2). tan 30°=1/√3, tan 45°=1, tan 60°=√3."),
            ("🛡️ Fundamental Pythagorean Identities", "1. sin² θ + cos² θ = 1; 2. 1 + tan² θ = sec² θ (sec² θ - tan² θ = 1); 3. 1 + cot² θ = cosec² θ (cosec² θ - cot² θ = 1)."),
            ("🔧 Algebraic Identity Manipulations", "Important relations: (sec θ - tan θ)(sec θ + tan θ) = 1 ⇒ sec θ - tan θ = 1 / (sec θ + tan θ). Similar relation holds for (cosec θ - cot θ).")
        ],
        "strategy": "When proving trigonometric identities, convert everything into sin θ and cos θ terms as the universal fallback strategy. Memorize standard table values perfectly.",
        "link": "<a href='../math-formulas.html#ch8' style='color:var(--primary); font-weight:700;'>Trigonometry Table &amp; Identities Formula Sheet →</a>"
    },
    "mathematics/ch09_some_applications_of_trigonometry.html": {
        "title": "Chapter 9: Some Applications of Trigonometry",
        "subject": "Mathematics (Trigonometry)",
        "weightage": "4–5 Marks",
        "overview": "Real-world heights and distances problems: line of sight, angle of elevation (looking upwards), angle of depression (looking downwards), and solving single and two right-angled triangle configurations.",
        "cards": [
            ("🔭 Angle of Elevation & Depression", "Angle of elevation is angle formed by line of sight with horizontal when object is above observer. Angle of depression is angle below horizontal. By alternate interior angles, both are equal."),
            ("📐 Single Triangle Setups", "Direct application of tan θ = Height / Distance. If angle is 45°, Height = Base (since tan 45° = 1). If angle is 30°, Height = Base / √3. If angle is 60°, Height = Base × √3."),
            ("🗼 Two Triangle Common Height / Base", "Two observation points on same side or opposite sides of tower. Set up two separate right-triangle equations with common height h and solve simultaneously."),
            ("🔢 Numerical Constant Substitutions", "Always substitute √3 ≈ 1.732 and √2 ≈ 1.414 only in the final step unless exact surd form is requested in the question.")
        ],
        "strategy": "Drawing a neat, correctly labeled geometric diagram with right angles marked accounts for 1 full mark in board evaluations. State all trigonometric ratios used clearly.",
        "link": "<a href='ch10_circles.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Circles Geometry Mock →</a>"
    },
    "mathematics/ch10_circles.html": {
        "title": "Chapter 10: Circles",
        "subject": "Mathematics (Geometry)",
        "weightage": "6 Marks",
        "overview": "Tangents to a circle, point of contact, Theorem 10.1 (radius is perpendicular to tangent at point of contact), and Theorem 10.2 (lengths of tangents drawn from an external point to a circle are equal).",
        "cards": [
            ("📍 Tangent & Point of Contact", "A tangent to a circle is a straight line that touches the circle at exactly one point (point of contact). Secant cuts in two points; chord joins two points."),
            ("📐 Theorem 10.1 (Perpendicularity)", "The tangent at any point of a circle is perpendicular to the radius through the point of contact: OP ⊥ AB where P is point of contact and O is center."),
            ("📏 Theorem 10.2 (Lengths of Tangents)", "The lengths of tangents drawn from an external point to a circle are equal: If tangents PA and PB are drawn from external point P, then PA = PB. Also ∠OPA = ∠OPB."),
            ("⭕ Quadrilateral Circumscribing Circle", "If a quadrilateral ABCD circumscribes a circle touching at P, Q, R, S, then AB + CD = AD + BC (sum of opposite sides are equal).")
        ],
        "strategy": "The proof of Theorem 10.2 (PA = PB using RHS congruency ΔOPA ≅ ΔOPB) is one of the most frequently asked 3-mark proofs in CBSE Class 10 history.",
        "link": "<a href='ch11_areas_related_to_circles.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Areas Related to Circles Mock →</a>"
    },
    "mathematics/ch11_areas_related_to_circles.html": {
        "title": "Chapter 11: Areas Related to Circles",
        "subject": "Mathematics (Mensuration)",
        "weightage": "4–5 Marks",
        "overview": "Formulas for perimeter (circumference) and area of circle, area of sector of a circle (minor and major), length of an arc of a sector, and area of segment of a circle.",
        "cards": [
            ("⭕ Circle Circumference & Area", "Circumference C = 2πr = πd. Area A = πr². For a semicircle, perimeter is (πr + 2r)."),
            ("🍰 Area of a Sector of a Circle", "Area of minor sector of angle θ: A = (θ / 360°) × πr². Area of major sector = πr² - Area of minor sector."),
            ("📏 Length of an Arc of a Sector", "Length of arc l corresponding to central angle θ: l = (θ / 360°) × 2πr. Notice relation: Area of sector = (1/2) × l × r."),
            ("🥧 Area of a Segment of a Circle", "Area of minor segment = Area of corresponding sector - Area of corresponding triangle = (θ/360°)πr² - (1/2)r² sin θ.")
        ],
        "strategy": "Use π = 22/7 unless explicitly specified as 3.14. For equilateral triangle inscribed in circle, area = (√3/4)a². Double check units (cm² vs m²).",
        "link": "<a href='ch12_surface_areas_volumes.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Surface Areas &amp; Volumes Mock →</a>"
    },
    "mathematics/ch12_surface_areas_volumes.html": {
        "title": "Chapter 12: Surface Areas and Volumes",
        "subject": "Mathematics (Mensuration)",
        "weightage": "6–8 Marks",
        "overview": "Surface areas and volumes of combinations of solid shapes: cubes, cuboids, right circular cylinders, right circular cones, spheres, and hemispheres.",
        "cards": [
            ("🧊 Cubes & Cuboids", "Cuboid: TSA = 2(lb + bh + hl), CSA = 2h(l + b), Volume = lbh. Cube: TSA = 6a², CSA = 4a², Volume = a³."),
            ("🥫 Cylinder & Cone Formulas", "Cylinder: CSA = 2πrh, TSA = 2πr(r + h), Volume = πr²h. Cone: Slant height l = √(r² + h²), CSA = πrl, TSA = πr(l + r), Volume = (1/3)πr²h."),
            ("⚽ Sphere & Hemisphere Formulas", "Sphere: Surface Area = 4πr², Volume = (4/3)πr³. Hemisphere: CSA = 2πr², TSA = 3πr², Volume = (2/3)πr³."),
            ("🧩 Combination of Solids Rules", "Total surface area of combined solid is sum of EXPOSED curved surface areas (do not include faces joined together). Total volume is simply the sum of individual volumes.")
        ],
        "strategy": "Never add internal contact surfaces when finding total surface area of combined solids. Calculate volume by factoring common π terms out before final arithmetic.",
        "link": "<a href='../math-formulas.html#ch12' style='color:var(--primary); font-weight:700;'>Mensuration Formulas Master Cheat Sheet →</a>"
    },
    "mathematics/ch13_statistics.html": {
        "title": "Chapter 13: Statistics",
        "subject": "Mathematics (Statistics)",
        "weightage": "6–7 Marks",
        "overview": "Measures of central tendency for grouped data: Mean (Direct Method, Assumed Mean Method), Mode of grouped frequency distributions, Median using cumulative frequency, and empirical formula.",
        "cards": [
            ("📊 Mean of Grouped Data (x̄)", "Direct method: x̄ = ∑(fᵢxᵢ) / ∑fᵢ. Assumed mean method: x̄ = a + [ ∑(fᵢdᵢ) / ∑fᵢ ] where dᵢ = xᵢ - a and xᵢ is class mark = (upper + lower limit)/2."),
            ("🎯 Mode of Grouped Data", "Mode = l + [ (f₁ - f₀) / (2f₁ - f₀ - f₂) ] × h. Modal class has highest frequency f₁; f₀ is preceding frequency; f₂ is succeeding frequency; h is class size."),
            ("📈 Median of Grouped Data", "Median = l + [ (N/2 - cf) / f ] × h. Median class is first class whose cumulative frequency cf exceeds N/2 (where N = ∑fᵢ)."),
            ("⚖️ Empirical Central Tendency Relation", "Empirical formula connecting the three measures: 3 Median = Mode + 2 Mean (or Mode = 3 Median - 2 Mean). Frequently tested in 1-mark board questions.")
        ],
        "strategy": "Ensure class intervals are continuous before calculating Mode or Median. If discontinuous (e.g. 1-10, 11-20), adjust boundaries by subtracting 0.5 from lower limit and adding 0.5 to upper limit.",
        "link": "<a href='ch14_probability.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Probability Theory Mock →</a>"
    },
    "mathematics/ch14_probability.html": {
        "title": "Chapter 14: Probability",
        "subject": "Mathematics (Probability)",
        "weightage": "4 Marks",
        "overview": "Classical theoretical probability of an event, elementary events, sample spaces (coins, dice, playing cards), impossible events (P = 0), sure events (P = 1), and complementary events P(E) + P(not E) = 1.",
        "cards": [
            ("🎲 Classical Probability Formula", "P(E) = Number of outcomes favorable to E / Total number of possible outcomes = n(E) / n(S). Probability always satisfies: 0 ≤ P(E) ≤ 1."),
            ("🪙 Coins & Dice Sample Spaces", "Single coin: {H, T} (2). Two coins: {HH, HT, TH, TT} (4). Three coins: 8 outcomes. Single die: {1, 2, 3, 4, 5, 6} (6). Pair of dice: 6 × 6 = 36 outcomes."),
            ("🃏 Standard 52-Card Pack Breakdown", "52 cards = 26 Red (13 Hearts, 13 Diamonds) + 26 Black (13 Spades, 13 Clubs). Face cards = 12 (4 Kings, 4 Queens, 4 Jacks). Aces = 4 (not face cards)."),
            ("🚫 Impossible & Sure Events", "Impossible event: P(E) = 0 (e.g. rolling 7 on a standard 6-sided die). Sure/Certain event: P(E) = 1. Complementary relation: P(E) + P(Ē) = 1 ⇒ P(Ē) = 1 - P(E).")
        ],
        "strategy": "Remember that probability can never be negative and cannot exceed 1 (or 100%). For playing cards questions, face cards strictly count Kings, Queens, and Jacks (total 12 cards).",
        "link": "<a href='../index.html' style='color:var(--primary); font-weight:700;'>Class 10 Portal Home — 48 Chapter Catalog →</a>"
    },

    # -------------------------------------------------------------------------
    # SOCIAL SCIENCE (21 Chapters: History, Geography, Pol Science, Economics)
    # -------------------------------------------------------------------------
    "social-science/ch01_rise_of_nationalism_europe.html": {
        "title": "Chapter 1: The Rise of Nationalism in Europe",
        "subject": "Social Science (History)",
        "weightage": "5–6 Marks",
        "overview": "Explores the emergence of the nation-state in 19th-century Europe, Frédéric Sorrieu's utopian vision, the French Revolution's civic legacy, the Napoleonic Civil Code of 1804, liberal nationalism, the Zollverein customs union, and the unifications of Germany and Italy.",
        "cards": [
            ("🎨 Frédéric Sorrieu's Utopian Vision", "1848 series of four prints visualizing a world made up of democratic and social republics marching past the Statue of Liberty (holding Torch of Enlightenment and Charter of Rights)."),
            ("📜 Napoleonic Code of 1804", "Civil Code abolished privileges based on birth, established equality before law, and secured the right to property. Standardized weights and measures; exported to Dutch Republic and Switzerland."),
            ("⚔️ Unification of Germany & Italy", "Germany: Otto von Bismarck led three wars over 7 years (Austria, Denmark, France) proclaiming Kaiser William I at Versailles (1871). Italy: Cavour (diplomacy), Mazzini (Young Italy), Garibaldi (Red Shirts), Victor Emmanuel II (1861)."),
            ("🕊️ Balkan Crisis & World War I", "Nationalist tensions in the Ottoman Balkan provinces (Slavic nationalities) fueled rivalries between European great powers (Russia, Germany, Britain, Austro-Hungary) culminating in World War I.")
        ],
        "strategy": "Clearly distinguish the roles of Giuseppe Mazzini (ideologue), Count Cavour (diplomat), and Giuseppe Garibaldi (military leader) in the Italian unification.",
        "link": "<a href='ch02_nationalism_in_india.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Nationalism in India Mock →</a>"
    },
    "social-science/ch02_nationalism_in_india.html": {
        "title": "Chapter 2: Nationalism in India",
        "subject": "Social Science (History)",
        "weightage": "6–8 Marks",
        "overview": "First World War impact, Mahatma Gandhi's Satyagraha (Champaran, Kheda, Ahmedabad), the Rowlatt Act, Jallianwala Bagh massacre (1919), the Non-Cooperation and Khilafat Movements, the Salt March (1930), and Civil Disobedience.",
        "cards": [
            ("✊ Gandhi's Satyagraha Philosophy", "Truth and non-violence as active moral force. Champaran (1917, indigo farmers), Kheda (1917, crop failure tax remission), and Ahmedabad (1918, cotton mill workers wage hike)."),
            ("⚠️ Rowlatt Act & Jallianwala Bagh", "Rowlatt Act (1919) authorized detention without trial. On 13 April 1919, General Dyer opened fire on peaceful gathering at Baisakhi fair in Jallianwala Bagh, Amritsar, killing hundreds."),
            ("🚫 Non-Cooperation Movement (1920–22)", "Boycott of foreign goods, government schools, and courts. Surrender of titles. Called off by Gandhi in Feb 1922 following violent clash at Chauri Chaura police post."),
            ("🧂 Dandi Salt March & Civil Disobedience", "12 March 1930: Gandhi marched 240 miles from Sabarmati to Dandi with 78 volunteers, breaking salt law on 6 April. Unlike Non-Cooperation, Civil Disobedience involved active violation of colonial laws.")
        ],
        "strategy": "Remember that Non-Cooperation aimed to refuse cooperation with British rule, whereas Civil Disobedience specifically broke colonial statutory laws (e.g. salt manufacturing, forest laws). Map work on Indian National Congress sessions (Calcutta, Nagpur, Madras) is frequent.",
        "link": "<a href='ch03_making_of_a_global_world.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Making of a Global World Mock →</a>"
    },
    "social-science/ch03_making_of_a_global_world.html": {
        "title": "Chapter 3: The Making of a Global World",
        "subject": "Social Science (History)",
        "weightage": "4–5 Marks",
        "overview": "Pre-modern global interconnections, ancient Silk Routes linking Asia with Europe and Africa, food travel (potatoes, noodles), conquest and biological warfare (smallpox in Americas), the 19th-century global economy, and the Great Depression.",
        "cards": [
            ("🐫 Silk Routes & Trade Networks", "Historic overland and maritime trade pathways connecting China, India, and Persia with the Mediterranean. Facilitated exchange of Chinese silk, Indian spices, pottery, and spread of Buddhism and Islam."),
            ("🥔 Food Travel & Columbian Exchange", "Introduction of American crops (potatoes, tomatoes, maize, chili) transformed European diets. Irish Potato Famine (1845–49) killed nearly one million people due to potato blight."),
            ("🦠 Biological Conquest of the Americas", "Spanish and Portuguese conquistadors conquered America not solely by conventional arms, but using deadly smallpox germs to which indigenous populations had no natural immunity."),
            ("📉 The Great Depression (1929)", "US stock market crash on Wall Street (October 1929) triggered worldwide economic collapse: agricultural overproduction, banking failures, soaring unemployment, and fall of global commodity prices.")
        ],
        "strategy": "Focus on the interconnected nature of pre-modern trade. Note how the introduction of the potato altered European survival and how smallpox acted as a biological weapon.",
        "link": "<a href='ch04_age_of_industrialisation.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Age of Industrialisation Mock →</a>"
    },
    "social-science/ch04_age_of_industrialisation.html": {
        "title": "Chapter 4: The Age of Industrialisation",
        "subject": "Social Science (History)",
        "weightage": "4–5 Marks",
        "overview": "Proto-industrialization before the factory system, arrival of steam power, labor conditions in Victorian Britain, the slow pace of mechanization, emergence of textile mills in colonial India, and marketing goods through advertisements.",
        "cards": [
            ("🧵 Proto-Industrialization System", "Network of decentralized rural domestic manufacturing financed by urban merchants before the rise of centralized factories. Peasants and artisans produced textiles in cottages."),
            ("⚙️ Steam Power & Hand Labour", "Steam engines (James Watt/Matthew Boulton) were expensive and broke down frequently. In Victorian Britain, cheap abundant human labor made capitalists prefer hand labor for seasonal industries."),
            ("🏭 Early Indian Industrialists", "Pioneers like Dwarkanath Tagore, Dinshaw Petit, Jamsetjee Nusserwanjee Tata (TISCO 1912), and Seth Hukumchand established early cotton, jute, and steel industries amidst colonial restrictions."),
            ("🏷️ Advertisements & Calenders", "Manufacturers used labels with images of Indian gods (Krishna, Saraswati) and historical emperors on cloth bundles ('Made in Manchester') to inspire consumer trust and domestic purchase.")
        ],
        "strategy": "Highlight that proto-industrialization occurred outside the factory system in rural households. Note why European capitalists were initially reluctant to adopt expensive machinery.",
        "link": "<a href='ch05_print_culture_modern_world.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Print Culture Mock →</a>"
    },
    "social-science/ch05_print_culture_modern_world.html": {
        "title": "Chapter 5: Print Culture and the Modern World",
        "subject": "Social Science (History)",
        "weightage": "5–6 Marks",
        "overview": "Evolution of print from hand calligraphy in East Asia (China, Japan, Korea) to Johannes Gutenberg's movable type press in Europe, the Protestant Reformation, print revolution, and its impact on the Indian national movement.",
        "cards": [
            ("🖨️ Johannes Gutenberg's Printing Press", "Mid-15th century Strasbourg: Gutenberg adapted olive and wine press mechanics with lead-alloy movable metal types. The first printed book was the Latin Bible (~180 copies in 3 years)."),
            ("✝️ Protestant Reformation (Martin Luther)", "In 1517, Martin Luther wrote Ninety-Five Theses criticizing Catholic Church corruptions and indulgences. Rapid printing and circulation catalyzed the Protestant Reformation ('Print is the ultimate gift of God')."),
            ("🇫🇷 Print & the French Revolution", "Print popularized enlightenment ideas of Voltaire and Rousseau, eroded absolute monarchical authority, and created a critical public sphere of political debate and caricature."),
            ("🇮🇳 Print Evolution in Colonial India", "First press brought by Portuguese Jesuit priests to Goa (1556). James Augustus Hickey started Bengal Gazette (1780). Vernacular Press Act (1878) modeled on Irish press laws to censor nationalist newspapers.")
        ],
        "strategy": "Remember that the Vernacular Press Act (1878) specifically targeted regional Indian language newspapers. Memorize the quotation by Martin Luther on print.",
        "link": "<a href='ch06_resources_and_development.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Resources &amp; Development Mock →</a>"
    },
    "social-science/ch06_resources_and_development.html": {
        "title": "Chapter 6: Resources and Development",
        "subject": "Social Science (Geography)",
        "weightage": "4–5 Marks",
        "overview": "Classification of natural resources, sustainable development, Agenda 21 of Rio Earth Summit 1992, resource planning in India, land utilization, land degradation, and the major soil types of India.",
        "cards": [
            ("🌍 Sustainable Development & Agenda 21", "Development without damaging the environment or compromising needs of future generations. Adopted at 1992 UN Rio Earth Summit to combat poverty and disease through global cooperation."),
            ("🌾 Major Indian Soil Classifications", "Alluvial (Northern Plains, Khadar new fertile vs Bhangar old kankar), Black/Regur (Deccan basalt, ideal for cotton), Red & Yellow (crystalline igneous), Laterite (leached, cashews), Arid (sandy/saline)."),
            ("⚠️ Land Degradation Causes", "Overgrazing (Gujarat, Rajasthan), Deforestation and mining (Jharkhand, Odisha), Over-irrigation causing salinity/alkalinity (Punjab, Haryana, Western UP)."),
            ("🛡️ Soil Conservation Measures", "Contour plowing (decelerates water runoff), terrace farming (Himalayas), strip cropping (strips of grass break wind force), and shelterbelts (rows of trees stabilizing sand dunes).")
        ],
        "strategy": "Identify soils on India outline maps: Black soil (Maharashtra/Gujarat), Alluvial (Gangetic plain), Laterite (Western Ghats). Differentiate Khadar (fertile new alluvium) and Bhangar (older kankar-rich).",
        "link": "<a href='ch07_forest_and_wildlife_resources.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Forest &amp; Wildlife Mock →</a>"
    },
    "social-science/ch07_forest_and_wildlife_resources.html": {
        "title": "Chapter 7: Forest and Wildlife Resources",
        "subject": "Social Science (Geography)",
        "weightage": "3–4 Marks",
        "overview": "Flora and fauna diversity in India, IUCN classification of species (endangered, vulnerable, rare, endemic, extinct), causes of biodiversity depletion, and community-led conservation movements.",
        "cards": [
            ("🐾 IUCN Species Classification", "Normal (cattle), Endangered (Black buck, Indian wild ass), Vulnerable (Blue sheep, Asiatic elephant), Rare (Himalayan brown bear), Endemic (Andaman teal), Extinct (Asiatic cheetah)."),
            ("🌲 Forest Administrative Categories", "Reserved Forests (more than 50% of total forests, highest protection), Protected Forests (one-third, protected from further depletion), Unclassed Forests (managed by communities/govt)."),
            ("🤝 Community Conservation Movements", "Chipko Movement in Uttarakhand (hugging trees prevented logging), Beej Bachao Andolan in Tehri, Sariska Tiger Reserve villagers resisting mining, Bhairodev Dakav 'Sonchuri' in Alwar."),
            ("🐅 Project Tiger (1973)", "Pioneering wildlife conservation campaign initiated to protect the Bengal tiger from extinction. Established major tiger reserves like Corbett (Uttarakhand), Sundarbans (WB), and Bandhavgarh (MP).")
        ],
        "strategy": "Know the distinction between Reserved and Protected forests. Memorize community initiatives like Chipko and Joint Forest Management (JFM) started in Odisha in 1988.",
        "link": "<a href='ch08_water_resources.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Water Resources Mock →</a>"
    },
    "social-science/ch08_water_resources.html": {
        "title": "Chapter 8: Water Resources",
        "subject": "Social Science (Geography)",
        "weightage": "3–4 Marks",
        "overview": "Water scarcity causes, multipurpose river valley projects ('Temples of modern India'), ecological drawbacks of large dams, and traditional rainwater harvesting techniques across regional India.",
        "cards": [
            ("💧 Causes of Water Scarcity", "Growing population, intensive agricultural expansion (tube wells depleting water tables), industrial pollution, unequal access, and over-exploitation of freshwater reserves."),
            ("🏗️ Multipurpose River Valley Projects", "Dams built for flood control, hydroelectricity, irrigation, navigation, and fish breeding. Jawaharlal Nehru proudly called them 'Temples of modern India' for integrating agriculture and industry."),
            ("⚠️ Ecological & Social Drawbacks", "Submergence of fertile lands and forests, disruption of natural river flow and silt transport, loss of aquatic habitats, displacement of indigenous tribes, and interstate water disputes (Cauvery, Krishna-Godavari)."),
            ("🌧️ Traditional Rainwater Harvesting", "'Guls' and 'Kuls' in Western Himalayas; 'Inundation channels' in Bengal; 'Khadins' in Jaisalmer and 'Johads' in Rajasthan; Rooftop rainwater harvesting mandatory in Tamil Nadu.")
        ],
        "strategy": "State both benefits and ecological criticisms of large dams. Note that Tamil Nadu is the first Indian state to make rooftop rainwater harvesting compulsory by law.",
        "link": "<a href='ch09_agriculture.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Agriculture &amp; Cropping Patterns Mock →</a>"
    },
    "social-science/ch09_agriculture.html": {
        "title": "Chapter 9: Agriculture",
        "subject": "Social Science (Geography)",
        "weightage": "5–6 Marks",
        "overview": "Farming systems in India (primitive subsistence, intensive subsistence, commercial plantation), cropping seasons (Rabi, Kharif, Zaid), major food and commercial crops, and institutional agricultural reforms.",
        "cards": [
            ("🌾 Indian Cropping Seasons", "Kharif: Sown with onset of monsoon (June-July), harvested Sept-Oct (Rice, Maize, Jowar, Cotton). Rabi: Sown in winter (Oct-Dec), harvested April-June (Wheat, Barley, Gram, Mustard). Zaid: Summer crops (Watermelon, Cucumber)."),
            ("🍚 Major Food Crops Climatic Criteria", "Rice: Kharif crop requiring high temp (>25°C), high humidity, annual rainfall >100 cm. Wheat: Rabi crop requiring cool growing season, bright sunshine, 50-75 cm rainfall."),
            ("☕ Plantation & Commercial Crops", "Tea (beverage crop on well-drained fertile acidic soil, Assam), Coffee (Arabica variety from Yemen, Nilgiris), Cotton (Black soil, 210 frost-free days), Jute ('Golden fiber', high rainfall/floods)."),
            ("🚜 Institutional & Tech Reforms", "Green Revolution, White Revolution (Operation Flood), Land consolidation (Chakbandi), Abolition of Zamindari, Kisan Credit Card (KCC), Personal Accident Insurance Scheme (PAIS), and MSP.")
        ],
        "strategy": "Map work for Rice, Wheat, Cotton, Tea, and Sugarcane producing states is guaranteed. Memorize the temperature, rainfall, and soil requirements for Rice vs Wheat.",
        "link": "<a href='ch10_minerals_and_energy_resources.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Minerals &amp; Energy Resources Mock →</a>"
    },
    "social-science/ch10_minerals_and_energy_resources.html": {
        "title": "Chapter 10: Minerals and Energy Resources",
        "subject": "Social Science (Geography)",
        "weightage": "5–6 Marks",
        "overview": "Mode of occurrence of minerals (veins, lodes, beds, placer deposits), classification into metallic (ferrous/non-ferrous) and non-metallic, conventional energy sources (coal, petroleum), and non-conventional renewable energy.",
        "cards": [
            ("⛏️ Mode of Mineral Occurrence", "Igneous/metamorphic rocks: Veins (small) and Lodes (large). Sedimentary rocks: Beds and layers (Coal, Gypsum). Residual weathered mass: Bauxite. Alluvial placer deposits in sands: Gold, Silver, Platinum."),
            ("🔩 Ferrous & Non-Ferrous Minerals", "Iron Ore: Magnetite (finest 70% iron, magnetic), Hematite (50-60% iron). Major belts: Odisha-Jharkhand, Durg-Bastar-Chandrapur, Bellary-Chitradurga. Bauxite: Aluminum ore (Panchpatmali in Odisha)."),
            ("⚡ Conventional Energy Resources", "Coal (Anthracite highest grade, Bituminous commercial, Lignite brown soft, Peat). Petroleum fields: Mumbai High (63%), Gujarat (Ankleshwar), Assam (Digboi oldest oil field)."),
            ("☀️ Non-Conventional Renewable Energy", "Solar energy (Photovoltaic technology), Wind power (Muppandal in Tamil Nadu), Biogas (Gobar gas plants in rural areas), Tidal energy (Gulf of Kuchchh), Geothermal energy (Parvati Valley, Puga Valley).")
        ],
        "strategy": "Distinguish between Magnetite (highest magnetic content) and Hematite. Digboi is India's oldest operating oilfield. Mumbai High is India's largest offshore field.",
        "link": "<a href='ch11_manufacturing_industries.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Manufacturing Industries Mock →</a>"
    },
    "social-science/ch11_manufacturing_industries.html": {
        "title": "Chapter 11: Manufacturing Industries",
        "subject": "Social Science (Geography)",
        "weightage": "4–5 Marks",
        "overview": "Importance of manufacturing as the backbone of economic development, industrial location factors, classification of industries (agro-based, mineral-based), iron and steel industry, and industrial environmental pollution control.",
        "cards": [
            ("🏭 Economic Significance & Agglomeration", "Manufacturing transforms raw materials into valuable finished goods. Agglomeration economies occur when industries cluster in urban centers to share banking, labor, and transport infrastructure."),
            ("🧵 Agro-Based Industries", "Cotton textiles (first successful mill Mumbai 1854, concentrated in Gujarat/Maharashtra due to raw cotton, port, humid climate). Jute textiles (first mill Rishra near Kolkata 1855, Hugli basin)."),
            ("🔩 Iron & Steel Mineral Industry", "Basic heavy industry requiring raw materials in ratio 4 Iron ore : 2 Coking coal : 1 Limestone. Concentrated in Chhota Nagpur plateau due to low-cost iron ore, coking coal, and cheap labor."),
            ("🌊 Industrial Pollution & Environmental Control", "Air pollution (SO2, CO from chimneys), Water pollution (organic/inorganic effluents), Thermal pollution (hot water dumped into rivers). Control: Effluent Treatment Plants (ETP) and electrostatic precipitators.")
        ],
        "strategy": "Explain why the jute textile industry is clustered along the banks of the Hugli river (water for retting, raw jute proximity, cheap labor, Kolkata port).",
        "link": "<a href='ch12_lifelines_of_national_economy.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Lifelines of National Economy Mock →</a>"
    },
    "social-science/ch12_lifelines_of_national_economy.html": {
        "title": "Chapter 12: Lifelines of National Economy",
        "subject": "Social Science (Geography)",
        "weightage": "3–4 Marks",
        "overview": "Transport networks (roadways, railways, pipelines, waterways, airways), communication networks, international trade as economic barometer, and tourism as a thriving modern industry.",
        "cards": [
            ("🛣️ Roadways Classification", "Golden Quadrilateral Super Highways (linking Delhi-Kolkata-Chennai-Mumbai by NHAI), National Highways, State Highways, District Roads, Border Roads (constructed by BRO in northern frontiers)."),
            ("🚆 Railways Network Advantages", "Principal mode of freight and passenger transportation in India. Dense network in northern plains due to level land, high population density, and rich agricultural resources."),
            ("⛽ Pipeline & Inland Waterway Networks", "Pipelines transport crude oil, petroleum products, and natural gas (HVJ pipeline 1,700 km). National Waterway No. 1 on Ganga river (Allahabad to Haldia, 1,620 km)."),
            ("🚢 Major Sea Ports & International Trade", "Kandla/Deendayal Port (tidal port, Gujarat), Mumbai (biggest port), Marmagao (iron ore export), New Mangalore, Kochi (natural harbor), Chennai, Visakhapatnam (deepest landlocked).")
        ],
        "strategy": "Remember that National Waterway 1 runs between Prayagraj (Allahabad) and Haldia on the Ganga. Kandla was developed after partition to relieve pressure on Mumbai port.",
        "link": "<a href='ch13_power_sharing.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Power Sharing Mock →</a>"
    },
    "social-science/ch13_power_sharing.html": {
        "title": "Chapter 13: Power Sharing",
        "subject": "Social Science (Political Science)",
        "weightage": "4–5 Marks",
        "overview": "Comparative analysis of ethnic accommodation in Belgium versus majoritarianism in Sri Lanka, the fundamental moral and prudential reasons for power sharing in modern constitutional democracies.",
        "cards": [
            ("🇧🇪 Belgium Ethnic Accommodation", "Complex ethnic composition (59% Dutch in Flemish, 40% French in Wallonia; Brussels 80% French, 20% Dutch). Four constitutional amendments (1970-1993) ensured equal ministers and Community Government."),
            ("🇱🇰 Sri Lanka Majoritarian Disaster", "74% Sinhala Buddhists passed 1956 Act making Sinhala sole official language, favoring Sinhalas in university admissions and government jobs, alienating 18% Tamils and sparking civil war."),
            ("💡 Prudential Reasons for Power Sharing", "Power sharing reduces the possibility of conflict and violence between social groups, ensuring political stability and preventing majority tyranny."),
            ("🏛️ Forms of Power Sharing", "Horizontal division among Legislature, Executive, Judiciary (System of Checks and Balances). Vertical division between Union, State, and Local tiers (Federalism). Community groups & coalitions.")
        ],
        "strategy": "Contrast Belgium's peaceful institutional accommodation with Sri Lanka's majoritarian civil war. Know the difference between horizontal (checks & balances) and vertical (federal) power sharing.",
        "link": "<a href='ch14_federalism.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Federalism &amp; Decentralization Mock →</a>"
    },
    "social-science/ch14_federalism.html": {
        "title": "Chapter 14: Federalism",
        "subject": "Social Science (Political Science)",
        "weightage": "4–5 Marks",
        "overview": "Theory and practice of federalism in India, 'Coming Together' vs 'Holding Together' federations, constitutional division of legislative powers (Union, State, Concurrent Lists), and the 1992 Panchayati Raj decentralization.",
        "cards": [
            ("🏛️ Key Features of Federalism", "Two or more tiers of government; each tier has its own jurisdiction in legislation, taxation, and administration specified in constitution; courts act as umpire in disputes."),
            ("🤝 Coming vs Holding Together", "'Coming Together' federations: Independent states pool sovereignty to form bigger unit (USA, Switzerland, Australia). 'Holding Together': Large country divides power between national and state units (India, Spain, Belgium)."),
            ("📜 Three-Fold Legislative Distribution", "Union List (97 items: Defense, Foreign affairs, Banking - Parliament only); State List (66 items: Police, Trade, Agriculture - State legislature only); Concurrent List (47 items: Education, Forests - both, Union prevails on conflict)."),
            ("🗳️ 1992 Decentralization (73rd/74th Amendment)", "Mandatory regular local elections, 33% reservation for women in all local bodies, State Election Commission created, State Finance Commission shares revenues with Panchayats and Municipalities.")
        ],
        "strategy": "Remember that Residuary subjects (e.g. computer software) belong exclusively to the Union government. Understand that India is a 'holding together' federation where the central government is strong.",
        "link": "<a href='ch15_gender_religion_caste.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Gender, Religion and Caste Mock →</a>"
    },
    "social-science/ch15_gender_religion_caste.html": {
        "title": "Chapter 15: Gender, Religion and Caste",
        "subject": "Social Science (Political Science)",
        "weightage": "4–5 Marks",
        "overview": "Social divisions in constitutional politics: gender division, feminist movements, women's political representation, communalism vs secularism, and caste in politics versus politics in caste.",
        "cards": [
            ("👩 Gender Division & Feminism", "Sexual division of labor confines women to unpaid household chores. Feminist movements advocate equal rights for women in education, career, and political leadership (Panchayati Raj 1/3rd reservation)."),
            ("⛪ Communalism Danger", "Belief that religion is the principal basis of social community, leading to prejudice, communal violence, and state bias. Most ugly manifestation: communal riots and partition violence."),
            ("🕊️ Secular State Constitutional Pillars", "No official state religion; freedom to profess, practice, and propagate any religion (Article 25); prohibition of discrimination based on religion (Article 15); state intervention for equality (untouchability banned)."),
            ("👥 Caste in Politics vs Politics in Caste", "Caste in politics: parties select candidates matching caste composition of constituency. Politics in caste: caste groups incorporate neighboring sub-castes, form coalitions, and demand backward class quotas.")
        ],
        "strategy": "Explain the constitutional provisions that make India a secular state. Note that caste is not the sole determinant of Indian elections; performance and candidate charisma also dictate voting.",
        "link": "<a href='ch16_political_parties.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Political Parties Mock →</a>"
    },
    "social-science/ch16_political_parties.html": {
        "title": "Chapter 16: Political Parties",
        "subject": "Social Science (Political Science)",
        "weightage": "5–6 Marks",
        "overview": "Need and functions of political parties, party systems (one-party, two-party, multi-party), criteria for recognition as National and State political parties by Election Commission, and major challenges facing parties.",
        "cards": [
            ("🏛️ Three Components & Functions", "Components: The leaders, active members, and followers. Functions: Contest elections, put forward policies/programs, form and run government, play role of opposition, shape public opinion."),
            ("🗳️ National vs State Party Criteria", "National Party: 6% of valid votes in Lok Sabha or Assembly elections in 4 states + at least 4 Lok Sabha seats. State Party: 6% votes in state legislative assembly + at least 2 assembly seats."),
            ("⚠️ Challenges to Political Parties", "1. Lack of internal democracy (concentration of power in top leaders); 2. Dynastic succession; 3. Growing role of money and muscle power; 4. Lack of meaningful choices for voters."),
            ("🛠️ Electoral Reforms & Anti-Defection", "Anti-Defection Law (52nd Amendment) disqualifies legislators changing party after election. Mandatory affidavit declaring criminal cases and financial assets. IT returns filing.")
        ],
        "strategy": "State the difference between an alliance and a coalition. Memorize the Election Commission criteria for a National Party versus a State Party.",
        "link": "<a href='ch17_outcomes_of_democracy.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Outcomes of Democracy Mock →</a>"
    },
    "social-science/ch17_outcomes_of_democracy.html": {
        "title": "Chapter 17: Outcomes of Democracy",
        "subject": "Social Science (Political Science)",
        "weightage": "3–4 Marks",
        "overview": "Assessing the real outcomes of democracy: accountable, responsive, and legitimate government, economic growth versus inequality, accommodation of social diversity, and dignity and freedom of citizens.",
        "cards": [
            ("🏛️ Accountable, Responsive & Legitimate", "Democracy produces a government accountable to citizens and responsive to their needs. Deliberation and negotiation may cause delays, but make decisions more acceptable and legitimate."),
            ("📈 Economic Growth vs Dictatorships", "Historically, dictatorships recorded slightly higher rates of economic growth, but difference is negligible. Democracy guarantees better equitable distribution, human development, and rights."),
            ("🤝 Accommodation of Social Diversity", "No society can fully resolve conflicts permanently, but democracy provides peaceful mechanisms to negotiate differences. Requires majority to work with minority so government reflects common view."),
            ("👑 Dignity & Freedom of Citizens", "Democracy stands far superior to any other form of government in promoting dignity and freedom of the individual, transforming subjects into active rights-bearing citizens.")
        ],
        "strategy": "Emphasize that the most distinctive feature of democracy is that its examination is never over; as people get some benefits, they demand more, showing its dynamic success.",
        "link": "<a href='ch18_development.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Development Economics Mock →</a>"
    },
    "social-science/ch18_development.html": {
        "title": "Chapter 18: Development",
        "subject": "Social Science (Economics)",
        "weightage": "4–5 Marks",
        "overview": "Concept of development: different people have different developmental goals, conflicting aspirations, national income versus per capita income, World Bank criteria, and UNDP Human Development Index (HDI).",
        "cards": [
            ("🎯 Conflicting Developmental Goals", "What may be development for one may not be development for the other; it may even be destructive (e.g. industrialists want big dams for power, but dams submerge tribal farmlands)."),
            ("💰 Income & Other Non-Material Goals", "Besides money and income, people seek equal treatment, freedom, security, respectful working conditions, clean environment, and work-life balance."),
            ("🌐 World Bank vs UNDP Metrics", "World Bank World Development Report uses only Per Capita Income (PCI = Total National Income / Population) to classify rich and low-income countries. Excludes health and education."),
            ("📊 Human Development Index (HDI)", "UNDP Human Development Report compares nations on three composite pillars: 1. Educational attainment (mean/expected schooling), 2. Health status (Life expectancy at birth), and 3. Per capita income.")
        ],
        "strategy": "Compare World Bank's per capita income approach with UNDP's comprehensive Human Development Index (HDI). Highlight that Kerala has a low Infant Mortality Rate (IMR) due to adequate public healthcare.",
        "link": "<a href='ch19_sectors_of_indian_economy.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Sectors of the Indian Economy Mock →</a>"
    },
    "social-science/ch19_sectors_of_indian_economy.html": {
        "title": "Chapter 19: Sectors of the Indian Economy",
        "subject": "Social Science (Economics)",
        "weightage": "5–6 Marks",
        "overview": "Classification of economic activities: Primary (agriculture), Secondary (manufacturing), and Tertiary (services); GDP calculation via final goods; historical shift in sectors; disguised unemployment; organized vs unorganized sectors.",
        "cards": [
            ("🌾 Three Economic Sectors", "Primary (extracting natural resources: agriculture, fishing, mining). Secondary (manufacturing finished goods in factories). Tertiary (services aiding production: transport, banking, IT)."),
            ("💰 Gross Domestic Product (GDP)", "Value of all FINAL goods and services produced within a country during a particular year. Intermediate goods (e.g. flour used in biscuits) are excluded to prevent double counting."),
            ("⚠️ Disguised Unemployment in Agriculture", "More people work in agriculture than necessary. If workers are removed, total agricultural production does not fall (marginal productivity = zero). Need rural non-farm employment."),
            ("🏢 Organized vs Unorganized Sectors", "Organized: registered with government, job security, fixed working hours, paid leave, provident fund, medical benefits. Unorganized: small scattered units, low wages, zero job security.")
        ],
        "strategy": "Explain why only final goods are counted in GDP (double counting problem). Memorize the key provisions of MGNREGA 2005 (100 days of guaranteed wage employment per rural household).",
        "link": "<a href='ch20_money_and_credit.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Money &amp; Credit Mock →</a>"
    },
    "social-science/ch20_money_and_credit.html": {
        "title": "Chapter 20: Money and Credit",
        "subject": "Social Science (Economics)",
        "weightage": "5–6 Marks",
        "overview": "Money as medium of exchange, eliminating double coincidence of wants in barter, modern forms of money (currency, demand deposits, cheques), loan activities of banks, terms of credit, and Self-Help Groups (SHGs).",
        "cards": [
            ("💵 Money Eliminates Barter", "Barter economy required double coincidence of wants (both parties must desire each other's goods). Money acts as universal intermediate medium of exchange, eliminating this constraint."),
            ("🏦 Modern Money & Bank Lending", "Currency notes authorized by RBI. Commercial banks keep ~15% deposits as cash reserve for depositors and extend remaining 85% as credit/loans at interest."),
            ("📝 Terms of Credit & Debt Trap", "Terms of credit: Interest rate, collateral (security asset like land, vehicle pledged to lender), documentation, and mode of repayment. High informal moneylender interest creates vicious debt trap."),
            ("🤝 Formal vs Informal & SHGs", "Formal sector (Banks, Cooperatives supervised by RBI with low interest); Informal sector (moneylenders, traders charging 36-60% interest). Self-Help Groups (15-20 women pooling savings).")
        ],
        "strategy": "Explain the role of the Reserve Bank of India (RBI) in supervising commercial banks (verifying cash reserve ratio and ensuring loans are granted to small borrowers, not just rich corporations).",
        "link": "<a href='ch21_globalisation_and_indian_economy.html' style='color:var(--primary); font-weight:700;'>Next Chapter: Globalisation &amp; Indian Economy Mock →</a>"
    },
    "social-science/ch21_globalisation_and_indian_economy.html": {
        "title": "Chapter 21: Globalisation and the Indian Economy",
        "subject": "Social Science (Economics)",
        "weightage": "5–6 Marks",
        "overview": "Production across countries by Multinational Corporations (MNCs), foreign direct investment (FDI), integration of markets through foreign trade, rapid advancement in IT and logistics, liberalization of foreign trade (1991), and WTO.",
        "cards": [
            ("🌐 MNCs & Global Production", "Multinational Corporations own or control production in more than one nation, setting up offices and factories in regions with cheap labor, raw materials, and supportive government policies."),
            ("💻 Technology & Container Logistics", "Telecommunications, internet, and refrigerated container shipping drastically reduced transport costs and enabled remote business process outsourcing (call centers, software)."),
            ("🔓 1991 Liberalization Policy", "Removing trade barriers and import quotas on foreign trade and investment. Allowed Indian producers to compete globally and attracted massive foreign direct investment (FDI)."),
            ("🏛️ World Trade Organization (WTO)", "International body promoting free global trade without tariffs. Critique: developed countries retain massive agricultural subsidies while forcing developing nations to open markets.")
        ],
        "strategy": "Explain how MNCs spread production (joint ventures, purchasing local companies, placing orders with small producers). State both benefits (more consumer choice) and challenges (small unorganized producers hurt).",
        "link": "<a href='../index.html' style='color:var(--primary); font-weight:700;'>Class 10 Portal Home — 48 Chapter Catalog →</a>"
    }
}

def generate_guide_html(guide_data):
    cards_html = ""
    for icon_title, body in guide_data["cards"]:
        cards_html += f"""      <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:8px; padding:16px;">
        <strong style="color:var(--primary); display:block; margin-bottom:6px; font-size:0.95rem;">{icon_title}</strong>
        <span style="font-size:0.82rem; color:var(--text-secondary); line-height:1.4; display:block;">{body}</span>
      </div>\n"""

    html = f"""
  <!-- Academic Chapter Guide & CBSE Board Blueprint (SEO & E-E-A-T Grounding) -->
  <section class="cbt-academic-guide" style="max-width:1200px; margin:40px auto; padding:0 20px;">
    <div style="border-top:1px solid var(--border-color); padding-top:32px; margin-bottom:24px;">
      <h2 style="font-size:1.35rem; font-weight:700; margin-bottom:12px; color:var(--text-primary);">
        📘 CBSE Class 10 {guide_data["subject"]} — {guide_data["title"]} Blueprint
      </h2>
      <p style="font-size:0.92rem; color:var(--text-secondary); line-height:1.6; margin-bottom:16px;">
        {guide_data["overview"]}
      </p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px; margin-bottom:24px;">
{cards_html}    </div>

    <div style="background:var(--bg-subtle); border-radius:8px; padding:18px; margin-bottom:24px; font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
      <strong style="color:var(--text-primary); display:block; margin-bottom:6px;">⚖️ Official CBSE Marking Scheme &amp; Strategy:</strong>
      • <strong>Marks Weightage:</strong> {guide_data["weightage"]} in annual board theory paper.<br>
      • <strong>Question Formats:</strong> Section A (Standalone MCQs &amp; Assertion-Reasoning), Section B/C (Short/Long Answers), Section E (Case Studies).<br>
      • <strong>Strategy &amp; Common Pitfalls:</strong> {guide_data["strategy"]}<br>
      • <strong>Curriculum Navigation:</strong> {guide_data["link"]}
    </div>
  </section>
"""
    return html

def process_all_chapters():
    updated_count = 0
    missing_count = 0

    for rel_path, guide_data in CHAPTER_GUIDES.items():
        file_path = os.path.join(ROOT, rel_path)
        if not os.path.exists(file_path):
            print(f"Warning: File not found: {file_path}")
            missing_count += 1
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if guide already exists
        if '<section class="cbt-academic-guide"' in content:
            # Replace existing section with updated one
            content = re.sub(
                r'<!-- Academic Chapter Guide & CBSE Board Blueprint.*?<\/section>',
                generate_guide_html(guide_data).strip(),
                content,
                flags=re.DOTALL
            )
        else:
            # Insert right before footer
            guide_block = generate_guide_html(guide_data)
            if '<!-- Site Footer -->' in content:
                content = content.replace('<!-- Site Footer -->', f"{guide_block}\n  <!-- Site Footer -->")
            elif '<footer class="site-footer">' in content:
                content = content.replace('<footer class="site-footer">', f"{guide_block}\n  <footer class=\"site-footer\">")
            else:
                print(f"Error: Could not locate footer insertion point in {rel_path}")
                continue

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        updated_count += 1

    print(f"Successfully processed {updated_count} / {len(CHAPTER_GUIDES)} Class 10 chapters!")
    if missing_count > 0:
        print(f"Missing files: {missing_count}")

if __name__ == '__main__':
    process_all_chapters()
