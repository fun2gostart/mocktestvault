#!/usr/bin/env python3
"""
Generates Civics Chapter 17 (Outcomes of Democracy) Sets 1, 2, and 3.
Total: 3 sets = 60 questions.
100% NCERT and CBSE Class 10 Social Science Board grounded.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# =============================================================================
# CHAPTER 17: OUTCOMES OF DEMOCRACY (Civics Ch 5 / Total SST Ch 17)
# =============================================================================

# -----------------------------------------------------------------------------
# SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch17_set1 = [
  {
    "id": "cbse10-sst-civ-ch17-s1-001",
    "type": "mcq",
    "subtopic": "Fundamental Reasons Supporting Democracy",
    "difficulty": "Easy",
    "question": "Which of the following is widely accepted as a core principle demonstrating why democracy is superior to non-democratic regimes?",
    "options": [
      "It promotes equality among citizens and enhances the dignity of the individual",
      "It eliminates the need for national defense spending completely",
      "It guarantees uniform wealth distribution within two fiscal quarters",
      "It allows executive heads to rule without any parliamentary consultation"
    ],
    "answer": 0,
    "explanation": "Democracy is considered a better form of government because it promotes equality among citizens, enhances individual dignity, improves decision quality, provides conflict resolution mechanisms, and allows room to correct mistakes.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-002",
    "type": "mcq",
    "subtopic": "Accountability in Democracy",
    "difficulty": "Easy",
    "question": "In a democratic government, to whom are elected rulers fundamentally accountable?",
    "options": [
      "To the citizens and electorate who vote them into power",
      "Only to the international monetary institutions",
      "To hereditary feudal landholders",
      "To supreme military commanders"
    ],
    "answer": 0,
    "explanation": "In a democracy, we are most concerned with ensuring that people will have the right to choose their rulers and people will have control over the rulers. Whenever possible, citizens should participate in decision-making.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-003",
    "type": "mcq",
    "subtopic": "Democratic Decision-Making Deliberation",
    "difficulty": "Medium",
    "question": "Why do democratic decision-making processes often take more time compared to non-democratic dictatorships?",
    "options": [
      "Because democracies follow established norms, deliberation, and extensive consultation before arriving at a decision",
      "Because democratic legislatures only meet once every ten years",
      "Because computers and telecommunications are legally banned in parliament",
      "Because judges must personally approve every municipal bylaw"
    ],
    "answer": 0,
    "explanation": "Democracy is based on the idea of deliberation and negotiation. A non-democratic government can take decisions very quickly because it does not have to bother about consultation or parliamentary majorities. But democracy follows norms and procedures, resulting in more acceptable decisions.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-004",
    "type": "mcq",
    "subtopic": "Transparency Definition",
    "difficulty": "Medium",
    "question": "The right and the means available to a citizen in a democracy to examine the process of government decision-making is termed:",
    "options": [
      "Transparency",
      "Autocracy",
      "Bureaucratic hegemony",
      "Judicial oligarchy"
    ],
    "answer": 0,
    "explanation": "A citizen who wants to know if a decision was taken through the correct procedures can find this out. She has the right and the means to examine the process of decision making. This is known as transparency.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-005",
    "type": "mcq",
    "subtopic": "Right to Information (RTI)",
    "difficulty": "Easy",
    "question": "In India, which landmark legislation enacted in 2005 empowered citizens to inspect government records and uphold transparency?",
    "options": [
      "Right to Information Act (RTI Act 2005)",
      "National Education Policy Act",
      "Consumer Protection Act",
      "Industrial Disputes Act"
    ],
    "answer": 0,
    "explanation": "The Right to Information (RTI) Act of 2005 empowers Indian citizens to seek information from public authorities, promoting transparency and holding the government accountable.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Box Note on Transparency"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-006",
    "type": "mcq",
    "subtopic": "Legitimate Government Concept",
    "difficulty": "Medium",
    "question": "Why is a democratic government regarded as a 'legitimate government' despite occasional inefficiency or slowness?",
    "options": [
      "Because it is the people's own freely elected government",
      "Because it is chosen by international observers and foreign treaties",
      "Because it commands a standing army larger than its civil workforce",
      "Because it suppresses dissenting political opinions entirely"
    ],
    "answer": 0,
    "explanation": "A democratic government may be slow, less efficient, not always very responsive or clean. But a democratic government is the people's own government. That is why there is an overwhelming support for the idea of democracy all over the world.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-007",
    "type": "mcq",
    "subtopic": "Democracy vs Dictatorship: Economic Growth",
    "difficulty": "Hard",
    "question": "When comparing economic growth records between democracies and dictatorships during the period 1950–2000, evidence shows that:",
    "options": [
      "Dictatorships had a slightly higher rate of economic growth overall",
      "Democracies grew at ten times the speed of any authoritarian state",
      "Economic growth was completely zero across all democratic nations",
      "No measurable economic data was recorded during this 50-year period"
    ],
    "answer": 0,
    "explanation": "If you consider all democracies and all dictatorships for the fifty years between 1950 and 2000, dictatorships have slightly higher rates of economic growth. However, among poor countries, the difference in economic growth is negligible.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.2"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-008",
    "type": "mcq",
    "subtopic": "Determinants of Economic Development",
    "difficulty": "Medium",
    "question": "Economic development of a nation depends on several factors besides the form of government. Which of the following is NOT a primary determinant?",
    "options": [
      "The ruling dynasty's astrological horoscope",
      "Country's population size and demographic profile",
      "Global economic situation and foreign trade partnerships",
      "Cooperation from other nations and economic priorities adopted"
    ],
    "answer": 0,
    "explanation": "Economic development depends on several factors: country's population size, global situation, cooperation from other countries, economic priorities adopted by the country, etc. Astrological beliefs have no factual role.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.2"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-009",
    "type": "mcq",
    "subtopic": "Reduction of Inequality",
    "difficulty": "Medium",
    "question": "Democracies are based on political equality, yet in the economic sphere they have frequently struggled to:",
    "options": [
      "Reduce growing income inequalities between the ultra-rich and the impoverished",
      "Hold universal adult franchise general elections",
      "Allow legal registration of opposition political parties",
      "Permit citizens to criticize parliamentary policies"
    ],
    "answer": 0,
    "explanation": "Parallel to the process of bringing individuals into the political arena on an equal footing, we find growing economic inequalities. A small number of ultra-rich enjoy a highly disproportionate share of wealth and incomes, while the poor struggle for basic needs.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.3"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-010",
    "type": "mcq",
    "subtopic": "Poverty in South Asian Democracies",
    "difficulty": "Medium",
    "question": "In countries like Bangladesh, what stark economic reality coexists with political democracy?",
    "options": [
      "More than half of its total population lives in acute poverty",
      "All citizens belong to the top 1% global income tier",
      "Private commerce and agricultural markets are legally outlawed",
      "The national poverty rate reached zero in 1995"
    ],
    "answer": 0,
    "explanation": "In actual life, democracies do not appear to be very successful in reducing economic inequalities. In Bangladesh, more than half of its population lives in poverty. People in several poor countries are now dependent on the rich countries even for food supplies.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.3"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-011",
    "type": "mcq",
    "subtopic": "Accommodation of Social Diversity",
    "difficulty": "Easy",
    "question": "What is the primary mechanism through which democracies handle social differences and ethnic conflicts?",
    "options": [
      "By evolving open mechanisms and constitutional dialogue to negotiate and accommodate differences peacefully",
      "By permanently disenfranchising minority cultural groups",
      "By declaring martial law whenever community disagreements arise",
      "By expelling linguistic minorities to neighbouring countries"
    ],
    "answer": 0,
    "explanation": "No society can fully and permanently resolve conflicts among different groups. But we can certainly learn to respect these differences and we can also evolve mechanisms to negotiate the differences. Democracy is best suited to produce this outcome.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-012",
    "type": "mcq",
    "subtopic": "Two Conditions for Accommodating Diversity",
    "difficulty": "Hard",
    "question": "In order to successfully accommodate social diversity, democracy must fulfill two conditions. The first condition is that:",
    "options": [
      "The majority must always work with the minority so that governments represent the general collective view",
      "The minority community must be stripped of judicial rights",
      "Elections must be won exclusively on religious identity appeals",
      "The opposition leader must be exiled during legislative voting"
    ],
    "answer": 0,
    "explanation": "Condition 1: It is necessary to understand that democracy is not simply rule by majority opinion. The majority always needs to work with the minority so that governments function to represent the general view.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-013",
    "type": "mcq",
    "subtopic": "Majority Rule Condition",
    "difficulty": "Hard",
    "question": "What is the second essential condition for a healthy democracy regarding majority rule?",
    "options": [
      "Rule by majority must not become rule by a single religious, racial, or linguistic majority community permanently",
      "The majority must seize all private commercial banks",
      "The majority must suspend the constitution every alternate year",
      "The majority party must permanently abolish local municipal elections"
    ],
    "answer": 0,
    "explanation": "Condition 2: Rule by majority must not become rule by majority community in terms of religion or race or linguistic group. Rule by majority means that in case of every decision or election, different persons and groups may and can form a majority.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-014",
    "type": "mcq",
    "subtopic": "Dignity and Freedom of Women",
    "difficulty": "Medium",
    "question": "How has democracy strengthened the long struggle of women for equality and respect in patriarchal societies?",
    "options": [
      "By providing a moral and legal recognition to the principle of gender equality, making discrimination legally challengeable",
      "By completely eliminating domestic chauvinism overnight",
      "By replacing all male judges with royal appointees",
      "By creating a single-party female dictatorship"
    ],
    "answer": 0,
    "explanation": "Most societies across the world were historically male dominated. Long struggles by women have created some sensitivity today that respect to and equal treatment of women are necessary ingredients of a democratic society. Once the principle is recognised, it becomes easier for women to wage a struggle.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-015",
    "type": "mcq",
    "subtopic": "Caste Claims in Indian Democracy",
    "difficulty": "Medium",
    "question": "How has democracy in India impacted historically disadvantaged and discriminated castes?",
    "options": [
      "It has strengthened their claims for equal status and equal opportunities through constitutional guarantees and voting power",
      "It has made traditional caste discrimination legally mandatory",
      "It has forced all backward communities to abandon agriculture",
      "It has eliminated all reservations in public employment and education"
    ],
    "answer": 0,
    "explanation": "Democracy in India has strengthened the claims of the disadvantaged and discriminated castes for equal status and equal opportunities. There are still instances of caste-based inequalities and atrocities, but these lack moral and legal foundations.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-016",
    "type": "mcq",
    "subtopic": "Democracy's Ongoing Examination",
    "difficulty": "Hard",
    "question": "What is meant by the statement: 'The most distinctive thing about democracy is that its examination never gets over'?",
    "options": [
      "As democracy passes one test, people produce another test; people constantly demand more benefits and better governance",
      "School examinations are conducted every weekend under democratic law",
      "Civil servants must take competitive exams every calendar month",
      "Democratic parliaments dissolve themselves every thirty days"
    ],
    "answer": 0,
    "explanation": "The most distinctive thing about democracy is that its examination never gets over. As democracy passes one test, it produces another test. As people get some benefits of democracy, they ask for more and want to make democracy even better.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-017",
    "type": "mcq",
    "subtopic": "Citizen Awareness and Complaints",
    "difficulty": "Medium",
    "question": "A public that is vocal, critical, and continuously complains about government performance is considered:",
    "options": [
      "A testimony to the success of democracy, showing citizens are alert and transform subjects into active participants",
      "A sign of imminent civil collapse and institutional treason",
      "A punishable offense under parliamentary penal codes",
      "Proof that military dictatorship is immediately required"
    ],
    "answer": 0,
    "explanation": "A public expression of dissatisfaction with democracy shows the success of the democratic project: it transforms people from the status of a subject into that of a citizen. Most individuals today believe that their vote makes a difference.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-018",
    "type": "mcq",
    "subtopic": "Global Support for Democracy",
    "difficulty": "Easy",
    "question": "Surveys across South Asian nations (India, Pakistan, Bangladesh, Sri Lanka, Nepal) show that support for democracy is:",
    "options": [
      "Widespread and overwhelmingly preferred over dictatorship across all countries",
      "Restricted only to university professors and wealthy bankers",
      "Non-existent, with over 90% preferring direct foreign rule",
      "Declining rapidly in favor of military juntas in every country"
    ],
    "answer": 0,
    "explanation": "Evidence from South Asia shows that support for democracy exists across countries with democratic regimes as well as regimes without democracy. People wish to be ruled by representatives elected by them.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1 & Table on South Asia"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-019",
    "type": "mcq",
    "subtopic": "Room to Correct Mistakes",
    "difficulty": "Easy",
    "question": "Why does a democracy provide better room to correct its own policy mistakes than an autocracy?",
    "options": [
      "Decisions are open to public debate and scrutiny, and ruling parties can be voted out if they refuse to rectify errors",
      "The Supreme Court automatically removes prime ministers every Sunday",
      "Government policies are erased automatically after six months",
      "All laws require unanimous consent of every adult citizen"
    ],
    "answer": 0,
    "explanation": "Democracy allows room to correct mistakes because mistakes cannot be hidden for long. There is a space for public discussion on these mistakes and room for correction; either rulers have to change their decisions or rulers themselves can be changed.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s1-020",
    "type": "mcq",
    "subtopic": "Core Dilemma in Evaluating Democracy",
    "difficulty": "Medium",
    "question": "What is the primary dilemma educators and political scientists observe when assessing democracy?",
    "options": [
      "Democracy is seen as good in principle, but felt to be not so good in its actual practice",
      "Democracy is practiced everywhere but has no written constitution",
      "Democracy requires all citizens to serve in active combat forces",
      "Democracy bans newspapers and independent investigative journalism"
    ],
    "answer": 0,
    "explanation": "Our fascination with democracy often pushes us into taking a position that democracy can address all socio-economic and political problems. We face a dilemma: democracy is seen to be good in principle, but felt to be not so good in its practice.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  }
]

# -----------------------------------------------------------------------------
# SET 2: NCERT Exemplar & Applied Scenarios (20 Qs)
# -----------------------------------------------------------------------------
ch17_set2 = [
  {
    "id": "cbse10-sst-civ-ch17-s2-001",
    "type": "mcq",
    "subtopic": "Responsiveness of Democratic Governments",
    "difficulty": "Medium",
    "question": "When examining the actual record of democracies on being 'responsive to the needs and demands of the people', what does historical evidence suggest?",
    "options": [
      "Democracies often frustrate the needs of the people and frequently ignore the demands of a majority of their population",
      "Democracies fulfill 100% of all citizen requests within 24 hours of petitioning",
      "Democracies are immune to corruption and bribery at all bureaucratic tiers",
      "Democracies never experience worker strikes or civic demonstrations"
    ],
    "answer": 0,
    "explanation": "The record of democracies is not impressive on responsiveness: democracies often frustrate the needs of the people and often ignore the demands of a majority of its population. The routine tales of corruption are enough to convince that democracy is not free of this evil.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-002",
    "type": "mcq",
    "subtopic": "Comparing Corruption: Democracy vs Dictatorship",
    "difficulty": "Medium",
    "question": "Does non-democratic rule eliminate bureaucratic corruption better than democracy?",
    "options": [
      "No; there is nothing to show that non-democracies are less corrupt or more sensitive to the people, but their corruption is concealed from public scrutiny",
      "Yes; non-democratic rulers are constitutionally incapable of accepting bribes",
      "Yes; military dictatorships execute all corrupt officials within one hour",
      "No; non-democracies have no government officials or revenue systems"
    ],
    "answer": 0,
    "explanation": "There is nothing to show that non-democracies are less corrupt or more sensitive to the people. In fact, in dictatorships there is no free press or independent judiciary to investigate and expose corruption.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-003",
    "type": "mcq",
    "subtopic": "Evaluating Democracy by Real Standards",
    "difficulty": "Board Standard",
    "question": "If you want to evaluate democracies on the basis of expected institutional practices, which regular setup would you look for?",
    "options": [
      "Regular, free and fair elections, open public debate on major policies and legislation, and citizens' right to information",
      "Single-party rule with life tenure for the prime minister",
      "Judicial appointments made directly by the army chief of staff",
      "Mandatory government censorship on all private news media"
    ],
    "answer": 0,
    "explanation": "To measure democracy on expected outcomes, we look for practices and institutions: regular, free and fair elections; open public debate on major policies and legislations; and citizens' right to information about the government and its functioning.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-004",
    "type": "mcq",
    "subtopic": "Record on Free and Fair Elections",
    "difficulty": "Medium",
    "question": "What does the historical record show regarding democracies holding regular and fair elections?",
    "options": [
      "Most democracies have succeeded in setting up regular and free elections, though fair elections offering every voter equal opportunity still face challenges",
      "No democracy has ever managed to conduct more than one general election",
      "Elections in all democracies are completely rigged by commercial corporations",
      "Democracies have replaced ballot voting with hereditary succession"
    ],
    "answer": 0,
    "explanation": "Most democracies have set up regular and free elections and conditions for open public debate. But most democracies fall short of elections that provide a fair chance to everyone and in subjecting every decision to public debate.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-005",
    "type": "mcq",
    "subtopic": "Inequality in Brazil and South Africa",
    "difficulty": "Hard",
    "question": "In highly unequal democratic countries such as South Africa and Brazil, official data indicates that:",
    "options": [
      "The top 20% of the population takes away more than 60% of the national income, while the bottom 20% receives less than 3%",
      "National income is distributed with perfect mathematical equality to each citizen",
      "The bottom 20% owns 95% of all national agricultural land and gold mines",
      "Taxation has abolished the concept of private personal earnings"
    ],
    "answer": 0,
    "explanation": "In countries like South Africa and Brazil, the top 20% people take away more than 60% of the national income, leaving less than 3% for the bottom 20%. This illustrates severe income inequality in electoral democracies.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Table on Inequality of Income in Selected Countries"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-006",
    "type": "mcq",
    "subtopic": "Democracy as a Condition vs Outcome",
    "difficulty": "Board Standard",
    "question": "Political science clarifies that democracy is primarily a 'form of government'. What does this imply for solving socio-economic problems?",
    "options": [
      "It can only create conditions for achieving something; the citizens have to take advantage of those conditions and achieve those goals",
      "It automatically solves all poverty and unemployment without any citizen effort",
      "It relieves citizens of any duty to pay taxes or obey traffic laws",
      "It guarantees that all citizens will become millionaire investors"
    ],
    "answer": 0,
    "explanation": "Our first step is to recognise that democracy is just a form of government. It can only create conditions for achieving something. The citizens have to take advantage of those conditions and achieve those goals.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-007",
    "type": "mcq",
    "subtopic": "Conflict Resolution in Plural Societies",
    "difficulty": "Medium",
    "question": "Why did non-democratic regimes like Sri Lanka (historically under majoritarian policies) fail to accommodate diversity compared to power-sharing democracies like Belgium?",
    "options": [
      "Non-democratic and majoritarian systems often turn a blind eye to or suppress internal social differences, leading to violent civil strife",
      "Sri Lanka had too many regional parliamentary elections every month",
      "Belgium forced all citizens to speak a single newly invented language",
      "Sri Lanka banned foreign tourism and international tea exports"
    ],
    "answer": 0,
    "explanation": "The ability to handle social differences, divisions and conflict is a definite plus point of democratic regimes. But the example of Sri Lanka reminds us that a democracy must fulfill two conditions (working with minority, avoiding majoritarian oppression) to achieve this.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-008",
    "type": "mcq",
    "subtopic": "Democratic Legitimacy Survey in India",
    "difficulty": "Medium",
    "question": "In nationwide surveys in India, when citizens were asked: 'Does your vote make a difference?', what was the predominant response?",
    "options": [
      "An overwhelming majority of voters (over 65%) affirmed that their vote definitely makes a difference in government functioning",
      "Almost all voters stated that their vote is completely meaningless",
      "Only hereditary royal families claimed their vote makes a difference",
      "Voters believed that elections are decided purely by lotteries"
    ],
    "answer": 0,
    "explanation": "In India and across South Asia, survey data demonstrates that an overwhelming majority of citizens believe their vote makes a difference to the way things are run in the country, confirming democratic legitimacy.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Survey Chart: Efficacy of Voting"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-009",
    "type": "mcq",
    "subtopic": "Economic Disparities and Political Power",
    "difficulty": "Hard",
    "question": "Even though poor voters constitute a massive proportion of the electorate in democracies, why do democratically elected governments often seem reluctant to address poverty aggressively?",
    "options": [
      "Because rich donors and powerful commercial lobbies exert immense influence over party campaigns and economic policy decisions",
      "Because the constitution legally forbids spending revenue on welfare schemes",
      "Because poor citizens are barred from voting in general elections",
      "Because the United Nations disallows domestic antipoverty programs"
    ],
    "answer": 0,
    "explanation": "The poor constitute a large proportion of our voters and no party will like to lose their votes. Yet democratically elected governments do not appear to be as keen to address the question of poverty as you would expect them to, largely due to political complacency and influence of economic elites.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.3"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-010",
    "type": "mcq",
    "subtopic": "Public Scrutiny of Rulers",
    "difficulty": "Medium",
    "question": "Which of the following scenarios best demonstrates that people are acting as 'citizens' rather than 'subjects' in a democracy?",
    "options": [
      "Citizens organise peaceful demonstrations and file public petitions demanding accountability when a bridge project fails safety audits",
      "Citizens quietly obey every administrative edict without questioning misuse of funds",
      "Citizens celebrate hereditary dynastic rulers with unconditional loyalty",
      "Citizens refuse to participate in census surveys or register their births"
    ],
    "answer": 0,
    "explanation": "The transformation of people from the status of subjects to citizens occurs when they recognise their rights, critically assess ruler actions, and organise civic actions to hold officials accountable.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-011",
    "type": "mcq",
    "subtopic": "Democracy and Individual Liberty",
    "difficulty": "Easy",
    "question": "Why is individual freedom and dignity inherently safer in a democracy than in a monarchy or military junta?",
    "options": [
      "Because democratic constitutions grant fundamental civil rights enforceable by an independent judiciary",
      "Because monarchs sign contracts with trade unions every morning",
      "Because military generals are forbidden from commanding soldiers",
      "Because autocracies have no police forces or jails"
    ],
    "answer": 0,
    "explanation": "Democracy stands much superior to any other form of government in promoting dignity and freedom of the individual. In non-democracies, the principle of individual freedom often has no legal or moral backing, and subjects cannot demand rights as legal entitlements.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-012",
    "type": "mcq",
    "subtopic": "Majority vs Permanent Minority",
    "difficulty": "Board Standard",
    "question": "If a democratic system permanently excludes a minority community from ever participating in the ruling majority coalition based purely on their birth or religion, what happens to that democracy?",
    "options": [
      "Democracy ceases to be accommodative for that group and violates the fundamental principle of democratic equality",
      "The democracy automatically becomes the wealthiest economy on Earth",
      "The country qualifies for automatic permanent membership in the UN Security Council",
      "The minority group achieves supreme legislative veto power"
    ],
    "answer": 0,
    "explanation": "Democracy remains democracy only as long as every citizen has a chance of being in majority at some point of time. If someone is barred from being in majority on the basis of birth, then the democratic rule ceases to be accommodative for that person or group.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-013",
    "type": "mcq",
    "subtopic": "Democracy and Economic Quality of Life",
    "difficulty": "Medium",
    "question": "When examining poor countries under democratic rule versus poor countries under authoritarian rule, what does empirical evidence demonstrate about human development?",
    "options": [
      "There is negligible difference in economic growth rates, but democracies offer vastly superior civil liberties and social security protection",
      "Authoritarian poor countries have ten times higher literacy rates than any democracy",
      "Democracies have higher infant mortality rates than any dictatorship",
      "All authoritarian regimes achieve 100% university graduation rates"
    ],
    "answer": 0,
    "explanation": "The difference in rates of economic growth between less developed countries with dictatorships and democracies is negligible. Overall, we cannot say that democracy is a guarantee of economic development, but we can expect democracy not to lag behind dictatorships in this respect while preserving human rights.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.2"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-014",
    "type": "mcq",
    "subtopic": "Case Analysis: Women's Equal Dignity",
    "difficulty": "Medium",
    "question": "Even if male chauvinism and domestic violence still persist in many households, why is the democratic recognition of women's rights a decisive turning point?",
    "options": [
      "It provides women with legal rights and institutional standing to wage organized struggles against injustice in courts and public forums",
      "It automatically converts all husbands into domestic servants",
      "It bans men from entering legislative assemblies",
      "It dissolves all family institutions permanently"
    ],
    "answer": 0,
    "explanation": "Once the principle of equal treatment of women is recognised, it becomes easier for women to wage a struggle against what is now unacceptable legally and morally. In a non-democratic setup, this unacceptability would not have legal basis.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-015",
    "type": "mcq",
    "subtopic": "Electoral Efficiency vs Consultation",
    "difficulty": "Medium",
    "question": "A critic argues: 'Democracies are inefficient because debates in parliament take months before a law is passed.' How does democratic theory counter this criticism?",
    "options": [
      "The time spent on consultation prevents hasty, flawed, or oppressive decisions, ensuring wider public acceptance and long-term stability",
      "Parliamentary debates are conducted solely to entertain television audiences",
      "Dictatorial decrees are always 100% error-free and never cause public unrest",
      "Laws should only be written by private consulting corporations"
    ],
    "answer": 0,
    "explanation": "The cost of time that democracy pays is perhaps worth it because decisions arrived at through consultation and debate are more effective, balanced, and widely accepted by the populace.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-016",
    "type": "mcq",
    "subtopic": "Democracy and National Disintegration",
    "difficulty": "Hard",
    "question": "Why did multinational and multi-ethnic democracies like India remain united, while some authoritarian regimes collapsed into ethnic Balkanisation?",
    "options": [
      "Because democratic power sharing and linguistic state reorganization accommodated regional aspirations within a unified constitutional framework",
      "Because India strictly banned all regional languages and native dialects",
      "Because India maintained mandatory military rule across all state capitals",
      "Because regional identities were eradicated by royal decree in 1947"
    ],
    "answer": 0,
    "explanation": "Democracies accommodate social diversity through power sharing, federal autonomy, and linguistic reorganization (as in Belgium and India), whereas authoritarian suppression of ethnic aspirations triggers violent civil collapse.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-017",
    "type": "mcq",
    "subtopic": "The Voice of the Ordinary Citizen",
    "difficulty": "Easy",
    "question": "In a democracy, what transforms an ordinary voter from a helpless subject into an empowered political sovereign?",
    "options": [
      "The constitutional right to universal adult franchise, secret ballot, and regular accountability of rulers",
      "Direct monetary subsidies deposited every night by commercial banks",
      "The privilege of carrying military firearms in parliament",
      "Exemption from all criminal and civil penal laws"
    ],
    "answer": 0,
    "explanation": "Universal adult franchise, equal voting power ('one person, one vote, one value'), and regular elections give every citizen a constitutional voice that politicians cannot ignore.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-018",
    "type": "mcq",
    "subtopic": "Expectations from Democracy as an Indicator",
    "difficulty": "Medium",
    "question": "When citizens express dissatisfaction that public hospitals and government schools are not functioning adequately, this demonstrates that:",
    "options": [
      "Citizens have developed high democratic consciousness and hold the state accountable for public welfare delivery",
      "Citizens want to replace democracy with a military dictatorship immediately",
      "The country should permanently abolish public healthcare and education",
      "Elections have failed completely and should be canceled"
    ],
    "answer": 0,
    "explanation": "The fact that people are complaining is itself a testimony to the success of democracy: it shows that people have developed awareness and the ability to expect and to look critically at power holders and the high and the mighty.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-019",
    "type": "mcq",
    "subtopic": "Evaluating Non-Democratic Governments",
    "difficulty": "Medium",
    "question": "Which of the following is an undeniable structural defect inherent in non-democratic regimes?",
    "options": [
      "The rulers are not accountable to the citizens, and there are no institutional mechanisms to change them peacefully if they turn tyrannical",
      "They spend too much time debating legislation in public assemblies",
      "They are compelled to publish all financial transactions on public websites",
      "They give supreme veto rights to independent trade unions"
    ],
    "answer": 0,
    "explanation": "Non-democratic rulers do not have to face elections or parliamentary questioning; citizens have no legal mechanism to demand transparency or remove despotic rulers peacefully.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s2-020",
    "type": "mcq",
    "subtopic": "Summary Assessment of Democracy",
    "difficulty": "Board Standard",
    "question": "Which statement best captures the realistic assessment of democratic outcomes according to the NCERT curriculum?",
    "options": [
      "Democracy is not a magical cure for all ills, but it provides the most just, transparent, and dignified institutional framework for human self-governance",
      "Democracy guarantees that every family will receive identical income regardless of effort",
      "Democracy has proved worse than military rule in protecting fundamental human liberties",
      "Democracy functions perfectly without any citizen participation or vigilance"
    ],
    "answer": 0,
    "explanation": "Democracy is not a magical solution to all economic and social woes, but it is demonstrably better than any alternative because it respects human dignity, resolves conflicts peacefully, and ensures rulers remain answerable to the governed.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Chapter Overview"
  }
]

# -----------------------------------------------------------------------------
# SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch17_set3 = [
  {
    "id": "cbse10-sst-civ-ch17-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Deliberation vs Efficiency",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Democratic governments take more time to take decisions compared to authoritarian regimes.\nReason (R): Democratic decision-making is based on consultation, negotiation, and adherence to established constitutional procedures.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Democracy is based on deliberation and negotiation. Because it follows norms and procedures, decision-making takes time, but the decisions are more acceptable and effective.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Legitimate Government",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Democratic government is universally acknowledged as a legitimate government.\nReason (R): A democratic government is the people's own government, elected by the citizens through universal adult franchise.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Legitimacy stems directly from popular sovereignty: because the rulers are elected by the people themselves, the government enjoys universal legal and moral legitimacy.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Economic Growth in Democracies",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Democracy cannot be considered a sole guarantee of rapid economic development.\nReason (R): Economic development depends on a multitude of factors including population size, global economic climate, foreign capital cooperation, and domestic policy priorities.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Form of government alone does not dictate economic prosperity. Economic growth is driven by population, resource endowment, trade relationships, and domestic infrastructure priorities.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.2"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Transparency in Governance",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Transparency is an indispensable feature of democratic governance.\nReason (R): In a democracy, citizens possess the legal right and institutional means to examine the process through which decisions were made by public officials.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Transparency means that government procedures are open to public scrutiny; citizens have the right and mechanisms (like the RTI Act) to inspect government decision-making.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Accommodating Social Differences",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Democracies are uniquely capable of accommodating social diversities and resolving internal social friction peacefully.\nReason (R): Democratic political systems provide legitimate constitutional mechanisms for negotiation, compromise, and power sharing among diverse community groups.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "While no society can completely eradicate conflict, democracies provide institutional forums for negotiation and power sharing, preventing violent social explosions.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-006",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Majority Community vs Majority Rule",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Rule by majority must not be converted into rule by a majority community based on religion, race, or language.\nReason (R): If rule by majority becomes majoritarian domination, democracy ceases to accommodate minorities and violates fundamental human equality.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Democratic majority rule means shifting political majorities on issues and elections; when it degenerates into permanent ethnic/religious majoritarianism, democratic accommodation collapses.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-007",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Public Dissatisfaction as Success",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Public complaints and constant criticism of the ruling regime are evidence of the success of democracy.\nReason (R): Widespread public dissatisfaction proves that citizens have developed critical awareness and actively expect power holders to deliver better governance.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Public critique testifies that democracy has successfully transformed subjects into vigilant citizens who understand their democratic rights and demand accountability.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Economic Equality vs Political Equality",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Political equality in democracies does not automatically lead to the elimination of economic inequality.\nReason (R): While every citizen receives one vote of equal value, wealth and productive resources remain unevenly concentrated in market economies.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Political equality (universal adult franchise) guarantees equal voting rights, but free market economic structures can simultaneously generate severe wealth disparities.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.3"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-009",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Dignity of Women in Democracy",
    "difficulty": "Board Standard",
    "question": "Assertion (A): In India and across global democracies, the passion for respect and freedom has provided legal strength to women's movements.\nReason (R): Once the moral and legal principle of gender equality is established in a constitution, discrimination loses its systemic legitimacy.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Constitutional enshrinement of gender equality provides a powerful legal lever that empowers women to fight discrimination through courts and civic movements.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Correcting Mistakes in Democracy",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Democracy offers better mechanisms for correcting policy blunders than non-democratic systems.\nReason (R): In a democracy, policies are subject to public debate, investigative media scrutiny, judicial review, and periodic electoral recall.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Because democracy is open and accountable, mistakes cannot remain concealed indefinitely; rulers must either reform bad policies or face electoral defeat.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-011",
    "type": "case_based",
    "subtopic": "Case Analysis: Decision-Making Procedures",
    "difficulty": "Board Standard",
    "question": "Consider a case where a municipal corporation passes an infrastructure blueprint without holding mandatory ward hearings or public disclosures. Which democratic outcome is being directly compromised?",
    "options": [
      "Transparency and procedural accountability",
      "National military sovereignty",
      "International monetary credit rating",
      "State boundary demarcation rights"
    ],
    "answer": 0,
    "explanation": "When decisions bypass consultation, publication, and established procedural norms, transparency and citizen oversight are directly subverted.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis: Sri Lanka vs Belgium Lesson",
    "difficulty": "Hard",
    "question": "In 1956, Sri Lanka made Sinhala the sole official language, disregarding Tamil speakers. In contrast, Belgium amended its constitution four times to ensure Dutch and French speakers shared power equally. What fundamental lesson does this offer regarding democratic outcomes?",
    "options": [
      "Democracy succeeds only when the majority works with minorities and refrains from majoritarian tyranny",
      "Democracy requires all nations to adopt multilingual currency notes",
      "Authoritarian military dictatorships handle linguistic diversity better than democracies",
      "Small nations should never conduct parliamentary elections"
    ],
    "answer": 0,
    "explanation": "Belgium accommodated diversity by sharing power; Sri Lanka imposed majoritarianism which provoked civil war. Democracy requires majorities to cooperate with minorities.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-013",
    "type": "case_based",
    "subtopic": "Case Analysis: RTI and Public Scrutiny",
    "difficulty": "Medium",
    "question": "An NGO in rural Rajasthan uses the Right to Information (RTI) Act to access muster rolls of drought relief works, uncovering ghost workers and siphoned wages. This real-world application illustrates how:",
    "options": [
      "Institutional transparency empowers citizens to enforce administrative accountability and fight corruption",
      "RTI laws cause government departments to shut down completely",
      "Citizens are legally forbidden from checking public expenditure records",
      "Drought relief projects should only be executed by foreign contractors"
    ],
    "answer": 0,
    "explanation": "The RTI movement in Rajasthan exemplifies how transparency mechanisms turn passive subjects into active citizens capable of auditing the state and curbing corruption.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Box Note on RTI"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-014",
    "type": "case_based",
    "subtopic": "Case Analysis: South Asian Popular Support",
    "difficulty": "Medium",
    "question": "Cross-national survey data reveals that over 70% of respondents in India, Nepal, and Bangladesh agree that 'democracy is suitable for our country', despite widespread poverty and governance flaws. What explains this persistent support?",
    "options": [
      "Democracy provides personal dignity, human rights, and the legitimacy of being governed by people's own chosen representatives",
      "Citizens in South Asia are legally penalized if they express support for other systems",
      "South Asian nations have completely eliminated all poverty and unemployment",
      "International aid agencies withhold food aid if citizens criticize democracy"
    ],
    "answer": 0,
    "explanation": "Democracy is valued because it is legitimate and belongs to the people; citizens cherish political dignity, self-determination, and the power of the vote.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Table on South Asian Perceptions"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-015",
    "type": "case_based",
    "subtopic": "Case Analysis: Economic Disparity in Latin America",
    "difficulty": "Hard",
    "question": "In a democratic South American republic, the top 10% own 70% of land and national income, while rural farmworkers earn below minimum wage. What does this reveal about democratic performance?",
    "options": [
      "While political democracy grants equal franchise, it does not automatically produce economic redistribution without strong progressive policy intervention",
      "Electoral democracy inevitably causes total agricultural collapse",
      "Land ownership is legally restricted to foreign multinational directors",
      "Elected presidents are constitutionally banned from collecting income taxes"
    ],
    "answer": 0,
    "explanation": "Democracy ensures political equality but does not automatically equalize wealth unless targeted redistribution policies and welfare programs are implemented.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.3"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-016",
    "type": "mcq",
    "subtopic": "Comparing Non-Democracies on Social Peace",
    "difficulty": "Medium",
    "question": "Why do dictatorial regimes often appear superficially calmer and less plagued by open strikes and ethnic disputes than democracies?",
    "options": [
      "Because authoritarian states forcibly suppress dissent, outlaw strikes, and censor media, giving an illusion of harmony while grievances fester underground",
      "Because all citizens in dictatorships share identical religious and cultural beliefs",
      "Because non-democratic governments provide free housing and cars to every citizen",
      "Because dictatorships abolish ethnic diversity by scientific genetic cloning"
    ],
    "answer": 0,
    "explanation": "Authoritarian regimes suppress dissent through police coercion, hiding conflicts under the surface; democracies allow conflicts to be expressed openly and resolved peacefully.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.4"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-017",
    "type": "mcq",
    "subtopic": "Citizen as Sovereign vs Subject",
    "difficulty": "Easy",
    "question": "What fundamental conceptual shift occurs when a nation transitions from an autocratic monarchy to a constitutional democracy?",
    "options": [
      "Inhabitants cease to be obedient 'subjects' of a king and become rights-bearing 'citizens' who hold sovereign political power",
      "All private commercial businesses are liquidated by parliament",
      "The national currency is abolished in favor of barter trading",
      "Courts are replaced by military martial law tribunals"
    ],
    "answer": 0,
    "explanation": "In a democracy, people are not subjects of a ruler; they are the rulers themselves and citizens possessing constitutional rights and ultimate sovereignty.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-018",
    "type": "mcq",
    "subtopic": "Evaluating Democracy's Endless Tests",
    "difficulty": "Hard",
    "question": "Why is the fact that 'democracy's examination never gets over' actually its greatest strength rather than a failure?",
    "options": [
      "It shows that citizens refuse to become complacent, continuously raising expectations and pushing governance towards higher standards of justice and equality",
      "It proves that constitutional laws are constantly invalidated by international treaties",
      "It ensures that prime ministers must write civil service exam papers every month",
      "It keeps election commission officials employed year-round"
    ],
    "answer": 0,
    "explanation": "Continuous citizen scrutiny and rising expectations indicate an alert, active polity that prevents democratic decay and constantly drives governance improvements.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.5"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-019",
    "type": "mcq",
    "subtopic": "Role of Independent Media in Democratic Outcomes",
    "difficulty": "Medium",
    "question": "In evaluating how democratic governments perform on responsiveness, what critical role does an independent, free press play?",
    "options": [
      "It acts as a public watchdog, exposing corruption, amplifying citizen grievances, and ensuring transparency",
      "It prints official government propaganda without verification",
      "It decides court verdicts in criminal cases",
      "It levies customs duties on imported paper"
    ],
    "answer": 0,
    "explanation": "A free and independent press investigates state actions, gives voice to public issues, and facilitates open debate, which is essential for government responsiveness.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Section 5.1"
  },
  {
    "id": "cbse10-sst-civ-ch17-s3-020",
    "type": "mcq",
    "subtopic": "Final Verdict on Democracy's Outcomes",
    "difficulty": "Board Standard",
    "question": "When balancing democracy's drawbacks (slowness, corruption, inequality) against its achievements, what is the definitive conclusion drawn by political scientists?",
    "options": [
      "Democracy is undeniably the best political system available because it derives its authority from the consent of the governed and protects individual dignity and freedom",
      "Military dictatorships should be adopted as the permanent global standard",
      "Monarchies are more progressive in protecting civil liberties",
      "Anarchy without government is the most efficient economic system"
    ],
    "answer": 0,
    "explanation": "Democracy is superior because it is legitimate, responsive in principle, capable of self-correction, accommodates diverse populations, and places human dignity and liberty at its core.",
    "citation": "NCERT Class 10 Civics, Chapter 5, Chapter Summary"
  }
]

# Write Chapter 17 Sets 1, 2, and 3
with open(os.path.join(DATA_DIR, "ch17_outcomes_of_democracy_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch17_set1}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch17_outcomes_of_democracy_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch17_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch17_outcomes_of_democracy_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch17_set3}, f, indent=2, ensure_ascii=False)

print("Generated Ch 17 (Outcomes of Democracy) Sets 1, 2, 3 (60 Qs total) successfully!")
