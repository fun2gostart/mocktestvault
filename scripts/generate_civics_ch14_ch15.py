#!/usr/bin/env python3
"""
Generates Civics Ch 14 (Federalism) Sets 1, 2, 3
and Ch 15 (Gender, Religion and Caste) Sets 1, 2, 3.
Total: 6 sets = 120 questions.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# =============================================================================
# CHAPTER 14: FEDERALISM (Civics Ch 2)
# =============================================================================

ch14_set1 = [
  {
    "id": "cbse10-sst-civ-ch14-s1-001",
    "type": "mcq",
    "subtopic": "Federalism Definition",
    "difficulty": "Easy",
    "question": "Federalism is a system of government in which power is divided between:",
    "options": [
      "A central authority and various constituent units of the country",
      "The military high command and police forces",
      "Different multinational corporations",
      "The head of state and judicial magistrates only"
    ],
    "answer": 0,
    "explanation": "Federalism is a system of government in which the power is divided between a central authority and various constituent units of the country.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-002",
    "type": "mcq",
    "subtopic": "Unitary vs Federal System",
    "difficulty": "Medium",
    "question": "How does a federal system differ fundamentally from a unitary system of government?",
    "options": [
      "In a federal system, state governments have constitutional powers of their own for which they are not answerable to the central government",
      "In a federal system, there are no regional courts or state police",
      "In a unitary system, power is divided equally between 50 independent states",
      "In a federal system, the central government can dissolve state legislatures at its whim"
    ],
    "answer": 0,
    "explanation": "Under the unitary system, either there is only one level of government or the sub-units are subordinate to the central government. In a federal system, the central government cannot order the state government to do something unconstitutional within its jurisdiction; both governments are separately answerable to the people.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-003",
    "type": "mcq",
    "subtopic": "Key Features of Federalism",
    "difficulty": "Medium",
    "question": "Which of the following is NOT a core constitutional feature of a federal system?",
    "options": [
      "The fundamental provisions of the constitution can be unilaterally altered by the central legislature alone",
      "There are two or more tiers (or levels) of government",
      "Different tiers of government govern the same citizens, but each tier has its own jurisdiction",
      "Courts have the power to interpret the constitution and umpire disputes between levels of government"
    ],
    "answer": 0,
    "explanation": "The fundamental provisions of the constitution cannot be unilaterally changed by one level of government. Such changes require the consent of both the levels of government (e.g. Article 368 in India).",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-004",
    "type": "mcq",
    "subtopic": "'Coming Together' Federations",
    "difficulty": "Medium",
    "question": "Which of the following countries is an example of a 'Coming Together' federation where independent states pooled their sovereignty?",
    "options": ["USA, Switzerland, and Australia", "India, Spain, and Belgium", "United Kingdom, France, and Japan", "China, Russia, and Cuba"],
    "answer": 0,
    "explanation": "In 'coming together' federations, independent states come together on their own to form a bigger unit, so that by pooling sovereignty and retaining identity they can increase their security. Examples include USA, Switzerland and Australia.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-005",
    "type": "mcq",
    "subtopic": "'Holding Together' Federations",
    "difficulty": "Medium",
    "question": "In 'Holding Together' federations, a large country decides to divide its power between constituent states and the national government. Which of the following is an example?",
    "options": ["India, Spain, and Belgium", "USA and Australia", "Switzerland and Canada", "South Africa and New Zealand"],
    "answer": 0,
    "explanation": "In 'holding together' federations, a large country decides to divide its power between the constituent States and the national government. India, Spain and Belgium are examples of this category.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-006",
    "type": "mcq",
    "subtopic": "Union List Subjects",
    "difficulty": "Easy",
    "question": "Which of the following subjects falls under the 'Union List' in the Seventh Schedule of the Indian Constitution?",
    "options": ["Defence, Foreign Affairs, Banking, and Currency", "Police and Trade", "Agriculture and Irrigation", "Marriage and Adoption"],
    "answer": 0,
    "explanation": "Union List includes subjects of national importance such as defence of the country, foreign affairs, banking, communications and currency, on which only the Central Parliament can legislate.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-007",
    "type": "mcq",
    "subtopic": "State List Subjects",
    "difficulty": "Easy",
    "question": "Which of the following subjects is included in the 'State List' on which State legislatures have exclusive power to make laws?",
    "options": ["Police, Trade, Commerce, Agriculture, and Irrigation", "Defence and Atomic Energy", "Foreign Treaties and Passports", "Currency and Coinage"],
    "answer": 0,
    "explanation": "State List contains subjects of State and local importance such as police, trade, commerce, agriculture and irrigation.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-008",
    "type": "mcq",
    "subtopic": "Concurrent List Conflict Rule",
    "difficulty": "Board Standard",
    "question": "The Concurrent List includes subjects of common interest such as education, forests, trade unions, marriage, and adoption. If there is a conflict between a Central law and a State law on a Concurrent subject:",
    "options": [
      "The law made by the Union Parliament prevails",
      "The State law automatically overrides the Central law",
      "The law is referred to the United Nations",
      "Both laws are struck down and the subject remains unregulated"
    ],
    "answer": 0,
    "explanation": "If there is a conflict between the laws made by the Union and the State on a subject in the Concurrent List, the law made by the Union Government will prevail.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-009",
    "type": "mcq",
    "subtopic": "Residuary Subjects",
    "difficulty": "Medium",
    "question": "Subjects that came up after the Constitution was written, such as computer software and cyber law, are called 'Residuary Subjects'. Who has the power to legislate on them?",
    "options": ["The Union Government", "The State Governments exclusively", "The Zilla Parishad", "The High Courts of states"],
    "answer": 0,
    "explanation": "According to our constitution, the Union Government has the power to legislate on these 'residuary' subjects that do not fall in any of the three lists.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-010",
    "type": "mcq",
    "subtopic": "Union Territories in India",
    "difficulty": "Easy",
    "question": "Territories such as Chandigarh, Lakshadweep, or the capital city of Delhi, which are too small to become independent states, are known as:",
    "options": ["Union Territories", "Autonomous Provinces", "Protectorates", "Residuary Zones"],
    "answer": 0,
    "explanation": "These units are called Union Territories. These territories do not have the powers of a State. The Central Government has special powers in running these areas.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-011",
    "type": "mcq",
    "subtopic": "Amending Federal Provisions",
    "difficulty": "Hard",
    "question": "To change the basic federal power-sharing arrangement between the Union and the States in the Indian Constitution, what special procedure is required?",
    "options": [
      "Passing by at least two-thirds majority in both Houses of Parliament AND ratification by legislatures of at least half of the total States",
      "A simple executive order signed by the President of India",
      "Approval by the Supreme Court Chief Justice alone",
      "A national referendum held across all district headquarters"
    ],
    "answer": 0,
    "explanation": "Any change to the constitutional division of powers has to be first passed by both the Houses of Parliament with at least two-thirds majority. Then it has to be ratified by the legislatures of at least half of the total States.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-012",
    "type": "mcq",
    "subtopic": "Umpire Role of Judiciary",
    "difficulty": "Easy",
    "question": "In case of any dispute between different levels of government about the division of powers or revenue, which institution acts as the umpire?",
    "options": [
      "The High Courts and the Supreme Court",
      "The Union Home Ministry",
      "The Comptroller and Auditor General",
      "The armed forces tribunal"
    ],
    "answer": 0,
    "explanation": "The judiciary plays an important role in overseeing the implementation of constitutional provisions and procedures. In case of any dispute about the division of powers, the High Courts and the Supreme Court make a decision.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-013",
    "type": "mcq",
    "subtopic": "Linguistic States Formation",
    "difficulty": "Medium",
    "question": "The creation of Linguistic States in 1956 and thereafter was the first and a major test for democratic politics in our country. What was the ultimate outcome?",
    "options": [
      "It actually made the country more united and made administration easier",
      "It led to the disintegration and partition of India into multiple nations",
      "It forced all regional languages to be replaced by Latin",
      "It caused continuous inter-state civil wars"
    ],
    "answer": 0,
    "explanation": "When the demand for the formation of States on the basis of language was raised, some national leaders feared it would lead to disintegration. But experience has shown that the formation of linguistic States has actually made the country more united and administration much easier.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-014",
    "type": "mcq",
    "subtopic": "National Language Constitutional Position",
    "difficulty": "Medium",
    "question": "What is the exact constitutional position regarding a 'National Language' in India?",
    "options": [
      "Our Constitution did not give the status of national language to any one language; Hindi was identified as the official language",
      "Hindi was declared the sole National Language for all citizens",
      "Sanskrit was declared the national language of all courts",
      "English was declared the national language of all states"
    ],
    "answer": 0,
    "explanation": "Our Constitution did not give the status of national language to any one language. Hindi was identified as the official language. But Hindi is the mother tongue of only about 40 percent of Indians. Therefore, there were many safeguards to protect other languages.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-015",
    "type": "mcq",
    "subtopic": "Eighth Schedule Scheduled Languages",
    "difficulty": "Easy",
    "question": "Besides Hindi, how many other languages are recognized as 'Scheduled Languages' by the Eighth Schedule of the Indian Constitution?",
    "options": ["21 other languages (total 22)", "14 other languages", "28 other languages", "10 other languages"],
    "answer": 0,
    "explanation": "Besides Hindi, there are 21 other languages recognised as Scheduled Languages by the Constitution. A candidate in an examination conducted for Central Government positions may opt to take the examination in any of these languages.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-016",
    "type": "mcq",
    "subtopic": "Coalition Era Impact on Federalism",
    "difficulty": "Medium",
    "question": "The era of Coalition Governments beginning in 1990 strengthened Indian federalism because:",
    "options": [
      "No single national party got a clear majority in the Lok Sabha, leading to alliances with regional parties and respect for state autonomy",
      "State governments were stripped of all tax revenue",
      "The Central Government took direct control of all state police departments",
      "Elections to the Lok Sabha were abolished for twenty years"
    ],
    "answer": 0,
    "explanation": "The era of coalition governments at the Centre meant that since no single party got a clear majority in the Lok Sabha, major national parties had to enter into alliances with many parties including regional parties. This led to a new culture of power sharing and respect for the autonomy of State Governments.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-017",
    "type": "mcq",
    "subtopic": "Decentralisation Rationale",
    "difficulty": "Medium",
    "question": "Why is decentralisation of power to local self-governments considered essential in a vast and populous country like India?",
    "options": [
      "A large number of problems and issues are best settled at the local level because local people have better knowledge of problems in their localities",
      "It allows central ministers to take vacations throughout the year",
      "It eliminates the need for police stations and district magistrates",
      "It prevents villagers from participating in national elections"
    ],
    "answer": 0,
    "explanation": "The basic idea behind decentralisation is that there are a large number of problems and issues which are best settled at the local level. People have better knowledge of problems in their localities, have better ideas on where to spend money and how to manage things more efficiently.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-018",
    "type": "mcq",
    "subtopic": "1992 Decentralisation Amendment",
    "difficulty": "Easy",
    "question": "A major constitutional step towards decentralisation was taken in which year, introducing mandatory local body elections and reservation for women?",
    "options": ["1992 (73rd and 74th Amendments)", "1950", "1976", "2005"],
    "answer": 0,
    "explanation": "A major step towards decentralisation was taken in 1992 through the 73rd and 74th Constitutional Amendments. The Constitution was amended to make the third-tier of democracy more powerful and effective.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-019",
    "type": "mcq",
    "subtopic": "Women Reservation in Local Bodies",
    "difficulty": "Easy",
    "question": "Under the 1992 constitutional amendment for local self-governments, what proportion of seats is reserved for women in rural Panchayats and urban Municipalities?",
    "options": ["At least one-third (33%)", "Fifty percent in all states", "Ten percent", "Five percent"],
    "answer": 0,
    "explanation": "At least one-third of all positions are reserved for women in local self-governing bodies. This has brought over 10 lakh elected women into active political governance across India.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s1-020",
    "type": "mcq",
    "subtopic": "State Election Commission Role",
    "difficulty": "Medium",
    "question": "An independent institution called the 'State Election Commission' was created in each state by the 1992 amendment to:",
    "options": [
      "Conduct regular panchayat and municipal elections",
      "Conduct Lok Sabha general elections across India",
      "Appoint judges to the High Court of the state",
      "Audit commercial private corporate bank accounts"
    ],
    "answer": 0,
    "explanation": "An independent institution called the State Election Commission has been created in each State to conduct panchayat and municipal elections.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  }
]

# Write Chapter 14 Set 1
with open(os.path.join(DATA_DIR, "ch14_federalism_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch14_set1}, f, indent=2, ensure_ascii=False)

print("Generated: ch14_federalism_set1.json (20 Qs)")

# -----------------------------------------------------------------------------
# CH 14 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch14_set2 = [
  {
    "id": "cbse10-sst-civ-ch14-s2-001",
    "type": "mcq",
    "subtopic": "Panchayati Raj Structure - Gram Sabha",
    "difficulty": "Easy",
    "question": "The decision-making body of a village panchayat, consisting of all adult voters of the village who meet at least twice or thrice a year, is called the:",
    "options": ["Gram Sabha", "Nyaya Panchayat", "Zilla Parishad", "Block Samiti"],
    "answer": 0,
    "explanation": "The Gram Panchayat works under the overall supervision of the Gram Sabha. All the voters in the village are its members. It has to meet at least twice or thrice in a year to approve the annual budget and review performance.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-002",
    "type": "mcq",
    "subtopic": "Panchayat Samiti / Block Level",
    "difficulty": "Medium",
    "question": "A few Gram Panchayats are grouped together to form what is usually called a:",
    "options": ["Panchayat Samiti, Block, or Mandal", "Zilla Parishad", "Gram Sabha", "Municipal Corporation"],
    "answer": 0,
    "explanation": "A few Gram Panchayats are grouped together to form what is usually called a Panchayat Samiti or Block or Mandal. The members of this representative body are elected by all the panchayat members in that area.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-003",
    "type": "mcq",
    "subtopic": "Zilla Parishad Chairperson",
    "difficulty": "Medium",
    "question": "All the Panchayat Samitis or Mandals in a district together constitute the Zilla (district) Parishad. Who is the political head of the Zilla Parishad?",
    "options": ["Zilla Parishad Chairperson", "District Magistrate (Collector)", "State Governor", "Mayor"],
    "answer": 0,
    "explanation": "Zilla Parishad Chairperson is the political head of the Zilla Parishad. Members of the Lok Sabha and MLAs of that district and some other officials of other district-level bodies are also its members.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-004",
    "type": "mcq",
    "subtopic": "Municipal Corporation Head",
    "difficulty": "Easy",
    "question": "Big cities are constituted into Municipal Corporations. What is the elected political head of a Municipal Corporation called?",
    "options": ["Mayor", "Municipal Commissioner", "Sarpanch", "Governor"],
    "answer": 0,
    "explanation": "Municipalities are set up in towns. Big cities are constituted into Municipal Corporations. Both are controlled by elected bodies. Municipal Chairperson is the political head of the municipality. In a Municipal Corporation such an officer is called the Mayor.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-005",
    "type": "mcq",
    "subtopic": "Language Policy Flexibility",
    "difficulty": "Board Standard",
    "question": "How did Indian leaders handle the language dispute in 1965 when English was scheduled to cease as an official language?",
    "options": [
      "The Central Government agreed to continue the use of English along with Hindi for official purposes, showing flexibility",
      "The Central Government forcefully banned English across all universities",
      "All non-Hindi states were expelled from the Indian Union",
      "Hindi was made compulsory for all private businesses"
    ],
    "answer": 0,
    "explanation": "According to the Constitution, the use of English for official purposes was to stop in 1965. However, many non-Hindi speaking States demanded that the use of English continue. The Central Government responded by agreeing to continue the use of English along with Hindi for official purposes. Promotion of Hindi continues to be official policy, but promotion does not mean imposition.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-006",
    "type": "mcq",
    "subtopic": "Special Provisions under Article 371",
    "difficulty": "Hard",
    "question": "States such as Assam, Nagaland, Arunachal Pradesh, and Mizoram enjoy special constitutional provisions under Article 371 primarily due to:",
    "options": [
      "Protection of land rights of indigenous indigenous peoples, customary laws, and preferential employment",
      "Total exemption from paying income tax or customs duties",
      "Right to print their own state currency notes",
      "Right to sign military treaties with neighbouring foreign countries"
    ],
    "answer": 0,
    "explanation": "Some States enjoy a special status under Article 371 due to their peculiar social and historical circumstances. These special powers are especially enjoyable with respect to protection of land rights of indigenous peoples, their culture and also preferential employment in government services.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-007",
    "type": "mcq",
    "subtopic": "Revenue Sources Guarantee",
    "difficulty": "Medium",
    "question": "Why does a federal constitution explicitly specify the sources of revenue for each level of government?",
    "options": [
      "To ensure its financial autonomy and operational independence",
      "To allow the central government to confiscate all state bank accounts",
      "To ensure that citizens pay zero taxes to municipal councils",
      "To prevent states from spending money on public schools"
    ],
    "answer": 0,
    "explanation": "Sources of revenue for each level of government are clearly specified to ensure its financial autonomy. A government cannot remain truly federal without independent financial resources.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-008",
    "type": "mcq",
    "subtopic": "Misuse of Article 356 Historical Decline",
    "difficulty": "Board Standard",
    "question": "Prior to 1990, the Central Government often dismissed State Governments led by rival political parties under Article 356 (President's Rule). What major development curtailed this undemocratic practice?",
    "options": [
      "A landmark Supreme Court judgment making arbitrary dismissal difficult, along with the rise of regional coalition governance",
      "Total abolition of the office of State Governor",
      "A complete ban on political party formation in states",
      "The United Nations Security Council intervention"
    ],
    "answer": 0,
    "explanation": "A major judgment of the Supreme Court made it difficult for the Central Government to dismiss state governments in an arbitrary manner. Coupled with the era of coalition governments, this significantly strengthened federal autonomy post-1990.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-009",
    "type": "mcq",
    "subtopic": "Dual Objectives of Federalism",
    "difficulty": "Medium",
    "question": "What are the two core dual objectives of a federal system?",
    "options": [
      "To safeguard and promote unity of the country, while at the same time accommodating regional diversity",
      "To eliminate regional cultural identities and enforce total uniformity",
      "To maximize central military expenditure and reduce social welfare",
      "To replace democratic elections with judicial decrees"
    ],
    "answer": 0,
    "explanation": "Federal system has dual objectives: to safeguard and promote unity of the country, while at the same time accommodate regional diversity.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-010",
    "type": "mcq",
    "subtopic": "Third Tier Scope & Scale",
    "difficulty": "Easy",
    "question": "India's constitutional experiment in local self-governance is the largest experiment in democracy anywhere in the world. Approximately how many elected representatives are there in rural and urban local bodies?",
    "options": ["About 36 lakh (3.6 million) elected representatives", "About 50,000 representatives", "About 1 lakh representatives", "About 10 million representatives"],
    "answer": 0,
    "explanation": "There are now about 36 lakh elected representatives in the panchayats and municipalities etc., all over the country. This number is bigger than the population of many countries in the world.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-011",
    "type": "mcq",
    "subtopic": "States Reorganisation Commission 1956",
    "difficulty": "Medium",
    "question": "States like Andhra Pradesh, Maharashtra, and Gujarat were reorganized or created primarily on the basis of:",
    "options": ["Linguistic identity (language spoken by people)", "Religious majorities", "Height of mountain ranges", "Annual rainfall levels"],
    "answer": 0,
    "explanation": "In 1947, the boundaries of several old States of India were changed in order to create new States. This was done to ensure that people who spoke the same language lived in the same State.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-012",
    "type": "mcq",
    "subtopic": "States Created on Culture and Ethnicity",
    "difficulty": "Medium",
    "question": "Which group of Indian states was created not on the basis of language, but to recognize differences based on culture, ethnicity, or geography?",
    "options": ["Nagaland, Uttarakhand, and Jharkhand", "Punjab and Haryana", "Kerala and Tamil Nadu", "Odisha and West Bengal"],
    "answer": 0,
    "explanation": "Some States were created not on the basis of language but to recognise differences based on culture, ethnicity or geography. These include States like Nagaland, Uttarakhand and Jharkhand.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-013",
    "type": "mcq",
    "subtopic": "Weaknesses of Local Self-Governments",
    "difficulty": "Board Standard",
    "question": "While constitutional status for local government has deepened democracy in India, what remains a significant continuing challenge?",
    "options": [
      "Many state governments have not transferred significant powers and adequate revenue resources to local bodies",
      "Villagers refuse to vote in panchayat elections",
      "The Supreme Court declared Panchayati Raj unconstitutional",
      "Panchayats are prohibited from maintaining village roads"
    ],
    "answer": 0,
    "explanation": "While elections are held regularly, Gram Sabhas are not held regularly. Most state governments have not transferred significant powers to the local governments, nor have they given adequate resources.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-014",
    "type": "mcq",
    "subtopic": "Brazil Experiment with Participatory Democracy",
    "difficulty": "Medium",
    "question": "The city of Porto Alegre in Brazil is globally renowned in democratic theory for developing which innovative local governance mechanism?",
    "options": [
      "Participatory Democracy where local citizens directly deliberate on the city budget",
      "A complete military dictatorship with zero municipal taxation",
      "A city ruled entirely by artificial intelligence computer algorithms",
      "Privatisation of all municipal roads and parks"
    ],
    "answer": 0,
    "explanation": "The city of Porto Alegre set up a parallel organisation operating alongside the municipal council, where nearly 50,000 citizens participate in meetings to decide how the municipal budget should be spent.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4 (Box Story: Porto Alegre)"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-015",
    "type": "mcq",
    "subtopic": "Concurrent List Forestry Subject",
    "difficulty": "Easy",
    "question": "Both the Central Government and State Governments can enact environmental and wildlife conservation regulations because 'Forests' are placed in the:",
    "options": ["Concurrent List", "Union List", "State List", "Residuary List"],
    "answer": 0,
    "explanation": "Forests, education, trade unions, marriage, adoption, and succession are placed in the Concurrent List, allowing both Centre and States to make laws.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-016",
    "type": "mcq",
    "subtopic": "Jurisdiction Defined",
    "difficulty": "Easy",
    "question": "The legal authority of a government or court over a specific territory, subject matter, or category of citizens is formally defined as:",
    "options": ["Jurisdiction", "Sovereign immunity", "Diplomatic protocol", "Veto prerogative"],
    "answer": 0,
    "explanation": "Jurisdiction is the area over which someone has legal authority. The area may be defined in terms of geographical boundaries or in terms of certain kinds of subjects.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Glossary"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-017",
    "type": "mcq",
    "subtopic": "Holding Together Equal Power Nuance",
    "difficulty": "Medium",
    "question": "In 'Holding Together' federations like India, constituent states:",
    "options": [
      "Very often do not have equal powers; some units are granted special powers or asymmetrical status",
      "Always possess identical identical constitutional authority and independent militaries",
      "Can secede unilaterally from the union at any moment",
      "Have zero control over their state police departments"
    ],
    "answer": 0,
    "explanation": "In 'holding together' federations, the central government tends to be more powerful vis-a-vis the States. Very often different constituent units of the federation have unequal powers; some units are granted special powers.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-018",
    "type": "mcq",
    "subtopic": "Panchayat Head Title",
    "difficulty": "Easy",
    "question": "Each village or a group of villages in some states has a Gram Panchayat. The directly elected president or head of the panchayat is called the:",
    "options": ["Sarpanch", "Mayor", "Collector", "Governor"],
    "answer": 0,
    "explanation": "Each village or a group of villages has a Gram Panchayat. This is a council consisting of several ward members, often called panch, and a president or Sarpanch.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-019",
    "type": "mcq",
    "subtopic": "Official Purpose of Hindi Promotion",
    "difficulty": "Medium",
    "question": "According to the Indian Constitution, the official policy of promoting Hindi as an official language:",
    "options": [
      "Does not mean that the Central Government can impose Hindi on States where people speak a different language",
      "Mandates that all citizens must pass a compulsory Hindi speaking exam",
      "Allows the Centre to dismiss any non-Hindi speaking Chief Minister",
      "Prohibits state civil services from using regional languages"
    ],
    "answer": 0,
    "explanation": "Promotion of Hindi continues to be the official policy of the Government of India. But promotion does not mean that the Central Government can impose Hindi on States where people speak a different language.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s2-020",
    "type": "mcq",
    "subtopic": "Cooperative Federalism Spirit",
    "difficulty": "Easy",
    "question": "The success of Indian federalism depends not merely on constitutional provisions, but fundamentally on:",
    "options": [
      "The nature of democratic politics, respect for diversity, and shared desire for living together",
      "The size of the national standing army",
      "The price of crude oil in international markets",
      "The total number of national holidays declared each year"
    ],
    "answer": 0,
    "explanation": "Constitutional provisions are necessary for the success of federalism but these are not sufficient. The real success of federalism in India can be attributed to the nature of democratic politics in our country.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  }
]

# -----------------------------------------------------------------------------
# CH 14 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch14_set3 = [
  {
    "id": "cbse10-sst-civ-ch14-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Linguistic Reorganisation Success",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The creation of linguistic States has made India more united and administration much easier.\nReason (R): Forming states on the basis of language satisfied regional aspirations and eliminated fears of forced cultural subjugation.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Experience proved that accommodating linguistic identities strengthened national integration rather than dividing it.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Supremacy in Concurrent List",
    "difficulty": "Board Standard",
    "question": "Assertion (A): If there is a conflict between a law enacted by the Union Parliament and a law enacted by a State Legislature on a Concurrent subject, the Union law prevails.\nReason (R): The Indian Constitution establishes a strong Centre to maintain national uniformity and legislative supremacy on matters of national interest.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Article 254 dictates that in case of conflict on a Concurrent subject, central legislation overrides state law.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Rigidity of Federal Amendments",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Central Government in India cannot unilaterally alter the division of powers between the Union and the States.\nReason (R): Any amendment to federal provisions requires a two-thirds majority in Parliament and ratification by at least half of the State Legislatures.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Federal provisions are entrenched; the requirement of state legislative ratification ensures that the Centre cannot abolish state powers unilaterally.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Language Policy Accommodation",
    "difficulty": "Board Standard",
    "question": "Assertion (A): India avoided the kind of violent linguistic conflict that Sri Lanka experienced.\nReason (R): Indian leaders adopted a flexible language policy by allowing English to continue alongside Hindi for official work and not imposing Hindi on non-Hindi speaking states.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Unlike Sri Lanka where Sinhala was aggressively imposed in 1956, Indian leaders demonstrated flexibility by recognizing 22 scheduled languages and retaining English for central administration.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: 1992 Decentralisation Impact",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The 1992 constitutional amendment made the third tier of democracy significantly more powerful and institutionalized.\nReason (R): Regular elections were made mandatory, seats were constitutionally reserved for women and backward classes, and State Election Commissions were established.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Prior to 1992, local body elections were irregular and controlled by state bureaucracy. The 73rd and 74th Amendments created constitutional mandates for regular elections and reservations.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-006",
    "type": "case_based",
    "subtopic": "Case Analysis - Cyber Crime Legislation",
    "difficulty": "Medium",
    "question": "A dispute arises over whether a State Assembly has the constitutional power to enact a law regulating international cryptocurrency exchanges operating on the internet. As 'cyber laws' and 'computer software' do not appear in the Union, State, or Concurrent lists, which level of government has legislative authority?",
    "options": [
      "The Union Government alone, because it possesses residuary legislative powers",
      "The State Government alone, because internet servers are physically located in states",
      "Neither government; only international courts can legislate",
      "The Gram Panchayat where the user resides"
    ],
    "answer": 0,
    "explanation": "Subjects not included in any of the three lists are known as 'residuary subjects'. Under Article 248 of the Indian Constitution, the Union Parliament has exclusive power to legislate on residuary matters.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-007",
    "type": "case_based",
    "subtopic": "Case Analysis - Gram Sabha Oversight",
    "difficulty": "Medium",
    "question": "The Sarpanch of a village plans to construct a community drainage ditch. Under Panchayati Raj norms, whose approval is required for the annual development plans and financial budget of the Gram Panchayat?",
    "options": [
      "The Gram Sabha, which consists of all adult registered voters of the village",
      "The District Superintendent of Police",
      "The Governor of the State exclusively",
      "The Union Minister of Rural Development"
    ],
    "answer": 0,
    "explanation": "The Gram Panchayat works under the overall democratic supervision of the Gram Sabha, which meets at least twice or thrice a year to approve the annual budget.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Coming Together vs Holding Together Powers",
    "difficulty": "Board Standard",
    "question": "Assertion (A): In 'Coming Together' federations like the USA, constituent states generally have equal powers and are very strong vis-a-vis the federal government.\nReason (R): In 'Holding Together' federations like India, constituent states very often have unequal powers, and the Central Government tends to be more powerful.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 1,
    "explanation": "Both statements are correct comparative constitutional facts from NCERT, though each describes a distinct historical route to federation.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-009",
    "type": "mcq",
    "subtopic": "Police and Law Enforcement Jurisdiction",
    "difficulty": "Easy",
    "question": "If a criminal case occurs in Lucknow, Uttar Pradesh, which government possesses constitutional jurisdiction over the 'Police' and public order?",
    "options": ["The State Government of Uttar Pradesh", "The Union Defence Ministry", "The United Nations", "The Mayor of New Delhi"],
    "answer": 0,
    "explanation": "'Police' and public order are subjects listed under the State List, meaning the State Government has exclusive administrative and legislative authority over them.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Judicial Arbiter in Federalism",
    "difficulty": "Board Standard",
    "question": "Assertion (A): An independent judiciary is an indispensable prerequisite for the functioning of a federal system.\nReason (R): The judiciary acts as an impartial umpire when disputes arise between the Central Government and State Governments over constitutional powers or revenue.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The judiciary plays the vital role of interpreting constitutional boundaries and settling inter-governmental jurisdictional disputes.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1 & 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-011",
    "type": "mcq",
    "subtopic": "Municipal Body Urban Distinction",
    "difficulty": "Easy",
    "question": "What is the primary difference in local government between small urban towns and big metropolitan cities?",
    "options": [
      "Municipalities operate in towns headed by a Municipal Chairperson, while big cities have Municipal Corporations headed by a Mayor",
      "Towns are ruled by Gram Sabhas, while cities are ruled by the military",
      "Municipalities do not hold elections, while Corporations do",
      "Cities have zero municipal councillors"
    ],
    "answer": 0,
    "explanation": "Municipalities are set up in smaller towns (headed by Municipal Chairperson). Big metropolitan cities are constituted into Municipal Corporations (headed by a Mayor).",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis - Civil Services Examination Medium",
    "difficulty": "Medium",
    "question": "A candidate appearing for the Union Public Service Commission (UPSC) Civil Services Examination wishes to write the paper in Tamil or Marathi. According to the Eighth Schedule of the Constitution, is this permissible?",
    "options": [
      "Yes, a candidate may opt to take the examination in any of the 22 Scheduled Languages",
      "No, only English and Hindi are constitutionally permitted",
      "No, only Hindi is allowed in central government recruitment",
      "Yes, but only if the candidate pays a special linguistic penalty fee"
    ],
    "answer": 0,
    "explanation": "A candidate in an examination conducted for the Central Government positions may opt to take the examination in any of the 22 Scheduled Languages recognized by the Constitution.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-013",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Financial Autonomy Necessity",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Constitution clearly demarcates specific taxation and revenue powers for the Centre and the States.\nReason (R): Without guaranteed independent revenue sources, states would remain financially dependent beggars at the mercy of the Central Government.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Financial autonomy is an essential pillar of federalism. Clear revenue streams prevent central financial coercion over states.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-014",
    "type": "mcq",
    "subtopic": "Decentralisation Deepening Democracy",
    "difficulty": "Medium",
    "question": "How does constitutional decentralisation at the grassroots directly promote the 'habit of democratic participation'?",
    "options": [
      "Local government provides a direct practical school for citizens to participate in local budgeting and decision-making directly",
      "It makes voting mandatory under penalty of imprisonment",
      "It allows villages to refuse all central developmental grants",
      "It eliminates political disagreements permanently"
    ],
    "answer": 0,
    "explanation": "At the local level, it is possible for the people to directly participate in decision making. This helps to inculcate a habit of democratic participation.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-015",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Coalition Government Culture",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The post-1990 era saw the decline of single-party dominance at the Centre and the emergence of strong regional parties.\nReason (R): This development fostered a genuine culture of power sharing and reinforced constitutional respect for the autonomy of State Governments.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The necessity of coalition building elevated the bargaining power of regional parties, directly solidifying federal balance against central overreach.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 3"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-016",
    "type": "mcq",
    "subtopic": "Belgium vs Sri Lanka System Comparison",
    "difficulty": "Hard",
    "question": "In 1993, Belgium amended its constitution to transform its government into which system, while Sri Lanka continued to remain which system?",
    "options": [
      "Belgium shifted from a unitary to a federal system; Sri Lanka remained a unitary system",
      "Belgium became a unitary monarchy; Sri Lanka became a multi-tiered federation",
      "Both countries became unitary states without regional parliaments",
      "Both countries abolished all regional languages"
    ],
    "answer": 0,
    "explanation": "In 1993, regional governments in Belgium were given constitutional powers that were no longer dependent on the central government, shifting Belgium from a unitary to a federal system. Sri Lanka continues to be a unitary system where the national government has all powers.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-017",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Overlapping Tiers Same Citizens",
    "difficulty": "Board Standard",
    "question": "Assertion (A): In India, a citizen is governed simultaneously by the Union Government, a State Government, and a Local Panchayat or Municipality.\nReason (R): Different tiers of government govern the same citizens, but each tier has its own separate constitutional jurisdiction in matters of legislation, taxation, and administration.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "This is a fundamental feature of federalism: co-existing jurisdictions over the same populace defined by constitutional lists.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 1"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-018",
    "type": "mcq",
    "subtopic": "Defense and Foreign Affairs Rationale",
    "difficulty": "Easy",
    "question": "Why are 'Defense' and 'Foreign Affairs' placed exclusively in the Union List rather than the State List?",
    "options": [
      "Because we need a uniform defense policy and external diplomatic stance for the entire nation",
      "Because states have zero geographic borders",
      "Because only central ministers speak foreign languages",
      "Because the United Nations only recognises central governments"
    ],
    "answer": 0,
    "explanation": "Subjects of national importance like defence, foreign affairs, and currency are placed in the Union List because the country needs a uniform policy on these matters throughout the nation.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 2"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-019",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Women Leadership in Local Bodies",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The 73rd Constitutional Amendment has dramatically increased women's voice and representation in Indian democracy.\nReason (R): Over ten lakh (one million) women are currently elected as representatives in rural panchayats and urban local bodies across the country.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The 1/3rd constitutional reservation for women in local self-governments created a massive pool of over 10 lakh elected women leaders, deepening grassroots gender empowerment.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  },
  {
    "id": "cbse10-sst-civ-ch14-s3-020",
    "type": "mcq",
    "subtopic": "Core Principle of Decentralisation",
    "difficulty": "Easy",
    "question": "Decentralisation takes away power from the Central and State governments and gives it to local government because:",
    "options": [
      "Local self-government is the best way to realise one important principle of democracy, namely local self-rule",
      "Central governments want to dissolve themselves permanently",
      "Villagers do not pay any national taxes",
      "High Courts do not have jurisdiction in rural districts"
    ],
    "answer": 0,
    "explanation": "Local people know their problems and priorities best. Decentralisation is the most effective way to realize participatory democracy and direct self-rule.",
    "citation": "NCERT Class 10 Civics, Chapter 2, Section 4"
  }
]

# Write Chapter 14 Sets 2 and 3
with open(os.path.join(DATA_DIR, "ch14_federalism_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch14_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch14_federalism_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch14_set3}, f, indent=2, ensure_ascii=False)

print("Generated: ch14 Sets 2 & 3 (40 Qs)")


# Write Chapter 15 Set 1
with open(os.path.join(DATA_DIR, "ch15_gender_religion_caste_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch15_set1}, f, indent=2, ensure_ascii=False)

print("Generated: ch15_gender_religion_caste_set1.json (20 Qs)")
