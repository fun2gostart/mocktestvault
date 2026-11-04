#!/usr/bin/env python3
"""
Generate authentic NEET UG speed drills:
- data/in/nta/neet_ug_drill1.json (45 Qs: 25 Biology, 10 Chemistry, 10 Physics)
- data/in/nta/neet_ug_drill2.json (45 Qs: 25 Biology, 10 Chemistry, 10 Physics)
Calibrated to NTA standard blueprint with +4 / -1 negative marking.
"""

import json

neet_ug_drill1 = [
    # Biology (Q1-Q25)
    {
        "id": 1,
        "question": "Which of the following cell organelles is responsible for the formation of glycoproteins and glycolipids in eukaryotic cells?",
        "options": ["Golgi apparatus", "Endoplasmic reticulum", "Lysosomes", "Peroxisomes"],
        "answer": 0,
        "subtopic": "Biology • Cell Biology",
        "explanation": "The Golgi apparatus (Golgi complex) is the primary site for post-translational modification and glycosylation of proteins and lipids synthesized by the endoplasmic reticulum, converting them into glycoproteins and glycolipids.",
        "citation": "NCERT Class 11 Biology Chapter 8 (Cell: The Unit of Life)"
    },
    {
        "id": 2,
        "question": "During which phase of meiosis do homologous chromosomes pair and undergo crossing over via synaptonemal complex formation?",
        "options": ["Pachytene of Prophase I", "Zygotene of Prophase I", "Diplotene of Prophase I", "Diakinesis of Prophase I"],
        "answer": 0,
        "subtopic": "Biology • Cell Cycle & Division",
        "explanation": "Homologous chromosomes synapsis begins in Zygotene, but genetic recombination and crossing over between non-sister chromatids, mediated by the recombinase enzyme complex, occurs specifically during the Pachytene stage of Prophase I.",
        "citation": "NCERT Class 11 Biology Chapter 10 (Cell Cycle and Cell Division)"
    },
    {
        "id": 3,
        "question": "The primary carbon dioxide acceptor in C4 plants during photosynthetic carbon fixation is:",
        "options": ["Phosphoenolpyruvate (PEP)", "Ribulose-1,5-bisphosphate (RuBP)", "Oxaloacetic acid (OAA)", "Phosphoglyceric acid (PGA)"],
        "answer": 0,
        "subtopic": "Biology • Plant Physiology",
        "explanation": "In C4 plants (such as maize and sugarcane), atmospheric CO₂ is initially accepted by phosphoenolpyruvate (PEP), a 3-carbon compound in the mesophyll cells, catalyzed by the enzyme PEP carboxylase (PEPcase) to form the 4-carbon acid oxaloacetate (OAA).",
        "citation": "NCERT Class 11 Biology Chapter 13 (Photosynthesis in Higher Plants)"
    },
    {
        "id": 4,
        "question": "During aerobic cellular respiration, the net yield of ATP synthesized per molecule of glucose oxidized via substrate-level phosphorylation exclusively in the Krebs cycle (citric acid cycle) is:",
        "options": ["2 ATP (or GTP)", "4 ATP", "36 ATP", "1 ATP"],
        "answer": 0,
        "subtopic": "Biology • Plant Physiology",
        "explanation": "For each turn of the citric acid cycle, one GTP (or ATP) is synthesized directly by substrate-level phosphorylation during the conversion of succinyl-CoA to succinate. Since one glucose molecule yields two molecules of acetyl-CoA, the Krebs cycle turns twice per glucose, generating exactly 2 ATP/GTP molecules.",
        "citation": "NCERT Class 11 Biology Chapter 14 (Respiration in Plants)"
    },
    {
        "id": 5,
        "question": "Which phytohormone is predominantly synthesized in ripening fruits and aging tissues and promotes senescence and fruit ripening?",
        "options": ["Ethylene", "Abscisic acid", "Auxin", "Gibberellin"],
        "answer": 0,
        "subtopic": "Biology • Plant Physiology",
        "explanation": "Ethylene (C₂H₄) is a gaseous plant growth regulator that promotes transverse growth, fruit ripening (by enhancing respiration rate, known as respiratory climacteric), and abscission of leaves and flowers.",
        "citation": "NCERT Class 11 Biology Chapter 15 (Plant Growth and Development)"
    },
    {
        "id": 6,
        "question": "In the human electrocardiogram (ECG), the depolarization of atria is represented by the:",
        "options": ["P wave", "QRS complex", "T wave", "ST segment"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "In a standard clinical ECG: The P wave represents electrical depolarization of the atria (atrial contraction); the QRS complex represents ventricular depolarization; and the T wave represents ventricular repolarization.",
        "citation": "NCERT Class 11 Biology Chapter 18 (Body Fluids and Circulation)"
    },
    {
        "id": 7,
        "question": "The counter-current multiplier system that maintains the hyperosmotic medullary gradient in mammalian kidneys operates between the:",
        "options": ["Henle's loop and Vasa recta", "Proximal convoluted tubule and Bowman's capsule", "Distal convoluted tubule and collecting duct", "Glomerulus and efferent arteriole"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "The counter-current mechanism operates between the descending and ascending limbs of the Loop of Henle and the corresponding limbs of the Vasa recta capillary network, concentrating interstitial fluid from 300 mOsmol/L in the cortex to 1200 mOsmol/L in the deep renal medulla.",
        "citation": "NCERT Class 11 Biology Chapter 19 (Excretory Products and their Elimination)"
    },
    {
        "id": 8,
        "question": "Which hormone acts on the kidneys to increase water reabsorption from the distal convoluted tubule and collecting duct, preventing diuresis?",
        "options": ["Antidiuretic hormone (Vasopressin)", "Atrial natriuretic peptide (ANP)", "Oxytocin", "Prolactin"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "Antidiuretic hormone (ADH / Vasopressin), released from the posterior pituitary (neurohypophysis) in response to hypothalamic osmoreceptor stimulation, increases the permeability of DCT and collecting ducts to water via aquaporin insertion, concentrating urine and preventing diuresis.",
        "citation": "NCERT Class 11 Biology Chapter 22 (Chemical Coordination and Integration)"
    },
    {
        "id": 9,
        "question": "The resting membrane potential of a mammalian neuron is maintained predominantly by:",
        "options": ["Na⁺/K⁺ ATPase pump (3 Na⁺ out for 2 K⁺ in)", "Passive influx of Na⁺ through voltage-gated channels", "Efflux of Cl⁻ ions into the extracellular space", "Active export of Ca²⁺ into synaptic vesicles"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "The resting membrane potential (-70 mV) is maintained by the active transport of ions against their electrochemical gradient by the electrogenic Na⁺/K⁺ ATPase pump, which expels 3 Na⁺ ions outward while importing 2 K⁺ ions inward, assisted by resting potassium leak channels.",
        "citation": "NCERT Class 11 Biology Chapter 21 (Neural Control and Coordination)"
    },
    {
        "id": 10,
        "question": "In human female reproductive physiology, ovulation is triggered directly by a rapid surge in which pituitary gonadotropin?",
        "options": ["Luteinizing hormone (LH)", "Follicle stimulating hormone (FSH)", "Progesterone", "Estrogen"],
        "answer": 0,
        "subtopic": "Biology • Human Reproduction",
        "explanation": "High estrogen levels produced by the mature Graafian follicle trigger a positive feedback on the anterior pituitary, causing a sudden spike in LH secretion (the 'LH surge') around day 14 of the menstrual cycle, inducing rupture of the Graafian follicle and release of the secondary oocyte (ovulation).",
        "citation": "NCERT Class 12 Biology Chapter 3 (Human Reproduction)"
    },
    {
        "id": 11,
        "question": "Which of the following is an example of a non-medicated Intrauterine Device (IUD)?",
        "options": ["Lippes loop", "CuT (Copper T)", "LNG-20", "Progestasert"],
        "answer": 0,
        "subtopic": "Biology • Reproductive Health",
        "explanation": "Lippes loop is a non-medicated, double-S shaped polyethylene IUD. CuT, Cu7, and Multiload 375 are copper-releasing IUDs, whereas Progestasert and LNG-20 are hormone-releasing IUDs.",
        "citation": "NCERT Class 12 Biology Chapter 4 (Reproductive Health)"
    },
    {
        "id": 12,
        "question": "In a Mendelian dihybrid cross between heterozygous round yellow seeded pea plants (RrYy × RrYy), what proportion of the F₂ progeny is expected to be homozygous recessive for both traits (rryy)?",
        "options": ["1 / 16", "3 / 16", "9 / 16", "1 / 4"],
        "answer": 0,
        "subtopic": "Biology • Genetics & Inheritance",
        "explanation": "The classical Mendelian dihybrid phenotypic ratio is 9:3:3:1. The double homozygous recessive genotype (rryy, wrinkled green seeds) occurs with a probability of P(rr) × P(yy) = (1/4) × (1/4) = 1/16.",
        "citation": "NCERT Class 12 Biology Chapter 5 (Principles of Inheritance and Variation)"
    },
    {
        "id": 13,
        "question": "A color-blind man marries a woman with normal vision whose father was color-blind. What is the probability that their son will be color-blind?",
        "options": ["50% (1/2)", "100%", "25% (1/4)", "0%"],
        "answer": 0,
        "subtopic": "Biology • Genetics & Inheritance",
        "explanation": "Color blindness is an X-linked recessive trait. The woman's father was color-blind (X^c Y), so she must carry the allele and be heterozygous: X^C X^c. The man is color-blind: X^c Y. A son receives his father's Y chromosome and has an equal (50%) chance of inheriting either X^C (normal vision) or X^c (color-blind) from his carrier mother.",
        "citation": "NCERT Class 12 Biology Chapter 5 (Principles of Inheritance and Variation)"
    },
    {
        "id": 14,
        "question": "During prokaryotic transcription, the core RNA polymerase enzyme requires which factor for specific promoter recognition and transcription initiation?",
        "options": ["Sigma (σ) factor", "Rho (ρ) factor", "TATA-binding protein", "Elongation factor Tu"],
        "answer": 0,
        "subtopic": "Biology • Molecular Basis of Inheritance",
        "explanation": "Prokaryotic RNA polymerase core enzyme (α₂ββ'ω) requires the transient association of the sigma (σ) subunit to form the holoenzyme capable of binding specifically to promoter consensus sequences (-10 Pribnow box and -35 sequence) to initiate transcription.",
        "citation": "NCERT Class 12 Biology Chapter 6 (Molecular Basis of Inheritance)"
    },
    {
        "id": 15,
        "question": "In the operon model of gene regulation in E. coli, the lac repressor protein is encoded by the:",
        "options": ["i gene", "z gene", "y gene", "a gene"],
        "answer": 0,
        "subtopic": "Biology • Molecular Basis of Inheritance",
        "explanation": "The lac repressor protein is synthesized constitutively by the regulatory i gene (inhibitor gene). In the absence of an inducer (lactose/allolactose), the repressor binds to the operator region (lacO), preventing RNA polymerase from transcribing the structural genes z, y, and a.",
        "citation": "NCERT Class 12 Biology Chapter 6 (Molecular Basis of Inheritance)"
    },
    {
        "id": 16,
        "question": "The semi-conservative nature of DNA replication was experimentally demonstrated using heavy isotope ¹⁵N in E. coli by:",
        "options": ["Meselson and Stahl", "Hershey and Chase", "Avery, MacLeod, and McCarty", "Griffith"],
        "answer": 0,
        "subtopic": "Biology • Molecular Basis of Inheritance",
        "explanation": "Matthew Meselson and Franklin Stahl (1958) utilized equilibrium density gradient centrifugation with cesium chloride (CsCl) on E. coli grown sequentially in ¹⁵NH₄Cl and ¹⁴NH₄Cl media to demonstrate that daughter DNA duplexes contain one parental and one newly synthesized strand.",
        "citation": "NCERT Class 12 Biology Chapter 6 (Molecular Basis of Inheritance)"
    },
    {
        "id": 17,
        "question": "The bones of forelimbs of whales, bats, cheetahs, and humans have the same anatomical plan (humerus, radius, ulna, carpals, metacarpals) but perform different functions. This represents:",
        "options": ["Homologous organs resulting from divergent evolution", "Analogous organs resulting from convergent evolution", "Vestigial organs resulting from natural selection", "Atavistic structures resulting from genetic drift"],
        "answer": 0,
        "subtopic": "Biology • Evolution",
        "explanation": "Homology indicates common evolutionary ancestry (divergent evolution) where ancestral anatomical structures are adapted to perform different functions in response to different ecological niches.",
        "citation": "NCERT Class 12 Biology Chapter 7 (Evolution)"
    },
    {
        "id": 18,
        "question": "In a population at Hardy-Weinberg equilibrium, the frequency of a recessive allele a is q = 0.4. The percentage of heterozygous individuals (Aa) in this population is:",
        "options": ["48%", "24%", "16%", "36%"],
        "answer": 0,
        "subtopic": "Biology • Evolution",
        "explanation": "In Hardy-Weinberg equilibrium: p + q = 1. Given q = 0.4, p = 1 - 0.4 = 0.6. The frequency of heterozygotes is 2pq = 2 × 0.6 × 0.4 = 0.48 = 48%.",
        "citation": "NCERT Class 12 Biology Chapter 7 (Evolution)"
    },
    {
        "id": 19,
        "question": "Which of the following restriction endonucleases produces sticky (cohesive) ends by making staggered cuts in the recognition palindromic sequence 5'-G↓AATTC-3'?",
        "options": ["EcoRI", "SmaI", "HaeIII", "EcoRV"],
        "answer": 0,
        "subtopic": "Biology • Biotechnology",
        "explanation": "EcoRI cleaves the phosphodiester backbone between G and A in the 5'-GAATTC-3' sequence, generating 5' single-stranded overhanging sticky ends (cohesive ends). SmaI and HaeIII make blunt cuts.",
        "citation": "NCERT Class 12 Biology Chapter 11 (Biotechnology: Principles and Processes)"
    },
    {
        "id": 20,
        "question": "The correct sequence of steps in each cycle of Polymerase Chain Reaction (PCR) is:",
        "options": ["Denaturation → Primer Annealing → Primer Extension", "Primer Annealing → Denaturation → Extension", "Extension → Denaturation → Primer Annealing", "Denaturation → Extension → Primer Annealing"],
        "answer": 0,
        "subtopic": "Biology • Biotechnology",
        "explanation": "Each PCR cycle consists of three thermal steps: (1) Denaturation at ~94-96 °C to melt dsDNA into single strands, (2) Annealing of oligonucleotide primers at ~50-60 °C, and (3) Extension at ~72 °C catalyzed by thermostable Taq DNA polymerase.",
        "citation": "NCERT Class 12 Biology Chapter 11 (Biotechnology: Principles and Processes)"
    },
    {
        "id": 21,
        "question": "Bt cotton plants are resistant to lepidopteran pests (such as cotton bollworms) due to the incorporation of genes encoding Cry proteins isolated from:",
        "options": ["Bacillus thuringiensis", "Agrobacterium tumefaciens", "Thermus aquaticus", "Escherichia coli"],
        "answer": 0,
        "subtopic": "Biology • Biotechnology Applications",
        "explanation": "Bt toxin genes (cryIAc and cryIIAb) were cloned from the soil bacterium Bacillus thuringiensis. In the alkaline pH of the insect midgut, the inactive protoxin is solubilized and cleaved into active endotoxin that binds to epithelial cells, creating pores that cause cell lysis and death.",
        "citation": "NCERT Class 12 Biology Chapter 12 (Biotechnology and its Applications)"
    },
    {
        "id": 22,
        "question": "The pyramid of biomass in a typical open marine or aquatic ecosystem is generally:",
        "options": ["Inverted", "Upright", "Spindle-shaped", "Horizontal"],
        "answer": 0,
        "subtopic": "Biology • Ecology & Environment",
        "explanation": "In aquatic ecosystems (like oceans and lakes), the biomass of primary producers (phytoplankton) at any given instant is very small compared to the biomass of primary and secondary consumers (zooplankton and fish) due to the rapid turnover and short lifespan of phytoplankton. Thus, the standing biomass pyramid is inverted.",
        "citation": "NCERT Class 12 Biology Chapter 14 (Ecosystem)"
    },
    {
        "id": 23,
        "question": "According to Robert May's global estimates, the total number of species currently existing on Earth is approximately:",
        "options": ["7 million", "1.7 million", "20 to 50 million", "100 million"],
        "answer": 0,
        "subtopic": "Biology • Ecology & Environment",
        "explanation": "While approximately 1.5 to 1.7 million living species have been scientifically described, ecologist Robert May applied conservative statistical extrapolations to estimate the total global species richness at approximately 7 million species.",
        "citation": "NCERT Class 12 Biology Chapter 15 (Biodiversity and Conservation)"
    },
    {
        "id": 24,
        "question": "Which of the following is an example of ex-situ conservation of endangered species?",
        "options": ["Zoological parks and Botanical gardens", "National Parks", "Wildlife Sanctuaries", "Biosphere Reserves"],
        "answer": 0,
        "subtopic": "Biology • Ecology & Environment",
        "explanation": "Ex-situ ('off-site') conservation involves removing threatened animal and plant species from their natural wild habitat and maintaining them under human care in protective facilities such as zoological gardens, botanical gardens, wildlife safari parks, seed banks, and cryopreservation vaults.",
        "citation": "NCERT Class 12 Biology Chapter 15 (Biodiversity and Conservation)"
    },
    {
        "id": 25,
        "question": "The high Biochemical Oxygen Demand (BOD) value of a freshwater water sample indicates that:",
        "options": ["The water is heavily polluted with organic matter", "The water is highly pure and saturated with dissolved oxygen", "The water has zero microbial activity", "The water contains high concentrations of heavy metals only"],
        "answer": 0,
        "subtopic": "Biology • Environmental Issues",
        "explanation": "Biochemical Oxygen Demand (BOD) measures the amount of dissolved oxygen consumed by aerobic microorganisms to oxidize biodegradable organic matter present in a water sample. A higher BOD value indicates heavy organic sewage pollution and depleted dissolved oxygen.",
        "citation": "NCERT Class 12 Biology Chapter 16 (Environmental Issues)"
    },

    # Chemistry (Q26-Q35)
    {
        "id": 26,
        "question": "According to Henry's law, the solubility of a gas in a liquid at constant temperature is directly proportional to the partial pressure of the gas above the liquid. The Henry's law constant K_H:",
        "options": ["Increases with increase in temperature, resulting in lower gas solubility", "Decreases with increase in temperature", "Is independent of both temperature and nature of gas", "Increases with decrease in temperature"],
        "answer": 0,
        "subtopic": "Chemistry • Solutions",
        "explanation": "Henry's law is p = K_H × x. Higher values of K_H at a given pressure correspond to lower solubility x. Since gas dissolution in liquid is an exothermic process (ΔH_solution < 0), solubility decreases as temperature rises, which means K_H increases with increasing temperature.",
        "citation": "NCERT Class 12 Chemistry Chapter 2 (Solutions)"
    },
    {
        "id": 27,
        "question": "The solubility product of AgCl is K_sp = 1.0 × 10⁻¹⁰ at 298 K. Its solubility in a 0.1 M aqueous NaCl solution is:",
        "options": ["1.0 × 10⁻⁹ mol/L", "1.0 × 10⁻⁵ mol/L", "1.0 × 10⁻¹⁰ mol/L", "0.1 mol/L"],
        "answer": 0,
        "subtopic": "Chemistry • Ionic Equilibrium",
        "explanation": "In 0.1 M NaCl, [Cl⁻] ≈ 0.1 M due to complete dissociation of NaCl. By the common ion effect: K_sp = [Ag⁺][Cl⁻] ⇒ 1.0 × 10⁻¹⁰ = s × 0.1 ⇒ s = 1.0 × 10⁻⁹ mol/L.",
        "citation": "NCERT Class 11 Chemistry Chapter 7 (Equilibrium)"
    },
    {
        "id": 28,
        "question": "The addition of HBr to propene (CH₃-CH=CH₂) in the presence of benzoyl peroxide yields primarily:",
        "options": ["1-Bromopropane (n-propyl bromide)", "2-Bromopropane (isopropyl bromide)", "1,2-Dibromopropane", "2,2-Dibromopropane"],
        "answer": 0,
        "subtopic": "Chemistry • Hydrocarbons",
        "explanation": "In the presence of organic peroxides, HBr undergoes free-radical addition (the Kharasch effect or peroxide effect). The bromine radical attacks the terminal sp² carbon of propene to generate the more stable 2° alkyl radical, yielding 1-bromopropane via anti-Markovnikov regioselectivity.",
        "citation": "NCERT Class 11 Chemistry Chapter 13 (Hydrocarbons)"
    },
    {
        "id": 29,
        "question": "According to IUPAC nomenclature, the coordination compound [Co(NH₃)₅(CO₃)]Cl is named as:",
        "options": ["Pentaamminecarbonatocobalt(III) chloride", "Pentaamminecarbonatocobalt(II) chloride", "Carbonatopentaamminecobalt(III) chloride", "Pentaamminechlorocobalt(III) carbonate"],
        "answer": 0,
        "subtopic": "Chemistry • Coordination Compounds",
        "explanation": "Ligands are named alphabetically: 'ammine' (NH₃) precedes 'carbonato' (CO₃²⁻). Cobalt oxidation state: Co + 5(0) + (-2) + (-1) = 0 ⇒ Co = +3. The IUPAC name is pentaamminecarbonatocobalt(III) chloride.",
        "citation": "NCERT Class 12 Chemistry Chapter 9 (Coordination Compounds)"
    },
    {
        "id": 30,
        "question": "How many Coulombs of electric charge are required to electroplate 54 g of silver (Ag, atomic mass = 108 g/mol) from an aqueous AgNO₃ solution? (1 Faraday ≈ 96500 C)",
        "options": ["48,250 C", "96,500 C", "193,000 C", "24,125 C"],
        "answer": 0,
        "subtopic": "Chemistry • Electrochemistry",
        "explanation": "Ag⁺ + e⁻ → Ag(s). 1 mole of Ag (108 g) requires 1 Faraday of charge (96,500 C). For 54 g of Ag (0.50 moles): Q = 0.50 × 96,500 C = 48,250 C.",
        "citation": "NCERT Class 12 Chemistry Chapter 3 (Electrochemistry)"
    },
    {
        "id": 31,
        "question": "Which of the following aldehydes lacks α-hydrogens and therefore undergoes the Cannizzaro reaction upon treatment with concentrated KOH?",
        "options": ["Benzaldehyde (C₆H₅CHO)", "Acetaldehyde (CH₃CHO)", "Propionaldehyde (CH₃CH₂CHO)", "Phenylethanal (C₆H₅CH₂CHO)"],
        "answer": 0,
        "subtopic": "Chemistry • Aldehydes & Ketones",
        "explanation": "Aldehydes that lack α-hydrogen atoms (such as benzaldehyde and formaldehyde) undergo disproportionation (self-oxidation and reduction) in concentrated alkali: 2 C₆H₅CHO + KOH → C₆H₅COOK + C₆H₅CH₂OH (potassium benzoate and benzyl alcohol).",
        "citation": "NCERT Class 12 Chemistry Chapter 12 (Aldehydes, Ketones and Carboxylic Acids)"
    },
    {
        "id": 32,
        "question": "According to the Hardy-Schulze rule, which of the following ions has the highest flocculating (coagulating) power for a negatively charged arsenious sulfide (As₂S₃) sol?",
        "options": ["Al³⁺", "Ba²⁺", "Na⁺", "PO₄³⁻"],
        "answer": 0,
        "subtopic": "Chemistry • Surface Chemistry",
        "explanation": "The Hardy-Schulze rule states that the coagulating power of an electrolyte depends on the valency of the active flocculating ion carrying a charge opposite to that of the colloidal particles. For a negatively charged sol, cations are effective and coagulating power follows Al³⁺ > Ba²⁺ > Na⁺.",
        "citation": "NCERT Class 12 Chemistry Chapter 5 (Surface Chemistry)"
    },
    {
        "id": 33,
        "question": "Reductive ozonolysis (O₃ followed by Zn/H₂O) of 2-methylbut-2-ene yields:",
        "options": ["Propan-2-one (acetone) and ethanal (acetaldehyde)", "Two molecules of acetone", "Two molecules of acetaldehyde", "Formaldehyde and butan-2-one"],
        "answer": 0,
        "subtopic": "Chemistry • Hydrocarbons",
        "explanation": "2-Methylbut-2-ene is (CH₃)₂C=CH-CH₃. Cleavage of the double bond by ozonolysis followed by zinc dust reduction splits the C=C bond: the (CH₃)₂C= portion becomes acetone (CH₃COCH₃) and the =CH-CH₃ portion becomes acetaldehyde (CH₃CHO).",
        "citation": "NCERT Class 11 Chemistry Chapter 13 (Hydrocarbons)"
    },
    {
        "id": 34,
        "question": "The total number of lone pairs of electrons in a molecule of chlorine trifluoride (ClF₃) is:",
        "options": ["11", "2", "3", "9"],
        "answer": 0,
        "subtopic": "Chemistry • Chemical Bonding",
        "explanation": "The central chlorine atom has 7 valence electrons: 3 shared in single bonds with fluorines + 2 lone pairs = 2 lone pairs on Cl. Each of the three fluorine atoms has 3 non-bonding lone pairs = 3 × 3 = 9 lone pairs. Total lone pairs in the molecule = 2 (on Cl) + 9 (on F atoms) = 11 lone pairs.",
        "citation": "NCERT Class 12 Chemistry Chapter 7 (p-Block Elements)"
    },
    {
        "id": 35,
        "question": "Which of the following vitamins is water-soluble and its deficiency causes scurvy characterized by spongy bleeding gums?",
        "options": ["Vitamin C (Ascorbic acid)", "Vitamin A (Retinol)", "Vitamin D (Cholecalciferol)", "Vitamin K (Phylloquinone)"],
        "answer": 0,
        "subtopic": "Chemistry • Biomolecules",
        "explanation": "Vitamin C (ascorbic acid) and B-complex vitamins are water-soluble and cannot be stored in the body. Vitamin C is essential for collagen synthesis; its deficiency leads to scurvy. Vitamins A, D, E, and K are fat-soluble.",
        "citation": "NCERT Class 12 Chemistry Chapter 14 (Biomolecules)"
    },

    # Physics (Q36-Q45)
    {
        "id": 36,
        "question": "The dimensional formula of the universal gravitational constant G is:",
        "options": ["[M⁻¹ L³ T⁻²]", "[M L³ T⁻²]", "[M⁻¹ L² T⁻¹]", "[M L² T⁻²]"],
        "answer": 0,
        "subtopic": "Physics • Units & Dimensions",
        "explanation": "From Newton's law of universal gravitation: F = G m₁ m₂ / r² ⇒ G = F r² / m². Dimensions of force are [M L T⁻²], length is [L], and mass is [M]. Thus, [G] = [M L T⁻²][L²] / [M²] = [M⁻¹ L³ T⁻²].",
        "citation": "NCERT Class 11 Physics Chapter 2 (Units and Measurements)"
    },
    {
        "id": 37,
        "question": "A car negotiates a curved circular road of radius 40 m banked at angle θ. If the safe speed without relying on friction is 20 m/s, the banking angle θ is (g = 10 m/s²):",
        "options": ["45°", "30°", "60°", "15°"],
        "answer": 0,
        "subtopic": "Physics • Circular Motion",
        "explanation": "For an optimally banked curve without lateral friction: tan θ = v² / (r g). Given v = 20 m/s, r = 40 m, and g = 10 m/s²: tan θ = (20)² / (40 × 10) = 400 / 400 = 1 ⇒ θ = 45°.",
        "citation": "NCERT Class 11 Physics Chapter 5 (Laws of Motion)"
    },
    {
        "id": 38,
        "question": "A cylindrical tank filled with water to a depth of 5.0 m has an orifice opened at a depth of 3.2 m below the free surface. The speed of efflux of water from the hole is (g = 9.8 m/s²):",
        "options": ["7.92 m/s", "9.90 m/s", "6.26 m/s", "4.00 m/s"],
        "answer": 0,
        "subtopic": "Physics • Fluid Mechanics",
        "explanation": "By Torricelli's Law of efflux derived from Bernoulli's equation: v = √(2gh), where h is the depth of the orifice below the free liquid surface. Here h = 3.2 m. v = √(2 × 9.8 × 3.2) = √(62.72) ≈ 7.92 m/s.",
        "citation": "NCERT Class 11 Physics Chapter 10 (Mechanical Properties of Fluids)"
    },
    {
        "id": 39,
        "question": "According to Wien's displacement law, a black body at temperature 2000 K emits maximum radiation at wavelength λ_max = 1450 nm. If its temperature is increased to 4000 K, λ_max will be:",
        "options": ["725 nm", "2900 nm", "1450 nm", "362.5 nm"],
        "answer": 0,
        "subtopic": "Physics • Thermal Properties",
        "explanation": "Wien's displacement law states that λ_max × T = b (constant). Thus, λ₁ T₁ = λ₂ T₂ ⇒ λ₂ = λ₁ (T₁ / T₂) = 1450 nm × (2000 / 4000) = 1450 / 2 = 725 nm.",
        "citation": "NCERT Class 11 Physics Chapter 11 (Thermal Properties of Matter)"
    },
    {
        "id": 40,
        "question": "Two equal positive point charges separated by distance d in vacuum repel each other with force F. When placed at the same separation inside an oil dielectric medium (dielectric constant K = 4), the electrostatic force becomes:",
        "options": ["F / 4", "4 F", "F / 16", "F / 2"],
        "answer": 0,
        "subtopic": "Physics • Electrostatics",
        "explanation": "Coulomb's force in a medium of dielectric constant K is F_med = F_vac / K. With K = 4, the repulsive force is reduced by a factor of 4: F' = F / 4.",
        "citation": "NCERT Class 12 Physics Chapter 1 (Electric Charges and Fields)"
    },
    {
        "id": 41,
        "question": "A cylindrical copper wire of resistance 4 Ω is uniformly stretched until its length is doubled. Its new resistance is:",
        "options": ["16 Ω", "8 Ω", "2 Ω", "4 Ω"],
        "answer": 0,
        "subtopic": "Physics • Current Electricity",
        "explanation": "Since the volume of the wire remains constant during stretching (V = A × L), doubling the length (L' = 2L) halves the cross-sectional area (A' = A/2). Resistance R = ρ L / A, so R' = ρ (2L) / (A/2) = 4 (ρ L / A) = 4 R = 4 × 4 Ω = 16 Ω.",
        "citation": "NCERT Class 12 Physics Chapter 3 (Current Electricity)"
    },
    {
        "id": 42,
        "question": "Two thin convex lenses of focal lengths +20 cm and +30 cm are placed in coaxial contact. The power of the lens combination is:",
        "options": ["+8.33 D", "+5.00 D", "+1.20 D", "+10.0 D"],
        "answer": 0,
        "subtopic": "Physics • Ray Optics",
        "explanation": "Power of a lens is P = 1 / f (in meters). For the first lens: P₁ = 100 / 20 = +5.0 D. For the second lens: P₂ = 100 / 30 = +3.33 D. Total equivalent power is P = P₁ + P₂ = 5.0 + 3.33 = +8.33 D.",
        "citation": "NCERT Class 12 Physics Chapter 9 (Ray Optics and Optical Instruments)"
    },
    {
        "id": 43,
        "question": "A radioactive sample has a half-life of 20 days. The percentage of initial undecayed radioactive nuclei remaining after 60 days is:",
        "options": ["12.5%", "25%", "6.25%", "50%"],
        "answer": 0,
        "subtopic": "Physics • Modern Physics",
        "explanation": "Number of elapsed half-lives is n = total time / T_(1/2) = 60 / 20 = 3 half-lives. Fraction remaining is (1/2)ⁿ = (1/2)³ = 1/8 = 0.125 = 12.5%.",
        "citation": "NCERT Class 12 Physics Chapter 13 (Nuclei)"
    },
    {
        "id": 44,
        "question": "In the Bohr model of the hydrogen atom, the radius of the nth electronic orbit is proportional to:",
        "options": ["n²", "n", "1 / n", "1 / n²"],
        "answer": 0,
        "subtopic": "Physics • Atoms",
        "explanation": "According to Bohr's postulate: m v r = n h / (2π) and Coulomb force k e² / r² = m v² / r. Solving for radius gives r_n = (n² h² ε₀) / (π m e²) = a₀ n² / Z. For hydrogen (Z = 1), r_n ∝ n².",
        "citation": "NCERT Class 12 Physics Chapter 12 (Atoms)"
    },
    {
        "id": 45,
        "question": "A silicon p-n junction diode operates under forward bias. As the forward bias voltage exceeds the threshold knee voltage (~0.7 V):",
        "options": ["The depletion layer width decreases and diffusion current increases exponentially", "The depletion layer width increases and drift current dominates", "The barrier height increases linearly", "The diode breaks down into avalanche multiplication"],
        "answer": 0,
        "subtopic": "Physics • Semiconductor Electronics",
        "explanation": "Under forward bias (p-side connected to positive, n-side to negative), the external potential opposes and neutralizes the built-in barrier potential. The depletion layer narrows, permitting majority charge carriers (holes and electrons) to diffuse across the junction, causing current to rise exponentially.",
        "citation": "NCERT Class 12 Physics Chapter 14 (Semiconductor Electronics)"
    }
]

# Generate NEET UG Drill 2 (45 Questions)
neet_ug_drill2 = [
    # Biology (Q1-Q25)
    {
        "id": 1,
        "question": "Which specialized cell junction prevents leakage of substances across epithelial tissue layers?",
        "options": ["Tight junctions", "Adhering junctions", "Gap junctions", "Desmosomes"],
        "answer": 0,
        "subtopic": "Biology • Animal Tissues",
        "explanation": "Tight junctions form water-tight seals between adjacent plasma membranes, preventing extracellular fluid and ions from leaking across epithelial sheets (such as in the stomach lining and renal tubules).",
        "citation": "NCERT Class 11 Biology Chapter 7 (Structural Organisation in Animals)"
    },
    {
        "id": 2,
        "question": "Ribosomes of eukaryotic cytoplasm and mitochondrial matrix are characterized respectively as:",
        "options": ["80S and 70S", "70S and 80S", "80S and 80S", "70S and 70S"],
        "answer": 0,
        "subtopic": "Biology • Cell Biology",
        "explanation": "Eukaryotic cytosolic ribosomes are 80S (composed of 60S and 40S subunits), whereas ribosomes located inside mitochondria and chloroplasts are 70S (composed of 50S and 30S subunits), reflecting their endosymbiotic prokaryotic origin.",
        "citation": "NCERT Class 11 Biology Chapter 8 (Cell: The Unit of Life)"
    },
    {
        "id": 3,
        "question": "In which anatomical layer of dicot root do Caspian strips composed of suberin occur in the radial and tangential cell walls?",
        "options": ["Endodermis", "Pericycle", "Epidermis", "Cortex"],
        "answer": 0,
        "subtopic": "Biology • Plant Anatomy",
        "explanation": "The endodermis is the innermost cortical layer. Its cells possess band-like thickenings of waterproof, waxy suberin called Casparian strips, blocking apoplastic water transport and forcing water through the symplast.",
        "citation": "NCERT Class 11 Biology Chapter 6 (Anatomy of Flowering Plants)"
    },
    {
        "id": 4,
        "question": "Which of the following mineral elements is an essential constituent of the chlorophyll porphyrin ring and acts as an activator for RuBisCO and PEPcase?",
        "options": ["Magnesium (Mg²⁺)", "Iron (Fe²⁺)", "Manganese (Mn²⁺)", "Zinc (Zn²⁺)"],
        "answer": 0,
        "subtopic": "Biology • Mineral Nutrition",
        "explanation": "Magnesium (Mg²⁺) is the central divalent atom coordinated inside the tetrapyrrole porphyrin head of the chlorophyll molecule and serves as a vital cofactor for key carbon fixation enzymes RuBisCO and PEP carboxylase.",
        "citation": "NCERT Class 11 Biology Chapter 12 (Mineral Nutrition)"
    },
    {
        "id": 5,
        "question": "Photolysis of water (water-splitting complex) during the light reaction of photosynthesis is associated with:",
        "options": ["Photosystem II (PS II) located on inner thylakoid membrane", "Photosystem I (PS I)", "Stroma lamellae", "Cytochrome b6f complex"],
        "answer": 0,
        "subtopic": "Biology • Plant Physiology",
        "explanation": "The oxygen-evolving complex (water splitting complex) containing manganese and calcium ions is physically associated with Photosystem II (P680) on the lumen side of the thylakoid membrane.",
        "citation": "NCERT Class 11 Biology Chapter 13 (Photosynthesis in Higher Plants)"
    },
    {
        "id": 6,
        "question": "The respiratory quotient (RQ = Volume of CO₂ evolved / Volume of O₂ consumed) for the complete oxidation of tripalmitin (fat) is approximately:",
        "options": ["0.7", "1.0", "0.9", "0.5"],
        "answer": 0,
        "subtopic": "Biology • Plant Physiology",
        "explanation": "For tripalmitin: 2 C₅₁H₉₈O₆ + 145 O₂ → 102 CO₂ + 98 H₂O + energy. RQ = 102 CO₂ / 145 O₂ ≈ 0.7. For carbohydrates RQ = 1.0; for proteins RQ ≈ 0.9.",
        "citation": "NCERT Class 11 Biology Chapter 14 (Respiration in Plants)"
    },
    {
        "id": 7,
        "question": "Parietal (oxyntic) cells in the mucosal epithelium of the human stomach secrete:",
        "options": ["Hydrochloric acid (HCl) and Castle's intrinsic factor", "Pepsinogen", "Mucus", "Gastrin"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "Oxyntic (parietal) cells in gastric glands secrete hydrochloric acid (which activates pepsinogen to pepsin) and Castle's intrinsic factor (essential for intestinal absorption of vitamin B₁₂ in the ileum). Chief cells secrete pepsinogen.",
        "citation": "NCERT Class 11 Biology Chapter 16 (Digestion and Absorption)"
    },
    {
        "id": 8,
        "question": "Under normal physiological conditions, what volume of oxygen (O₂) is delivered to tissues by every 100 mL of oxygenated arterial blood?",
        "options": ["5 mL", "20 mL", "4 mL", "15 mL"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "Every 100 mL of oxygenated blood carries approximately 20 mL of O₂. Under resting physiological conditions, tissues extract approximately 25% of this content, delivering ~5 mL of O₂ per 100 mL of blood.",
        "citation": "NCERT Class 11 Biology Chapter 17 (Breathing and Exchange of Gases)"
    },
    {
        "id": 9,
        "question": "The functional contractile unit of a human skeletal muscle myofibril bounded by two successive Z-lines is called a:",
        "options": ["Sarcomere", "Sarcolemma", "Sarcoplasmic reticulum", "A-band"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "A sarcomere is the basic structural and functional contractile unit of striated muscle tissue, defined as the region between two adjacent Z-discs (Z-lines), containing an A-band flanked by two half I-bands.",
        "citation": "NCERT Class 11 Biology Chapter 20 (Locomotion and Movement)"
    },
    {
        "id": 10,
        "question": "Which endocrine gland produces melatonin, regulating the 24-hour diurnal (circadian) sleep-wake rhythm in humans?",
        "options": ["Pineal gland", "Thyroid gland", "Thymus gland", "Adrenal cortex"],
        "answer": 0,
        "subtopic": "Biology • Human Physiology",
        "explanation": "The pineal gland, situated on the dorsal side of the forebrain, secretes the indoleamine hormone melatonin, which coordinates the 24-hour diurnal cycle, body temperature, pigmentation, and menstrual cycles.",
        "citation": "NCERT Class 11 Biology Chapter 22 (Chemical Coordination and Integration)"
    },
    {
        "id": 11,
        "question": "The primary structural component of the exine layer of flowering plant pollen grains, which makes them extraordinarily resistant to chemical, thermal, and enzymatic degradation, is:",
        "options": ["Sporopollenin", "Cellulose", "Pectin", "Chitin"],
        "answer": 0,
        "subtopic": "Biology • Sexual Reproduction in Flowering Plants",
        "explanation": "Sporopollenin, a highly cross-linked biopolymer composed of fatty acids and phenolics, forms the hard exine of pollen grains. No known enzyme degrades sporopollenin, enabling pollen to fossilize well.",
        "citation": "NCERT Class 12 Biology Chapter 2 (Sexual Reproduction in Flowering Plants)"
    },
    {
        "id": 12,
        "question": "Double fertilization in angiosperms is defined as the fusion of:",
        "options": ["One male gamete with egg (syngamy) and the second male gamete with secondary nucleus (triple fusion)", "Two male gametes with a single egg", "One male gamete with synergid and one with antipodal", "Two polar nuclei fusing together"],
        "answer": 0,
        "subtopic": "Biology • Sexual Reproduction in Flowering Plants",
        "explanation": "Double fertilization involves: (1) Syngamy: One sperm nucleus fuses with the egg nucleus (n + n) to form the diploid zygote (2n), and (2) Triple fusion: The second sperm nucleus fuses with two polar nuclei (n + 2n) to form the triploid primary endosperm nucleus (PEN, 3n).",
        "citation": "NCERT Class 12 Biology Chapter 2 (Sexual Reproduction in Flowering Plants)"
    },
    {
        "id": 13,
        "question": "Which of the following is a sexually transmitted disease caused by the bacterium Treponema pallidum?",
        "options": ["Syphilis", "Gonorrhea", "Chlamydiasis", "Genital warts"],
        "answer": 0,
        "subtopic": "Biology • Reproductive Health",
        "explanation": "Syphilis is caused by the spirochete bacterium Treponema pallidum. Gonorrhea is caused by Neisseria gonorrhoeae, while genital warts are caused by Human Papillomavirus (HPV).",
        "citation": "NCERT Class 12 Biology Chapter 4 (Reproductive Health)"
    },
    {
        "id": 14,
        "question": "In humans, Turner's syndrome is a chromosomal disorder caused by:",
        "options": ["Monosomy of X chromosome (44 + XO)", "Trisomy of chromosome 21 (47, +21)", "XXY karyotype (44 + XXY)", "Trisomy of chromosome 18"],
        "answer": 0,
        "subtopic": "Biology • Genetics & Chromosomes",
        "explanation": "Turner's syndrome results from monosomy of the sex chromosome (45, XO). Affected females are sterile with rudimentary ovaries, short stature, webbed neck, and lack of secondary sexual characteristics.",
        "citation": "NCERT Class 12 Biology Chapter 5 (Principles of Inheritance and Variation)"
    },
    {
        "id": 15,
        "question": "The unwinding of the DNA double helix during replication at the replication fork is catalyzed by the enzyme:",
        "options": ["DNA helicase", "DNA ligase", "Topoisomerase", "RNA primase"],
        "answer": 0,
        "subtopic": "Biology • Molecular Biology",
        "explanation": "DNA helicase breaks hydrogen bonds between complementary base pairs to unwind the double helix ahead of the replication fork. Single-strand binding proteins (SSBs) stabilize single strands, and topoisomerase relieves supercoiling tension.",
        "citation": "NCERT Class 12 Biology Chapter 6 (Molecular Basis of Inheritance)"
    },
    {
        "id": 16,
        "question": "The initiation codon in eukaryotic and prokaryotic mRNA is AUG, which codes for which amino acid?",
        "options": ["Methionine", "Valine", "Phenylalanine", "Tryptophan"],
        "answer": 0,
        "subtopic": "Biology • Molecular Biology",
        "explanation": "AUG serves dual functions: (1) It acts as the universal initiation codon for protein translation, and (2) It encodes the amino acid methionine (formyl-methionine in prokaryotes).",
        "citation": "NCERT Class 12 Biology Chapter 6 (Molecular Basis of Inheritance)"
    },
    {
        "id": 26,
        "question": "Darwin's finches of the Galápagos Islands represent a classic textbook example of:",
        "options": ["Adaptive radiation", "Convergent evolution", "Industrial melanism", "Artificial selection"],
        "answer": 0,
        "subtopic": "Biology • Evolution",
        "explanation": "Darwin's finches diversified from an original ancestral seed-eating finch on the South American mainland into varied beak shapes adapted for insectivorous, vegetarian, and cactus-feeding niches across island habitats, exemplifying adaptive radiation.",
        "citation": "NCERT Class 12 Biology Chapter 7 (Evolution)"
    },
    {
        "id": 17,
        "question": "The infectious infective stage of the malaria parasite Plasmodium that is transmitted into the human bloodstream during the bite of an infected female Anopheles mosquito is:",
        "options": ["Sporozoite", "Trophozoite", "Merozoite", "Gametocyte"],
        "answer": 0,
        "subtopic": "Biology • Human Health & Disease",
        "explanation": "Sporozoites stored in the salivary glands of the female Anopheles mosquito enter human blood during feeding, migrate to the liver to reproduce asexually, and later emerge as merozoites to invade RBCs.",
        "citation": "NCERT Class 12 Biology Chapter 8 (Human Health and Disease)"
    },
    {
        "id": 18,
        "question": "Which antibody class is the most abundant in colostrum (first mother's milk) and provides natural passive immunity to newborns?",
        "options": ["IgA", "IgG", "IgM", "IgE"],
        "answer": 0,
        "subtopic": "Biology • Human Health & Disease",
        "explanation": "Secretory IgA is the predominant immunoglobulin present in colostrum, saliva, and tears, protecting mucosal surfaces against pathogens and conferring passive immunity to breastfed infants.",
        "citation": "NCERT Class 12 Biology Chapter 8 (Human Health and Disease)"
    },
    {
        "id": 19,
        "question": "The enzyme used in cheese production that curdles milk protein casein is:",
        "options": ["Rennin (Chymosin)", "Amylase", "Lipase", "Protease"],
        "answer": 0,
        "subtopic": "Biology • Microbes in Human Welfare",
        "explanation": "Rennin (chymosin) is a proteolytic enzyme that coagulates milk by converting soluble casein into insoluble paracasein in the presence of calcium ions, forming cheese curds.",
        "citation": "NCERT Class 12 Biology Chapter 10 (Microbes in Human Welfare)"
    },
    {
        "id": 20,
        "question": "In agarose gel electrophoresis of DNA fragments, DNA fragments migrate toward which electrode and separate based on what physical property?",
        "options": ["Toward anode (+) based on molecular size", "Toward cathode (-) based on charge", "Toward anode (+) based on base composition", "Toward cathode (-) based on shape"],
        "answer": 0,
        "subtopic": "Biology • Biotechnology",
        "explanation": "DNA molecules carry a negative charge due to their phosphate backbone and therefore migrate toward the positive anode (+). The agarose gel acts as a sieve, so smaller fragments migrate faster and further than larger fragments.",
        "citation": "NCERT Class 12 Biology Chapter 11 (Biotechnology: Principles and Processes)"
    },
    {
        "id": 21,
        "question": "Thermus aquaticus is the source bacterium for which thermostable enzyme critical to Polymerase Chain Reaction (PCR)?",
        "options": ["Taq polymerase", "Vent polymerase", "DNA ligase", "Reverse transcriptase"],
        "answer": 0,
        "subtopic": "Biology • Biotechnology",
        "explanation": "Taq DNA polymerase is isolated from the thermophilic bacterium Thermus aquaticus, which thrives in hydrothermal vents. It remains stable and enzymatically active even at 95 °C during PCR denaturation cycles.",
        "citation": "NCERT Class 12 Biology Chapter 11 (Biotechnology: Principles and Processes)"
    },
    {
        "id": 22,
        "question": "An interaction between two species where one species benefits while the other is neither helped nor harmed (+ / 0) is classified as:",
        "options": ["Commensalism", "Mutualism", "Amensalism", "Parasitism"],
        "answer": 0,
        "subtopic": "Biology • Ecology",
        "explanation": "Commensalism (+/0) is an interspecific interaction in which one organism derives benefit while the other is unaffected. Examples include barnacles on whales and epiphytic orchids growing on mango branches.",
        "citation": "NCERT Class 12 Biology Chapter 13 (Organisms and Populations)"
    },
    {
        "id": 23,
        "question": "In an ecological food chain, what percentage of chemical energy is transferred from one trophic level to the next higher trophic level according to Lindeman's efficiency law?",
        "options": ["10%", "1%", "50%", "20%"],
        "answer": 0,
        "subtopic": "Biology • Ecosystem",
        "explanation": "Raymond Lindeman's 10% law of ecological efficiency states that on average only about 10% of the energy stored in organic matter at one trophic level is converted into biomass at the next trophic level, with the rest lost as metabolic heat.",
        "citation": "NCERT Class 12 Biology Chapter 14 (Ecosystem)"
    },
    {
        "id": 24,
        "question": "The Montreux Record is a register of wetland sites on the List of Wetlands of International Importance under which international convention?",
        "options": ["Ramsar Convention", "Kyoto Protocol", "Montreal Protocol", "Basel Convention"],
        "answer": 0,
        "subtopic": "Biology • Environmental Issues",
        "explanation": "The Montreux Record is a register of wetland sites on the Ramsar List where ecological character changes have occurred, are occurring, or are likely to occur as a result of technological developments, pollution, or human interference.",
        "citation": "NCERT Class 12 Biology Chapter 16 (Environmental Issues)"
    },
    {
        "id": 25,
        "question": "Which atmospheric layer contains the beneficial 'good' ozone layer that absorbs harmful solar ultraviolet-B (UV-B) radiation?",
        "options": ["Stratosphere", "Troposphere", "Mesosphere", "Thermosphere"],
        "answer": 0,
        "subtopic": "Biology • Environmental Issues",
        "explanation": "The 'good' ozone layer is located in the stratosphere (between 15 and 30 km above Earth's surface) and shields biological organisms from harmful ultraviolet (UV-B) radiation. Tropospheric ozone is a harmful pollutant.",
        "citation": "NCERT Class 12 Biology Chapter 16 (Environmental Issues)"
    },

    # Chemistry (Q26-Q35)
    {
        "id": 27,
        "question": "What is the molarity of a solution prepared by dissolving 4.0 g of NaOH (molar mass = 40 g/mol) in sufficient distilled water to make 250 mL of solution?",
        "options": ["0.40 M", "0.10 M", "1.00 M", "0.25 M"],
        "answer": 0,
        "subtopic": "Chemistry • Solutions",
        "explanation": "Moles of NaOH = 4.0 g / 40 g/mol = 0.10 mol. Volume of solution = 250 mL = 0.250 L. Molarity M = moles / volume (L) = 0.10 mol / 0.250 L = 0.40 M.",
        "citation": "NCERT Class 12 Chemistry Chapter 2 (Solutions)"
    },
    {
        "id": 28,
        "question": "According to the Arrhenius equation k = A e^(-Ea / RT), the slope of a plot of ln k versus 1/T is equal to:",
        "options": ["-Ea / R", "Ea / R", "-Ea / (2.303 R)", "ln A"],
        "answer": 0,
        "subtopic": "Chemistry • Chemical Kinetics",
        "explanation": "Taking natural logarithm: ln k = ln A - (Ea / R)(1/T). Comparing with the linear equation y = c + mx, the independent variable is x = 1/T, giving a slope m = -Ea / R.",
        "citation": "NCERT Class 12 Chemistry Chapter 4 (Chemical Kinetics)"
    },
    {
        "id": 29,
        "question": "Which of the following noble gas compounds is isostructural with the interhalogen anion ICl₄⁻?",
        "options": ["XeF₄", "XeF₂", "XeO₃", "XeOF₄"],
        "answer": 0,
        "subtopic": "Chemistry • p-Block Elements",
        "explanation": "ICl₄⁻ has 7 + 4(7) + 1 = 36 valence electrons: 4 bond pairs and 2 lone pairs on iodine → sp³d² hybridization, square planar geometry. XeF₄ also has 8 + 4(7) = 36 valence electrons: 4 bond pairs and 2 lone pairs on xenon → square planar geometry. Thus, both are isostructural.",
        "citation": "NCERT Class 12 Chemistry Chapter 7 (p-Block Elements)"
    },
    {
        "id": 30,
        "question": "The oxidation states of Cr in K₂Cr₂O₇ and Mn in KMnO₄ are respectively:",
        "options": ["+6 and +7", "+6 and +6", "+3 and +7", "+7 and +6"],
        "answer": 0,
        "subtopic": "Chemistry • Redox Reactions",
        "explanation": "In K₂Cr₂O₇: 2(+1) + 2(Cr) + 7(-2) = 0 ⇒ 2Cr - 12 = 0 ⇒ Cr = +6. In KMnO₄: (+1) + Mn + 4(-2) = 0 ⇒ Mn - 7 = 0 ⇒ Mn = +7.",
        "citation": "NCERT Class 11 Chemistry Chapter 8 (Redox Reactions)"
    },
    {
        "id": 31,
        "question": "Which of the following organic reagents distinguishes a primary aliphatic amine from secondary and tertiary amines via the Hinsberg test?",
        "options": ["Benzenesulfonyl chloride (Hinsberg's reagent)", "Bromine water", "Neutral FeCl₃ solution", "Lucas reagent"],
        "answer": 0,
        "subtopic": "Chemistry • Amines",
        "explanation": "Benzenesulfonyl chloride (C₆H₅SO₂Cl) reacts with primary amines to form N-alkylbenzenesulfonamides having an acidic hydrogen on nitrogen, which dissolves in aqueous KOH. Secondary amines yield an insoluble precipitate, while tertiary amines do not react.",
        "citation": "NCERT Class 12 Chemistry Chapter 13 (Amines)"
    },
    {
        "id": 32,
        "question": "Lucas test is used to differentiate primary, secondary, and tertiary alcohols. The reagent consists of:",
        "options": ["Concentrated HCl and anhydrous ZnCl₂", "Dilute H₂SO₄ and KMnO₄", "PCl₅ and pyridine", "CrO₃ and pyridine"],
        "answer": 0,
        "subtopic": "Chemistry • Alcohols, Phenols and Ethers",
        "explanation": "Lucas reagent is an equimolar mixture of concentrated HCl and anhydrous ZnCl₂. Tertiary alcohols form alkyl chloride turbidity immediately; secondary alcohols take 5 minutes; primary alcohols remain clear at room temperature.",
        "citation": "NCERT Class 12 Chemistry Chapter 11 (Alcohols, Phenols and Ethers)"
    },
    {
        "id": 33,
        "question": "Which of the following compounds exhibits optical isomerism (enantiomerism) due to the presence of a chiral stereocenter?",
        "options": ["Butan-2-ol", "Butan-1-ol", "Propan-2-ol", "2-Methylpropan-2-ol"],
        "answer": 0,
        "subtopic": "Chemistry • Stereochemistry",
        "explanation": "In butan-2-ol (CH₃-CH(OH)-CH₂-CH₃), carbon-2 is bonded to four distinct substituents: -H, -OH, -CH₃, and -CH₂CH₃. Because it contains an asymmetric carbon atom, it is chiral and exhibits optical activity.",
        "citation": "NCERT Class 12 Chemistry Chapter 10 (Haloalkanes and Haloarenes)"
    },
    {
        "id": 34,
        "question": "The pH of a 1.0 × 10⁻³ M aqueous solution of strong monoprotic hydrochloric acid (HCl) at 25 °C is:",
        "options": ["3.0", "11.0", "7.0", "1.0"],
        "answer": 0,
        "subtopic": "Chemistry • Ionic Equilibrium",
        "explanation": "HCl completely ionizes: [H₃O⁺] = 1.0 × 10⁻³ M. pH = -log₁₀[H⁺] = -log₁₀(1.0 × 10⁻³) = 3.0.",
        "citation": "NCERT Class 11 Chemistry Chapter 7 (Equilibrium)"
    },
    {
        "id": 35,
        "question": "The peptide linkage formed during condensation of two amino acids is chemically an:",
        "options": ["Amide bond (-CO-NH-)", "Ester bond (-COO-)", "Glycosidic bond (-O-)", "Ether bond (-C-O-C-)"],
        "answer": 0,
        "subtopic": "Chemistry • Biomolecules",
        "explanation": "A peptide bond is an amide linkage formed between the α-carboxyl group of one amino acid and the α-amino group of an adjacent amino acid with the loss of a water molecule: -COOH + H₂N- → -CO-NH- + H₂O.",
        "citation": "NCERT Class 12 Chemistry Chapter 14 (Biomolecules)"
    },

    # Physics (Q36-Q45)
    {
        "id": 36,
        "question": "A body of mass 2 kg executes simple harmonic motion (SHM) with amplitude A = 0.1 m and angular frequency ω = 10 rad/s. The maximum kinetic energy of the oscillator is:",
        "options": ["1.0 J", "0.5 J", "2.0 J", "0.1 J"],
        "answer": 0,
        "subtopic": "Physics • Oscillations",
        "explanation": "The maximum kinetic energy in SHM occurs at the mean position: K_max = (1/2) m v_max² = (1/2) m (ω A)² = (1/2) × 2 × (10 × 0.1)² = 1 × (1.0)² = 1.0 J.",
        "citation": "NCERT Class 11 Physics Chapter 14 (Oscillations)"
    },
    {
        "id": 37,
        "question": "A transverse wave traveling along a stretched string is described by y(x,t) = 0.05 sin(20x - 400t), where x, y are in meters and t in seconds. The wave speed is:",
        "options": ["20 m/s", "400 m/s", "8000 m/s", "0.05 m/s"],
        "answer": 0,
        "subtopic": "Physics • Waves",
        "explanation": "In standard form y = A sin(kx - ωt): wave number k = 20 rad/m and angular frequency ω = 400 rad/s. Wave velocity is v = ω / k = 400 / 20 = 20 m/s.",
        "citation": "NCERT Class 11 Physics Chapter 15 (Waves)"
    },
    {
        "id": 38,
        "question": "An ideal monoatomic gas (γ = 5/3) is heated at constant pressure. What fraction of the heat supplied is converted into external work done?",
        "options": ["2 / 5 (40%)", "3 / 5 (60%)", "1 / 3 (33%)", "2 / 3 (67%)"],
        "answer": 0,
        "subtopic": "Physics • Thermodynamics",
        "explanation": "At constant pressure: Q = n C_p ΔT and W = n R ΔT. Fraction of heat converted to work is W / Q = R / C_p. For a monoatomic gas, C_p = (5/2) R. Therefore, W / Q = R / ((5/2) R) = 2 / 5 = 0.40 (40%).",
        "citation": "NCERT Class 11 Physics Chapter 12 (Thermodynamics)"
    },
    {
        "id": 39,
        "question": "A point object is placed 30 cm in front of a concave mirror of focal length 20 cm. The distance of the image formed from the mirror is:",
        "options": ["60 cm in front of mirror (real)", "12 cm behind mirror", "30 cm in front of mirror", "60 cm behind mirror"],
        "answer": 0,
        "subtopic": "Physics • Ray Optics",
        "explanation": "By Cartesian sign convention: u = -30 cm and f = -20 cm. Mirror formula: 1/f = 1/v + 1/u ⇒ 1/v = 1/f - 1/u = 1/(-20) - 1/(-30) = -1/20 + 1/30 = (-3 + 2) / 60 = -1/60 ⇒ v = -60 cm. The image is real, inverted, and located 60 cm in front of the mirror.",
        "citation": "NCERT Class 12 Physics Chapter 9 (Ray Optics and Optical Instruments)"
    },
    {
        "id": 40,
        "question": "A long straight solenoid of length 1.0 m has 1000 turns of wire. When a current of 2.0 A flows through it, the magnetic field inside near the center is (μ₀ = 4π × 10⁻⁷ T·m/A):",
        "options": ["8π × 10⁻⁴ T (2.51 mT)", "4π × 10⁻⁴ T", "2π × 10⁻⁴ T", "16π × 10⁻⁴ T"],
        "answer": 0,
        "subtopic": "Physics • Magnetism",
        "explanation": "Magnetic field inside an ideal solenoid is B = μ₀ n I, where n = N / L = 1000 / 1.0 = 1000 turns/m. B = (4π × 10⁻⁷) × 1000 × 2.0 = 8π × 10⁻⁴ T ≈ 2.51 × 10⁻³ T = 2.51 mT.",
        "citation": "NCERT Class 12 Physics Chapter 4 (Moving Charges and Magnetism)"
    },
    {
        "id": 41,
        "question": "In a series AC circuit containing pure resistance R and pure inductance L connected to an AC source of voltage V and frequency ω, the impedance Z is:",
        "options": ["√(R² + ω² L²)", "R + ω L", "√(R² - ω² L²)", "R / (ω L)"],
        "answer": 0,
        "subtopic": "Physics • Alternating Current",
        "explanation": "In an RL series circuit, resistive voltage and inductive voltage are 90° out of phase: V = √(V_R² + V_L²). Dividing by current I yields total impedance Z = √(R² + X_L²) = √(R² + (ω L)²).",
        "citation": "NCERT Class 12 Physics Chapter 7 (Alternating Current)"
    },
    {
        "id": 42,
        "question": "Electromagnetic waves with frequencies just below visible red light that produce heating effects and are detected by thermopiles or bolometers are:",
        "options": ["Infrared waves", "Ultraviolet rays", "X-rays", "Microwaves"],
        "answer": 0,
        "subtopic": "Physics • Electromagnetic Waves",
        "explanation": "Infrared radiation (wavelengths ~700 nm to 1 mm) lies adjacent to red in the visible spectrum. Often termed 'heat waves', they are produced by hot bodies and molecular vibrations and are widely used in physical therapy and night vision.",
        "citation": "NCERT Class 12 Physics Chapter 8 (Electromagnetic Waves)"
    },
    {
        "id": 43,
        "question": "When a monochromatic light beam travels from air into a glass slab of refractive index 1.5, which property of the light wave remains unchanged?",
        "options": ["Frequency", "Wavelength", "Speed", "Amplitude"],
        "answer": 0,
        "subtopic": "Physics • Wave Optics",
        "explanation": "The frequency of a light wave is determined solely by the source oscillation that emitted it. Upon entering an optically denser medium, speed decreases (v = c / μ) and wavelength shortens (λ' = λ / μ), but frequency remains strictly constant.",
        "citation": "NCERT Class 12 Physics Chapter 10 (Wave Optics)"
    },
    {
        "id": 44,
        "question": "The de Broglie wavelength of a thermal neutron of mass m at absolute temperature T is proportional to:",
        "options": ["1 / √T", "√T", "1 / T", "T"],
        "answer": 0,
        "subtopic": "Physics • Dual Nature of Matter",
        "explanation": "Average kinetic energy of a thermal neutron in equilibrium at temperature T is K = (3/2) k_B T. Momentum p = √(2m K) = √(3 m k_B T). By de Broglie relation: λ = h / p = h / √(3 m k_B T) ∝ 1 / √T.",
        "citation": "NCERT Class 12 Physics Chapter 11 (Dual Nature of Radiation and Matter)"
    },
    {
        "id": 45,
        "question": "In a nuclear reaction, 1 atomic mass unit (1 u) of mass defect is converted entirely into energy. The equivalent energy released is approximately:",
        "options": ["931.5 MeV", "93.15 MeV", "1.6 × 10⁻¹⁹ J", "3.0 × 10⁸ J"],
        "answer": 0,
        "subtopic": "Physics • Nuclei",
        "explanation": "Using Einstein's mass-energy equivalence E = Δm c²: 1 u = 1.6605 × 10⁻²⁷ kg. E = (1.6605 × 10⁻²⁷ kg) × (2.9979 × 10⁸ m/s)² ≈ 1.4924 × 10⁻¹⁰ J. Converting to electron-volts: (1.4924 × 10⁻¹⁰ J) / (1.6022 × 10⁻¹³ J/MeV) ≈ 931.5 MeV.",
        "citation": "NCERT Class 12 Physics Chapter 13 (Nuclei)"
    }
]

# Write out the files
with open('/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com/data/in/nta/neet_ug_drill1.json', 'w', encoding='utf-8') as f:
    json.dump(neet_ug_drill1, f, indent=2, ensure_ascii=False)

with open('/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com/data/in/nta/neet_ug_drill2.json', 'w', encoding='utf-8') as f:
    json.dump(neet_ug_drill2, f, indent=2, ensure_ascii=False)

print(f"Generated NEET UG Drill 1: {len(neet_ug_drill1)} Qs")
print(f"Generated NEET UG Drill 2: {len(neet_ug_drill2)} Qs")
