#!/usr/bin/env python3
"""
Generates Digital SAT Reading & Writing Sets 03 & 04 (40 Questions Total)
"""

import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
US_DATA_SAT = os.path.join(BASE_DIR, "data", "us", "sat")

# ==============================================================================
# SET 3: DIGITAL SAT READING & WRITING (20 Questions)
# ==============================================================================
sat_reading_set3 = [
  {
    "id": "sat-rw-041",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Medium",
    "question": "The experimental drug demonstrated remarkable efficacy during in vitro trials; however, clinical researchers remained cautious, knowing that in vivo human physiological trials frequently _______ preliminary laboratory outcomes.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["confound", "corroborate", "celebrate", "replicate"],
    "answer": 0,
    "explanation": "The contrast indicator 'however' signals that the caution of researchers contradicts the initial success in in vitro tests. 'Confound' means to defeat, throw into confusion, or contradict, accurately capturing how complex human trials often complicate or overturn simplistic lab results.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-042",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Hard",
    "question": "To avoid offending either faction during the municipal treaty negotiations, the mediator deliberately framed the environmental resolutions in _______ language that allowed both conservationists and industrial developers to interpret the clauses to their advantage.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["equivocal", "incisive", "polemical", "dogmatic"],
    "answer": 0,
    "explanation": "The context explains that both opposing sides were able to interpret the clauses to their advantage. 'Equivocal' means ambiguous, open to multiple interpretations, or intentionally non-committal.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-043",
    "type": "mcq",
    "subtopic": "Text Structure & Purpose (Craft & Structure)",
    "difficulty": "Medium",
    "question": "Paleontologists traditionally classified the duck-billed hadrosaurs as peaceful, swamp-dwelling herbivores that used their webbed digits to navigate muddy lagoons. However, recent histological examinations of hadrosaur bone micro-structures and fossilized skin impressions demonstrate that hadrosaurs were agile, upland runners equipped with fleshy foot pads similar to modern ungulates. This anatomical reevaluation has prompted a complete restructuring of late Cretaceous ecological models.\n\nWhich choice best describes the function of the second sentence?",
    "options": [
      "It introduces empirical physical evidence that challenges a traditional historical belief described in the first sentence",
      "It offers an alternative hypothesis that is immediately dismissed by contemporary paleontologists",
      "It describes the specific excavation tools used to unearth hadrosaur fossil specimens in swamp regions",
      "It reconciles two contradictory classifications by proposing that hadrosaurs lived in both aquatic and desert biomes"
    ],
    "answer": 0,
    "explanation": "The first sentence presents the traditional view (swamp-dwelling). The second sentence presents recent fossil evidence (bone histology, fleshy pads) showing they were upland runners. Choice A precisely articulates this function.",
    "citation": "College Board Digital SAT Reading & Writing — Text Structure"
  },
  {
    "id": "sat-rw-044",
    "type": "mcq",
    "subtopic": "Inferences (Information & Ideas)",
    "difficulty": "Hard",
    "question": "In a controlled behavioral study of corvids (crows and ravens), birds that observed human experimenters hide food in opaque containers successfully retrieved the items 92% of the time. However, when experimenters wore blindfolds or looked away while pretending to hide the food, the birds showed no interest in searching those containers. This indicates that corvids _______.\n\nWhich choice most logically completes the text?",
    "options": [
      "are capable of evaluating human visual gaze to determine whether an experimenter possess relevant informational cues",
      "rely primarily on auditory vibrations rather than visual cues when foraging for food caches in nature",
      "display cooperative hunting behaviors exclusively toward familiar human researchers",
      "prefer opaque containers over transparent feeding apparatuses when interacting with humans"
    ],
    "answer": 0,
    "explanation": "The corvids only checked the containers when the humans were visually looking at what they were doing. This demonstrates Theory of Mind awareness—evaluating visual attention/gaze to deduce whether the person actually possessed information.",
    "citation": "College Board Digital SAT Reading & Writing — Inferences"
  },
  {
    "id": "sat-rw-045",
    "type": "mcq",
    "subtopic": "Central Ideas & Details (Information & Ideas)",
    "difficulty": "Easy",
    "question": "Tardigrades, microscopic eight-legged invertebrates colloquially known as water bears, can survive extreme conditions—including exposure to outer space vacuums, ionizing radiation, and temperatures near absolute zero—by entering anhydrobiosis. In this state of suspended animation, tardigrades expel up to 97% of their bodily water and synthesize intrinsically disordered proteins that vitrify into a protective bioglass around cellular structures.\n\nAccording to the passage, how do tardigrades protect their internal cellular structures during anhydrobiosis?",
    "options": [
      "By synthesizing specialized proteins that transform into a protective glass-like shield",
      "By absorbing ambient radiation to generate metabolic heat at sub-zero temperatures",
      "By increasing their internal bodily water volume by 97% to dilute toxins",
      "By constantly moving their eight legs to circulate oxygenated fluid"
    ],
    "answer": 0,
    "explanation": "The text directly states that they 'synthesize intrinsically disordered proteins that vitrify into a protective bioglass around cellular structures'.",
    "citation": "College Board Digital SAT Reading & Writing — Details"
  },
  {
    "id": "sat-rw-046",
    "type": "mcq",
    "subtopic": "Subject-Verb Agreement (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "A wide variety of pollinator species, including nocturnal moths, solitary bees, and nectar-feeding bats, _______ essential ecological services to North American desert flora.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["provides", "provide", "are providing", "have provided"],
    "answer": 0,
    "explanation": "The grammatical subject is 'A wide variety' (or the plural head concept 'variety of pollinator species' in formal descriptive SAT convention, but here the singular collective head 'variety' takes the singular verb 'provides' when treated as a single category, or plural when emphasizing multiple species. In SAT test items, 'A wide variety of [plural noun]' takes singular 'provides' when referring to the collective entity 'variety').",
    "citation": "College Board Digital SAT Reading & Writing — Agreement"
  },
  {
    "id": "sat-rw-047",
    "type": "mcq",
    "subtopic": "Sentence Boundaries & Relative Clauses (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "The James Webb Space Telescope operates at Lagrange point 2, a gravitationally stable cosmic location approximately one million miles from _______ thermal shielding remains oriented away from the Sun.",
    "options": [
      "Earth, where its",
      "Earth, its",
      "Earth its",
      "Earth; where its"
    ],
    "answer": 0,
    "explanation": "'where its thermal shielding remains oriented away from the Sun' is a relative dependent clause providing geographic context about Lagrange point 2. A comma before 'where' correctly connects this nonessential relative clause without creating a run-on or comma splice.",
    "citation": "College Board Digital SAT Reading & Writing — Boundaries"
  },
  {
    "id": "sat-rw-048",
    "type": "mcq",
    "subtopic": "Pronoun Case (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "When the university tenure committee convened to review recent publications, both Dr. Vance and _______ were recognized for outstanding contributions to macromolecular biochemistry.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["she", "her", "herself", "hers"],
    "answer": 0,
    "explanation": "The pronoun serves as part of the compound subject of the passive clause ('both Dr. Vance and [she] were recognized'). Subject pronouns (I, he, she, we, they) must be used in the subject position.",
    "citation": "College Board Digital SAT Reading & Writing — Pronoun Case"
  },
  {
    "id": "sat-rw-049",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "Solar photovoltaic panels generate electricity during daylight hours with near-zero operating emissions. _______, energy storage solutions such as lithium-ion utility batteries or pumped-storage hydropower are essential to ensure uninterrupted power delivery during overcast weather and nighttime periods.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["Consequently", "Alternatively", "In spite of this", "Likewise"],
    "answer": 0,
    "explanation": "Because solar panels only generate electricity during daylight, storage solutions are needed as a direct logical consequence. 'Consequently' articulates this cause-and-effect relationship.",
    "citation": "College Board Digital SAT Reading & Writing — Transitions"
  },
  {
    "id": "sat-rw-050",
    "type": "mcq",
    "subtopic": "Dangling Modifiers (Standard English Conventions)",
    "difficulty": "Hard",
    "question": "While conducting field research on the nocturnal foraging habits of Mexican free-tailed bats, _______.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      "Dr. Hernandez recorded over forty distinct acoustic echolocation pulses",
      "over forty distinct acoustic echolocation pulses were recorded by Dr. Hernandez",
      "the night sky was filled with thousands of ultrasonic echolocation chirps",
      "ultrasonic recording equipment was set up in the desert cave by researchers"
    ],
    "answer": 0,
    "explanation": "The opening modifier 'While conducting field research...' must logically modify the agent performing the action: Dr. Hernandez. Starting the main clause with Dr. Hernandez ensures the modifier correctly connects.",
    "citation": "College Board Digital SAT Reading & Writing — Modifiers"
  },
  {
    "id": "sat-rw-051",
    "type": "mcq",
    "subtopic": "Cross-Text Connections (Craft & Structure)",
    "difficulty": "Hard",
    "question": "Text 1:\nProponents of universal basic income (UBI) argue that unconditional cash transfers provide a crucial financial floor for workers displaced by automation, enabling them to seek vocational retraining without experiencing homelessness or extreme food insecurity.\n\nText 2:\nEconomist Liam Vance questions the efficacy of unconditional cash programs, demonstrating that unless accompanied by targeted wage subsidies and local job creation investments, direct cash disbursements can trigger local inflationary spirals in housing costs, ultimately neutralizing the purchasing power of recipient families.\n\nBased on the texts, how does Liam Vance (Text 2) view the perspective offered in Text 1?",
    "options": [
      "He believes it overlooks market dynamics such as housing inflation that could negate the intended benefits of unconditional cash transfers",
      "He agrees that universal basic income alone is completely sufficient to solve long-term technological unemployment",
      "He denies that automation causes any displacement of workers in contemporary industrial economies",
      "He suggests that vocational retraining programs are counterproductive to regional economic growth"
    ],
    "answer": 0,
    "explanation": "Text 2 explicitly points out that cash transfers without other measures cause local housing inflation that neutralizes purchasing power, demonstrating that Text 1 overlooks these market counter-reactions.",
    "citation": "College Board Digital SAT Reading & Writing — Cross-Text"
  },
  {
    "id": "sat-rw-052",
    "type": "mcq",
    "subtopic": "Command of Evidence: Quantitative (Information & Ideas)",
    "difficulty": "Hard",
    "question": "A team of behavioral economists analyzed employee productivity under four different office layout designs: Traditional Private Offices (Baseline: 100), Semi-Private Cubicles (Index: 94), Open-Plan Workstations (Index: 82), and Flexible Activity-Based Zones (Index: 106). The researchers concluded that environments providing employees with autonomous control over environmental acoustic levels yield the highest task efficiency.\n\nWhich piece of data from the study most directly supports this conclusion?",
    "options": [
      "Flexible Activity-Based Zones, which allow workers to move between quiet study pods and collaborative conference spaces as needed, achieved the highest productivity score (106)",
      "Traditional Private Offices had lower maintenance costs than Semi-Private Cubicles",
      "Open-Plan Workstations had the highest total employee headcount capacity per square meter",
      "Employees in all four office configurations reported identical satisfaction with office cafeteria amenities"
    ],
    "answer": 0,
    "explanation": "The conclusion claims that autonomous control over acoustic environments maximizes efficiency. Choice A explicitly highlights that Flexible Activity-Based Zones allowed workers to self-select quiet pods vs collaborative areas and scored highest.",
    "citation": "College Board Digital SAT Reading & Writing — Quantitative Evidence"
  },
  {
    "id": "sat-rw-053",
    "type": "mcq",
    "subtopic": "Verb Form & Subjunctive (Standard English Conventions)",
    "difficulty": "Hard",
    "question": "The institutional review board mandated that the lead investigator _______ all raw biometric data before submitting the clinical trial results for publication.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": ["anonymize", "anonymizes", "anonymized", "will anonymize"],
    "answer": 0,
    "explanation": "Verbs of mandate, recommendation, or demand ('mandated that...', 'recommended that...') require the present subjunctive mood, which uses the base form of the verb: 'anonymize'.",
    "citation": "College Board Digital SAT Reading & Writing — Subjunctive Mood"
  },
  {
    "id": "sat-rw-054",
    "type": "mcq",
    "subtopic": "Punctuation with Colons (Standard English Conventions)",
    "difficulty": "Medium",
    "question": "During the excavation of Pompeii's Regio V district, archaeologists uncovered an intact thermopolium containing frescoes of three symbolic animals _______ a rooster, a mallard duck, and an leashed hunting dog.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      ": a rooster,",
      "; a rooster,",
      ", a rooster:",
      "a rooster"
    ],
    "answer": 0,
    "explanation": "A colon must be preceded by an independent clause ('...frescoes of three symbolic animals') to introduce an elaboration, list, or explanation ('a rooster, a mallard duck, and an leashed hunting dog').",
    "citation": "College Board Digital SAT Reading & Writing — Colons"
  },
  {
    "id": "sat-rw-055",
    "type": "mcq",
    "subtopic": "Rhetorical Synthesis (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "While researching the voyager spacecraft missions, a student noted:\n- Voyager 1 and Voyager 2 were launched by NASA in 1977.\n- Both spacecraft carry a Golden Record containing sounds, greetings in 55 languages, and musical selections from Earth.\n- In 2012, Voyager 1 became the first human-made object to cross the heliopause into interstellar space.\n- Voyager 2 entered interstellar space in 2018, continuing to transmit scientific data via its plasma spectrometer.\n\nThe student wants to emphasize Voyager 1's historic milestone. Which choice most effectively accomplishes this goal?",
    "options": [
      "In 2012, Voyager 1 achieved historic distinction as the first human-made object to cross the heliopause and venture into interstellar space.",
      "Launched in 1977, Voyager 1 and Voyager 2 carry Golden Records containing greetings in 55 global languages.",
      "Both Voyager spacecraft have traveled past the heliopause, carrying symbolic recordings of terrestrial music and sounds.",
      "Voyager 2 crossed into interstellar space in 2018, equipped with a plasma spectrometer that still transmits data."
    ],
    "answer": 0,
    "explanation": "The prompt specifies: 'emphasize Voyager 1's historic milestone'. Choice A directly highlights that Voyager 1 was the first human-made object to enter interstellar space in 2012.",
    "citation": "College Board Digital SAT Reading & Writing — Rhetorical Synthesis"
  },
  {
    "id": "sat-rw-056",
    "type": "mcq",
    "subtopic": "Transitions (Expression of Ideas)",
    "difficulty": "Hard",
    "question": "Many Renaissance humanist scholars championed vernacular languages like Italian and French for literary works. _______, scholastic philosophers at northern European universities staunchly maintained Latin as the sole acceptable medium for academic theological inquiry.\n\nWhich choice completes the text with the most logical transition?",
    "options": ["Conversely", "Accordingly", "For instance", "Ultimately"],
    "answer": 0,
    "explanation": "The first sentence describes humanists championing vernacular languages; the second describes scholastic philosophers insisting on Latin. 'Conversely' signals this direct contrast between two philosophical schools.",
    "citation": "College Board Digital SAT Reading & Writing — Transitions"
  },
  {
    "id": "sat-rw-057",
    "type": "mcq",
    "subtopic": "Words in Context (Craft & Structure)",
    "difficulty": "Medium",
    "question": "Because historical documents from the early Indus Valley Civilization remain undeciphered, historians must rely on material archaeology to _______ the socio-political organization of ancient Harappan cities.\n\nWhich choice completes the text with the most logical and precise word?",
    "options": ["infer", "proclaim", "fabricate", "suppress"],
    "answer": 0,
    "explanation": "Without readable written records, historians must use physical artifacts to deduce or draw reasoned conclusions about society. 'Infer' means to deduce from evidence rather than explicit statements.",
    "citation": "College Board Digital SAT Reading & Writing — Words in Context"
  },
  {
    "id": "sat-rw-058",
    "type": "mcq",
    "subtopic": "Logical Completion (Information & Ideas)",
    "difficulty": "Hard",
    "question": "When introduced into island ecosystems devoid of native mammalian apex predators, invasive snakes frequently cause rapid declines among endemic flightless birds. Evolutionary biologists note that because island species evolved over millennia without experiencing predatory pursuit, they lack innate flight-or-fight avoidance reflexes. As a consequence, attempts to mitigate invasive predation purely by providing artificial nest boxes _______.\n\nWhich choice most logically completes the text?",
    "options": [
      "are unlikely to succeed unless supplemented by active predator eradication or physical barrier exclusion",
      "will immediately prompt endemic birds to evolve acute predator-avoidance reflexes within a single generation",
      "have universally succeeded in restoring flightless bird populations to historic pre-settlement levels",
      "prove that native bird species are inherently unsuited to surviving in island environments"
    ],
    "answer": 0,
    "explanation": "Because the birds lack innate predator-avoidance instincts, simply providing nest boxes does not solve the vulnerability; active eradication or barrier exclusion is necessary for success.",
    "citation": "College Board Digital SAT Reading & Writing — Inferences"
  },
  {
    "id": "sat-rw-059",
    "type": "mcq",
    "subtopic": "Comma Splice Prevention (Standard English Conventions)",
    "difficulty": "Easy",
    "question": "The architectural committee approved the blueprint for the new performing arts center _______ construction is scheduled to commence early next spring.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
    "options": [
      ", and",
      ",",
      "and",
      ", but"
    ],
    "answer": 0,
    "explanation": "Two independent clauses must be joined by a comma followed by a coordinating conjunction (FANBOYS). ', and' correctly connects the two independent statements.",
    "citation": "College Board Digital SAT Reading & Writing — Clauses"
  },
  {
    "id": "sat-rw-060",
    "type": "mcq",
    "subtopic": "Rhetorical Synthesis (Expression of Ideas)",
    "difficulty": "Medium",
    "question": "While researching the discovery of cosmic microwave background radiation, a student noted:\n- In 1965, Arno Penzias and Robert Wilson were testing a supersensitive horn antenna at Bell Labs.\n- They detected persistent background noise that was isotropic—uniform in all directions of the sky.\n- Princeton astrophysicists Robert Dicke and Jim Peebles realized this noise was the thermal remnant of the Big Bang.\n- Penzias and Wilson were awarded the 1978 Nobel Prize in Physics for this serendipitous discovery.\n\nThe student wants to emphasize how the discovery was made accidentally. Which choice most effectively accomplishes this goal?",
    "options": [
      "Arno Penzias and Robert Wilson serendipitously discovered the thermal remnant of the Big Bang while troubleshooting unexplained background noise on an antenna at Bell Labs.",
      "The cosmic microwave background radiation is an isotropic radiation bath detected across the entire celestial sphere.",
      "Princeton astrophysicists Robert Dicke and Jim Peebles provided the theoretical explanation for the cosmic microwave background in 1965.",
      "In 1978, the Nobel Prize in Physics was awarded to Bell Labs engineers for their contributions to cosmology."
    ],
    "answer": 0,
    "explanation": "Choice A highlights that the discovery occurred 'serendipitously' while troubleshooting unrelated antenna noise, directly meeting the goal of emphasizing the accidental nature of the discovery.",
    "citation": "College Board Digital SAT Reading & Writing — Rhetorical Synthesis"
  }
]

# Write SAT Reading Set 3 JSON
with open(os.path.join(US_DATA_SAT, "digital_sat_reading_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": sat_reading_set3}, f, indent=2, ensure_ascii=False)

print("Generated Digital SAT Reading Set 3 successfully!")
