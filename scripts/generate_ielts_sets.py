import json
import os

set2_questions = [
    # Passage 1: The Domestication of Emmer Wheat & Fertile Crescent Agriculture
    {
        "id": "ielts-read-021",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: Fertile Crescent Agriculture)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Radiocarbon dating of carbonised grain deposits at Abu Hureyra indicates that nomadic foragers began cultivating wild rye and emmer wheat approximately 11,500 years ago during the Younger Dryas cold event, when wild game populations plummeted.'\n\nQuestion: Foragers at Abu Hureyra transitioned to cereal cultivation primarily because wild animals became scarce during a period of climatic cooling.",
        "options": [
            "TRUE (The statement agrees with the information in the text)",
            "FALSE (The statement contradicts the information in the text)",
            "NOT GIVEN (There is no information on this in the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The passage confirms that foragers began cultivating grains 'during the Younger Dryas cold event, when wild game populations plummeted' (animals became scarce during climatic cooling). The assertion is directly supported: TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-022",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: Fertile Crescent Agriculture)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Wild cereals possessed brittle rachises that shattered automatically upon maturity, scattering seeds widely across the hillside soils.'\n\nQuestion: Early Neolithic farmers preferred cereals with brittle rachises because they were easier to harvest in large quantities.",
        "options": [
            "FALSE (The statement directly contradicts the information in the text)",
            "TRUE (The statement agrees with the information in the text)",
            "NOT GIVEN (There is no information on this in the text)",
            "INSUFFICIENT CONTEXT"
        ],
        "answer": 0,
        "explanation": "The text explains that wild cereals with brittle rachises scattered seeds automatically across hillsides, which made harvesting difficult; domestication selected for non-shattering rachises so grains stayed on the stalk. The claim that farmers preferred brittle rachises contradicts botanical and archaeological reality: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-023",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: Fertile Crescent Agriculture)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'Skeletal remains from early agricultural strata display pronounced lumbar osteoarthritis and dental caries, reflecting the physically punitive grinding of grains with quern stones and high carbohydrate intake.'\n\nQuestion: Hunter-gatherer communities in the Levant suffered higher rates of tooth decay than settled agriculturalists.",
        "options": [
            "FALSE (The statement contradicts the text, which associates dental caries specifically with agricultural carbohydrate diets)",
            "TRUE (The statement agrees with the text)",
            "NOT GIVEN (No comparison of hunter-gatherer dental health is made in the text)",
            "INSUFFICIENT DATA"
        ],
        "answer": 0,
        "explanation": "The text links dental caries (tooth decay) specifically to the high carbohydrate intake of settled agriculturalists. Asserting that hunter-gatherers suffered higher rates contradicts the passage findings: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-024",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: Fertile Crescent Agriculture)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Storage pits lined with calcified lime plaster allowed surplus harvests to be preserved across multiple drought cycles, fostering permanent village architecture.'\n\nQuestion: Ceramic pottery was invented in Abu Hureyra prior to the use of plastered storage pits.",
        "options": [
            "NOT GIVEN (The passage describes plastered storage pits but makes no mention of the invention timeline of ceramic pottery)",
            "TRUE (The statement agrees with the text)",
            "FALSE (The statement contradicts the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The passage details the use of lime plaster storage pits for surplus preservation, but never mentions ceramic pottery or its chronological invention. Therefore, it is NOT GIVEN.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-025",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Lexical Resource)",
        "difficulty": "Hard",
        "question": "Passage Sentence: 'The shift from foraging to sedentary farming was not an abrupt revolution but a protracted, **piecemeal** adaptation spanning centuries.'\n\nIn this sentence, the word 'piecemeal' is closest in meaning to:",
        "options": [
            "Gradual and happening in separate, unsystematic stages",
            "Disastrous and economically devastating",
            "Premeditated and coordinated across distant tribes",
            "Universal and adopted simultaneously worldwide"
        ],
        "answer": 0,
        "explanation": "'Piecemeal' means done gradually or piece by piece, rather than all at once. The author contrasts it with an 'abrupt revolution' to describe a protracted process occurring in separate stages.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Lexical Resource"
    },
    {
        "id": "ielts-read-026",
        "type": "mcq",
        "subtopic": "Summary Completion (Passage 1: Fertile Crescent Agriculture)",
        "difficulty": "Medium",
        "question": "Summary Sentence: 'The preservation of surplus grain in lime-plastered pits enabled early communities to withstand recurrent __________, which laid the social foundation for permanent architectural settlements.'\n\nWhich word from the passage correctly completes the summary?",
        "options": [
            "drought cycles",
            "predator invasions",
            "seasonal migrations",
            "pluvial floods"
        ],
        "answer": 0,
        "explanation": "The text states: 'storage pits lined with calcified lime plaster allowed surplus harvests to be preserved across multiple drought cycles'. Thus, 'drought cycles' completes the summary accurately.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Summary Completion"
    },
    {
        "id": "ielts-read-027",
        "type": "mcq",
        "subtopic": "Matching Headings (Passage 1: Fertile Crescent Agriculture)",
        "difficulty": "Hard",
        "question": "Paragraph: 'By cultivating dense monocultures of wheat and barley, Neolithic communities unintentionally depleted micronutrients in alluvial soils, necessitating fallow rotations and organic soil replenishment through animal manure. This agricultural intensification also facilitated the transmission of zoonotic pathogens from livestock to human hosts, introducing tuberculosis and measles to crowded mudbrick settlements.'\n\nWhich heading best expresses the main idea of this paragraph?",
        "options": [
            "Unforeseen ecological degradation and epidemiological consequences of sedentary farming",
            "Methods of domesticating cattle and caprines in upper Mesopotamia",
            "Archaeological evidence for the eradication of prehistoric infectious diseases",
            "The chemical composition of alluvial river valleys in the Fertile Crescent"
        ],
        "answer": 0,
        "explanation": "The paragraph focuses on two major negative outcomes of intensive farming: soil nutrient depletion (ecological) and the transfer of zoonotic pathogens like measles and TB (epidemiological). 'Unforeseen ecological degradation and epidemiological consequences of sedentary farming' captures both core arguments.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Matching Headings"
    },

    # Passage 2: Deep-Sea Manganese Nodules and Benthic Ecosystems
    {
        "id": "ielts-read-028",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 2: Deep-Sea Manganese Nodules)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Polymetallic nodules resting on the abyssal plains of the Clarion-Clipperton Zone grow at rates of merely several millimetres per million years through the precipitation of metallic ions from ambient seawater.'\n\nQuestion: Deep-sea polymetallic nodules accumulate mass far more slowly than terrestrial geological deposits.",
        "options": [
            "TRUE (The statement agrees with the information in the text)",
            "FALSE (The statement contradicts the information in the text)",
            "NOT GIVEN (There is no information on this in the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "A growth rate of 'several millimetres per million years' is among the slowest geological processes on Earth, vastly slower than normal sedimentary or terrestrial mineral deposits. The assertion agrees: TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-029",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 2: Deep-Sea Manganese Nodules)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'These potato-sized concretions provide the sole hard substrate in a vast desert of soft sediment, anchoring specialized benthic fauna such as stalked hexactinellid sponges and xenophyophores.'\n\nQuestion: Sessile benthic organisms in the abyssal plain can thrive with equal abundance on soft pelagic sediment alone.",
        "options": [
            "FALSE (The statement contradicts the text, which designates nodules as the 'sole hard substrate' required by these specialized organisms)",
            "TRUE (The statement agrees with the text)",
            "NOT GIVEN (There is no mention of sediment survival)",
            "INSUFFICIENT EVIDENCE"
        ],
        "answer": 0,
        "explanation": "The passage states that nodules provide the 'sole hard substrate' anchoring these specialized stalked sponges. Claiming they can thrive with equal abundance on soft sediment contradicts this: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-030",
        "type": "mcq",
        "subtopic": "Matching Headings (Passage 2: Deep-Sea Manganese Nodules)",
        "difficulty": "Hard",
        "question": "Paragraph: 'Proposed commercial seabed extraction techniques utilize heavy tracked harvesting vehicles that scrape the top twenty centimetres of abyssal mud. Beyond the physical annihilation of nodule-dependent communities, this process generates dense sediment plumes that linger in suspension across ocean currents for weeks, potentially clogging the filter-feeding apparatus of midwater pelagic species.'\n\nWhich heading best summarizes this paragraph?",
        "options": [
            "Environmental ramifications: Habitat obliteration and suspended particulate plumes",
            "Engineering breakthroughs in subsea robotic propulsion systems",
            "The global market demand for nickel and cobalt in battery manufacturing",
            "International legal jurisdiction over outer continental shelf resources"
        ],
        "answer": 0,
        "explanation": "The paragraph explores two direct impacts of seabed mining: the physical destruction of benthic communities and the damaging suspension plumes that affect pelagic organisms. Heading 'Environmental ramifications: Habitat obliteration and suspended particulate plumes' summarizes this completely.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Matching Headings"
    },
    {
        "id": "ielts-read-031",
        "type": "mcq",
        "subtopic": "Multiple Choice (Passage 2: Deep-Sea Manganese Nodules)",
        "difficulty": "Medium",
        "question": "According to the passage, why are mining consortia primarily interested in polymetallic nodules in the Clarion-Clipperton Zone?",
        "options": [
            "They contain exceptionally high concentrations of critical energy-transition metals like nickel, cobalt, and copper",
            "They can be extracted with zero carbon footprint compared to underground mining",
            "They are located entirely within national territorial waters free of United Nations oversight",
            "They contain vast pockets of trapped petroleum hydrocarbons"
        ],
        "answer": 0,
        "explanation": "Polymetallic nodules are coveted by international mining consortia because they are rich in nickel, cobalt, copper, and manganese—essential inputs for electric vehicle batteries and grid energy storage.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Multiple Choice"
    },
    {
        "id": "ielts-read-032",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 2: Deep-Sea Manganese Nodules)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'The International Seabed Authority (ISA), established under the 1982 United Nations Convention on the Law of the Sea (UNCLOS), is tasked with regulating mineral-related activities in the international seabed Area.'\n\nQuestion: The International Seabed Authority has already issued permanent exploitation permits for commercial deep-sea mining in the Atlantic Ocean.",
        "options": [
            "NOT GIVEN (The passage identifies the ISA's mandate under UNCLOS, but provides no information regarding commercial permits in the Atlantic Ocean)",
            "TRUE (The statement agrees with the text)",
            "FALSE (The statement contradicts the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The passage establishes the regulatory role of the ISA under UNCLOS, but says nothing about whether commercial exploitation permits have been issued in the Atlantic Ocean: NOT GIVEN.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-033",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Lexical Resource)",
        "difficulty": "Medium",
        "question": "Passage Sentence: 'Because benthic metabolic rates are extraordinarily sluggish in the near-freezing abyssal waters, disturbed communities exhibit negligible **recuperation** even decades after experimental trawling.'\n\nIn this context, 'recuperation' is closest in meaning to:",
        "options": [
            "Recovery and biological restoration",
            "Degradation and biological collapse",
            "Reproduction of commercial fish stocks",
            "Evolutionary divergence into new species"
        ],
        "answer": 0,
        "explanation": "'Recuperation' means the recovery or restoration of health, strength, or functioning. In an ecological context, it refers to the natural recovery of organisms and habitats after physical disruption.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Lexical Resource"
    },
    {
        "id": "ielts-read-034",
        "type": "mcq",
        "subtopic": "Summary Completion (Passage 2: Deep-Sea Manganese Nodules)",
        "difficulty": "Medium",
        "question": "Summary Sentence: 'The abyssal environment lacks natural hard surfaces, which makes nodule fields essential because they provide the only __________ capable of anchoring sessile organisms like hexactinellid sponges.'\n\nWhich term from the passage completes the summary?",
        "options": [
            "hard substrate",
            "saline current",
            "thermal vent",
            "hydrocarbon seep"
        ],
        "answer": 0,
        "explanation": "The passage explicitly notes that nodules 'provide the sole hard substrate in a vast desert of soft sediment, anchoring specialized benthic fauna'. Hence, 'hard substrate' is the exact required term.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Summary Completion"
    },

    # Passage 3: Neuroplasticity and Cognitive Reserve in Bilingual Adults
    {
        "id": "ielts-read-035",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 3: Neuroplasticity in Bilinguals)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Longitudinal functional neuroimaging reveals that lifelong bilinguals exhibit significantly greater grey matter density in the anterior cingulate cortex, a region responsible for executive control and conflict monitoring.'\n\nQuestion: Bilingualism leads to measurable anatomical differences in brain regions associated with managing conflicting information.",
        "options": [
            "TRUE (The statement agrees with the information in the text)",
            "FALSE (The statement contradicts the information in the text)",
            "NOT GIVEN (There is no information on this in the text)",
            "INSUFFICIENT CONTEXT"
        ],
        "answer": 0,
        "explanation": "The text states that bilinguals show greater grey matter density in the anterior cingulate cortex, 'a region responsible for executive control and conflict monitoring' (managing conflicting information). This is directly supported: TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-036",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 3: Neuroplasticity in Bilinguals)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'When speaking in one language, bilingual individuals continuously suppress competing lexical candidates from their other language through active inhibitory control mechanisms.'\n\nQuestion: Bilingual speakers completely deactivate their non-target language so that it never interferes during speech production.",
        "options": [
            "FALSE (The text states they 'continuously suppress competing lexical candidates', proving the non-target language remains active and requires inhibition)",
            "TRUE (The statement agrees with the text)",
            "NOT GIVEN (There is no mention of language deactivation)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The passage states that bilinguals must 'continuously suppress competing lexical candidates', meaning the unused language remains activated and competing, rather than being completely deactivated: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-037",
        "type": "mcq",
        "subtopic": "Multiple Choice (Passage 3: Neuroplasticity in Bilinguals)",
        "difficulty": "Medium",
        "question": "According to epidemiological studies cited in the text, how does bilingualism influence the clinical manifestation of Alzheimer's disease?",
        "options": [
            "It delays the onset of observable clinical symptoms by four to five years through enhanced cognitive reserve, despite equivalent underlying neuropathology",
            "It prevents the physical formation of amyloid-beta plaques in brain tissue",
            "It eliminates all forms of age-related memory deterioration entirely",
            "It restricts neurodegenerative decline exclusively to the primary auditory cortex"
        ],
        "answer": 0,
        "explanation": "Studies by Bialystok and colleagues demonstrate that bilinguals show clinical dementia symptoms 4 to 5 years later than monolinguals, not because brain pathology is absent, but because enhanced cognitive reserve allows them to compensate longer.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Multiple Choice"
    },
    {
        "id": "ielts-read-038",
        "type": "mcq",
        "subtopic": "Matching Headings (Passage 3: Neuroplasticity in Bilinguals)",
        "difficulty": "Hard",
        "question": "Paragraph: 'Critics of the bilingual advantage hypothesis argue that reported benefits in executive function tasks like the Simon or Flanker task often vanish when studies control strictly for socioeconomic status, parental education, and cultural immersion. Several high-powered pre-registered replications have failed to replicate statistically significant reaction-time differences between monolingual and multilingual adult cohorts.'\n\nWhich heading best encapsulates this paragraph?",
        "options": [
            "Methodological scepticism and non-replication of the executive function advantage",
            "The neural correlates of childhood simultaneous language acquisition",
            "Statistical superiority of bilingual processing in auditory memory tests",
            "Genetic predispositions to multilingual fluency in European populations"
        ],
        "answer": 0,
        "explanation": "The paragraph highlights criticisms of the bilingual advantage, pointing out confounding variables (socioeconomic status) and replication failures in large studies. 'Methodological scepticism and non-replication of the executive function advantage' encapsulates this perfectly.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Matching Headings"
    },
    {
        "id": "ielts-read-039",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Lexical Resource)",
        "difficulty": "Hard",
        "question": "Passage Sentence: 'The brain's ability to maintain functional integrity in the face of pathological insult is termed cognitive reserve, serving as a neural buffer against neurodegenerative **attenuation**.'\n\nIn this sentence, 'attenuation' is closest in meaning to:",
        "options": [
            "Weakening, reduction, or diminishment",
            "Acceleration or rapid advancement",
            "Genetic mutation or cellular transformation",
            "Complete physical calcification"
        ],
        "answer": 0,
        "explanation": "'Attenuation' denotes a reduction in force, intensity, effect, or value. In neurology, it describes the progressive weakening or impairment caused by disease.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Lexical Resource"
    },
    {
        "id": "ielts-read-040",
        "type": "mcq",
        "subtopic": "Writer's View / Claim (Yes / No / Not Given)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'While acquiring a second language later in life may not produce the native-like phonological accents of early bilinguals, it nevertheless stimulates white matter structural neuroplasticity across the corpus callosum.'\n\nQuestion: Late language learners can never derive structural neurological benefits from foreign language study.",
        "options": [
            "NO (The writer's claim is that late language acquisition nevertheless stimulates white matter structural neuroplasticity)",
            "YES (The statement agrees with the writer's claim)",
            "NOT GIVEN (The writer expresses no view on late learners)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The author specifically states that late language learning 'nevertheless stimulates white matter structural neuroplasticity across the corpus callosum'. Claiming they can never derive structural benefits directly contradicts the writer's assertion: NO.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Writer's View / Claim"
    }
]

