#!/usr/bin/env python3
"""
Generates TOEFL® iBT Reading Diagnostic Test 02 (toefl-read-021 to 040)
and GMAT® Focus Edition Diagnostic Test 02 (gmat-focus-021 to 040).
"""

import json, os

BASE_DIR = '/Users/swapneshmhatre/Desktop/Buywisehub_website/mocktestvault.com'

# ==============================================================================
# 1. TOEFL® iBT Reading Diagnostic Test 02 (20 Questions: toefl-read-021 to 040)
# ==============================================================================

toefl_questions_set2 = [
    # --- Passage 1: Coral Biomineralization & Ocean Acidification (Qs 21–30) ---
    {
        "id": "toefl-read-021",
        "type": "mcq",
        "subtopic": "Factual Information (Passage 1: Coral Biomineralization)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'Scleractinian reef-building corals construct massive calcium carbonate skeletons through an intricate biomineralization process executed within the sub-calicoblastic extracellular space—an isolated microscopic compartment sealed between the coral's aboral ectoderm tissue and the preexisting mineral substratum. Within this protected microenvironment, specialized Ca2+-ATPase molecular proton pumps actively export hydrogen ions (H+) across the membrane, deliberately elevating the local internal pH up to 0.5–1.0 units above ambient seawater.'\n\nAccording to paragraph 1, what is the primary role of Ca2+-ATPase molecular pumps in coral biomineralization?",
        "options": [
            "They actively transport hydrogen ions out of the calcifying space to elevate the internal pH above ambient seawater levels.",
            "They absorb dissolved organic nitrogen directly from incoming pelagic currents.",
            "They dissolve older mineral layers to create space for softer coral polyp tissues.",
            "They pump excess carbonate ions into open ocean waters to maintain osmotic equilibrium."
        ],
        "answer": 0,
        "explanation": "The text explicitly states that 'specialized Ca2+-ATPase molecular proton pumps actively export hydrogen ions (H+) across the membrane, deliberately elevating the local internal pH up to 0.5–1.0 units above ambient seawater.' Option 0 directly reflects this.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Factual Information"
    },
    {
        "id": "toefl-read-022",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Passage 1: Coral Biomineralization)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'This physiological proton extrusion is indispensable for maintaining the aragonite saturation state (Ωarag) within the calicoblastic fluid at hyper-saturated levels, thereby facilitating spontaneous calcium carbonate crystallization.'\n\nThe word 'indispensable' in the passage is closest in meaning to:",
        "options": [
            "absolutely essential",
            "moderately helpful",
            "physically visible",
            "easily replaceable"
        ],
        "answer": 0,
        "explanation": "'Indispensable' means absolutely necessary or essential. In this physiological context, proton extrusion is essential for maintaining hyper-saturated aragonite levels.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Vocabulary in Context"
    },
    {
        "id": "toefl-read-023",
        "type": "mcq",
        "subtopic": "Negative Factual Information (Passage 1: Coral Biomineralization)",
        "difficulty": "Hard",
        "question": "Passage Excerpt: 'As anthropogenic carbon dioxide dissolves into surface seawater, it reacts with H2O to form carbonic acid (H2CO3), which dissociates into bicarbonate (HCO3-) and free protons (H+). These surplus hydrogen ions avidly react with naturally occurring carbonate ions (CO3 2-) to form additional bicarbonate, systematically depleting the seawater carbonate pool, suppressing the aragonite saturation state, and increasing the metabolic energy required for coral proton extrusion.'\n\nAccording to the passage, the absorption of anthropogenic CO2 into surface seawater causes all of the following chemical consequences EXCEPT:",
        "options": [
            "A dramatic surge in the concentration of free carbonate ions (CO3 2-)",
            "A systematic decline in the aragonite saturation state (Ωarag)",
            "An increase in the concentration of free hydrogen ions (H+)",
            "A heightened metabolic energy expenditure for corals pumping protons"
        ],
        "answer": 0,
        "explanation": "The passage explains that surplus hydrogen ions react with carbonate ions, thereby 'systematically depleting the seawater carbonate pool'. Thus, carbonate ions decrease, not increase: Option 0 is the correct EXCEPT choice.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Negative Factual Information"
    },
    {
        "id": "toefl-read-024",
        "type": "mcq",
        "subtopic": "Inference (Passage 1: Coral Biomineralization)",
        "difficulty": "Hard",
        "question": "Passage Excerpt: 'When the saturation state Ωarag drops below 1.0, seawater becomes chemically undersaturated with respect to aragonite, meaning calcium carbonate structures dissolve faster than they can precipitate. Even before this thermodynamic tipping point is reached, net reef accretion typically shifts to net structural erosion when Ωarag drops below 3.0 because bioeroding sponges, parrotfish, and macro-boring worms accelerate their mechanical and chemical destruction of the reef framework.'\n\nWhich of the following can be inferred from paragraph 3 about coral reefs in waters where Ωarag is between 1.5 and 2.5?",
        "options": [
            "Reefs can suffer a net loss of structural framework even though ambient water is technically still supersaturated with respect to aragonite.",
            "Living coral polyps completely cease biological calcification and die within hours.",
            "Bioeroding organisms like sponges and worms become inactive due to low pH.",
            "Aragonite crystals dissolve purely through thermodynamic undersaturation."
        ],
        "answer": 0,
        "explanation": "At Ωarag between 1.5 and 2.5, water is above 1.0 (so technically supersaturated), yet below 3.0, where 'net reef accretion typically shifts to net structural erosion' due to bioeroding organisms. Hence, reefs can suffer net loss despite technical supersaturation.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Inference"
    },
    {
        "id": "toefl-read-025",
        "type": "mcq",
        "subtopic": "Rhetorical Purpose (Passage 1: Coral Biomineralization)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'Unlike tropical zooxanthellate corals that thrive in sunlit shallows, azooxanthellate cold-water scleractinians, such as Lophelia pertusa, form extensive biogenic reefs in cold, dark bathyal depths between 200 and 1,000 meters. Because colder ocean water absorbs more atmospheric CO2 and has an inherently lower aragonite saturation horizon, Lophelia reefs serve as natural sentinels for the earliest biological impacts of ocean acidification.'\n\nWhy does the author discuss the cold-water coral species Lophelia pertusa?",
        "options": [
            "To highlight an organism that experiences the impacts of ocean acidification earlier due to the temperature dynamics of cold water.",
            "To demonstrate that tropical coral species could easily migrate to deep bathyal zones to escape warming waters.",
            "To argue that sunlight is harmful to most marine biomineralizing organisms.",
            "To prove that zooxanthellae are unnecessary for any form of marine life."
        ],
        "answer": 0,
        "explanation": "The text states that colder water absorbs more CO2 and has a lower aragonite saturation horizon, so Lophelia reefs 'serve as natural sentinels for the earliest biological impacts of ocean acidification': Option 0 accurately captures the author's rhetorical purpose.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Rhetorical Purpose"
    },
    {
        "id": "toefl-read-026",
        "type": "mcq",
        "subtopic": "Sentence Simplification (Passage 1: Coral Biomineralization)",
        "difficulty": "Hard",
        "question": "Which of the sentences below best expresses the essential information in the following highlighted sentence?\n\n'Although symbiotic zooxanthellae supply corals with up to 90 percent of their metabolic energy via photosynthetically fixed glycerol and glucose, excessive thermal stress destabilizes Photosystem II in the algal chloroplasts, generating toxic reactive oxygen species that compel the coral host to expel its endosymbionts in a catastrophic breakdown termed coral bleaching.'\n\nIncorrect choices change the meaning in important ways or leave out essential information.",
        "options": [
            "While algal endosymbionts normally provide most of a coral's energy, severe heat disrupts their photosynthetic machinery and produces toxins that force the coral to expel them, causing bleaching.",
            "Coral bleaching occurs when corals run out of glucose and glycerol, forcing zooxanthellae to consume the coral's outer tissues.",
            "Photosystem II prevents reactive oxygen species from damaging coral polyps during prolonged marine heatwaves.",
            "Symbiotic algae abandon their coral hosts voluntarily whenever ocean waters become too cold for photosynthesis."
        ],
        "answer": 0,
        "explanation": "Option 0 captures all essential points of the original sentence: zooxanthellae provide vital energy, but thermal stress damages Photosystem II, producing toxic reactive oxygen species that cause the host coral to expel them (bleaching).",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Sentence Simplification"
    },
    {
        "id": "toefl-read-027",
        "type": "mcq",
        "subtopic": "Factual Information (Passage 1: Coral Biomineralization)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'Following a bleaching event, a coral is not immediately dead, but it enters a state of severe starvation. If elevated sea surface temperatures subside within several weeks, surviving zooxanthellae can repopulate the gastrodermal tissues; however, if thermal anomalies persist, opportunistic cyanobacteria and fleshy turf algae rapidly smother the bare skeleton, permanently preventing coral larval recruitment.'\n\nAccording to the passage, what determines whether a bleached coral can recover?",
        "options": [
            "Whether elevated ocean temperatures decline quickly enough before turf algae smother the skeleton.",
            "The depth of the oceanic trench in which the coral colony is anchored.",
            "The total absence of marine herbivores such as grazing parrotfish.",
            "The immediate application of artificial nitrogen fertilizers by marine biologists."
        ],
        "answer": 0,
        "explanation": "The text states that if elevated temperatures subside within several weeks, surviving zooxanthellae can repopulate the tissues, but if anomalies persist, turf algae smother the skeleton permanently: Option 0.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Factual Information"
    },
    {
        "id": "toefl-read-028",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Passage 1: Coral Biomineralization)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'The synergistic combination of chronic ocean acidification and acute marine heatwaves exerts a deleterious impact on the structural integrity of tropical barrier reef systems worldwide.'\n\nThe word 'deleterious' in the passage is closest in meaning to:",
        "options": [
            "harmful and damaging",
            "insignificant",
            "beneficial",
            "temporary"
        ],
        "answer": 0,
        "explanation": "'Deleterious' means causing harm or damage. In this sentence, the synergistic stressors cause harmful, damaging impacts on structural integrity.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Vocabulary in Context"
    },
    {
        "id": "toefl-read-029",
        "type": "mcq",
        "subtopic": "Insert Text (Passage 1: Coral Biomineralization)",
        "difficulty": "Hard",
        "question": "Look at the four brackets [A], [B], [C], and [D] that indicate where the following sentence could be added to the passage:\n\n'Without this metabolic subsidy, the energetic cost of operating proton pumps in acidic water becomes unsustainable.'\n\nWhere would the sentence best fit?\n\n'Calcification and symbiosis are fundamentally coupled in tropical corals. [A] Under normal conditions, photosynthetic sugars fuel the high ATP demands of calicoblastic proton pumping. [B] When thermal stress induces bleaching, the coral loses access to this primary carbohydrate reserve. [C] Consequently, calcification rates plummet by up to 80 percent within days of symbiont loss. [D]'",
        "options": [
            "[A]",
            "[B]",
            "[C]",
            "[D]"
        ],
        "answer": 2,
        "explanation": "Position [C] follows the statement that bleaching deprives the coral of its primary carbohydrate reserve, making 'Without this metabolic subsidy...' logically coherent, which then causes calcification rates to plummet in sentence [D].",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Insert Text"
    },
    {
        "id": "toefl-read-030",
        "type": "mcq",
        "subtopic": "Prose Summary (Passage 1: Coral Biomineralization)",
        "difficulty": "Hard",
        "question": "An introductory sentence for a brief summary of the passage is provided below:\n\n'Scleractinian coral reefs face compounding ecological challenges from anthropogenic ocean acidification and rising sea temperatures.'\n\nWhich of the following statements best synthesizes the primary concepts presented in the passage?",
        "options": [
            "Corals build skeletons by actively pumping protons in a sealed sub-calicoblastic space, but declining ocean carbonate saturation and thermal bleaching synergistically undermine both biological calcification and skeletal survival.",
            "Ocean acidification is entirely offset by the photosynthetic activity of zooxanthellae, meaning corals are impervious to rising atmospheric CO2.",
            "Cold-water corals are immune to changing ocean chemistry because they do not rely on aragonite for skeleton construction.",
            "Coral reefs will completely dissolve before the year 2030 regardless of global greenhouse gas emissions."
        ],
        "answer": 0,
        "explanation": "Option 0 accurately synthesizes the full scope of the passage: the biological mechanism of proton pumping, the threat of carbonate depletion (acidification), and thermal stress (bleaching) undermining reef accretion.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Prose Summary"
    },

    # --- Passage 2: Neural Mechanisms of Working Memory & Executive Control (Qs 31–40) ---
    {
        "id": "toefl-read-031",
        "type": "mcq",
        "subtopic": "Factual Information (Passage 2: Working Memory)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'In her seminal neurophysiological investigations during the late twentieth century, Patricia Goldman-Rakic recorded single-neuron action potentials in non-human primates performing the oculomotor delayed-response task. She discovered that pyramidal neurons within the principal sulcus of the dorsolateral prefrontal cortex (dlPFC) exhibited sustained, tonic firing throughout a multi-second delay interval when no visual stimulus was present, bridged only by the animal's mental representation of the spatial target.'\n\nAccording to paragraph 1, what did Goldman-Rakic observe in dlPFC pyramidal neurons during delayed-response tasks?",
        "options": [
            "They maintained continuous, active firing during the delay period in the complete absence of external sensory cues.",
            "They ceased firing entirely until a novel visual reward appeared on screen.",
            "They fired exclusively when the animal was asleep to consolidate long-term motor memories.",
            "They were activated only when physical touch receptors on the animal's limbs were stimulated."
        ],
        "answer": 0,
        "explanation": "The text states that dlPFC pyramidal neurons 'exhibited sustained, tonic firing throughout a multi-second delay interval when no visual stimulus was present', maintaining the internal mental representation.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Factual Information"
    },
    {
        "id": "toefl-read-032",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Passage 2: Working Memory)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'Unlike passive sensory iconic memory which decays within hundreds of milliseconds, working memory is an active, ephemeral cognitive workspace that retains task-relevant representations against distracting interference.'\n\nThe word 'ephemeral' in the passage is closest in meaning to:",
        "options": [
            "short-lived and transient",
            "permanently enduring",
            "physically visible",
            "computationally flawed"
        ],
        "answer": 0,
        "explanation": "'Ephemeral' means lasting for a very short time; transient. Working memory retains representations temporarily for task execution rather than indefinitely.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Vocabulary in Context"
    },
    {
        "id": "toefl-read-033",
        "type": "mcq",
        "subtopic": "Inference (Passage 2: Working Memory)",
        "difficulty": "Hard",
        "question": "Passage Excerpt: 'In the multicomponent working memory model formulated by Baddeley and Hitch, verbal representations are actively refreshed through the phonological loop via sub-vocal rehearsal in Broca's area. When human participants are subjected to articulatory suppression—such as being required to repeat an irrelevant syllable ('the, the, the') out loud—their capacity to memorize printed verbal lists degrades sharply, whereas their ability to retain simultaneous visual-spatial patterns remains largely intact.'\n\nWhat can be inferred from the finding that articulatory suppression does not impair visual-spatial task performance?",
        "options": [
            "The phonological loop and the visuospatial sketchpad operate as distinct, modular subsystems with independent processing resources.",
            "Visual-spatial memory is located entirely within the vocal cords rather than the cerebral cortex.",
            "Human working memory has an unlimited total storage capacity for verbal information.",
            "Articulatory suppression permanently damages Broca's area."
        ],
        "answer": 0,
        "explanation": "Because articulatory suppression selectively disrupts verbal recall while leaving visuospatial retention intact, it demonstrates that verbal and visual-spatial memory depend on separate, modular subsystems with independent cognitive resources: Option 0.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Inference"
    },
    {
        "id": "toefl-read-034",
        "type": "mcq",
        "subtopic": "Negative Factual Information (Passage 2: Working Memory)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'The central executive component coordinates attentional focus, performs cognitive task-switching, inhibits prepotent automatic motor reflexes, and directs the episodic buffer to integrate multimodal sensory inputs into coherent chronological representations.'\n\nAccording to the passage, the central executive is responsible for all of the following functions EXCEPT:",
        "options": [
            "Directly synthesizing myelin sheaths along peripheral sensory nerves",
            "Inhibiting prepotent automatic motor reflexes",
            "Coordinating attentional focus between competing tasks",
            "Directing the integration of multimodal sensory streams"
        ],
        "answer": 0,
        "explanation": "The passage identifies attentional focus, task-switching, inhibiting prepotent reflexes, and multimodal integration as central executive functions. Synthesizing peripheral myelin is a cellular biological process, not an executive cognitive function: Option 0.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Negative Factual Information"
    },
    {
        "id": "toefl-read-035",
        "type": "mcq",
        "subtopic": "Rhetorical Purpose (Passage 2: Working Memory)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'Long-term potentiation (LTP) in the hippocampus solidifies memories by structurally remodeling dendritic spines and inserting AMPA receptors over hours or days. In contrast, the delay-period activity of working memory relies upon reverberatory recurrent microcircuits that persist solely through rapid synaptic feedback loops among prefrontal pyramidal neurons without requiring permanent morphological changes.'\n\nWhy does the author contrast working memory with long-term potentiation?",
        "options": [
            "To emphasize that working memory operates via dynamic electrical persistence rather than permanent anatomical remodeling.",
            "To argue that hippocampal memories are less accurate than prefrontal memories.",
            "To demonstrate that long-term memory formation consumes less cellular energy than working memory.",
            "To prove that the human brain does not possess the capacity for synaptic plasticity."
        ],
        "answer": 0,
        "explanation": "The author contrasts the two mechanisms to clarify that working memory relies on dynamic reverberatory electrical activity rather than enduring anatomical changes (like AMPA insertion or dendritic remodeling): Option 0.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Rhetorical Purpose"
    },
    {
        "id": "toefl-read-036",
        "type": "mcq",
        "subtopic": "Sentence Simplification (Passage 2: Working Memory)",
        "difficulty": "Hard",
        "question": "Which of the sentences below best expresses the essential information in the following highlighted sentence?\n\n'Rather than functioning as an insular storage receptacle, the dorsolateral prefrontal cortex exerts top-down modulatory bias over posterior sensory cortices, amplifying relevant visual or auditory features while suppressing irrelevant background distractors.'\n\nIncorrect choices change the meaning in important ways or leave out essential information.",
        "options": [
            "The dlPFC is not an isolated storage box; instead, it actively controls sensory areas by boosting important information and filtering out distractions.",
            "Posterior sensory cortices dictate which memories the prefrontal cortex is permitted to store.",
            "Sensory cortices suppress prefrontal activity whenever background distractions are present in the environment.",
            "The prefrontal cortex stores all sensory inputs indiscriminately without prioritizing relevant information."
        ],
        "answer": 0,
        "explanation": "Option 0 accurately captures the highlighted sentence's essential meaning: the dlPFC is not a passive storage box, but an active top-down controller that boosts relevant inputs and suppresses distractors in sensory cortices.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Sentence Simplification"
    },
    {
        "id": "toefl-read-037",
        "type": "mcq",
        "subtopic": "Factual Information (Passage 2: Working Memory)",
        "difficulty": "Hard",
        "question": "Passage Excerpt: 'Pharmacological investigations reveal an inverted-U dose-response curve governing dopamine modulation in prefrontal working memory. Moderate stimulation of dopamine D1 receptors sharpens the signal-to-noise ratio of delay-period firing by suppressing spontaneous background noise. However, excessive D1 receptor activation—such as during acute psychological stress—or deficient stimulation under sedation causes delay firing to collapse.'\n\nAccording to the passage, what effect does acute psychological stress have on prefrontal working memory circuits?",
        "options": [
            "It triggers excessive D1 receptor activation that collapses delay-period neuronal firing.",
            "It causes an immediate permanent loss of hippocampal dendritic spines.",
            "It converts working memory into indestructible long-term procedural habits.",
            "It completely halts the synthesis of dopamine throughout the brainstem."
        ],
        "answer": 0,
        "explanation": "The text states that 'excessive D1 receptor activation—such as during acute psychological stress... causes delay firing to collapse': Option 0.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Factual Information"
    },
    {
        "id": "toefl-read-038",
        "type": "mcq",
        "subtopic": "Vocabulary in Context (Passage 2: Working Memory)",
        "difficulty": "Medium",
        "question": "Passage Excerpt: 'By selectively engaging recurrent excitation through NMDA receptors, prefrontal networks exhibit robust resistance to intervening cognitive distractors.'\n\nThe word 'robust' in the passage is closest in meaning to:",
        "options": [
            "strong and resilient",
            "fragile",
            "unreliable",
            "sporadic"
        ],
        "answer": 0,
        "explanation": "'Robust' means vigorous, strong, and capable of withstanding adverse conditions. Here, prefrontal networks show strong, resilient resistance to distraction.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Vocabulary in Context"
    },
    {
        "id": "toefl-read-039",
        "type": "mcq",
        "subtopic": "Insert Text (Passage 2: Working Memory)",
        "difficulty": "Hard",
        "question": "Look at the four brackets [A], [B], [C], and [D] that indicate where the following sentence could be added to the passage:\n\n'In patients with frontal lobe lesions, this inhibitory control fails, resulting in stimulus-bound behaviors where every environmental cue compels an unthinking action.'\n\nWhere would the sentence best fit?\n\n'A defining hallmark of human executive control is the capacity to suppress reflexive responses in favor of goal-directed actions. [A] This inhibition is mediated by projections from the inferior frontal gyrus to the subthalamic nucleus. [B] Patients with intact prefrontal cortices easily resist reaching for objects placed in front of them if instructed not to do so. [C] Consequently, studying executive dysfunction illuminates how the healthy brain decouples thought from immediate sensory reflex. [D]'",
        "options": [
            "[A]",
            "[B]",
            "[C]",
            "[D]"
        ],
        "answer": 2,
        "explanation": "Position [C] follows the description of healthy patients resisting impulses, setting up the exact counterexample: 'In patients with frontal lobe lesions, this inhibitory control fails...', which leads directly into the concluding observation [D].",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Insert Text"
    },
    {
        "id": "toefl-read-040",
        "type": "mcq",
        "subtopic": "Prose Summary (Passage 2: Working Memory)",
        "difficulty": "Hard",
        "question": "An introductory sentence for a brief summary of the passage is provided below:\n\n'Working memory operates as an active, multicomponent system supported by specialized prefrontal microcircuits.'\n\nWhich of the following statements best synthesizes the core findings detailed in the passage?",
        "options": [
            "Working memory relies on persistent reverberatory firing in dlPFC pyramidal microcircuits, modulated by an optimal inverted-U dopamine balance and exerting top-down control over sensory modalities.",
            "Working memory is identical in anatomical structure and temporal duration to long-term synaptic potentiation in the hippocampus.",
            "Human executive function is located entirely within Broca's area without involving prefrontal cortical networks.",
            "Dopamine D1 receptor antagonists permanently cure all forms of cognitive distractibility."
        ],
        "answer": 0,
        "explanation": "Option 0 synthesizes the key themes: persistent firing in dlPFC, inverted-U dopamine modulation, and top-down control over sensory cortices.",
        "citation": "ETS TOEFL® iBT Reading Section — Question Type: Prose Summary"
    }
]

