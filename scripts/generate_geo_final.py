#!/usr/bin/env python3
"""
Generates Geography Ch 11 (Manufacturing Industries) Sets 2 & 3
and Ch 12 (Lifelines of National Economy) Sets 1, 2, 3.
Total: 5 sets = 100 questions.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# -----------------------------------------------------------------------------
# CH 11 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch11_set2 = [
  {
    "id": "cbse10-sst-geo-ch11-s2-001",
    "type": "mcq",
    "subtopic": "Steel Raw Material Ratio",
    "difficulty": "Hard",
    "question": "What is the approximate ideal ratio of iron ore, coking coal, and limestone required to produce steel in an integrated blast furnace?",
    "options": ["4 : 2 : 1", "2 : 1 : 4", "1 : 2 : 4", "4 : 1 : 2"],
    "answer": 0,
    "explanation": "Iron ore, coking coal, and limestone are required in roughly the ratio of 4 : 2 : 1. Some quantity of manganese is also required to harden the steel.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-002",
    "type": "mcq",
    "subtopic": "Mini vs Integrated Steel Plant",
    "difficulty": "Medium",
    "question": "Which of the following statements correctly distinguishes Mini Steel Plants from Integrated Steel Plants?",
    "options": [
      "Mini steel plants use electric furnaces, sponge iron, and steel scrap, producing mild and alloy steel of specified sizes",
      "Mini steel plants handle everything from raw iron ore melting to steel shaping in one complex",
      "Integrated steel plants operate exclusively in rural villages without electricity",
      "Mini steel plants can only manufacture agricultural ploughs"
    ],
    "answer": 0,
    "explanation": "Mini steel plants are smaller, have electric furnaces, use steel scrap and sponge iron. They have re-rollers that produce mild and alloy steel of given specifications, whereas integrated steel plants handle raw material handling, blast furnace melting, and rolling in one large complex.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-003",
    "type": "mcq",
    "subtopic": "Chemical Industry Share",
    "difficulty": "Medium",
    "question": "Which branch of the chemical industry produces heavy chemicals like sulphuric acid (used for fertilisers, synthetic fibres, plastics, paints) and soda ash (used for glass, soap, paper)?",
    "options": ["Inorganic chemical industry", "Organic petrochemical industry", "Pharmaceutical biotechnology", "Fine perfumes industry"],
    "answer": 0,
    "explanation": "Inorganic chemicals include sulphuric acid (used to manufacture fertilisers, synthetic fibres, plastics, adhesives, paints, dye stuffs), nitric acid, alkalies, soda ash (used to make glass, soaps and detergents, paper) and caustic soda.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.3"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-004",
    "type": "mcq",
    "subtopic": "Organic Chemicals Raw Material",
    "difficulty": "Medium",
    "question": "Organic chemicals include petrochemicals, which are used for manufacturing synthetic fibres, synthetic rubber, plastics, and pharmaceuticals. Where are organic chemical plants usually located?",
    "options": [
      "Near oil refineries or petrochemical complexes",
      "Exclusively on river banks in the Himalayas",
      "Near limestone quarries in dry plateaus",
      "Only in port cities that export iron ore"
    ],
    "answer": 0,
    "explanation": "Organic chemicals include petrochemicals, which are used for manufacturing synthetic fibres, synthetic rubber, plastics, dye-stuffs, and pharmaceuticals. Organic chemical plants are located near oil refineries or petrochemical plants.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.3"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-005",
    "type": "mcq",
    "subtopic": "Fertiliser Industry Raw Material Dependency",
    "difficulty": "Medium",
    "question": "India is entirely dependent on imports for which of the following essential fertiliser nutrients, as the country does not have commercially usable reserves?",
    "options": ["Potash (Potassium)", "Nitrogen (Urea)", "Phosphorus (Rock phosphate)", "Ammonium sulphate"],
    "answer": 0,
    "explanation": "India is the third largest producer of nitrogenous fertilisers. However, India does not have any reserves of commercially usable potash or potassium compounds in any form, making India completely dependent on imports for potash.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.4"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-006",
    "type": "mcq",
    "subtopic": "Automobile Industry Growth Post-1991",
    "difficulty": "Easy",
    "question": "What primary economic catalyst led to the rapid, healthy growth and technological upgradation of the Indian automobile industry?",
    "options": [
      "Liberalisation and the entry of new global contemporary models post-1991",
      "Total ban on private vehicle registrations",
      "Mandatory usage of horse carriages in metropolitan areas",
      "Free allocation of steel to luxury car manufacturers"
    ],
    "answer": 0,
    "explanation": "The coming in of new and contemporary models stimulated the demand for vehicles in the market, which led to the healthy growth of the industry after the liberalisation policy of 1991.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.5"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-007",
    "type": "mcq",
    "subtopic": "Information Technology Employment",
    "difficulty": "Easy",
    "question": "A major encouraging impact of the Information Technology and Electronics industry in India is that:",
    "options": [
      "A continuing large proportion (over 30%) of the workforce employed in this sector are women",
      "It requires no electrical power or telecommunication infrastructure",
      "It operates exclusively through barter exchange",
      "It has replaced agriculture as India's sole export product"
    ],
    "answer": 0,
    "explanation": "A major impact of this industry has been on employment generation. It is encouraging to know that 30 percent of the people employed in this sector are women. The continuing growth in the hardware and software is the key to the success of IT industry in India.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.6"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-008",
    "type": "mcq",
    "subtopic": "BPO & Foreign Exchange",
    "difficulty": "Easy",
    "question": "BPO industry has emerged as a major foreign exchange earner for India. BPO stands for:",
    "options": [
      "Business Process Outsourcing",
      "Basic Production Output",
      "Board of Petroleum Operations",
      "Broadband Protocol Organisation"
    ],
    "answer": 0,
    "explanation": "Business Process Outsourcing (BPO) sector has become a major foreign exchange earner in India because of its fast-growing business and call-centre operations.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.6"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-009",
    "type": "mcq",
    "subtopic": "Air Pollution Particulate Matter",
    "difficulty": "Medium",
    "question": "Particulate matter in the air emitted by chemical, metallurgical, and brick kiln industries can be reduced by fitting smoke stacks with:",
    "options": [
      "Electrostatic precipitators, fabric filters, scrubbers, and inertial separators",
      "Cooling towers that spray raw river water",
      "Diesel-powered exhaust blowers",
      "Lead-lined atmospheric chimneys"
    ],
    "answer": 0,
    "explanation": "Particulate matter in the air can be reduced by fitting smoke stacks to factories with electrostatic precipitators, fabric filters, scrubbers and inertial separators. Smoke can also be reduced by using oil or gas instead of coal.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-010",
    "type": "mcq",
    "subtopic": "Noise Pollution Control",
    "difficulty": "Easy",
    "question": "Industrial machinery and generators that cause high noise levels leading to hearing impairment and hypertension can be mitigated by:",
    "options": [
      "Fitting silencers and redesigning machinery to enhance acoustic energy efficiency",
      "Operating machines only during peak monsoon rainstorms",
      "Increasing the operating speed of vibrating un-lubricated gears",
      "Replacing electric generators with two-stroke petrol motors"
    ],
    "answer": 0,
    "explanation": "Generators should be fitted with silencers. Almost all machinery can be redesigned to increase energy efficiency and reduce noise. Noise-absorbing materials may be used apart from personal earplugs and earphones.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-011",
    "type": "mcq",
    "subtopic": "National Jute Board & Synthetic Competition",
    "difficulty": "Medium",
    "question": "The Indian jute industry faces stiff international competition primarily from:",
    "options": [
      "Synthetic substitutes and other jute-producing nations like Bangladesh, Brazil, and Egypt",
      "Cotton textiles produced in European greenhouses",
      "Aluminium foil wrappers used in milk packing",
      "Handmade silk sarees from Kanchipuram"
    ],
    "answer": 0,
    "explanation": "Challenges faced by the jute industry include stiff competition in the international market from synthetic substitutes and from other competitors like Bangladesh, Brazil, Philippines, Egypt and Thailand.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 3.2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-012",
    "type": "mcq",
    "subtopic": "Global Steel Consumption Benchmark",
    "difficulty": "Medium",
    "question": "Per capita consumption of steel in a country is often regarded as an index of:",
    "options": [
      "The country's level of economic and industrial development",
      "The agricultural fertility of river deltas",
      "The percentage of forested land cover",
      "The density of rural postal networks"
    ],
    "answer": 0,
    "explanation": "Production and consumption of steel is often regarded as the index of a country's economic development, as almost all basic, capital, and consumer goods infrastructure rely on steel.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-013",
    "type": "mcq",
    "subtopic": "SAIL & Steel Marketing",
    "difficulty": "Easy",
    "question": "Most of the public sector undertakings in India market their steel through which organisation?",
    "options": [
      "Steel Authority of India Ltd. (SAIL)",
      "Tata Steel International",
      "National Mineral Development Corporation",
      "Minerals and Metals Trading Corporation (MMTC)"
    ],
    "answer": 0,
    "explanation": "Most of the public sector undertakings market their steel through Steel Authority of India Ltd. (SAIL).",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-014",
    "type": "mcq",
    "subtopic": "NMCC Role",
    "difficulty": "Medium",
    "question": "What is the full form of NMCC, an apex body set up to improve manufacturing productivity and competitiveness in India?",
    "options": [
      "National Manufacturing Competitiveness Council",
      "National Mineral Conversion Commission",
      "National Maritime Coal Corporation",
      "Nodal Metallurgical Certification Committee"
    ],
    "answer": 0,
    "explanation": "The National Manufacturing Competitiveness Council (NMCC) was set up with the objective of improving industrial productivity and achieving a targeted growth rate of 12% in the manufacturing sector.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-015",
    "type": "mcq",
    "subtopic": "NTPC Ash Water Recycling",
    "difficulty": "Board Standard",
    "question": "Which of the following techniques is practiced by NTPC to minimise environmental pollution at power generation sites?",
    "options": [
      "Ash water recycling systems and liquid waste management",
      "Releasing untreated heavy metals into open irrigation canals",
      "Burying nuclear waste under fertile agricultural fields",
      "Operating high-sulphur coal burners without exhaust filters"
    ],
    "answer": 0,
    "explanation": "NTPC practices ecological monitoring through ash utilisation, ash water recycling systems, and liquid waste management to minimise waste generation and protect ground water.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-016",
    "type": "mcq",
    "subtopic": "Agro-Based vs Mineral-Based",
    "difficulty": "Easy",
    "question": "Which of the following pairs of industries consists purely of agro-based manufacturing units?",
    "options": [
      "Cotton textiles and Sugar industry",
      "Iron & Steel and Cement industry",
      "Petrochemicals and Aluminium smelting",
      "Automobile assembly and Electronic hardware"
    ],
    "answer": 0,
    "explanation": "Cotton textiles, jute, silk, woollen textiles, sugar, and edible oil industries are based on agricultural raw materials and are therefore classified as agro-based industries.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-017",
    "type": "mcq",
    "subtopic": "Sugar Industry Co-operative Sector",
    "difficulty": "Medium",
    "question": "Why is the cooperative sector particularly suited for the sugar industry in India?",
    "options": [
      "Sugarcane is a seasonal crop and cooperatives allow cane-growing farmers to share profits and risks directly",
      "Sugarcane can only be transported through government helicopters",
      "Sugar cannot be sold in open retail markets without international licenses",
      "Private companies are legally prohibited from purchasing agricultural produce"
    ],
    "answer": 0,
    "explanation": "Sugar industry is seasonal in nature and ideally suited to the cooperative sector where sugarcane growers pool resources and directly control the processing mills, sharing both profit and risk.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 3.3"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-018",
    "type": "mcq",
    "subtopic": "Electronics Hardware Parks",
    "difficulty": "Easy",
    "question": "Software Technology Parks of India (STPIs) provide which critical operational facilities to IT companies?",
    "options": [
      "Single-window service and high data communication facilities",
      "Free raw cotton and coal supply",
      "Exemption from all domestic intellectual property laws",
      "Direct control over international commercial shipping lanes"
    ],
    "answer": 0,
    "explanation": "Software technology parks provide single-window service and high data communication facilities to software experts and multinational tech corporations across India.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.6"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-019",
    "type": "mcq",
    "subtopic": "Water Treatment - Secondary Stage",
    "difficulty": "Board Standard",
    "question": "What is the primary biological mechanism utilized during the 'Secondary Treatment' of industrial wastewater?",
    "options": [
      "Biological aeration where aerobic bacteria digest organic matter in aeration tanks",
      "Passing high-voltage electric currents through sludge",
      "Freezing wastewater to extract pure ice blocks",
      "Chemical neutralisation using concentrated nitric acid"
    ],
    "answer": 0,
    "explanation": "Secondary treatment involves biological processes: wastewater is passed through aeration tanks where aerobic bacteria and microbes digest and break down organic pollutants.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s2-020",
    "type": "mcq",
    "subtopic": "Limestone in Iron Smelting",
    "difficulty": "Medium",
    "question": "What is the function of limestone in the blast furnace during the smelting of iron ore?",
    "options": [
      "It acts as a flux that combines with impurities to form slag",
      "It provides the thermal combustion fuel to melt iron",
      "It hardens steel into stainless alloy",
      "It removes moisture from coking coal"
    ],
    "answer": 0,
    "explanation": "Limestone is added to the blast furnace as a fluxing material. It reacts with silica and alumina impurities in the iron ore to form molten slag, which floats on top and is separated from molten iron.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.1"
  }
]

# -----------------------------------------------------------------------------
# CH 11 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch11_set3 = [
  {
    "id": "cbse10-sst-geo-ch11-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Agriculture and Industry Interdependence",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Agriculture and industry in India are not exclusive of each other; they move hand in hand.\nReason (R): Agro-industries have given a major boost to agriculture by raising its productivity, while agricultural raw materials feed industrial manufacturing.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Agriculture and industry depend on each other. Industries depend on agriculture for raw materials and sell products like irrigation pumps, fertilisers, insecticides, pesticides, and PVC pipes to farmers, raising agricultural productivity.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Jute Concentration along Hugli",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Most of the jute mills in India are concentrated along the banks of the Hugli river in West Bengal.\nReason (R): Hugli basin provides proximity to raw jute cultivation, cheap water transport, abundant processing water, and inexpensive labour from nearby states.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "All geographical and economic factors (proximity to jute belt, water for retting/processing, port facilities, railway network, cheap labour) converge on the Hugli basin.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 3.2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Chotanagpur Steel Cluster",
    "difficulty": "Board Standard",
    "question": "Assertion (A): India's iron and steel industry is largely concentrated in the Chotanagpur plateau region.\nReason (R): The Chotanagpur plateau has vast reserves of high-grade petroleum that directly powers blast furnaces.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 2,
    "explanation": "Assertion is true, but Reason is false. The region has coking coal and high-grade iron ore, not petroleum reserves. Blast furnaces are powered by coking coal and electric power, not petroleum.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Sugar Industry Shift to South",
    "difficulty": "Board Standard",
    "question": "Assertion (A): In recent years, sugar mills are increasingly shifting towards Maharashtra and southern states.\nReason (R): The sugarcane grown in southern India has higher sucrose content and the maritime climate prolongs the crushing season.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Higher sucrose content, longer crushing season due to cooler coastal climate, and successful cooperative management are the primary drivers of this shift.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 3.3"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Aluminium Smelting Power Requirement",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Regular supply of electricity and assured raw material source at minimum cost are prime factors for the location of aluminium smelting plants.\nReason (R): Aluminium smelting is an extremely energy-intensive process consuming approximately 18,600 kWh of electricity per tonne of metal produced.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Aluminium smelting requires enormous electrical energy for electrolytic reduction of alumina. Hence, unbroken electricity supply and cheap bauxite are prime locational prerequisites.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-006",
    "type": "case_based",
    "subtopic": "Case Study - Textile Value Chain",
    "difficulty": "Medium",
    "question": "Read the following statement: 'India exports high-quality cotton yarn to Japan and other countries, but our garment manufacturers often have to import high-quality fabric.' What major structural weakness of India's textile sector does this illustrate?",
    "options": [
      "A mismatch between highly developed spinning capacity and fragmented, decentralized weaving/knitting units",
      "Lack of skilled weavers in rural areas",
      "Government prohibition on domestic fabric dyeing",
      "High import tariffs imposed on domestic cotton seeds"
    ],
    "answer": 0,
    "explanation": "While spinning capacity in India is world-class and competitive globally, weaving and knitting are fragmented in small units that cannot utilize all high-quality yarn domestically, forcing garment makers to import synthetic or fine fabric.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 3.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-007",
    "type": "case_based",
    "subtopic": "Case Study - Sustainable Manufacturing",
    "difficulty": "Medium",
    "question": "An industrial unit producing paper uses 1,000 litres of fresh water per day. According to NCERT environmental guidelines, one litre of untreated industrial wastewater can pollute approximately how many litres of fresh water?",
    "options": [
      "Eight times the quantity of fresh water",
      "Two times the quantity of fresh water",
      "Fifty times the quantity of fresh water",
      "Half the quantity of fresh water"
    ],
    "answer": 0,
    "explanation": "According to NCERT data, one litre of wastewater discharged by our manufacturing industry pollutes eight times the quantity of fresh water.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Thermal Pollution",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Discharging untreated hot water from thermal plants into rivers severely degrades aquatic ecosystems.\nReason (R): High water temperatures lower dissolved oxygen levels and kill eggs and larvae of aquatic organisms.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Thermal discharge elevates temperature, drastically depleting dissolved oxygen concentrations and harming aquatic flora and fauna.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-009",
    "type": "mcq",
    "subtopic": "Biodegradable Jute Packaging",
    "difficulty": "Easy",
    "question": "Why has the global demand for Indian jute packaging materials rebounded in recent years?",
    "options": [
      "Global concern for environment-friendly, biodegradable, and sustainable materials",
      "Synthetic polymer production was permanently banned worldwide",
      "Jute fabric has become cheaper than recycled paper",
      "International shipping companies require jute sacks for gold bullion"
    ],
    "answer": 0,
    "explanation": "The growing global awareness for environment-friendly, biodegradable materials has opened once again the opportunity for jute products over non-biodegradable plastics.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 3.2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: NTPC Afforestation",
    "difficulty": "Board Standard",
    "question": "Assertion (A): NTPC power stations create extensive green belts around their project perimeters.\nReason (R): Afforestation around thermal plants helps absorb dust particulates, reduce noise, and maintain ecological balance.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "NTPC actively maintains green belts for nurturing ecological balance and afforestation around all its thermal power facilities.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-011",
    "type": "mcq",
    "subtopic": "Rainwater Harvesting in Industries",
    "difficulty": "Easy",
    "question": "How can industrial factories reduce their daily pressure on municipal groundwater tables?",
    "options": [
      "By harvesting rainwater to meet industrial requirements and recycling treated water",
      "By pumping groundwater from deeper tube-wells continuously",
      "By draining toxic effluents directly into underground borewells",
      "By evaporating all wastewater into open atmosphere"
    ],
    "answer": 0,
    "explanation": "Rainwater harvesting to meet water requirements and recycling wastewater in two or more successive stages reduces reliance on groundwater reserves.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis - Agglomeration",
    "difficulty": "Medium",
    "question": "An entrepreneur establishes a software firm in Noida near Delhi. The firm benefits from nearby airports, high-speed fiber optic cables, universities providing software engineers, and commercial banks. This is a classic example of:",
    "options": [
      "Agglomeration economies",
      "Cottage industry decentralisation",
      "Pure agro-processing cluster",
      "Extractive metallurgical mining"
    ],
    "answer": 0,
    "explanation": "The enterprise benefits from urban infrastructure, financial networks, educational pools, and communications, representing agglomeration economies.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-013",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Chemical Industry Distribution",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The chemical industry in India is widely dispersed across the country.\nReason (R): The chemical industry is its own largest consumer; basic chemicals are converted into other chemicals used for agriculture, textiles, and consumer goods.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The chemical industry is its own largest consumer. Basic chemicals undergo processing to further produce other chemicals used for industrial applications, agriculture or consumer markets, leading to widespread national dispersion.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.3"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-014",
    "type": "mcq",
    "subtopic": "Fly Ash Utilization",
    "difficulty": "Medium",
    "question": "Fly ash produced in huge quantities by thermal power plants can be constructively utilised in:",
    "options": [
      "Manufacturing Portland pozzolana cement, concrete bricks, and road embankment filling",
      "Refining high-grade edible vegetable cooking oils",
      "Purifying drinking municipal tap water",
      "Manufacturing nitrogenous organic fertilisers"
    ],
    "answer": 0,
    "explanation": "Fly ash is an industrial byproduct of coal combustion. It is extensively utilized in cement manufacturing, concrete fly-ash bricks, and civil road embankments.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-015",
    "type": "assertion_reasoning",
    "subtopic": "A-R: FDI in Automobile Sector",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Foreign Direct Investment (FDI) brought new technology and aligned the Indian automobile industry with global developments.\nReason (R): Post-liberalisation, several international manufacturers established assembly lines in clusters around Gurugram, Chennai, and Pune.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "FDI brought in cutting-edge global technology and stimulated vehicle demand, leading to major manufacturing hubs in Gurugram, Pune, Chennai, Mumbai, and Sanand.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 4.5"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-016",
    "type": "mcq",
    "subtopic": "Tertiary Effluent Treatment Method",
    "difficulty": "Hard",
    "question": "Tertiary treatment of industrial wastewater, aimed at recycling water for reuse, involves which combination of processes?",
    "options": [
      "Biological, chemical, and physical processes including reverse osmosis and filtration",
      "Only mechanical screening through wire meshes",
      "Boiling the effluent at 500 degrees Celsius",
      "Diluting industrial effluent with fresh river water in open dams"
    ],
    "answer": 0,
    "explanation": "Tertiary treatment involves biological, chemical and physical processes. This involves recycling of wastewater so it can be reused safely within the industrial cycle.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-017",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Heavy Industry Classification",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Iron and steel manufacturing is classified as a heavy industry.\nReason (R): Both the raw materials (iron ore, coal, limestone) and the finished steel products are bulky, heavy, and incur high freight transportation costs.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Heavy industries use bulky and heavy raw materials and produce heavy finished goods, incurring substantial transport costs.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-018",
    "type": "mcq",
    "subtopic": "Consumer Industries Example",
    "difficulty": "Easy",
    "question": "Which of the following is an example of a 'consumer industry' that produces goods directly for end-consumer use?",
    "options": [
      "Toothpaste and paper manufacturing",
      "Copper smelting",
      "Heavy engineering forge press",
      "Pig iron manufacturing"
    ],
    "answer": 0,
    "explanation": "Consumer industries produce goods for direct use by consumers, such as sugar, toothpaste, paper, sewing machines, and fans.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-019",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Soil and Groundwater Degradation",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Dumping of industrial wastes such as glass, harmful chemicals, and fly ash leads to both soil pollution and groundwater contamination.\nReason (R): Rainwater percolates through polluted soil, carrying soluble contaminants down into the groundwater table.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Soil and water pollution are closely related. Dumping wastes makes soil barren. Rainwater percolating through the soil carries hazardous soluble pollutants into subterranean aquifers, contaminating groundwater.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5"
  },
  {
    "id": "cbse10-sst-geo-ch11-s3-020",
    "type": "mcq",
    "subtopic": "Integrated Eco-friendly Strategy",
    "difficulty": "Medium",
    "question": "Which principle forms the bedrock of sustainable industrial development as envisioned by the National Green Tribunal and NCERT guidelines?",
    "options": [
      "Integration of economic growth with environmental preservation through reduction, recycling, and clean energy adoption",
      "Complete shut-down of all metallurgical and chemical units",
      "Exporting all industrial waste to neighbouring islands",
      "Mandating that industries operate only once every quarter"
    ],
    "answer": 0,
    "explanation": "Sustainable development demands that industrial and economic growth proceed in harmony with environmental protection through clean technologies, waste minimization, treatment, and recycling.",
    "citation": "NCERT Class 10 Geography, Chapter 6, Section 5.1"
  }
]

# Write Chapter 11 Sets 2 and 3
with open(os.path.join(DATA_DIR, "ch11_manufacturing_industries_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch11_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch11_manufacturing_industries_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch11_set3}, f, indent=2, ensure_ascii=False)

print("Generated: ch11 Sets 2 & 3 (40 Qs)")