set3_questions = [
    # Passage 1: The Cryptographic Methods of the Voynich Manuscript
    {
        "id": "ielts-read-041",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: The Voynich Manuscript)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Carbon-14 testing conducted by the University of Arizona firmly dates the vellum folios of the enigmatic Voynich Manuscript to between 1404 and 1438, securely placing its manufacture in the early Italian Renaissance.'\n\nQuestion: Scientific testing confirms that the Voynich Manuscript's parchment was produced during the fifteenth century.",
        "options": [
            "TRUE (The statement agrees with the information in the text: 1404–1438 falls within the 15th century)",
            "FALSE (The statement contradicts the information in the text)",
            "NOT GIVEN (There is no information on this in the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The years 1404 to 1438 fall directly in the early 15th century. Carbon-14 testing confirming this date range makes the statement completely TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-042",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: The Voynich Manuscript)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'Unlike natural European languages which follow Zipf's law with predictable word-length distributions, 'Voynichese' features unusually low entropy and an almost complete absence of words exceeding two syllables.'\n\nQuestion: The vocabulary of Voynichese conforms to the statistical frequency patterns typical of medieval Latin and German.",
        "options": [
            "FALSE (The text explicitly contrasts Voynichese with natural European languages, noting its unusually low entropy and atypical distribution)",
            "TRUE (The statement agrees with the text)",
            "NOT GIVEN (No comparison with Latin or German is made)",
            "INSUFFICIENT DATA"
        ],
        "answer": 0,
        "explanation": "The text states that unlike natural European languages, Voynichese has unusually low entropy and an absence of longer words, contradicting the claim that it conforms to typical medieval European patterns: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-043",
        "type": "mcq",
        "subtopic": "Matching Headings (Passage 1: The Voynich Manuscript)",
        "difficulty": "Hard",
        "question": "Paragraph: 'Palaeobotanists inspecting the manuscript's botanical illustrations have struggled to identify a single living plant specimen with certainty. Many drawings combine the leaves of one species with the roots of another, leading some cryptanalysts to hypothesize that the text is an elaborate fifteenth-century hoax crafted with Cardan grilles to fetch a princely sum from Emperor Rudolf II.'\n\nWhich heading best encapsulates this paragraph?",
        "options": [
            "Botanical incongruities and the fraudulent artefact hypothesis",
            "Renaissance classification systems for alpine herbal pharmacology",
            "The imperial library archives of Emperor Rudolf II in Prague",
            "Microscopic chemical analysis of Renaissance manuscript pigments"
        ],
        "answer": 0,
        "explanation": "The paragraph highlights two core points: the impossible, mixed botanical drawings (incongruities) and the resulting hypothesis that it was a deliberate hoax created to deceive Emperor Rudolf II. Heading 'Botanical incongruities and the fraudulent artefact hypothesis' summarizes this precisely.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Matching Headings"
    },
    {
        "id": "ielts-read-044",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 1: The Voynich Manuscript)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'During World War II, famed cryptanalyst William Friedman led a team of codebreakers attempting to decipher the text using early IBM tabulating machinery, yet concluded without identifying a single deciphered sentence.'\n\nQuestion: William Friedman succeeded in cracking military ciphers, but found the Voynich script completely unyielding.",
        "options": [
            "TRUE (The statement agrees with the text, which identifies Friedman as a famed cryptanalyst who failed to decipher a single sentence of the manuscript)",
            "FALSE (The statement contradicts the text)",
            "NOT GIVEN (Friedman's other successes are not discussed)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The text notes that renowned codebreaker William Friedman worked on it with punch-card tabulators and concluded without identifying a single deciphered sentence: TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-045",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Lexical Resource)",
        "difficulty": "Medium",
        "question": "Passage Sentence: 'Despite recent breakthroughs in neural natural language processing, the manuscript's internal semantics remain wholly **inscrutable**.'\n\nIn this sentence, the word 'inscrutable' is closest in meaning to:",
        "options": [
            "Impossible to understand or interpret",
            "Widely disputed among political historians",
            "Prone to sudden physical deterioration",
            "Easily converted into numerical tables"
        ],
        "answer": 0,
        "explanation": "'Inscrutable' means impossible to comprehend, interpret, or penetrate. The author emphasizes that modern AI models still cannot decipher the manuscript's meaning.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Lexical Resource"
    },
    {
        "id": "ielts-read-046",
        "type": "mcq",
        "subtopic": "Summary Completion (Passage 1: The Voynich Manuscript)",
        "difficulty": "Medium",
        "question": "Summary Sentence: 'The physical vellum pages of the Voynich Manuscript were reliably dated to the early 1400s using __________ testing.'\n\nWhich phrase from the text correctly completes the summary?",
        "options": [
            "Carbon-14",
            "DNA sequence",
            "infrared spectroscopy",
            "thermoluminescence"
        ],
        "answer": 0,
        "explanation": "The text states: 'Carbon-14 testing conducted by the University of Arizona firmly dates the vellum folios'. Thus, 'Carbon-14' completes the summary.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Summary Completion"
    },
    {
        "id": "ielts-read-047",
        "type": "mcq",
        "subtopic": "Multiple Choice (Passage 1: The Voynich Manuscript)",
        "difficulty": "Hard",
        "question": "Why do some linguistic researchers maintain that Voynichese might still represent an authentic natural language rather than meaningless gibberish?",
        "options": [
            "Its character co-occurrence statistics closely mirror the mathematical entropy metrics of natural languages in other writing systems",
            "Several chapters contain direct marginal glosses written in standard Renaissance French",
            "The chemical ink formulation exactly matches contemporary theological manuscripts from Oxford",
            "Radio telescopes detected matching signals in interstellar background radiation"
        ],
        "answer": 0,
        "explanation": "Quantitative computational linguists have found that despite low word-level entropy, characters and words in Voynichese exhibit long-range thematic clustering and statistical co-occurrence properties that are extremely difficult to fake randomly.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Multiple Choice"
    },

    # Passage 2: Cryosphere Retreat and the Albedo Feedback Loop
    {
        "id": "ielts-read-048",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 2: Cryosphere Retreat & Albedo)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Fresh sea ice reflects up to 85 percent of incoming solar radiation back into space, whereas exposed dark open ocean water absorbs roughly 90 percent of the identical thermal energy.'\n\nQuestion: Open seawater reflects substantially less solar heat than sea ice.",
        "options": [
            "TRUE (The statement agrees with the information in the text: 10% reflected vs 85% reflected)",
            "FALSE (The statement contradicts the information in the text)",
            "NOT GIVEN (There is no information on this in the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "Ice reflects up to 85% while open water absorbs 90% (reflecting only ~10%). Thus open seawater reflects substantially less heat than ice: TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-049",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 2: Cryosphere Retreat & Albedo)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'This discrepancy creates a self-reinforcing positive feedback mechanism: diminishing sea ice exposes darker ocean water, which absorbs more heat, warming the surface layer and expediting further ice melting.'\n\nQuestion: The ice-albedo feedback cycle causes regional polar air temperatures to cool down during summer months.",
        "options": [
            "FALSE (The passage describes a positive feedback loop that amplifies warming and accelerates melting, rather than causing cooling)",
            "TRUE (The statement agrees with the text)",
            "NOT GIVEN (No seasonal details are mentioned)",
            "INSUFFICIENT DATA"
        ],
        "answer": 0,
        "explanation": "The text explains that the cycle absorbs more heat, warms surface waters, and expedites further melting. The assertion that it causes temperatures to cool down directly contradicts the passage: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-040",
        "type": "mcq",
        "subtopic": "Matching Headings (Passage 2: Cryosphere Retreat & Albedo)",
        "difficulty": "Hard",
        "question": "Paragraph: 'As perennial multi-year ice is replaced by fragile seasonal first-year ice, the physical barrier preventing atmospheric moisture exchange weakens. Enhanced evaporation over newly open Arctic waters fuels heavier autumn snowfall over Siberia, which perturb the stratospheric polar vortex and destabilize mid-latitude jet stream trajectories across North America and Western Europe.'\n\nWhich heading best describes this paragraph?",
        "options": [
            "Trans-regional weather destabilization linked to diminished polar ice thickness",
            "Historical commercial shipping routes across the Northwest Passage",
            "The chemical desalinization of North Atlantic deep water formation",
            "Satellite telemetry techniques for calculating sea ice thickness"
        ],
        "answer": 0,
        "explanation": "The paragraph details how thinner ice increases evaporation, alters Siberian snow cover, and destabilizes the polar vortex and jet streams in Europe and North America. 'Trans-regional weather destabilization linked to diminished polar ice thickness' captures this accurately.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Matching Headings"
    },
    {
        "id": "ielts-read-051",
        "type": "mcq",
        "subtopic": "Summary Completion (Passage 2: Cryosphere Retreat & Albedo)",
        "difficulty": "Medium",
        "question": "Summary Sentence: 'The transition from reflective white ice to dark seawater establishes a __________ feedback loop that accelerates planetary heat absorption.'\n\nWhich word from the passage completes the summary?",
        "options": [
            "positive",
            "negative",
            "stagnant",
            "linear"
        ],
        "answer": 0,
        "explanation": "The text specifically characterizes this as a 'self-reinforcing positive feedback mechanism'. 'Positive' is the correct scientific term.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Summary Completion"
    },
    {
        "id": "ielts-read-052",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 2: Cryosphere Retreat & Albedo)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Methane clathrate deposits trapped within submarine permafrost along the East Siberian Arctic Shelf represent a potent greenhouse gas reservoir vulnerable to rising bottom-water temperatures.'\n\nQuestion: Scientists have calculated the exact calendar year when all East Siberian methane clathrates will be released.",
        "options": [
            "NOT GIVEN (The text notes their vulnerability to warming, but never mentions a specific calendar year prediction)",
            "TRUE (The statement agrees with the text)",
            "FALSE (The statement contradicts the text)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The passage discusses the vulnerability of methane clathrates to rising temperatures, but provides no specific calendar date or year for when complete release will occur: NOT GIVEN.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-053",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Lexical Resource)",
        "difficulty": "Hard",
        "question": "Passage Sentence: 'The melting of subpolar ice caps threatens to introduce massive volumes of freshwater into the Nordic Seas, potentially **disrupting** the thermohaline circulation.'\n\nIn this sentence, the word 'disrupting' is closest in meaning to:",
        "options": [
            "Upsetting, disturbing, or throwing into disorder",
            "Accelerating and increasing the efficiency of",
            "Purifying and improving chemical quality of",
            "Stabilizing and insulating against fluctuations"
        ],
        "answer": 0,
        "explanation": "'Disrupting' means causing disorder, turmoil, or interruption to an established process or system. The freshwater influx threatens to upset the density-driven oceanic conveyor belt.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Lexical Resource"
    },
    {
        "id": "ielts-read-054",
        "type": "mcq",
        "subtopic": "Multiple Choice (Passage 2: Cryosphere Retreat & Albedo)",
        "difficulty": "Medium",
        "question": "According to the passage, why is 'multi-year ice' ecologically and climatologically superior to 'first-year seasonal ice'?",
        "options": [
            "It is significantly thicker, less saline, and more resilient against summer solar radiation",
            "It contains higher concentrations of photosynthetic cyanobacteria",
            "It moves faster across ocean currents, distributing colder water globally",
            "It forms exclusively in tropical reef environments"
        ],
        "answer": 0,
        "explanation": "Multi-year ice survives successive summer melting seasons, allowing it to become thicker, expel more brine (lower salinity), and build greater structural resilience against solar heating than fragile first-year ice.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Multiple Choice"
    },

    # Passage 3: Biomimetic Engineering of Geckos' Van der Waals Adhesion
    {
        "id": "ielts-read-055",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 3: Gecko Van der Waals Adhesion)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Geckos achieve dry, residue-free adhesion across inverted surfaces through millions of microscopic keratinous hairs termed setae, which branch into hundreds of nanoscale spatulae.'\n\nQuestion: Geckos rely on sticky liquid chemical secretions from specialized toe glands to adhere to walls.",
        "options": [
            "FALSE (The passage explicitly defines their adhesion as 'dry, residue-free' resulting from microscopic physical structures, not chemical liquids)",
            "TRUE (The statement agrees with the text)",
            "NOT GIVEN (Chemical glands are not discussed)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The text states that geckos use 'dry, residue-free adhesion' facilitated by physical nanoscale structures (setae and spatulae). The assertion that they rely on sticky liquid secretions directly contradicts this: FALSE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-056",
        "type": "mcq",
        "subtopic": "True / False / Not Given (Passage 3: Gecko Van der Waals Adhesion)",
        "difficulty": "Hard",
        "question": "Passage Statement: 'When these nanoscale spatulae conform intimately to the microscopic contours of a surface, intermolecular attraction occurs via Van der Waals forces, which require no suction or vacuum to operate.'\n\nQuestion: Van der Waals adhesion can function effectively in the vacuum of outer space.",
        "options": [
            "TRUE (The passage notes that Van der Waals forces 'require no suction or vacuum to operate', meaning atmospheric pressure is not needed)",
            "FALSE (The statement contradicts the text)",
            "NOT GIVEN (There is no reference to space environments in the text)",
            "INSUFFICIENT DATA"
        ],
        "answer": 0,
        "explanation": "Because the text specifies that Van der Waals forces 'require no suction or vacuum to operate' (i.e. they do not rely on air pressure or suction cups), the intermolecular adhesion functions independently of an atmosphere, making it viable in a vacuum: TRUE.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: True/False/Not Given"
    },
    {
        "id": "ielts-read-057",
        "type": "mcq",
        "subtopic": "Matching Headings (Passage 3: Gecko Van der Waals Adhesion)",
        "difficulty": "Hard",
        "question": "Paragraph: 'A central challenge in fabricating synthetic gecko adhesives lies in replicating the hierarchy of stiffness. Fabricating microscopic pillars out of soft polymers often leads to structural collapse, where adjacent pillars adhere to one another rather than the substrate. Researchers have solved this by manufacturing composite structures featuring a rigid polyurethane stalk capped with a highly compliant polydimethylsiloxane (PDMS) tip.'\n\nWhich heading best matches this paragraph?",
        "options": [
            "Overcoming structural clustering through multi-tiered synthetic materials",
            "The evolutionary taxonomy of Gekkonidae lizards in Southeast Asia",
            "Methods of synthesizing carbon nanotubes in high-temperature furnaces",
            "Comparing gecko adhesion with tree frog wet mucus pads"
        ],
        "answer": 0,
        "explanation": "The paragraph explains the engineering obstacle of pillar clustering/collapse and how composite materials with different stiffness levels (polyurethane stalk + PDMS tip) solved it. 'Overcoming structural clustering through multi-tiered synthetic materials' fits perfectly.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Matching Headings"
    },
    {
        "id": "ielts-read-058",
        "type": "mcq",
        "subtopic": "Summary Completion (Passage 3: Gecko Van der Waals Adhesion)",
        "difficulty": "Medium",
        "question": "Summary Sentence: 'Gecko adhesion operates at the molecular level, relying on weak intermolecular __________ forces rather than chemical glues or suction cups.'\n\nWhich phrase from the text completes the summary?",
        "options": [
            "Van der Waals",
            "hydrophobic covalent",
            "magnetic dipolar",
            "electrostatic ionic"
        ],
        "answer": 0,
        "explanation": "The text states: 'intermolecular attraction occurs via Van der Waals forces'. 'Van der Waals' is the precise scientific term.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Summary Completion"
    },
    {
        "id": "ielts-read-059",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Lexical Resource)",
        "difficulty": "Hard",
        "question": "Passage Sentence: 'To detach its foot, the gecko alters the angle of inclination of its toes, a mechanism that instantly **abates** the shear stress holding the spatulae against the substrate.'\n\nIn this context, the word 'abates' is closest in meaning to:",
        "options": [
            "Reduces, lessens, or diminishes",
            "Multiplies or amplifies",
            "Reverses polarity of",
            "Transfers into electrical kinetic energy"
        ],
        "answer": 0,
        "explanation": "'Abate' means to become less intense or widespread, or to lessen and reduce. Changing the toe angle decreases the adhesion forces instantly.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Lexical Resource"
    },
    {
        "id": "ielts-read-060",
        "type": "mcq",
        "subtopic": "Writer's View / Claim (Yes / No / Not Given)",
        "difficulty": "Medium",
        "question": "Passage Statement: 'Robotic grasping systems outfitted with synthetic gecko pads have successfully demonstrated autonomous capture of non-cooperative orbital space debris without requiring toxic chemical propellants or damaging clamping pressure.'\n\nQuestion: Biomimetic gecko adhesives offer practical utility in aerospace technology.",
        "options": [
            "YES (The writer's claim is that synthetic gecko pads successfully capture orbital space debris without harmful clamping pressure)",
            "NO (The statement contradicts the writer's claim)",
            "NOT GIVEN (The writer expresses no opinion on aerospace applications)",
            "CANNOT BE DETERMINED"
        ],
        "answer": 0,
        "explanation": "The passage explicitly demonstrates their successful implementation in capturing orbital space debris without damage, confirming that they offer practical aerospace utility: YES.",
        "citation": "Cambridge IELTS Academic Reading — Question Type: Writer's View / Claim"
    }
]

os.makedirs('mocktestvault.com/data/global/ielts', exist_ok=True)

with open('mocktestvault.com/data/global/ielts/ielts_reading_set2.json', 'w', encoding='utf-8') as f:
    json.dump({"questions": set2_questions}, f, indent=2)

with open('mocktestvault.com/data/global/ielts/ielts_reading_set3.json', 'w', encoding='utf-8') as f:
    json.dump({"questions": set3_questions}, f, indent=2)

print("Generated ielts_reading_set2.json (20 Qs) and ielts_reading_set3.json (20 Qs) successfully!")
