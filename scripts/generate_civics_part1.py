#!/usr/bin/env python3
"""
Generates Civics Ch 13 (Power Sharing) Sets 1, 2, 3
and Ch 14 (Federalism) Sets 1, 2, 3.
Total: 6 sets = 120 questions.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# =============================================================================
# CHAPTER 13: POWER SHARING (Civics Ch 1)
# =============================================================================

ch13_set1 = [
  {
    "id": "cbse10-sst-civ-ch13-s1-001",
    "type": "mcq",
    "subtopic": "Belgium Ethnic Composition",
    "difficulty": "Easy",
    "question": "In Belgium, what percentage of the total population lives in the Flemish region and speaks the Dutch language?",
    "options": ["59 percent", "40 percent", "80 percent", "20 percent"],
    "answer": 0,
    "explanation": "Of the country's total population, 59 percent lives in the Flemish region and speaks Dutch language. Another 40 percent people live in the Wallonia region and speak French. The remaining 1 percent of the Belgians speak German.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-002",
    "type": "mcq",
    "subtopic": "Brussels Linguistic Peculiarity",
    "difficulty": "Medium",
    "question": "In the capital city of Belgium, Brussels, what was the special linguistic composition that created tension?",
    "options": [
      "80% people spoke French while 20% spoke Dutch, reversing the national majority",
      "100% of the population spoke only German",
      "Dutch speakers were the overwhelming majority with 95% share",
      "English was the sole mother tongue of all citizens"
    ],
    "answer": 0,
    "explanation": "In Brussels, 80 percent of the people speak French while 20 percent are Dutch-speaking. The Dutch-speaking people constituted a majority in the country, but a minority in the capital.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-003",
    "type": "mcq",
    "subtopic": "Sri Lanka Ethnic Composition",
    "difficulty": "Easy",
    "question": "In Sri Lanka, which social group forms the largest demographic majority of the population?",
    "options": ["Sinhala speakers (74%)", "Tamil speakers (18%)", "Christian community (7%)", "Muslim community (10%)"],
    "answer": 0,
    "explanation": "The major social groups in Sri Lanka are the Sinhala-speakers (74 percent) and the Tamil-speakers (18 percent).",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-004",
    "type": "mcq",
    "subtopic": "Tamil Sub-groups in Sri Lanka",
    "difficulty": "Medium",
    "question": "Among Tamils in Sri Lanka, who are known as 'Indian Tamils'?",
    "options": [
      "Those whose forefathers came from India as plantation workers during the colonial period",
      "Tamil natives whose ancestors always lived in northern Sri Lanka",
      "Merchants who migrated to Colombo after 1948",
      "Diplomats posted at the Indian High Commission"
    ],
    "answer": 0,
    "explanation": "Tamil natives of the country are called 'Sri Lankan Tamils' (13 percent). The rest, whose forefathers came from India as plantation workers during colonial period, are called 'Indian Tamils' (5 percent).",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-005",
    "type": "mcq",
    "subtopic": "Majoritarian Act of 1956 in Sri Lanka",
    "difficulty": "Medium",
    "question": "In 1956, an Act was passed by the Sri Lankan parliament to establish Sinhala supremacy. What did this Act mandate?",
    "options": [
      "It recognized Sinhala as the only official language, disregarding Tamil",
      "It introduced equal power sharing between Sinhalas and Tamils",
      "It partitioned the island into two independent nations",
      "It adopted English as the national language of Sri Lanka"
    ],
    "answer": 0,
    "explanation": "In 1956, an Act was passed to recognise Sinhala as the only official language, thus disregarding Tamil. The governments followed preferential policies that favoured Sinhala applicants for university positions and government jobs.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-006",
    "type": "mcq",
    "subtopic": "State Religion in Sri Lankan Constitution",
    "difficulty": "Easy",
    "question": "The new constitution of Sri Lanka stipulated that the state shall foster and protect which religion?",
    "options": ["Buddhism", "Hinduism", "Christianity", "Islam"],
    "answer": 0,
    "explanation": "A new constitution stipulated that the state shall protect and foster Buddhism, further alienating the Sri Lankan Tamils who were predominantly Hindus and Muslims.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-007",
    "type": "mcq",
    "subtopic": "Tamil Eelam Demand",
    "difficulty": "Medium",
    "question": "By the 1980s, several political organisations were formed in Sri Lanka demanding which of the following?",
    "options": [
      "An independent Tamil Eelam (state) in northern and eastern parts of Sri Lanka",
      "Immediate merger of Sri Lanka with the Indian Union",
      "Total ban on the Sinhala language in Colombo",
      "Introduction of a military dictatorship"
    ],
    "answer": 0,
    "explanation": "By 1980s several political organisations were formed demanding an independent Tamil Eelam (state) in northern and eastern parts of Sri Lanka, leading to a prolonged civil war.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-008",
    "type": "mcq",
    "subtopic": "Belgian Constitutional Amendments",
    "difficulty": "Medium",
    "question": "Between 1970 and 1993, how many times did the leaders of Belgium amend their constitution to enable everyone to live together peacefully within the same country?",
    "options": ["Four times", "Two times", "Ten times", "Zero times"],
    "answer": 0,
    "explanation": "Between 1970 and 1993, the Belgian leaders amended their constitution four times so as to work out an arrangement that would enable everyone to live together within the same country.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-009",
    "type": "mcq",
    "subtopic": "Belgian Model - Central Ministerial Parity",
    "difficulty": "Medium",
    "question": "Under the Belgian model of accommodation, what is the rule regarding the central government cabinet?",
    "options": [
      "The number of Dutch and French-speaking ministers shall be equal in the central government",
      "French ministers must hold at least 80% of all portfolios",
      "The Prime Minister must always belong to the German minority",
      "Ministers are chosen exclusively by the King without parliamentary vote"
    ],
    "answer": 0,
    "explanation": "Constitution prescribes that the number of Dutch and French-speaking ministers shall be equal in the central government. Some special laws require the support of majority of members from each linguistic group.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-010",
    "type": "mcq",
    "subtopic": "Community Government in Belgium",
    "difficulty": "Board Standard",
    "question": "Apart from the Central and State Governments, what unique third tier of government exists in Belgium?",
    "options": [
      "'Community Government' elected by people belonging to one language group (Dutch, French, and German)",
      "Military tribunals headed by NATO generals",
      "A religious clergy council representing Catholic bishops",
      "Privatized corporate municipal councils"
    ],
    "answer": 0,
    "explanation": "Apart from the Central and the State Government, there is a third kind of government. This 'community government' is elected by people belonging to one language community — Dutch, French and German-speaking — no matter where they live. It has power regarding cultural, educational and language-related issues.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-011",
    "type": "mcq",
    "subtopic": "European Union Headquarters Choice",
    "difficulty": "Easy",
    "question": "When many countries of Europe came together to form the European Union, which city was chosen as its headquarters due to its successful model of power sharing?",
    "options": ["Brussels", "Paris", "Berlin", "Geneva"],
    "answer": 0,
    "explanation": "When many countries of Europe came together to form the European Union (EU), Brussels was chosen as its headquarters.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-012",
    "type": "mcq",
    "subtopic": "Prudential Reason for Power Sharing",
    "difficulty": "Medium",
    "question": "Which of the following represents a 'prudential' reason for power sharing?",
    "options": [
      "It reduces the possibility of conflict between social groups and ensures political stability",
      "Power sharing is an intrinsic sacred moral virtue",
      "It allows dictators to consolidate supreme personal power",
      "It completely eliminates the need for periodic elections"
    ],
    "answer": 0,
    "explanation": "Prudential reasons stress that power sharing will bring out better outcomes. It helps to reduce the possibility of conflict between social groups, preventing violence and political instability.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-013",
    "type": "mcq",
    "subtopic": "Moral Reason for Power Sharing",
    "difficulty": "Medium",
    "question": "Which of the following represents a 'moral' reason for power sharing in a democracy?",
    "options": [
      "Power sharing is the very spirit of democracy; people have a right to be consulted on how they are to be governed",
      "Power sharing maximizes industrial tax revenue for the state",
      "It reduces administrative paper costs of government offices",
      "It guarantees that only one political party remains in power forever"
    ],
    "answer": 0,
    "explanation": "Moral reasons emphasise the very act of power sharing as valuable. A democratic rule involves sharing power with those affected by its exercise, and who have to live with its effects.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-014",
    "type": "mcq",
    "subtopic": "Horizontal Distribution of Power",
    "difficulty": "Easy",
    "question": "Power shared among different organs of government, such as the legislature, executive, and judiciary, is termed as:",
    "options": [
      "Horizontal distribution of power",
      "Vertical division of power",
      "Community power distribution",
      "Federal delegation of power"
    ],
    "answer": 0,
    "explanation": "Power is shared among different organs of government, such as the legislature, executive and judiciary. It is called horizontal distribution of power because it allows different organs of government placed at the same level to exercise different powers.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-015",
    "type": "mcq",
    "subtopic": "System of Checks and Balances",
    "difficulty": "Medium",
    "question": "Why is the horizontal distribution of power also known as a 'system of checks and balances'?",
    "options": [
      "None of the organs can exercise unlimited power, and each organ checks the other, creating a balance of power",
      "Banks check commercial loans and balance trade deficits",
      "Citizens have to pay equal balance checks to judges and ministers",
      "The military checks and balances the political parties"
    ],
    "answer": 0,
    "explanation": "In a horizontal arrangement, judges can check the functioning of executive or laws made by the legislatures. Even though ministers exercise power, they are responsible to the Parliament. This arrangement results in a system of checks and balances.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-016",
    "type": "mcq",
    "subtopic": "Vertical Division of Power",
    "difficulty": "Easy",
    "question": "Power shared among governments at different levels—such as a general central government for the entire country and provincial or regional governments—is called:",
    "options": [
      "Vertical division of power",
      "Horizontal distribution of power",
      "Judicial supremacy",
      "Bureaucratic delegation"
    ],
    "answer": 0,
    "explanation": "Division of power involving higher and lower levels of government (such as Union, State, and Local governments) is called vertical division of power.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-017",
    "type": "mcq",
    "subtopic": "Power Sharing Among Social Groups",
    "difficulty": "Medium",
    "question": "The system of 'reserved constituencies' in assemblies and the parliament of India is an example of power sharing among:",
    "options": [
      "Different religious and socially weaker groups",
      "Different multinational corporations",
      "Armed forces and civilian police",
      "The prime minister and the chief justice"
    ],
    "answer": 0,
    "explanation": "Power may also be shared among different social groups, such as the religious and linguistic groups. 'Community government' in Belgium and 'reserved constituencies' in India are good examples of this arrangement.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-018",
    "type": "mcq",
    "subtopic": "Coalition Government as Power Sharing",
    "difficulty": "Easy",
    "question": "When two or more political parties form an alliance to contest elections and win to form a government together, it is called a:",
    "options": ["Coalition government", "Unitary state", "Presidential dictatorship", "One-party regime"],
    "answer": 0,
    "explanation": "When two or more parties form an alliance to contest elections, if their alliance is elected, they form a coalition government and thus share power directly.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-019",
    "type": "mcq",
    "subtopic": "Pressure Groups and Interest Groups",
    "difficulty": "Medium",
    "question": "How do interest groups such as traders, businessmen, industrialists, farmers, and industrial workers share in governmental power?",
    "options": [
      "Through participation in governmental committees and bringing influence on decision-making processes",
      "By replacing the supreme court with trade union councils",
      "By collecting national defense taxes directly from citizens",
      "By appointing ambassadors to foreign countries"
    ],
    "answer": 0,
    "explanation": "Interest groups share governmental power either through participation in governmental committees or bringing influence on the decision-making process.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s1-020",
    "type": "mcq",
    "subtopic": "Consequence of Majoritarianism",
    "difficulty": "Medium",
    "question": "What was the direct catastrophic consequence of majoritarian policies adopted by the Sri Lankan government?",
    "options": [
      "Distrust turned into widespread conflict and culminated in a protracted civil war",
      "Sri Lanka became the most prosperous nation in South Asia without poverty",
      "Tamil was adopted as the universal language across all schools",
      "The United Nations took over sovereign control of Sri Lanka"
    ],
    "answer": 0,
    "explanation": "The distrust between Sinhala and Tamil communities turned into widespread conflict and soon turned into a Civil War. As a result, thousands of people of both communities were killed, causing a terrible setback to the social, cultural and economic life of the country.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  }
]

# Write Chapter 13 Set 1
with open(os.path.join(DATA_DIR, "ch13_power_sharing_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch13_set1}, f, indent=2, ensure_ascii=False)

print("Generated: ch13_power_sharing_set1.json (20 Qs)")

# -----------------------------------------------------------------------------
# CH 13 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch13_set2 = [
  {
    "id": "cbse10-sst-civ-ch13-s2-001",
    "type": "mcq",
    "subtopic": "Brussels Accommodation Factor",
    "difficulty": "Medium",
    "question": "Why did the French-speaking community in Brussels accept equal representation in the capital city's government?",
    "options": [
      "Because the Dutch-speaking community had accepted equal representation in the Central Government despite being a national majority",
      "Because French speakers were legally forced by the European Union court",
      "Because the Dutch community agreed to pay all national income taxes",
      "Because Brussels was placed under direct rule of the German monarchy"
    ],
    "answer": 0,
    "explanation": "Brussels has a separate government in which both the communities have equal representation. The French-speaking people accepted equal representation in Brussels because the Dutch-speaking community has accepted equal representation in the Central Government.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-002",
    "type": "mcq",
    "subtopic": "Definition of Majoritarianism",
    "difficulty": "Medium",
    "question": "What is meant by the political concept of 'Majoritarianism'?",
    "options": [
      "A belief that the majority community should be able to rule a country in whichever way it wants, by disregarding the wishes and needs of the minority",
      "A system where all decisions are made strictly through unanimous consensus",
      "Rule by military generals elected by majority soldiers",
      "Protection of fundamental minority rights under constitutional supremacy"
    ],
    "answer": 0,
    "explanation": "Majoritarianism is a belief that the majority community should be able to rule a country in whichever way it wants, by disregarding the wishes and needs of the minority.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-003",
    "type": "mcq",
    "subtopic": "Civil War Definition",
    "difficulty": "Easy",
    "question": "A violent conflict between opposing groups within a country that becomes so intense that it appears like a war is called a:",
    "options": ["Civil war", "Cold war", "Proxy border dispute", "Colonial rebellion"],
    "answer": 0,
    "explanation": "A civil war is a violent conflict between opposing groups within a country that becomes so intense that it appears like a war.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-004",
    "type": "mcq",
    "subtopic": "Community Government Powers",
    "difficulty": "Medium",
    "question": "What specific subjects fall under the jurisdiction of the 'Community Government' in Belgium?",
    "options": [
      "Cultural, educational, and language-related issues",
      "National currency, defence, and foreign treaties",
      "Direct taxation on commercial banking profits",
      "Appointing judges to the international court of justice"
    ],
    "answer": 0,
    "explanation": "The 'community government' in Belgium has the power regarding cultural, educational and language-related issues.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-005",
    "type": "mcq",
    "subtopic": "Power Sharing in Modern Democracies",
    "difficulty": "Medium",
    "question": "In a modern democracy, political power should be distributed among as many citizens as possible because:",
    "options": [
      "People are the source of all political power and rule themselves through institutions of self-governance",
      "It prevents any law from ever being passed in the legislature",
      "Citizens should be forced to vote on every municipal tax bill daily",
      "Judges should replace politicians in executive offices"
    ],
    "answer": 0,
    "explanation": "One basic principle of democracy is that people are the source of all political power. In a good democratic government, due respect is given to diverse groups and views that exist in a society.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-006",
    "type": "mcq",
    "subtopic": "Separation of Powers Philosophical Basis",
    "difficulty": "Board Standard",
    "question": "The concept of horizontal distribution of power and checks and balances is designed to prevent:",
    "options": [
      "Any single organ of government from exercising unlimited, unchecked power",
      "Elections from occurring at regular constitutional intervals",
      "Citizens from forming independent civil society organisations",
      "State governments from collecting local municipal revenue"
    ],
    "answer": 0,
    "explanation": "Horizontal distribution ensures that none of the organs can exercise unlimited power. Each organ checks the others, resulting in a balance of power among various institutions.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-007",
    "type": "mcq",
    "subtopic": "Sri Lankan Independence Year",
    "difficulty": "Easy",
    "question": "In which year did Sri Lanka emerge as an independent nation?",
    "options": ["1948", "1947", "1950", "1956"],
    "answer": 0,
    "explanation": "Sri Lanka emerged as an independent country in 1948. The leaders of the Sinhala community sought to secure dominance over government by virtue of their majority.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-008",
    "type": "mcq",
    "subtopic": "Lebanon Power Sharing Agreement",
    "difficulty": "Board Standard",
    "question": "In the case study of Beirut (Lebanon), how was power shared among different religious communities to end the civil war?",
    "options": [
      "President must be Maronite Christian, Prime Minister Sunni Muslim, Deputy PM Orthodox Christian, and Speaker Shi'a Muslim",
      "Only Christian citizens can hold cabinet positions while Muslims vote in elections",
      "Lebanon was divided into four separate sovereign city-states",
      "The French ambassador was appointed permanent military head of state"
    ],
    "answer": 0,
    "explanation": "Under the power-sharing pact in Lebanon: President must be a Maronite Christian, Prime Minister must be a Sunni Muslim, Deputy Prime Minister an Orthodox Christian, and the Speaker a Shi'a Muslim. Christians agreed not to seek French protection and Muslims agreed not to seek unification with Syria.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4 (Box Story: Khalil's Dilemma)"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-009",
    "type": "mcq",
    "subtopic": "Tyranny of Majority",
    "difficulty": "Medium",
    "question": "Why is the tyranny of the majority not just oppressive for the minority, but often ruins the majority itself?",
    "options": [
      "It destroys national unity, provokes violent rebellion, and tears the fabric of the state apart",
      "It forces the majority to pay 100% of the taxes while the minority pays nothing",
      "It dissolves the military defense of the country",
      "It leads to automatic expulsion from the United Nations"
    ],
    "answer": 0,
    "explanation": "Tyranny of the majority is not just oppressive for the minority; it often brings ruin to the majority as well by breeding social instability, violent conflict, and political partition.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-010",
    "type": "mcq",
    "subtopic": "Linguistic Diversity in Belgium",
    "difficulty": "Easy",
    "question": "Which minority linguistic community accounted for only 1 percent of Belgium's population and lived in the eastern border area?",
    "options": ["German-speaking Belgians", "Italian-speaking immigrants", "Spanish-speaking traders", "Danish-speaking farmers"],
    "answer": 0,
    "explanation": "The remaining 1 percent of Belgians speak German and reside primarily along the eastern border region of the country.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-011",
    "type": "mcq",
    "subtopic": "Special Laws in Belgian Parliament",
    "difficulty": "Hard",
    "question": "Under the Belgian constitution, how are 'special linguistic laws' passed in the central parliament?",
    "options": [
      "They require the support of a majority of members from each linguistic group separately",
      "They are passed only if the King issues a royal decree",
      "They require a simple 51% majority of all members present regardless of community",
      "They can only be drafted by German-speaking senators"
    ],
    "answer": 0,
    "explanation": "Some special laws require the support of a majority of members from each linguistic group. Thus, no single community can make decisions unilaterally.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-012",
    "type": "mcq",
    "subtopic": "State Governments in Belgium",
    "difficulty": "Medium",
    "question": "How did the Belgian model restructure the relationship between the Central Government and the regional State Governments?",
    "options": [
      "Many powers of the Central Government were given to State Governments, and State Governments are not subordinate to the Central Government",
      "State Governments were abolished and replaced by military administrators",
      "State Governments were made completely subordinate to the Brussels mayor",
      "Central government retained 100% control over all municipal policing"
    ],
    "answer": 0,
    "explanation": "Many powers of the central government have been given to state governments of the two regions. The state governments are not subordinate to the Central Government.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-013",
    "type": "mcq",
    "subtopic": "Religious Composition of Sri Lankan Tamils",
    "difficulty": "Medium",
    "question": "Most of the Sinhala-speaking people in Sri Lanka are Buddhists. What is the religious composition of the Tamil speakers?",
    "options": [
      "Most are Hindus or Muslims, with about 7 percent Christians across both Sinhala and Tamil communities",
      "100 percent of Tamils are Buddhists",
      "All Tamils in Sri Lanka practice Zoroastrianism",
      "Tamils in Sri Lanka are exclusively Roman Catholics"
    ],
    "answer": 0,
    "explanation": "Most of the Sinhala-speaking people are Buddhists, while most of the Tamils are Hindus or Muslims. There are about 7 percent Christians, who are both Tamil and Sinhala.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-014",
    "type": "mcq",
    "subtopic": "Tamil Alienation Factors",
    "difficulty": "Medium",
    "question": "Which feeling became widespread among Sri Lankan Tamils as a result of successive majoritarian government policies after 1956?",
    "options": [
      "A feeling of alienation, believing that none of the major political parties led by Buddhist Sinhalas were sensitive to their language and culture",
      "A sense of immense gratitude towards the Colombo parliament",
      "A desire to dissolve their own Tamil linguistic identity",
      "A complete rejection of all educational and university degrees"
    ],
    "answer": 0,
    "explanation": "Sri Lankan Tamils felt that none of the major political parties led by the Buddhist Sinhala leaders were sensitive to their language and culture. They felt that the constitution and government policies denied them equal political rights, creating deep alienation.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-015",
    "type": "mcq",
    "subtopic": "Power Sharing in Coalition Governance",
    "difficulty": "Easy",
    "question": "In contemporary democracies, the rise of coalition governments at national and state levels ensures power sharing among:",
    "options": [
      "Different political parties representing diverse regional and ideological interests",
      "Foreign diplomats and local governors",
      "Private commercial banks and real estate builders",
      "Judicial clerks and municipal sweepers"
    ],
    "answer": 0,
    "explanation": "Coalition governments bring together different political parties that represent different ideologies and social groups, ensuring direct sharing of political power.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-016",
    "type": "mcq",
    "subtopic": "Federal Division of Power Terminology",
    "difficulty": "Easy",
    "question": "The vertical division of power between a higher level of government and lower levels of government is also commonly known as:",
    "options": [
      "Federal division of power",
      "Totalitarian concentration of power",
      "Monarchical delegation",
      "Bureaucratic hierarchy"
    ],
    "answer": 0,
    "explanation": "A general government for the entire country and governments at the provincial or regional level is called federal division of power.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-017",
    "type": "mcq",
    "subtopic": "Power Sharing through Pressure Groups",
    "difficulty": "Medium",
    "question": "Movements and pressure groups (such as anti-dam movements, farmers' associations, and environmental groups) share power by:",
    "options": [
      "Influencing governmental decisions through protests, lobbying, and media campaigns",
      "Dissolving the Parliament and establishing emergency rule",
      "Appointing judges to the Supreme Court directly",
      "Printing their own regional currency notes"
    ],
    "answer": 0,
    "explanation": "In a democracy, citizens also have the freedom to organise movements and interest groups. These groups influence those in power through democratic mobilisation and policy advocacy.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-018",
    "type": "mcq",
    "subtopic": "Comparing Belgium and Sri Lanka Lessons",
    "difficulty": "Board Standard",
    "question": "What fundamental comparative political lesson do the contrasting experiences of Belgium and Sri Lanka teach modern democracies?",
    "options": [
      "Unity of the nation is possible only by respecting the feelings and interests of different communities and regions",
      "A majority community must forcefully suppress all linguistic minorities to achieve rapid economic growth",
      "Small nations should never adopt democratic constitutions",
      "Countries with multiple languages must immediately partition into tiny sovereign states"
    ],
    "answer": 0,
    "explanation": "Belgium showed that national unity is possible only by respecting the feelings and interests of different communities. Sri Lanka showed that if a majority community forces its dominance over others and refuses to share power, it can undermine the unity of the nation.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3 & 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-019",
    "type": "mcq",
    "subtopic": "Decentralisation as Vertical Power Sharing",
    "difficulty": "Easy",
    "question": "Extending power sharing down to local self-governing bodies such as Panchayats and Municipalities is an application of:",
    "options": [
      "Vertical division of power",
      "Horizontal checks and balances",
      "Judicial review",
      "Diplomatic immunity"
    ],
    "answer": 0,
    "explanation": "The division of powers between Central, State, and Local levels of government (Panchayati Raj and Municipalities) represents vertical division of power.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s2-020",
    "type": "mcq",
    "subtopic": "Legitimate Government Hallmark",
    "difficulty": "Medium",
    "question": "According to democratic theory, what is the hallmark of a 'legitimate government'?",
    "options": [
      "A government where citizens, through participation, acquire a stake in the system",
      "A government that never changes its prime minister",
      "A government with zero opposition parties in parliament",
      "A government where rulers inherit power by royal birth"
    ],
    "answer": 0,
    "explanation": "A legitimate government is one where citizens, through participation, acquire a stake in the system and have an active voice in governance.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  }
]

# -----------------------------------------------------------------------------
# CH 13 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch13_set3 = [
  {
    "id": "cbse10-sst-civ-ch13-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Power Sharing and Social Harmony",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Power sharing is good for democracies because it helps reduce the possibility of conflict between social groups.\nReason (R): Since social conflict often leads to violence and political instability, power sharing is a good way to ensure the stability of political order.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Power sharing prevents alienation of social groups, averts violent unrest, and fosters long-term political stability, representing the prudential logic of democracy.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Majoritarianism in Sri Lanka",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The leaders of the Sinhala community adopted majoritarian measures to establish Sinhala supremacy.\nReason (R): In 1956, Sinhala was made the sole official language, and preferential policies favoured Sinhalas in university admissions and government jobs.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The 1956 Act and discriminatory state policies were concrete manifestations of majoritarian governance aimed at cementing Sinhala dominance.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Belgium Ethnic Accommodation Success",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Belgium successfully avoided civic strife between Dutch and French-speaking communities.\nReason (R): Belgian leaders recognized the existence of regional differences and cultural diversities and amended the constitution to ensure equal power sharing.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Constitutional flexibility and genuine mutual accommodation between Dutch and French leaders prevented civil division and preserved Belgian unity.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Checks and Balances Mechanism",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The horizontal division of power is also called a system of checks and balances.\nReason (R): In horizontal power sharing, different organs of government placed at the same level exercise different powers and monitor each other.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Because legislature, executive, and judiciary are placed at the same level and check one another's actions, a healthy constitutional equilibrium is maintained.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Moral Argument for Power Sharing",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Power sharing is considered the very spirit of democracy.\nReason (R): A democratic government involves sharing power with all citizens who are affected by its decisions.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The moral reason emphasizes that democracy is meaningless if citizens lack participation in the exercise of authority that impacts their daily lives.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-006",
    "type": "case_based",
    "subtopic": "Case Analysis - Community Government",
    "difficulty": "Medium",
    "question": "A German-speaking citizen living in the French-speaking Wallonia region of Belgium wants to vote on the language curriculum taught in German-medium schools. Which governmental authority in Belgium handles this matter?",
    "options": [
      "The German Community Government, which has jurisdiction over cultural, educational, and language issues regardless of where members reside",
      "The French Wallonia Regional Council",
      "The Brussels City Corporation",
      "The European Court of Human Rights"
    ],
    "answer": 0,
    "explanation": "The 'community government' is elected by people belonging to one language community — Dutch, French and German-speaking — no matter where they live in Belgium. It has power regarding cultural, educational and language-related issues.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-007",
    "type": "case_based",
    "subtopic": "Case Analysis - Sri Lankan Tamils Demands",
    "difficulty": "Medium",
    "question": "Sri Lankan Tamils launched parties and struggles for: (i) recognition of Tamil as an official language, (ii) regional autonomy, and (iii) equality of opportunity in securing education and jobs. Why were these demands repeatedly denied by the Colombo government?",
    "options": [
      "Because Sinhala leaders adhered strictly to majoritarian dominance and feared losing political supremacy",
      "Because the United Nations forbade regional autonomy in island states",
      "Because Tamils refused to pay taxes to the government",
      "Because Sri Lanka did not have a constitution"
    ],
    "answer": 0,
    "explanation": "Sinhala majoritarian politicians viewed Tamil cultural and political equality as a threat to Sinhala political hegemony, repeatedly rejecting Tamil autonomy demands.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Reserved Constituencies in India",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Indian Constitution provides for reserved constituencies for Scheduled Castes and Scheduled Tribes in the Lok Sabha and State Assemblies.\nReason (R): This arrangement gives space in government and administration to diverse social groups who would otherwise feel alienated from the political system.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Reserved constituencies represent a practical mechanism of power sharing among socially weaker groups, ensuring their legitimate democratic representation.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-009",
    "type": "mcq",
    "subtopic": "Comparison of Electoral Rules",
    "difficulty": "Medium",
    "question": "If a democratic country has 55% majority community A and 45% minority community B, what will happen if it adopts majoritarian democracy without minority safeguards?",
    "options": [
      "Community A can monopolize all government institutions, breeding minority resentment and threatening national integrity",
      "Community B will automatically take over all judicial posts",
      "Both communities will live in permanent harmony without elections",
      "The country will be automatically merged with a neighbouring superpower"
    ],
    "answer": 0,
    "explanation": "Pure majoritarianism without constitutional power-sharing leads to the exclusion of minorities, severe social friction, and potential state fragmentation (as seen in Sri Lanka).",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Brussels Headquarters for European Union",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Brussels was selected as the headquarters of the European Union when European nations unified their community.\nReason (R): Brussels represented an internationally acclaimed symbol of peaceful linguistic accommodation, compromise, and power sharing.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Belgian success in handling complex linguistic divisions peacefully through democratic power sharing made Brussels the natural diplomatic capital of Europe.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-011",
    "type": "mcq",
    "subtopic": "Power Sharing among Organs of Government",
    "difficulty": "Easy",
    "question": "In India, even though the Prime Minister and Council of Ministers are part of the Executive, they are accountable to which constitutional body?",
    "options": ["The Parliament (Legislature)", "The Supreme Court Bar Association", "The Election Commission", "The Union Public Service Commission"],
    "answer": 0,
    "explanation": "Under the parliamentary system and checks and balances, the Executive is drawn from and directly answerable to the elected Parliament.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis - Sri Lanka Civil War Damage",
    "difficulty": "Medium",
    "question": "Sri Lanka had an excellent record of economic development, education, and healthcare in South Asia. What factor caused a catastrophic setback to its social and cultural life?",
    "options": [
      "The protracted civil war triggered by majoritarian policies and denial of power sharing to Tamils",
      "Severe droughts that dried up all tea plantations permanently",
      "A total collapse of international maritime shipping routes",
      "The refusal of foreign tourists to visit tropical islands"
    ],
    "answer": 0,
    "explanation": "The civil war caused a terrible setback to the social, cultural and economic life of Sri Lanka, undermining decades of remarkable human development.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-013",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Coalition Era Democracy",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Coalition governments lead to a new culture of power sharing and respect for the autonomy of State Governments.\nReason (R): In a coalition, the national ruling party depends on regional parties to maintain a parliamentary majority, making unilateral central decisions impossible.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Since no single party secures an absolute majority, alliances necessitate consensus building and mutual respect for regional autonomy.",
    "citation": "NCERT Class 10 Civics, Chapter 1 & 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-014",
    "type": "mcq",
    "subtopic": "Prudential vs Moral Distinction",
    "difficulty": "Hard",
    "question": "Consider the two statements below:\nI. Power sharing is desirable because it avoids bloodshed and civil war.\nII. Power sharing is desirable because democracy requires government with the consent of the governed.\nWhich of the following classifications is correct?",
    "options": [
      "Statement I is Prudential; Statement II is Moral",
      "Statement I is Moral; Statement II is Prudential",
      "Both Statement I and II are Prudential",
      "Both Statement I and II are Moral"
    ],
    "answer": 0,
    "explanation": "Statement I focuses on practical beneficial outcomes (avoiding war = Prudential), while Statement II focuses on intrinsic democratic values (consent of the governed = Moral).",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-015",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Federal vs Unitary Division",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Under a unitary system, either there is only one level of government or the sub-units are subordinate to the central government.\nReason (R): In a federal system, the central government cannot order the state government to do something unconstitutional within the state's jurisdiction.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 1,
    "explanation": "Both statements are correct definitions of unitary and federal systems respectively, though Reason is not the direct causal explanation of Assertion.",
    "citation": "NCERT Class 10 Civics, Chapter 1 & 2"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-016",
    "type": "mcq",
    "subtopic": "Power Sharing in Pressure Group Politics",
    "difficulty": "Medium",
    "question": "Which of the following is an example of indirect power sharing through competitive party politics?",
    "options": [
      "Citizens choosing between different political parties during free and fair elections",
      "A military general suspending the constitution",
      "A monarch selecting a successor from within the royal family",
      "Judges serving lifetime appointments without retirement"
    ],
    "answer": 0,
    "explanation": "Competition among different parties ensures that power does not remain in one hand. In the long run, power is shared among different political parties representing different ideologies.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-017",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Tamil Diaspora Origin",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Sri Lankan Tamils were historically concentrated in the north and east of the island.\nReason (R): Indian Tamils were brought to Sri Lanka during British colonial rule to work as indentured labour on tea and rubber plantations.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 1,
    "explanation": "Both statements are factually correct demographic descriptions from NCERT, but Reason describes Indian Tamils while Assertion describes Sri Lankan Tamils.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-018",
    "type": "mcq",
    "subtopic": "Horizontal vs Vertical Distinction",
    "difficulty": "Easy",
    "question": "Sharing of power between the Union Government, State Governments, and Panchayats is an example of:",
    "options": ["Vertical division of power", "Horizontal checks and balances", "Judicial arbitration", "Military confederacy"],
    "answer": 0,
    "explanation": "Power shared among governments at different vertical levels (Union, State, Local) is called vertical division of power.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-019",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Political Stability via Power Sharing",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Imposing the will of the majority community over minority communities may look attractive in the short run, but undermines national unity in the long run.\nReason (R): Forcing unity through subjugation creates deep-seated grievances that eventually explode into violent secessionist movements.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Forced majoritarianism inevitably creates alienation and rebellion, whereas equitable power sharing preserves peaceful coexistence.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch13-s3-020",
    "type": "mcq",
    "subtopic": "Core Axiom of Democratic Power Sharing",
    "difficulty": "Easy",
    "question": "What is the ultimate purpose of power sharing in a constitutional democracy?",
    "options": [
      "To ensure that power is not concentrated in any single hand and that all citizens have a meaningful voice in governance",
      "To ensure that elections are never conducted again",
      "To eliminate all opposition political parties",
      "To transfer all legislative authority to international corporations"
    ],
    "answer": 0,
    "explanation": "The ultimate purpose of power sharing is to democratize decision-making, respect diversity, prevent authoritarian tyranny, and preserve popular sovereignty.",
    "citation": "NCERT Class 10 Civics, Chapter 1, Section 4 & 5"
  }
]

# Write Chapter 13 Sets 2 and 3
with open(os.path.join(DATA_DIR, "ch13_power_sharing_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch13_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch13_power_sharing_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch13_set3}, f, indent=2, ensure_ascii=False)

print("Generated: ch13 Sets 2 & 3 (40 Qs)")
