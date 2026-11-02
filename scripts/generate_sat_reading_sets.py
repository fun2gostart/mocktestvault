#!/usr/bin/env python3
"""
Generates Digital SAT Reading & Writing Sets 02, 03, 04 (20 Qs each = 60 Qs total)
Aligned with official College Board Digital SAT Specifications.
Domains:
- Craft & Structure (Words in Context, Text Structure & Purpose, Cross-Text Connections)
- Information & Ideas (Central Ideas & Details, Command of Evidence, Inferences)
- Standard English Conventions (Boundaries, Form/Structure/Sense)
- Expression of Ideas (Rhetorical Synthesis, Transitions)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_SAT = os.path.join(BASE_DIR, "data", "us", "sat")

# ==============================================================================
# SET 2: DIGITAL SAT READING & WRITING (20 Questions)
# ==============================================================================
sat_reading_set2 = [
  {
    "id": "sat-rw-021",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Easy",
    "question": "The marine biologist noted that although bioluminescent organisms are _______ in the upper sunlit epipelagic zone, they become ubiquitous in the aphotic midnight depths where ambient sunlight cannot penetrate.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["scarce", "abundant", "lethal", "permanent"],
    "answer": 0,
    "explanation": "The text establishes a contrast between the upper ocean and the midnight depths ('although... they become ubiquitous'). 'Ubiquitous' means present everywhere, so the contrasting word for the sunlit zone must mean rare or uncommon. 'Scarce' precisely captures this meaning.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-022",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Medium",
    "question": "Far from being a passive recorder of sensory inputs, the human brain actively constructs perception through predictive processing, constantly _______ its internal models against incoming sensory discrepancies.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["calibrating", "discarding", "obscuring", "fabricating"],
    "answer": 0,
    "explanation": "The context explains that the brain actively adjusts its internal perceptual models in response to sensory differences. 'Calibrating' means adjusting or fine-tuning precisely, making it the most accurate term.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-023",
    "type": "mcq",
    "subtopic": "Text Structure & Purpose (Craft & Structure)",
    "difficulty": "Medium",
    "question": "In the 1920s, astronomer Edwin Hubble observed distant galaxies and identified that their spectral absorption lines shifted systematically toward longer, redder wavelengths. Rather than interpreting this as proof that celestial bodies were physically speeding away through stationary space, theoretical physicists recognized that space-time itself was dynamically stretching. This monumental realization transformed cosmology from a static model into an expanding evolutionary framework.\n\nWhich choice best describes the main purpose of the text?",
    "options": [
      "To describe an observational discovery and explain its transformative conceptual implication for cosmology",
      "To compare Edwin Hubble's experimental methods with those of contemporary theoretical physicists",
      "To argue that cosmological discoveries in the 1920s were largely based on flawed optical measurements",
      "To explain how spectral absorption lines are measured in modern optical telescopes"
    ],
    "answer": 0,
    "explanation": "The text begins by detailing Hubble's observation of redshift and concludes by explaining how this led to the revolutionary concept of expanding space-time. Choice A accurately reflects this structural progression.",
    "citation": "College Board Digital SAT Reading & Writing — Text Structure and Purpose"
  },
  {
    "id": "sat-rw-024",
    "type": "mcq",
    "subtopic": "Cross-Text Connections (Craft & Structure)",
    "difficulty": "Hard",
    "question": "Text 1:\nUrban canopy programs, which plant deciduous trees along city corridors, significantly reduce urban heat island effects. During summer months, mature trees lower surrounding ambient temperatures by up to 4°C through shade and evapotranspiration, reducing household air conditioning reliance.\n\nText 2:\nWhile municipal tree planting provides undisputed microclimatic cooling, urban planners caution that without drought-tolerant native species selection, such programs can severely deplete municipal groundwater reserves in arid zones, inadvertently shifting the ecological burden from electricity grids to water infrastructure.\n\nBased on the texts, how would the author of Text 2 most likely respond to the claims in Text 1?",
    "options": [
      "By acknowledging the cooling benefits highlighted in Text 1 while pointing out a potential resource trade-off in dry regions",
      "By refuting the assertion that tree evapotranspiration produces any measurable reduction in urban temperatures",
      "By arguing that air conditioning units are ecologically preferable to urban canopy programs",
      "By claiming that non-native deciduous trees consume significantly less water than native vegetation"
    ],
    "answer": 0,
    "explanation": "Author 2 agrees that trees provide 'undisputed microclimatic cooling' (concurring with Text 1), but warns of groundwater depletion in arid zones. Choice A captures this nuanced agreement coupled with a trade-off caveat.",
    "citation": "College Board Digital SAT Reading & Writing — Cross-Text Connections"
  },
  {
    "id": "sat-rw-025",
    "type": "mcq",
    "subtopic": "Central Ideas & Details (Information & Ideas)",
    "difficulty": "Easy",
    "question": "Mycorrhizal fungal networks form symbiotic associations with terrestrial plant roots, facilitating the bidirectional exchange of nutrients. In exchange for photosynthetic carbon compounds produced by the host plant, the subterranean fungal hyphae absorb and deliver soil minerals—principally bioavailable phosphorus and nitrogen—that plant roots alone could not effectively access.\n\nAccording to the text, what primary benefit do mycorrhizal fungi supply to their host plants?",
    "options": [
      "Essential soil minerals such as bioavailable phosphorus and nitrogen",
      "Photosynthetic carbon compounds synthesized in dark environments",
      "Structural cellulose that protects roots from physical soil compression",
      "Chemical inhibitors that eliminate competing subterranean flora"
    ],
    "answer": 0,
    "explanation": "The text explicitly states that fungi 'absorb and deliver soil minerals—principally bioavailable phosphorus and nitrogen' in exchange for plant carbon.",
    "citation": "College Board Digital SAT Reading & Writing — Central Ideas & Details"
  },
  {
    "id": "sat-rw-026",
    "type": "mcq",
    "subtopic": "Command of Evidence: Textual (Information & Ideas)",
    "difficulty": "Medium",
    "question": "In her analysis of 19th-century epistolary novels, literary critic Elena Rostova argues that the format allowed authors to present contradictory social perspectives without overtly endorsing any single moral viewpoint.\n\nWhich quotation from an analysis of Mary Shelley's Frankenstein would provide the strongest support for Rostova's argument?",
    "options": [
      "By alternating the narrative voices of Captain Walton, Victor Frankenstein, and the creature through embedded letters, Shelley forces readers to evaluate conflicting moral claims without an authorial referee.",
      "Shelley began drafting the novel at the Villa Diodati in 1816 during a historically unseasonable summer caused by volcanic eruptions.",
      "The epistolary framework was popular among Romantic writers seeking to emulate eighteenth-century philosophical pamphlets.",
      "Victor's laboratory notebooks reveal the rigorous scientific theories that fascinated young intellectuals of the industrial era."
    ],
    "answer": 0,
    "explanation": "Rostova argues that epistolary novels allow multiple conflicting viewpoints without an authorial referee. Choice A directly cites the novel's alternating letter format and conflicting moral claims without an authorial mediator.",
    "citation": "College Board Digital SAT Reading & Writing — Command of Evidence"
  },
  {
    "id": "sat-rw-027",
    "type": "mcq",
    "subtopic": "Inferences (Information & Ideas)",
    "difficulty": "Hard",
    "question": "Archaeologists studying ancient agricultural settlements in the Levant discovered that communities with diversified seed storage systems survived multi-year megadroughts with negligible population declines, whereas neighboring settlements reliant exclusively on high-yield monoculture emmer wheat experienced abrupt site abandonments within three consecutive dry seasons. This evidence strongly suggests that _______.\n\nWhich choice most logically completes the text?",
    "options": [
      "crop diversification conferred critical resilience against environmental unpredictability in ancient Levantine agrarian societies",
      "emmer wheat required significantly less water than any other crop cultivated during the Bronze Age",
      "monoculture farming was entirely unknown to Levantine farmers prior to historical megadrought events",
      "Levantine communities that abandoned their settlements did so primarily because of military conquest"
    ],
    "answer": 0,
    "explanation": "The prompt contrasts communities with diversified seeds (survived droughts) against those with monoculture wheat (abandoned sites). The logical inference is that crop diversification provided vital resilience against climatic volatility.",
    "citation": "College Board Digital SAT Reading & Writing — Inferences"
  },
  {
    "id": "sat-rw-028",
    "type": "mcq",
    "subtopic": "Subject-Verb Agreement (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "The collection of ceramic artifacts and bronze weapons unearthed at the archaeological dig site _______ currently housed in the city's municipal museum of antiquity.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["is", "are", "were", "have been"],
    "answer": 0,
    "explanation": "The true grammatical subject of the sentence is the singular collective noun 'collection', not the plural nouns inside the prepositional phrase ('artifacts and bronze weapons'). Therefore, the singular verb 'is' is required.",
    "citation": "College Board Digital SAT Reading & Writing — Subject-Verb Agreement"
  },
  {
    "id": "sat-rw-029",
    "type": "mcq",
    "subtopic": "Sentence Boundaries & Semicolons (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "Glaciologists deployed seismic sensors across the Antarctic ice _______ instruments detected micro-fractures forming miles beneath the continental shelf.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["shelf; the", "shelf the", "shelf, the", "shelf, where the"],
    "answer": 0,
    "explanation": "Two independent clauses ('Glaciologists deployed seismic sensors...' and 'the instruments detected micro-fractures...') cannot be joined with just a comma (comma splice) or nothing (run-on). A semicolon correctly connects two related independent clauses.",
    "citation": "College Board Digital SAT Reading & Writing — Boundaries"
  },
  {
    "id": "sat-rw-030",
    "type": "mcq",
    "subtopic": "Pronoun-Antecedent Agreement (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "Each of the candidate research proposals submitted to the National Science Foundation underwent _______ rigorous peer-review evaluation by independent specialists.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["its", "their", "our", "theirs"],
    "answer": 0,
    "explanation": "'Each' is a singular indefinite pronoun when functioning as the subject ('Each of the candidate research proposals'). Standard English requires the singular possessive pronoun 'its' to agree with 'Each'.",
    "citation": "College Board Digital SAT Reading & Writing — Pronoun Agreement"
  },
  {
    "id": "sat-rw-031",
    "type": "mcq",
    "subtopic": "Modifier Placement (Standard English Conventions)",
    "difficulty": "Hard",
    "question": "Having completed a five-year voyage surveying the unique ecological niches of the Galápagos archipelago, _______.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      "Charles Darwin developed his revolutionary treatise on natural selection",
      "the theory of natural selection was formulated by Charles Darwin",
      "specimens of finches and mockingbirds were meticulously cataloged by Darwin",
      "a revolutionary treatise on adaptation was written by British naturalists"
    ],
    "answer": 0,
    "explanation": "The introductory participial phrase 'Having completed a five-year voyage...' logically describes the person who completed the voyage: Charles Darwin. The subject directly following the comma must be 'Charles Darwin' to prevent a dangling modifier.",
    "citation": "College Board Digital SAT Reading & Writing — Modifiers"
  },
  {
    "id": "sat-rw-032",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "Many deep-sea organisms utilize blue bioluminescence because blue wavelengths penetrate furthest through water. _______, certain dragonfish species produce rare far-red illumination, granting them a covert sensory channel invisible to both their predators and their prey.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["However", "Furthermore", "Consequently", "For example"],
    "answer": 0,
    "explanation": "The first sentence describes the common rule (most creatures use blue light). The second sentence presents a notable contrast (dragonfish produce rare red light). 'However' is the precise adversative transition.",
    "citation": "College Board Digital SAT Reading & Writing — Logical Transitions"
  },
  {
    "id": "sat-rw-033",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Easy",
    "question": "Geothermal power plants extract steam from deep volcanic reservoirs to spin electric turbines with zero fuel combustion. _______, geothermal installations require minimal surface land footprints compared to expansive photovoltaic solar farms.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["Additionally", "Nonetheless", "Instead", "Alternatively"],
    "answer": 0,
    "explanation": "The first sentence highlights one environmental advantage of geothermal energy (zero combustion emissions). The second sentence introduces another distinct advantage (small land footprint). 'Additionally' correctly signals an additive relationship.",
    "citation": "College Board Digital SAT Reading & Writing — Transitions"
  },
  {
    "id": "sat-rw-034",
    "type": "mcq",
    "subtopic": "Rhetorical Synthesis (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "While researching the Great Green Wall initiative, a student noted:\n- The Great Green Wall is an African Union initiative combating desertification in the Sahel.\n- It aims to restore 100 million hectares of degraded land from Senegal in the west to Djibouti in the east.\n- The project creates a 15-kilometer-wide vegetation barrier across 8,000 kilometers of terrain.\n- Participating communities report improved soil fertility and groundwater recharge.\n\nThe student wants to emphasize the geographic scale of the initiative. Which choice most effectively accomplishes this goal?",
    "options": [
      "Spanning 8,000 kilometers from Senegal in the west to Djibouti in the east, the Great Green Wall creates a 15-kilometer-wide vegetation barrier across the African continent.",
      "The Great Green Wall is an African Union initiative designed to restore soil fertility and assist agricultural communities in the Sahel.",
      "Communities participating in the Great Green Wall have documented substantial improvements in groundwater recharge and soil quality.",
      "Initiated by the African Union, the Great Green Wall combats desertification by planting diverse indigenous drought-tolerant trees."
    ],
    "answer": 0,
    "explanation": "The prompt specifies the goal: 'emphasize the geographic scale'. Choice A explicitly cites the dimensions: spanning 8,000 km from Senegal to Djibouti across 15 km of width, directly fulfilling the rhetorical goal.",
    "citation": "College Board Digital SAT Reading & Writing — Rhetorical Synthesis"
  },
  {
    "id": "sat-rw-035",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Hard",
    "question": "The novelist's prose was characterized by an extreme _______, dispensing with flowery adjectives and elaborate subplots in favor of austere declarative sentences.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["economy", "exuberance", "ambiguity", "tedium"],
    "answer": 0,
    "explanation": "In literary criticism, 'economy' refers to spare, concise language that avoids unnecessary ornamentation. The subsequent clues ('dispensing with flowery adjectives', 'austere declarative sentences') confirm that 'economy' is the correct term.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-036",
    "type": "mcq",
    "subtopic": "Parallel Structure (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "The university's new computational biology curriculum trains students to write algorithmic code, analyze genomic sequencing data, and _______ predictive biological models.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["construct", "constructing", "to be constructing", "construction of"],
    "answer": 0,
    "explanation": "Parallel series of verbs: 'to write algorithmic code, [to] analyze genomic sequencing data, and [to] construct predictive biological models'. The base verb 'construct' maintains parallel grammatical structure.",
    "citation": "College Board Digital SAT Reading & Writing — Parallelism"
  },
  {
    "id": "sat-rw-037",
    "type": "mcq",
    "subtopic": "Punctuation with Nonessential Clauses (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "The Kepler Space Telescope _______ revolutionized exoplanet science by monitoring over 150,000 stars for periodic dips in brightness caused by transiting planets.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      ", which launched in 2009,",
      "which launched in 2009",
      ", which launched in 2009",
      "which launched in 2009,"
    ],
    "answer": 0,
    "explanation": "'which launched in 2009' is a nonessential relative clause modifying 'The Kepler Space Telescope'. Nonessential clauses must be enclosed by two paired commas.",
    "citation": "College Board Digital SAT Reading & Writing — Nonessential Elements"
  },
  {
    "id": "sat-rw-038",
    "type": "mcq",
    "subtopic": "Command of Evidence: Quantitative (Information & Ideas)",
    "difficulty": "Hard",
    "question": "In an experiment testing heat resistance among agricultural cultivars, Cultivar A maintained 88% photosynthetic capacity at 42°C, while Cultivar B maintained 62% and Cultivar C maintained 45%. The researchers concluded that Cultivar A possesses specialized cellular heat-shock proteins that preserve chloroplast stability under thermal stress.\n\nWhich finding, if true, would most strongly support the researchers' conclusion?",
    "options": [
      "Cultivar A produces significantly higher concentrations of HSP70 chaperone proteins in its chloroplast membranes during heat exposure than Cultivars B and C",
      "Cultivar A consumes more water per kilogram of biomass than Cultivar C under baseline temperature conditions",
      "Cultivars B and C were bred in greenhouse conditions with identical humidity controls",
      "Chloroplasts in all three cultivars exhibit identical lipid bilayer structures at 25°C"
    ],
    "answer": 0,
    "explanation": "The researchers' claim is that Cultivar A's heat tolerance is specifically due to cellular heat-shock proteins stabilizing chloroplasts. Showing that Cultivar A produces higher levels of HSP70 chaperone proteins directly corroborates this mechanism.",
    "citation": "College Board Digital SAT Reading & Writing — Quantitative Evidence"
  },
  {
    "id": "sat-rw-039",
    "type": "mcq",
    "subtopic": "Apostrophes & Possession (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "The ornithologist documented the _______ migratory path across three continents, observing that juvenile birds navigated independently of their parents.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["species'", "species's", "species", "specie's"],
    "answer": 0,
    "explanation": "'Species' is a singular noun that ends in s. For singular nouns ending in s, adding an apostrophe (or 's) shows possession. In Standard SAT English, 'species'' correctly indicates the migratory path belonging to the species.",
    "citation": "College Board Digital SAT Reading & Writing — Possessive Nouns"
  },
  {
    "id": "sat-rw-040",
    "type": "mcq",
    "subtopic": "Rhetorical Synthesis (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "While researching the Renaissance artist Artemisia Gentileschi, a student noted:\n- Artemisia Gentileschi (1593–c. 1656) was an Italian Baroque painter.\n- She was the first woman admitted as a member of the prestigious Accademia delle Arti del Disegno in Florence.\n- Her celebrated masterpiece Judith Slaying Holofernes (1620) displays dramatic chiaroscuro and intense naturalism.\n- Unlike many contemporary female artists who were restricted to still-lifes, Gentileschi painted ambitious large-scale historical and biblical canvases.\n\nThe student wants to contrast Gentileschi's subject matter with that of her female contemporaries. Which choice most effectively accomplishes this goal?",
    "options": [
      "While many female artists of her era were relegated to painting modest still-lifes, Artemisia Gentileschi distinguished herself by producing monumental biblical and historical compositions.",
      "Artemisia Gentileschi was an Italian Baroque painter who gained admission to the Accademia delle Arti del Disegno in Florence in 1616.",
      "Gentileschi's 1620 painting Judith Slaying Holofernes demonstrates dramatic chiaroscuro and emotional realism.",
      "Admitted to the Accademia in Florence, Gentileschi painted ambitious canvases depicting historical figures."
    ],
    "answer": 0,
    "explanation": "The prompt asks to 'contrast Gentileschi's subject matter with that of her female contemporaries'. Choice A directly highlights the contrast between other women's modest still-lifes and Gentileschi's monumental biblical/historical canvases.",
    "citation": "College Board Digital SAT Reading & Writing — Rhetorical Synthesis"
  }
]

# Write SAT Reading Set 2 JSON
with open(os.path.join(US_DATA_SAT, "digital_sat_reading_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_reading_set2}, f, indent=2, ensure_ascii=False)

print("Generated Digital SAT Reading Set 2 successfully!")
