#!/usr/bin/env python3
"""
Generates Civics Ch 15 (Gender, Religion and Caste) Sets 1, 2, 3.
Total: 3 sets = 60 questions.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# -----------------------------------------------------------------------------
# CH 15 SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch15_set1 = [
  {
    "id": "cbse10-sst-civ-ch15-s1-001",
    "type": "mcq",
    "subtopic": "Sexual Division of Labour Definition",
    "difficulty": "Easy",
    "question": "A system in which all work inside the home is either done by the women of the family, or organised by them through domestic helpers, is termed:",
    "options": ["Sexual division of labour", "Occupational mobility", "Feminist hierarchy", "Secular division"],
    "answer": 0,
    "explanation": "Sexual division of labour is a system in which all work inside the home is either done by the women of the family, or organised by them through domestic helpers.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-002",
    "type": "mcq",
    "subtopic": "Feminist Movement Objective",
    "difficulty": "Easy",
    "question": "Movements aimed at achieving equal rights, voting franchise, educational access, and career opportunities for women are known as:",
    "options": ["Feminist movements", "Communal movements", "Secular movements", "Universal franchise movements"],
    "answer": 0,
    "explanation": "More radical women's movements aimed at equality in personal and family life as well. These movements are called Feminist movements.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-003",
    "type": "mcq",
    "subtopic": "Patriarchy Definition",
    "difficulty": "Easy",
    "question": "A society or social system ruled by men, where women are subordinated and men hold primary power, is called:",
    "options": ["A patriarchal society", "A matriarchal society", "An egalitarian commune", "A secular state"],
    "answer": 0,
    "explanation": "Patriarchy literally means rule by father. This concept is used to refer to a system that values men more and gives them power over women.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-004",
    "type": "mcq",
    "subtopic": "Literacy Disparity in India",
    "difficulty": "Medium",
    "question": "According to census data highlighted in NCERT, what is the approximate literacy rate comparison between women and men in India?",
    "options": [
      "The literacy rate among women is only about 54% compared to 76% among men",
      "Women literacy is 95% while men literacy is 50%",
      "Both women and men have identical literacy of 75%",
      "Women literacy is 100% across all northern states"
    ],
    "answer": 0,
    "explanation": "The literacy rate among women is only 54 percent compared with 76 percent among that of men. Similarly, a smaller proportion of girl students go for higher studies because parents prefer to spend their resources on sons.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-005",
    "type": "mcq",
    "subtopic": "Equal Remuneration Act 1976",
    "difficulty": "Medium",
    "question": "What is the primary legal mandate of the Equal Remuneration Act, 1976?",
    "options": [
      "Equal wages must be paid for equal work regardless of gender",
      "Women are legally prohibited from working night shifts in hospitals",
      "Men must receive double the wages of women in agricultural fields",
      "Only women can be hired in the textile industry"
    ],
    "answer": 0,
    "explanation": "The Equal Remuneration Act, 1976 provides that equal wages should be paid to equal work. Yet in almost all areas of work, from sports and cinema, to factories and fields, women are often paid less than men for exactly the same work.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-006",
    "type": "mcq",
    "subtopic": "Child Sex Ratio Decline Cause",
    "difficulty": "Medium",
    "question": "The declining child sex ratio in India (number of girl children per thousand boys dropping below 900 in several states) is primarily driven by:",
    "options": [
      "Sex-selective abortion of female foetuses due to patriarchal son preference",
      "Higher female migration to international universities",
      "Natural biological birth imbalances",
      "Strict government dietary regulations"
    ],
    "answer": 0,
    "explanation": "In many parts of India, parents prefer to have sons and find ways to have the girl child aborted before she is born. Such sex-selective abortion led to a fall in child sex ratio in the country.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-007",
    "type": "mcq",
    "subtopic": "Women Representation in Parliament",
    "difficulty": "Medium",
    "question": "In India, what has been the historical status of women's representation in the Lok Sabha (national parliament)?",
    "options": [
      "The percentage of elected women MPs has historically remained low, barely crossing 12–14%",
      "Women have always held exactly 50% of all parliamentary seats",
      "Women representation in India is higher than in all Scandinavian countries",
      "Women are constitutionally barred from contesting national elections"
    ],
    "answer": 0,
    "explanation": "In India, the proportion of women in legislature has been very low. For example, the percentage of elected women members in Lok Sabha touched 14.36 percent of its total strength for the first time in 2019. Their share in state assemblies is less than 5 percent.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-008",
    "type": "mcq",
    "subtopic": "Mahatma Gandhi on Religion and Politics",
    "difficulty": "Medium",
    "question": "Mahatma Gandhi famously said that 'religion can never be separated from politics'. What did he mean by 'religion' in this context?",
    "options": [
      "Moral and ethical values drawn from all religions that should guide political governance",
      "Strict legal imposition of orthodox Hindu rituals by the state",
      "Banning all minority religious practices in public schools",
      "Rule by religious priests and clergy instead of parliament"
    ],
    "answer": 0,
    "explanation": "Gandhiji used to say that religion can never be separated from politics. What he meant by religion was not any particular religion like Hinduism or Islam, but moral values that inform all religions. He believed that politics must be guided by ethics drawn from religion.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-009",
    "type": "mcq",
    "subtopic": "Communalism Core Belief",
    "difficulty": "Medium",
    "question": "What is the foundational underlying belief of 'Communal Politics'?",
    "options": [
      "Religion is the principal basis of social and political community, and people of different religions cannot have common interests",
      "All religions preach the same universal brotherhood and equality",
      "Religion should remain strictly a private personal matter with zero political role",
      "Scientific reason must replace religious worship in schools"
    ],
    "answer": 0,
    "explanation": "Communal politics is based on the idea that religion is the principal basis of social community. It asserts that the followers of a particular religion must belong to one community, and that people who follow different religions cannot belong to the same social community.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-010",
    "type": "mcq",
    "subtopic": "Extreme Form of Communalism",
    "difficulty": "Easy",
    "question": "What is the most hideous and dangerous manifestation of communalism in a multi-religious society?",
    "options": [
      "Communal violence, riots, and massacres",
      "Celebrating religious festivals with public lights",
      "Publishing inter-faith philosophical literature",
      "Building multi-faith prayer rooms in hospitals"
    ],
    "answer": 0,
    "explanation": "The most ugly form of communalism is communal violence, riots and massacre. India and Pakistan suffered some of the worst communal riots at the time of the Partition.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-011",
    "type": "mcq",
    "subtopic": "Secular State Model in India",
    "difficulty": "Easy",
    "question": "Which of the following constitutional provisions reflects that India is a 'Secular State'?",
    "options": [
      "There is no official religion for the Indian state, and Article 25 gives freedom to profess and practice any religion",
      "Hinduism is declared the primary national faith in the Preamble",
      "Only religious scholars can contest parliamentary elections",
      "The state funds religious temples exclusively from public taxes"
    ],
    "answer": 0,
    "explanation": "There is no official religion for the Indian state. Unlike the status of Buddhism in Sri Lanka, that of Islam in Pakistan and Christianity in England, our Constitution does not give a special status to any religion. It provides to all individuals and communities freedom to profess, practise and propagate any religion.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-012",
    "type": "mcq",
    "subtopic": "State Intervention in Religion",
    "difficulty": "Board Standard",
    "question": "Does Indian secularism prohibit the state from intervening in religious matters altogether?",
    "options": [
      "No; the Constitution allows the state to intervene in the matters of religion to ensure equality and ban discriminatory practices like untouchability",
      "Yes; the Indian state can never interfere in any religious practice under any circumstance",
      "Yes; religious personal laws are superior to the Indian Constitution",
      "No; the state can unilaterally dissolve all religious institutions"
    ],
    "answer": 0,
    "explanation": "At the same time, the Constitution allows the state to intervene in the matters of religion in order to ensure equality within religious communities. For example, it bans untouchability.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-013",
    "type": "mcq",
    "subtopic": "Caste System Roots",
    "difficulty": "Medium",
    "question": "The caste system in India was historically rooted in an extreme form of:",
    "options": [
      "Hereditary occupational division sanctioned by ritual notions of purity and pollution",
      "Voluntary membership in competitive corporate guild unions",
      "Democratic elections conducted by village panchayats",
      "Equal distribution of agricultural land across all families"
    ],
    "answer": 0,
    "explanation": "Caste system was based on exclusion of and discrimination against the 'outcaste' groups. They were subjected to the inhuman practice of untouchability and rigid hereditary occupational division.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-014",
    "type": "mcq",
    "subtopic": "Social Reformers Against Caste",
    "difficulty": "Easy",
    "question": "Which of the following groups of social reformers worked tirelessly to establish a society free from caste discrimination and untouchability?",
    "options": [
      "Jyotirao Phule, Mahatma Gandhi, Dr. B.R. Ambedkar, and Periyar Ramaswami",
      "Lord Wellesley, Lord Dalhousie, and Lord Curzon",
      "Adam Smith, David Ricardo, and John Stuart Mill",
      "Napoleon Bonaparte and Otto von Bismarck"
    ],
    "answer": 0,
    "explanation": "Social reformers like Jotiba Phule, Gandhiji, B.R. Ambedkar and Periyar Ramaswami advocated and worked to establish a society in which caste inequalities are absent.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-015",
    "type": "mcq",
    "subtopic": "Factors Breaking Caste Hierarchy",
    "difficulty": "Medium",
    "question": "Which modern socio-economic processes have contributed significantly to breaking down old caste hierarchies in India?",
    "options": [
      "Urbanisation, growth of literacy, occupational mobility, and weakening of landlords' position in villages",
      "Strict reinforcement of hereditary village trades",
      "Abolition of modern public transport like buses and railways",
      "Mandatory caste markings on clothing"
    ],
    "answer": 0,
    "explanation": "Partly due to their efforts and partly due to other socio-economic changes, castes and caste system in modern India have undergone great changes. With economic development, large-scale urbanisation, growth of literacy and education, occupational mobility and the weakening of the position of landlords in the villages, the old notions of caste hierarchy are breaking down.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-016",
    "type": "mcq",
    "subtopic": "Occupational Mobility Definition",
    "difficulty": "Easy",
    "question": "The shift from one occupation to another, usually when a new generation takes up work different from that practiced by their ancestors, is known as:",
    "options": ["Occupational mobility", "Sexual division of labour", "Caste polarisation", "Secularisation"],
    "answer": 0,
    "explanation": "Occupational mobility refers to the shift from one occupation to another, usually when a new generation takes up occupations other than those practiced by their ancestors.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-017",
    "type": "mcq",
    "subtopic": "Caste in Politics - Candidate Selection",
    "difficulty": "Medium",
    "question": "How does caste manifest itself when political parties choose candidates for elections?",
    "options": [
      "Parties keep in mind the caste composition of the electorate and nominate candidates from different castes so as to muster support to win elections",
      "Parties randomly pick names out of a lottery drum",
      "Candidates are chosen strictly based on physical athletic fitness",
      "Parties nominate candidates only from foreign countries"
    ],
    "answer": 0,
    "explanation": "When parties choose candidates in elections, they keep in mind the caste composition of the electorate and nominate candidates from different castes so as to muster necessary support to win elections.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-018",
    "type": "mcq",
    "subtopic": "No Single Caste Majority Constituency",
    "difficulty": "Board Standard",
    "question": "Which electoral reality proves that elections in India are not decided purely on caste lines?",
    "options": [
      "No parliamentary constituency in India has a clear majority of one single caste; every candidate must win the confidence of more than one caste",
      "Only members of one caste are legally allowed to vote in each state",
      "Caste names are banned from being printed on identity cards",
      "No political party ever mentions caste during election campaigns"
    ],
    "answer": 0,
    "explanation": "No parliamentary constituency in the country has a clear majority of one single caste. So, every candidate and party needs to win the confidence of more than one caste and community to win an election.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-019",
    "type": "mcq",
    "subtopic": "Politics in Caste",
    "difficulty": "Board Standard",
    "question": "Politics does not just get caste-ridden; caste also gets politicised ('politics in caste'). How does this happen?",
    "options": [
      "Caste groups seek to become bigger by incorporating sub-castes, form coalitions, and new caste groups like 'backward' and 'forward' emerge in dialogue with the state",
      "Castes completely abandon their social identity and dissolve into army units",
      "Caste councils replace state legislative assemblies",
      "All religious places are converted into voting booths"
    ],
    "answer": 0,
    "explanation": "Each caste group tries to become bigger by incorporating neighbouring castes or sub-castes which were earlier excluded. Various caste groups are required to enter into a coalition with other castes or communities and thus enter into a dialogue and negotiation.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s1-020",
    "type": "mcq",
    "subtopic": "Healthy vs Negative Caste Politics",
    "difficulty": "Medium",
    "question": "When does caste-based political mobilization become negative and dangerous for democracy?",
    "options": [
      "When politics focuses exclusively on caste, leading to social tensions, violence, and disruption of national unity",
      "When disadvantaged castes demand reservations in education and jobs",
      "When lower castes demand equal dignity and respect in society",
      "When political parties field candidates from backward classes"
    ],
    "answer": 0,
    "explanation": "Exclusive attention to caste can produce negative results. It can divert attention from other pressing issues like poverty, development and corruption. In some cases, caste division leads to tensions, conflict and even violence.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.2"
  }
]

# -----------------------------------------------------------------------------
# CH 15 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch15_set2 = [
  {
    "id": "cbse10-sst-civ-ch15-s2-001",
    "type": "mcq",
    "subtopic": "Unpaid Domestic Work",
    "difficulty": "Medium",
    "question": "A feminist analysis highlighted in NCERT shows that although women constitute half of humanity, their public role is minimal because:",
    "options": [
      "Their domestic labour (cooking, cleaning, caregiving) is unpaid, undervalued, and not accounted for in national income statistics",
      "Women are legally prohibited from working in banks and offices",
      "Men perform 90% of all household washing and cooking in rural areas",
      "Women refuse to participate in higher education"
    ],
    "answer": 0,
    "explanation": "Although women constitute half of humanity, their role in public life, especially politics, is minimal in most societies. Their household work is invisible, unpaid, and socially devalued.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-002",
    "type": "mcq",
    "subtopic": "Family Laws Definition",
    "difficulty": "Easy",
    "question": "Laws that deal with family-related matters such as marriage, divorce, adoption, inheritance, and succession are known as:",
    "options": ["Family laws", "Criminal laws", "Corporate mercantile laws", "Maritime laws"],
    "answer": 0,
    "explanation": "Family laws are those laws that deal with family related matters such as marriage, divorce, adoption, inheritance, etc. In our country, different family laws apply to followers of different religions.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-003",
    "type": "mcq",
    "subtopic": "Feminist Critique of Family Laws",
    "difficulty": "Medium",
    "question": "Women's rights movements argue that family laws of all religions discriminate against women, and therefore demand that:",
    "options": [
      "The government should reform these laws to make them equitable and gender-just",
      "All family relationships should be permanently abolished by law",
      "Women should be barred from owning property or land",
      "Divorce should be banned under every circumstance"
    ],
    "answer": 0,
    "explanation": "Women's movement has argued that family laws of all religions discriminate against women. So they have demanded that government should change these laws to make them more equitable.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-004",
    "type": "mcq",
    "subtopic": "Communalism in Daily Beliefs",
    "difficulty": "Medium",
    "question": "In everyday life, communalism most commonly expresses itself through:",
    "options": [
      "Religious prejudices, stereotypes of religious communities, and belief in the superiority of one's religion over other religions",
      "Participating in multi-religious trade fairs",
      "Reading secular history textbooks",
      "Supporting constitutional freedom of speech"
    ],
    "answer": 0,
    "explanation": "The most common expression of communalism is in everyday beliefs. These routinely involve religious prejudices, stereotypes of religious communities and belief in the superiority of one's religion over other religions.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-005",
    "type": "mcq",
    "subtopic": "Political Mobilisation on Religious Lines",
    "difficulty": "Medium",
    "question": "How do communal political parties typically mobilize voters during election campaigns?",
    "options": [
      "By using religious symbols, holy books, emotional appeals by religious leaders, and plain fear to unite followers",
      "By debating macroeconomic industrial manufacturing policies",
      "By presenting comparative data on infant mortality rates across districts",
      "By encouraging inter-faith inter-caste community marriages"
    ],
    "answer": 0,
    "explanation": "A communal mind often leads to a quest for political dominance of one's own religious community. Political mobilisation on religious lines involves the use of sacred symbols, religious leaders, emotional appeal and plain fear.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-006",
    "type": "mcq",
    "subtopic": "Article 15 Anti-Discrimination",
    "difficulty": "Easy",
    "question": "Article 15 of the Indian Constitution prohibits discrimination against any citizen on grounds of:",
    "options": [
      "Religion, race, caste, sex, or place of birth",
      "Wealth and financial tax bracket",
      "Educational qualification and degrees",
      "Political party membership"
    ],
    "answer": 0,
    "explanation": "The Constitution prohibits discrimination on grounds of religion, race, caste, sex or place of birth under Article 15.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-007",
    "type": "mcq",
    "subtopic": "Untouchability Abolition Article 17",
    "difficulty": "Easy",
    "question": "Which fundamental constitutional provision officially abolished the practice of untouchability and made its practice in any form a punishable offence?",
    "options": ["Article 17 of the Indian Constitution", "Article 370", "Article 356", "Article 1"],
    "answer": 0,
    "explanation": "The Constitution of India abolished the inhuman practice of untouchability under Article 17, making its enforcement in any form strictly forbidden and punishable by law.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-008",
    "type": "mcq",
    "subtopic": "Persistence of Caste Inequalities",
    "difficulty": "Medium",
    "question": "Despite constitutional provisions, why does caste continue to be closely linked to economic status in modern India?",
    "options": [
      "Castes that had access to education and wealth under the old system have done very well in modern education and white-collar jobs, while backward castes lagged behind",
      "The Constitution mandates that lower castes cannot enter universities",
      "Modern banks refuse to open accounts for urban workers",
      "Private companies only hire workers based on hereditary village caste lists"
    ],
    "answer": 0,
    "explanation": "Caste continues to be closely linked to economic status. The castes that had access to education under the old system have done very well in acquiring modern education. Those groups that did not have access to education or were prohibited from acquiring it have naturally lagged behind.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-009",
    "type": "mcq",
    "subtopic": "Vote Bank Concept",
    "difficulty": "Medium",
    "question": "When a political party claims that a particular caste is its 'vote bank', it usually signifies that:",
    "options": [
      "A large proportion of the voters from that caste vote for that party",
      "Every single member of that caste is legally obligated to vote for that candidate",
      "The caste owns shares in the party's commercial bank",
      "Voters of that caste are prohibited from voting for any other party"
    ],
    "answer": 0,
    "explanation": "When people say that a caste is a 'vote bank' of one party, it usually means that a large proportion of the voters from that caste vote for that party, though not 100% of them.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-010",
    "type": "mcq",
    "subtopic": "Sitting MP/MLA Defeats Disproving Caste Hegemony",
    "difficulty": "Board Standard",
    "question": "Which recurring phenomenon in Indian democratic elections disproves the notion that voters vote blindly based solely on caste?",
    "options": [
      "Ruling MPs and MLAs frequently lose elections and are voted out of power",
      "Every election results in a 100% victory for the incumbent minister",
      "All elections are decided by judicial decree without counting ballots",
      "Voters never turn out in rural constituencies"
    ],
    "answer": 0,
    "explanation": "Many ruling MPs and MLAs frequently lose elections in our country. That could not have happened if all caste groups voted blindly for their own caste candidates or remained permanent vote banks.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-011",
    "type": "mcq",
    "subtopic": "Scandinavian Countries Gender Equality",
    "difficulty": "Easy",
    "question": "In which region of the world is the political participation and representation of women in public life exceptionally high (around 40% or more)?",
    "options": ["Nordic / Scandinavian countries (Sweden, Norway, Finland)", "Sub-Saharan Africa", "Arab States", "South Asian nations"],
    "answer": 0,
    "explanation": "In Scandinavian countries such as Sweden, Norway and Finland, the participation of women in public life is exceptionally high.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-012",
    "type": "mcq",
    "subtopic": "Panchayati Raj 1/3rd Women Milestone",
    "difficulty": "Easy",
    "question": "How did India solve the problem of low women's political representation at the grassroots level?",
    "options": [
      "By legally reserving one-third of all seats in local government bodies (Panchayats and Municipalities) for women",
      "By banning men from contesting village elections",
      "By appointing women through non-elected hereditary succession",
      "By dissolving all rural village councils"
    ],
    "answer": 0,
    "explanation": "One-third of seats in local government bodies — in panchayats and municipalities — are now reserved for women. Now there are more than 10 lakh elected women representatives in rural and urban local bodies.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-013",
    "type": "mcq",
    "subtopic": "Religious Identity and Secularism",
    "difficulty": "Medium",
    "question": "A secular constitution guarantees religious freedom, but simultaneously insists that:",
    "options": [
      "No community shall exercise dominance over other religious communities, and religion cannot be used to discriminate",
      "All citizens must attend religious ceremonies in government offices",
      "Religious literature must be banned from private homes",
      "The military can dictate who becomes a temple priest"
    ],
    "answer": 0,
    "explanation": "Secularism is not just an ideology of some parties or persons; it is a fundamental pillar of the Indian Constitution ensuring that religion cannot be used to discriminate, dominate, or suppress minorities.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-014",
    "type": "mcq",
    "subtopic": "Caste Group Coalitions",
    "difficulty": "Medium",
    "question": "How do smaller castes in contemporary India gain greater political bargaining leverage during state elections?",
    "options": [
      "By forming broad political coalitions with neighbouring castes, creating wider electoral fronts",
      "By refusing to vote in all general elections",
      "By converting their villages into separate sovereign countries",
      "By emigrating en masse to foreign islands"
    ],
    "answer": 0,
    "explanation": "Various caste groups enter into coalitions with other castes or communities and thus enter into dialogue and political negotiation, creating broad electoral fronts.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-015",
    "type": "mcq",
    "subtopic": "Universal Adult Franchise Impact on Caste",
    "difficulty": "Board Standard",
    "question": "What powerful democratic instrument forced upper-caste politicians to respect and court the support of marginalized backward castes?",
    "options": [
      "Universal Adult Franchise and the principle of 'one person, one vote'",
      "The introduction of high educational fees for voting",
      "The hereditary power of traditional village zamindars",
      "Military conscription of rural youth"
    ],
    "answer": 0,
    "explanation": "Universal adult franchise and the principle of one-person-one-vote compelled political leaders to gear up to the task of mobilising and securing political support from backward and Dalit voters, shattering old notions of unchallengeable upper-caste dominance.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-016",
    "type": "mcq",
    "subtopic": "Urbanisation Weakening Caste",
    "difficulty": "Easy",
    "question": "Why does urbanisation weaken the rigid observance of caste untouchability in daily life?",
    "options": [
      "In crowded urban buses, trains, restaurants, and offices, people live and work side by side without knowing or caring about caste identities",
      "Urban municipal laws ban all social interaction among citizens",
      "Caste is legally dissolved as soon as someone enters a railway station",
      "All urban citizens are assigned identical names by the municipal corporation"
    ],
    "answer": 0,
    "explanation": "In cities, economic mobility and shared public spaces (restaurants, buses, metros, workplaces) make it practically impossible to practice rigid caste segregation or purity-pollution taboos.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-017",
    "type": "mcq",
    "subtopic": "Feminist Perspective on Politics",
    "difficulty": "Medium",
    "question": "The feminist slogan 'The Personal is Political' expresses the view that:",
    "options": [
      "Power inequalities, sexual division of labour, and domestic oppression within the family must be addressed through political and legal reforms",
      "Private family matters should never be discussed outside the home",
      "Only women should hold political office in the state",
      "Personal friendships should dictate all foreign policy decisions"
    ],
    "answer": 0,
    "explanation": "Feminists argue that personal relations inside the family (domestic division of labour, property inheritance, domestic violence) are structured by power inequalities and therefore require political and legal attention.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-018",
    "type": "mcq",
    "subtopic": "Communalism Undermining Democracy",
    "difficulty": "Medium",
    "question": "Why does communalism pose a fundamental threat to the spirit of a plural democratic nation like India?",
    "options": [
      "It assumes that people of different religions cannot live together as equal citizens within one nation and fosters mutual hatred",
      "It promotes higher voter turnout in rural constituencies",
      "It encourages international commercial shipping",
      "It requires all citizens to learn Sanskrit and Urdu"
    ],
    "answer": 0,
    "explanation": "Communalism is based on the flawed assumption that religious differences are the primary social divide and that people of different faiths have conflicting political interests, which destroys democratic fraternity.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-019",
    "type": "mcq",
    "subtopic": "Positive Role of Caste in Politics",
    "difficulty": "Board Standard",
    "question": "In what way can the political expression of caste play a positive and healthy role in a developing democracy?",
    "options": [
      "It allows historically disadvantaged and backward castes to demand their legitimate share of power, dignity, and access to resources",
      "It ensures that only upper-caste landlords hold ministerial portfolios",
      "It abolishes all competitive entrance examinations permanently",
      "It prevents regional parties from contesting national elections"
    ],
    "answer": 0,
    "explanation": "Caste politics has helped people from Dalits and OBC castes to gain better access to decision making. Several political and non-political organisations have been demanding and agitating for an end to discrimination, for more dignity and more access to land, resources and opportunities.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s2-020",
    "type": "mcq",
    "subtopic": "Intersection of Gender and Caste",
    "difficulty": "Medium",
    "question": "In Indian society, Dalit and Adivasi women suffer from what sociologists describe as:",
    "options": [
      "Double or multiple disadvantage (gender subordination combined with caste and economic deprivation)",
      "Total political domination over male landlords",
      "Immunity from all state taxation",
      "Automatic appointment to diplomatic embassies"
    ],
    "answer": 0,
    "explanation": "Women from socially disadvantaged castes face multiple layers of systemic marginalization: gender bias, caste discrimination, and severe economic poverty.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1 & 3"
  }
]

# -----------------------------------------------------------------------------
# CH 15 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch15_set3 = [
  {
    "id": "cbse10-sst-civ-ch15-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Gender as Social Construction",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Gender division is not based on biology but on social expectations and stereotypes.\nReason (R): Society trains boys and girls from childhood to believe that the main responsibility of women is housework and child rearing, while men work outside.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Gender division is a form of hierarchical social division seen everywhere, but it is not based on biology; it is socially constructed through cultural conditioning and sexual division of labour.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Equal Remuneration Reality",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Despite the Equal Remuneration Act 1976, women in India are often paid less than men for exactly the same work.\nReason (R): Patriarchal prejudice and unorganized labour markets undervalue women's work, treating male breadwinners preferentially.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Widespread gender discrimination and lack of effective enforcement in unorganised sectors lead to wage disparity despite statutory guarantees.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Flaw of Communal Ideology",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The fundamental premise of communal politics is fundamentally flawed and empirically false.\nReason (R): People of the same religion do not have the same interests and aspirations in every context; every individual has multiple identities and roles.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Communalism assumes all members of a religion think alike. In reality, people of the same faith differ across caste, economic class, gender, and regional aspirations.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Secular Constitution of India",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The makers of the Indian Constitution chose the model of a secular state.\nReason (R): India experienced catastrophic communal violence and partition in 1947, demonstrating that state-sponsored religion would destroy the nation.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The traumatic experience of partition convinced national leaders that India could survive only as a plural, secular state where all religions are treated equally.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Untouchability and Constitutional Law",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Constitution of India strictly prohibits discrimination on grounds of caste and bans untouchability.\nReason (R): Yet, caste has not completely disappeared from contemporary India, and caste endogamy remains widespread.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 1,
    "explanation": "Both statements are correct facts from NCERT. However, Reason is not the explanation of Assertion; it describes the sociological persistence of caste despite legal prohibition.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-006",
    "type": "case_based",
    "subtopic": "Case Analysis - Political Representation of Women",
    "difficulty": "Medium",
    "question": "A village in Rajasthan elects a woman as Sarpanch under the 33% reservation policy. In her first year, she builds public water taps, organizes a girls' secondary school bus, and shuts down illegal liquor vends. What broader democratic truth does this illustrate?",
    "options": [
      "Affirmative reservation for women brings urgent social and livelihood issues to the forefront of governance",
      "Women sarpanches only focus on private household chores",
      "Local councils become bankrupt under women leadership",
      "Villages should be managed exclusively by state police officers"
    ],
    "answer": 0,
    "explanation": "Empirical studies in India confirm that women representatives prioritize basic community needs—drinking water, sanitation, girls' education, and health.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-007",
    "type": "case_based",
    "subtopic": "Case Analysis - Election Caste Arithmetic Failure",
    "difficulty": "Medium",
    "question": "A political party fields a candidate belonging to Caste X, which constitutes 35% of a constituency's electorate. Two other rival parties also field strong candidates belonging to Caste X. What is the inevitable electoral consequence?",
    "options": [
      "The Caste X vote gets divided among the three candidates, and the election is decided by the votes of other caste communities",
      "The election is automatically cancelled by the Supreme Court",
      "All three candidates are declared joint winners",
      "Caste X voters are prohibited from casting ballots"
    ],
    "answer": 0,
    "explanation": "When multiple parties field candidates from the same dominant caste, the caste vote divides. Candidates must therefore build a multi-caste coalition to win.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Caste in Politics Multi-Dimensional Reality",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Caste is only one of many factors that influence voters' choices in Indian elections.\nReason (R): Voters have strong attachments to political parties, evaluate government economic performance, and vote based on candidate reputation.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Voters do not vote solely on caste lines. Party loyalty, economic satisfaction, leadership charisma, and local issues play decisive roles.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-009",
    "type": "mcq",
    "subtopic": "Nari Shakti Vandan Adhiniyam Milestone",
    "difficulty": "Medium",
    "question": "What historic legislative milestone was passed to guarantee one-third reservation for women in the Lok Sabha and State Legislative Assemblies?",
    "options": [
      "The Women's Reservation Act (106th Constitutional Amendment)",
      "The Factories Act Amendment",
      "The Hindu Succession Act of 1956",
      "The Dowry Prohibition Act"
    ],
    "answer": 0,
    "explanation": "The Women's Reservation Bill (Nari Shakti Vandan Adhiniyam / 106th Amendment Act) fulfills the long-standing demand for 33% reservation for women in Lok Sabha and State Assemblies.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Endogamy Persistence",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The practice of marriage within one's own caste or community (endogamy) continues to be the dominant norm in contemporary India.\nReason (R): Centuries of caste conditioning and family pressures make caste identity a persistent social barrier in private life.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Even in modern urban India, matrimonial advertisements demonstrate that marrying within one's own caste remains deeply entrenched.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-011",
    "type": "mcq",
    "subtopic": "Sexual Harassment at Workplace Legal Framework",
    "difficulty": "Easy",
    "question": "Legal protections such as the POSH (Prevention of Sexual Harassment) Act and Domestic Violence Act were enacted primarily due to:",
    "options": [
      "Decades of sustained agitations and advocacy by women's feminist organisations",
      "Orders issued by international shipping cartels",
      "Decrees issued by traditional caste panchayats",
      "Directives from foreign central banks"
    ],
    "answer": 0,
    "explanation": "Feminist organisations and women's rights groups waged long legal and social struggles to secure protective legislation against domestic violence and workplace harassment.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis - Communal Mobilisation Hazard",
    "difficulty": "Medium",
    "question": "During an election in a sensitive constituency, an extremist orator delivers inflammatory speeches claiming that 'our religion is under grave threat from the minority community'. How does such rhetoric violate democratic norms?",
    "options": [
      "It exploits religious fears, divides citizens into hostile factions, and violates the Model Code of Conduct and Representation of the People Act",
      "It promotes higher inter-community trade",
      "It helps municipal workers collect property tax",
      "It strengthens the secular character of the republic"
    ],
    "answer": 0,
    "explanation": "Appealing to religious hatred and fear undermines democratic brotherhood, incites communal tension, and is an electoral offence under Indian law.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-013",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Politics in Caste Sub-caste Absorption",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Caste groups in India increasingly try to expand their demographic base by incorporating neighbouring sub-castes.\nReason (R): In competitive electoral democracy, larger numbers translate into greater political bargaining power with ruling parties.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Democratic competition drives smaller sub-castes to merge into broader caste confederations to maximize electoral clout.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-014",
    "type": "mcq",
    "subtopic": "Economic Inequality by Caste",
    "difficulty": "Medium",
    "question": "According to National Sample Survey data cited in NCERT, which social group continues to have the lowest proportion of population living above the poverty line in India?",
    "options": ["Scheduled Tribes (STs) and Scheduled Castes (SCs)", "Upper Caste Forward Communities", "Urban Merchant Classes", "Non-resident Indians"],
    "answer": 0,
    "explanation": "NSSO data reveals that Scheduled Tribes and Scheduled Castes have the highest percentages of people living in severe poverty, reflecting historical socio-economic exclusion.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-015",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Communal Politics Majoritarian Variant",
    "difficulty": "Board Standard",
    "question": "Assertion (A): For people who belong to the majority community, communalism frequently takes the form of majoritarian dominance.\nReason (R): For people belonging to the minority community, communalism often takes the form of a desire to form a separate political unit.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 1,
    "explanation": "Both statements are exact constitutional-sociological analyses from NCERT, describing the distinct expressions of communalism among majority and minority groups.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-016",
    "type": "mcq",
    "subtopic": "Role of Women in Agricultural Labour",
    "difficulty": "Easy",
    "question": "In rural India, an agricultural survey reveals that women perform approximately what proportion of agricultural operations (sowing, weeding, harvesting)?",
    "options": [
      "A massive share of farm work, yet their land ownership remains negligible",
      "Zero farm work because they only work in software",
      "Farm work only on Sundays",
      "100% of the mechanical tractor driving while men weed manually"
    ],
    "answer": 0,
    "explanation": "Women make up a huge portion of rural agricultural labour, yet titles to land and farming assets are almost entirely held in men's names.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-017",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Religious Symbols in Elections Prohibition",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Election Commission of India strictly prohibits the use of religious places, deities, and sacred symbols for election campaigning.\nReason (R): Exploiting religious sentiments vitiates free and fair democratic choice and violates the secular foundations of the Constitution.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Under the Model Code of Conduct and election law, seeking votes in the name of religion or using places of worship is an illegal corrupt practice.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-018",
    "type": "mcq",
    "subtopic": "Caste Consciousness vs Human Dignity",
    "difficulty": "Medium",
    "question": "Dr. B.R. Ambedkar argued that political democracy in India would remain incomplete and fragile unless accompanied by:",
    "options": [
      "Social democracy that recognizes liberty, equality, and fraternity in everyday social relations",
      "The total militarization of village life",
      "The abolition of the Parliament",
      "The dissolution of all high courts"
    ],
    "answer": 0,
    "explanation": "Ambedkar emphasized in his historic constituent assembly speeches that political equality (one person, one vote) must be anchored in social equality (ending caste hierarchy and discrimination).",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-019",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Broadening of Caste Identities",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Modern democratic politics has transformed ancient narrow sub-caste identities into broader political groupings like 'OBCs' and 'Dalits'.\nReason (R): Political parties create broad socio-economic coalitions to mobilize common class and caste interests for electoral victory.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Democratic mobilisation encourages disparate jatis to forge larger political identities (e.g. backward castes) to influence state welfare policies.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-civ-ch15-s3-020",
    "type": "mcq",
    "subtopic": "Holistic Democratic Ideal",
    "difficulty": "Easy",
    "question": "What is the ultimate vision of a healthy constitutional democracy regarding gender, religion, and caste?",
    "options": [
      "A society where diversity is celebrated, discrimination is eradicated, and every citizen enjoys equal dignity, rights, and voice",
      "A society where the majority religion suppresses all minorities",
      "A society where women are confined strictly to domestic cooking",
      "A society where hereditary caste dictates a person's entire career"
    ],
    "answer": 0,
    "explanation": "Democracy is not just an electoral contest; it is a moral commitment to eradicate systemic inequalities and ensure human dignity for all.",
    "citation": "NCERT Class 10 Civics, Chapter 3, Conclusion"
  }
]

# Write Chapter 15 Sets 1, 2, 3
with open(os.path.join(DATA_DIR, "ch15_gender_religion_caste_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch15_set1}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch15_gender_religion_caste_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch15_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch15_gender_religion_caste_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch15_set3}, f, indent=2, ensure_ascii=False)

print("Generated: ch15 Sets 1, 2, 3 (60 Qs)")
