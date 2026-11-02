#!/usr/bin/env python3
"""
Generates Civics Ch 16 (Political Parties) Sets 1, 2, 3
and Ch 17 (Outcomes of Democracy) Sets 1, 2, 3.
Total: 6 sets = 120 questions.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# =============================================================================
# CHAPTER 16: POLITICAL PARTIES (Civics Ch 4)
# =============================================================================

ch16_set1 = [
  {
    "id": "cbse10-sst-civ-ch16-s1-001",
    "type": "mcq",
    "subtopic": "Political Party Definition",
    "difficulty": "Easy",
    "question": "A political party is defined as a group of people who come together to:",
    "options": [
      "Contest elections and hold power in the government",
      "Organize religious festivals and pilgrimages",
      "Operate private commercial transport networks",
      "Provide judicial arbitration in civil disputes"
    ],
    "answer": 0,
    "explanation": "A political party is a group of people who come together to contest elections and hold power in the government. They agree on some policies and programmes for the society with a view to promote the collective good.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-002",
    "type": "mcq",
    "subtopic": "Three Components of a Political Party",
    "difficulty": "Easy",
    "question": "A political party has three core components. Which of the following correctly identifies all three?",
    "options": [
      "The leaders, the active members, and the followers",
      "The prime minister, the supreme court judges, and the police",
      "The president, the governor, and the chief election commissioner",
      "The civil servants, the army generals, and the media reporters"
    ],
    "answer": 0,
    "explanation": "A political party has three components: (i) the leaders, (ii) the active members, and (iii) the followers.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-003",
    "type": "mcq",
    "subtopic": "Partisanship Definition",
    "difficulty": "Medium",
    "question": "A person who is strongly committed to a party, group, or faction, and is marked by a tendency to take a side and an inability to take a balanced view, is known as a:",
    "options": ["Partisan", "Defector", "Dissident", "Pluralist"],
    "answer": 0,
    "explanation": "A partisan is a person who is strongly committed to a party, group or faction. Partisanship is marked by a tendency to take a side and inability to take a balanced view on an issue.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-004",
    "type": "mcq",
    "subtopic": "Functions of Political Parties - Making Laws",
    "difficulty": "Medium",
    "question": "Parties play a decisive role in making laws for a country. Formally, laws are debated and passed in the legislature, but most members belong to a party and go by:",
    "options": [
      "The direction of the party leadership, irrespective of their personal opinions",
      "Secret lottery draws held by the speaker",
      "Orders issued by foreign international agencies",
      "Instructions given by local municipal ward corporators"
    ],
    "answer": 0,
    "explanation": "Parties play a decisive role in making laws for a country. Formally, laws are debated and passed in the legislature. But since most of the members belong to a party, they go by the direction of the party leadership, irrespective of their personal opinions.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-005",
    "type": "mcq",
    "subtopic": "Role of the Opposition",
    "difficulty": "Easy",
    "question": "Those parties that lose in the elections play the vital constitutional role of opposition by:",
    "options": [
      "Voicing different views and criticising government for its failures or wrong policies",
      "Suspending the sittings of the High Court",
      "Calling upon the military to seize executive power",
      "Refusing to participate in any future democratic elections"
    ],
    "answer": 0,
    "explanation": "Those parties that lose in the elections play the role of opposition to the parties in power, by voicing different views and criticising government for its failures or wrong policies.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-006",
    "type": "mcq",
    "subtopic": "Necessity of Political Parties Thought Experiment",
    "difficulty": "Board Standard",
    "question": "Imagine a situation without political parties where every candidate in an election is independent. What would be the major consequence?",
    "options": [
      "No one will be able to make any promises to the people about any major policy changes, and no one will be responsible for how the country will be run",
      "All public corruption would vanish instantly overnight",
      "Economic growth would accelerate to 100% per annum",
      "Elections would be completely free of any financial expenditure"
    ],
    "answer": 0,
    "explanation": "If every candidate is independent, no one will be able to make any promises to the people about any major policy changes. The government may be formed, but its utility will remain ever uncertain. Elected representatives will be accountable to their constituency for what they do in the locality, but no one will be responsible for how the country will be run.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-007",
    "type": "mcq",
    "subtopic": "One-Party System Example",
    "difficulty": "Easy",
    "question": "Which of the following countries is a prominent example of a 'One-Party System' where only one party is legally permitted to control and run the government?",
    "options": ["China (Communist Party)", "United States of America", "India", "United Kingdom"],
    "answer": 0,
    "explanation": "In China, only the Communist Party is allowed to rule. Although legally people are free to form political parties, the electoral system does not permit free competition for power.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-008",
    "type": "mcq",
    "subtopic": "Two-Party System Example",
    "difficulty": "Easy",
    "question": "In which pair of countries does a 'Two-Party System' operate, where power usually alternates between two major political parties?",
    "options": [
      "United States of America and United Kingdom",
      "India and Pakistan",
      "China and North Korea",
      "France and Italy"
    ],
    "answer": 0,
    "explanation": "In some countries, power usually changes between two main parties. The United States of America and the United Kingdom are examples of a two-party system.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-009",
    "type": "mcq",
    "subtopic": "Multi-Party System in India",
    "difficulty": "Medium",
    "question": "Why has India evolved a Multi-Party System rather than a one-party or two-party system?",
    "options": [
      "Because the vast social and geographical diversity in such a large country cannot be easily absorbed by two or three parties",
      "Because the Constitution bans any two parties from merging",
      "Because Indian voters are required to register in at least three parties simultaneously",
      "Because multi-party systems eliminate the need for an Election Commission"
    ],
    "answer": 0,
    "explanation": "Party system is not something any country can choose. It evolves over a long time, depending on the nature of society, its social and regional divisions, its history of politics and its system of elections. India has evolved a multi-party system because the social and geographical diversity in such a large country is not easily absorbed by two or even three parties.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-010",
    "type": "mcq",
    "subtopic": "National Party Eligibility Criteria",
    "difficulty": "Hard",
    "question": "According to the Election Commission of India, a party that secures at least what percentage of total votes and wins how many seats is recognized as a 'National Party'?",
    "options": [
      "At least 6% of the total votes in Lok Sabha elections OR Assembly elections in four states, AND wins at least 4 seats in the Lok Sabha",
      "At least 50% of the total votes in any single state",
      "At least 10 seats in the Rajya Sabha and 1 seat in the Lok Sabha",
      "At least 25% of the total votes across all southern states"
    ],
    "answer": 0,
    "explanation": "A party that secures at least six per cent of the total votes in Lok Sabha elections or Assembly elections in four States and wins at least four seats in the Lok Sabha is recognised as a national party.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-011",
    "type": "mcq",
    "subtopic": "State Party Eligibility Criteria",
    "difficulty": "Hard",
    "question": "What is the criteria laid down by the Election Commission of India for recognition as a 'State Party' (regional party)?",
    "options": [
      "A party that secures at least 6% of the total votes in an election to the Legislative Assembly of a State and wins at least 2 seats",
      "A party that wins at least 50 seats in the Lok Sabha",
      "A party that has offices in at least 20 different states",
      "A party whose president is a sitting Chief Minister"
    ],
    "answer": 0,
    "explanation": "A party that secures at least six per cent of the total votes in an election to the Legislative Assembly of a State and wins at least two seats is recognised as a State party.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-012",
    "type": "mcq",
    "subtopic": "Bharatiya Janata Party (BJP) Philosophy",
    "difficulty": "Medium",
    "question": "The Bharatiya Janata Party (founded in 1980 by reviving the Bharatiya Jana Sangh) draws inspiration from which cultural concept articulated by Deendayal Upadhyaya?",
    "options": [
      "Integral Humanism and Antyodaya, with cultural nationalism (Hindutva)",
      "Proletarian dictatorship and Marxist-Leninism",
      "Fabian socialism and democratic centralism",
      "Laissez-faire unbridled corporate capitalism"
    ],
    "answer": 0,
    "explanation": "Cultural nationalism (or 'Hindutva') is an important element in its conception of Indian nationhood and politics. It draws inspiration from ancient Indian culture, Deendayal Upadhyaya's ideas of integral humanism and Antyodaya.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-013",
    "type": "mcq",
    "subtopic": "Indian National Congress (INC) Stance",
    "difficulty": "Medium",
    "question": "The Indian National Congress (popularly known as the Congress Party, founded in 1885) espouses which political orientation in its ideological posture?",
    "options": [
      "A centrist party (neither rightist nor leftist) supporting secularism and welfare of weaker sections",
      "An extreme far-right militarist party",
      "A revolutionary communist party seeking armed insurrection",
      "A single-issue environmental green party"
    ],
    "answer": 0,
    "explanation": "Under the leadership of Jawaharlal Nehru, the party sought to build a modern secular democratic republic in India. A centrist party in its ideological orientation, it espouses secularism and welfare of weaker sections and minorities.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-014",
    "type": "mcq",
    "subtopic": "Bahujan Samaj Party (BSP) Philosophy",
    "difficulty": "Medium",
    "question": "Formed in 1984 under the leadership of Kanshi Ram, the Bahujan Samaj Party (BSP) seeks to represent and secure power for the 'Bahujan Samaj', which includes:",
    "options": [
      "Dalits, Adivasis, OBCs, and religious minorities",
      "Urban corporate industrial executives only",
      "Non-resident Indian foreign investors",
      "Traditional feudal royal families"
    ],
    "answer": 0,
    "explanation": "Formed in 1984 under the leadership of Kanshi Ram, it seeks to represent and secure power for the bahujan samaj which includes the dalits, adivasis, OBCs and religious minorities. It draws inspiration from the ideas of Sahu Maharaj, Mahatma Phule, Periyar and Babasaheb Ambedkar.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-015",
    "type": "mcq",
    "subtopic": "Communist Party of India (Marxist) - CPI(M)",
    "difficulty": "Medium",
    "question": "Founded in 1964, the CPI(M) believes in Marxism-Leninism, supports socialism, secularism and democracy, and enjoys its strongest mass base in:",
    "options": ["West Bengal, Kerala, and Tripura", "Gujarat, Rajasthan, and Haryana", "Maharashtra, Goa, and Karnataka", "Uttar Pradesh and Bihar"],
    "answer": 0,
    "explanation": "CPI(M) was in power in West Bengal without a break for 34 years. It enjoys strong support in West Bengal, Kerala and Tripura, especially among factory workers, farmers, agricultural labourers and the intelligentsia.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-016",
    "type": "mcq",
    "subtopic": "Aam Aadmi Party (AAP) Recognition",
    "difficulty": "Easy",
    "question": "Formed in 2012 following the India Against Corruption movement, which political party emerged as a recognized National Party by forming governments in Delhi and Punjab?",
    "options": ["Aam Aadmi Party (AAP)", "Janata Dal (United)", "Samajwadi Party", "Rashtriya Janata Dal"],
    "answer": 0,
    "explanation": "Aam Aadmi Party (AAP), formed in 2012, espouses accountability, clean governance, and education/health reforms, securing national party status after strong performances in Delhi, Punjab, Goa, and Gujarat.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-017",
    "type": "mcq",
    "subtopic": "First Challenge: Lack of Internal Democracy",
    "difficulty": "Board Standard",
    "question": "The first major challenge faced by political parties in India is the 'lack of internal democracy'. This primarily manifests as:",
    "options": [
      "Concentration of power in one or a few top leaders; parties do not hold regular organizational elections or maintain membership registers",
      "Voters being barred from voting on voting day",
      "The Supreme Court drafting political manifestos",
      "All party members receiving identical government salaries"
    ],
    "answer": 0,
    "explanation": "All over the world there is a tendency in political parties towards the concentration of power in one or few leaders at the top. Parties do not keep membership registers, do not hold organisational meetings, and do not conduct internal elections regularly.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-018",
    "type": "mcq",
    "subtopic": "Second Challenge: Dynastic Succession",
    "difficulty": "Easy",
    "question": "The challenge of 'Dynastic Succession' in political parties refers to the practice where:",
    "options": [
      "Top positions are always controlled by members of one family, denying ordinary workers fair opportunity to rise",
      "Ministers are chosen exclusively from the civil service",
      "Political leaders pass an annual physical fitness test",
      "Party presidency changes every month by lottery"
    ],
    "answer": 0,
    "explanation": "Since most political parties do not practice open and transparent procedures for their functioning, there are very few ways for an ordinary worker to rise to the top. Those who happen to be the leaders are in a position of unfair advantage to favour people close to them or even their family members.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-019",
    "type": "mcq",
    "subtopic": "Third Challenge: Money and Muscle Power",
    "difficulty": "Medium",
    "question": "The growing role of 'money and muscle power' in political parties during elections results in:",
    "options": [
      "Parties nominating rich candidates or criminals who can raise funds and win seats, rather than ideologically committed workers",
      "The abolition of all private banks in India",
      "The elimination of electronic voting machines",
      "A complete ban on television election news broadcasts"
    ],
    "answer": 0,
    "explanation": "Since parties are focused only on winning elections, they tend to use short-cuts to win elections. They tend to nominate those candidates who have or can raise lots of money. Rich people and companies who give funds to the parties tend to have influence on the policies and decisions of the party. In some cases, parties support criminals who can win elections.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s1-020",
    "type": "mcq",
    "subtopic": "Fourth Challenge: Lack of Meaningful Choice",
    "difficulty": "Medium",
    "question": "The fourth challenge to political parties is that very often they do not seem to offer a 'meaningful choice' to voters. Why is this so in recent decades?",
    "options": [
      "There is a significant ideological convergence where major parties agree on fundamental economic policies, differing only in minor details",
      "All parties use identical election symbols on the ballot",
      "Candidates are chosen by foreign ambassadors",
      "Voters are prohibited from reading political newspapers"
    ],
    "answer": 0,
    "explanation": "In recent years there has been a decline in the ideological differences among parties in most parts of the world. For example, the difference between the Labour Party and the Conservative Party in Britain is very little. In India too, the differences among all the major parties on the economic policies have reduced.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  }
]

# Write Chapter 16 Set 1
with open(os.path.join(DATA_DIR, "ch16_political_parties_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch16_set1}, f, indent=2, ensure_ascii=False)

print("Generated: ch16_political_parties_set1.json (20 Qs)")

# -----------------------------------------------------------------------------
# CH 16 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch16_set2 = [
  {
    "id": "cbse10-sst-civ-ch16-s2-001",
    "type": "mcq",
    "subtopic": "Anti-Defection Law",
    "difficulty": "Easy",
    "question": "The Constitution was amended (52nd Amendment) to introduce the Anti-Defection Law primarily to prevent:",
    "options": [
      "Elected MLAs and MPs from changing parties after being elected in order to become ministers or for cash payoffs",
      "Voters from casting negative votes in elections",
      "New political parties from registering with the Election Commission",
      "Judges from hearing election petition cases"
    ],
    "answer": 0,
    "explanation": "The Constitution was amended to prevent elected MLAs and MPs from changing parties. This was done because many elected representatives were indulging in defection in order to become ministers or for cash rewards. Now the law says that if any MLA or MP changes parties, he or she will lose the seat in the legislature.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-002",
    "type": "mcq",
    "subtopic": "Supreme Court Affidavit Order",
    "difficulty": "Medium",
    "question": "To reduce the influence of money and criminals in elections, what mandatory requirement was passed by the Supreme Court of India?",
    "options": [
      "Every candidate contesting elections must file an Affidavit giving details of their property and criminal cases pending against them",
      "Candidates must pay a cash deposit of 10 crore rupees",
      "Criminals are given automatic pardons before election day",
      "Candidates must transfer all their personal assets to the state treasury"
    ],
    "answer": 0,
    "explanation": "The Supreme Court passed an order to reduce the influence of money and criminals. Now, it is mandatory for every candidate who contests elections to file an AFFIDAVIT giving details of his property and criminal cases pending against him. This made a lot of information available to the public.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-003",
    "type": "mcq",
    "subtopic": "Affidavit Definition",
    "difficulty": "Easy",
    "question": "What is an 'Affidavit' in the context of election nominations?",
    "options": [
      "A signed document submitted to an officer, where a person makes a sworn statement regarding their personal information",
      "A party manifesto promising free electricity to voters",
      "A secret ballot paper used by military officers",
      "A court warrant ordering the arrest of a politician"
    ],
    "answer": 0,
    "explanation": "An affidavit is a signed document submitted to an officer, where a person makes a sworn statement regarding his/her personal information.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-004",
    "type": "mcq",
    "subtopic": "ECI Mandatory Internal Elections Order",
    "difficulty": "Medium",
    "question": "The Election Commission of India passed an order making it necessary for political parties to:",
    "options": [
      "Hold their organizational elections and file their income tax returns",
      "Nominate candidates exclusively below the age of 25",
      "Disband all regional party branches",
      "Hand over all party funds to the Union Finance Ministry"
    ],
    "answer": 0,
    "explanation": "The Election Commission passed an order making it necessary for political parties to hold their organisational elections and file their income tax returns.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-005",
    "type": "mcq",
    "subtopic": "State Funding of Elections Proposal",
    "difficulty": "Medium",
    "question": "What is meant by the reform proposal of 'State Funding of Elections'?",
    "options": [
      "The government should give parties money/resources (petrol, paper, telephone) to support their election expenses, reducing reliance on corporate donors",
      "The state government should purchase all commercial radio stations during elections",
      "Citizens should be fined if their chosen party loses an election",
      "All election campaign advertisements should be paid for by foreign embassies"
    ],
    "answer": 0,
    "explanation": "There should be state funding of elections. The government should give parties money to support their election expenses. This support could be given in kind: petrol, paper, telephone etc., or it could be given in cash on the basis of the votes secured by the party in the last election.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-006",
    "type": "mcq",
    "subtopic": "Women Quota in Party Tickets Proposal",
    "difficulty": "Medium",
    "question": "To ensure greater participation of women in legislative bodies, what reform has been strongly recommended for political parties?",
    "options": [
      "It should be made mandatory for political parties to give a minimum proportion of tickets (about one-third) to women candidates",
      "Women should be barred from becoming party treasurers",
      "Only men should contest urban municipal corporation seats",
      "Political party membership should be restricted to retired judges"
    ],
    "answer": 0,
    "explanation": "It should be made mandatory for political parties to give a minimum number of tickets, about one-third, to women candidates. Similarly, there should be a quota for women in the decision-making bodies of the party.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-007",
    "type": "mcq",
    "subtopic": "Nationalist Congress Party (NCP)",
    "difficulty": "Easy",
    "question": "Formed in 1999 following a split in the Congress Party, the Nationalist Congress Party (NCP) espouses democracy, Gandhian secularism, equity, social justice, and federalism, and has a major presence in:",
    "options": ["Maharashtra", "Punjab", "Tamil Nadu", "Assam"],
    "answer": 0,
    "explanation": "Formed in 1999 following a split in the Congress Party, NCP espouses democracy, Gandhian secularism, equity, social justice and federalism. It has a major presence in Maharashtra.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-008",
    "type": "mcq",
    "subtopic": "All India Trinamool Congress (AITC)",
    "difficulty": "Easy",
    "question": "Launched on 1 January 1998 under the leadership of Mamata Banerjee, the All India Trinamool Congress (AITC) was recognized as a National Party in 2016 and has been in power in which state since 2011?",
    "options": ["West Bengal", "Odisha", "Tripura", "Jharkhand"],
    "answer": 0,
    "explanation": "Launched on 1 January 1998 under the leadership of Mamata Banerjee, recognised as a national party in 2016, the party's symbol is flowers and grass. Committed to secularism and federalism, it has been in power in West Bengal since 2011.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-009",
    "type": "mcq",
    "subtopic": "State Parties Strengthening Federalism",
    "difficulty": "Board Standard",
    "question": "Over the last three decades, the number and strength of regional and State Parties has expanded. What direct impact has this had on the Indian Parliament?",
    "options": [
      "No single national party was able to secure an absolute majority on its own for decades, compelling national parties into federal coalitions with State Parties",
      "State parties were permanently barred from speaking in the Lok Sabha",
      "The Parliament was reduced to an advisory club without legislative powers",
      "The Rajya Sabha was dissolved and replaced by a judicial committee"
    ],
    "answer": 0,
    "explanation": "Before 2014, no one national party was able to secure on its own a majority in Lok Sabha. As a result, the national parties were compelled to form alliances with State parties, making our Parliament politically more diverse and strengthening federalism.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-010",
    "type": "mcq",
    "subtopic": "Public Pressure for Party Reforms",
    "difficulty": "Medium",
    "question": "How can ordinary citizens, media, and civil society pressure political parties into reforming their internal functioning?",
    "options": [
      "Through petitions, publicity, protest movements, and voting against unresponsive corrupt parties in elections",
      "By staging violent attacks on government treasuries",
      "By refusing to send their children to government schools",
      "By surrendering their Indian citizenship cards"
    ],
    "answer": 0,
    "explanation": "People can put pressure on political parties. This can be done through petitions, publicity and agitations. Ordinary citizens, pressure groups, movements and the media can play an important role in this. If parties feel that they would lose public support by not taking up reforms, they will become more serious about reforms.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-011",
    "type": "mcq",
    "subtopic": "CPI Foundation Year",
    "difficulty": "Easy",
    "question": "Formed in 1925, believing in Marxism-Leninism, secularism and democracy, and opposing forces of secessionism and communalism, is which historic party?",
    "options": [
      "Communist Party of India (CPI)",
      "Bharatiya Janata Party (BJP)",
      "Indian National Congress (INC)",
      "Bahujan Samaj Party (BSP)"
    ],
    "answer": 0,
    "explanation": "The Communist Party of India (CPI) was formed in 1925. It believes in Marxism-Leninism, secularism and democracy and opposed secessionism and communalism.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-012",
    "type": "mcq",
    "subtopic": "Shaping Public Opinion Function",
    "difficulty": "Medium",
    "question": "Political parties shape public opinion primarily through which of the following mechanisms?",
    "options": [
      "They raise and highlight issues; parties have lakhs of members and activists spread all over the country and launch movements for resolving citizens' grievances",
      "They ban all private news channels from broadcasting during monsoons",
      "They pass judicial verdicts on criminal appeals",
      "They operate private commercial airlines"
    ],
    "answer": 0,
    "explanation": "Parties shape public opinion. They raise and highlight issues. Parties have lakhs of members and activists spread all over the country. Many of the pressure groups are the extensions of political parties among different sections of society.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-013",
    "type": "mcq",
    "subtopic": "Parties Providing Access to Government Schemes",
    "difficulty": "Medium",
    "question": "Why do ordinary citizens, especially in rural villages, find it easier to approach a local party leader than a government officer?",
    "options": [
      "Party leaders feel close to local citizens and are responsive to their needs, knowing they have to face voters in the next election",
      "Government officers live exclusively in foreign embassies",
      "Party leaders have legal authority to arrest anyone who enters a police station",
      "Government officers refuse to speak the local language"
    ],
    "answer": 0,
    "explanation": "For an ordinary citizen, it is easy to approach a local party leader than a government officer. That is why they feel close to parties even when they do not fully trust them. Parties have to be responsive to people's needs and demands, otherwise people can reject them in the next elections.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-014",
    "type": "mcq",
    "subtopic": "Coalition Alliances in 2004",
    "difficulty": "Board Standard",
    "question": "In the 2004 parliamentary elections in India, which three major multi-party coalitions dominated the electoral landscape?",
    "options": [
      "National Democratic Alliance (NDA), United Progressive Alliance (UPA), and Left Front",
      "Whigs, Tories, and Labour Party",
      "Federalists, Republicans, and Democrats",
      "Bolsheviks, Mensheviks, and Social Revolutionaries"
    ],
    "answer": 0,
    "explanation": "In India, there were three such major alliances in 2004 parliamentary elections — the National Democratic Alliance (NDA), the United Progressive Alliance (UPA) and the Left Front.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-015",
    "type": "mcq",
    "subtopic": "Multi-Party Coalition Instability Myth vs Reality",
    "difficulty": "Medium",
    "question": "While a multi-party system often appears messy and leads to political coalitions, its greatest democratic virtue is that:",
    "options": [
      "It allows a variety of diverse interests and opinions to enjoy political representation in governance",
      "It makes the Prime Minister an absolute monarch",
      "It completely eliminates the need for taxation",
      "It guarantees that no laws are ever enacted in the parliament"
    ],
    "answer": 0,
    "explanation": "The multi-party system often appears very messy and leads to political instability. At the same time, this system allows a variety of interests and opinions to enjoy political representation.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-016",
    "type": "mcq",
    "subtopic": "Internal Party Dispute Regulation Proposal",
    "difficulty": "Medium",
    "question": "What legal reform has been proposed to regulate the internal affairs of political parties in India?",
    "options": [
      "Enacting a law making it mandatory for parties to maintain a register of members, follow their own constitution, and have an independent authority to judge internal disputes",
      "Dissolving all political party central offices and holding rallies in sports stadiums only",
      "Allowing party presidents to appoint their sons as permanent successors",
      "Making party manifestos legally enforceable under criminal treason laws"
    ],
    "answer": 0,
    "explanation": "A law should be made to regulate the internal affairs of political parties. It should be made compulsory for political parties to maintain a register of its members, to follow its own constitution, to have an independent authority to act as a judge in case of party disputes.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-017",
    "type": "mcq",
    "subtopic": "Defection Definition",
    "difficulty": "Easy",
    "question": "Changing party allegiance from the party on whose ticket a person got elected to a legislative body to a different party is formally known as:",
    "options": ["Defection", "Partisanship", "Coalition formation", "Dissolution"],
    "answer": 0,
    "explanation": "Defection refers to changing party allegiance from the party on which a person got elected (to a legislative body) to a different party.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-018",
    "type": "mcq",
    "subtopic": "Berlusconi Conflict of Interest Cartoon",
    "difficulty": "Medium",
    "question": "The famous NCERT cartoon about Italian Prime Minister Silvio Berlusconi owning major television channels, a newspaper, and a football club highlights which dangerous modern challenge to democracy?",
    "options": [
      "Concentration of media ownership and political power in the hands of wealthy tycoons",
      "The total failure of football clubs in European politics",
      "The prohibition of private newspapers in Italy",
      "The lack of television sets in rural households"
    ],
    "answer": 0,
    "explanation": "The Berlusconi cartoon illustrates the dangerous nexus between corporate wealth, media ownership monopoly, and political office, undermining free democratic accountability.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Cartoon Study (Berlusconi)"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-019",
    "type": "mcq",
    "subtopic": "Quality of Democracy and Public Involvement",
    "difficulty": "Board Standard",
    "question": "Ultimately, the quality of a democracy and the responsiveness of its political parties depends on:",
    "options": [
      "The degree of public participation; democracy cannot be improved if ordinary citizens merely criticize from outside without joining politics",
      "The total amount of gold held in the central bank",
      "The length of constitutional textbooks taught in schools",
      "The speed of supersonic jet fighters owned by the military"
    ],
    "answer": 0,
    "explanation": "The quality of democracy depends on the degree of public participation. It is difficult to reform politics if ordinary citizens do not take part in it and simply criticise it from the outside. The problem of bad politics can be solved by more politics and better politics.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s2-020",
    "type": "mcq",
    "subtopic": "Election Commission Symbol Allocation",
    "difficulty": "Easy",
    "question": "Every political party in India has to register with the Election Commission. What unique facility is granted to recognized 'National' and 'State' parties?",
    "options": [
      "An exclusive official election symbol that only that party's official candidates can use",
      "100 crore rupees of cash before every election",
      "Immunity from all Indian criminal and civil laws",
      "Free fuel for all party members' private cars"
    ],
    "answer": 0,
    "explanation": "The Election Commission offers some special facilities to large and established parties. They are given a unique symbol — only the official candidates of that party can use that election symbol. Parties that get this privilege and some other special facilities are 'recognised' by the Election Commission.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3"
  }
]

# -----------------------------------------------------------------------------
# CH 16 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch16_set3 = [
  {
    "id": "cbse10-sst-civ-ch16-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Necessity of Political Parties",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Modern representative democracies cannot exist without political parties.\nReason (R): Political parties aggregate diverse public opinions into coherent policy directions, form accountable governments, and provide a legitimate opposition.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Without parties, candidates would be fragmented and unable to formulate national policies or accept collective accountability for governance.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Anti-Defection Constitutional Amendment",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Anti-Defection law has helped bring down political corruption and unprincipled party hopping.\nReason (R): Any elected MP or MLA who defects to another party loses their seat in the legislature immediately.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The constitutional penalty of disqualification creates a strong deterrent against opportunistic floor crossing for money or ministerial posts.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Lack of Internal Democracy Impact",
    "difficulty": "Board Standard",
    "question": "Assertion (A): In most political parties, ordinary members do not know what happens inside the party and cannot influence major decisions.\nReason (R): There is a global tendency towards the concentration of power in one or few top leaders who decide tickets and party policy.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Absence of regular organizational elections and internal debate causes ordinary workers to become mere foot soldiers, while supreme authority concentrates at the top.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Dynastic Succession Inefficiency",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Dynastic succession in political parties is harmful to the health of democracy.\nReason (R): People who do not have adequate experience or popular grassroots support often come to occupy positions of supreme power simply by virtue of their birth.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Dynastic nepotism deprives competent grassroots leaders of fair opportunities and places inexperienced family scions in control of national governance.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Evolution of Party System",
    "difficulty": "Board Standard",
    "question": "Assertion (A): A country cannot artificially choose its party system; it evolves over decades.\nReason (R): Party systems reflect a nation's social and regional divisions, history of politics, and electoral geography.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "No country can simply adopt a one-party, two-party, or multi-party system by decree. It is an organic product of societal diversity and historical struggles.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-006",
    "type": "case_based",
    "subtopic": "Case Analysis - Candidate Selection Dilemma",
    "difficulty": "Medium",
    "question": "A political party in an upcoming state election rejects a loyal grassroots worker of 20 years who runs free evening schools, and instead nominates a wealthy mining baron who joined the party three days ago and has multiple criminal extortion charges. What structural pathology of modern party politics does this exemplify?",
    "options": [
      "The growing, corrosive influence of money and muscle power in winnability calculations",
      "Strict adherence to democratic meritocracy",
      "Compliance with the Supreme Court's ethical guidelines",
      "Application of the Panchayati Raj quota system"
    ],
    "answer": 0,
    "explanation": "Parties focused purely on electoral victory prioritize candidates who can self-finance expensive campaigns or exert muscle power, sidelining principled public servants.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-007",
    "type": "case_based",
    "subtopic": "Case Analysis - Coalition Compromise",
    "difficulty": "Medium",
    "question": "A national coalition government consists of 8 different parties. When the leading party attempts to pass a national retail reform bill, two regional coalition partners threaten to withdraw support unless agricultural subsidies in their states are doubled. What aspect of coalition governance does this demonstrate?",
    "options": [
      "Coalition governance forces consensus and bargaining, preventing unilateral central imposition while accommodating regional interests",
      "The complete breakdown of the Indian Constitution",
      "The superiority of one-party dictatorships",
      "The abolition of the Supreme Court's power"
    ],
    "answer": 0,
    "explanation": "Coalitions balance national initiatives with regional sensitivities through ongoing negotiation and mutual compromise.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Supreme Court Affidavit Limitation",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The mandatory filing of Affidavits has made rich information about candidates' assets and criminal records available to the public.\nReason (R): However, there is no official system to verify if the information provided by candidates in the affidavit is true, and it has not yet led to a decline in rich or criminal candidates.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 1,
    "explanation": "Both statements are correct facts from NCERT. Reason describes the current enforcement limitation of affidavits, while Assertion notes the breakthrough in transparency.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-009",
    "type": "mcq",
    "subtopic": "Recognized National Parties Criteria",
    "difficulty": "Medium",
    "question": "Which of the following parties is recognized as a 'National Party' in India based on widespread electoral presence and vote share across multiple states?",
    "options": [
      "Bharatiya Janata Party (BJP)",
      "Shiromani Akali Dal",
      "Dravida Munnetra Kazhagam (DMK)",
      "Biju Janata Dal (BJD)"
    ],
    "answer": 0,
    "explanation": "BJP, INC, BSP, CPI(M), AAP, and NPP are recognized National Parties, whereas Akali Dal, DMK, and BJD are recognized State/regional parties.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Opposition as Democratic Guardian",
    "difficulty": "Board Standard",
    "question": "Assertion (A): A vibrant opposition is as essential to democracy as the ruling government.\nReason (R): The opposition mobilises public opinion against anti-people policies, checks executive corruption, and offers alternative policy solutions.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "A democracy without an active opposition risks degenerating into an authoritarian dictatorship where rulers face zero accountability.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-011",
    "type": "mcq",
    "subtopic": "Ideological Convergence Hazard",
    "difficulty": "Medium",
    "question": "When all major political parties adopt nearly identical economic and social policies, what negative dilemma does the voter face?",
    "options": [
      "A lack of meaningful choice; voters who want fundamentally different economic policies have no viable party option to vote for",
      "Voters are forced to pay double poll taxes",
      "The ballot paper becomes 50 meters long",
      "The Election Commission cancels the election"
    ],
    "answer": 0,
    "explanation": "A meaningful choice requires parties to offer genuinely different ideological options. When parties agree on core policies, voters can only choose different personalities, not different policies.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis - Defection and Anti-Defection Enforcement",
    "difficulty": "Medium",
    "question": "An elected MLA from Party A votes against her own party's no-confidence motion in the assembly after being promised a cabinet ministry by rival Party B. Under the Anti-Defection Law, what legal consequence will she face?",
    "options": [
      "She will lose her seat in the legislative assembly and be disqualified as an MLA",
      "She will be rewarded with a seat in the Rajya Sabha automatically",
      "She will be appointed Chief Justice of the state",
      "Nothing; party loyalty is completely optional under the law"
    ],
    "answer": 0,
    "explanation": "Under the 52nd Constitutional Amendment (Anti-Defection Law), voting against the party whip or defecting to another party results in forfeiture of legislative membership.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-013",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Partisanship and Public Division",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Political parties reflect fundamental political divisions in a society.\nReason (R): Parties are about a part of the society and thus involve partisanship, championing the interests of certain social classes over others.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Because a party represents a segment of society, party competition inevitably articulates and reflects existing social, regional, and economic cleavages.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-014",
    "type": "mcq",
    "subtopic": "State Parties National Coalitions Historical Role",
    "difficulty": "Board Standard",
    "question": "How did regional state parties like Samajwadi Party, DMK, TMC, and JD(U) contribute to Indian national governance between 1996 and 2014?",
    "options": [
      "Nearly every state party got an opportunity to be part of one or the other national level coalition government at the Centre",
      "They permanently abolished national general elections",
      "They prevented the Union Government from collecting customs duties",
      "They converted India into a loose confederation without a central army"
    ],
    "answer": 0,
    "explanation": "Since 1996, nearly every one of the State parties got an opportunity to be a part of one or the other national coalition government, making national governance truly federal.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-015",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Need for State Funding",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Proponents of democratic reform advocate for state funding of elections in India.\nReason (R): State funding of election expenses would level the playing field and liberate political parties from financial subservience to corporate oligarchs and criminal syndicates.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Public funding of elections in cash or kind curbs the corrupting influence of black money and corporate donations in candidate selection and policy making.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-016",
    "type": "mcq",
    "subtopic": "One-Party Democracy Absence",
    "difficulty": "Easy",
    "question": "Why is a one-party system (like China's Communist Party rule) not considered a democratic option?",
    "options": [
      "Because a democratic system must allow at least two parties to compete in elections and provide a fair chance for the competing parties to come to power",
      "Because one-party systems do not allow people to use smartphones",
      "Because China has zero public factories",
      "Because single parties are banned by the World Bank"
    ],
    "answer": 0,
    "explanation": "We cannot consider one-party system as a good option because this is not a democratic option. Any democratic system must allow at least two parties to compete in elections and provide a fair chance for the competing parties to come to power.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-017",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Parties Forming Government",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Political parties recruit leaders, train them, and make them ministers to run the government.\nReason (R): In a parliamentary democracy, executive ministers must enjoy the political confidence of the legislative majority.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Parties train and field leaders who, upon securing a parliamentary majority, form the Council of Ministers to execute party policies through the state machinery.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.1"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-018",
    "type": "mcq",
    "subtopic": "Anti-Defection Law Unintended Consequence",
    "difficulty": "Hard",
    "question": "What has been an unintended negative side-effect of the Anti-Defection Law on parliamentary debate in India?",
    "options": [
      "It has made all dissent within parties difficult; MPs and MLAs must blindly vote according to the party whip, reducing individual conscience",
      "It caused all parliamentary committees to be abolished",
      "It allowed MPs to vote without attending parliament",
      "It banned ministers from answering questions in Question Hour"
    ],
    "answer": 0,
    "explanation": "While preventing corrupt defection, the law has made any dissent difficult. MPs and MLAs must accept whatever the party leadership decides, curbing open internal debate.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-019",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Political Reforms through Citizens",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Legal solutions alone cannot completely eliminate corruption or undemocratic practices within political parties.\nReason (R): Over-regulation through laws can lead to parties finding clever loopholes; genuine reform requires active citizen participation, public vigilance, and media exposure.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Laws are necessary but not sufficient. Sustainable political hygiene depends on active citizen participation, voter education, and grassroots political engagement.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 5"
  },
  {
    "id": "cbse10-sst-civ-ch16-s3-020",
    "type": "mcq",
    "subtopic": "Summary Axiom on Political Parties",
    "difficulty": "Easy",
    "question": "In conclusion, political parties are indispensable to representative democracy because they act as:",
    "options": [
      "An essential agency that gathers different views on various issues and presents them to the government, ensuring popular sovereignty",
      "Military training academies for civil defense",
      "Tax collection agencies replacing the revenue department",
      "Commercial marketing corporations selling voter databases"
    ],
    "answer": 0,
    "explanation": "Political parties act as an institutional bridge between civil society and the state, articulating popular will and rendering rulers accountable to the electorate.",
    "citation": "NCERT Class 10 Civics, Chapter 4, Section 1.2"
  }
]

# Write Chapter 16 Sets 2 and 3
with open(os.path.join(DATA_DIR, "ch16_political_parties_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch16_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch16_political_parties_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch16_set3}, f, indent=2, ensure_ascii=False)

print("Generated: ch16 Sets 2 & 3 (40 Qs)")
