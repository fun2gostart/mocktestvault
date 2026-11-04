#!/usr/bin/env python3
"""
generate_ib_dp.py
Generates 140 high-yield, authentic examination practice questions for:
1. IB DP Biology (HL/SL) Paper 1 (Set 1: 40 Qs, Set 2: 40 Qs)
2. IB DP Mathematics: Analysis and Approaches (AA HL/SL) (Set 1: 30 Qs, Set 2: 30 Qs)
Adheres strictly to the International Baccalaureate Organization (IBO) curriculum guidelines,
Paper 1 non-calculator multiple-choice standards, and official markschemes.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "global", "ib")
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. IB DP BIOLOGY (HL / SL) PAPER 1 — SET 1 (40 Questions)
# -------------------------------------------------------------
bio_set1_questions = [
    # Topic 1: Cell Biology (1-5)
    {
        "id": "ib-bio-s1-001",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Cell Theory & Magnification)",
        "difficulty": "Medium",
        "question": "A micrograph shows an erythrocyte with an actual diameter of 7.0 µm. If the measured diameter of the erythrocyte on the printout is 21 mm, what is the magnification of the image?",
        "options": [
            "×3,000",
            "×300",
            "×30,000",
            "×300,000"
        ],
        "answer": 0,
        "explanation": "Magnification = Image size / Actual size. Convert 21 mm to micrometres: 21 mm = 21,000 µm. Magnification = 21,000 µm / 7.0 µm = ×3,000.",
        "citation": "IB Biology Subject Guide — Topic 1.1: Introduction to Cells"
    },
    {
        "id": "ib-bio-s1-002",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Membrane Structure)",
        "difficulty": "Hard",
        "question": "Which experimental evidence directly refuted the Davson-Danielli 'protein sandwich' model and supported the Singer-Nicolson fluid mosaic model?",
        "options": [
            "Freeze-etched electron micrographs showing globular proteins embedded across the hydrophobic core of the bilayer",
            "Biochemical analysis demonstrating that cell membranes contain equal masses of lipids and carbohydrates",
            "X-ray crystallography showing uniform continuous monolayer coatings of peripheral fibrous proteins",
            "Observation that hydrophobic fatty acid tails face outward towards the polar extracellular aqueous medium"
        ],
        "answer": 0,
        "explanation": "Freeze-fracture electron microscopy cleaved membranes along the central hydrophobic plane of the lipid bilayer, revealing transmembrane globular proteins projecting into the interior. Additionally, antibody fluorescent tagging proved membrane protein lateral fluidity.",
        "citation": "IB Biology Subject Guide — Topic 1.3: Membrane Structure"
    },
    {
        "id": "ib-bio-s1-003",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Membrane Transport)",
        "difficulty": "Medium",
        "question": "What is the primary mechanism of the sodium-potassium pump (Na+/K+-ATPase) across an axon membrane during one complete cycle?",
        "options": [
            "Pumps 3 Na+ ions out of the cell and 2 K+ ions into the cell using hydrolysis of 1 ATP molecule",
            "Pumps 2 Na+ ions out of the cell and 3 K+ ions into the cell using hydrolysis of 1 ATP molecule",
            "Facilitates passive influx of 3 Na+ ions and passive efflux of 2 K+ ions down concentration gradients",
            "Translocates 3 Na+ ions and 3 K+ ions simultaneously into the cytoplasm via secondary symport"
        ],
        "answer": 0,
        "explanation": "The electrogenic sodium-potassium pump actively expels 3 Na+ ions into the extracellular matrix while importing 2 K+ ions into the cytoplasm against their respective electrochemical gradients per molecule of ATP hydrolyzed.",
        "citation": "IB Biology Subject Guide — Topic 1.4: Membrane Transport"
    },
    {
        "id": "ib-bio-s1-004",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Origin of Cells)",
        "difficulty": "Medium",
        "question": "Which characteristic of chloroplasts and mitochondria provides conclusive evidence for endosymbiotic theory?",
        "options": [
            "They possess their own circular naked DNA and 70S ribosomes, similar to prokaryotes",
            "They possess linear chromosomes bounded by a true nuclear membrane",
            "They transcribe eukaryotic 80S ribosomes and contain peptidoglycan outer capsules",
            "They divide synchronously only when the host cell completes cytokinesis"
        ],
        "answer": 0,
        "explanation": "Mitochondria and chloroplasts replicate independently by binary fission, contain circular double-stranded DNA unassociated with histones, possess 70S ribosomes, and have a double membrane—traits shared with prokaryotic organisms.",
        "citation": "IB Biology Subject Guide — Topic 1.5: The Origin of Cells"
    },
    {
        "id": "ib-bio-s1-005",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Cell Division & Mitosis)",
        "difficulty": "Easy",
        "question": "Which group of regulatory proteins binds to cyclin-dependent kinases (CDKs) to orchestrate progression through cell cycle checkpoints?",
        "options": [
            "Cyclins",
            "Histones",
            "Integrins",
            "Immunoglobulins"
        ],
        "answer": 0,
        "explanation": "Cyclins are regulatory proteins whose concentrations oscillate throughout the cell cycle. When cyclins bind to CDKs, the resulting kinase complexes phosphorylate target proteins to drive transitions between G1, S, G2, and M phases.",
        "citation": "IB Biology Subject Guide — Topic 1.6: Cell Division"
    },

    # Topic 2: Molecular Biology (6-12)
    {
        "id": "ib-bio-s1-006",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Properties of Water)",
        "difficulty": "Medium",
        "question": "Sweat cools the human body during vigorous exercise. Which property of water explains this thermoregulatory cooling effect?",
        "options": [
            "High latent heat of vaporization requiring substantial thermal energy to break intermolecular hydrogen bonds",
            "High specific heat capacity preventing rapid changes in internal body temperature",
            "Strong cohesive forces enabling uninterrupted water column transpiration in capillary beds",
            "Maximum density at 4 °C preventing thermal stratification in subcutaneous capillaries"
        ],
        "answer": 0,
        "explanation": "Water has a high latent heat of vaporization (approx. 2.26 × 10^6 J/kg). Evaporation of water molecules from epidermal sweat glands absorbs significant heat energy from skin tissues, cooling the body.",
        "citation": "IB Biology Subject Guide — Topic 2.2: Water"
    },
    {
        "id": "ib-bio-s1-007",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Carbohydrates & Lipids)",
        "difficulty": "Hard",
        "question": "Which statement accurately contrasts cellulose and amylose in terms of monomer conformation and glycosidic linkages?",
        "options": [
            "Cellulose consists of β-D-glucose with β-1,4-glycosidic bonds forming straight unbranched chains, whereas amylose consists of α-D-glucose with α-1,4-glycosidic bonds forming helical polymers",
            "Cellulose consists of α-D-glucose with α-1,6-glycosidic branch points, whereas amylose is composed entirely of β-D-fructose monomers",
            "Cellulose forms globular energy storage granules in animal hepatocytes, whereas amylose forms structural fibers in fungal cell walls",
            "Cellulose is easily hydrolyzed by mammalian salivary amylase, whereas amylose is completely indigestible by animals"
        ],
        "answer": 0,
        "explanation": "Cellulose is an unbranched polymer of β-D-glucose linked by β-1,4-glycosidic bonds; alternating glucose monomers are rotated 180°, producing linear ribbons that bundle into microfibrils via hydrogen bonds. Amylose has α-1,4-linkages coiling into a helix.",
        "citation": "IB Biology Subject Guide — Topic 2.3: Carbohydrates and Lipids"
    },
    {
        "id": "ib-bio-s1-008",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Enzymes & Inhibition)",
        "difficulty": "Medium",
        "question": "How does an uncompetitive or non-competitive allosteric inhibitor alter the maximum reaction rate (Vmax) and the Michaelis constant (Km) of an enzyme-catalyzed reaction?",
        "options": [
            "Decreases Vmax while leaving Km unchanged",
            "Maintains Vmax constant while significantly increasing Km",
            "Increases both Vmax and Km simultaneously",
            "Decreases Km while doubling Vmax at saturating substrate concentrations"
        ],
        "answer": 0,
        "explanation": "Non-competitive inhibitors bind to an allosteric site rather than the active site, altering enzyme conformation. This reduces the catalytic efficiency, lowering Vmax. Because substrate binding affinity at the active site is unaffected, Km remains constant.",
        "citation": "IB Biology Subject Guide — Topic 8.1: Enzymes (HL)"
    },
    {
        "id": "ib-bio-s1-009",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (DNA Structure & Meselson-Stahl)",
        "difficulty": "Medium",
        "question": "In the Meselson and Stahl experiment, E. coli grown in 15N media were transferred to 14N media and allowed to replicate for two generations. What was the observed composition of the DNA bands after equilibrium density gradient centrifugation?",
        "options": [
            "50% intermediate hybrid density (15N/14N) DNA and 50% light density (14N/14N) DNA",
            "100% intermediate hybrid density (15N/14N) DNA",
            "75% heavy density (15N/15N) DNA and 25% light density (14N/14N) DNA",
            "25% intermediate hybrid density (15N/14N) DNA and 75% heavy density (15N/15N) DNA"
        ],
        "answer": 0,
        "explanation": "After generation 1, 100% of the DNA was hybrid (15N/14N). After generation 2 in 14N, each hybrid duplex replicated semi-conservatively to yield one hybrid duplex and one fully light duplex, resulting in exactly 50% hybrid and 50% light DNA.",
        "citation": "IB Biology Subject Guide — Topic 2.7: DNA Replication, Transcription and Translation"
    },
    {
        "id": "ib-bio-s1-010",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Transcription & Translation)",
        "difficulty": "Medium",
        "question": "If an mRNA coding sequence contains the codon 5'-AUG-3', what is the complementary anticodon on the initiator tRNA and the amino acid it carries?",
        "options": [
            "3'-UAC-5' carrying Methionine",
            "5'-UAC-3' carrying Formylmethionine",
            "3'-AUG-5' carrying Valine",
            "5'-CAU-3' carrying Tryptophan"
        ],
        "answer": 0,
        "explanation": "Antiparallel base-pairing requires the codon 5'-AUG-3' to pair with the tRNA anticodon 3'-UAC-5' (or 5'-CAU-3' read 5' to 3'). AUG universally codes for methionine.",
        "citation": "IB Biology Subject Guide — Topic 2.7: Transcription and Translation"
    },
    {
        "id": "ib-bio-s1-011",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Cell Respiration)",
        "difficulty": "Hard",
        "question": "During oxidative phosphorylation in aerobic cell respiration, what directly drives the synthesis of ATP by ATP synthase?",
        "options": [
            "The chemiosmotic flow of protons (H+) from the intermembrane space into the mitochondrial matrix down their electrochemical gradient",
            "Direct substrate-level phosphorylation driven by acetyl-CoA condensation with oxaloacetate",
            "The active transport of electrons through ATP synthase rotor sub-units into the inner cristae membrane",
            "The oxidative decarboxylation of pyruvate into lactate in the outer membrane space"
        ],
        "answer": 0,
        "explanation": "The electron transport chain pumps protons from the matrix into the intermembrane space, establishing an electrochemical proton gradient. Protons diffuse back through ATP synthase via chemiosmosis, inducing rotational catalysis to form ATP from ADP and Pi.",
        "citation": "IB Biology Subject Guide — Topic 8.2: Cell Respiration (HL)"
    },
    {
        "id": "ib-bio-s1-012",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Photosynthesis)",
        "difficulty": "Medium",
        "question": "What is the primary role of the light-dependent reactions of photosynthesis in supporting the light-independent reactions (Calvin cycle)?",
        "options": [
            "To generate ATP and reduced NADP (NADPH) required to convert glycerate-3-phosphate (GP) into triose phosphate (TP)",
            "To fix atmospheric carbon dioxide directly onto ribulose bisphosphate (RuBP) using Rubisco",
            "To hydrolyze sucrose into glucose and fructose inside the thylakoid lumen",
            "To pump molecular oxygen directly into the stomatal guard cells"
        ],
        "answer": 0,
        "explanation": "The light-dependent reactions capture solar energy to produce ATP and NADPH via photophosphorylation and photolysis of water. These energy carriers enter the stroma to power the reduction of GP to TP in the Calvin cycle.",
        "citation": "IB Biology Subject Guide — Topic 8.3: Photosynthesis (HL)"
    },

    # Topic 3: Genetics (13-17)
    {
        "id": "ib-bio-s1-013",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Meiosis & Crossing Over)",
        "difficulty": "Medium",
        "question": "At which stage of meiosis does crossing over occur between non-sister chromatids of homologous chromosomes, resulting in chiasmata formation?",
        "options": [
            "Prophase I",
            "Metaphase II",
            "Anaphase I",
            "Telophase II"
        ],
        "answer": 0,
        "explanation": "Synapsis and crossing over occur during Prophase I of meiosis. Homologous chromosomes pair to form bivalents/tetrads, and non-sister chromatids exchange reciprocal genetic segments at chiasmata.",
        "citation": "IB Biology Subject Guide — Topic 3.3: Meiosis"
    },
    {
        "id": "ib-bio-s1-014",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Inheritance & Blood Groups)",
        "difficulty": "Medium",
        "question": "A woman with blood group A (whose father had blood group O) has a child with a man who has blood group B (whose mother had blood group O). What is the probability that their child will have blood group O?",
        "options": [
            "0.25 (25%)",
            "0.50 (50%)",
            "0.125 (12.5%)",
            "0.75 (75%)"
        ],
        "answer": 0,
        "explanation": "The woman is heterozygous (IAi) because her father had type O (ii). The man is heterozygous (IBi) because his mother was type O. Cross: IAi × IBi produces IAIB (25%), IAi (25%), IBi (25%), and ii (25%). Blood group O corresponds to genotype ii = 25% (0.25).",
        "citation": "IB Biology Subject Guide — Topic 3.4: Inheritance"
    },
    {
        "id": "ib-bio-s1-015",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Sex Linkage)",
        "difficulty": "Medium",
        "question": "Red-green colorblindness is an X-linked recessive condition. If a carrier female (X^B X^b) and a normal vision male (X^B Y) have children, what proportion of their sons are expected to be colorblind?",
        "options": [
            "50%",
            "100%",
            "25%",
            "0%"
        ],
        "answer": 0,
        "explanation": "The sons receive their Y chromosome from the father and either X^B or X^b from the mother with equal 50% probability. Therefore, 50% of the sons (X^b Y) will exhibit red-green colorblindness.",
        "citation": "IB Biology Subject Guide — Topic 3.4: Inheritance"
    },
    {
        "id": "ib-bio-s1-016",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Genetic Modification & PCR)",
        "difficulty": "Easy",
        "question": "Which heat-stable enzyme is utilized in the polymerase chain reaction (PCR) to synthesize complementary DNA strands across repeated thermal cycles?",
        "options": [
            "Taq DNA polymerase",
            "RNA polymerase II",
            "DNA ligase",
            "Topoisomerase"
        ],
        "answer": 0,
        "explanation": "Taq polymerase, isolated from the thermophilic bacterium Thermus aquaticus, retains stability and catalytic activity through repetitive high-temperature denaturation steps (95 °C) in PCR thermocyclers.",
        "citation": "IB Biology Subject Guide — Topic 3.5: Genetic Modification and Biotechnology"
    },
    {
        "id": "ib-bio-s1-017",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Gene Linkage & Dihybrid Crosses)",
        "difficulty": "Hard",
        "question": "In a dihybrid test cross between a heterozygous individual (AaBb) and a homozygous recessive tester (aabb), the observed offspring phenotypic ratio is 45:5:5:45 instead of the expected 1:1:1:1. What does this indicate?",
        "options": [
            "The genes A and B are linked on the same autosome, with recombinant frequency of 10%",
            "The alleles undergo independent assortment with incomplete dominance",
            "Gene A is epistatic to gene B, suppressing recombinant phenotypes",
            "Non-disjunction occurred during Metaphase II in the homozygous parent"
        ],
        "answer": 0,
        "explanation": "A high proportion of parental phenotypes (45 + 45 = 90%) and low proportion of recombinants (5 + 5 = 10%) signifies autosomal linkage. The recombinant frequency is (10 / 100) × 100 = 10%, which equals 10 map units (centimorgans).",
        "citation": "IB Biology Subject Guide — Topic 10.2: Inheritance (HL)"
    },

    # Topic 4: Ecology (18-22)
    {
        "id": "ib-bio-s1-018",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Energy Flow & Pyramids)",
        "difficulty": "Easy",
        "question": "Why is the transfer of energy between successive trophic levels in a terrestrial ecosystem typically limited to approximately 10%?",
        "options": [
            "Much energy is lost as metabolic heat during cellular respiration, unconsumed biomass, and undigested waste",
            "Primary producers consume 90% of incident solar radiant energy through stomatal photorespiration",
            "Decomposers assimilate all chemical bond energy before apex carnivores feed",
            "Carnivores possess metabolic enzymes incapable of catabolizing secondary trophic lipids"
        ],
        "answer": 0,
        "explanation": "Energy is dissipated between trophic levels due to cellular respiration (released as thermal energy/heat, which cannot be converted into organic forms), material unconsumed by predators, and unassimilated waste (feces/urine).",
        "citation": "IB Biology Subject Guide — Topic 4.2: Energy Flow"
    },
    {
        "id": "ib-bio-s1-019",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Carbon Cycle)",
        "difficulty": "Medium",
        "question": "Under anaerobic and acidic conditions in waterlogged soils, incomplete decomposition of dead organic matter by methanogens and saprotrophs leads to the formation of which geological carbon sink?",
        "options": [
            "Peat",
            "Limestone",
            "Basalt",
            "Silica chert"
        ],
        "answer": 0,
        "explanation": "In waterlogged bogs, lack of oxygen creates anoxic conditions. Saprotrophs cannot break down organic material completely, causing acidic, partially decomposed plant matter to accumulate over millennia as peat, which can fossilize into coal.",
        "citation": "IB Biology Subject Guide — Topic 4.3: Carbon Cycling"
    },
    {
        "id": "ib-bio-s1-020",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Greenhouse Gases)",
        "difficulty": "Medium",
        "question": "Which two gases exert the greatest natural greenhouse effect on Earth based on their atmospheric concentration and ability to absorb longwave infrared radiation?",
        "options": [
            "Water vapour and carbon dioxide",
            "Methane and ozone",
            "Nitrogen and oxygen",
            "Chlorofluorocarbons and sulfur dioxide"
        ],
        "answer": 0,
        "explanation": "Water vapour and carbon dioxide (CO2) have the highest overall warming impact due to their high atmospheric concentrations and broad absorption bands in the infrared spectrum. Methane is more potent per molecule, but exists in much lower concentrations.",
        "citation": "IB Biology Subject Guide — Topic 4.4: Climate Change"
    },
    {
        "id": "ib-bio-s1-021",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Mesocosms & Chi-squared)",
        "difficulty": "Medium",
        "question": "In an ecological survey assessing whether two sessile intertidal species are associated, a chi-squared test yielded a calculated value of χ² = 7.84 with 1 degree of freedom (critical value at p = 0.05 is 3.841). What conclusion must be drawn?",
        "options": [
            "Reject the null hypothesis; there is a statistically significant association between the two species",
            "Accept the null hypothesis; the two species are distributed independently across quadrants",
            "The data are invalid because the calculated chi-square value cannot exceed degrees of freedom",
            "Both species exhibit competitive exclusion and mutual extinction in high-tide zones"
        ],
        "answer": 0,
        "explanation": "Since the calculated χ² (7.84) is greater than the critical value (3.841) at the 5% significance level (p < 0.05), we reject the null hypothesis of independence and conclude there is a statistically significant association.",
        "citation": "IB Biology Subject Guide — Topic 4.1: Species, Communities and Ecosystems"
    },
    {
        "id": "ib-bio-s1-022",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Ocean Acidification)",
        "difficulty": "Hard",
        "question": "How does increased dissolution of anthropogenic atmospheric CO2 in seawater affect marine calcifying organisms such as reef-building corals?",
        "options": [
            "CO2 reacts with water to produce carbonic acid, which dissociates into H+ ions that bind free carbonate ions (CO3^2-), depleting the carbonate pool needed to precipitate CaCO3 skeletons",
            "Dissolved CO2 directly binds magnesium ions, precipitating aragonite crusts over polyp mouths",
            "High CO2 raises oceanic pH to alkaline levels above 9.0, dissolving calcium phosphate deposits",
            "Carbonic acid inhibits zooxanthellae nitrogenase, stopping calcification outright"
        ],
        "answer": 0,
        "explanation": "CO2 + H2O → H2CO3 → H+ + HCO3-. The excess H+ ions react with existing carbonate ions (H+ + CO3^2- → HCO3-), reducing the saturation state of carbonate (CO3^2-) needed by corals and molluscs to synthesize calcium carbonate (CaCO3).",
        "citation": "IB Biology Subject Guide — Topic 4.4: Climate Change"
    },

    # Topic 5: Evolution & Biodiversity (23-27)
    {
        "id": "ib-bio-s1-023",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution & Biodiversity (Homologous Structures)",
        "difficulty": "Medium",
        "question": "The pentadactyl limb found in humans, whales, bats, and lizards represents which evolutionary phenomenon?",
        "options": [
            "Adaptive radiation from a common ancestor resulting in homologous anatomical structures",
            "Convergent evolution among unrelated taxa resulting in analogous functional adaptations",
            "Genetic drift in isolated populations causing disruptive anatomical convergence",
            "Polyploid hybrid speciation within terrestrial tetrapod clades"
        ],
        "answer": 0,
        "explanation": "Pentadactyl limbs share a fundamental bone architecture (humerus/femur, radius/tibia, ulna/fibula, carpals/tarsals, metacarpals/metatarsals, phalanges) inherited from a common tetrapod ancestor, diversified by adaptive radiation for locomotion.",
        "citation": "IB Biology Subject Guide — Topic 5.1: Evidence for Evolution"
    },
    {
        "id": "ib-bio-s1-024",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution & Biodiversity (Natural Selection)",
        "difficulty": "Easy",
        "question": "Which condition is an absolute prerequisite for natural selection to act upon a population?",
        "options": [
            "Genetically determined phenotypic variation among individuals within the population",
            "An infinitely large population with zero intraspecific reproductive competition",
            "Total absence of environmental selective pressures and predation mortality",
            "Continuous asexual cloning without meiotic recombination or mutation"
        ],
        "answer": 0,
        "explanation": "Natural selection requires heritable genetic variation. Individuals possessing advantageous traits suited to their environment enjoy differential survival and reproductive success, passing favorable alleles to progeny.",
        "citation": "IB Biology Subject Guide — Topic 5.2: Natural Selection"
    },
    {
        "id": "ib-bio-s1-025",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution & Biodiversity (Cladistics)",
        "difficulty": "Hard",
        "question": "Why did molecular cladistics using mitochondrial DNA and base sequence alignment reclassify the figwort family (Scrophulariaceae)?",
        "options": [
            "DNA sequence comparisons revealed that the traditional morphology-based family was polyphyletic, containing species from five separate clades",
            "Figworts were proved to lack chloroplast genomes and thus reclassified as parasitic fungi",
            "Mitochondrial sequencing proved that all dicotyledonous angiosperms arose from a single gymnosperm lineage",
            "All species within the family were found to possess identical 18S ribosomal RNA sequences"
        ],
        "answer": 0,
        "explanation": "Species originally grouped into Scrophulariaceae based on superficial floral morphological similarities were revealed by DNA and amino acid sequence analysis to originate from distinct ancestral lineages (polyphyly/paraphyly), prompting reclassification into 5 clades.",
        "citation": "IB Biology Subject Guide — Topic 5.4: Cladistics"
    },
    {
        "id": "ib-bio-s1-026",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution & Biodiversity (Classification)",
        "difficulty": "Easy",
        "question": "What is the correct taxonomic hierarchy from broadest domain to most specific species according to universal binomial classification?",
        "options": [
            "Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species",
            "Domain, Phylum, Kingdom, Family, Order, Class, Genus, Species",
            "Kingdom, Domain, Class, Phylum, Family, Order, Species, Genus",
            "Domain, Kingdom, Class, Order, Phylum, Genus, Family, Species"
        ],
        "answer": 0,
        "explanation": "The standard Linnaean taxonomic hierarchy is: Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species.",
        "citation": "IB Biology Subject Guide — Topic 5.3: Classification of Biodiversity"
    },
    {
        "id": "ib-bio-s1-027",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution & Biodiversity (Antibiotic Resistance)",
        "difficulty": "Medium",
        "question": "How does widespread sub-therapeutic antibiotic administration in livestock accelerate the evolution of multi-drug resistant bacterial strains?",
        "options": [
            "It establishes strong directional selection, eliminating vulnerable bacteria while selecting for individuals bearing resistance alleles (often on plasmids)",
            "The antibiotic directly mutates bacterial chromosomal DNA at a specific point locus",
            "It induces eukaryotic endosymbiosis within gastrointestinal flora",
            "Antibiotics act as allosteric co-factors that activate ribosomal transcription factors in non-resistant strains"
        ],
        "answer": 0,
        "explanation": "Antibiotic exposure applies directional natural selection. Sensitive bacteria are destroyed, while rare mutants possessing resistance genes (often encoded on R-plasmids transmitted via conjugation) survive, reproduce, and dominate the population.",
        "citation": "IB Biology Subject Guide — Topic 5.2: Natural Selection"
    },

    # Topic 6: Human Physiology (28-34)
    {
        "id": "ib-bio-s1-028",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Digestion)",
        "difficulty": "Medium",
        "question": "Which enzyme is secreted by the acinar cells of the exocrine pancreas to digest triglycerides into monoglycerides and two free fatty acids in the small intestine?",
        "options": [
            "Pancreatic lipase",
            "Pepsin",
            "Salivary amylase",
            "Enteropeptidase"
        ],
        "answer": 0,
        "explanation": "Pancreatic lipase hydrolyzes dietary triglycerides emulsified by bile salts into monoglycerides and fatty acids within the alkaline lumen of the duodenum and jejunum.",
        "citation": "IB Biology Subject Guide — Topic 6.1: Digestion and Absorption"
    },
    {
        "id": "ib-bio-s1-029",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Circulatory System)",
        "difficulty": "Medium",
        "question": "What is the physiological role of the sinoatrial (SA) node located in the right atrium of the human heart?",
        "options": [
            "Acts as the primary cardiac pacemaker, initiating spontaneous myogenic electrical depolarizations that propagate across atrial myocytes",
            "Delays the action potential by 0.12 seconds to ensure complete ventricular filling before systole",
            "Rapidly conducts action potentials through the interventricular septum via Purkinje fibers",
            "Detects elevated systemic blood pressure and secretes antidiuretic hormone directly into coronary veins"
        ],
        "answer": 0,
        "explanation": "The sinoatrial (SA) node consists of modified myogenic cardiomyocytes that generate rhythmic action potentials without nervous stimulation, setting the basal heart rate (pacemaker).",
        "citation": "IB Biology Subject Guide — Topic 6.2: The Blood System"
    },
    {
        "id": "ib-bio-s1-030",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Immune Response)",
        "difficulty": "Hard",
        "question": "In the human blood clotting cascade, what is the role of active thrombin?",
        "options": [
            "Catalyzes the conversion of soluble fibrinogen into insoluble fibrin strands that entrap platelets and erythrocytes",
            "Hydrolyzes prothrombin into tissue thromboplastin at damaged endothelial surfaces",
            "Directly stimulates cytotoxic T cells to phagocytose circulating pathogenic bacterial clots",
            "Secretes heparin to prevent unwanted thrombosis in intact cerebral capillaries"
        ],
        "answer": 0,
        "explanation": "Clotting factors released from damaged platelets convert inactive prothrombin into active thrombin. Thrombin then enzymatically converts soluble fibrinogen into insoluble fibrin monomers that cross-link to form a mesh stabilizing the platelet plug.",
        "citation": "IB Biology Subject Guide — Topic 6.3: Defence Against Infectious Disease"
    },
    {
        "id": "ib-bio-s1-031",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Gas Exchange)",
        "difficulty": "Medium",
        "question": "What is the specialized function of Type II pneumocytes in the alveolar epithelium of human lungs?",
        "options": [
            "Secretion of pulmonary surfactant (phospholipids and proteins) to reduce alveolar surface tension and prevent lung collapse",
            "Extremely thin flattened squamous morphology to facilitate rapid passive diffusion of oxygen and carbon dioxide",
            "Ciliated beat movements to translocate mucus upward toward the pharyngeal mucociliary escalator",
            "Phagocytosis of inhaled asbestos particulate matter and microbial spores"
        ],
        "answer": 0,
        "explanation": "Type II pneumocytes are cuboidal cells that secrete pulmonary surfactant, a lipoprotein mixture that reduces surface tension in alveolar fluid, preventing alveoli from collapsing during expiration. (Type I pneumocytes carry out gas exchange).",
        "citation": "IB Biology Subject Guide — Topic 6.4: Gas Exchange"
    },
    {
        "id": "ib-bio-s1-032",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Neurons & Synapses)",
        "difficulty": "Hard",
        "question": "During the repolarization phase of an action potential along an axon, which ion channels open and which direction do the ions move?",
        "options": [
            "Voltage-gated K+ channels open, allowing rapid efflux of K+ ions out of the axon into extracellular fluid",
            "Voltage-gated Na+ channels open, allowing rapid influx of Na+ ions into the axoplasm",
            "Ligand-gated Cl- channels open, causing influx of Cl- ions to depolarize the axolemma",
            "Mechanosensitive Ca2+ pumps open, importing Ca2+ ions to restore the -70 mV resting potential"
        ],
        "answer": 0,
        "explanation": "At peak depolarization (+30 to +40 mV), voltage-gated Na+ channels inactivate. Voltage-gated K+ channels open, driving K+ ions out of the cell down their electrochemical gradient, restoring the negative internal membrane potential (repolarization).",
        "citation": "IB Biology Subject Guide — Topic 6.5: Neurons and Synapses"
    },
    {
        "id": "ib-bio-s1-033",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Endocrine Regulation)",
        "difficulty": "Easy",
        "question": "When blood glucose levels fall below normal fasting concentrations (~4.0–5.5 mmol/L), which hormone is secreted by the alpha (α) cells of the pancreatic islets of Langerhans?",
        "options": [
            "Glucagon",
            "Insulin",
            "Thyroxin",
            "Leptin"
        ],
        "answer": 0,
        "explanation": "Alpha cells secrete glucagon in response to hypoglycemia. Glucagon stimulates glycogenolysis (breakdown of glycogen to glucose) and gluconeogenesis in hepatocytes, releasing glucose into the bloodstream.",
        "citation": "IB Biology Subject Guide — Topic 6.6: Hormones, Homeostasis and Reproduction"
    },
    {
        "id": "ib-bio-s1-034",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Reproduction)",
        "difficulty": "Medium",
        "question": "Which hormone surge triggers ovulation (follicular rupture and secondary oocyte release) during the human menstrual cycle?",
        "options": [
            "Luteinizing hormone (LH)",
            "Progesterone",
            "Human chorionic gonadotropin (hCG)",
            "Prolactin"
        ],
        "answer": 0,
        "explanation": "Rising estrogen levels from the maturing Graafian follicle exert positive feedback on the anterior pituitary gland around day 12–14, triggering a steep spike in Luteinizing Hormone (LH surge) that initiates ovulation.",
        "citation": "IB Biology Subject Guide — Topic 6.6: Hormones, Homeostasis and Reproduction"
    },

    # Topic 7-11: Higher Level (HL) Extensions (35-40)
    {
        "id": "ib-bio-s1-035",
        "type": "mcq",
        "subtopic": "Topic 7: Nucleic Acids (DNA Replication Details)",
        "difficulty": "Hard",
        "question": "What is the specific enzymatic function of DNA Polymerase I during lagging strand replication in prokaryotes?",
        "options": [
            "Removes RNA primers through 5' to 3' exonuclease activity and replaces them with complementary deoxyribonucleotides",
            "Synthesizes the bulk of the Okazaki fragments continuously from 5' to 3'",
            "Unwinds the double-stranded DNA helix ahead of the replication fork by breaking hydrogen bonds",
            "Forms covalent phosphodiester bonds between adjacent 3'-hydroxyl and 5'-phosphate Okazaki termini"
        ],
        "answer": 0,
        "explanation": "DNA Polymerase III synthesizes Okazaki fragments. DNA Polymerase I removes the RNA primer ribonucleotides using its 5'→3' exonuclease activity and fills the resulting gaps with DNA nucleotides. DNA ligase subsequently seals the nicks.",
        "citation": "IB Biology Subject Guide — Topic 7.1: DNA Structure and Replication (HL)"
    },
    {
        "id": "ib-bio-s1-036",
        "type": "mcq",
        "subtopic": "Topic 9: Plant Biology (Transpiration Stream)",
        "difficulty": "Medium",
        "question": "Which physical forces maintain the continuous unbroken column of water in xylem vessels under negative pressure during transpiration in tall trees?",
        "options": [
            "Cohesion between water molecules via hydrogen bonding and adhesion of water molecules to hydrophilic xylem cell walls containing cellulose and lignin",
            "Active symplastic pumping of sucrose by companion cells into vessel elements",
            "Positive turgor pressure generated by root cortical endodermis Casparian strips",
            "Osmotic pull generated exclusively by active stomatal closure at midday"
        ],
        "answer": 0,
        "explanation": "The cohesion-tension theory explains water transport: evaporation at mesophyll cell surfaces generates negative hydrostatic pressure (tension). Cohesion (hydrogen bonds between water molecules) and adhesion (attraction to xylem walls) prevent cavitation.",
        "citation": "IB Biology Subject Guide — Topic 9.1: Transport in the Xylem of Plants (HL)"
    },
    {
        "id": "ib-bio-s1-037",
        "type": "mcq",
        "subtopic": "Topic 9: Plant Biology (Phloem Translocation)",
        "difficulty": "Hard",
        "question": "How is sucrose loaded into phloem sieve tube elements at a source (e.g., mature photosynthetic leaf)?",
        "options": [
            "Proton pumps actively expel H+ into the apoplast; H+/sucrose symporters then transport sucrose into companion cells against its concentration gradient",
            "Passive facilitated diffusion through non-gated aquaporin channels down a steep concentration gradient",
            "Pinocytosis of starch granules directly into sieve tube companion cell vacuoles",
            "Bulk flow driven by negative hydrostatic pressure created by root endodermal transpiration"
        ],
        "answer": 0,
        "explanation": "Active phloem loading uses ATP-driven proton pumps (H+-ATPase) to export protons into the apoplast. Sucrose-H+ symporters then cotransport sucrose together with protons back into companion cells, from where sucrose diffuses through plasmodesmata into sieve tubes.",
        "citation": "IB Biology Subject Guide — Topic 9.2: Transport in the Phloem of Plants (HL)"
    },
    {
        "id": "ib-bio-s1-038",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Kidney & Osmoregulation)",
        "difficulty": "Hard",
        "question": "How does antidiuretic hormone (ADH / vasopressin) increase water reabsorption in the human kidney collecting duct?",
        "options": [
            "ADH binds basolateral V2 receptors, triggering cAMP-mediated exocytosis of aquaporin-2 water channels into the apical luminal membrane",
            "ADH directly pumps sodium ions out of the collecting duct lumen to create an osmotic draw",
            "ADH constricts the afferent arteriole to drastically increase glomerular filtration pressure",
            "ADH hydrolyzes urea in the renal pelvis to generate hypotonic medullary interstitium"
        ],
        "answer": 0,
        "explanation": "ADH binds G-protein coupled receptors on principal cells in collecting ducts, initiating a signal cascade that translocates aquaporin-2 storage vesicles into the apical membrane. This dramatically increases water permeability, allowing water reabsorption into the hypertonic medulla.",
        "citation": "IB Biology Subject Guide — Topic 11.3: The Kidney and Osmoregulation (HL)"
    },
    {
        "id": "ib-bio-s1-039",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Muscle Contraction)",
        "difficulty": "Hard",
        "question": "What is the biochemical role of calcium ions (Ca2+) released from the sarcoplasmic reticulum during skeletal muscle contraction?",
        "options": [
            "Ca2+ binds to troponin, causing a conformational change in tropomyosin that exposes myosin-binding sites on actin filaments",
            "Ca2+ hydrolyzes ATP bound to the myosin heavy chain to trigger cross-bridge detachment",
            "Ca2+ binds to the Z-disc, mechanically shortening titin filaments within each sarcomere",
            "Ca2+ stimulates acetylcholine release from T-tubule voltage gates into the synaptic cleft"
        ],
        "answer": 0,
        "explanation": "Depolarization of T-tubules releases Ca2+ from the sarcoplasmic reticulum. Ca2+ binds troponin C, inducing a conformational shift that pulls tropomyosin away from actin active sites, enabling myosin heads to bind and form cross-bridges.",
        "citation": "IB Biology Subject Guide — Topic 11.2: Movement (HL)"
    },
    {
        "id": "ib-bio-s1-040",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Monoclonal Antibodies)",
        "difficulty": "Medium",
        "question": "In the production of monoclonal antibodies, what are hybridoma cells formed by fusing?",
        "options": [
            "Antigen-sensitized B-lymphocytes (plasma cells) and immortal myeloma (cancer) cells",
            "Cytotoxic T-lymphocytes and active macrophages",
            "Red blood cells and embryonic stem cell colonies",
            "Human memory helper T cells and bacterial spheroplasts"
        ],
        "answer": 0,
        "explanation": "Hybridoma technology fuses antibody-producing plasma B cells (isolated from an immunized animal spleen) with immortal myeloma cells. The resulting hybrid cells divide indefinitely while producing large quantities of a single monoclonal antibody.",
        "citation": "IB Biology Subject Guide — Topic 11.1: Antibody Production and Vaccination (HL)"
    }
]

# -------------------------------------------------------------
# 2. IB DP BIOLOGY (HL / SL) PAPER 1 — SET 2 (40 Questions)
# -------------------------------------------------------------
bio_set2_questions = [
    {
        "id": "ib-bio-s2-001",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Stem Cells & Differentiation)",
        "difficulty": "Medium",
        "question": "What defines pluripotent embryonic stem cells compared to multipotent adult stem cells?",
        "options": [
            "Pluripotent stem cells can differentiate into almost any cell type derived from all three germ layers, whereas multipotent stem cells are committed to a limited lineage",
            "Pluripotent stem cells cannot undergo continuous mitotic division in cell culture",
            "Multipotent stem cells can differentiate into entire functional extraembryonic placental tissues",
            "Pluripotent stem cells contain only half the diploid number of chromosomes"
        ],
        "answer": 0,
        "explanation": "Pluripotent stem cells (e.g. from the blastocyst inner cell mass) can form cells from ectoderm, mesoderm, and endoderm. Multipotent stem cells (e.g., hematopoietic bone marrow cells) can only produce cells of a specific related lineage.",
        "citation": "IB Biology Subject Guide — Topic 1.1: Introduction to Cells"
    },
    {
        "id": "ib-bio-s2-002",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Prokaryotic vs Eukaryotic Ultrastructure)",
        "difficulty": "Easy",
        "question": "Which organelle is found in both prokaryotic bacterium and eukaryotic hepatocytes?",
        "options": [
            "Ribosomes",
            "Mitochondria",
            "Endoplasmic reticulum",
            "Golgi apparatus"
        ],
        "answer": 0,
        "explanation": "Ribosomes are non-membrane bound organelles present in both prokaryotes (70S) and eukaryotes (80S), carrying out polypeptide translation.",
        "citation": "IB Biology Subject Guide — Topic 1.2: Ultrastructure of Cells"
    },
    {
        "id": "ib-bio-s2-003",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Osmosis & Plant Turgor)",
        "difficulty": "Medium",
        "question": "When plant tissue is placed in a hypertonic sucrose solution with a more negative water potential than the cytoplasm, what physiological event occurs?",
        "options": [
            "Plasmolysis occurs as water leaves the cell by osmosis, causing the plasma membrane to detach from the cell wall",
            "The cell becomes fully turgid as water rushes into the central vacuole down its osmotic gradient",
            "The cell bursts due to osmotic lysis because plant cell walls cannot withstand tensile tension",
            "Active sucrose symporters pump water out of the cell against concentration gradients"
        ],
        "answer": 0,
        "explanation": "In a hypertonic solution (lower water potential/higher osmolarity), water leaves the plant cell vacuole via osmosis. Turgor pressure drops to zero, and the shrinking protoplast pulls away from the rigid cellulose wall (plasmolysis).",
        "citation": "IB Biology Subject Guide — Topic 1.4: Membrane Transport"
    },
    {
        "id": "ib-bio-s2-004",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Mitotic Index & Oncogenesis)",
        "difficulty": "Medium",
        "question": "In a biopsy sample of malignant tumor tissue, 120 cells out of 800 counted cells are undergoing active mitosis. What is the mitotic index?",
        "options": [
            "0.15 (15%)",
            "0.015 (1.5%)",
            "0.66 (66%)",
            "0.08 (8%)"
        ],
        "answer": 0,
        "explanation": "Mitotic Index = (Number of cells in mitosis) / (Total number of cells). Mitotic Index = 120 / 800 = 0.15 (or 15%). Elevated mitotic indices are diagnostic of rapid cell proliferation in carcinomas.",
        "citation": "IB Biology Subject Guide — Topic 1.6: Cell Division"
    },
    {
        "id": "ib-bio-s2-005",
        "type": "mcq",
        "subtopic": "Topic 1: Cell Biology (Endocytosis vs Exocytosis)",
        "difficulty": "Easy",
        "question": "Which vesicular transport process involves the cell engulfing large extracellular macromolecules by invaginating its plasma membrane to pinch off an intracellular vesicle?",
        "options": [
            "Endocytosis",
            "Exocytosis",
            "Facilitated diffusion",
            "Osmotic filtration"
        ],
        "answer": 0,
        "explanation": "Endocytosis is the active process by which cells internalize external particles or fluid by folding the plasma membrane inward until a vesicle forms inside the cell (requires ATP and membrane fluidity).",
        "citation": "IB Biology Subject Guide — Topic 1.4: Membrane Transport"
    },
    {
        "id": "ib-bio-s2-006",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Anabolism vs Catabolism)",
        "difficulty": "Easy",
        "question": "Which reaction represents an anabolic metabolic process requiring condensation and ATP input?",
        "options": [
            "Synthesis of a polypeptide chain from amino acid monomers on a ribosome",
            "Hydrolysis of glycogen into individual glucose-6-phosphate molecules in skeletal muscle",
            "Catabolic breakdown of glucose to pyruvate during glycolysis",
            "Oxidative deamination of amino acids into urea and keto acids in liver tissue"
        ],
        "answer": 0,
        "explanation": "Anabolism refers to the metabolic synthesis of complex organic macromolecules from simpler precursor monomers via condensation reactions, consuming ATP energy (e.g. protein synthesis, DNA replication).",
        "citation": "IB Biology Subject Guide — Topic 2.1: Molecules to Metabolism"
    },
    {
        "id": "ib-bio-s2-007",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Protein Denaturation)",
        "difficulty": "Medium",
        "question": "How does extreme deviation from optimum pH cause permanent denaturation of a globular enzyme?",
        "options": [
            "Alters the ionization and charges on amino acid R-groups, disrupting ionic bonds and hydrogen bonds that maintain tertiary structure",
            "Breaks all primary peptide bonds between adjacent amino acids",
            "Hydrolyzes all carbon-carbon covalent bonds throughout the polypeptide backbone",
            "Inverts the chirality of alpha carbons from L-amino acids to D-amino acids"
        ],
        "answer": 0,
        "explanation": "Changes in pH alter the ionization of acidic and basic R-groups (e.g., carboxyl and amino groups). This disrupts ionic interactions and hydrogen bonds stabilizing the enzyme's specific 3D tertiary conformation, causing loss of catalytic active site structure.",
        "citation": "IB Biology Subject Guide — Topic 2.5: Enzymes"
    },
    {
        "id": "ib-bio-s2-008",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (DNA vs RNA)",
        "difficulty": "Easy",
        "question": "Which combination of pentose sugar and nitrogenous pyrimidine base distinguishes RNA from DNA?",
        "options": [
            "Ribose and Uracil",
            "Deoxyribose and Thymine",
            "Ribose and Cytosine",
            "Deoxyribose and Adenine"
        ],
        "answer": 0,
        "explanation": "RNA contains ribose sugar (with a 2'-OH hydroxyl group) and the pyrimidine base uracil, whereas DNA contains 2'-deoxyribose sugar and thymine.",
        "citation": "IB Biology Subject Guide — Topic 2.6: Structure of DNA and RNA"
    },
    {
        "id": "ib-bio-s2-009",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Cell Respiration & Anaerobic Fermentation)",
        "difficulty": "Medium",
        "question": "What is the primary evolutionary purpose of converting pyruvate to lactate during anaerobic exercise in human myocytes?",
        "options": [
            "To regenerate NAD+ from NADH so that glycolysis can continue synthesizing ATP",
            "To yield 36 additional ATP molecules in the absence of oxygen",
            "To transport surplus carbon into the mitochondrial cristae for storage",
            "To neutralize lactic acidosis within the blood plasma buffer system"
        ],
        "answer": 0,
        "explanation": "In anaerobic conditions, the electron transport chain shuts down, accumulating NADH. Lactate dehydrogenase reduces pyruvate to lactate while oxidizing NADH to NAD+, replenishing the NAD+ required to sustain ATP production by glycolysis.",
        "citation": "IB Biology Subject Guide — Topic 2.8: Cell Respiration"
    },
    {
        "id": "ib-bio-s2-010",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Action Spectrum vs Absorption Spectrum)",
        "difficulty": "Medium",
        "question": "What does the action spectrum of photosynthesis depict?",
        "options": [
            "The relative rate of photosynthetic activity at different wavelengths of light across the visible spectrum",
            "The percentage of light absorbed by an isolated solution of chlorophyll a",
            "The exact absorption bands of thylakoid carotenes in non-polar organic solvents",
            "The rate of stomatal transpiration at varying ambient temperatures"
        ],
        "answer": 0,
        "explanation": "An action spectrum shows the rate of photosynthesis (e.g. oxygen production) across the visible light spectrum (400–700 nm), demonstrating peak efficiency in blue (~430 nm) and red (~660 nm) wavelengths.",
        "citation": "IB Biology Subject Guide — Topic 2.9: Photosynthesis"
    },
    {
        "id": "ib-bio-s2-011",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (Rubisco & Calvin Cycle)",
        "difficulty": "Hard",
        "question": "In the light-independent reactions (Calvin cycle), which reaction is catalyzed by the enzyme Rubisco?",
        "options": [
            "Carboxylation of ribulose bisphosphate (RuBP, 5C) by CO2 to yield an unstable 6C intermediate that splits into two molecules of glycerate-3-phosphate (GP, 3C)",
            "Reduction of glycerate-3-phosphate (GP) into triose phosphate (TP) using ATP and NADPH",
            "Regeneration of RuBP from triose phosphate requiring consumption of GTP",
            "Oxidative decarboxylation of glucose into two molecules of oxaloacetate"
        ],
        "answer": 0,
        "explanation": "Ribulose-1,5-bisphosphate carboxylase-oxygenase (Rubisco) fixes atmospheric CO2 onto the 5-carbon sugar RuBP. The unstable 6-carbon intermediate breaks down immediately into two 3-carbon molecules of glycerate-3-phosphate (GP).",
        "citation": "IB Biology Subject Guide — Topic 8.3: Photosynthesis (HL)"
    },
    {
        "id": "ib-bio-s2-012",
        "type": "mcq",
        "subtopic": "Topic 2: Molecular Biology (End-Product Inhibition)",
        "difficulty": "Hard",
        "question": "In the metabolic pathway converting threonine to isoleucine in bacteria, how does isoleucine regulate its own synthesis when cellular concentrations are high?",
        "options": [
            "Acts as a non-competitive allosteric inhibitor of the first enzyme in the pathway, threonine deaminase",
            "Binds covalently to bacterial ribosomes to permanently degrade mRNA transcripts",
            "Competes directly with threonine at the catalytic active site of threonine deaminase",
            "Hydrolyzes all downstream intermediate metabolites through feedback proteolysis"
        ],
        "answer": 0,
        "explanation": "This is the classic textbook example of end-product feedback inhibition. When isoleucine accumulates, it binds to an allosteric regulatory site on threonine deaminase (the first enzyme), altering its conformation and shutting down the pathway.",
        "citation": "IB Biology Subject Guide — Topic 8.1: Enzymes (HL)"
    },
    {
        "id": "ib-bio-s2-013",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Karyograms & Non-Disjunction)",
        "difficulty": "Medium",
        "question": "A diagnostic karyogram shows 47 chromosomes with three copies of chromosome 21 in every somatic cell. What clinical condition is diagnosed, and what meiotic error caused it?",
        "options": [
            "Down syndrome; caused by non-disjunction of homologous chromosomes during Anaphase I or sister chromatids during Anaphase II",
            "Turner syndrome; caused by non-disjunction of sex chromosomes in parental spermatogenesis",
            "Klinefelter syndrome; caused by maternal crossing over failure in Prophase II",
            "Edward syndrome; caused by Robertsonian translocation of chromosome 18"
        ],
        "answer": 0,
        "explanation": "Trisomy 21 causes Down syndrome. It results from non-disjunction during gametogenesis (failure of homologous chromosomes to separate in anaphase I or sister chromatids in anaphase II), leading to a gamete with 24 chromosomes.",
        "citation": "IB Biology Subject Guide — Topic 3.3: Meiosis"
    },
    {
        "id": "ib-bio-s2-014",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Sickle Cell Anemia Mutation)",
        "difficulty": "Medium",
        "question": "Which specific base substitution mutation in the HBB gene causes sickle cell anemia?",
        "options": [
            "GAG is mutated to GTG on the sense DNA strand, causing valine to replace glutamic acid at position 6 of the beta-globin polypeptide",
            "AAG is mutated to TAG, introducing a premature stop codon that truncates the alpha-globin chain",
            "Insertion of an extra adenine residue, causing a complete frameshift mutation",
            "Deletion of three nucleotides, deleting a single phenylalanine residue in the transmembrane channel"
        ],
        "answer": 0,
        "explanation": "The sickle-cell mutation is a single base substitution where the 6th codon of the beta-globin gene changes from GAG to GTG (mRNA: GAG to GUG). This substitutes polar, hydrophilic glutamic acid with non-polar, hydrophobic valine, causing hemoglobin to polymerize in low oxygen.",
        "citation": "IB Biology Subject Guide — Topic 3.1: Genes"
    },
    {
        "id": "ib-bio-s2-015",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Gel Electrophoresis)",
        "difficulty": "Easy",
        "question": "During agarose gel electrophoresis of restriction-digested DNA fragments, why do smaller DNA fragments migrate faster towards the positive anode (+)?",
        "options": [
            "All DNA fragments have a uniform negative charge due to phosphate groups, and smaller fragments experience less frictional resistance through the agarose matrix",
            "Smaller DNA fragments possess a higher net positive charge than larger fragments",
            "Agarose gel pores selectively bind larger nucleotide bases like adenine and guanine",
            "DNA ligase actively propels smaller fragments towards the electrode"
        ],
        "answer": 0,
        "explanation": "DNA has a constant charge-to-mass ratio due to negatively charged phosphate groups in its sugar-phosphate backbone, causing it to migrate toward the positive anode (+). The agarose gel acts as a molecular sieve; shorter fragments encounter less resistance and travel further.",
        "citation": "IB Biology Subject Guide — Topic 3.5: Genetic Modification and Biotechnology"
    },
    {
        "id": "ib-bio-s2-016",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Polygenic Inheritance)",
        "difficulty": "Hard",
        "question": "Why does continuous variation (such as human height or melanin skin pigmentation) follow a bell-shaped normal distribution curve?",
        "options": [
            "The trait is controlled by multiple unlinked polygenic loci, whose additive alleles combine with environmental influences",
            "The trait is governed by a single Mendelian locus with complete dominance",
            "The trait results strictly from autosomal non-disjunction in parental meiosis",
            "Epigenetic methylation completely silences all maternal alleles in embryonic development"
        ],
        "answer": 0,
        "explanation": "Polygenic traits are controlled by two or more genes located at different loci. As the number of contributing additive alleles increases, the number of possible phenotypic combinations increases dramatically, approximating a smooth bell-shaped normal distribution.",
        "citation": "IB Biology Subject Guide — Topic 10.2: Inheritance (HL)"
    },
    {
        "id": "ib-bio-s2-017",
        "type": "mcq",
        "subtopic": "Topic 3: Genetics (Gene Pools & Allele Frequencies)",
        "difficulty": "Medium",
        "question": "In a population of butterflies in Hardy-Weinberg equilibrium, the frequency of homozygous recessive white wing phenotype (q²) is 0.09. What is the frequency of heterozygous carriers (2pq) in this population?",
        "options": [
            "0.42 (42%)",
            "0.49 (49%)",
            "0.30 (30%)",
            "0.21 (21%)"
        ],
        "answer": 0,
        "explanation": "q² = 0.09 ⇒ q = 0.3. Since p + q = 1, p = 1 - 0.3 = 0.7. The heterozygous carrier frequency is 2pq = 2(0.7)(0.3) = 0.42 (42%).",
        "citation": "IB Biology Subject Guide — Topic 10.3: Gene Pools and Speciation (HL)"
    },
    {
        "id": "ib-bio-s2-018",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Trophic Classification)",
        "difficulty": "Easy",
        "question": "An organism that ingests other living or recently killed organisms to obtain internal chemical nutrition is classified as what?",
        "options": [
            "A consumer (heterotroph)",
            "A saprotroph",
            "An autotroph",
            "A detritivore"
        ],
        "answer": 0,
        "explanation": "Consumers are heterotrophs that feed on living organisms by ingestion. Detritivores ingest non-living organic detritus internally, while saprotrophs secrete digestive enzymes externally and absorb the products.",
        "citation": "IB Biology Subject Guide — Topic 4.1: Species, Communities and Ecosystems"
    },
    {
        "id": "ib-bio-s2-019",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Methanogenesis)",
        "difficulty": "Medium",
        "question": "Which domain of organisms produces methane (CH4) gas from organic matter in anoxic environments like wetlands, digestive tracts of ruminants, and landfill sites?",
        "options": [
            "Archaea (methanogenic archaeans)",
            "Eubacteria (cyanobacteria)",
            "Fungi (ascomycetes)",
            "Protista (ciliates)"
        ],
        "answer": 0,
        "explanation": "Methanogenesis is carried out exclusively by methanogenic archaeans in strictly anaerobic conditions. They convert acetate, carbon dioxide, and hydrogen into methane gas: CO2 + 4H2 → CH4 + 2H2O.",
        "citation": "IB Biology Subject Guide — Topic 4.3: Carbon Cycling"
    },
    {
        "id": "ib-bio-s2-020",
        "type": "mcq",
        "subtopic": "Topic 4: Ecology (Sustainability of Ecosystems)",
        "difficulty": "Medium",
        "question": "Which three fundamental requirements are essential for the long-term sustainability of an ecological mesocosm?",
        "options": [
            "Continuous supply of energy (light), nutrient recycling by decomposers, and detoxification of metabolic waste products",
            "Continuous artificial addition of synthetic nitrogen fertilizer, aeration, and pesticide application",
            "Presence of apex carnivorous predators, continuous water outflow, and soil turnover",
            "Constant ambient temperature of exactly 37 °C, zero fungal presence, and airtight vacuum sealing"
        ],
        "answer": 0,
        "explanation": "Ecosystem sustainability depends on three requirements: continuous energy availability (e.g., sunlight for photosynthesis), nutrient availability through internal nutrient cycles (saprotrophic recycling), and recycling/detoxification of waste products.",
        "citation": "IB Biology Subject Guide — Topic 4.1: Species, Communities and Ecosystems"
    },
    {
        "id": "ib-bio-s2-021",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution (Speciation & Reproductive Isolation)",
        "difficulty": "Medium",
        "question": "Two closely related species of chorus frogs occupy the same geographical pond habitat but breed during different months of the spring season. What type of reproductive isolation maintains their separate gene pools?",
        "options": [
            "Temporal isolation (sympatric)",
            "Geographic allopatric isolation",
            "Mechanical gametic isolation",
            "Behavioral hybrid inviability"
        ],
        "answer": 0,
        "explanation": "Temporal isolation occurs when populations reproduce at different times of day or different seasons, preventing interbreeding even when sharing the same geographic location (sympatric isolation).",
        "citation": "IB Biology Subject Guide — Topic 10.3: Gene Pools and Speciation (HL)"
    },
    {
        "id": "ib-bio-s2-022",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution (Directional, Stabilizing & Disruptive Selection)",
        "difficulty": "Hard",
        "question": "In a forest inhabited by light-colored and dark-colored peppered moths, intense industrial soot deposits on tree trunks led to a rapid increase in dark melanic morphs while light morphs were heavily predated. What form of natural selection occurred?",
        "options": [
            "Directional selection",
            "Stabilizing selection",
            "Disruptive selection",
            "Artificial cloning selection"
        ],
        "answer": 0,
        "explanation": "Directional selection favors one extreme phenotype over intermediate and opposite extreme phenotypes, shifting the population mean towards the advantageous extreme (melanism).",
        "citation": "IB Biology Subject Guide — Topic 10.3: Gene Pools and Speciation (HL)"
    },
    {
        "id": "ib-bio-s2-023",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution (Three Domains of Life)",
        "difficulty": "Medium",
        "question": "Based on Carl Woese's ribosomal RNA (16S/18S rRNA) sequence phylogeny, what are the three universally recognized domains of cellular life?",
        "options": [
            "Archaea, Eubacteria, and Eukaryota",
            "Monera, Protista, and Animalia",
            "Prokaryota, Plantae, and Fungi",
            "Bacteria, Extremophiles, and Mammalia"
        ],
        "answer": 0,
        "explanation": "Molecular sequencing established the three-domain system: Archaea, Eubacteria (true bacteria), and Eukaryota (eukaryotes).",
        "citation": "IB Biology Subject Guide — Topic 5.3: Classification of Biodiversity"
    },
    {
        "id": "ib-bio-s2-024",
        "type": "mcq",
        "subtopic": "Topic 5: Evolution (Analogous Structures & Convergent Evolution)",
        "difficulty": "Medium",
        "question": "The streamlined body shape and dorsal fins of sharks (cartilaginous fish) and dolphins (mammals) represent which evolutionary concept?",
        "options": [
            "Analogous structures arising from convergent evolution in response to similar hydrodynamic selective pressures",
            "Homologous structures inherited directly from an ancestral cetacean ancestor",
            "Vestigial structures undergoing rapid disruptive genetic drift",
            "Adaptive divergence from a recent common terrestrial ancestor"
        ],
        "answer": 0,
        "explanation": "Sharks and dolphins belong to distinct taxonomic classes (Chondrichthyes vs Mammalia). Their similar aquatic body forms are analogous structures evolved independently through convergent evolution in an open water habitat.",
        "citation": "IB Biology Subject Guide — Topic 5.4: Cladistics"
    },
    {
        "id": "ib-bio-s2-025",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Arteries vs Veins vs Capillaries)",
        "difficulty": "Medium",
        "question": "Which structural feature enables systemic arteries to withstand high pulsatile hydrostatic pressures generated during left ventricular systole?",
        "options": [
            "Thick tunica media containing dense elastic fibers and smooth muscle layers with a narrow lumen",
            "Thin collagenous walls with internal bicuspid pocket valves and wide lumens",
            "Fenestrated single-cell endothelium with zero basement membrane",
            "Continuous peristaltic bands of voluntary skeletal muscle"
        ],
        "answer": 0,
        "explanation": "Arteries have a thick tunica media rich in elastin fibers and smooth muscle, allowing them to expand during ventricular systole and recoil elastically during diastole, maintaining blood pressure.",
        "citation": "IB Biology Subject Guide — Topic 6.2: The Blood System"
    },
    {
        "id": "ib-bio-s2-026",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Antibiotic Specificity)",
        "difficulty": "Easy",
        "question": "Why are clinical antibiotics completely ineffective in treating viral infections such as influenza, measles, and COVID-19?",
        "options": [
            "Viruses lack their own metabolic pathways and cellular structures (no bacterial cell wall, 70S ribosomes, or replication enzymes), relying on host eukaryotic machinery",
            "Viruses rapidly mutate their outer lipid bilayers into peptidoglycan within minutes",
            "Antibiotics are degraded by human gastric bile salts before reaching viruses",
            "Viruses possess active efflux pumps that neutralize beta-lactam rings"
        ],
        "answer": 0,
        "explanation": "Antibiotics target bacterial prokaryotic structures and processes (e.g., transpeptidase enzymes that crosslink peptidoglycan cell walls, 70S bacterial ribosomes). Viruses lack cellular metabolism, replicating inside host eukaryotic cells, rendering antibiotics ineffective.",
        "citation": "IB Biology Subject Guide — Topic 6.3: Defence Against Infectious Disease"
    },
    {
        "id": "ib-bio-s2-027",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Mechanism of Breathing)",
        "difficulty": "Medium",
        "question": "During active physical inspiration, what are the coordinated muscular actions of the diaphragm and the intercostal muscles?",
        "options": [
            "The diaphragm contracts and flattens downward while external intercostal muscles contract, pulling ribs upward and outward to increase thoracic volume",
            "The diaphragm relaxes and arches upward while internal intercostal muscles contract",
            "Both internal and external intercostal muscles contract simultaneously, compressing pleural sacs",
            "The diaphragm relaxes while abdominal wall rectus muscles contract inward"
        ],
        "answer": 0,
        "explanation": "Inspiration requires expanding thoracic volume to lower intra-pulmonary pressure below atmospheric pressure. The diaphragm contracts and moves downward, and external intercostal muscles contract, pulling ribs up and out (antagonistic muscle action).",
        "citation": "IB Biology Subject Guide — Topic 6.4: Gas Exchange"
    },
    {
        "id": "ib-bio-s2-028",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Synaptic Transmission)",
        "difficulty": "Hard",
        "question": "At a cholinergic chemical synapse, what event directly triggers the exocytosis of acetylcholine vesicles into the synaptic cleft?",
        "options": [
            "Influx of calcium ions (Ca2+) through voltage-gated Ca2+ channels into the presynaptic terminal in response to an arriving action potential",
            "Efflux of potassium ions (K+) through non-gated leak channels",
            "Direct opening of ligand-gated sodium channels in the presynaptic axon hillock",
            "Hydrolysis of ATP by acetylcholinesterase bound to the presynaptic membrane"
        ],
        "answer": 0,
        "explanation": "When an action potential arrives at the axon terminal, the local depolarization causes voltage-gated Ca2+ channels in the presynaptic membrane to open. Inward diffusion of Ca2+ causes synapsin phosphorylation and vesicle fusion with the presynaptic membrane, releasing acetylcholine.",
        "citation": "IB Biology Subject Guide — Topic 6.5: Neurons and Synapses"
    },
    {
        "id": "ib-bio-s2-029",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Thyroxin & Thermoregulation)",
        "difficulty": "Easy",
        "question": "What is the primary physiological effect of thyroxin secreted by the thyroid gland?",
        "options": [
            "Increases basal metabolic rate and protein synthesis across body tissues, generating heat to regulate body temperature",
            "Lowers circulating calcium levels by stimulating osteoblast bone deposition",
            "Inhibits gluconeogenesis in hepatocytes during periods of physical sleep",
            "Accelerates water reabsorption in renal distal convoluted tubules"
        ],
        "answer": 0,
        "explanation": "Thyroxin (T4) targets nearly all body cells, stimulating the transcription of enzymes that increase the basal metabolic rate, oxygen consumption, and cellular carbohydrate/lipid metabolism, generating metabolic body heat.",
        "citation": "IB Biology Subject Guide — Topic 6.6: Hormones, Homeostasis and Reproduction"
    },
    {
        "id": "ib-bio-s2-030",
        "type": "mcq",
        "subtopic": "Topic 6: Human Physiology (Leptin & Melatonin)",
        "difficulty": "Medium",
        "question": "Which hormone is secreted by adipose tissue to act on the hypothalamus to inhibit appetite, and which hormone is secreted by the pineal gland to regulate circadian sleep cycles?",
        "options": [
            "Leptin (adipose) and Melatonin (pineal gland)",
            "Ghrelin (adipose) and Cortisol (pineal gland)",
            "Insulin (adipose) and Adrenaline (pineal gland)",
            "Prolactin (adipose) and Oxytocin (pineal gland)"
        ],
        "answer": 0,
        "explanation": "Leptin is produced by adipocytes; higher fat stores increase leptin secretion, which binds receptors in the hypothalamus to signal satiety. Melatonin is synthesized by the pineal gland in response to darkness, synchronizing the 24-hour sleep-wake cycle.",
        "citation": "IB Biology Subject Guide — Topic 6.6: Hormones, Homeostasis and Reproduction"
    },
    {
        "id": "ib-bio-s2-031",
        "type": "mcq",
        "subtopic": "Topic 7: Nucleic Acids (Nucleosomes & Epigenetics)",
        "difficulty": "Hard",
        "question": "How does chemical acetylation of lysine residues on histone protein tails affect gene expression?",
        "options": [
            "Neutralizes positive charges on histones, reducing their affinity for negatively charged DNA and decondensing chromatin into transcriptionally active euchromatin",
            "Tightens DNA wrapping around the nucleosome core into transcriptionally inactive heterochromatin",
            "Induces cleavage of phosphodiester bonds at all promoter TATA boxes",
            "Permanently deletes promoter regions from mammalian somatic chromosomes"
        ],
        "answer": 0,
        "explanation": "Histones are rich in positively charged lysine residues that bind negatively charged DNA. Histone acetyltransferases add acetyl groups, neutralizing lysine's charge. Chromatin relaxes into open euchromatin, allowing RNA polymerase access.",
        "citation": "IB Biology Subject Guide — Topic 7.2: Transcription and Gene Expression (HL)"
    },
    {
        "id": "ib-bio-s2-032",
        "type": "mcq",
        "subtopic": "Topic 7: Nucleic Acids (tRNA Activation)",
        "difficulty": "Hard",
        "question": "What is required for the attachment of a specific amino acid to its cognate tRNA molecule by an aminoacyl-tRNA synthetase enzyme?",
        "options": [
            "Hydrolysis of ATP to AMP and pyrophosphate (PPi) to form an aminoacyl-AMP intermediate",
            "Cleavage of GTP to GDP during peptide bond elongation",
            "Phosphorylation of the tRNA anticodon loop by cyclin-dependent kinases",
            "Direct protonation of the 5'-phosphate terminus of the acceptor stem"
        ],
        "answer": 0,
        "explanation": "Amino acid activation is a two-step reaction catalyzed by specific aminoacyl-tRNA synthetases: Amino acid + ATP → Aminoacyl-AMP + PPi, followed by transfer of the amino acid to the 3'-CCA terminus of the tRNA, storing energy for peptide bond synthesis.",
        "citation": "IB Biology Subject Guide — Topic 7.3: Translation (HL)"
    },
    {
        "id": "ib-bio-s2-033",
        "type": "mcq",
        "subtopic": "Topic 8: Cell Respiration (Krebs Cycle)",
        "difficulty": "Hard",
        "question": "For each turn of the citric acid (Krebs) cycle within the mitochondrial matrix, what are the total products generated from one acetyl-CoA (2C) molecule?",
        "options": [
            "2 CO2, 3 NADH, 1 FADH2, and 1 ATP (via GTP)",
            "1 CO2, 2 NADH, 2 FADH2, and 2 ATP",
            "3 CO2, 1 NADH, 3 FADH2, and 0 ATP",
            "4 CO2, 4 NADH, 0 FADH2, and 4 ATP"
        ],
        "answer": 0,
        "explanation": "One acetyl-CoA combines with oxaloacetate (4C) to form citrate (6C). During two oxidative decarboxylations and further dehydrogenations, 2 CO2 are released, 3 NAD+ are reduced to NADH, 1 FAD is reduced to FADH2, and 1 ATP/GTP is formed by substrate-level phosphorylation.",
        "citation": "IB Biology Subject Guide — Topic 8.2: Cell Respiration (HL)"
    },
    {
        "id": "ib-bio-s2-034",
        "type": "mcq",
        "subtopic": "Topic 9: Plant Biology (Xerophyte Adaptations)",
        "difficulty": "Medium",
        "question": "Which morphological adaptation minimizes transpirational water loss in xerophytic desert plants like Marram grass (Ammophila arenaria)?",
        "options": [
            "Rolled leaves with sunken stomata situated in interior microcrypts protected by epidermal trichomes (hairs)",
            "Extremely thin cuticles with broad flattened lamina to maximize radiant cooling",
            "High density of stomata exclusively on the upper adaxial leaf surface",
            "Permanent daytime opening of stomata coupled with total absence of root endodermis"
        ],
        "answer": 0,
        "explanation": "Marram grass rolls its leaves, trapping moist air in the inner core. Sunken stomata located in hair-lined pits create localized microclimates of high humidity, dramatically decreasing the water vapor concentration gradient and transpirational flux.",
        "citation": "IB Biology Subject Guide — Topic 9.1: Transport in the Xylem of Plants (HL)"
    },
    {
        "id": "ib-bio-s2-035",
        "type": "mcq",
        "subtopic": "Topic 9: Plant Biology (Phytochrome & Photoperiodism)",
        "difficulty": "Hard",
        "question": "How does phytochrome control flowering in short-day (long-night) plants?",
        "options": [
            "Active phytochrome Pfr acts as an inhibitor of flowering; during long uninterrupted nights, Pfr slowly reverts to inactive Pr, removing the inhibition and allowing flowering",
            "Pr absorbs far-red light and directly stimulates flowering promoter genes at noon",
            "Pfr accumulates during long nights and stimulates florigen synthesis in root meristems",
            "Short-day plants flower only when night length is repeatedly interrupted by brief red light flashes"
        ],
        "answer": 0,
        "explanation": "Phytochrome exists in two interconvertible forms: Pr (absorbs red light ~660 nm, converting to Pfr) and Pfr (absorbs far-red light ~730 nm, slowly reverting to Pr in darkness). In short-day plants, Pfr is an inhibitor of flowering. A long uninterrupted darkness period allows Pfr to drop below the threshold, triggering flowering.",
        "citation": "IB Biology Subject Guide — Topic 9.3: Reproduction in Plants (HL)"
    },
    {
        "id": "ib-bio-s2-036",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Antibody Structure)",
        "difficulty": "Medium",
        "question": "What structural feature of an immunoglobulin G (IgG) antibody molecule enables it to bind specifically to two identical epitopes simultaneously on a pathogen?",
        "options": [
            "A bivalent Y-shaped quaternary structure with two identical variable antigen-binding sites (Fab fragments) formed by the heavy and light chains",
            "A single constant domain containing four allosteric catalytic protease sites",
            "A circular carbohydrate ring surrounded by eight identical Fc fragments",
            "Disulfide bonds that crosslink with host erythrocyte hemoglobin"
        ],
        "answer": 0,
        "explanation": "An antibody consists of 4 polypeptide chains (2 heavy, 2 light) linked by disulfide bonds into a Y-shape. The tips of the Y form two hypervariable antigen-binding regions (Fab), conferring bivalent specificity.",
        "citation": "IB Biology Subject Guide — Topic 11.1: Antibody Production and Vaccination (HL)"
    },
    {
        "id": "ib-bio-s2-037",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Ultrafiltration in the Glomerulus)",
        "difficulty": "Hard",
        "question": "Which anatomical barrier in the renal corpuscle prevents albumin and other large plasma proteins from passing into the glomerular filtrate in Bowman's capsule?",
        "options": [
            "The negatively charged basement membrane (lamina densa) and filtration slits between podocyte pedicels",
            "The microvilli of the loop of Henle thin descending limb",
            "The endothelial tight junctions of the vasa recta capillaries",
            "The dense muscular sphincter of the macula densa"
        ],
        "answer": 0,
        "explanation": "Glomerular ultrafiltration is mediated by a 3-layer barrier: fenestrated capillary endothelium, the negatively charged basement membrane (which electrostatically repels negative plasma proteins like albumin), and interdigitating podocyte filtration slits.",
        "citation": "IB Biology Subject Guide — Topic 11.3: The Kidney and Osmoregulation (HL)"
    },
    {
        "id": "ib-bio-s2-038",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Countercurrent Multiplier in Loop of Henle)",
        "difficulty": "Hard",
        "question": "Why is the descending limb of the loop of Henle permeable to water but impermeable to sodium chloride, while the ascending limb is impermeable to water and actively pumps sodium chloride?",
        "options": [
            "To establish a steep hypertonic osmotic gradient in the medullary interstitium, enabling maximum passive water reabsorption from the collecting duct",
            "To neutralize acidic glomerular filtrate before it enters the renal pelvis",
            "To pump glucose into the renal cortex against steep diffusion gradients",
            "To dilute urine into hypotonic sweat for cutaneous excretion"
        ],
        "answer": 0,
        "explanation": "The countercurrent multiplier system creates an increasing osmotic gradient in the renal medulla (up to ~1200 mOsm/L). The active transport of Na+ and Cl- out of the thick ascending limb without water creates hypertonicity, drawing water out of the descending limb and collecting duct.",
        "citation": "IB Biology Subject Guide — Topic 11.3: The Kidney and Osmoregulation (HL)"
    },
    {
        "id": "ib-bio-s2-039",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Oogenesis vs Spermatogenesis)",
        "difficulty": "Medium",
        "question": "How does human oogenesis differ fundamentally from spermatogenesis in terms of meiotic timing and cellular yield?",
        "options": [
            "Oogenesis produces one functional ovum and polar bodies through unequal cytokinesis, with meiosis arrested in Prophase I until puberty, whereas spermatogenesis continuously produces four equal functional spermatozoa",
            "Oogenesis begins at puberty and produces four functional gametes per primary oocyte",
            "Spermatogenesis arrests in Metaphase II during embryonic fetal life until copulation",
            "Oogenesis proceeds without meiotic crossing over or chiasmata formation"
        ],
        "answer": 0,
        "explanation": "Oogenesis starts before birth (primary oocytes arrest in Prophase I until puberty). Each cycle, one oocyte resumes meiosis, arresting at Metaphase II until fertilization, producing only 1 mature ovum and 2-3 non-functional polar bodies due to unequal cytoplasmic division.",
        "citation": "IB Biology Subject Guide — Topic 11.4: Sexual Reproduction (HL)"
    },
    {
        "id": "ib-bio-s2-040",
        "type": "mcq",
        "subtopic": "Topic 11: Animal Physiology (Cortical Reaction & Polyspermy Prevention)",
        "difficulty": "Hard",
        "question": "What is the biochemical mechanism of the cortical reaction in the ovum following sperm fusion?",
        "options": [
            "Cortical granules release enzymes via exocytosis that digest sperm-binding receptors and harden the zona pellucida, permanently preventing polyspermy",
            "Rapid influx of potassium ions hyperpolarizes the vitelline membrane, attracting additional sperm nuclei",
            "The ovum discharges maternal lysosomes into the perivitelline space to hydrolyze the male pronucleus",
            "The corona radiata forms an impermeable chitin shell within 5 milliseconds"
        ],
        "answer": 0,
        "explanation": "Sperm-egg fusion triggers an intracellular Ca2+ wave that prompts cortical granules to fuse with the egg plasma membrane. Their exocytosed proteases destroy ZP3 receptors and cross-link glycoproteins, hardening the zona pellucida into an impenetrable fertilization envelope (slow block to polyspermy).",
        "citation": "IB Biology Subject Guide — Topic 11.4: Sexual Reproduction (HL)"
    }
]

# ----------------------------------------------------------------------------------
# 3. IB DP MATHEMATICS: ANALYSIS & APPROACHES (AA HL/SL) — SET 1 (30 Questions)
# -------------------------------------------------------------
math_set1_questions = [
    # Topic 1: Number and Algebra (1-6)
    {
        "id": "ib-math-s1-001",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Arithmetic Sequences & Series)",
        "difficulty": "Easy",
        "question": "An arithmetic sequence has first term \\( u_1 = 5 \\) and common difference \\( d = 3 \\). What is the sum of the first 20 terms, \\( S_{20} \\)?",
        "options": [
            "670",
            "640",
            "700",
            "610"
        ],
        "answer": 0,
        "explanation": "Use \\( S_n = \\frac{n}{2}[2u_1 + (n-1)d] \\). Here \\( n = 20, u_1 = 5, d = 3 \\): \\( S_{20} = \\frac{20}{2}[2(5) + (19)(3)] = 10[10 + 57] = 10(67) = 670 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.2: Arithmetic Sequences and Series"
    },
    {
        "id": "ib-math-s1-002",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Infinite Geometric Series)",
        "difficulty": "Medium",
        "question": "The first term of a geometric sequence is \\( u_1 = 12 \\) and the sum to infinity is \\( S_\\infty = 36 \\). What is the common ratio \\( r \\)?",
        "options": [
            "\\( \\frac{2}{3} \\)",
            "\\( \\frac{1}{3} \\)",
            "\\( -\\frac{2}{3} \\)",
            "\\( \\frac{3}{4} \\)"
        ],
        "answer": 0,
        "explanation": "For an infinite convergent geometric series with \\( |r| < 1 \\), \\( S_\\infty = \\frac{u_1}{1 - r} \\). Substituting values: \\( 36 = \\frac{12}{1 - r} \\implies 1 - r = \\frac{12}{36} = \\frac{1}{3} \\implies r = 1 - \\frac{1}{3} = \\frac{2}{3} \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.3: Geometric Sequences and Series"
    },
    {
        "id": "ib-math-s1-003",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Logarithms & Exponents)",
        "difficulty": "Medium",
        "question": "If \\( \\log_3(x) + \\log_3(x - 2) = 1 \\), what is the value of \\( x \\)?",
        "options": [
            "3",
            "-1",
            "1",
            "\\( \\sqrt{3} \\)"
        ],
        "answer": 0,
        "explanation": "Combine logarithms: \\( \\log_3[x(x - 2)] = 1 \\implies x(x - 2) = 3^1 \\implies x^2 - 2x - 3 = 0 \\). Factoring gives \\( (x - 3)(x + 1) = 0 \\). Because the domain of \\( \\log_3(x) \\) requires \\( x > 2 \\), \\( x = -1 \\) is rejected as extraneous, so \\( x = 3 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.5: Laws of Logarithms"
    },
    {
        "id": "ib-math-s1-004",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Binomial Theorem)",
        "difficulty": "Medium",
        "question": "What is the coefficient of \\( x^4 \\) in the expansion of \\( (2x - 1)^6 \\)?",
        "options": [
            "240",
            "-240",
            "60",
            "160"
        ],
        "answer": 0,
        "explanation": "The general term is \\( T_{r+1} = \\binom{6}{r} (2x)^{6-r} (-1)^r \\). For the \\( x^4 \\) term, \\( 6 - r = 4 \\implies r = 2 \\). Term = \\( \\binom{6}{2} (2x)^4 (-1)^2 = 15 \\times 16x^4 \\times 1 = 240x^4 \\). Thus the coefficient is 240.",
        "citation": "IB Mathematics AA Guide — Topic 1.9: Binomial Theorem"
    },
    {
        "id": "ib-math-s1-005",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Complex Numbers in Polar Form)",
        "difficulty": "Hard",
        "question": "Let \\( z = 1 + i\\sqrt{3} \\). What is the exact value of \\( z^6 \\) using de Moivre's theorem?",
        "options": [
            "64",
            "-64",
            "64i",
            "-64i"
        ],
        "answer": 0,
        "explanation": "Modulus \\( r = \\sqrt{1^2 + (\\sqrt{3})^2} = 2 \\). Argument \\( \\theta = \\arctan(\\sqrt{3}/1) = \\frac{\\pi}{3} \\). In polar form, \\( z = 2 e^{i\\pi/3} \\). By de Moivre's theorem, \\( z^6 = 2^6 e^{i(6 \\times \\pi/3)} = 64 e^{i(2\\pi)} = 64(\\cos 2\\pi + i\\sin 2\\pi) = 64(1 + 0) = 64 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.13: Complex Numbers (HL)"
    },
    {
        "id": "ib-math-s1-006",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Proof by Mathematical Induction)",
        "difficulty": "Hard",
        "question": "When proving by mathematical induction that \\( 4^n - 1 \\) is divisible by 3 for all integers \\( n \\ge 1 \\), what is the inductive step algebraic expression for \\( 4^{k+1} - 1 \\)?",
        "options": [
            "\\( 4(4^k - 1) + 3 \\)",
            "\\( (4^k - 1) + 4 \\)",
            "\\( 3(4^k) - 4 \\)",
            "\\( 4^k(4 - 1) - 3 \\)"
        ],
        "answer": 0,
        "explanation": "\\( 4^{k+1} - 1 = 4 \\cdot 4^k - 1 = 4(4^k - 1 + 1) - 1 = 4(4^k - 1) + 4 - 1 = 4(4^k - 1) + 3 \\). Since \\( 4^k - 1 = 3M \\) by induction hypothesis, \\( 4(3M) + 3 = 3(4M + 1) \\), which is divisible by 3.",
        "citation": "IB Mathematics AA Guide — Topic 1.15: Proof by Induction (HL)"
    },

    # Topic 2: Functions (7-12)
    {
        "id": "ib-math-s1-007",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Composite & Inverse Functions)",
        "difficulty": "Medium",
        "question": "Let \\( f(x) = \\frac{2x + 1}{x - 3} \\) for \\( x \\ne 3 \\). What is the inverse function \\( f^{-1}(x) \\)?",
        "options": [
            "\\( \\frac{3x + 1}{x - 2} \\), \\( x \\ne 2 \\)",
            "\\( \\frac{x - 3}{2x + 1} \\), \\( x \\ne -\\frac{1}{2} \\)",
            "\\( \\frac{2x - 1}{x + 3} \\), \\( x \\ne -3 \\)",
            "\\( \\frac{3x - 1}{x - 2} \\), \\( x \\ne 2 \\)"
        ],
        "answer": 0,
        "explanation": "Set \\( y = \\frac{2x + 1}{x - 3} \\). Swap \\( x \\) and \\( y \\): \\( x = \\frac{2y + 1}{y - 3} \\implies x(y - 3) = 2y + 1 \\implies xy - 3x = 2y + 1 \\implies xy - 2y = 3x + 1 \\implies y(x - 2) = 3x + 1 \\implies y = \\frac{3x + 1}{x - 2} \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.2: Composite and Inverse Functions"
    },
    {
        "id": "ib-math-s1-008",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Transformations of Graphs)",
        "difficulty": "Easy",
        "question": "The graph of \\( y = f(x) \\) is transformed to \\( y = 3f(x - 2) + 5 \\). Which sequence of geometric transformations describes this change?",
        "options": [
            "Translation by vector \\( \\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix} \\) and vertical stretch with scale factor 3",
            "Translation by vector \\( \\begin{pmatrix} -2 \\\\ 5 \\end{pmatrix} \\) and horizontal stretch with scale factor 3",
            "Translation by vector \\( \\begin{pmatrix} 2 \\\\ -5 \\end{pmatrix} \\) and vertical stretch with scale factor \\( \\frac{1}{3} \\)",
            "Reflection in the x-axis followed by translation by vector \\( \\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix} \\)"
        ],
        "answer": 0,
        "explanation": "\\( f(x - 2) \\) translates the graph 2 units to the right (vector \\( \\begin{pmatrix} 2 \\\\ 0 \\end{pmatrix} \\)). Multiplying by 3 stretches the graph vertically by scale factor 3. Adding 5 translates the graph 5 units upward (vector \\( \\begin{pmatrix} 0 \\\\ 5 \\end{pmatrix} \\)). Total translation vector is \\( \\begin{pmatrix} 2 \\\\ 5 \\end{pmatrix} \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.3: Transformations of Graphs"
    },
    {
        "id": "ib-math-s1-009",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Quadratic Discriminant & Tangency)",
        "difficulty": "Medium",
        "question": "For what values of \\( k \\) does the line \\( y = 2x + k \\) touch the parabola \\( y = x^2 - 4x + 5 \\) at exactly one point?",
        "options": [
            "\\( k = -4 \\)",
            "\\( k = 4 \\)",
            "\\( k = 0 \\)",
            "\\( k = -1 \\)"
        ],
        "answer": 0,
        "explanation": "Set the equations equal: \\( x^2 - 4x + 5 = 2x + k \\implies x^2 - 6x + (5 - k) = 0 \\). For tangency (one intersection), the discriminant \\( \\Delta = b^2 - 4ac = 0 \\). \\( (-6)^2 - 4(1)(5 - k) = 0 \\implies 36 - 20 + 4k = 0 \\implies 16 + 4k = 0 \\implies 4k = -16 \\implies k = -4 \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.6: Quadratic Functions"
    },
    {
        "id": "ib-math-s1-010",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Rational Functions & Asymptotes)",
        "difficulty": "Medium",
        "question": "What are the vertical and horizontal asymptotes of the rational function \\( f(x) = \\frac{4x - 7}{2x + 6} \\)?",
        "options": [
            "Vertical asymptote: \\( x = -3 \\); Horizontal asymptote: \\( y = 2 \\)",
            "Vertical asymptote: \\( x = 3 \\); Horizontal asymptote: \\( y = 4 \\)",
            "Vertical asymptote: \\( x = -3 \\); Horizontal asymptote: \\( y = -\\frac{7}{6} \\)",
            "Vertical asymptote: \\( x = 2 \\); Horizontal asymptote: \\( y = -3 \\)"
        ],
        "answer": 0,
        "explanation": "The vertical asymptote occurs where the denominator is zero: \\( 2x + 6 = 0 \\implies x = -3 \\). The horizontal asymptote is the limit as \\( x \\to \\pm\\infty \\): \\( \\lim_{x \\to \\infty} \\frac{4x - 7}{2x + 6} = \\frac{4}{2} = 2 \\implies y = 2 \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.8: Rational Functions"
    },
    {
        "id": "ib-math-s1-011",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Modulus Equations)",
        "difficulty": "Medium",
        "question": "What is the complete solution set to the equation \\( |2x - 5| = x + 1 \\)?",
        "options": [
            "\\( x = 6 \\) and \\( x = \\frac{4}{3} \\)",
            "\\( x = 6 \\) only",
            "\\( x = 4 \\) and \\( x = -2 \\)",
            "\\( x = \\frac{4}{3} \\) only"
        ],
        "answer": 0,
        "explanation": "Case 1: \\( 2x - 5 = x + 1 \\implies x = 6 \\). Check: \\( |2(6) - 5| = |7| = 7 \\), \\( 6 + 1 = 7 \\) (Valid). Case 2: \\( 2x - 5 = -(x + 1) = -x - 1 \\implies 3x = 4 \\implies x = \\frac{4}{3} \\). Check: \\( |2(4/3) - 5| = |8/3 - 15/3| = |-7/3| = 7/3 \\), \\( 4/3 + 1 = 7/3 \\) (Valid). Both solutions are valid.",
        "citation": "IB Mathematics AA Guide — Topic 2.12: Modulus Functions (HL)"
    },
    {
        "id": "ib-math-s1-012",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Odd and Even Functions)",
        "difficulty": "Easy",
        "question": "Which of the following functions satisfies \\( f(-x) = -f(x) \\) for all \\( x \\in \\mathbb{R} \\) (is an odd function)?",
        "options": [
            "\\( f(x) = x^3 + \\sin(x) \\)",
            "\\( f(x) = x^4 + \\cos(x) \\)",
            "\\( f(x) = e^x + e^{-x} \\)",
            "\\( f(x) = x^2 + 3 \\)"
        ],
        "answer": 0,
        "explanation": "\\( f(-x) = (-x)^3 + \\sin(-x) = -x^3 - \\sin(x) = -(x^3 + \\sin x) = -f(x) \\). Since \\( f(-x) = -f(x) \\), the function is odd with rotational symmetry of 180° about the origin.",
        "citation": "IB Mathematics AA Guide — Topic 2.13: Odd and Even Functions (HL)"
    },

    # Topic 3: Geometry and Trigonometry (13-18)
    {
        "id": "ib-math-s1-013",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Radian Measure & Arc Length)",
        "difficulty": "Easy",
        "question": "A circle of radius \\( r = 6 \\text{ cm} \\) has a sector with an arc length of \\( 4\\pi \\text{ cm} \\). What is the area of this sector?",
        "options": [
            "\\( 12\\pi \\text{ cm}^2 \\)",
            "\\( 24\\pi \\text{ cm}^2 \\)",
            "\\( 6\\pi \\text{ cm}^2 \\)",
            "\\( 36\\pi \\text{ cm}^2 \\)"
        ],
        "answer": 0,
        "explanation": "Arc length \\( l = r\\theta \\implies 4\\pi = 6\\theta \\implies \\theta = \\frac{4\\pi}{6} = \\frac{2\\pi}{3} \\text{ rad} \\). Area of sector \\( A = \\frac{1}{2} r^2 \\theta = \\frac{1}{2} (6)^2 \\left(\\frac{2\\pi}{3}\\right) = \\frac{1}{2}(36)\\left(\\frac{2\\pi}{3}\\right) = 18 \\times \\frac{2\\pi}{3} = 12\\pi \\text{ cm}^2 \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.1: Radians, Arcs and Sectors"
    },
    {
        "id": "ib-math-s1-014",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Trigonometric Identities)",
        "difficulty": "Medium",
        "question": "Given that \\( \\cos\\theta = \\frac{3}{5} \\) and \\( \\frac{3\\pi}{2} < \\theta < 2\\pi \\) (Quadrant IV), what is the exact value of \\( \\sin(2\\theta) \\)?",
        "options": [
            "\\( -\\frac{24}{25} \\)",
            "\\( \\frac{24}{25} \\)",
            "\\( -\\frac{7}{25} \\)",
            "\\( \\frac{7}{25} \\)"
        ],
        "answer": 0,
        "explanation": "In Quadrant IV, sine is negative: \\( \\sin\\theta = -\\sqrt{1 - \\cos^2\\theta} = -\\sqrt{1 - 9/25} = -\\frac{4}{5} \\). Using the double angle identity \\( \\sin(2\\theta) = 2\\sin\\theta\\cos\\theta \\): \\( \\sin(2\\theta) = 2\\left(-\\frac{4}{5}\\right)\\left(\\frac{3}{5}\\right) = -\\frac{24}{25} \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.6: Double Angle Identities"
    },
    {
        "id": "ib-math-s1-015",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Trigonometric Equations)",
        "difficulty": "Medium",
        "question": "How many solutions exist for the equation \\( 2\\cos^2 x - \\cos x - 1 = 0 \\) in the interval \\( 0 \\le x \\le 2\\pi \\)?",
        "options": [
            "3",
            "2",
            "4",
            "1"
        ],
        "answer": 0,
        "explanation": "Factor the quadratic in \\( \\cos x \\): \\( (2\\cos x + 1)(\\cos x - 1) = 0 \\). Either \\( \\cos x = 1 \\) or \\( \\cos x = -\\frac{1}{2} \\). For \\( \\cos x = 1 \\) in \\( [0, 2\\pi] \\): \\( x = 0, 2\\pi \\) (2 solutions). For \\( \\cos x = -\\frac{1}{2} \\): \\( x = \\frac{2\\pi}{3}, \\frac{4\\pi}{3} \\) (2 solutions). Total solutions = 4? Wait, let's recount: \\( x = 0, \\frac{2\\pi}{3}, \\frac{4\\pi}{3}, 2\\pi \\). There are 4 solutions! Wait: Let's adjust options: 4, 3, 2, 1. If options: 4 is answer index 0.",
        "options": [
            "4",
            "3",
            "2",
            "1"
        ],
        "answer": 0,
        "explanation": "Factoring gives \\( (2\\cos x + 1)(\\cos x - 1) = 0 \\). From \\( \\cos x = 1 \\), we have \\( x = 0 \\) and \\( x = 2\\pi \\). From \\( \\cos x = -\\frac{1}{2} \\), we have \\( x = \\frac{2\\pi}{3} \\) and \\( x = \\frac{4\\pi}{3} \\). All four values lie in the interval \\( 0 \\le x \\le 2\\pi \\). Thus, there are exactly 4 solutions.",
        "citation": "IB Mathematics AA Guide — Topic 3.5: Solving Trigonometric Equations"
    },
    {
        "id": "ib-math-s1-016",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Scalar Product of Vectors)",
        "difficulty": "Easy",
        "question": "For which value of \\( p \\) are the vectors \\( \\mathbf{a} = \\begin{pmatrix} 3 \\\\ -2 \\\\ 4 \\end{pmatrix} \\) and \\( \\mathbf{b} = \\begin{pmatrix} 2 \\\\ p \\\\ -4 \\end{pmatrix} \\) perpendicular?",
        "options": [
            "\\( -5 \\)",
            "5",
            "\\( -2 \\)",
            "10"
        ],
        "answer": 0,
        "explanation": "Two non-zero vectors are perpendicular if and only if their scalar (dot) product is zero: \\( \\mathbf{a} \\cdot \\mathbf{b} = 0 \\implies (3)(2) + (-2)(p) + (4)(-4) = 0 \\implies 6 - 2p - 16 = 0 \\implies -10 - 2p = 0 \\implies 2p = -10 \\implies p = -5 \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.13: Scalar Product (HL)"
    },
    {
        "id": "ib-math-s1-017",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Vector Equation of a Line)",
        "difficulty": "Medium",
        "question": "A line \\( L \\) passes through point \\( A(1, -2, 3) \\) with direction vector \\( \\mathbf{d} = \\begin{pmatrix} 2 \\\\ 1 \\\\ -1 \\end{pmatrix} \\). Which of the following points lies on line \\( L \\)?",
        "options": [
            "\\( (5, 0, 1) \\)",
            "\\( (3, -1, 4) \\)",
            "\\( (-1, -3, 5) \\)",
            "\\( (1, 0, 2) \\)"
        ],
        "answer": 0,
        "explanation": "Vector equation: \\( \\mathbf{r} = \\begin{pmatrix} 1 \\\\ -2 \\\\ 3 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ 1 \\\\ -1 \\end{pmatrix} \\). For \\( \\lambda = 2 \\): \\( x = 1 + 2(2) = 5 \\), \\( y = -2 + 2(1) = 0 \\), \\( z = 3 + 2(-1) = 1 \\). Point \\( (5, 0, 1) \\) lies on the line.",
        "citation": "IB Mathematics AA Guide — Topic 3.14: Vector Equations of Lines (HL)"
    },
    {
        "id": "ib-math-s1-018",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Compound Angle Identities)",
        "difficulty": "Medium",
        "question": "What is the exact value of \\( \\cos(75^\\circ) = \\cos\\left(\\frac{5\\pi}{12}\\right) \\)?",
        "options": [
            "\\( \\frac{\\sqrt{6} - \\sqrt{2}}{4} \\)",
            "\\( \\frac{\\sqrt{6} + \\sqrt{2}}{4} \\)",
            "\\( \\frac{\\sqrt{3} - 1}{2} \\)",
            "\\( \\frac{\\sqrt{2} - \\sqrt{6}}{4} \\)"
        ],
        "answer": 0,
        "explanation": "Write \\( 75^\\circ = 45^\\circ + 30^\\circ \\). Using \\( \\cos(A + B) = \\cos A \\cos B - \\sin A \\sin B \\): \\( \\cos(45^\\circ + 30^\\circ) = \\cos 45^\\circ \\cos 30^\\circ - \\sin 45^\\circ \\sin 30^\\circ = \\left(\\frac{\\sqrt{2}}{2}\\right)\\left(\\frac{\\sqrt{3}}{2}\\right) - \\left(\\frac{\\sqrt{2}}{2}\\right)\\left(\\frac{1}{2}\\right) = \\frac{\\sqrt{6} - \\sqrt{2}}{4} \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.6: Compound Angle Identities"
    },

    # Topic 4: Statistics and Probability (19-24)
    {
        "id": "ib-math-s1-019",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Independent Events & Bayes)",
        "difficulty": "Medium",
        "question": "Events \\( A \\) and \\( B \\) are independent with \\( P(A) = 0.4 \\) and \\( P(B) = 0.5 \\). What is \\( P(A \\cup B) \\)?",
        "options": [
            "0.70",
            "0.90",
            "0.20",
            "0.60"
        ],
        "answer": 0,
        "explanation": "For independent events, \\( P(A \\cap B) = P(A) \\times P(B) = (0.4)(0.5) = 0.20 \\). Using the addition rule: \\( P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = 0.4 + 0.5 - 0.20 = 0.70 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.5: Independent Events"
    },
    {
        "id": "ib-math-s1-020",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Discrete Random Variables)",
        "difficulty": "Medium",
        "question": "A discrete random variable \\( X \\) has the probability distribution where \\( P(X=1) = 0.2 \\), \\( P(X=2) = 0.5 \\), and \\( P(X=3) = 0.3 \\). What is the expected value \\( E(X) \\)?",
        "options": [
            "2.1",
            "2.0",
            "2.3",
            "1.8"
        ],
        "answer": 0,
        "explanation": "\\( E(X) = \\sum x \\cdot P(X = x) = (1)(0.2) + (2)(0.5) + (3)(0.3) = 0.2 + 1.0 + 0.9 = 2.1 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.7: Discrete Random Variables"
    },
    {
        "id": "ib-math-s1-021",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Binomial Distribution)",
        "difficulty": "Medium",
        "question": "A fair six-sided die is rolled 5 times. Let \\( X \\) be the number of times a '6' is rolled (\\( X \\sim B(5, 1/6) \\)). What is the probability of rolling exactly two sixes, \\( P(X = 2) \\)?",
        "options": [
            "\\( 10 \\left(\\frac{1}{6}\\right)^2 \\left(\\frac{5}{6}\\right)^3 = \\frac{625}{3888} \\)",
            "\\( 5 \\left(\\frac{1}{6}\\right)^2 \\left(\\frac{5}{6}\\right)^3 = \\frac{625}{7776} \\)",
            "\\( \\left(\\frac{1}{6}\\right)^2 \\left(\\frac{5}{6}\\right)^3 \\)",
            "\\( 10 \\left(\\frac{1}{6}\\right)^3 \\left(\\frac{5}{6}\\right)^2 \\)"
        ],
        "answer": 0,
        "explanation": "Using the binomial formula \\( P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k} \\): \\( P(X = 2) = \\binom{5}{2} \\left(\\frac{1}{6}\\right)^2 \\left(\\frac{5}{6}\\right)^3 = 10 \\times \\frac{1}{36} \\times \\frac{125}{216} = \\frac{1250}{7776} = \\frac{625}{3888} \\approx 0.1608 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.8: Binomial Distribution"
    },
    {
        "id": "ib-math-s1-022",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Normal Distribution)",
        "difficulty": "Easy",
        "question": "A continuous random variable \\( X \\sim N(50, 16) \\) has mean \\( \\mu = 50 \\) and standard deviation \\( \\sigma = 4 \\). What is the z-score corresponding to \\( x = 58 \\)?",
        "options": [
            "+2.0",
            "+0.5",
            "+1.5",
            "-2.0"
        ],
        "answer": 0,
        "explanation": "Standardized score formula: \\( z = \\frac{x - \\mu}{\\sigma} \\). Variance \\( \\sigma^2 = 16 \\implies \\sigma = 4 \\). Thus, \\( z = \\frac{58 - 50}{4} = \\frac{8}{4} = +2.0 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.9: Normal Distribution"
    },
    {
        "id": "ib-math-s1-023",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Conditional Probability)",
        "difficulty": "Medium",
        "question": "Given that \\( P(A) = 0.6 \\), \\( P(B) = 0.3 \\), and \\( P(A \\cap B) = 0.18 \\), what is \\( P(A | B) \\)?",
        "options": [
            "0.60",
            "0.30",
            "0.18",
            "0.50"
        ],
        "answer": 0,
        "explanation": "By definition, \\( P(A | B) = \\frac{P(A \\cap B)}{P(B)} = \\frac{0.18}{0.3} = 0.60 \\). Note that \\( P(A | B) = P(A) \\), proving \\( A \\) and \\( B \\) are independent.",
        "citation": "IB Mathematics AA Guide — Topic 4.6: Conditional Probability"
    },
    {
        "id": "ib-math-s1-024",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Variance of Linear Transformation)",
        "difficulty": "Hard",
        "question": "A random variable \\( X \\) has variance \\( \\text{Var}(X) = 9 \\). What is the variance of \\( Y = 3 - 2X \\)?",
        "options": [
            "36",
            "-18",
            "18",
            "27"
        ],
        "answer": 0,
        "explanation": "By properties of variance for linear transformation \\( Y = aX + b \\): \\( \\text{Var}(aX + b) = a^2 \\text{Var}(X) \\). Here \\( a = -2 \\) and \\( b = 3 \\): \\( \\text{Var}(3 - 2X) = (-2)^2 \\text{Var}(X) = 4 \\times 9 = 36 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.14: Linear Combinations of Variables (HL)"
    },

    # Topic 5: Calculus (25-30)
    {
        "id": "ib-math-s1-025",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Chain Rule & Product Rule)",
        "difficulty": "Medium",
        "question": "What is the derivative of \\( f(x) = x^2 e^{3x} \\) with respect to \\( x \\)?",
        "options": [
            "\\( x e^{3x}(2 + 3x) \\)",
            "\\( 2x e^{3x} \\)",
            "\\( 6x e^{3x} \\)",
            "\\( 3x^2 e^{3x} \\)"
        ],
        "answer": 0,
        "explanation": "Using the product rule \\( (uv)' = u'v + uv' \\) with \\( u = x^2 \\implies u' = 2x \\) and \\( v = e^{3x} \\implies v' = 3e^{3x} \\): \\( f'(x) = 2x e^{3x} + x^2 (3e^{3x}) = x e^{3x}(2 + 3x) \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.6: Product and Chain Rules"
    },
    {
        "id": "ib-math-s1-026",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Equation of Tangent Line)",
        "difficulty": "Medium",
        "question": "What is the equation of the tangent line to the curve \\( y = x^3 - 2x + 4 \\) at the point where \\( x = 1 \\)?",
        "options": [
            "\\( y = x + 2 \\)",
            "\\( y = 3x \\)",
            "\\( y = x - 2 \\)",
            "\\( y = 2x + 1 \\)"
        ],
        "answer": 0,
        "explanation": "When \\( x = 1 \\), \\( y = 1^3 - 2(1) + 4 = 3 \\). The point of tangency is \\( (1, 3) \\). Derivative \\( \\frac{dy}{dx} = 3x^2 - 2 \\). At \\( x = 1 \\), gradient \\( m = 3(1)^2 - 2 = 1 \\). Tangent equation: \\( y - y_1 = m(x - x_1) \\implies y - 3 = 1(x - 1) \\implies y = x + 2 \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.7: Tangents and Normals"
    },
    {
        "id": "ib-math-s1-027",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Optimization & Second Derivative Test)",
        "difficulty": "Medium",
        "question": "For the function \\( f(x) = 2x^3 - 9x^2 + 12x - 3 \\), what are the coordinates and nature of the local maximum point?",
        "options": [
            "\\( (1, 2) \\), Local Maximum",
            "\\( (2, 1) \\), Local Maximum",
            "\\( (1, 2) \\), Local Minimum",
            "\\( (2, 1) \\), Point of Inflexion"
        ],
        "answer": 0,
        "explanation": "\\( f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x - 1)(x - 2) \\). Stationary points at \\( x = 1 \\) and \\( x = 2 \\). Second derivative \\( f''(x) = 12x - 18 \\). At \\( x = 1 \\): \\( f''(1) = 12 - 18 = -6 < 0 \\implies \\) Local Maximum. Value \\( f(1) = 2(1)^3 - 9(1)^2 + 12(1) - 3 = 2 \\). Local maximum is at \\( (1, 2) \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.8: Local Extrema and Curve Sketching"
    },
    {
        "id": "ib-math-s1-028",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Kinematics)",
        "difficulty": "Medium",
        "question": "A particle moves along a straight line such that its velocity at time \\( t \\ge 0 \\) is \\( v(t) = 3t^2 - 12t + 9 \\text{ m/s} \\). At what times is the particle instantaneously at rest?",
        "options": [
            "\\( t = 1 \\text{ s} \\) and \\( t = 3 \\text{ s} \\)",
            "\\( t = 2 \\text{ s} \\) only",
            "\\( t = 0 \\text{ s} \\) and \\( t = 4 \\text{ s} \\)",
            "\\( t = 3 \\text{ s} \\) and \\( t = 9 \\text{ s} \\)"
        ],
        "answer": 0,
        "explanation": "A particle is instantaneously at rest when \\( v(t) = 0 \\). Set \\( 3t^2 - 12t + 9 = 0 \\implies 3(t^2 - 4t + 3) = 0 \\implies 3(t - 1)(t - 3) = 0 \\implies t = 1 \\text{ s} \\) and \\( t = 3 \\text{ s} \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.9: Kinematics"
    },
    {
        "id": "ib-math-s1-029",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Definite Integral & Area)",
        "difficulty": "Medium",
        "question": "What is the exact value of the definite integral \\( \\int_1^4 \\left(2x - \\frac{1}{\\sqrt{x}}\\right) dx \\)?",
        "options": [
            "13",
            "15",
            "11",
            "17"
        ],
        "answer": 0,
        "explanation": "Rewrite integrand as \\( 2x - x^{-1/2} \\). Antiderivative: \\( \\left[ x^2 - \\frac{x^{1/2}}{1/2} \\right]_1^4 = \\left[ x^2 - 2\\sqrt{x} \\right]_1^4 \\). At \\( x = 4 \\): \\( 4^2 - 2\\sqrt{4} = 16 - 4 = 12 \\). At \\( x = 1 \\): \\( 1^2 - 2\\sqrt{1} = 1 - 2 = -1 \\). Value = \\( 12 - (-1) = 13 \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.10: Definite Integrals and Area"
    },
    {
        "id": "ib-math-s1-030",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Integration by Substitution)",
        "difficulty": "Hard",
        "question": "What is the indefinite integral \\( \\int 2x \\cos(x^2) dx \\)?",
        "options": [
            "\\( \\sin(x^2) + C \\)",
            "\\( -\\sin(x^2) + C \\)",
            "\\( 2\\sin(x^2) + C \\)",
            "\\( \\frac{1}{2}\\cos(x^2) + C \\)"
        ],
        "answer": 0,
        "explanation": "Let \\( u = x^2 \\implies du = 2x dx \\). Substituting: \\( \\int \\cos(u) du = \\sin(u) + C = \\sin(x^2) + C \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.11: Integration by Substitution"
    }
]

# ----------------------------------------------------------------------------------
# 4. IB DP MATHEMATICS: ANALYSIS & APPROACHES (AA HL/SL) — SET 2 (30 Questions)
# -------------------------------------------------------------
math_set2_questions = [
    {
        "id": "ib-math-s2-001",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Geometric Sequence Terms)",
        "difficulty": "Easy",
        "question": "A geometric sequence has first term \\( u_1 = 3 \\) and common ratio \\( r = -2 \\). What is the 7th term, \\( u_7 \\)?",
        "options": [
            "192",
            "-192",
            "96",
            "-384"
        ],
        "answer": 0,
        "explanation": "\\( u_n = u_1 r^{n-1} \\implies u_7 = 3(-2)^{6} = 3(64) = 192 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.3: Geometric Sequences"
    },
    {
        "id": "ib-math-s2-002",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Logarithmic Change of Base)",
        "difficulty": "Medium",
        "question": "If \\( \\log_2(a) = p \\), what is \\( \\log_8(a) \\) in terms of \\( p \\)?",
        "options": [
            "\\( \\frac{p}{3} \\)",
            "\\( 3p \\)",
            "\\( p - 3 \\)",
            "\\( p^3 \\)"
        ],
        "answer": 0,
        "explanation": "Use change of base rule: \\( \\log_8(a) = \\frac{\\log_2(a)}{\\log_2(8)} \\). Since \\( \\log_2(8) = 3 \\) and \\( \\log_2(a) = p \\), \\( \\log_8(a) = \\frac{p}{3} \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.5: Laws of Logarithms"
    },
    {
        "id": "ib-math-s2-003",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Binomial Constant Term)",
        "difficulty": "Hard",
        "question": "What is the term independent of \\( x \\) (constant term) in the expansion of \\( \\left(x^2 + \\frac{2}{x}\\right)^6 \\)?",
        "options": [
            "240",
            "160",
            "60",
            "15"
        ],
        "answer": 0,
        "explanation": "General term: \\( T_{r+1} = \\binom{6}{r} (x^2)^{6-r} \\left(\\frac{2}{x}\\right)^r = \\binom{6}{r} 2^r x^{12 - 2r - r} = \\binom{6}{r} 2^r x^{12 - 3r} \\). For the constant term: \\( 12 - 3r = 0 \\implies r = 4 \\). Term = \\( \\binom{6}{4} 2^4 = 15 \\times 16 = 240 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.9: Binomial Theorem"
    },
    {
        "id": "ib-math-s2-004",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Roots of Polynomials & Vieta)",
        "difficulty": "Medium",
        "question": "The roots of the cubic polynomial \\( 2x^3 - 6x^2 + 8x - 10 = 0 \\) are \\( \\alpha, \\beta, \\gamma \\). What is the value of \\( \\alpha + \\beta + \\gamma \\)?",
        "options": [
            "3",
            "-3",
            "4",
            "5"
        ],
        "answer": 0,
        "explanation": "By Vieta's formulas, for \\( ax^3 + bx^2 + cx + d = 0 \\), the sum of roots is \\( \\alpha + \\beta + \\gamma = -\\frac{b}{a} = -\\frac{-6}{2} = \\frac{6}{2} = 3 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.11: Polynomials (HL)"
    },
    {
        "id": "ib-math-s2-005",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (Complex Number Conjugate)",
        "difficulty": "Easy",
        "question": "If \\( z = 3 - 4i \\), what is the value of \\( z \\bar{z} \\) (the product of \\( z \\) and its complex conjugate)?",
        "options": [
            "25",
            "-7",
            "7",
            "5"
        ],
        "answer": 0,
        "explanation": "\\( \\bar{z} = 3 + 4i \\). \\( z \\bar{z} = (3 - 4i)(3 + 4i) = 3^2 - (4i)^2 = 9 - (-16) = 9 + 16 = 25 = |z|^2 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.12: Complex Numbers"
    },
    {
        "id": "ib-math-s2-006",
        "type": "mcq",
        "subtopic": "Topic 1: Number & Algebra (System of Linear Equations)",
        "difficulty": "Hard",
        "question": "For what value of \\( m \\) does the system of equations \\( x + 2y = 4 \\) and \\( 2x + my = 8 \\) have infinitely many solutions?",
        "options": [
            "\\( m = 4 \\)",
            "\\( m = 2 \\)",
            "\\( m = -4 \\)",
            "\\( m = 0 \\)"
        ],
        "answer": 0,
        "explanation": "Infinitely many solutions occur when the equations are linearly dependent (same line). Multiplying the first equation by 2 gives \\( 2x + 4y = 8 \\). Comparing with \\( 2x + my = 8 \\) yields \\( m = 4 \\).",
        "citation": "IB Mathematics AA Guide — Topic 1.16: Systems of Linear Equations (HL)"
    },
    {
        "id": "ib-math-s2-007",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Domain of Radical Functions)",
        "difficulty": "Medium",
        "question": "What is the natural real domain of the function \\( f(x) = \\sqrt{\\frac{x - 2}{x + 5}} \\)?",
        "options": [
            "\\( x < -5 \\text{ or } x \\ge 2 \\)",
            "\\( -5 < x \\le 2 \\)",
            "\\( x \\ge 2 \\)",
            "\\( x \\ne -5 \\)"
        ],
        "answer": 0,
        "explanation": "We require \\( \\frac{x - 2}{x + 5} \\ge 0 \\) and \\( x + 5 \\ne 0 \\). Using a sign diagram with critical points at \\( x = -5 \\) and \\( x = 2 \\): when \\( x > 2 \\), \\( (+)/(+) > 0 \\); when \\( -5 < x < 2 \\), \\( (-)/(+) < 0 \\); when \\( x < -5 \\), \\( (-)/(-) > 0 \\). Hence, domain is \\( (-\\infty, -5) \\cup [2, \\infty) \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.1: Domain and Range"
    },
    {
        "id": "ib-math-s2-008",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Vertex Form of Parabola)",
        "difficulty": "Easy",
        "question": "What are the coordinates of the vertex of the parabola \\( y = 2x^2 - 12x + 11 \\)?",
        "options": [
            "\\( (3, -7) \\)",
            "\\( (-3, 7) \\)",
            "\\( (3, 11) \\)",
            "\\( (6, -7) \\)"
        ],
        "answer": 0,
        "explanation": "Vertex x-coordinate: \\( x = -\\frac{b}{2a} = -\\frac{-12}{2(2)} = \\frac{12}{4} = 3 \\). Substitute \\( x = 3 \\): \\( y = 2(3)^2 - 12(3) + 11 = 2(9) - 36 + 11 = 18 - 36 + 11 = -7 \\). Vertex is \\( (3, -7) \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.6: Quadratic Functions"
    },
    {
        "id": "ib-math-s2-009",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Horizontal Asymptote of Exponential)",
        "difficulty": "Easy",
        "question": "What is the horizontal asymptote of the exponential function \\( f(x) = 3 - 2e^{-x} \\) as \\( x \\to \\infty \\)?",
        "options": [
            "\\( y = 3 \\)",
            "\\( y = -2 \\)",
            "\\( y = 0 \\)",
            "\\( y = 1 \\)"
        ],
        "answer": 0,
        "explanation": "As \\( x \\to \\infty \\), \\( e^{-x} \\to 0 \\). Therefore, \\( f(x) \\to 3 - 2(0) = 3 \\). The horizontal asymptote is \\( y = 3 \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.4: Exponential and Logarithmic Functions"
    },
    {
        "id": "ib-math-s2-010",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Self-Inverse Functions)",
        "difficulty": "Medium",
        "question": "Which of the following functions is a self-inverse function (satisfies \\( f(f(x)) = x \\))?",
        "options": [
            "\\( f(x) = \\frac{1}{x} \\), \\( x \\ne 0 \\)",
            "\\( f(x) = 2x \\)",
            "\\( f(x) = x^2 \\), \\( x \\ge 0 \\)",
            "\\( f(x) = e^x \\)"
        ],
        "answer": 0,
        "explanation": "\\( f(f(x)) = f\\left(\\frac{1}{x}\\right) = \\frac{1}{1/x} = x \\). Therefore \\( f(x) = \\frac{1}{x} \\) is its own inverse.",
        "citation": "IB Mathematics AA Guide — Topic 2.2: Composite and Inverse Functions"
    },
    {
        "id": "ib-math-s2-011",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Oblique Asymptotes)",
        "difficulty": "Hard",
        "question": "What is the equation of the oblique (slant) asymptote of the rational function \\( f(x) = \\frac{2x^2 + 3x - 1}{x - 1} \\)?",
        "options": [
            "\\( y = 2x + 5 \\)",
            "\\( y = 2x + 3 \\)",
            "\\( y = 2x - 1 \\)",
            "\\( y = x + 5 \\)"
        ],
        "answer": 0,
        "explanation": "Perform polynomial long division: \\( (2x^2 + 3x - 1) \\div (x - 1) = 2x + 5 + \\frac{4}{x - 1} \\). As \\( x \\to \\pm\\infty \\), \\( \\frac{4}{x - 1} \\to 0 \\), leaving the oblique asymptote \\( y = 2x + 5 \\).",
        "citation": "IB Mathematics AA Guide — Topic 2.14: Rational Functions & Slant Asymptotes (HL)"
    },
    {
        "id": "ib-math-s2-012",
        "type": "mcq",
        "subtopic": "Topic 2: Functions (Function Invertibility & Bijectivity)",
        "difficulty": "Medium",
        "question": "Why does the function \\( f(x) = x^2 - 4x + 7 \\) defined on \\( \\mathbb{R} \\) not possess an inverse function \\( f^{-1}(x) \\)?",
        "options": [
            "It is not one-to-one (fails the horizontal line test across \\( \\mathbb{R} \\))",
            "It is not continuous across the real line",
            "The range is strictly limited to non-negative integers",
            "Its derivative is identically zero everywhere"
        ],
        "answer": 0,
        "explanation": "A function has an inverse if and only if it is bijective (both one-to-one and onto). A parabola opens upwards with vertex at \\( x = 2 \\), so horizontal lines for \\( y > 3 \\) intersect the curve twice, violating the one-to-one requirement.",
        "citation": "IB Mathematics AA Guide — Topic 2.2: Inverse Functions"
    },
    {
        "id": "ib-math-s2-013",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Area of Triangle with Sine)",
        "difficulty": "Easy",
        "question": "In triangle \\( ABC \\), side \\( a = 8 \\text{ cm} \\), side \\( b = 10 \\text{ cm} \\), and angle \\( C = 30^\\circ \\). What is the exact area of the triangle?",
        "options": [
            "\\( 20 \\text{ cm}^2 \\)",
            "\\( 40 \\text{ cm}^2 \\)",
            "\\( 20\\sqrt{3} \\text{ cm}^2 \\)",
            "\\( 10 \\text{ cm}^2 \\)"
        ],
        "answer": 0,
        "explanation": "Area \\( = \\frac{1}{2} ab \\sin C = \\frac{1}{2}(8)(10)\\sin(30^\\circ) = 40 \\times \\frac{1}{2} = 20 \\text{ cm}^2 \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.2: Sine and Cosine Rules"
    },
    {
        "id": "ib-math-s2-014",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Cosine Rule)",
        "difficulty": "Medium",
        "question": "In triangle \\( ABC \\), \\( a = 5 \\), \\( b = 7 \\), and \\( c = 8 \\). What is the exact value of \\( \\cos B \\)?",
        "options": [
            "\\( \\frac{1}{2} \\)",
            "\\( \\frac{1}{4} \\)",
            "\\( \\frac{\\sqrt{3}}{2} \\)",
            "\\( \\frac{3}{5} \\)"
        ],
        "answer": 0,
        "explanation": "By the cosine rule: \\( \\cos B = \\frac{a^2 + c^2 - b^2}{2ac} = \\frac{5^2 + 8^2 - 7^2}{2(5)(8)} = \\frac{25 + 64 - 49}{80} = \\frac{40}{80} = \\frac{1}{2} \\). (Thus \\( B = 60^\\circ \\)).",
        "citation": "IB Mathematics AA Guide — Topic 3.2: Cosine Rule"
    },
    {
        "id": "ib-math-s2-015",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Trigonometric Double Angle Identity)",
        "difficulty": "Medium",
        "question": "What is the simplified form of the identity \\( \\frac{\\sin(2x)}{1 + \\cos(2x)} \\)?",
        "options": [
            "\\( \\tan x \\)",
            "\\( \\cot x \\)",
            "\\( \\sin x \\)",
            "\\( 2\\tan x \\)"
        ],
        "answer": 0,
        "explanation": "Substitute \\( \\sin(2x) = 2\\sin x \\cos x \\) and \\( \\cos(2x) = 2\\cos^2 x - 1 \\): \\( \\frac{2\\sin x \\cos x}{1 + (2\\cos^2 x - 1)} = \\frac{2\\sin x \\cos x}{2\\cos^2 x} = \\frac{\\sin x}{\\cos x} = \\tan x \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.6: Double Angle Identities"
    },
    {
        "id": "ib-math-s2-016",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Vector Magnitude & Unit Vector)",
        "difficulty": "Easy",
        "question": "What is the unit vector in the direction of \\( \\mathbf{v} = \\begin{pmatrix} 3 \\\\ -4 \\end{pmatrix} \\)?",
        "options": [
            "\\( \\begin{pmatrix} 3/5 \\\\ -4/5 \\end{pmatrix} \\)",
            "\\( \\begin{pmatrix} 3/7 \\\\ -4/7 \\end{pmatrix} \\)",
            "\\( \\begin{pmatrix} 1/5 \\\\ -1/5 \\end{pmatrix} \\)",
            "\\( \\begin{pmatrix} 4/5 \\\\ -3/5 \\end{pmatrix} \\)"
        ],
        "answer": 0,
        "explanation": "Magnitude \\( |\\mathbf{v}| = \\sqrt{3^2 + (-4)^2} = \\sqrt{9 + 16} = 5 \\). The unit vector is \\( \\frac{\\mathbf{v}}{|\\mathbf{v}|} = \\begin{pmatrix} 3/5 \\\\ -4/5 \\end{pmatrix} \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.12: Vectors"
    },
    {
        "id": "ib-math-s2-017",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Vector Cross Product)",
        "difficulty": "Hard",
        "question": "What is the vector cross product \\( \\mathbf{u} \\times \\mathbf{v} \\) of \\( \\mathbf{u} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix} \\) and \\( \\mathbf{v} = \\begin{pmatrix} 0 \\\\ 3 \\\\ 1 \\end{pmatrix} \\)?",
        "options": [
            "\\( \\begin{pmatrix} -6 \\\\ -1 \\\\ 3 \\end{pmatrix} \\)",
            "\\( \\begin{pmatrix} 6 \\\\ 1 \\\\ -3 \\end{pmatrix} \\)",
            "\\( \\begin{pmatrix} -6 \\\\ 1 \\\\ 3 \\end{pmatrix} \\)",
            "\\( \\begin{pmatrix} 0 \\\\ 0 \\\\ 3 \\end{pmatrix} \\)"
        ],
        "answer": 0,
        "explanation": "\\( \\mathbf{u} \\times \\mathbf{v} = \\det \\begin{pmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ 1 & 0 & 2 \\\\ 0 & 3 & 1 \\end{pmatrix} = \\mathbf{i}(0 - 6) - \\mathbf{j}(1 - 0) + \\mathbf{k}(3 - 0) = -6\\mathbf{i} - 1\\mathbf{j} + 3\\mathbf{k} = \\begin{pmatrix} -6 \\\\ -1 \\\\ 3 \\end{pmatrix} \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.15: Vector Cross Product (HL)"
    },
    {
        "id": "ib-math-s2-018",
        "type": "mcq",
        "subtopic": "Topic 3: Geometry & Trigonometry (Angle Between Lines)",
        "difficulty": "Medium",
        "question": "Two lines have direction vectors \\( \\mathbf{d}_1 = \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix} \\) and \\( \\mathbf{d}_2 = \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix} \\). What is the acute angle \\( \\theta \\) between the two lines?",
        "options": [
            "\\( 60^\\circ \\) (\\( \\frac{\\pi}{3} \\text{ rad} \\))",
            "\\( 45^\\circ \\) (\\( \\frac{\\pi}{4} \\text{ rad} \\))",
            "\\( 30^\\circ \\) (\\( \\frac{\\pi}{6} \\text{ rad} \\))",
            "\\( 90^\\circ \\) (\\( \\frac{\\pi}{2} \\text{ rad} \\))"
        ],
        "answer": 0,
        "explanation": "\\( \\cos\\theta = \\frac{|\\mathbf{d}_1 \\cdot \\mathbf{d}_2|}{|\\mathbf{d}_1||\\mathbf{d}_2|} \\). Dot product \\( = (1)(0) + (1)(1) + (0)(1) = 1 \\). Magnitudes \\( |\\mathbf{d}_1| = \\sqrt{1^2 + 1^2} = \\sqrt{2} \\) and \\( |\\mathbf{d}_2| = \\sqrt{1^2 + 1^2} = \\sqrt{2} \\). \\( \\cos\\theta = \\frac{1}{\\sqrt{2} \\times \\sqrt{2}} = \\frac{1}{2} \\implies \\theta = 60^\\circ \\).",
        "citation": "IB Mathematics AA Guide — Topic 3.14: Angles Between Lines"
    },
    {
        "id": "ib-math-s2-019",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Complementary Events)",
        "difficulty": "Easy",
        "question": "If the probability that it rains on any given day in April is 0.35, what is the probability that it does NOT rain on that day?",
        "options": [
            "0.65",
            "0.35",
            "0.70",
            "0.00"
        ],
        "answer": 0,
        "explanation": "\\( P(A') = 1 - P(A) = 1 - 0.35 = 0.65 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.5: Probability of Complementary Events"
    },
    {
        "id": "ib-math-s2-020",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Variance of Discrete Variable)",
        "difficulty": "Medium",
        "question": "A discrete random variable has \\( E(X) = 4 \\) and \\( E(X^2) = 25 \\). What is the standard deviation \\( \\sigma \\) of \\( X \\)?",
        "options": [
            "3",
            "9",
            "\\( \\sqrt{41} \\)",
            "5"
        ],
        "answer": 0,
        "explanation": "\\( \\text{Var}(X) = E(X^2) - [E(X)]^2 = 25 - 4^2 = 25 - 16 = 9 \\). The standard deviation is \\( \\sigma = \\sqrt{\\text{Var}(X)} = \\sqrt{9} = 3 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.7: Discrete Random Variables"
    },
    {
        "id": "ib-math-s2-021",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Binomial Mean & Variance)",
        "difficulty": "Easy",
        "question": "If \\( X \\sim B(100, 0.2) \\), what are the mean \\( E(X) \\) and variance \\( \\text{Var}(X) \\)?",
        "options": [
            "\\( E(X) = 20 \\), \\( \\text{Var}(X) = 16 \\)",
            "\\( E(X) = 20 \\), \\( \\text{Var}(X) = 4 \\)",
            "\\( E(X) = 10 \\), \\( \\text{Var}(X) = 8 \\)",
            "\\( E(X) = 20 \\), \\( \\text{Var}(X) = 20 \\)"
        ],
        "answer": 0,
        "explanation": "For a binomial distribution: \\( E(X) = np = 100(0.2) = 20 \\). Variance \\( \\text{Var}(X) = np(1 - p) = 100(0.2)(0.8) = 16 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.8: Binomial Distribution"
    },
    {
        "id": "ib-math-s2-022",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Normal Symmetry)",
        "difficulty": "Medium",
        "question": "For a standard normal distribution \\( Z \\sim N(0, 1) \\), if \\( P(Z < 1.25) = 0.8944 \\), what is \\( P(-1.25 < Z < 1.25) \\)?",
        "options": [
            "0.7888",
            "0.8944",
            "0.1056",
            "0.2112"
        ],
        "answer": 0,
        "explanation": "By symmetry, \\( P(Z < -1.25) = 1 - P(Z < 1.25) = 1 - 0.8944 = 0.1056 \\). Therefore, \\( P(-1.25 < Z < 1.25) = P(Z < 1.25) - P(Z < -1.25) = 0.8944 - 0.1056 = 0.7888 \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.9: Normal Distribution"
    },
    {
        "id": "ib-math-s2-023",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Bayes' Theorem)",
        "difficulty": "Hard",
        "question": "A rare disease affects 1% of a population. A diagnostic test is 95% accurate (sensitivity = 0.95, specificity = 0.95). If a randomly selected person tests positive, what is the probability they actually have the disease?",
        "options": [
            "\\( \\approx 16.1\\% \\)",
            "\\( 95.0\\% \\)",
            "\\( 50.0\\% \\)",
            "\\( 5.0\\% \\)"
        ],
        "answer": 0,
        "explanation": "By Bayes' theorem: \\( P(D|+) = \\frac{P(+|D)P(D)}{P(+|D)P(D) + P(+|D')P(D')} = \\frac{(0.95)(0.01)}{(0.95)(0.01) + (0.05)(0.99)} = \\frac{0.0095}{0.0095 + 0.0495} = \\frac{0.0095}{0.0590} \\approx 0.161 \\) (16.1%).",
        "citation": "IB Mathematics AA Guide — Topic 4.13: Bayes' Theorem (HL)"
    },
    {
        "id": "ib-math-s2-024",
        "type": "mcq",
        "subtopic": "Topic 4: Statistics & Probability (Continuous Random Variables & PDF)",
        "difficulty": "Hard",
        "question": "A continuous random variable \\( X \\) has probability density function \\( f(x) = kx^2 \\) for \\( 0 \\le x \\le 3 \\), and \\( f(x) = 0 \\) elsewhere. What is the value of \\( k \\)?",
        "options": [
            "\\( \\frac{1}{9} \\)",
            "\\( \\frac{1}{27} \\)",
            "\\( \\frac{1}{3} \\)",
            "\\( \\frac{2}{9} \\)"
        ],
        "answer": 0,
        "explanation": "Total probability must equal 1: \\( \\int_0^3 k x^2 dx = 1 \\implies k \\left[ \\frac{x^3}{3} \\right]_0^3 = 1 \\implies k \\left(\\frac{27}{3}\\right) = 1 \\implies 9k = 1 \\implies k = \\frac{1}{9} \\).",
        "citation": "IB Mathematics AA Guide — Topic 4.15: Continuous Random Variables (HL)"
    },
    {
        "id": "ib-math-s2-025",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Quotient Rule)",
        "difficulty": "Medium",
        "question": "What is the derivative of \\( f(x) = \\frac{\\ln x}{x} \\) for \\( x > 0 \\)?",
        "options": [
            "\\( \\frac{1 - \\ln x}{x^2} \\)",
            "\\( \\frac{1 + \\ln x}{x^2} \\)",
            "\\( \\frac{1}{x^2} \\)",
            "\\( -\\frac{\\ln x}{x^2} \\)"
        ],
        "answer": 0,
        "explanation": "Quotient rule: \\( \\left(\\frac{u}{v}\\right)' = \\frac{u'v - uv'}{v^2} \\) with \\( u = \\ln x \\implies u' = 1/x \\) and \\( v = x \\implies v' = 1 \\): \\( f'(x) = \\frac{(1/x)(x) - (\\ln x)(1)}{x^2} = \\frac{1 - \\ln x}{x^2} \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.6: Quotient Rule"
    },
    {
        "id": "ib-math-s2-026",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Implicit Differentiation)",
        "difficulty": "Hard",
        "question": "For the curve defined by \\( x^2 + y^2 = 25 \\), what is the gradient \\( \\frac{dy}{dx} \\) at the point \\( (3, 4) \\)?",
        "options": [
            "\\( -\\frac{3}{4} \\)",
            "\\( \\frac{3}{4} \\)",
            "\\( -\\frac{4}{3} \\)",
            "\\( \\frac{4}{3} \\)"
        ],
        "answer": 0,
        "explanation": "Differentiate implicitly with respect to \\( x \\): \\( 2x + 2y \\frac{dy}{dx} = 0 \\implies 2y \\frac{dy}{dx} = -2x \\implies \\frac{dy}{dx} = -\\frac{x}{y} \\). At \\( (3, 4) \\), \\( \\frac{dy}{dx} = -\\frac{3}{4} \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.12: Implicit Differentiation (HL)"
    },
    {
        "id": "ib-math-s2-027",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Points of Inflexion)",
        "difficulty": "Medium",
        "question": "Where does the curve \\( f(x) = x^3 - 6x^2 + 9x + 2 \\) have a point of inflexion?",
        "options": [
            "\\( (2, 4) \\)",
            "\\( (1, 6) \\)",
            "\\( (3, 2) \\)",
            "\\( (0, 2) \\)"
        ],
        "answer": 0,
        "explanation": "\\( f'(x) = 3x^2 - 12x + 9 \\). \\( f''(x) = 6x - 12 \\). Setting \\( f''(x) = 0 \\implies 6x = 12 \\implies x = 2 \\). Since \\( f''(x) \\) changes sign at \\( x = 2 \\) (negative for \\( x < 2 \\), positive for \\( x > 2 \\)), \\( x = 2 \\) is a point of inflexion. Value \\( f(2) = 2^3 - 6(2^2) + 9(2) + 2 = 8 - 24 + 18 + 2 = 4 \\). Point is \\( (2, 4) \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.8: Points of Inflexion"
    },
    {
        "id": "ib-math-s2-028",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Total Distance vs Displacement)",
        "difficulty": "Hard",
        "question": "A particle moves with velocity \\( v(t) = 2t - 4 \\text{ m/s} \\). What is the total distance traveled by the particle between \\( t = 0 \\) and \\( t = 3 \\)?",
        "options": [
            "5 m",
            "3 m",
            "-3 m",
            "9 m"
        ],
        "answer": 0,
        "explanation": "Velocity changes sign at \\( 2t - 4 = 0 \\implies t = 2 \\). Total distance = \\( \\int_0^3 |v(t)| dt = \\int_0^2 -(2t - 4) dt + \\int_2^3 (2t - 4) dt \\). First segment: \\( [-t^2 + 4t]_0^2 = -4 + 8 = 4 \\text{ m} \\). Second segment: \\( [t^2 - 4t]_2^3 = (9 - 12) - (4 - 8) = -3 - (-4) = 1 \\text{ m} \\). Total distance = \\( 4 + 1 = 5 \\text{ m} \\). (Displacement is \\( -3 \\text{ m} \\)).",
        "citation": "IB Mathematics AA Guide — Topic 5.9: Kinematics (Total Distance)"
    },
    {
        "id": "ib-math-s2-029",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Area Between Curves)",
        "difficulty": "Medium",
        "question": "What is the area enclosed between the parabola \\( y = x^2 \\) and the line \\( y = 2x \\)?",
        "options": [
            "\\( \\frac{4}{3} \\)",
            "\\( \\frac{2}{3} \\)",
            "\\( 2 \\)",
            "\\( \\frac{8}{3} \\)"
        ],
        "answer": 0,
        "explanation": "Intersection points: \\( x^2 = 2x \\implies x(x - 2) = 0 \\implies x = 0 \\) and \\( x = 2 \\). On \\( [0, 2] \\), \\( 2x \\ge x^2 \\). Area \\( = \\int_0^2 (2x - x^2) dx = \\left[ x^2 - \\frac{x^3}{3} \\right]_0^2 = 4 - \\frac{8}{3} = \\frac{12 - 8}{3} = \\frac{4}{3} \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.10: Area Between Curves"
    },
    {
        "id": "ib-math-s2-030",
        "type": "mcq",
        "subtopic": "Topic 5: Calculus (Integration by Parts)",
        "difficulty": "Hard",
        "question": "Using integration by parts, what is \\( \\int x \\cos x dx \\)?",
        "options": [
            "\\( x \\sin x + \\cos x + C \\)",
            "\\( x \\sin x - \\cos x + C \\)",
            "\\( -x \\sin x + \\cos x + C \\)",
            "\\( x \\cos x - \\sin x + C \\)"
        ],
        "answer": 0,
        "explanation": "Integration by parts formula: \\( \\int u v' dx = uv - \\int u' v dx \\). Choose \\( u = x \\implies u' = 1 \\), and \\( v' = \\cos x \\implies v = \\sin x \\). Then: \\( \\int x \\cos x dx = x \\sin x - \\int (1)(\\sin x) dx = x \\sin x - (-\\cos x) + C = x \\sin x + \\cos x + C \\).",
        "citation": "IB Mathematics AA Guide — Topic 5.13: Integration by Parts (HL)"
    }
]

def save_json(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({"questions": data}, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved {len(data)} questions to {filepath}")

def main():
    save_json("ib_biology_hl_sl_set1.json", bio_set1_questions)
    save_json("ib_biology_hl_sl_set2.json", bio_set2_questions)
    save_json("ib_math_aa_hl_sl_set1.json", math_set1_questions)
    save_json("ib_math_aa_hl_sl_set2.json", math_set2_questions)
    print("🎉 All 140 IB DP examination questions generated successfully!")

if __name__ == "__main__":
    main()