out_toefl_set2 = os.path.join(BASE_DIR, 'data/global/toefl/toefl_reading_set2.json')
with open(out_toefl_set2, 'w', encoding='utf-8') as f:
    json.dump({"questions": toefl_questions_set2}, f, indent=2, ensure_ascii=False)
print(f"Generated {len(toefl_questions_set2)} TOEFL reading questions at {out_toefl_set2}!")

# ==============================================================================
# 2. GMAT® Focus Edition Diagnostic Test 02 (20 Questions: gmat-focus-021 to 040)
# ==============================================================================

gmat_questions_set2 = [
    # --- Data Insights: Table Analysis & Graphical Interpretation (Qs 21–26) ---
    {
        "id": "gmat-focus-021",
        "type": "mcq",
        "subtopic": "Table Analysis (Data Insights: Cloud Data Centers)",
        "difficulty": "Medium",
        "question": "A global infrastructure manager evaluates 5 cloud data centers based on operational metrics:\n\n| Facility | Power Usage Eff (PUE) | Renewable Energy % | Compute Uptime | Cooling Water (kL/day) |\n| :--- | :--- | :--- | :--- | :--- |\n| Dublin-1 | 1.18 | 85% | 99.98% | 140 |\n| Frankfurt-2 | 1.25 | 92% | 99.95% | 180 |\n| Virginia-3 | 1.14 | 70% | 99.99% | 220 |\n| Singapore-4 | 1.32 | 60% | 99.92% | 310 |\n| Oregon-5 | 1.12 | 95% | 99.99% | 90 |\n\nQuestion: Which facilities satisfy the dual criteria: Power Usage Effectiveness (PUE) strictly below 1.20 AND Renewable Energy % strictly above 80%?",
        "options": [
            "Dublin-1 and Oregon-5 only",
            "Oregon-5 only",
            "Dublin-1, Virginia-3, and Oregon-5",
            "Frankfurt-2 and Oregon-5",
            "Dublin-1 only"
        ],
        "answer": 0,
        "explanation": "Criterion 1 (PUE < 1.20): Dublin-1 (1.18), Virginia-3 (1.14), Oregon-5 (1.12).\nCriterion 2 (Renewable Energy > 80%): Dublin-1 (85%), Frankfurt-2 (92%), Oregon-5 (95%).\nIntersection of both criteria: Dublin-1 (1.18 < 1.20 and 85% > 80%) and Oregon-5 (1.12 < 1.20 and 95% > 80%). Virginia-3 fails renewable (70% < 80%). Frankfurt-2 fails PUE (1.25 > 1.20). Singapore-4 fails both.\nBoth Dublin-1 and Oregon-5 satisfy: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Data Insights: Table Analysis"
    },
    {
        "id": "gmat-focus-022",
        "type": "mcq",
        "subtopic": "Table Analysis (Data Insights: Cloud Data Centers)",
        "difficulty": "Hard",
        "question": "Refer to the data center table above:\n\nIf Frankfurt-2 upgrades its cooling chillers to reduce its daily cooling water consumption by 25% and improves its PUE by 0.05 units, what will be its revised cooling water consumption and revised PUE?",
        "options": [
            "Cooling Water = 135 kL/day; PUE = 1.20",
            "Cooling Water = 140 kL/day; PUE = 1.20",
            "Cooling Water = 135 kL/day; PUE = 1.22",
            "Cooling Water = 150 kL/day; PUE = 1.20",
            "Cooling Water = 130 kL/day; PUE = 1.18"
        ],
        "answer": 0,
        "explanation": "1. Frankfurt-2 baseline cooling water = 180 kL/day. A 25% reduction = 180 * (1 - 0.25) = 180 * 0.75 = 135 kL/day.\n2. Frankfurt-2 baseline PUE = 1.25. An improvement of 0.05 units = 1.25 - 0.05 = 1.20.\nRevised cooling water = 135 kL/day and PUE = 1.20: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Data Insights: Table Analysis"
    },
    {
        "id": "gmat-focus-023",
        "type": "mcq",
        "subtopic": "Graphical Interpretation (Data Insights: Logarithmic Retention Curve)",
        "difficulty": "Hard",
        "question": "A subscription mobile app tracks user retention $R(t)$ (as a percentage of original signups) at month $t$ (where $1 \\le t \\le 12$) modeled by the logarithmic curve:\n$$R(t) = 90 - 25 \\cdot \\ln(t)$$\n\nUsing the approximation $\\ln(2) \\approx 0.693$ and $\\ln(4) = 2 \\cdot \\ln(2) \\approx 1.386$:\nQuestion: What is the approximate difference in user retention percentage between Month 1 and Month 4?",
        "options": [
            "34.7 percentage points",
            "25.0 percentage points",
            "17.3 percentage points",
            "45.0 percentage points",
            "28.6 percentage points"
        ],
        "answer": 0,
        "explanation": "1. At t = 1: R(1) = 90 - 25 * ln(1) = 90 - 25(0) = 90%.\n2. At t = 4: R(4) = 90 - 25 * ln(4) ≈ 90 - 25(1.386) = 90 - 34.65 = 55.35%.\n3. Difference = R(1) - R(4) = 90 - 55.35 = 34.65 percentage points ≈ 34.7 percentage points: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Data Insights: Graphical Interpretation"
    },
    {
        "id": "gmat-focus-024",
        "type": "mcq",
        "subtopic": "Graphical Interpretation (Data Insights: Scatter Plot Variance)",
        "difficulty": "Medium",
        "question": "An analytics firm measures customer lifetime value ($LTV$, in thousands of dollars) versus customer acquisition cost ($CAC$, in hundreds of dollars) across 5 marketing channels: (CAC, LTV) = (2, 8), (4, 14), (6, 18), (8, 22), (10, 24).\n\nQuestion: Which consecutive CAC interval exhibits the highest ratio of incremental LTV gained per unit of additional CAC expended?",
        "options": [
            "CAC from 2 to 4 (ΔCAC = 2)",
            "CAC from 4 to 6 (ΔCAC = 2)",
            "CAC from 6 to 8 (ΔCAC = 2)",
            "CAC from 8 to 10 (ΔCAC = 2)",
            "All intervals yield identical incremental ratios"
        ],
        "answer": 0,
        "explanation": "Incremental ratio = ΔLTV / ΔCAC (where ΔCAC = 2 hundreds of dollars for all consecutive steps):\n- From 2 to 4: ΔLTV = 14 - 8 = 6. Ratio = 6 / 2 = 3.0\n- From 4 to 6: ΔLTV = 18 - 14 = 4. Ratio = 4 / 2 = 2.0\n- From 6 to 8: ΔLTV = 22 - 18 = 4. Ratio = 4 / 2 = 2.0\n- From 8 to 10: ΔLTV = 24 - 22 = 2. Ratio = 2 / 2 = 1.0\nThe highest incremental ratio is 3.0, achieved on the interval from 2 to 4: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Data Insights: Graphical Interpretation"
    },
    {
        "id": "gmat-focus-025",
        "type": "mcq",
        "subtopic": "Multi-Source Reasoning (Data Insights: Convertible Note vs SAFE)",
        "difficulty": "Hard",
        "question": "Tab 1 (Investment Instrument Specs):\n• Option A (Convertible Note): $1,000,000 investment with a 20% conversion discount, a $10,000,000 valuation cap, and 6% simple annual interest accrued over 1 year.\n• Option B (Post-Money SAFE): $1,000,000 investment with no interest, no discount, and an $8,000,000 post-money valuation cap.\n\nTab 2 (Series A Priced Round Trigger):\nOne year later, the company raises a Series A round at a pre-money valuation of $15,000,000 with a share price of $10.00.\n\nQuestion: Under Option A, what is the effective conversion price per share after accounting for 1 year of 6% simple interest on the $1,000,000 principal at the $10,000,000 valuation cap?",
        "options": [
            "$6.67 per share",
            "$8.00 per share",
            "$7.50 per share",
            "$5.33 per share",
            "$10.00 per share"
        ],
        "answer": 0,
        "explanation": "Conversion Price under Option A is determined by the lower of the discount price or the cap price:\n1. 20% discount price = $10.00 * (1 - 0.20) = $8.00.\n2. Valuation cap price = (Valuation Cap / Series A Valuation) * Series A Share Price = ($10,000,000 / $15,000,000) * $10.00 = (2/3) * $10.00 ≈ $6.67 per share.\n3. The investor gets the lower price: min($8.00, $6.67) = $6.67 per share.\n(The 6% interest increases the total note conversion amount to $1,060,000, but does not alter the conversion price per share): Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Data Insights: Multi-Source Reasoning"
    },
    {
        "id": "gmat-focus-026",
        "type": "mcq",
        "subtopic": "Two-Part Analysis (Data Insights: Pricing & Contribution Margin)",
        "difficulty": "Hard",
        "question": "A SaaS startup currently sells an annual software subscription for $P = $600 with variable server hosting costs of $V = $120 per user. Next year, the team plans to adjust price $P$ and invest in infrastructure to change variable cost $V$.\n\nIf the contribution margin ratio is defined as:\n$$\\text{Margin Ratio} = \\frac{P - V}{P}$$\n\nWhich pair of values for $(P, V)$ will result in a contribution margin ratio of exactly 85%?",
        "options": [
            "P = $800, V = $120",
            "P = $700, V = $150",
            "P = $900, V = $180",
            "P = $1,000, V = $200",
            "P = $750, V = $125"
        ],
        "answer": 0,
        "explanation": "Margin Ratio = (P - V) / P = 1 - (V / P) = 0.85.\nTherefore, V / P = 1 - 0.85 = 0.15 = 15%.\nLet's test Option 0: P = $800, V = $120. V / P = 120 / 800 = 12 / 80 = 3 / 20 = 0.15 (15%). Margin ratio = (800 - 120)/800 = 680/800 = 85%. Exactly 85%: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Data Insights: Two-Part Analysis"
    },

    # --- Data Insights / Quantitative: Data Sufficiency (Qs 27–32) ---
    {
        "id": "gmat-focus-027",
        "type": "mcq",
        "subtopic": "Data Sufficiency (Quantitative: Prime Numbers)",
        "difficulty": "Hard",
        "question": "Is the positive integer $k$ a prime number?\n\nStatement (1): $k$ is an odd number between 20 and 30.\nStatement (2): $k + 2$ and $k + 4$ are both prime numbers.\n\nWhich of the following describes the sufficiency of the statements?",
        "options": [
            "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
            "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
            "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
            "EACH statement ALONE is sufficient.",
            "Statements (1) and (2) TOGETHER are NOT sufficient."
        ],
        "answer": 0,
        "explanation": "- Statement (1): Odd integers between 20 and 30 are {21, 23, 25, 27, 29}. 23 and 29 are prime, but 21, 25, 27 are composite. Insufficient.\n- Statement (2): k, k+2, k+4 are prime triplets. For any integer k, among k, k+2, k+4, exactly one must be divisible by 3. Since the only prime divisible by 3 is 3 itself, the only set of prime triplets is {3, 5, 7}, which forces k = 3. Since k = 3 is uniquely determined and prime, Statement (2) alone is sufficient!\nStatement (2) ALONE is sufficient: Option 0 (Choice B in GMAC).",
        "citation": "Official GMAC GMAT Focus Edition — Data Sufficiency Standard"
    },
    {
        "id": "gmat-focus-028",
        "type": "mcq",
        "subtopic": "Data Sufficiency (Quantitative: Absolute Values & Inequalities)",
        "difficulty": "Hard",
        "question": "Is $|x - 3| < 5$?\n\nStatement (1): $-1 < x < 7$\nStatement (2): $x^2 - 6x - 7 < 0$\n\nWhich of the following describes the sufficiency?",
        "options": [
            "EACH statement ALONE is sufficient.",
            "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
            "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
            "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
            "Statements (1) and (2) TOGETHER are NOT sufficient."
        ],
        "answer": 0,
        "explanation": "Target question: |x - 3| < 5 <=> -5 < x - 3 < 5 <=> -2 < x < 8.\n- Statement (1): -1 < x < 7. Every x in (-1, 7) lies strictly inside the target interval (-2, 8). Hence |x - 3| < 5 is definitely TRUE. Sufficient alone!\n- Statement (2): x^2 - 6x - 7 < 0 <=> (x - 7)(x + 1) < 0 <=> -1 < x < 7. This is the exact same interval as Statement (1)! Hence Statement (2) is also sufficient alone!\nEach statement ALONE is sufficient: Option 0 (Choice D in GMAC).",
        "citation": "Official GMAC GMAT Focus Edition — Data Sufficiency Standard"
    },
    {
        "id": "gmat-focus-029",
        "type": "mcq",
        "subtopic": "Data Sufficiency (Quantitative: Circles & Tangents)",
        "difficulty": "Hard",
        "question": "What is the circumference of circle $C$ in the $xy$-coordinate plane?\n\nStatement (1): Circle $C$ is tangent to both the $x$-axis and the $y$-axis.\nStatement (2): The area of circle $C$ is $49\\pi$.\n\nWhich of the following describes the sufficiency?",
        "options": [
            "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
            "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
            "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
            "EACH statement ALONE is sufficient.",
            "Statements (1) and (2) TOGETHER are NOT sufficient."
        ],
        "answer": 0,
        "explanation": "- Statement (1): A circle tangent to both axes can have any radius r > 0. The circumference 2πr cannot be determined without knowing r. Insufficient.\n- Statement (2): Area = πr^2 = 49π => r^2 = 49 => r = 7 (since radius > 0). Circumference = 2π(7) = 14π. Uniquely determined: Sufficient alone!\nStatement (2) ALONE is sufficient: Option 0 (Choice B in GMAC).",
        "citation": "Official GMAC GMAT Focus Edition — Data Sufficiency Standard"
    },
    {
        "id": "gmat-focus-030",
        "type": "mcq",
        "subtopic": "Data Sufficiency (Quantitative: Probability)",
        "difficulty": "Hard",
        "question": "What is the probability that both Event A and Event B occur, denoted $P(A \\cap B)$?\n\nStatement (1): $P(A) = 0.6$ and $P(B) = 0.5$\nStatement (2): Events A and B are independent events.\n\nWhich of the following describes the sufficiency?",
        "options": [
            "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
            "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
            "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
            "EACH statement ALONE is sufficient.",
            "Statements (1) and (2) TOGETHER are NOT sufficient."
        ],
        "answer": 0,
        "explanation": "- Statement (1): P(A) = 0.6 and P(B) = 0.5. Without knowing if the events are independent or mutually exclusive, P(A ∩ B) can range anywhere from 0.1 to 0.5. Insufficient.\n- Statement (2): Events are independent (meaning P(A ∩ B) = P(A) * P(B)), but their individual probabilities are unknown. Insufficient.\n- Together: From (2), P(A ∩ B) = P(A) * P(B). From (1), P(A) = 0.6 and P(B) = 0.5. P(A ∩ B) = 0.6 * 0.5 = 0.30. Uniquely determined!\nTogether they are sufficient: Option 0 (Choice C in GMAC).",
        "citation": "Official GMAC GMAT Focus Edition — Data Sufficiency Standard"
    },
    {
        "id": "gmat-focus-031",
        "type": "mcq",
        "subtopic": "Data Sufficiency (Quantitative: Work & Rates)",
        "difficulty": "Hard",
        "question": "Can Worker X and Worker Y together complete a certain warehouse task in less than 4 hours?\n\nStatement (1): Working alone, Worker X can complete the task in 6 hours.\nStatement (2): Working alone, Worker Y can complete the task in 10 hours.\n\nWhich of the following describes the sufficiency?",
        "options": [
            "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
            "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
            "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
            "EACH statement ALONE is sufficient.",
            "Statements (1) and (2) TOGETHER are NOT sufficient."
        ],
        "answer": 0,
        "explanation": "- Statement (1): Worker X takes 6 hours. If Worker Y took 1 hour, together they'd finish in < 4 hours. If Y took 100 hours, together they'd take ~5.6 hours (> 4 hours). Insufficient.\n- Statement (2): Worker Y takes 10 hours. Similarly, the time depends on Worker X's rate. Insufficient.\n- Together: Combined rate = 1/6 + 1/10 = (5 + 3)/30 = 8/30 = 4/15 task/hour. Time together = 15/4 = 3.75 hours (3 hours 45 mins). Since 3.75 < 4, the answer is definitively YES. Sufficient together!\nTogether they are sufficient: Option 0 (Choice C in GMAC).",
        "citation": "Official GMAC GMAT Focus Edition — Data Sufficiency Standard"
    },
    {
        "id": "gmat-focus-032",
        "type": "mcq",
        "subtopic": "Data Sufficiency (Quantitative: Overlapping Sets)",
        "difficulty": "Hard",
        "question": "In a group of 150 investors, how many invest in BOTH equities and real estate?\n\nStatement (1): 90 investors invest in equities and 70 invest in real estate.\nStatement (2): 20 investors invest in neither equities nor real estate.\n\nWhich of the following describes the sufficiency?",
        "options": [
            "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
            "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
            "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
            "EACH statement ALONE is sufficient.",
            "Statements (1) and (2) TOGETHER are NOT sufficient."
        ],
        "answer": 0,
        "explanation": "Total = 150. By set theory: Total = Equities + RealEstate - Both + Neither.\n150 = Equities + RealEstate - Both + Neither.\n- Statement (1): Equities = 90, RealEstate = 70. Without knowing 'Neither', 'Both' cannot be solved. Insufficient.\n- Statement (2): Neither = 20. Without individual counts, 'Both' cannot be solved. Insufficient.\n- Together: 150 = 90 + 70 - Both + 20 => 150 = 180 - Both => Both = 180 - 150 = 30. Uniquely determined!\nTogether they are sufficient: Option 0 (Choice C in GMAC).",
        "citation": "Official GMAC GMAT Focus Edition — Data Sufficiency Standard"
    },

    # --- Quantitative Problem Solving (Qs 33–40) ---
    {
        "id": "gmat-focus-033",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Permutations with Restrictions)",
        "difficulty": "Hard",
        "question": "In how many distinct ways can 5 executives and 3 board observers be seated in a row of 8 chairs if NO two board observers may sit in adjacent chairs?",
        "options": [
            "14,400",
            "12,000",
            "7,200",
            "20,160",
            "28,800"
        ],
        "answer": 0,
        "explanation": "Use the 'gap method':\n1. Arrange the 5 executives in a row: 5! = 120 ways.\n2. The 5 executives create 6 available spaces (gaps) where the observers can sit (including the two ends): _ E1 _ E2 _ E3 _ E4 _ E5 _\n3. To ensure no two observers sit adjacent, choose 3 of these 6 gaps for the observers and arrange them: P(6, 3) = 6 * 5 * 4 = 120 ways.\n4. Total arrangements = 5! * P(6, 3) = 120 * 120 = 14,400 ways: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Combinatorics"
    },
    {
        "id": "gmat-focus-034",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Speed, Distance & Average Speed)",
        "difficulty": "Medium",
        "question": "A courier drives from City A to City B at an average speed of 60 miles per hour and returns along the exact same route at an average speed of 40 miles per hour. What is the courier's average speed for the entire round trip?",
        "options": [
            "48 mph",
            "50 mph",
            "45 mph",
            "52 mph",
            "46 mph"
        ],
        "answer": 0,
        "explanation": "Average speed for equal distances is the harmonic mean: (2 * s1 * s2) / (s1 + s2).\nAverage Speed = (2 * 60 * 40) / (60 + 40) = 4800 / 100 = 48 mph.\n(Note: The arithmetic mean 50 mph is an incorrect trap answer because more time is spent traveling at the slower speed): Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Rates & Speed"
    },
    {
        "id": "gmat-focus-035",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Compound vs Simple Interest)",
        "difficulty": "Hard",
        "question": "The difference between the compound interest (compounded annually) and the simple interest on a principal sum $P$ invested for 2 years at an annual interest rate of $r\\%$ is exactly $72. If $r = 12\\%$, what is the principal sum $P$?",
        "options": [
            "$5,000",
            "$6,000",
            "$4,500",
            "$7,200",
            "$5,500"
        ],
        "answer": 0,
        "explanation": "For 2 years, Difference = P * (r / 100)^2.\n$72 = P * (12 / 100)^2\n$72 = P * (144 / 10,000)\nP = (72 * 10,000) / 144\nP = 10,000 / 2 = $5,000.\nThe principal is $5,000: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Financial Math"
    },
    {
        "id": "gmat-focus-036",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Modular Arithmetic & Units Digits)",
        "difficulty": "Hard",
        "question": "What is the units digit of the integer expression $7^{85} + 3^{67}$?",
        "options": [
            "4",
            "6",
            "8",
            "2",
            "0"
        ],
        "answer": 0,
        "explanation": "1. Powers of 7 cycle in units digits with period 4: 7^1 -> 7, 7^2 -> 9, 7^3 -> 3, 7^4 -> 1.\n85 = 4 * 21 + 1 (remainder 1), so 7^85 has units digit 7.\n2. Powers of 3 cycle in units digits with period 4: 3^1 -> 3, 3^2 -> 9, 3^3 -> 7, 3^4 -> 1.\n67 = 4 * 16 + 3 (remainder 3), so 3^67 has units digit 7.\n3. Sum of units digits = 7 + 7 = 14 => units digit is 4: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Number Theory"
    },
    {
        "id": "gmat-focus-037",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Algebraic Identities)",
        "difficulty": "Medium",
        "question": "If real numbers $x, y, z$ satisfy $x + y + z = 15$ and $x^2 + y^2 + z^2 = 83$, what is the value of the cross-product sum $xy + yz + zx$?",
        "options": [
            "71",
            "68",
            "74",
            "80",
            "65"
        ],
        "answer": 0,
        "explanation": "Use the standard algebraic expansion:\n(x + y + z)^2 = x^2 + y^2 + z^2 + 2(xy + yz + zx)\n15^2 = 83 + 2(xy + yz + zx)\n225 = 83 + 2(xy + yz + zx)\n2(xy + yz + zx) = 225 - 83 = 142\nxy + yz + zx = 142 / 2 = 71: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Algebra"
    },
    {
        "id": "gmat-focus-038",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Successive Mixture Dilution)",
        "difficulty": "Hard",
        "question": "A container initially contains 80 liters of pure ethanol. Exactly 20 liters of ethanol are removed and replaced with 20 liters of water. After the mixture is thoroughly stirred, 20 liters of the mixture are removed and replaced with 20 liters of water. What is the final volume of pure ethanol remaining in the container?",
        "options": [
            "45 liters",
            "40 liters",
            "48 liters",
            "50 liters",
            "36 liters"
        ],
        "answer": 0,
        "explanation": "Removal fraction f = 20 / 80 = 1/4 = 0.25 of the total volume each time.\nAfter each replacement, the remaining fraction of original substance is (1 - f) = 1 - 1/4 = 3/4.\nAfter 2 successive replacements:\nFinal ethanol = Initial * (1 - f)^2 = 80 * (3/4)^2 = 80 * (9 / 16) = 5 * 9 = 45 liters: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Mixtures"
    },
    {
        "id": "gmat-focus-039",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Geometry & Incircle)",
        "difficulty": "Hard",
        "question": "In right-angled triangle $ABC$ with right angle at $B$, the hypotenuse $AC$ has length 25 and the inradius of the incircle is $r = 4$. What is the perimeter of triangle $ABC$?",
        "options": [
            "58",
            "60",
            "56",
            "64",
            "54"
        ],
        "answer": 0,
        "explanation": "In any right triangle with legs a, b and hypotenuse c:\n1. Inradius r = (a + b - c) / 2.\n2. 4 = (a + b - 25) / 2\n8 = a + b - 25 => a + b = 33.\n3. Perimeter = a + b + c = 33 + 25 = 58.\n(Legs are 20 and 13? Let's check: 20^2 + 13^2 = 400 + 169 = 569 != 625. Wait, if legs are a and b, a+b=33, a^2+b^2=625. (a+b)^2 = a^2+b^2 + 2ab => 33^2 = 1089 = 625 + 2ab => 2ab = 464 => ab = 232. Discriminant of t^2 - 33t + 232 = 0 is 33^2 - 4(232) = 1089 - 928 = 161 > 0, so real legs exist! Perimeter = 33 + 25 = 58): Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Geometry"
    },
    {
        "id": "gmat-focus-040",
        "type": "mcq",
        "subtopic": "Problem Solving (Quantitative: Telescoping Series)",
        "difficulty": "Medium",
        "question": "What is the value of the finite sum:\n$$S = \\sum_{k=1}^{99} \\frac{1}{k(k+1)} = \\frac{1}{1 \\cdot 2} + \\frac{1}{2 \\cdot 3} + \\frac{1}{3 \\cdot 4} + \\dots + \\frac{1}{99 \\cdot 100}$$",
        "options": [
            "99 / 100 (0.99)",
            "100 / 99",
            "1 / 100 (0.01)",
            "98 / 99",
            "1.00"
        ],
        "answer": 0,
        "explanation": "Use partial fraction decomposition: 1 / (k(k+1)) = 1/k - 1/(k+1).\nThe sum telescopes:\nS = (1/1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ... + (1/99 - 1/100)\nAll intermediate terms cancel out:\nS = 1 - 1/100 = 99 / 100 = 0.99: Option 0.",
        "citation": "Official GMAC GMAT Focus Edition — Quantitative: Sequences & Series"
    }
]

out_gmat_set2 = os.path.join(BASE_DIR, 'data/global/gmat/gmat_focus_set2.json')
with open(out_gmat_set2, 'w', encoding='utf-8') as f:
    json.dump({"questions": gmat_questions_set2}, f, indent=2, ensure_ascii=False)
print(f"Generated {len(gmat_questions_set2)} GMAT Focus questions at {out_gmat_set2}!")
