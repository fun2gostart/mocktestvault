#!/usr/bin/env python3
"""
Generates Geography Ch 12 (Lifelines of National Economy) Sets 1, 2, 3.
Total: 3 sets = 60 questions.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# -----------------------------------------------------------------------------
# CH 12 SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch12_set1 = [
  {
    "id": "cbse10-sst-geo-ch12-s1-001",
    "type": "mcq",
    "subtopic": "Lifelines of a Nation Concept",
    "difficulty": "Easy",
    "question": "Efficient and rapid movement of goods, services, and people over space is a prerequisite for fast development. Hence, which sector is termed as the 'lifeline' of a national economy?",
    "options": ["Transport and communication", "Cottage handicraft weaving", "Subsistence agriculture", "Commercial advertising"],
    "answer": 0,
    "explanation": "Transport, communication, and trade are complementary to each other. Together, they facilitate economic exchange, integrate distant regions, and act as the lifelines of our economy.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-002",
    "type": "mcq",
    "subtopic": "Roadways Advantage over Railways",
    "difficulty": "Medium",
    "question": "Which of the following is a key operational advantage of roadways over railways?",
    "options": [
      "Roadways provide door-to-door service and the cost of loading/unloading is much lower",
      "Roadways can transport thousands of tonnes of iron ore in a single trip cheaper than trains",
      "Roadways do not require any construction or maintenance capital",
      "Roadways cannot be built on undulating hilly terrains"
    ],
    "answer": 0,
    "explanation": "Road transport provides door-to-door service, thus the cost of loading and unloading is much lower. Roads can also negotiate higher gradients of slopes and can traverse dissected mountains like the Himalayas.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-003",
    "type": "mcq",
    "subtopic": "Golden Quadrilateral Super Highways",
    "difficulty": "Easy",
    "question": "The Golden Quadrilateral Super Highway project links which four major mega cities of India with 6-lane highways?",
    "options": [
      "Delhi - Mumbai - Chennai - Kolkata",
      "Srinagar - Kanyakumari - Silchar - Porbandar",
      "Jaipur - Ahmedabad - Bengaluru - Hyderabad",
      "Amritsar - Bhopal - Patna - Guwahati"
    ],
    "answer": 0,
    "explanation": "The government launched the Golden Quadrilateral Super Highways project connecting Delhi-Kolkata-Chennai-Mumbai and Delhi by 6-lane super highways. It is implemented by the National Highways Authority of India (NHAI).",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-004",
    "type": "mcq",
    "subtopic": "North-South and East-West Corridors",
    "difficulty": "Easy",
    "question": "The North-South Corridor connects Srinagar (Jammu & Kashmir) with which southern coastal terminus?",
    "options": ["Kanniyakumari", "Kochi", "Chennai", "Thiruvananthapuram"],
    "answer": 0,
    "explanation": "The North-South corridor links Srinagar (Jammu & Kashmir) and Kanniyakumari (Tamil Nadu), while the East-West corridor connects Silchar (Assam) and Porbandar (Gujarat).",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-005",
    "type": "mcq",
    "subtopic": "National Highways Authority",
    "difficulty": "Easy",
    "question": "National Highways (NH) that link extreme parts of the country are constructed and maintained by which government agency?",
    "options": [
      "Central Public Works Department (CPWD)",
      "State Public Works Department (SPWD)",
      "Zilla Parishad",
      "Border Roads Organisation (BRO)"
    ],
    "answer": 0,
    "explanation": "National Highways are the primary road systems and are laid and maintained by the Central Public Works Department (CPWD).",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-006",
    "type": "mcq",
    "subtopic": "Sher Shah Suri Marg",
    "difficulty": "Easy",
    "question": "The historical highway between Delhi and Amritsar, known as Sher Shah Suri Marg, is officially designated as:",
    "options": ["National Highway No. 1", "National Highway No. 7", "National Highway No. 2", "National Highway No. 8"],
    "answer": 0,
    "explanation": "The historical Sher-Shah Suri Marg is called National Highway No. 1, between Delhi and Amritsar.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-007",
    "type": "mcq",
    "subtopic": "Border Roads Organisation (BRO)",
    "difficulty": "Medium",
    "question": "In which year was the Border Roads Organisation (BRO) established to develop roads of strategic importance in the northern and north-eastern border areas?",
    "options": ["1960", "1947", "1971", "1985"],
    "answer": 0,
    "explanation": "Border Roads Organisation (BRO), a Government of India undertaking, was established in 1960 for the development of the roads of strategic importance in the northern and north-eastern border areas.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-008",
    "type": "mcq",
    "subtopic": "Railways Density Factors",
    "difficulty": "Medium",
    "question": "The northern plains of India have the highest railway network density primarily due to:",
    "options": [
      "Vast level land, high population density, and rich agricultural resources",
      "Abundance of high mountain passes and gorges",
      "Dense evergreen forest reserves and marshy terrain",
      "Presence of dry desert dunes without vegetation"
    ],
    "answer": 0,
    "explanation": "The northern plains with their vast level land, high population density and rich agricultural resources provided the most favorable condition for the growth of railway network.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-009",
    "type": "mcq",
    "subtopic": "Konkan Railway Engineering Achievement",
    "difficulty": "Medium",
    "question": "The development of the Konkan Railway along the western coast of India facilitated passenger and freight travel, but has faced challenges such as:",
    "options": [
      "Sinking of tracks in some stretches and severe landslides during monsoons",
      "Total absence of rivers requiring bridges",
      "Extreme freezing temperatures causing tracks to crack in summer",
      "Opposition from neighbouring desert states"
    ],
    "answer": 0,
    "explanation": "Along the western coast, the Konkan railway has facilitated movement of passengers and goods. However, it has also faced problems such as sinking of track in some stretches and landslides during monsoon seasons.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-010",
    "type": "mcq",
    "subtopic": "Pipelines Transport",
    "difficulty": "Medium",
    "question": "Which of the following commodities is transported via underground pipelines after being converted into a slurry?",
    "options": ["Iron ore", "Cotton bales", "Raw timber", "Granite boulders"],
    "answer": 0,
    "explanation": "Pipelines transport crude oil, petroleum products, and natural gas. Solids can also be transported through a pipeline when converted into slurry, such as iron ore slurry from Kudremukh to Mangaluru.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-011",
    "type": "mcq",
    "subtopic": "HVJ Gas Pipeline",
    "difficulty": "Medium",
    "question": "The famous 1,700-km long cross-country Hazira-Vijaipur-Jagdishpur (HVJ) gas pipeline links gas fields in Gujarat to fertiliser and power complexes in:",
    "options": ["Madhya Pradesh and Uttar Pradesh", "Punjab and Haryana", "Karnataka and Kerala", "Odisha and West Bengal"],
    "answer": 0,
    "explanation": "The HVJ gas pipeline links Hazira in Gujarat with Jagdishpur in Uttar Pradesh, via Vijaipur in Madhya Pradesh. It feeds power stations and fertiliser plants across western and northern India.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-012",
    "type": "mcq",
    "subtopic": "National Waterway No. 1",
    "difficulty": "Easy",
    "question": "National Waterway No. 1 (NW-1), having a navigable length of 1,620 km, is situated on which river system?",
    "options": [
      "The Ganga river between Prayagraj and Haldia",
      "The Brahmaputra river between Sadiya and Dhubri",
      "The West Coast Canal in Kerala",
      "The Godavari-Krishna river stretch"
    ],
    "answer": 0,
    "explanation": "The Ganga river between Prayagraj (Allahabad) and Haldia (1,620 km) is declared as National Waterway No. 1 (NW-1).",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.4"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-013",
    "type": "mcq",
    "subtopic": "National Waterway No. 2",
    "difficulty": "Easy",
    "question": "National Waterway No. 2 (NW-2) spans a length of 891 km on which river in north-eastern India?",
    "options": [
      "The Brahmaputra river between Sadiya and Dhubri",
      "The Barak river between Lakhipur and Manga",
      "The Teesta river between Jalpaiguri and Rangpo",
      "The Subansiri river in Arunachal Pradesh"
    ],
    "answer": 0,
    "explanation": "The Brahmaputra river between Sadiya and Dhubri (891 km) is designated as National Waterway No. 2 (NW-2).",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.4"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-014",
    "type": "mcq",
    "subtopic": "Kandla Port Purpose",
    "difficulty": "Medium",
    "question": "Why was Kandla Port in Kachchh (Gujarat) developed immediately after Independence?",
    "options": [
      "To ease the volume of trade on Mumbai port after the loss of Karachi port to Pakistan",
      "To import crude petroleum exclusively for the Himalayan states",
      "To facilitate naval defense exercises during peace times",
      "To replace Kolkata port as an inland riverine terminus"
    ],
    "answer": 0,
    "explanation": "Kandla in Kachchh was the first port to be developed soon after Independence to ease the volume of trade on the Mumbai port, in the wake of loss of Karachi port to Pakistan after Partition.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-015",
    "type": "mcq",
    "subtopic": "Marmagao Iron Ore Export",
    "difficulty": "Easy",
    "question": "Which premier iron ore exporting port of India in Goa accounts for about 50 percent of the country's total iron ore export?",
    "options": ["Marmagao Port", "Kandla Port", "New Mangalore Port", "Tuticorin Port"],
    "answer": 0,
    "explanation": "Marmagao port (Goa) is the premier iron ore exporting port of the country. This port accounts for about fifty percent of India's iron ore export.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-016",
    "type": "mcq",
    "subtopic": "Deepest Landlocked Port",
    "difficulty": "Medium",
    "question": "Which port on the eastern coast of India is the deepest landlocked and well-protected port, originally conceived as an outlet for iron ore exports?",
    "options": ["Visakhapatnam Port", "Paradip Port", "Chennai Port", "Kolkata Port"],
    "answer": 0,
    "explanation": "Visakhapatnam is the deepest landlocked and well-protected port on the eastern coast. This port was originally conceived as an outlet for iron ore exports from Bailadila mines in Chhattisgarh.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-017",
    "type": "mcq",
    "subtopic": "Kolkata Riverine Tidal Port",
    "difficulty": "Medium",
    "question": "Which of the following ports is an inland riverine tidal port that serves a vast and rich hinterland of the Ganga-Brahmaputra basin?",
    "options": ["Kolkata Port", "Chennai Port", "Cochin Port", "Mumbai Port"],
    "answer": 0,
    "explanation": "Kolkata is a riverine port on the Hugli River. Being a tidal port, it requires constant dredging of the riverbed to maintain navigation depth for ocean-going vessels.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-018",
    "type": "mcq",
    "subtopic": "Pawan Hans Helicopters",
    "difficulty": "Easy",
    "question": "Pawan Hans Helicopters Ltd. provides helicopter transport services primarily to:",
    "options": [
      "Oil and Natural Gas Corporation (ONGC) in its off-shore operations and inaccessible areas of north-east India",
      "Private tourist luxury hotels in metropolitan cities",
      "Inter-state postal mail sorting depots",
      "Cargo shipping terminals in Mumbai"
    ],
    "answer": 0,
    "explanation": "Pawan Hans Helicopters Ltd. provides helicopter services to Oil and Natural Gas Corporation (ONGC) in its offshore operations, to inaccessible areas and difficult terrains like the north-eastern states and interior parts of Jammu and Kashmir, Himachal Pradesh and Uttarakhand.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.6"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-019",
    "type": "mcq",
    "subtopic": "First-Class Mail Transport",
    "difficulty": "Easy",
    "question": "Under the Indian postal network, which categories of mail are considered 'First-Class Mail' and are airlifted between stations covering both land and air?",
    "options": [
      "Cards and envelopes",
      "Book packets and registered newspapers",
      "Periodicals and heavy cargo parcels",
      "Agricultural seeds and fertiliser sacks"
    ],
    "answer": 0,
    "explanation": "Cards and envelopes are considered first-class mail and are airlifted between stations covering both land and air. Second-class mail includes book packets, registered newspapers and periodicals, carried by surface transport.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s1-020",
    "type": "mcq",
    "subtopic": "Favourable Balance of Trade",
    "difficulty": "Easy",
    "question": "A country is said to have a 'Favourable Balance of Trade' when:",
    "options": [
      "The value of its exports exceeds the value of its imports",
      "The value of its imports exceeds the value of its exports",
      "All foreign trade is conducted strictly through gold bullion",
      "The country ceases all commercial shipping with international partners"
    ],
    "answer": 0,
    "explanation": "The balance of trade of a country is the difference between its export and import. When the value of export exceeds the value of imports, it is called a favourable balance of trade.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 3"
  }
]

# Write Chapter 12 Set 1
with open(os.path.join(DATA_DIR, "ch12_lifelines_of_national_economy_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch12_set1}, f, indent=2, ensure_ascii=False)

print("Generated: ch12_lifelines_of_national_economy_set1.json (20 Qs)")

# -----------------------------------------------------------------------------
# CH 12 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch12_set2 = [
  {
    "id": "cbse10-sst-geo-ch12-s2-001",
    "type": "mcq",
    "subtopic": "Road Density Concept",
    "difficulty": "Medium",
    "question": "What is the standard geographic definition of 'Road Density'?",
    "options": [
      "The length of road per 100 square kilometres of area",
      "The number of registered vehicles per kilometer of expressway",
      "The total weight of asphalt used in a district",
      "The width of highway lanes across a state"
    ],
    "answer": 0,
    "explanation": "The length of road per 100 sq. km of area is known as density of roads. Distribution of road is not uniform in the country, varying from less than 12 km in Jammu & Kashmir to over 517 km in Kerala.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-002",
    "type": "mcq",
    "subtopic": "PMGSY Rural Roads",
    "difficulty": "Easy",
    "question": "Under which scheme do rural roads in India receive special impetus to link every eligible village with a major all-weather motorable road?",
    "options": [
      "Pradhan Mantri Grameen Sadak Yojana (PMGSY)",
      "National Rural Health Mission",
      "Swarnajayanti Gram Swarozgar Yojana",
      "Mahatma Gandhi National Rural Water Scheme"
    ],
    "answer": 0,
    "explanation": "Rural roads link rural areas and villages with towns. Special provisions under the Pradhan Mantri Grameen Sadak Yojana (PMGSY) ensure that every village in the country is linked to a major town by an all-season motorable road.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-003",
    "type": "mcq",
    "subtopic": "Himalayan Railway Obstacles",
    "difficulty": "Medium",
    "question": "Why are the Himalayan mountainous regions unfavourable for the construction of railway lines?",
    "options": [
      "High relief, sparse population, and lack of economic opportunities",
      "Excessive concentration of industrial chemical plants",
      "Total absence of snow or rainfall in mountain passes",
      "Flat uninterrupted river valleys requiring zero bridges"
    ],
    "answer": 0,
    "explanation": "The Himalayan mountainous regions are unfavourable for the construction of railway lines due to high relief, sparse population, and lack of economic opportunities, alongside difficult technical engineering terrain.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-004",
    "type": "mcq",
    "subtopic": "National Highway Authority Functions",
    "difficulty": "Easy",
    "question": "Which autonomous authority under the Ministry of Road Transport and Highways is responsible for the development and maintenance of the Golden Quadrilateral Super Highways?",
    "options": ["NHAI", "CPWD", "BRO", "SPWD"],
    "answer": 0,
    "explanation": "The National Highways Authority of India (NHAI) is responsible for the implementation, development, and maintenance of the Golden Quadrilateral and Corridor Super Highway projects.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-005",
    "type": "mcq",
    "subtopic": "State Highways Responsibility",
    "difficulty": "Easy",
    "question": "Roads linking a state capital with different district headquarters are known as State Highways. These are constructed and maintained by:",
    "options": [
      "State Public Works Department (PWD)",
      "Central Public Works Department (CPWD)",
      "Border Roads Organisation (BRO)",
      "Zilla Parishad"
    ],
    "answer": 0,
    "explanation": "Roads linking a state capital with different district headquarters are known as State Highways. These roads are constructed and maintained by the State Public Works Department (PWD) in State and Union Territories.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-006",
    "type": "mcq",
    "subtopic": "Pipelines Advantage",
    "difficulty": "Medium",
    "question": "What is the key long-term operational advantage of pipeline transport despite its high initial setup cost?",
    "options": [
      "Subsequent running and maintenance costs are minimal, and it rules out transit delays or trans-shipment losses",
      "It can be relocated to a different route every month easily",
      "It requires zero steel or construction materials",
      "It produces zero carbon emissions during pipe manufacture"
    ],
    "answer": 0,
    "explanation": "Though the initial cost of laying pipelines is high, subsequent running costs are minimal. It rules out trans-shipment losses or transit delays commonly faced in road and rail transport.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-007",
    "type": "mcq",
    "subtopic": "Kochi Natural Harbour",
    "difficulty": "Easy",
    "question": "Which major seaport on the south-west coast is located at the entrance of a lagoon with a natural harbour?",
    "options": ["Kochi Port", "Tuticorin Port", "Marmagao Port", "Mangaluru Port"],
    "answer": 0,
    "explanation": "Kochi is the extreme south-western port, located at the entrance of a lagoon with a natural harbour.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-008",
    "type": "mcq",
    "subtopic": "Tuticorin Port Features",
    "difficulty": "Medium",
    "question": "Which port located in the extreme south-east of India has a natural harbour and rich hinterland, facilitating cargo handling with neighbouring countries like Sri Lanka and Maldives?",
    "options": ["Tuticorin Port (V.O. Chidambaranar)", "Visakhapatnam Port", "Paradip Port", "Ennore Port"],
    "answer": 0,
    "explanation": "Tuticorin port in Tamil Nadu has a natural harbour and rich hinterland. It handles a large volume of domestic and international cargo to neighbouring countries like Sri Lanka and Maldives.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-009",
    "type": "mcq",
    "subtopic": "Oldest Artificial Port",
    "difficulty": "Medium",
    "question": "Which is one of the oldest artificial seaports of India on the eastern coast, ranked next to Mumbai in terms of the volume of trade and cargo?",
    "options": ["Chennai Port", "Kolkata Port", "Visakhapatnam Port", "Haldia Port"],
    "answer": 0,
    "explanation": "Chennai is one of the oldest artificial ports of the country. It is ranked next to Mumbai in terms of the volume of trade and cargo.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-010",
    "type": "mcq",
    "subtopic": "Paradip Port Specialisation",
    "difficulty": "Easy",
    "question": "Paradip port, situated in Odisha, specialises primarily in the export of:",
    "options": ["Iron ore", "Petroleum crude", "Raw cotton", "Bauxite alumina"],
    "answer": 0,
    "explanation": "Paradip port located in Odisha specializes in the export of iron ore extracted from Odisha and Jharkhand mines.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-011",
    "type": "mcq",
    "subtopic": "Haldia Port Subsidiary Role",
    "difficulty": "Easy",
    "question": "Why was the Haldia seaport developed on the Hugli river delta?",
    "options": [
      "As a subsidiary port to relieve growing congestion on Kolkata port",
      "To exclusively handle military submarines",
      "To replace the port of Mumbai after cyclone damage",
      "To export tea produced in Kerala"
    ],
    "answer": 0,
    "explanation": "Haldia port was developed as a subsidiary port, in order to relieve growing pressure on the Kolkata port.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-012",
    "type": "mcq",
    "subtopic": "Six Postal Mail Channels",
    "difficulty": "Medium",
    "question": "To facilitate quick delivery of mails in large towns and cities, Indian Post introduced six mail channels. Which of the following is NOT one of these six channels?",
    "options": ["Airmail Express Channel", "Rajdhani Channel", "Metro Channel", "Green Channel"],
    "answer": 0,
    "explanation": "The six mail channels are: Rajdhani Channel, Metro Channel, Green Channel, Business Channel, Bulk Mail Channel, and Periodical Channel. 'Airmail Express Channel' is not an official mail channel name.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-013",
    "type": "mcq",
    "subtopic": "STD Network Integration",
    "difficulty": "Easy",
    "question": "In telecommunications, what does the abbreviation 'STD' stand for, which integrated two-thirds of Indian villages with round-the-clock telephone service?",
    "options": [
      "Subscriber Trunk Dialling",
      "Standard Telephone Directory",
      "Satellite Transmission Data",
      "Stationary Telecom Device"
    ],
    "answer": 0,
    "explanation": "Subscriber Trunk Dialling (STD) facility integrated Indian villages with towns and cities, providing 24-hour telephone connectivity at uniform trunk call rates.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-014",
    "type": "mcq",
    "subtopic": "Doordarshan National Broadcaster",
    "difficulty": "Easy",
    "question": "The national television broadcaster of India, which is one of the largest terrestrial networks in the world broadcasting diverse educational and entertainment programmes, is:",
    "options": ["Doordarshan", "Prasar Bharati News Channel", "Akashvani", "Vividh Bharati"],
    "answer": 0,
    "explanation": "Doordarshan, the national television channel of India, is one of the largest terrestrial networks in the world, broadcasting a variety of programmes from entertainment, educational to sports for people of different age groups.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-015",
    "type": "mcq",
    "subtopic": "CBFC Film Certification",
    "difficulty": "Easy",
    "question": "Which statutory authority in India is empowered to certify both Indian and foreign feature films before public screening?",
    "options": [
      "Central Board of Film Certification (CBFC)",
      "Press Council of India",
      "Film and Television Institute of India",
      "National Film Development Corporation"
    ],
    "answer": 0,
    "explanation": "The Central Board of Film Certification (CBFC) is the authority responsible for certifying both Indian and foreign films for public exhibition.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-016",
    "type": "mcq",
    "subtopic": "Tourism as Invisible Export",
    "difficulty": "Medium",
    "question": "Tourism is often described as an 'invisible export' for a country because:",
    "options": [
      "It earns substantial foreign exchange through services provided to international visitors without exporting physical goods",
      "Tourists travel only during night flights without passport checks",
      "It involves smuggling of ancient cultural artefacts",
      "It cannot be accounted for in national income statistics"
    ],
    "answer": 0,
    "explanation": "Tourism earns foreign exchange directly through lodging, food, transport, and handicrafts purchased by foreign tourists without physical transfer of domestic assets abroad, acting as an invisible export trade.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 3.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-017",
    "type": "mcq",
    "subtopic": "Inland Waterways Fuel Efficiency",
    "difficulty": "Easy",
    "question": "Inland waterways are considered the most eco-friendly mode of transportation because they are:",
    "options": [
      "Fuel-efficient and have the lowest carbon footprint per tonne-kilometer of freight",
      "Built exclusively from natural bamboo rafts",
      "Completely immune to river floods or silting",
      "Faster than commercial turbo-prop aeroplanes"
    ],
    "answer": 0,
    "explanation": "Waterways are the cheapest means of transport. They are most suitable for carrying heavy and bulky goods. It is a fuel-efficient and environment-friendly mode of transport.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.4"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-018",
    "type": "mcq",
    "subtopic": "New Mangalore Port Kudremukh Ore",
    "difficulty": "Medium",
    "question": "New Mangalore port in Karnataka caters primarily to the export of iron ore concentrates originating from:",
    "options": ["Kudremukh mines", "Bailadila mines", "Singhbhum mines", "Mayurbhanj mines"],
    "answer": 0,
    "explanation": "New Mangalore port, located in Karnataka, caters to the export of iron ore concentrates from Kudremukh deposits.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-019",
    "type": "mcq",
    "subtopic": "Unfavourable Balance of Trade",
    "difficulty": "Easy",
    "question": "If India's value of imported goods (e.g., crude petroleum, electronics, machinery) exceeds the value of its exported commodities, the trade balance is:",
    "options": ["Unfavourable / Deficit", "Favourable / Surplus", "Neutral and bilateral", "Autarkic"],
    "answer": 0,
    "explanation": "If the value of imports is greater than the value of exports, it is termed as an unfavourable balance of trade (trade deficit).",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s2-020",
    "type": "mcq",
    "subtopic": "Jawaharlal Nehru Port Trust (JNPT)",
    "difficulty": "Easy",
    "question": "Jawaharlal Nehru Port (JNPT) near Mumbai was planned with the express purpose of:",
    "options": [
      "De-congesting the Mumbai port and serving as a modern container hub port for the region",
      "Serving inland river transport between Goa and Gujarat",
      "Replacing Kolkata port during winter cyclones",
      "Exporting coal to the Andaman islands"
    ],
    "answer": 0,
    "explanation": "Jawaharlal Nehru Port was planned with a view to decongest the Mumbai port and serve as a hub port for this region.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  }
]

# -----------------------------------------------------------------------------
# CH 12 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch12_set3 = [
  {
    "id": "cbse10-sst-geo-ch12-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Transport and Trade Interdependence",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Dense and efficient networks of transport and communication are a prerequisite for local, national, and global trade.\nReason (R): Today, the world has been converted into a large global village with the help of efficient and fast-moving transport systems.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Modern transport and communication technologies have transformed isolated regions into an integrated global marketplace, making them indispensable for trade and socio-economic progress.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Roadways in Hilly Terrain",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Roads can traverse dissected and undulating relief where railway tracks cannot be laid.\nReason (R): Motor vehicles can negotiate much steeper gradients and sharp curves than heavy railway locomotives.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Roads can negotiate higher gradients of slopes and can easily traverse difficult terrains like the Himalayas where laying railway tracks is technically and economically prohibitive.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Pipeline Transport Economies",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Oil refineries like Barauni, Mathura, and Panipat were established deep in the interior of India, away from coastal oil fields.\nReason (R): Underground pipelines made it economically viable to transport crude oil inland safely without transit delays or environmental leaks.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Refineries like Barauni, Mathura, Panipat and gas-based fertiliser plants could be located in the interior of India only because of cross-country pipeline networks.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Tidal Nature of Kolkata Port",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Kolkata port requires continuous, year-round dredging of the Hugli river channel.\nReason (R): Being a riverine tidal port, incoming tides deposit heavy silt which shallow the river mouth and obstruct ocean vessels.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Kolkata is an inland riverine tidal port. Tidal fluctuations carry immense river silt, necessitating continuous dredging to keep the shipping channel navigable.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Air Travel in North-Eastern States",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Air travel is the most preferred and essential mode of transport in the north-eastern states of India.\nReason (R): The north-eastern region is characterised by big dissected rivers, dense forests, dissected relief, and frequent floods that make road and railway construction extremely difficult.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Air travel can cover difficult terrains like high mountains, dreary deserts, dense forests, and oceanic stretches with great ease, making it vital for north-eastern connectivity.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.6"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-006",
    "type": "case_based",
    "subtopic": "Case Analysis - Tourism Multiplier",
    "difficulty": "Medium",
    "question": "Over 15 million people in India are directly engaged in the tourism industry. Beyond earning foreign exchange, how does tourism promote national integration and local crafts?",
    "options": [
      "It promotes national integration, provides support to local handicrafts and cultural pursuits, and fosters international understanding of Indian heritage",
      "It eliminates the need for domestic agriculture and banking",
      "It forces all rural youth to migrate permanently to foreign destinations",
      "It converts historical monuments into private industrial warehouses"
    ],
    "answer": 0,
    "explanation": "Tourism promotes national integration, provides livelihood support to traditional local handicrafts and cultural artists, and develops international understanding of Indian cultural heritage.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 3.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-007",
    "type": "case_based",
    "subtopic": "Case Analysis - Golden Quadrilateral Impact",
    "difficulty": "Medium",
    "question": "A logistics fleet operates refrigerated container trucks between Delhi and Chennai. Which primary economic objective of the Golden Quadrilateral Super Highways directly benefits this fleet?",
    "options": [
      "Reducing time and distance between the mega cities of India",
      "Eliminating all toll collection across India",
      "Restricting commercial trucks from entering port cities",
      "Mandating that trucks travel only during daytime hours"
    ],
    "answer": 0,
    "explanation": "The major objective of these Super Highways is to reduce the time and distance between the mega cities of India, drastically cutting transit turnaround time for freight.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Northern Railway Density vs Sandy Deserts",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Railway networks in western Rajasthan and the forested hill tracts of central India are sparse.\nReason (R): Sandy deserts, swampy salt marshes of Kachchh, and continuous undulating relief present severe physical obstacles to laying railway tracks.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Sandy plains of western Rajasthan, swamps of Gujarat, and forested tracks of Madhya Pradesh and Chhattisgarh are unfavorable for laying rail lines, resulting in low railway density.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-009",
    "type": "mcq",
    "subtopic": "Border Roads Strategic Value",
    "difficulty": "Medium",
    "question": "Apart from military troop mobility, what vital economic benefit do roads constructed by the Border Roads Organisation (BRO) provide to border inhabitants?",
    "options": [
      "They have improved accessibility in difficult terrain and aided in the economic development of border villages",
      "They provide free electricity to bordering countries",
      "They prohibit all local civilian vehicles from operating",
      "They replace local river irrigation networks"
    ],
    "answer": 0,
    "explanation": "These roads have improved accessibility in areas of difficult terrain and have helped in the economic development of border populations in remote northern and north-eastern regions.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.1"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: International Trade as Barometer",
    "difficulty": "Board Standard",
    "question": "Assertion (A): International trade of a country is an index to its economic prosperity.\nReason (R): As no country is self-sufficient in all resources, international trade allows exchange of surplus domestic commodities for deficit goods and technology.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "No country can survive without international trade because resources are space bound. Hence, foreign trade directly reflects economic wealth and development.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-011",
    "type": "mcq",
    "subtopic": "National Waterway No. 3",
    "difficulty": "Medium",
    "question": "National Waterway No. 3 (205 km) is located in which state along the Udyogamandal and Champakkara canals?",
    "options": ["Kerala", "Goa", "Odisha", "Tamil Nadu"],
    "answer": 0,
    "explanation": "The West-Coast Canal in Kerala (Kottapuram-Kollam, Udyogamandal and Champakkara canals - 205 km) is designated as National Waterway No. 3.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.4"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis - Port Selection",
    "difficulty": "Medium",
    "question": "A mining corporation extracts high-grade iron ore in the Bailadila range of Chhattisgarh and seeks the shortest and most secure deep-water maritime export corridor to Japan. Which seaport will it utilize?",
    "options": ["Visakhapatnam Port", "Kandla Port", "Mumbai Port", "Kolkata Port"],
    "answer": 0,
    "explanation": "Visakhapatnam is the deepest landlocked and well-protected port, specially designed and connected by rail to handle iron ore exports from the Bailadila range in Chhattisgarh.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-013",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Pipeline Slurry Innovation",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Pipelines are now increasingly used to transport solid mineral ores over long distances in India.\nReason (R): Crushed mineral ores can be mixed with water to form slurry, which is smoothly pumped through sealed underground pipes with zero dust pollution.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Solids can be transported through pipelines when converted into slurry. This technology prevents dust emissions and environmental spoilage along highways.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-014",
    "type": "mcq",
    "subtopic": "Indian Maritime Trade Volume",
    "difficulty": "Easy",
    "question": "Approximately what percentage of India's international trade volume is carried via maritime sea routes?",
    "options": ["95 percent", "50 percent", "25 percent", "70 percent"],
    "answer": 0,
    "explanation": "Ninety-five percent of the country's trade volume (68 percent in terms of value) is moved by sea.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.5"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-015",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Digital Telecom Expansion",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The government of India made special provisions to extend 24-hour STD and broadband connectivity to every village.\nReason (R): The integration of space technology with communication satellites was vital to accelerate socio-economic empowerment across rural India.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "There is a uniform rate of STD calls for the whole of India. This has been made possible by integrating development in space technology with communication technology to spur grassroots development.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-016",
    "type": "mcq",
    "subtopic": "Mass Communication Channels",
    "difficulty": "Easy",
    "question": "Which of the following media represents a 'mass communication' channel that creates national awareness and delivers educational entertainment to millions simultaneously?",
    "options": ["Radio and Television", "Personal handwritten postcard", "One-to-one telephonic call", "Private SMS message"],
    "answer": 0,
    "explanation": "Mass communication provides entertainment and creates awareness among people about various national programmes and policies. It includes radio, television, newspapers, magazines, books and films.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-017",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Indian Railways Challenges",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Unruly passenger behaviour, ticketless travel, and pulling of emergency chains cause immense financial and operational loss to Indian Railways.\nReason (R): Pulling emergency chains unnecessarily causes sudden stops, derails train schedules, and damages rolling stock braking equipment.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Many passengers travel without tickets. Thefts and damaging of railway property has not yet stopped completely. People stop the trains, pull the chain unnecessarily and this causes heavy damage and delays.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-018",
    "type": "mcq",
    "subtopic": "Commodities Exported from India",
    "difficulty": "Medium",
    "question": "Which of the following commodities groups constitutes a major portion of India's exports in international merchandise trade?",
    "options": [
      "Gems and jewellery, chemicals, engineering goods, and agricultural products",
      "Crude petroleum and liquefied natural gas",
      "Heavy mining locomotives and commercial jet airliners",
      "Coking coal and potassium fertilisers"
    ],
    "answer": 0,
    "explanation": "Commodities exported from India to other countries include petroleum products, gems and jewellery, chemicals and related products, engineering goods, and agriculture products.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 3"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-019",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Konkan Track Engineering",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The construction of the Konkan railway line along the rugged Western Ghats was a major engineering breakthrough in India.\nReason (R): The Konkan route negotiated over 2,000 bridges, 91 tunnels, and steep coastal mountain gorges.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The 760-km Konkan Railway route was an engineering marvel overcoming deep gorges, hundreds of rivers, and dozens of mountain tunnels across difficult coastal terrains.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 1.2"
  },
  {
    "id": "cbse10-sst-geo-ch12-s3-020",
    "type": "mcq",
    "subtopic": "Postal Network Mail Transport Integration",
    "difficulty": "Medium",
    "question": "What is the key structural benefit of having the largest postal network in the world, like India Post, integrated with modern airline routes?",
    "options": [
      "It facilitates uninterrupted, rapid personal and commercial communication across all remote corners of the nation within 24 to 48 hours",
      "It eliminates the need for written invoices in trade",
      "It converts all physical letters into television broadcasts automatically",
      "It requires no post offices or local postal delivery staff"
    ],
    "answer": 0,
    "explanation": "The Indian postal network handles parcels as well as personal written communications. First-class mail is airlifted between stations, bridging physical distances rapidly across India.",
    "citation": "NCERT Class 10 Geography, Chapter 7, Section 2"
  }
]

# Write Chapter 12 Sets 2 and 3
with open(os.path.join(DATA_DIR, "ch12_lifelines_of_national_economy_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch12_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch12_lifelines_of_national_economy_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch12_set3}, f, indent=2, ensure_ascii=False)

print("Generated: ch12 Sets 2 & 3 (40 Qs)")
