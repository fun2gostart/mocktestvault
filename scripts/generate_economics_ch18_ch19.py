#!/usr/bin/env python3
"""
Generates Economics Chapter 18 (Development) Sets 1, 2, 3
and Chapter 19 (Sectors of the Indian Economy) Sets 1, 2, 3.
Total: 6 sets = 120 questions.
100% NCERT and CBSE Class 10 Social Science Board grounded.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# =============================================================================
# CHAPTER 18: DEVELOPMENT (Economics Ch 1 / Total SST Ch 18)
# =============================================================================

# -----------------------------------------------------------------------------
# CH 18 SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch18_set1 = [
  {
    "id": "cbse10-sst-eco-ch18-s1-001",
    "type": "mcq",
    "subtopic": "Different People, Different Goals",
    "difficulty": "Easy",
    "question": "Which of the following statements best illustrates that 'different people can have different developmental goals'?",
    "options": [
      "A prosperous Punjab farmer seeks higher minimum support prices, while a landless rural labourer seeks more days of work and better daily wages",
      "All citizens in a country have mathematically identical aspirations for economic progress",
      "Industrialists and adivasi tribals always agree on building mega hydroelectric dams",
      "Urban unemployed youth seek identical developmental policies as rural subsistence farmers"
    ],
    "answer": 0,
    "explanation": "Different persons can have different developmental goals because their life situations differ. A prosperous farmer wants high support prices for crops and cheap labour, whereas a landless labourer wants more days of work, better wages, and quality local schooling for children.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.1"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-002",
    "type": "mcq",
    "subtopic": "Conflicting Developmental Goals",
    "difficulty": "Easy",
    "question": "What may be development for an industrialist who desires more electricity by constructing large dams may be destructive for:",
    "options": [
      "Local tribal communities and farmers whose lands and homes are submerged by the reservoir",
      "Multinational power transmission corporations",
      "Turbine and heavy electrical machinery manufacturers",
      "Urban factory owners seeking reliable electrical grid supplies"
    ],
    "answer": 0,
    "explanation": "To get more electricity, industrialists may want more dams. But this may submerge the land and disrupt the lives of people who are displaced — such as tribals. Thus, what may be development for one may not be development for the other; it may even be destructive for the other.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.1"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-003",
    "type": "mcq",
    "subtopic": "Income and Other Goals",
    "difficulty": "Easy",
    "question": "Besides seeking higher income, people also prioritize non-material goals such as:",
    "options": [
      "Equal treatment, freedom, security, and respect from others",
      "Unrestricted permission to violate traffic laws",
      "Exemption from paying municipal property taxes",
      "Hereditary titles of aristocratic nobility"
    ],
    "answer": 0,
    "explanation": "Besides seeking more income, one-way or another, people also seek things like equal treatment, freedom, security, and respect of others. They resent discrimination. All these are important non-material goals.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.2"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-004",
    "type": "mcq",
    "subtopic": "Average Income / Per Capita Income Calculation",
    "difficulty": "Easy",
    "question": "How is the 'Per Capita Income' (or Average Income) of a country calculated?",
    "options": [
      "Total national income divided by the total population of the country",
      "Total agricultural earnings multiplied by total industrial export volume",
      "Total foreign exchange reserves divided by annual gold imports",
      "Total tax collections divided by the number of registered companies"
    ],
    "answer": 0,
    "explanation": "The average income is also called per capita income. It is calculated by dividing the total national income of the country by its total population.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-005",
    "type": "mcq",
    "subtopic": "World Bank Classification Criteria",
    "difficulty": "Medium",
    "question": "Which criterion is primarily used by the World Bank in its World Development Reports to classify countries into rich and low-income categories?",
    "options": [
      "Per Capita Income (Average Income) measured in US Dollars",
      "Gross military expenditure per square kilometer",
      "Total annual production of crude petroleum",
      "Number of universities and technical engineering colleges"
    ],
    "answer": 0,
    "explanation": "In World Development Reports, brought out by the World Bank, per capita income criterion is used in classifying countries into rich countries and low-income countries.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-006",
    "type": "mcq",
    "subtopic": "Limitations of Average Income",
    "difficulty": "Medium",
    "question": "What is the most significant flaw or limitation of using average income alone to judge a country's development?",
    "options": [
      "It hides disparities and does not reveal how equitably or unequally income is distributed among the citizens",
      "It cannot be compared across different calendar years",
      "It completely excludes manufacturing and service sectors from calculation",
      "It fluctuates every hour based on international stock market indices"
    ],
    "answer": 0,
    "explanation": "While averages are useful for comparison, they also hide disparities. If a country has high average income but 90% of it is held by five citizens while the rest live in extreme poverty, the average gives a false impression of widespread well-being.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-007",
    "type": "mcq",
    "subtopic": "Infant Mortality Rate (IMR) Definition",
    "difficulty": "Easy",
    "question": "Infant Mortality Rate (IMR) indicates:",
    "options": [
      "The number of children that die before completing one year of age as a proportion of 1,000 live children born in that particular year",
      "The number of children born with severe malnutrition in rural hospitals",
      "The percentage of infants enrolled in primary preschool facilities",
      "The number of deaths among mothers during childbirth per 100,000 deliveries"
    ],
    "answer": 0,
    "explanation": "Infant Mortality Rate (or IMR) indicates the number of children that die before the age of one year as a proportion of 1,000 live children born in that particular year.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-008",
    "type": "mcq",
    "subtopic": "Literacy Rate Definition",
    "difficulty": "Easy",
    "question": "According to the Indian census and NCERT guidelines, 'Literacy Rate' measures the proportion of literate population in the age group of:",
    "options": [
      "7 years and above",
      "15 years and above",
      "21 years and above",
      "All individuals regardless of age from birth"
    ],
    "answer": 0,
    "explanation": "Literacy Rate measures the proportion of literate population in the 7-and-above age group.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-009",
    "type": "mcq",
    "subtopic": "Net Attendance Ratio Definition",
    "difficulty": "Medium",
    "question": "'Net Attendance Ratio' is defined as:",
    "options": [
      "The total number of children of age group 14 and 15 years attending school as a percentage of total number of children in the same age group",
      "The total number of teachers attending morning school assembly every day",
      "The proportion of college students who clear annual university examinations",
      "The percentage of school children who receive free midday meals"
    ],
    "answer": 0,
    "explanation": "Net Attendance Ratio is the total number of children of age group 14 and 15 years attending school as a percentage of total number of children in the same age group.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-010",
    "type": "mcq",
    "subtopic": "Kerala vs Haryana Comparison",
    "difficulty": "Board Standard",
    "question": "Even though Haryana has a higher per capita income than Kerala, Kerala has a much lower Infant Mortality Rate and higher literacy. What explains this outcome?",
    "options": [
      "Kerala has an adequate provision of basic health and educational facilities and an effective Public Distribution System (PDS)",
      "Kerala receives direct monetary subsidies from the World Bank for every citizen",
      "Haryana completely lacks roads and electricity networks",
      "Kerala citizens are exempted from paying income taxes by the central government"
    ],
    "answer": 0,
    "explanation": "Kerala has a low Infant Mortality Rate because it has adequate provision of basic health and educational facilities. Furthermore, in states like Kerala, the Public Distribution System (PDS) functions well, ensuring health and nutritional status of people.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-011",
    "type": "mcq",
    "subtopic": "Public Facilities Concept",
    "difficulty": "Easy",
    "question": "Why is income alone not a completely adequate indicator of material goods and services that citizens are able to use?",
    "options": [
      "Because money cannot buy a pollution-free environment or ensure protection from infectious diseases unless community preventative steps are taken",
      "Because paper currency loses its legal value every forty-eight hours",
      "Because private commercial banks refuse to accept cash deposits from workers",
      "Because foreign currencies are legally banned in domestic retail markets"
    ],
    "answer": 0,
    "explanation": "Money cannot buy you a pollution-free environment or ensure that you get unadulterated medicines, unless you can afford to shift to a community that already has all these things. Money may also not be able to protect you from infectious diseases, unless the whole community takes preventive steps.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-012",
    "type": "mcq",
    "subtopic": "UNDP Human Development Report (HDR)",
    "difficulty": "Medium",
    "question": "Which United Nations agency publishes the Human Development Report (HDR) comparing nations on education, health, and per capita income?",
    "options": [
      "UNDP (United Nations Development Programme)",
      "UNESCO (United Nations Educational, Scientific and Cultural Organization)",
      "UNICEF (United Nations Children's Fund)",
      "UNCTAD (United Nations Conference on Trade and Development)"
    ],
    "answer": 0,
    "explanation": "The Human Development Report published by UNDP (United Nations Development Programme) compares countries based on the educational levels of the people, their health status and per capita income.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-013",
    "type": "mcq",
    "subtopic": "Life Expectancy at Birth",
    "difficulty": "Easy",
    "question": "'Life Expectancy at Birth' denotes:",
    "options": [
      "The average expected length of life of a person at the time of birth based on prevailing mortality rates",
      "The maximum age reached by the oldest citizen in a nation",
      "The average retirement age of government civil servants",
      "The number of years an individual spends in formal university education"
    ],
    "answer": 0,
    "explanation": "Life Expectancy at birth denotes, as the name suggests, average expected length of life of a person at the time of birth.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-014",
    "type": "mcq",
    "subtopic": "Body Mass Index (BMI) Formula",
    "difficulty": "Medium",
    "question": "Nutritionists calculate Body Mass Index (BMI) to determine adult nutritional health using which standard formula?",
    "options": [
      "Weight in kilograms divided by the square of height in meters (kg/m²)",
      "Height in centimeters multiplied by total daily caloric intake",
      "Weight in pounds divided by annual income in rupees",
      "Waist circumference divided by blood pressure systolic reading"
    ],
    "answer": 0,
    "explanation": "To calculate BMI: take the weight of the person in kg; then take the height in metres; divide the weight in kg by the square of the height. BMI = weight(kg) / [height(m)]².",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4 (Activity 3)"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-015",
    "type": "mcq",
    "subtopic": "BMI Classification Standard",
    "difficulty": "Hard",
    "question": "According to international health standards cited in the NCERT curriculum, an adult with a BMI less than 18.5 is categorized as:",
    "options": [
      "Undernourished",
      "Overweight",
      "Severely obese",
      "Normal and optimal"
    ],
    "answer": 0,
    "explanation": "If the BMI is less than 18.5, then the person is considered undernourished. If this BMI is more than 25, then a person is considered overweight.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4 (Activity 3)"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-016",
    "type": "mcq",
    "subtopic": "Renewable Resource Overuse: Groundwater",
    "difficulty": "Medium",
    "question": "Groundwater is a renewable resource replenished by annual rainfall. Why is it facing a severe crisis in Punjab, Western UP, and hard-rock plateau areas of Central India?",
    "options": [
      "Because the rate of extraction for tube-well irrigation far exceeds natural rainwater replenishment",
      "Because underground rocks absorb all water into the Earth's molten core",
      "Because river waters are being exported to European nations",
      "Because monsoon rainfall has permanently ceased across Asia"
    ],
    "answer": 0,
    "explanation": "If we use more than what is being replenished by rain, then we are overusing this resource. Nearly one-third of the country is overusing their groundwater reserves due to excessive submersible pump extraction for intensive agriculture.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-017",
    "type": "mcq",
    "subtopic": "Non-Renewable Resource Definition",
    "difficulty": "Easy",
    "question": "Crude petroleum and mineral ores are categorized as 'non-renewable resources' because:",
    "options": [
      "They have a fixed stock on Earth and cannot be replenished once exhausted by continuous extraction",
      "They are generated by solar panels within a matter of days",
      "They can only be used by government-owned public corporations",
      "They multiply naturally in underground limestone caverns"
    ],
    "answer": 0,
    "explanation": "Non-renewable resources are those which will get exhausted after years of use. We have a fixed stock on earth which cannot be replenished. We do discover new resources that we did not know of earlier, but over time, even this will get exhausted.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-018",
    "type": "mcq",
    "subtopic": "Sustainable Development Definition",
    "difficulty": "Easy",
    "question": "'Sustainable Development' is defined as development that:",
    "options": [
      "Meets the needs of the present generation without compromising the ability of future generations to meet their own needs",
      "Maximizes immediate industrial exploitation of all forests within five years",
      "Bans all agricultural farming and livestock rearing permanently",
      "Restricts the use of electricity strictly to government ministries"
    ],
    "answer": 0,
    "explanation": "Sustainable development ensures that development takes place without damaging the environment and that the needs of the present are met without compromising the ability of future generations to meet their own needs.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-019",
    "type": "mcq",
    "subtopic": "Sri Lanka vs India HDI Comparison",
    "difficulty": "Medium",
    "question": "In the UNDP Human Development Report, what remarkable fact stands out when comparing India with its small southern island neighbour, Sri Lanka?",
    "options": [
      "Sri Lanka is well ahead of India in HDI ranking, life expectancy at birth, and mean years of schooling despite having a smaller economy",
      "India has ten times higher life expectancy than Sri Lanka",
      "Sri Lanka has zero adult literacy across all districts",
      "India has lower infant mortality than any Scandinavian country"
    ],
    "answer": 0,
    "explanation": "Isn't it surprising that a small country in our neighbourhood, Sri Lanka, is much ahead of India in every respect and has a far higher rank in the world in the Human Development Report? Sri Lanka has higher life expectancy and literacy.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4, Table 1.6"
  },
  {
    "id": "cbse10-sst-eco-ch18-s1-020",
    "type": "mcq",
    "subtopic": "Core Lesson on Development",
    "difficulty": "Medium",
    "question": "What is the ultimate lesson of the Human Development Index regarding what is truly important in national development?",
    "options": [
      "What is happening to citizens — their health, education, nutrition, and well-being — matters far more than mere accumulation of material wealth or national GDP",
      "The size of a nation's naval fleet is the sole measure of human progress",
      "Only countries with private corporate monopolies can achieve high literacy",
      "Welfare spending on public healthcare reduces national economic strength"
    ],
    "answer": 0,
    "explanation": "By pre-fixing Human to Development, HDR has made it crystal clear that what is important in development is what is happening to citizens of a country. It is people, their health, their well-being, that is most important.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  }
]

# -----------------------------------------------------------------------------
# CH 18 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch18_set2 = [
  {
    "id": "cbse10-sst-eco-ch18-s2-001",
    "type": "mcq",
    "subtopic": "Conflicting Interests: Flyover Construction",
    "difficulty": "Medium",
    "question": "A metropolitan city plans a high-speed elevated highway corridor. This project benefits private car owners by cutting commute times, but destroys the shops and livelihoods of roadside vendors and small shopkeepers. This scenario demonstrates:",
    "options": [
      "Developmental goals can be mutually conflicting; what represents development for one section can cause economic displacement for another",
      "Elevated expressways eliminate poverty for all citizens automatically",
      "Roadside vendors should be barred from using judicial courts",
      "Urban planning is legally exempted from constitutional review"
    ],
    "answer": 0,
    "explanation": "People have conflicting developmental goals. An urban commuter benefits from elevated flyovers, but small roadside vendors lose their shops and livelihoods when land is acquired, creating conflict between different social groups.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.1"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-002",
    "type": "mcq",
    "subtopic": "Job Selection Factors Beyond Salary",
    "difficulty": "Medium",
    "question": "A young engineer is offered two jobs: Job A offers very high pay but no job security and long erratic hours leaving no time for family; Job B offers slightly lower pay but regular hours, permanent job security, and health insurance for family. If she chooses Job B, it proves that:",
    "options": [
      "People look at a mix of goals including job security, working environment, and work-life balance, not just monetary salary alone",
      "High salaries are legally prohibited in private software corporations",
      "Engineers are irrational economic decision makers",
      "Job security is irrelevant to modern professionals"
    ],
    "answer": 0,
    "explanation": "If women or men are engaged in paid work, their dignity increases. But people look at a mix of goals: working environment, opportunity to learn, sense of security, and freedom are as critical as monetary salary.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.2"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-003",
    "type": "mcq",
    "subtopic": "Country Comparison: Equal vs Unequal Incomes",
    "difficulty": "Hard",
    "question": "Consider two countries X and Y with 5 citizens each, both having an average income of ₹10,000. In Country X, individual incomes are ₹9,500, ₹10,500, ₹9,800, ₹10,000, and ₹10,200. In Country Y, incomes are ₹500, ₹500, ₹500, ₹500, and ₹48,000. Which country would an equitable citizen prefer to live in?",
    "options": [
      "Country X, because income is equitably distributed with neither extreme riches nor abject poverty",
      "Country Y, because it has one ultra-wealthy billionaire who can buy luxury yachts",
      "Country Y, because 80% of citizens are guaranteed to remain poor",
      "Both countries are identical in every social and human dimension"
    ],
    "answer": 0,
    "explanation": "Even though both countries have the same average income (₹10,000), Country X is preferred because income is equitably distributed. In Country Y, four citizens are destitute while one person monopolizes nearly all wealth.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3, Table 1.2"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-004",
    "type": "mcq",
    "subtopic": "Purchasing Power Parity (PPP)",
    "difficulty": "Hard",
    "question": "Why does the World Bank and UNDP calculate per capita income in 'Purchasing Power Parity (PPP) Dollars' rather than nominal exchange rates?",
    "options": [
      "Because one dollar must be able to purchase the same quantity of goods and services in any country, eliminating currency price distortions",
      "Because nominal dollars are legally invalid in developing Asian countries",
      "Because the United Nations only accepts gold coins for calculations",
      "Because PPP dollars automatically double the national income of rich nations"
    ],
    "answer": 0,
    "explanation": "Per capita income is calculated in international dollars (PPP) so that one dollar buys the same basket of goods and services in any country, providing a fair standard of comparison.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4 (Footnote on PPP)"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-005",
    "type": "mcq",
    "subtopic": "Bihar's Educational Lag",
    "difficulty": "Medium",
    "question": "According to official data in NCERT Table 1.4, nearly half of children aged 14–15 in Bihar are not attending school beyond Class 8. What does this imply for Bihar's human development?",
    "options": [
      "A significant demographic proportion is deprived of secondary education, severely limiting future skilled employment opportunities and state development",
      "Bihar has achieved universal literacy in technical university degrees",
      "Children in Bihar are legally barred from entering secondary schools",
      "Bihar requires all teenagers to serve in the state police brigade"
    ],
    "answer": 0,
    "explanation": "In Bihar, around half of the children aged 14-15 are not attending school beyond Class 8. This means that if you went to school in Bihar, nearly half of your elementary cohort would be missing, indicating serious underdevelopment of human capital.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-006",
    "type": "mcq",
    "subtopic": "PDS Functioning and Nutrition",
    "difficulty": "Medium",
    "question": "In states like Tamil Nadu and Kerala, where the Public Distribution System (PDS) functions efficiently, surveys show that:",
    "options": [
      "The health and nutritional status of the rural poor is significantly better than in states with dysfunctional PDS",
      "Food grains in fair price shops remain unsold and rot in warehouses",
      "Agricultural farmers refuse to cultivate paddy crops",
      "The poverty rate rises by 50% every year"
    ],
    "answer": 0,
    "explanation": "In some states, the PDS functions well. In these states, the health and nutritional status of people is certainly likely to be better because cheap, subsidized food grains are regularly available to low-income families.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-007",
    "type": "mcq",
    "subtopic": "BMI Calculation Numerical Application",
    "difficulty": "Hard",
    "question": "A 25-year-old adult weighs 50 kg and is 1.60 meters tall. What is the individual's BMI, and what does it indicate about their nutritional status? (1.60² = 2.56)",
    "options": [
      "BMI ≈ 19.53 kg/m²; the individual falls in the normal, healthy nutritional range",
      "BMI ≈ 15.20 kg/m²; the individual is severely undernourished",
      "BMI ≈ 31.25 kg/m²; the individual is clinically obese",
      "BMI ≈ 10.50 kg/m²; the individual requires immediate medical hospitalization"
    ],
    "answer": 0,
    "explanation": "BMI = Weight / (Height)² = 50 / (1.60 × 1.60) = 50 / 2.56 ≈ 19.53. Since 19.53 is between 18.5 and 25, the person is within the normal and healthy nutritional range.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4 (Activity 3)"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-008",
    "type": "mcq",
    "subtopic": "Depletion of Crude Oil Reserves",
    "difficulty": "Medium",
    "question": "According to World Energy Review data cited in NCERT, global crude oil reserves are estimated to last roughly 50 years at current extraction rates. What serious developmental implication arises?",
    "options": [
      "Countries like India, which import over 80% of their crude oil, face severe economic vulnerability unless renewable energy alternatives are rapidly developed",
      "Crude oil prices will drop to zero permanently",
      "Internal combustion engines will run on sea water automatically",
      "Automobile transportation will be permanently banned globally by 2030"
    ],
    "answer": 0,
    "explanation": "India depends on importing oil from abroad because it does not have enough stocks of its own. If oil prices increase this becomes a burden for everyone. Moreover, non-renewable energy exhaustion threatens long-term sustainable development.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5, Table 1.7"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-009",
    "type": "mcq",
    "subtopic": "Collective Provision of Public Goods",
    "difficulty": "Medium",
    "question": "Why is collective provision of public services (e.g., municipal security, government schools) economically more sensible than individual private provision?",
    "options": [
      "It is vastly cheaper and more effective to provide community services collectively than for every individual house to hire private guards or set up private generators",
      "Private individuals are legally forbidden from purchasing private solar panels",
      "Collective provision guarantees that no public funds will ever be spent",
      "Private companies refuse to sell security alarms to homeowners"
    ],
    "answer": 0,
    "explanation": "Actually for many of the important things in life the best way, also the cheapest way, is to provide these goods and services collectively. Just think — will it be cheaper to have collective security for the whole locality or for each house to have its own security man?",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-010",
    "type": "mcq",
    "subtopic": "Gender Disparity in Rural Nutrition",
    "difficulty": "Medium",
    "question": "Surveys in rural India often reveal that women and young girls have significantly higher rates of low BMI (< 18.5) than men. What underlying socio-economic factor causes this?",
    "options": [
      "Intra-household nutritional discrimination where women eat last and least after serving other family members",
      "Genetic inability of rural women to digest food grains",
      "Government laws mandating that women fast five days a week",
      "Higher physical metabolism of women compared to male field labourers"
    ],
    "answer": 0,
    "explanation": "Sociological and economic surveys indicate that gender bias in intra-household food distribution, where women eat after male members and receive smaller shares of nutritious food, leads to higher female undernourishment.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4 (Activity 3 Analysis)"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-011",
    "type": "mcq",
    "subtopic": "Middle East Oil Wealth vs Human Development",
    "difficulty": "Hard",
    "question": "Why are several oil-rich Middle Eastern nations excluded from the category of 'developed countries' despite having extremely high per capita incomes?",
    "options": [
      "Because high income is derived almost entirely from oil rents rather than diversified human capabilities, and educational/gender development lags behind",
      "Because they refuse to use US dollars in petroleum trade",
      "Because their total geographical land area is less than 500 square kilometers",
      "Because the United Nations disallows monarchies from receiving developed status"
    ],
    "answer": 0,
    "explanation": "Countries with per capita income above the rich country threshold, excluding countries of Middle East and certain other small countries, are generally called developed countries because high development requires equitable social, educational, and political freedoms alongside wealth.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-012",
    "type": "mcq",
    "subtopic": "Environmental Degradation and National Boundaries",
    "difficulty": "Board Standard",
    "question": "'Consequences of environmental degradation do not respect national or state boundaries.' Which real-world example best validates this principle?",
    "options": [
      "Air pollution from stubble burning or greenhouse gas emissions warming global oceans affects neighbouring states and entire continents regardless of borders",
      "Municipal water taxes collected in Delhi are transferred to Sri Lanka",
      "Earthquake shocks only travel through countries that have signed the Paris Climate Accord",
      "Acid rain only falls on privately owned industrial factories"
    ],
    "answer": 0,
    "explanation": "Our future is linked together. Sustainability of development is a new area of knowledge in which scientists, economists, philosophers and other social scientists are working together because environmental crises (climate change, air pollution, ozone depletion) transcend political boundaries.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-013",
    "type": "mcq",
    "subtopic": "Girl Child Education in Rural India",
    "difficulty": "Medium",
    "question": "In many rural districts of Uttar Pradesh and Madhya Pradesh, girls drop out after Class 5 because:",
    "options": [
      "Government has not provided adequate secondary schools or safe transport nearby, and society does not yet value female schooling equally",
      "Girls are legally disqualified from learning arithmetic and science",
      "Secondary school teachers refuse to teach female students",
      "School textbooks are written exclusively in foreign languages"
    ],
    "answer": 0,
    "explanation": "Many girls are not able to achieve secondary level schooling because government/society has not provided adequate facilities. Where local schools and public transport are established, female enrolment rises dramatically.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-014",
    "type": "mcq",
    "subtopic": "Comparing Haryana and Kerala Health Metrics",
    "difficulty": "Hard",
    "question": "Haryana had a per capita income of ₹1,80,174 compared to Kerala's ₹1,63,476 (2016-17 data), but Kerala's IMR was only 10 per 1,000 live births compared to Haryana's 30. What does this contrast teach us?",
    "options": [
      "Higher personal income does not guarantee superior public health or child survival unless the state invests systematically in primary healthcare infrastructure",
      "Haryana residents prefer not to take sick infants to hospitals",
      "Per capita income in Kerala is completely inaccurate and fabricated",
      "Infant mortality has no relationship to medical infrastructure or nursing care"
    ],
    "answer": 0,
    "explanation": "Even though Haryana is wealthier in terms of average per capita income, an infant born in Haryana is three times more likely to die before age one than in Kerala, proving that public health infrastructure and social development are independent of mere income.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4, Tables 1.3 & 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-015",
    "type": "mcq",
    "subtopic": "National Development Definition",
    "difficulty": "Easy",
    "question": "'National Development' encompasses which of the following comprehensive objectives?",
    "options": [
      "Improving the living standards of citizens, providing food security, healthcare, education, and reducing social and economic inequalities",
      "Constructing the largest presidential palace in the world",
      "Doubling the national debt by purchasing foreign luxury automobiles",
      "Banning all foreign books and newspapers from public libraries"
    ],
    "answer": 0,
    "explanation": "National development means thinking about fair and just paths for all, whether there is a better way of doing things, and ensuring that development benefits the largest number of people equitably.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-016",
    "type": "mcq",
    "subtopic": "Human Development Index Components",
    "difficulty": "Medium",
    "question": "Which three dimensions are aggregated to calculate the Human Development Index (HDI)?",
    "options": [
      "Decent standard of living (GNI per capita), knowledge (mean and expected years of schooling), and long and healthy life (life expectancy)",
      "Military size, national gold reserves, and total highway kilometres",
      "Annual steel production, number of airports, and coal consumption",
      "Population density, agricultural land acreage, and foreign exchange reserves"
    ],
    "answer": 0,
    "explanation": "HDI is a composite index measuring average achievement in three basic dimensions of human development: a long and healthy life, knowledge, and a decent standard of living.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-017",
    "type": "mcq",
    "subtopic": "Groundwater Overuse in Agricultural States",
    "difficulty": "Medium",
    "question": "Which regions in India are experiencing the most critical depletion of underground water tables?",
    "options": [
      "Agriculturally prosperous regions of Punjab, Haryana, and Western Uttar Pradesh, and hard-rock plateau areas of central and southern India",
      "The Thar desert sand dunes of Western Rajasthan",
      "The glaciated mountain peaks of Ladakh",
      "The mangrove swamps of the Sundarbans in West Bengal"
    ],
    "answer": 0,
    "explanation": "Groundwater overuse is particularly found in the agriculturally prosperous regions of Punjab and Western U.P., hard rock plateau areas of central and south India, some coastal areas and rapidly growing urban settlements.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-018",
    "type": "mcq",
    "subtopic": "Renewable vs Non-Renewable Sustainability",
    "difficulty": "Board Standard",
    "question": "Why is the exploitation of non-renewable fossil fuels inherently incompatible with indefinite economic growth?",
    "options": [
      "Because fossil fuel reserves are finite and their combustion generates severe carbon emissions driving climate change and ecological collapse",
      "Because petroleum turns into gold after fifty years of underground storage",
      "Because foreign governments can confiscate underground oil reserves remotely",
      "Because fossil fuels cannot be transported through steel pipelines"
    ],
    "answer": 0,
    "explanation": "Fossil fuels are finite; once consumed, they cannot be regenerated on a human timescale, and their excessive usage causes atmospheric pollution and global warming, undermining sustainable development.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-019",
    "type": "mcq",
    "subtopic": "Poverty Line Determination Concept",
    "difficulty": "Medium",
    "question": "When assessing whether an individual is living below the poverty line, economists consider not just monetary income but also:",
    "options": [
      "Daily minimum nutritional caloric intake (2,400 calories in rural and 2,100 calories in urban areas) and access to essential clothing, shelter, and healthcare",
      "Whether the individual owns a four-bedroom luxury penthouse",
      "How many international vacation flights the person takes each year",
      "The number of designer wristwatches in the household"
    ],
    "answer": 0,
    "explanation": "Poverty measurement in India combines minimum income levels with basic nutritional calorie benchmarks (2,400 cal rural, 2,100 cal urban) and essential physical provisions necessary for survival.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s2-020",
    "type": "mcq",
    "subtopic": "Summary Insight: Development as Capability",
    "difficulty": "Board Standard",
    "question": "Nobel laureate Amartya Sen's approach to development, reflected in NCERT Economics, defines development fundamentally as:",
    "options": [
      "The expansion of human freedoms and capabilities to lead lives people have reason to value",
      "The accumulation of high monetary foreign exchange balances in central banks",
      "Maximizing industrial smokestacks and factory output at any environmental cost",
      "Eliminating all political debate in favor of technocratic decrees"
    ],
    "answer": 0,
    "explanation": "Development is fundamentally about expanding human capabilities — literacy, good health, freedom from avoidable disease, and social empowerment — enabling people to lead dignified, fulfilling lives.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  }
]

# -----------------------------------------------------------------------------
# CH 18 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch18_set3 = [
  {
    "id": "cbse10-sst-eco-ch18-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Per Capita Income Limitations",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Per Capita Income is not a comprehensive indicator of human development.\nReason (R): Per Capita Income measures only average monetary income and fails to capture disparities in distribution, healthcare, or educational attainment.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Per capita income hides income disparities and completely ignores non-material essentials like health, literacy, longevity, and environmental quality.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Kerala's Human Development",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Kerala has a remarkably low Infant Mortality Rate compared to Haryana despite having a lower per capita income.\nReason (R): Kerala has invested heavily in public healthcare, primary education, female literacy, and maintains a highly effective Public Distribution System (PDS).",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Kerala's health indicators demonstrate that equitable public provisioning of health clinics, schools, and food rations directly reduces infant mortality.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Groundwater Depletion",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Groundwater in northwest India is threatened with severe exhaustion.\nReason (R): Intensive green revolution agriculture relies heavily on tubewell extraction that exceeds natural annual rainfall replenishment.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Groundwater is renewable, but when extraction rates exceed replenishment rates, water tables drop drastically, threatening future agricultural sustainability.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Money Cannot Buy All Goods",
    "difficulty": "Board Standard",
    "question": "Assertion (A): High personal income alone cannot ensure a healthy and secure lifestyle.\nReason (R): Market purchasing power cannot buy an unpolluted atmosphere, freedom from infectious epidemics, or community peace.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Money in your pocket cannot buy a pollution-free environment or protect you from infectious diseases unless community preventive measures are taken.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Conflicting Developmental Goals",
    "difficulty": "Board Standard",
    "question": "Assertion (A): A developmental project can represent progress for one community while proving destructive for another.\nReason (R): Different social groups occupy different socioeconomic positions and have contradictory material interests.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Building a dam provides electricity to industrialists but submerges adivasi farmland, displacing their families and destroying their livelihoods.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.1"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-006",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Sustainable Development Imperative",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Modern economic growth must transition towards renewable energy and resource conservation.\nReason (R): Non-renewable resources like crude petroleum are finite and continuing current consumption will deplete global reserves within decades.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Crude oil is a non-renewable resource with fixed global stock; sustainable development demands transitioning to clean renewables to prevent economic collapse.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-007",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Public Facilities Efficiency",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Collective provision of public goods is economically more efficient than individual private arrangements.\nReason (R): Providing common security, mass public transport, or public sanitation for a community lowers per capita costs and ensures universal access.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Collective public provision harnesses economies of scale and guarantees that essential survival goods are not denied to poorer citizens.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Sri Lanka's HDI Superiority",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Sri Lanka ranks higher on the UNDP Human Development Index than India.\nReason (R): Sri Lanka has achieved higher life expectancy at birth, higher mean years of schooling, and a lower infant mortality rate.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Sri Lanka's long-term historical investments in universal free education and primary healthcare give it higher human development indices than India.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4, Table 1.6"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-009",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Literacy and Economic Productivity",
    "difficulty": "Board Standard",
    "question": "Assertion (A): A state with high literacy and secondary school attendance achieves higher long-term economic productivity.\nReason (R): Education enhances human capabilities, cognitive skills, technological adaptability, and earning potential.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Investment in human capital (schooling and skills) transforms an untrained population into a productive, innovative workforce.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Environmental Externalities",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Environmental degradation caused by industrial pollution is no longer a localized issue.\nReason (R): Ecological damage crosses administrative and international boundaries, threatening the collective sustainability of all human societies.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Environmental externalities like carbon emissions, acid rain, and ozone depletion affect the entire biosphere regardless of which country generated them.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-011",
    "type": "case_based",
    "subtopic": "Case Analysis: Narmada Dam Protests",
    "difficulty": "Board Standard",
    "question": "During the construction of the Sardar Sarovar Dam on the Narmada River, thousands of adivasis protested under the Narmada Bachao Andolan. Which economic reality does this event encapsulate?",
    "options": [
      "What is considered development by urban industrialists and electricity planners can be completely destructive for indigenous populations facing displacement",
      "Adivasis were protesting because they wanted to build a larger nuclear power plant",
      "The dam was built entirely to export water to foreign nations",
      "Hydroelectric power cannot generate electricity in developing nations"
    ],
    "answer": 0,
    "explanation": "The Narmada protests highlighted conflicting developmental goals: the state and industries wanted water and power, while local farmers and tribals faced involuntary displacement and loss of ancestral land.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.1"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis: Toxic Waste Dumping in Ivory Coast",
    "difficulty": "Hard",
    "question": "In 2006, a multinational company contracted a local firm to dump 500 tonnes of liquid toxic waste across open dumps in Abidjan (Ivory Coast), causing deaths and thousands of hospitalizations. This tragic case highlights:",
    "options": [
      "How commercial profit-seeking without stringent environmental regulation leads to devastating developmental exploitation of poor regions",
      "That toxic industrial waste improves agricultural crop yields",
      "That African countries have no judicial court systems",
      "That chemical waste disposal is legally exempt from international oversight"
    ],
    "answer": 0,
    "explanation": "The Abidjan toxic dumping incident (highlighted in NCERT Chapter 1) shows how unbridled commercial pursuit of cheap disposal at the expense of human safety devastates communities in developing regions.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Case Study Box on Abidjan"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-013",
    "type": "case_based",
    "subtopic": "Case Analysis: Tubewell Crisis in Punjab",
    "difficulty": "Board Standard",
    "question": "A farmer in Sangrur (Punjab) has had to deepen his submersible tubewell bore from 100 feet to 350 feet over the last twenty years due to dropping water tables. What economic concept does this illustrate?",
    "options": [
      "Overexploitation of a renewable natural resource leading to depletion when extraction exceeds natural replenishment",
      "Horizontal distribution of power among panchayat members",
      "Disguised unemployment in heavy steel manufacturing",
      "Terms of credit dictated by the Reserve Bank of India"
    ],
    "answer": 0,
    "explanation": "Boring deeper for water demonstrates falling water tables caused by pumping out water faster than annual rainfall can recharge the aquifer, threatening agricultural sustainability.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-014",
    "type": "case_based",
    "subtopic": "Case Analysis: Gender Nutrition Gap",
    "difficulty": "Medium",
    "question": "In a village survey, 35% of adult men and 46% of adult women were found to have a BMI below 18.5. What does this statistical disparity indicate about the community's development?",
    "options": [
      "Widespread undernutrition with pronounced gender inequality in intra-household food consumption and healthcare",
      "Men require fewer calories than women for physical farm labour",
      "Women in the village are choosing to follow Western fashion diet fads",
      "The village has completely eliminated all economic poverty"
    ],
    "answer": 0,
    "explanation": "A higher female undernourishment rate (BMI < 18.5) reflects gender-based disparities where girls and women receive poorer nutrition, validating the need for gender-sensitive development indicators.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-015",
    "type": "case_based",
    "subtopic": "Case Analysis: Haryana vs Kerala IMR",
    "difficulty": "Board Standard",
    "question": "A public health researcher notes that despite Haryana having a substantially higher per capita income than Kerala, out of 1,000 live births, 30 infants die before age one in Haryana compared to only 10 in Kerala. The researcher rightly concludes:",
    "options": [
      "Child survival depends critically on accessible public maternity clinics, universal immunization, and clean drinking water, which income alone cannot purchase",
      "Haryana infants have lower biological immunity than Kerala infants",
      "Hospitals in Haryana refuse to treat male children",
      "Kerala has five times higher income tax rates than Haryana"
    ],
    "answer": 0,
    "explanation": "Low infant mortality in Kerala is the direct result of comprehensive public health infrastructure, trained mid-wives, primary health centres, and high female literacy.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-016",
    "type": "mcq",
    "subtopic": "World Bank Threshold Categories",
    "difficulty": "Hard",
    "question": "According to the World Bank classification standard in World Development Reports, countries with per capita income above a certain benchmark are classified as 'high income' and those below a lower threshold as 'low-income'. What does this monetary classification overlook?",
    "options": [
      "Health, life expectancy, educational attainment, civil liberties, and equity of wealth distribution",
      "Total agricultural acreage under rice cultivation",
      "The number of commercial airports in the country",
      "The quantity of cement consumed in national highway construction"
    ],
    "answer": 0,
    "explanation": "The World Bank's per capita income metric completely overlooks non-income dimensions such as literacy, life expectancy, gender parity, and environmental sustainability.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.3"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-017",
    "type": "mcq",
    "subtopic": "Activity: Schooling Years in HDI",
    "difficulty": "Medium",
    "question": "In calculating HDI, UNDP uses two educational metrics: Mean Years of Schooling and Expected Years of Schooling. 'Mean Years of Schooling' measures:",
    "options": [
      "The average number of years of education received by people aged 25 and older in their lifetime",
      "The total number of hours children spend doing homework every day",
      "The percentage of teachers with doctorate degrees in universities",
      "The number of days schools remain closed for summer vacation"
    ],
    "answer": 0,
    "explanation": "Mean Years of Schooling estimates the average number of years of education completed by adults aged 25 years and older.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.4 (Technical Notes)"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-018",
    "type": "mcq",
    "subtopic": "Crude Oil Geopolitics and Indian Economy",
    "difficulty": "Medium",
    "question": "India imports roughly 85% of its crude oil requirements. If international oil prices double due to geopolitical conflict, how does this impact the Indian economy?",
    "options": [
      "Import bills surge, driving domestic inflation in transport and food, widening trade deficits and straining state budgets",
      "India's agricultural production automatically triples within one month",
      "The Indian Rupee becomes the strongest currency in the world",
      "Domestic railway fares drop by 50% immediately"
    ],
    "answer": 0,
    "explanation": "Because oil is imported, price shocks in global oil markets inflate transportation and electricity costs, raising prices across the entire domestic supply chain.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-019",
    "type": "mcq",
    "subtopic": "Sustainable Resource Management Strategy",
    "difficulty": "Board Standard",
    "question": "Which of the following national policy approaches aligns best with the principles of sustainable development?",
    "options": [
      "Investing aggressively in solar, wind, and green hydrogen power while enforcing rainwater harvesting and water recycling mandates",
      "Subsidizing free diesel fuel for heavy commercial trucks indefinitely",
      "Draining all natural freshwater wetlands to build shopping complexes",
      "Abolishing all environmental pollution control boards"
    ],
    "answer": 0,
    "explanation": "Sustainable development requires decoupling economic growth from environmental degradation through renewable clean energy, water conservation, and resource efficiency.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Section 1.5"
  },
  {
    "id": "cbse10-sst-eco-ch18-s3-020",
    "type": "mcq",
    "subtopic": "Synthesis: Multidimensional Nature of Development",
    "difficulty": "Board Standard",
    "question": "Which of the following statements provides the most comprehensive and accurate definition of modern development?",
    "options": [
      "Development is a multidimensional process that combines sustained income growth with equitable distribution, human capability expansion, social justice, and environmental sustainability",
      "Development is exclusively the percentage growth rate of a nation's Gross Domestic Product",
      "Development is achieved once a country builds fifty skyscrapers in its capital city",
      "Development means eliminating all public welfare schemes to lower government spending"
    ],
    "answer": 0,
    "explanation": "True development goes beyond income to incorporate equity, education, healthcare, civil liberties, and ecological sustainability for present and future generations.",
    "citation": "NCERT Class 10 Economics, Chapter 1, Chapter Review"
  }
]

# =============================================================================
# CHAPTER 19: SECTORS OF THE INDIAN ECONOMY (Economics Ch 2 / Total SST Ch 19)
# =============================================================================

# -----------------------------------------------------------------------------
# CH 19 SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch19_set1 = [
  {
    "id": "cbse10-sst-eco-ch19-s1-001",
    "type": "mcq",
    "subtopic": "Primary Sector Definition",
    "difficulty": "Easy",
    "question": "Economic activities that involve exploiting natural resources directly (such as agriculture, dairy, fishing, and forestry) belong to the:",
    "options": [
      "Primary Sector",
      "Secondary Sector",
      "Tertiary Sector",
      "Quaternary Sector"
    ],
    "answer": 0,
    "explanation": "When we produce a good by exploiting natural resources, it is an activity of the primary sector. This is because it forms the base for all other products that we subsequently make.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-002",
    "type": "mcq",
    "subtopic": "Secondary Sector Definition",
    "difficulty": "Easy",
    "question": "The sector that covers activities in which natural products are changed into other forms through manufacturing processes associated with industrial activity is the:",
    "options": [
      "Secondary Sector (Industrial Sector)",
      "Primary Sector",
      "Tertiary Sector",
      "Agrarian Sector"
    ],
    "answer": 0,
    "explanation": "The secondary sector covers activities in which natural products are changed into other forms through ways of manufacturing that we associate with industrial activity. For example, using sugarcane as a raw material to make sugar or gur.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-003",
    "type": "mcq",
    "subtopic": "Tertiary Sector Definition",
    "difficulty": "Easy",
    "question": "Activities that help in the development of the primary and secondary sectors by providing transport, storage, communication, and banking are classified under the:",
    "options": [
      "Tertiary Sector (Service Sector)",
      "Primary Sector",
      "Secondary Sector",
      "Extractive Sector"
    ],
    "answer": 0,
    "explanation": "These are activities that help in the development of the primary and secondary sectors. These activities, by themselves, do not produce a good but they are an aid or a support for the production process. Since these activities generate services, the tertiary sector is also called the service sector.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-004",
    "type": "mcq",
    "subtopic": "Gross Domestic Product (GDP) Definition",
    "difficulty": "Medium",
    "question": "Gross Domestic Product (GDP) of a country is defined as:",
    "options": [
      "The value of all final goods and services produced within a country during a particular year",
      "The total market value of all intermediate raw materials traded in agricultural mandis",
      "The total gold reserves stored in the vaults of the central bank",
      "The annual value of all foreign remittances sent by overseas citizens"
    ],
    "answer": 0,
    "explanation": "Gross Domestic Product (GDP) is the value of all final goods and services produced within a country during a particular year. It shows how big the economy is.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-005",
    "type": "mcq",
    "subtopic": "Avoiding Double Counting: Final Goods",
    "difficulty": "Medium",
    "question": "Why are only 'final goods and services' counted when calculating Gross Domestic Product?",
    "options": [
      "Because the value of final goods already includes the value of all intermediate goods used in making the final product",
      "Because intermediate goods have zero monetary value in wholesale markets",
      "Because government tax inspectors refuse to inspect raw material receipts",
      "Because intermediate goods are only produced by foreign multinational companies"
    ],
    "answer": 0,
    "explanation": "The value of final goods already includes the value of all the intermediate goods that are used in making the final good. For instance, the value of biscuits (final good) already includes the value of flour, sugar, and oil (intermediate goods). Counting intermediate goods separately would lead to double counting.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-006",
    "type": "mcq",
    "subtopic": "Historical Shift in Economic Sectors",
    "difficulty": "Medium",
    "question": "In the historical trajectory of today's developed nations, what was the typical sequence of sectoral dominance over time?",
    "options": [
      "Primary sector dominant first -> Secondary (manufacturing) sector dominant -> Tertiary (service) sector dominant",
      "Tertiary sector dominant first -> Primary sector -> Secondary sector",
      "Secondary sector dominant first -> Primary sector -> Tertiary sector",
      "All three sectors remained at exactly 33.3% share throughout history"
    ],
    "answer": 0,
    "explanation": "Historically, primary sector was the most important sector in the initial stages of development. With new manufacturing methods, factories came up and the secondary sector became dominant. In the past 100 years, there has been a further shift from secondary to tertiary sector in developed countries.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-007",
    "type": "mcq",
    "subtopic": "Rising Importance of Tertiary Sector in India",
    "difficulty": "Medium",
    "question": "Which of the following is a primary reason for the rapid growth of the tertiary sector in India over the past few decades?",
    "options": [
      "The government's responsibility to provide basic services like hospitals, schools, police stations, transport, and banking",
      "A complete shutdown of all agricultural farming and livestock rearing",
      "The legal prohibition of manufacturing factories in urban centres",
      "The elimination of personal computers and internet services"
    ],
    "answer": 0,
    "explanation": "In any country several basic services such as hospitals, educational institutions, post and telegraph services, police stations, courts, defense, transport, banks, and insurance are required. In a developing country, the government has to take responsibility for the provision of these services.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-008",
    "type": "mcq",
    "subtopic": "Employment vs GDP Mismatch in India",
    "difficulty": "Hard",
    "question": "While the tertiary sector contributes the largest share to India's GDP (over 50%), where does the largest proportion of the Indian workforce still remain employed?",
    "options": [
      "In the Primary (Agricultural) Sector",
      "In the Heavy Industrial Manufacturing Sector",
      "In the Information Technology and BPO Sector",
      "In the Commercial Banking and Insurance Sector"
    ],
    "answer": 0,
    "explanation": "A remarkable fact about India is that while there has been a change in the share of the three sectors in GDP, a similar shift has not taken place in employment. The primary sector continues to be the largest employer in India (employing over 44% of workers).",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-009",
    "type": "mcq",
    "subtopic": "Disguised Unemployment / Underemployment",
    "difficulty": "Easy",
    "question": "What is 'disguised unemployment' (or underemployment) which is prevalent in Indian agriculture?",
    "options": [
      "A situation where more people work on a farm than necessary, such that removing some workers does not reduce total crop production",
      "Workers who disguise their identity to avoid paying income taxes",
      "Workers who are unemployed during off-monsoon winter months",
      "Factory employees who work night shifts in textile mills"
    ],
    "answer": 0,
    "explanation": "Underemployment or disguised unemployment occurs when people are apparently working but all of them are made to work less than their potential. Even if you move a few people out, production will not be affected because they are surplus labour.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-010",
    "type": "mcq",
    "subtopic": "Example of Laxmi's Plot",
    "difficulty": "Medium",
    "question": "In the NCERT textbook example, farmer Laxmi owns a two-hectare unirrigated plot and all five family members work on it throughout the year. Why is this considered disguised unemployment?",
    "options": [
      "Each member does some work but none is fully employed; if two members take up outside wage labour, total farm output remains unchanged",
      "Laxmi's family produces crops exclusively for export to European markets",
      "The plot is owned by a multinational corporate conglomerate",
      "The family members receive salaries directly from the state treasury"
    ],
    "answer": 0,
    "explanation": "All five members work on the small plot because they have nowhere else to go for work. Each one does some work, but no one is fully employed. If two members move out to work in a mill, the family earns extra cash income while agricultural harvest remains the same.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-011",
    "type": "mcq",
    "subtopic": "Creating Rural Employment: Irrigation and Infrastructure",
    "difficulty": "Medium",
    "question": "How can the government directly reduce agricultural underemployment and create rural jobs?",
    "options": [
      "By constructing irrigation canals, check dams, and rural roads to connect villages with markets and enable multi-cropping",
      "By banning farmers from using tractors and organic seeds",
      "By evicting small farmers from their ancestral village lands",
      "By forcing all villagers to purchase commercial airline tickets"
    ],
    "answer": 0,
    "explanation": "If government spends some money on constructing a well or canals, farmers can irrigate their land and take a second crop (like wheat or pulses). This creates employment on the farm itself. Building rural roads and cold storages creates transport and marketing jobs.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-012",
    "type": "mcq",
    "subtopic": "MGNREGA 2005 Provisions",
    "difficulty": "Easy",
    "question": "What is the primary statutory guarantee provided under the Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA 2005)?",
    "options": [
      "100 days of guaranteed wage employment in a year to every rural household whose adult members volunteer to do unskilled manual work",
      "Free tractors and diesel fuel to all agricultural landholders",
      "365 days of salaried employment in urban corporate software firms",
      "Full monthly pensions to all citizens over the age of twenty-one"
    ],
    "answer": 0,
    "explanation": "Under MGNREGA 2005, all those who are able to, and are in need of, work in rural areas are guaranteed 100 days of employment in a year by the government.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-013",
    "type": "mcq",
    "subtopic": "MGNREGA Unemployment Allowance",
    "difficulty": "Medium",
    "question": "Under MGNREGA 2005, what happens if the government fails to provide employment within 15 days of an application?",
    "options": [
      "The government is legally obligated to pay a daily unemployment allowance to the applicant",
      "The applicant must forfeit their voter registration card",
      "The village sarpanch is immediately dismissed by the Supreme Court",
      "The applicant is allotted two hectares of central government forest land"
    ],
    "answer": 0,
    "explanation": "If the government fails in its duty to provide employment within 15 days, it gives unemployment allowances to the people. This is why it is known as the 'Right to Work'.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-014",
    "type": "mcq",
    "subtopic": "Organised Sector Features",
    "difficulty": "Easy",
    "question": "Which of the following is a hallmark characteristic of employment in the 'Organised Sector'?",
    "options": [
      "Jobs have formal appointment letters, security of employment, fixed working hours, and benefits like paid leave and provident fund",
      "Wages are paid randomly in cash with no formal payroll records",
      "Workers can be arbitrarily fired on any morning without notice or cause",
      "Workplaces are completely outside the scope of labour laws and Factory Acts"
    ],
    "answer": 0,
    "explanation": "Organised sector covers those enterprises where the terms of employment are regular and people have assured work. They are registered by government and have to follow rules like the Factories Act, Minimum Wages Act, Payment of Gratuity Act, providing job security and statutory benefits.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-015",
    "type": "mcq",
    "subtopic": "Unorganised Sector Features",
    "difficulty": "Easy",
    "question": "What is the primary condition of work in the 'Unorganised Sector' in India?",
    "options": [
      "Jobs are low-paid, often irregular, lack job security, and offer no provision for overtime pay, paid holidays, or medical leave",
      "Workers receive double pay for every hour of overtime worked",
      "Employees are covered by comprehensive group health insurance schemes",
      "Workers are represented by constitutionally recognized collective bargaining unions"
    ],
    "answer": 0,
    "explanation": "The unorganised sector is characterised by small and scattered units which are largely outside the control of the government. Jobs here are low-paid and often not regular. There is no provision for overtime, paid leave, holidays, leave due to sickness, etc.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-016",
    "type": "mcq",
    "subtopic": "Comparison: Kanta vs Kamal",
    "difficulty": "Medium",
    "question": "In the NCERT case study comparing Kanta (office worker) and Kamal (grocery store assistant), why is Kamal considered to be in the unorganised sector?",
    "options": [
      "Kamal works from 7:30 AM to 8:00 PM without overtime pay, gets no paid leave, has no formal appointment letter, and can be told to leave at any time",
      "Kamal receives a monthly provident fund statement from the central government",
      "Kamal gets free medical treatment at an executive corporate hospital",
      "Kamal works only two hours on weekends"
    ],
    "answer": 0,
    "explanation": "Kamal works in a small grocery store without formal appointment, works long hours without overtime pay, receives no paid holidays, and has no job security. Hence, he is in the unorganised sector.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-017",
    "type": "mcq",
    "subtopic": "Vulnerable Groups in Unorganised Sector",
    "difficulty": "Medium",
    "question": "In rural areas, who constitutes the bulk of vulnerable workers needing state protection in the unorganised sector?",
    "options": [
      "Landless agricultural labourers, small and marginal farmers, sharecroppers, and traditional artisans (weavers, blacksmiths, carpenters)",
      "Senior bank executives and financial fund managers",
      "Software architects working in metropolitan cyber parks",
      "Supreme Court senior advocates and corporate attorneys"
    ],
    "answer": 0,
    "explanation": "In rural areas, the unorganised sector mostly comprises landless agricultural labourers, small and marginal farmers, sharecroppers and artisans (such as weavers, blacksmiths, carpenters and goldsmiths).",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-018",
    "type": "mcq",
    "subtopic": "Public vs Private Sector Classification",
    "difficulty": "Easy",
    "question": "Economic activities are classified into 'Public Sector' and 'Private Sector' on the basis of:",
    "options": [
      "Ownership of assets and delivery of services (government vs private individuals/companies)",
      "The physical weight of the finished manufactured goods",
      "The geographical distance of factories from international seaports",
      "The number of female employees in administrative management"
    ],
    "answer": 0,
    "explanation": "Another way of classifying economic activities is based on who owns assets and is responsible for the delivery of services: in the public sector, the government owns most assets and provides services; in the private sector, ownership of assets is in the hands of private individuals or companies.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-019",
    "type": "mcq",
    "subtopic": "Public Sector Purpose",
    "difficulty": "Easy",
    "question": "What is the primary driving motivation behind economic activities undertaken by the Public Sector (such as Indian Railways and Post Office)?",
    "options": [
      "Social welfare and public benefit at affordable, subsidized rates",
      "Maximizing quarterly corporate profits for private equity shareholders",
      "Eliminating all competition to create private business monopolies",
      "Transferring state revenues to offshore foreign bank accounts"
    ],
    "answer": 0,
    "explanation": "Activities in the private sector are guided by the motive to earn profits. The purpose of the public sector is not just to earn profits. Governments raise money through taxes and other ways to meet expenses on the services rendered by it for public welfare.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s1-020",
    "type": "mcq",
    "subtopic": "Why Government Must Invest in Heavy Infrastructure",
    "difficulty": "Medium",
    "question": "Why cannot the private sector alone be expected to build mega infrastructure like railways, multipurpose dams, and ports?",
    "options": [
      "These projects require astronomical capital investments with very long gestation periods and cannot easily collect profits from millions of individual users",
      "The private sector is legally barred by the constitution from operating heavy machinery",
      "Engineers refuse to work for private commercial enterprises",
      "Infrastructure construction has zero impact on national economic development"
    ],
    "answer": 0,
    "explanation": "There are several things needed by society as a whole which the private sector will not provide at reasonable cost. These require huge spending which is beyond the capacity of the private sector, and collecting money from thousands of users is difficult. Thus, governments have to undertake heavy spending.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  }
]

# -----------------------------------------------------------------------------
# CH 19 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch19_set2 = [
  {
    "id": "cbse10-sst-eco-ch19-s2-001",
    "type": "mcq",
    "subtopic": "Interdependence of Economic Sectors",
    "difficulty": "Medium",
    "question": "If all truck drivers and transport operators across India decide to go on a nationwide strike, what immediate economic consequence will follow?",
    "options": [
      "Farmers will be unable to sell their vegetables and milk, causing produce to rot, while urban factories shut down due to lack of raw materials",
      "The agricultural sector will automatically double its food grain output",
      "Software companies will begin manufacturing heavy diesel trucks",
      "Wholesale commodity prices in urban retail markets will drop to zero"
    ],
    "answer": 0,
    "explanation": "This demonstrates sectoral interdependence: the tertiary sector (transport) links primary agricultural producers to urban consumers and secondary factory processors. Without transport, both primary and secondary sectors collapse.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1 (Table on Interdependence)"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-002",
    "type": "mcq",
    "subtopic": "Case Analysis: Cotton Textile Chain",
    "difficulty": "Medium",
    "question": "A farmer cultivates raw cotton (Primary), a textile mill spins yarn and weaves cloth (Secondary), and a wholesale trader transports and markets the shirts to retail stores (Tertiary). This value chain proves that:",
    "options": [
      "Economic sectors do not function in isolation; each successive sector adds economic value to the output of preceding sectors",
      "Raw cotton can be converted into shirts without any industrial processing",
      "Wholesale traders belong exclusively to the primary agricultural sector",
      "Secondary manufacturing can operate without raw materials from nature"
    ],
    "answer": 0,
    "explanation": "Each stage in the supply chain builds upon the preceding stage: primary provides raw natural fibre, secondary transforms it into fabric and garments, and tertiary distributes it to the consumer.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-003",
    "type": "mcq",
    "subtopic": "Disguised Unemployment in Urban Areas",
    "difficulty": "Medium",
    "question": "Does disguised unemployment exist only in rural agriculture, or is it also visible in urban areas?",
    "options": [
      "It is also visible in urban areas among thousands of casual street vendors, cart pushers, and repair persons who spend the whole day working but earn very little",
      "It is strictly illegal and non-existent in urban municipalities",
      "It only affects software engineers working in multinational corporate firms",
      "It is legally restricted to government civil servants"
    ],
    "answer": 0,
    "explanation": "There are thousands of casual workers in the service sector in urban areas who search for daily employment (painters, plumbers, repair persons, street vendors). They may spend the whole day but earn very little; they do this work because they lack better opportunities.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-004",
    "type": "mcq",
    "subtopic": "Employment Elasticity of Service Sector",
    "difficulty": "Hard",
    "question": "Over the past forty years, industrial production in India grew by more than 9 times while industrial employment grew by only around 3 times. Similarly, service output grew by 14 times while service employment grew by only 5 times. What fundamental structural challenge does this reveal?",
    "options": [
      "Growth in secondary and tertiary sectors has been capital-intensive, failing to generate sufficient employment commensurate with output growth ('jobless growth')",
      "Indian workers refuse to accept employment in factories or offices",
      "The Indian economy has completely de-industrialized since 1970",
      "The primary sector has completely absorbed all surplus urban engineers"
    ],
    "answer": 0,
    "explanation": "While production in service and industry expanded dramatically, employment did not grow at the same pace. As a result, more than half the country's workers remain stuck in primary agriculture where output per worker is low.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-005",
    "type": "mcq",
    "subtopic": "Potential of Tourism and Regional Crafts",
    "difficulty": "Medium",
    "question": "According to the Planning Commission (NITI Aayog) studies cited in NCERT, developing tourism in every state has the potential to generate additional employment for how many people annually?",
    "options": [
      "Over 35 lakh (3.5 million) people every year",
      "Exactly 500 individuals nationally",
      "Zero people, because tourism eliminates jobs in local transport",
      "Over 100 crore people every six months"
    ],
    "answer": 0,
    "explanation": "A study conducted by the Planning Commission (now NITI Aayog) estimates that if tourism as a sector is improved, every year we can give additional employment to more than 35 lakh people.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-006",
    "type": "mcq",
    "subtopic": "Right to Education as Employment Generator",
    "difficulty": "Medium",
    "question": "If India were to ensure that all children aged 5 to 17 attend quality schools as envisioned under the Right to Education, what significant employment outcome would emerge?",
    "options": [
      "Millions of additional jobs would be created for teachers, school administrators, building contractors, and support staff",
      "All adult workers would be forced into unemployment",
      "Government revenues would drop to zero immediately",
      "School textbook publishers would go bankrupt"
    ],
    "answer": 0,
    "explanation": "Nearly 200 million children in the school-going age group are not in school. To bring them into classrooms requires more buildings, teachers, and staff. Studies estimate that nearly 20 lakh jobs can be created in the education sector alone.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-007",
    "type": "mcq",
    "subtopic": "Credit as a Catalyst for Rural Employment",
    "difficulty": "Medium",
    "question": "Why is the provision of cheap and affordable formal credit to small farmers considered a vital strategy for employment generation?",
    "options": [
      "It allows farmers to purchase seeds, fertilizers, and irrigation equipment without falling into the debt-trap of exploitative local moneylenders",
      "It allows farmers to permanently stop farming and move to luxury resorts",
      "It forces commercial banks to forgive all corporate urban debts",
      "It eliminates the need for agricultural harvests"
    ],
    "answer": 0,
    "explanation": "Small farmers need credit for seeds, fertilizers, pumps, and pesticides. If local commercial or cooperative banks provide credit at reasonable interest, farmers can invest, grow multiple crops, and generate sustained on-farm employment.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-008",
    "type": "mcq",
    "subtopic": "Dualism Within the Service Sector",
    "difficulty": "Hard",
    "question": "Is the entire service sector in India expanding and prospering uniformly?",
    "options": [
      "No; only highly skilled services (IT, software, finance) are booming, while millions of unorganized service workers (hawkers, domestic maids, auto drivers) earn barely enough for survival",
      "Yes; every service worker in India earns over ₹1,00,000 per month",
      "No; all software engineers in India are living below the national poverty line",
      "Yes; there are no unorganized service workers left in Indian cities"
    ],
    "answer": 0,
    "explanation": "Service sector in India employs many different kinds of people. At one end there are a limited number of services that employ highly skilled and educated workers. At the other end, there are a very large number of workers engaged in services such as small shopkeepers, repair persons, transport persons. These people barely manage to earn a living.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-009",
    "type": "mcq",
    "subtopic": "Exploitation in the Unorganised Sector",
    "difficulty": "Medium",
    "question": "Why do many private enterprises in India deliberately evade registering under the Factories Act and prefer operating in the unorganised sector?",
    "options": [
      "To evade taxes, ignore minimum wage mandates, and avoid paying statutory employee benefits like provident fund and gratuity",
      "Because factory registration requires paying corporate taxes to the United Nations",
      "Because the government bans registered factories from using electricity",
      "Because unorganised factories receive free imported raw materials"
    ],
    "answer": 0,
    "explanation": "Many organized units adopt strategies to evade laws and refuse to follow regulations that protect labourers. As a result, a large number of workers are forced to enter the unorganised sector jobs, which pay a very low salary.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-010",
    "type": "mcq",
    "subtopic": "Social Discrimination and Unorganised Labour",
    "difficulty": "Board Standard",
    "question": "In India, what critical social reality intersects with employment in the unorganised sector?",
    "options": [
      "A vast majority of workers in unorganised jobs belong to Scheduled Castes (SC), Scheduled Tribes (ST), and backward communities, facing both economic insecurity and social discrimination",
      "Unorganised workers belong exclusively to upper-caste royal dynasties",
      "Caste has zero correlation with unorganised labour representation",
      "Scheduled Castes are constitutionally barred from working in the unorganised sector"
    ],
    "answer": 0,
    "explanation": "A majority of workers from scheduled castes, tribes and backward communities find themselves in the unorganised sector. Besides getting the irregular and low-paid work, these workers also face social discrimination. Protection and support to the unorganised sector workers is thus necessary for both economic and social development.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-011",
    "type": "mcq",
    "subtopic": "Government Support: Electricity Subsidies for Farmers",
    "difficulty": "Medium",
    "question": "Why does the government subsidize the price of electricity and diesel for agricultural tubewells and sell food grains at low prices through fair price shops?",
    "options": [
      "To protect small cultivators and poor consumers from market failures and ensure national food security",
      "To intentionally drive private electricity generating corporations into bankruptcy",
      "To encourage farmers to waste water and flood fertile agricultural soils",
      "To fulfill conditions imposed by foreign multinational corporations"
    ],
    "answer": 0,
    "explanation": "Governments have to support some activities. For example, selling electricity at the cost of generation may push up the costs of production of goods in small-scale units. The government bears part of the cost to protect small producers and consumers.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-012",
    "type": "mcq",
    "subtopic": "Calculating Total Production in GDP",
    "difficulty": "Hard",
    "question": "A farmer sells wheat to a flour mill for ₹10 per kg. The mill grinds the wheat and sells flour to a biscuit company for ₹12 per kg. The biscuit company uses flour, sugar, and oil to produce 4 packets of biscuits and sells them to consumers at ₹20 per packet (Total ₹80). What is the total value added to GDP?",
    "options": [
      "₹80 (the final market value of the biscuits)",
      "₹102 (₹10 + ₹12 + ₹80)",
      "₹10 (only the primary agricultural wheat)",
      "₹22 (₹10 wheat + ₹12 flour)"
    ],
    "answer": 0,
    "explanation": "In GDP, only the value of final goods and services is counted. The biscuits are the final good reaching the consumer, valued at ₹80. All intermediate values (wheat ₹10, flour ₹12) are already embedded in the final ₹80 price.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-013",
    "type": "mcq",
    "subtopic": "Tertiary Sector: IT & Communication Boom",
    "difficulty": "Medium",
    "question": "In the fourth factor explaining tertiary growth in India, which new services have expanded with extraordinary speed over the last two decades?",
    "options": [
      "Information and communication technology (ICT) and business process outsourcing (BPO) services",
      "Bullock cart freight and pigeon courier networks",
      "Handloom spinning wheel workshops in urban centres",
      "Coal-fired locomotive repair workshops"
    ],
    "answer": 0,
    "explanation": "Over the past decade or so, certain new services such as those based on information and communication technology have become important and essential. The production of these services has been rising rapidly.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-014",
    "type": "mcq",
    "subtopic": "Primary Sector Stagnation vs Growth",
    "difficulty": "Hard",
    "question": "Why does agricultural output per worker in India remain substantially lower than output per worker in manufacturing and services?",
    "options": [
      "Because agriculture suffers from severe disguised unemployment, small and fragmented landholdings, and dependence on monsoons",
      "Because Indian farmers refuse to use modern agricultural tools or high-yielding seeds",
      "Because agricultural grain has zero economic value in domestic consumer markets",
      "Because the government bans farmers from working more than three hours a day"
    ],
    "answer": 0,
    "explanation": "Nearly half the workforce produces only around one-sixth of GDP in agriculture because millions of surplus labourers are underemployed on fragmented plots without modern capital assets.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-015",
    "type": "mcq",
    "subtopic": "Agro-Processing Units in Semi-Rural Areas",
    "difficulty": "Medium",
    "question": "How can establishing agro-processing units (such as dal mills, cold storages, and honey collection centres) in semi-rural areas solve unemployment?",
    "options": [
      "They provide non-farm employment to rural youth while allowing local farmers to sell produce at higher prices without distress sales to middlemen",
      "They force all rural youth to migrate to metropolitan slum tenements",
      "They replace all agricultural farmland with concrete parking lots",
      "They require all village workers to be certified software programmers"
    ],
    "answer": 0,
    "explanation": "Setting up dal mills to process pulses, cold storage to store potatoes/onions, and honey collection centres creates jobs close to villages, absorbing surplus agricultural labour without forced urban migration.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-016",
    "type": "mcq",
    "subtopic": "Public Sector Examples",
    "difficulty": "Easy",
    "question": "Which of the following pairs represents classic examples of the Indian Public Sector?",
    "options": [
      "Indian Railways and Bharat Heavy Electricals Limited (BHEL)",
      "Reliance Industries Limited (RIL) and Tata Consultancy Services (TCS)",
      "Infosys Technologies and Mahindra & Mahindra",
      "Adani Ports and Larsen & Toubro (L&T)"
    ],
    "answer": 0,
    "explanation": "Indian Railways and Bharat Heavy Electricals Limited (BHEL) are owned, financed, and operated by the Government of India for public service and national infrastructure.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-017",
    "type": "mcq",
    "subtopic": "Private Sector Examples",
    "difficulty": "Easy",
    "question": "Which of the following pairs represents classic enterprises operating in the Private Sector in India?",
    "options": [
      "Tata Iron and Steel Company (TISCO) and Reliance Industries Limited (RIL)",
      "Indian Post Office and Steel Authority of India Limited (SAIL)",
      "Oil and Natural Gas Corporation (ONGC) and Coal India Limited (CIL)",
      "National Thermal Power Corporation (NTPC) and Reserve Bank of India (RBI)"
    ],
    "answer": 0,
    "explanation": "TISCO (Tata Steel) and Reliance Industries Limited (RIL) are privately owned corporations managed by shareholders and boards of directors for commercial profitability.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-018",
    "type": "mcq",
    "subtopic": "MGNREGA Focus on Drought-Proofing",
    "difficulty": "Medium",
    "question": "What type of public civil works are given priority under MGNREGA 2005?",
    "options": [
      "Water conservation, desilting ponds, drought-proofing, afforestation, and building rural connectivity roads that enhance long-term agricultural productivity",
      "Building five-star luxury tourist hotels in state capitals",
      "Assembling consumer electronic laptops for private export",
      "Constructing private residential swimming pools for urban landlords"
    ],
    "answer": 0,
    "explanation": "Under the Act, the types of work that would in future help to increase the production from land are given preference. These include water conservation, desilting of irrigation tanks, watershed development, and tree planting.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-019",
    "type": "mcq",
    "subtopic": "Social Protection in Unorganised Sector",
    "difficulty": "Board Standard",
    "question": "Why is government intervention and legal regulation essential to protect workers in the unorganised sector?",
    "options": [
      "Because market mechanisms leave workers defenseless against wage suppression, hazardous working conditions, arbitrary dismissal, and extreme poverty",
      "Because unorganised workers have formed private armies to take over parliament",
      "Because unorganised enterprises are owned by foreign sovereign governments",
      "Because unorganised workers are exempt from buying food in commercial markets"
    ],
    "answer": 0,
    "explanation": "Unorganised workers have zero bargaining power, face severe job insecurity, sub-minimum wages, and dangerous workplaces; without strict labour enforcement and social security schemes, they are perpetually trapped in poverty.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s2-020",
    "type": "mcq",
    "subtopic": "Synthesis: Sectoral Transformation of India",
    "difficulty": "Board Standard",
    "question": "How does India's sectoral transition differ fundamentally from the classical path followed by advanced industrialized nations like Britain and the USA?",
    "options": [
      "India leapfrogged directly from an agrarian economy to a service-dominant GDP economy without the manufacturing sector ever becoming the principal employer of labour",
      "India industrialized completely before developing any primary agricultural sector",
      "India has never developed any service or transport infrastructure",
      "India has 90% of its workforce employed in heavy steel foundries"
    ],
    "answer": 0,
    "explanation": "Unlike Western economies where surplus agrarian workers shifted first to factory manufacturing, India's secondary sector generated relatively few jobs; the GDP shift bypassed secondary dominance straight into services, leaving surplus labour stranded in agriculture.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  }
]

# -----------------------------------------------------------------------------
# CH 19 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch19_set3 = [
  {
    "id": "cbse10-sst-eco-ch19-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Counting Final Goods in GDP",
    "difficulty": "Board Standard",
    "question": "Assertion (A): While computing the Gross Domestic Product (GDP), only the value of final goods and services is considered.\nReason (R): Intermediate goods are completely consumed during the production process and their monetary value is already reflected in the market price of the final good.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Intermediate goods like flour and sugar are absorbed into final goods like biscuits; counting intermediate goods separately would cause the error of double counting.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Disguised Unemployment in Agriculture",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Disguised unemployment exists extensively in the Indian agricultural sector.\nReason (R): More people are engaged in farming activities than strictly required, and withdrawing a portion of farmworkers does not cause any decline in total agricultural output.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Surplus farm labourers share work on family plots; their marginal productivity is zero because pulling them away to other jobs leaves crop production unaffected.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Rising Dominance of Tertiary Sector",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Over the past forty years, the tertiary sector has emerged as the largest producing sector in India, replacing agriculture.\nReason (R): The demand for basic services like healthcare, education, transport, banking, and modern IT communications has expanded rapidly with development.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Tertiary sector growth is driven by government provision of basic public services, growth of trade, higher consumer spending on services, and the information technology revolution.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: MGNREGA as Right to Work",
    "difficulty": "Board Standard",
    "question": "Assertion (A): MGNREGA 2005 is referred to as the legislative realization of the 'Right to Work'.\nReason (R): If the state administration fails to provide 100 days of guaranteed wage employment within 15 days of demand, it is legally bound to pay an unemployment allowance.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "MGNREGA legally empowers rural adults with a statutory right to work or compensatory daily unemployment allowance, making employment an enforceable entitlement.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Organised vs Unorganised Employment",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Workers in the organised sector enjoy significantly higher employment security than workers in the unorganised sector.\nReason (R): Organised enterprises are registered under the government and bound by statutory labour legislations including the Factories Act and Industrial Disputes Act.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Legal registration under statutory acts mandates appointment letters, notice periods, severance pay, and grievance redressal in the organised sector.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-006",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Need for Public Sector in Infrastructure",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Heavy infrastructural projects like railways, multipurpose dams, and space exploration are primarily operated by the public sector.\nReason (R): These projects require massive capital outlay with long gestation cycles and cannot yield immediate high private profits.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Private capital seeks rapid profitability; strategic national infrastructure requires public investment aimed at broad economic facilitation rather than short-term profit.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-007",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Primary Sector Employment Lag",
    "difficulty": "Board Standard",
    "question": "Assertion (A): In India, a major structural shift in employment from the primary to secondary and tertiary sectors has not occurred despite massive GDP growth in services.\nReason (R): Not enough jobs were created in the secondary manufacturing and organized service sectors to absorb surplus agricultural labour.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Industrial and service growth in India has been largely capital- and technology-intensive rather than labour-intensive, failing to absorb rural labour.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Sectoral Interdependence",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The primary, secondary, and tertiary sectors are deeply interdependent.\nReason (R): An increase in agricultural output increases the demand for industrial processing and requires tertiary transport, banking, and storage services.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "No sector functions autonomously: primary supplies raw materials to secondary, secondary supplies machines/fertilizers to primary, and tertiary provides transport/finance to both.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-009",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Informalisation of the Workforce",
    "difficulty": "Board Standard",
    "question": "Assertion (A): A significant number of workers from the organized sector are sliding into the unorganized sector in recent decades.\nReason (R): Many private organized enterprises outsource jobs to informal contractors and sub-contractors to avoid complying with statutory labour welfare laws.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Corporate downsizing, subcontracting, and contractual hiring have expanded the unorganised workforce while stripping workers of permanent employment security.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Rural Credit and Employment",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Expanding affordable bank credit to rural farming households creates sustained non-farm employment.\nReason (R): Access to low-interest loans enables farmers to invest in irrigation, purchase livestock, or establish agro-processing units like flour mills.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Cheap capital unlocks productive capacity in villages, allowing families to start small enterprises and break free from agricultural underemployment.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-011",
    "type": "case_based",
    "subtopic": "Case Analysis: Laxmi's Family Plot",
    "difficulty": "Board Standard",
    "question": "Laxmi's family has 5 members working on their two-hectare unirrigated plot, producing 15 quintals of jowar. When an NGO helps two members secure jobs in a nearby spinning mill, the remaining three members still produce 15 quintals of jowar. What does this confirm?",
    "options": [
      "The two workers were previously underemployed (disguisedly unemployed), and their removal caused zero loss of agricultural output",
      "The plot has become three times more fertile due to soil erosion",
      "Laxmi's family has abandoned agriculture completely",
      "The spinning mill operates as an unorganised enterprise"
    ],
    "answer": 0,
    "explanation": "Because production remained at 15 quintals even after two workers left, those workers were contributing zero marginal product — the textbook definition of disguised unemployment.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis: Kanta in the Organised Sector",
    "difficulty": "Medium",
    "question": "Kanta works in an office from 9:30 AM to 5:30 PM, receives a regular monthly salary via direct bank transfer, gets medical benefits, paid Sunday holidays, and provident fund contributions. This case shows that Kanta:",
    "options": [
      "Enjoys the legal protections, job security, and statutory social welfare benefits guaranteed in the Organised Sector",
      "Works in an unorganised agricultural farm",
      "Is vulnerable to immediate dismissal without notice on Monday morning",
      "Is self-employed in the informal cottage sector"
    ],
    "answer": 0,
    "explanation": "Kanta's terms of employment demonstrate all criteria of the organised sector: formal appointment, fixed hours, paid leaves, medical care, and retirement provident fund.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-013",
    "type": "case_based",
    "subtopic": "Case Analysis: Kamal in the Unorganised Sector",
    "difficulty": "Medium",
    "question": "Kamal is Kanta's neighbour working as a daily-wage assistant in a grocery store. He works from 7:30 AM to 8:00 PM without extra overtime pay, has no paid sick leave, received no appointment letter, and was told he could be fired if business slows down. This case demonstrates:",
    "options": [
      "The complete lack of job security, sub-minimum wages, and absence of social safety nets characteristic of the Unorganised Sector",
      "That Kamal earns more money than Kanta every month",
      "That grocery stores are classified under the public sector",
      "That Kamal is a permanent civil service employee"
    ],
    "answer": 0,
    "explanation": "Kamal's precarious employment conditions are typical of unorganised labour: unregulated long hours, no overtime compensation, zero paid leave, and no job security.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-014",
    "type": "case_based",
    "subtopic": "Case Analysis: MGNREGA Pond Rejuvenation",
    "difficulty": "Medium",
    "question": "In a drought-prone village in Bundelkhand, 80 rural workers are employed under MGNREGA to deepen a village percolation tank. Which twin benefits does this project deliver?",
    "options": [
      "It provides immediate 100 days of guaranteed wage support while creating permanent productive water conservation infrastructure that boosts future crops",
      "It drains all groundwater to build private luxury resorts",
      "It forces all villagers to abandon their ancestral village lands",
      "It eliminates the need for future agricultural farming"
    ],
    "answer": 0,
    "explanation": "MGNREGA is designed to combine short-term livelihood relief (wages) with long-term ecological and productive assets (rainwater harvesting, tank desilting).",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.3"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-015",
    "type": "case_based",
    "subtopic": "Case Analysis: Biscuit Production Supply Chain",
    "difficulty": "Hard",
    "question": "A packet of biscuits is manufactured using flour, sugar, vegetable oil, and packaging paper. In computing national income, why is the statistician instructed to include only the retail price of the biscuit packet?",
    "options": [
      "Because counting the separate sales of wheat, flour, sugar, and oil before the biscuit is sold would count the same value multiple times, artificially inflating GDP",
      "Because agricultural wheat has no monetary value until it reaches the consumer",
      "Because biscuit manufacturers do not pay income taxes to the government",
      "Because intermediate goods are not traded in market economies"
    ],
    "answer": 0,
    "explanation": "Intermediate values are completely absorbed within the final product. Counting both intermediate inputs and final goods creates the classic GDP error of double counting.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.1"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-016",
    "type": "mcq",
    "subtopic": "Informal Workers in Urban Construction",
    "difficulty": "Medium",
    "question": "Construction workers gathered at urban 'labour chowks' every morning looking for daily work illustrate which employment reality?",
    "options": [
      "Urban informal underemployment where workers face unpredictable daily hiring, absence of safety equipment, and zero health or disability compensation",
      "Permanent tenured employment in the public sector",
      "Organised corporate employment under the Factories Act",
      "Software consultancy employment in IT cyber parks"
    ],
    "answer": 0,
    "explanation": "Urban labour chowks represent the precarious reality of daily-wage unorganised labour: hiring depends on daily demand, wages fluctuate, and there are no protections.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-017",
    "type": "mcq",
    "subtopic": "Government Support for Small Scale Industries",
    "difficulty": "Medium",
    "question": "Why does the central government provide marketing support, subsidized raw materials, and institutional credit to small scale industries (SSIs)?",
    "options": [
      "Because small scale industries are highly labour-intensive and generate substantial manufacturing employment across tier-2 and tier-3 towns",
      "Because small scale industries produce heavy nuclear submarines",
      "Because small scale industries are owned exclusively by state governments",
      "Because multinational corporations refuse to sell consumer goods"
    ],
    "answer": 0,
    "explanation": "Small-scale industries are crucial for decentralized industrialization and employment generation because they absorb more labour per unit of capital than large mega-factories.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.4"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-018",
    "type": "mcq",
    "subtopic": "Tertiary Sector Growth Engine",
    "difficulty": "Board Standard",
    "question": "Which of the following factors best explains why the expansion of agriculture and industry directly accelerates tertiary service growth?",
    "options": [
      "Greater farm and factory production requires more transport trucks, commercial warehouses, banking credit, and marketing retail distribution",
      "Agriculture and industry destroy service sector employment",
      "Farmers stop buying clothes once crop harvests increase",
      "Factory workers refuse to use commercial transport networks"
    ],
    "answer": 0,
    "explanation": "The development of agriculture and industry leads to the development of services such as transport, trade, and storage. The greater the development of primary and secondary sectors, the greater the demand for such services.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.2"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-019",
    "type": "mcq",
    "subtopic": "Public Sector Health and Education Obligations",
    "difficulty": "Medium",
    "question": "Why is the provision of quality basic education and healthcare universally acknowledged as the primary duty of the Public Sector rather than private businesses?",
    "options": [
      "Because education and healthcare are fundamental human rights that must be accessible to all citizens regardless of ability to pay, which profit-driven markets cannot ensure",
      "Because private hospitals are legally barred from treating patients",
      "Because government teachers refuse to accept salaries from private schools",
      "Because private schools are constitutionally banned in India"
    ],
    "answer": 0,
    "explanation": "Nearly half of India's children are malnourished and millions lack schooling. The government has a constitutional duty to ensure basic health, education, and drinking water as public goods.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Section 2.5"
  },
  {
    "id": "cbse10-sst-eco-ch19-s3-020",
    "type": "mcq",
    "subtopic": "Synthesis: Policy Blueprint for Sectoral Health",
    "difficulty": "Board Standard",
    "question": "To achieve balanced, inclusive, and employment-rich economic growth, which integrated strategy must India execute across its sectors?",
    "options": [
      "Modernize agriculture and agro-processing, stimulate labour-intensive manufacturing, expand affordable credit and skill development, and formalize unorganised worker protections",
      "Shut down all primary agricultural farming and import all food grains from abroad",
      "Nationalize all private corporate software companies and dismantle private enterprises",
      "Abolish all labour welfare laws to eliminate the organised sector completely"
    ],
    "answer": 0,
    "explanation": "Sustainable development requires agricultural productivity gains, expanding job-rich manufacturing, formalizing unorganised workers, and providing universal public health and education.",
    "citation": "NCERT Class 10 Economics, Chapter 2, Chapter Summary"
  }
]

# Write Chapter 18 Sets 1, 2, 3
with open(os.path.join(DATA_DIR, "ch18_development_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch18_set1}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch18_development_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch18_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch18_development_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch18_set3}, f, indent=2, ensure_ascii=False)
print("Generated Ch 18 (Development) Sets 1, 2, 3 (60 Qs total) successfully!")

# Write Chapter 19 Sets 1, 2, 3
with open(os.path.join(DATA_DIR, "ch19_sectors_of_indian_economy_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch19_set1}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch19_sectors_of_indian_economy_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch19_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch19_sectors_of_indian_economy_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch19_set3}, f, indent=2, ensure_ascii=False)
print("Generated Ch 19 (Sectors of Indian Economy) Sets 1, 2, 3 (60 Qs total) successfully!")
