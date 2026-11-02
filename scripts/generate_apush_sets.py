#!/usr/bin/env python3
"""
AP® U.S. History (APUSH) Question Bank Generator
Generates 100 authentic College Board CED-aligned stimulus-based MCQs across 5 sets:
- Set 1: Periods 1 & 2 (1491–1754) — 20 Questions
- Set 2: Periods 3 & 4 (1754–1848) — 20 Questions
- Set 3: Periods 5 & 6 (1844–1898) — 20 Questions
- Set 4: Periods 7 & 8 (1890–1980) — 20 Questions
- Set 5: Period 9 & Thematic Review (1980–Present) — 20 Questions
"""

import json
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "us", "ap")
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# SET 1: Periods 1 & 2 (1491–1754) — 20 Questions
# -------------------------------------------------------------
set1_questions = [
    {
        "id": "ap-ush-001",
        "type": "mcq",
        "subtopic": "Pre-Columbian Societies (Period 1: 1491–1607)",
        "difficulty": "Medium",
        "question": "“The people of this island and of all the other islands which I have found and of which I have information, all go naked, men and women, as their mothers bore them... They have no iron or steel or weapons, nor are they fitted to use them, not because they are not well built, of handsome stature, but because they are very marvelously timorous.”\n— Christopher Columbus, Letter to Luis de Santángel Regarding the First Voyage, 1493\n\nColumbus's description of indigenous peoples in the excerpt best reflects which of the following European perspectives during early contact?",
        "options": [
            "A perception of Native Americans as technologically and culturally suited for subjugation and religious conversion",
            "A recognition of indigenous legal sovereignty and territorial rights under European international law",
            "An appreciation for native horticultural advancements and decentralized democratic governance",
            "A desire to establish reciprocal military alliances against rival Ottoman expansion"
        ],
        "answer": 0,
        "explanation": "Columbus characterized native peoples as unarmed, docile ('timorous'), and lacking metallurgy, which reinforced European views that indigenous societies were vulnerable to conquest, ripe for exploitation as forced labor, and in need of Christian conversion.",
        "citation": "College Board AP® U.S. History CED — Unit 1: Topic 1.3 European Exploration in the Americas"
    },
    {
        "id": "ap-ush-002",
        "type": "mcq",
        "subtopic": "The Columbian Exchange (Period 1: 1491–1607)",
        "difficulty": "Easy",
        "question": "Which of the following was the most direct biological consequence of the Columbian Exchange on the indigenous populations of the Americas during the sixteenth century?",
        "options": [
            "A catastrophic demographic collapse caused by epidemic diseases such as smallpox, measles, and influenza",
            "A sharp increase in life expectancy resulting from the introduction of European livestock and horses",
            "The rapid development of genetic immunity to Eurasian pathogens within one generation",
            "The widespread migration of Native Americans to western European metropolitan centers"
        ],
        "answer": 0,
        "explanation": "Due to thousands of years of biological isolation from the Eastern Hemisphere, Native Americans possessed no immunities to Old World pathogens (smallpox, measles, typhus). Contact triggered virgin-soil epidemics that annihilated between 50% to 90% of native populations in many regions.",
        "citation": "College Board AP® U.S. History CED — Unit 1: Topic 1.4 Columbian Exchange, Spanish Exploration, and Conquest"
    },
    {
        "id": "ap-ush-003",
        "type": "mcq",
        "subtopic": "Spanish Labor & Encomienda System (Period 1: 1491–1607)",
        "difficulty": "Hard",
        "question": "“The Spanish have a perfect right to rule these barbarians of the New World and the adjacent islands, who in prudence, skill, virtues, and humanity are as inferior to the Spanish as children to adults, or women to men, for there exists between them as great a difference as between savage and cruel races and the most merciful, between the most intemperate and the moderate and temperate.”\n— Juan Ginés de Sepúlveda, Democrates Alter, or on the Just Causes for War Against the Indians, 1547\n\nThe arguments expressed in the excerpt were primarily intended to justify which of the following colonial institutions?",
        "options": [
            "The encomienda system of coerced indigenous agricultural and mining labor",
            "The establishment of Quaker principles of pacifism and fair purchase of Indian lands",
            "The French coureurs des bois system of collaborative fur-trading partnerships",
            "The Puritans' creation of self-governing religious praying towns"
        ],
        "answer": 0,
        "explanation": "Sepúlveda drew on Aristotelian theories of 'natural slavery' during the Valladolid Debate (1550–1551) to justify the Spanish Crown's encomienda system, arguing that indigenous peoples were naturally inferior and required Spanish dominion, forced labor, and Christian conversion.",
        "citation": "College Board AP® U.S. History CED — Unit 1: Topic 1.5 Labor, Slavery, and Caste in the Spanish Colonial System"
    },
    {
        "id": "ap-ush-004",
        "type": "mcq",
        "subtopic": "Columbian Exchange Economic Impact (Period 1: 1491–1607)",
        "difficulty": "Medium",
        "question": "How did the introduction of American crops—specifically maize and potatoes—most significantly impact European societies in the sixteenth and seventeenth centuries?",
        "options": [
            "They provided calorically dense, drought-resistant food staples that spurred significant population growth across Europe",
            "They led to the immediate collapse of the feudal manorial system and total urbanization",
            "They caused widespread agricultural inflation that bankrupted the English monarchy",
            "They forced European monarchs to abandon mercantilist economic controls in favor of free trade"
        ],
        "answer": 0,
        "explanation": "New World crops such as maize, potatoes, and manioc yielded far higher caloric returns per acre than traditional Old World grains (wheat and rye). Their adoption enriched European diets, alleviated periodic famines, and stimulated long-term European demographic expansion.",
        "citation": "College Board AP® U.S. History CED — Unit 1: Topic 1.4 Columbian Exchange"
    },
    {
        "id": "ap-ush-005",
        "type": "mcq",
        "subtopic": "Spanish Casta System (Period 1: 1491–1607)",
        "difficulty": "Medium",
        "question": "The development of the Spanish colonial 'Casta' system in the Americas was primarily a response to which of the following historical conditions?",
        "options": [
            "The extensive intermarriage and racial mixing (mestizaje) among Spanish settlers, indigenous populations, and enslaved Africans",
            "The strict prohibition of intermarriage enforced by the Catholic Inquisition",
            "The demographic parity between European women and male conquistadors",
            "The emergence of democratic representative legislatures modeled on English town meetings"
        ],
        "answer": 0,
        "explanation": "Because few Spanish women migrated to the Americas initially, male conquistadors and colonists intermarried with indigenous women and enslaved Africans. To maintain elite peninsulare control, the Spanish crown institutionalized the Casta system, a racial hierarchy granting legal and social privileges based on racial ancestry.",
        "citation": "College Board AP® U.S. History CED — Unit 1: Topic 1.5 Labor, Slavery, and Caste in the Spanish Colonial System"
    },
    {
        "id": "ap-ush-006",
        "type": "mcq",
        "subtopic": "Pueblo Revolt of 1680 (Period 2: 1607–1754)",
        "difficulty": "Hard",
        "question": "“The Indians were so incensed against the religious and the Spaniards that they said the God of the priests had died and that their ancient gods were resurrected... They burned the temples, broke up the bells, and profaned the vessels and ornaments of the Church.”\n— Fray Angelico Chavez, Account of the Pueblo Revolt, 1680\n\nWhich of the following was a direct long-term consequence of the Pueblo Revolt described in the excerpt?",
        "options": [
            "When the Spanish reconquered New Mexico in 1692, they adopted a more accommodating approach to Pueblo religious practices and reduced forced labor demands",
            "The Pueblo completely expelled all European settlers from North America permanently",
            "The English crown assumed direct governing control over the Southwestern borderlands",
            "The Spanish replaced all Franciscan friars with French Jesuit missionaries"
        ],
        "answer": 0,
        "explanation": "Led by Popé in 1680, the Pueblo Revolt temporarily expelled the Spanish from New Mexico. When Spain reconquered the region in 1692, colonial officials learned from the uprising: they eliminated the harsh encomienda system, allocated communal lands, and tolerated traditional Pueblo religious rituals alongside Catholicism.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.5 Interactions Between American Indians and Europeans"
    },
    {
        "id": "ap-ush-007",
        "type": "mcq",
        "subtopic": "Chesapeake vs. New England Colonization (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "“For we must consider that we shall be as a city upon a hill. The eyes of all people are upon us. So that if we shall deal falsely with our God in this work we have undertaken, and so cause Him to withdraw His present help from us, we shall be made a story and a by-word through the world.”\n— John Winthrop, A Modell of Christian Charity, 1630\n\nThe settlement pattern and social organization of the colony founded by John Winthrop contrasted most sharply with the Chesapeake colonies in which of the following ways?",
        "options": [
            "Winthrop's colony was founded by Puritans migrating as family units committed to tightly knit religious communities, whereas the early Chesapeake was settled predominantly by single young men seeking quick wealth",
            "Winthrop's colony relied on large plantation cash-crop agriculture powered by enslaved labor from its inception",
            "Winthrop's colony established total separation of church and state and practiced absolute religious tolerance",
            "The Chesapeake colonies were governed exclusively by direct democratic town hall meetings"
        ],
        "answer": 0,
        "explanation": "The Massachusetts Bay Colony (Puritans) migrated as multigenerational families with relatively balanced sex ratios, establishing compact, community-centered towns structured around meetinghouses and schools. The Chesapeake (Virginia/Maryland) was initially settled by single male indentured servants seeking quick profits through labor-intensive tobacco monoculture.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.3 The Regions of British Colonies"
    },
    {
        "id": "ap-ush-008",
        "type": "mcq",
        "subtopic": "Bacon's Rebellion (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "What was the most significant structural transition in the labor system of the Virginia colony following Bacon's Rebellion in 1676?",
        "options": [
            "Planters shifted reliance from white indentured servants to lifelong, racially hereditary enslaved Africans to minimize the threat of domestic rebellion",
            "The colonial assembly abolished all forms of unfree labor and established universal tenant farming",
            "Wealthy planters granted frontier lands and voting rights to all former indentured servants",
            "The Virginia Company replaced tobacco cultivation with industrial textile manufacturing"
        ],
        "answer": 0,
        "explanation": "Bacon's Rebellion united poor white indentured servants, landless freemen, and enslaved blacks against the planter aristocracy. Recognizing the danger of a growing class of disgruntled, landless former white servants, Virginia elites turned decisively toward the transatlantic slave trade to secure a permanent, hereditary, and racially divided labor force.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.6 Slavery in the British Colonies"
    },
    {
        "id": "ap-ush-009",
        "type": "mcq",
        "subtopic": "Mercantilism & Navigation Acts (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "Under British mercantilist theory, the primary economic purpose of the North American colonies was to:",
        "options": [
            "Supply raw materials to the mother country and serve as an exclusive captive market for British manufactured goods",
            "Develop independent manufacturing centers that could undersell French and Dutch competitors",
            "Establish unrestricted free-trade zones with Spanish South America and the Caribbean",
            "Accumulate domestic paper currency reserves to stabilize colonial credit markets"
        ],
        "answer": 0,
        "explanation": "Mercantilism viewed global wealth as a zero-sum game measured in bullion. Great Britain enacted the Navigation Acts to ensure colonies provided valuable raw commodities (tobacco, sugar, timber, indigo) exclusively to England and consumed British manufactured goods, ensuring a favorable balance of trade.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.4 Transatlantic Trade"
    },
    {
        "id": "ap-ush-010",
        "type": "mcq",
        "subtopic": "Salutary Neglect (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "The British policy of 'salutary neglect' toward the American colonies before 1763 contributed most directly to:",
        "options": [
            "The growth of autonomous colonial legislative assemblies accustomed to self-taxation and self-governance",
            "The complete obedience of colonial merchants to imperial maritime navigation laws",
            "The elimination of smuggling and illicit transatlantic trade with French colonies",
            "The decline of democratic municipal assemblies such as New England town meetings"
        ],
        "answer": 0,
        "explanation": "During the era of salutary neglect under Prime Minister Robert Walpole, Britain loosely enforced trade regulations as long as colonies remained profitable. This allowed colonial assemblies (such as the Virginia House of Burgesses and Massachusetts General Court) to exercise the 'power of the purse' and develop strong traditions of local self-rule.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.4 Transatlantic Trade"
    },
    {
        "id": "ap-ush-011",
        "type": "mcq",
        "subtopic": "The First Great Awakening (Period 2: 1607–1754)",
        "difficulty": "Hard",
        "question": "“The God that holds you over the pit of hell, much as one holds a spider, or some loathsome insect over the fire, abhors you, and is dreadfully provoked: his wrath towards you burns like fire... and yet it is nothing but his hand that holds you from falling into the fire every moment.”\n— Jonathan Edwards, Sinners in the Hands of an Angry God, 1741\n\nWhich of the following was a major social or political consequence of the religious movement reflected in Edwards' sermon?",
        "options": [
            "It fostered a shared intercolonial cultural identity and democratized religious authority by challenging traditional clerical hierarchies",
            "It led to the establishment of the Church of England as the official state church across all thirteen colonies",
            "It completely eradicated sectarian divisions between Old Lights and New Lights in Massachusetts",
            "It inspired an immediate intercolonial boycott of British imports decades ahead of the Revolution"
        ],
        "answer": 0,
        "explanation": "The First Great Awakening (1730s–1740s) introduced an emotional, personal style of evangelical Christianity. By empowering ordinary believers to judge ministers ('New Lights' vs. 'Old Lights') and crossing colonial borders, it created a pan-colonial communications network and eroded deference to established religious and political authorities.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.7 Colonial Society and Culture"
    },
    {
        "id": "ap-ush-012",
        "type": "mcq",
        "subtopic": "Metacom's / King Philip's War (Period 2: 1607–1754)",
        "difficulty": "Hard",
        "question": "What was the most significant outcome of King Philip's War (1675–1676) for southern New England?",
        "options": [
            "It effectively shattered independent Native American resistance and opened vast tracts of southern New England lands to uninterrupted colonial settlement",
            "The Wampanoag successfully drove English settlers back into coastal port cities and secured permanent borders",
            "The British crown repealed the Massachusetts colonial charter and granted full voting rights to indigenous tribes",
            "The French military intervened directly to establish a permanent protectorate in Massachusetts Bay"
        ],
        "answer": 0,
        "explanation": "Proportionate to population, King Philip's War was one of the deadliest conflicts in American history. The defeat of Metacom's alliance and his death in 1676 broke the military capability of indigenous tribes in southern New England, leaving surviving native populations subject to colonial dominion or displacement.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.5 Interactions Between American Indians and Europeans"
    },
    {
        "id": "ap-ush-013",
        "type": "mcq",
        "subtopic": "Middle Colonies Diversity (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "The proprietary colony of Pennsylvania, founded by William Penn in 1681, differed from the Massachusetts Bay Colony primarily because Pennsylvania:",
        "options": [
            "Practiced broad religious toleration, embraced Quaker pacifism, and sought cooperative relations with local indigenous tribes",
            "Restricted the franchise and land ownership exclusively to members of the Anglican clergy",
            "Depended entirely on enslaved African labor to harvest staple export crops like rice and indigo",
            "Banned all European immigrants who were not of English or Welsh genealogical origin"
        ],
        "answer": 0,
        "explanation": "William Penn founded Pennsylvania as a 'Holy Experiment' rooted in Quaker beliefs in the Inner Light. Unlike Puritan Massachusetts, Pennsylvania offered freedom of worship, established amicable treaties with the Delaware (Lenape) Indians, and attracted a diverse influx of German, Scots-Irish, and Dutch immigrants.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.3 The Regions of British Colonies"
    },
    {
        "id": "ap-ush-014",
        "type": "mcq",
        "subtopic": "The Stono Rebellion (Period 2: 1607–1754)",
        "difficulty": "Hard",
        "question": "Which of the following was the most direct legislative reaction by colonial authorities to the Stono Rebellion of 1739 in South Carolina?",
        "options": [
            "The enactment of the Negro Act of 1740, which drastically tightened slave codes, banned assembly, and restricted slave literacy",
            "The abolition of the transatlantic slave trade into Charleston harbor",
            "The voluntary manumission of all enslaved laborers who fought against Spanish raiding parties",
            "The creation of an autonomous territory for free African Americans in the Carolina backcountry"
        ],
        "answer": 0,
        "explanation": "Following the Stono Rebellion—where about 100 enslaved people seized weapons and marched toward Spanish Florida—the South Carolina legislature enacted the repressive Negro Act of 1740. It curtailed enslaved people's freedom of movement, assembly, ability to grow food, and ability to learn to read and write.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.6 Slavery in the British Colonies"
    },
    {
        "id": "ap-ush-015",
        "type": "mcq",
        "subtopic": "Maryland Act of Toleration (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "The Maryland Toleration Act of 1649 was primarily designed to:",
        "options": [
            "Protect the religious freedom and political rights of Roman Catholic settlers against the growing Protestant majority",
            "Establish absolute freedom of conscience for all religions, including non-Christian faiths",
            "Prohibit the practice of Catholicism within the proprietary boundaries of Lord Baltimore",
            "Mandate the adoption of the Anglican Book of Common Prayer in all Maryland parishes"
        ],
        "answer": 0,
        "explanation": "Lord Baltimore established Maryland as a haven for English Catholics. As Protestant immigrants began outnumbering Catholics in the colony, the assembly passed the Maryland Act Concerning Religion (1649) to guarantee religious freedom to all Trinitarian Christians, shielding the Catholic minority from persecution.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.3 The Regions of British Colonies"
    },
    {
        "id": "ap-ush-016",
        "type": "mcq",
        "subtopic": "French Colonization Patterns (Period 1 & 2)",
        "difficulty": "Medium",
        "question": "In contrast to British colonial settlements in North America, French colonization along the St. Lawrence River and Great Lakes was characterized by:",
        "options": [
            "Smaller settler populations centered on the fur trade and extensive diplomatic and trade alliances with indigenous nations",
            "Massive waves of family-based agricultural settlement that displaced local tribes",
            "The rapid establishment of large-scale tobacco plantations dependent on indentured servitude",
            "Strict non-engagement with native cultures and total avoidance of intermarriage"
        ],
        "answer": 0,
        "explanation": "New France sent relatively few permanent colonists. French Jesuit missionaries and fur traders (coureurs des bois) relied on extensive alliances, reciprocity, and intermarriage with Algonquin and Huron peoples to dominate the continental fur trade.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.2 European Colonization"
    },
    {
        "id": "ap-ush-017",
        "type": "mcq",
        "subtopic": "Colonial Press & Free Speech (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "The landmark 1735 New York trial of John Peter Zenger was historically significant because it:",
        "options": [
            "Established the principle that truth was a valid defense against libel charges, laying groundwork for freedom of the press",
            "Outlawed royal governors from issuing executive decrees without legislative consent",
            "Granted women and propertyless men the right to serve as jurors in colonial courts",
            "Ruled that colonial laws superseded acts of the British Parliament"
        ],
        "answer": 0,
        "explanation": "Zenger was prosecuted for seditious libel for criticizing Royal Governor William Cosby. Defended by Andrew Hamilton, the jury acquitted Zenger on the grounds that his published criticisms were factually true, establishing an enduring precedent for American freedom of the press.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.7 Colonial Society and Culture"
    },
    {
        "id": "ap-ush-018",
        "type": "mcq",
        "subtopic": "The Enlightenment in America (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "John Locke's Two Treatises of Government (1689) influenced colonial American political philosophy primarily through its articulation of:",
        "options": [
            "Natural rights to life, liberty, and property, and the concept that governments derive authority from the consent of the governed",
            "The divine right of kings as the sole guarantor of civil order and religious uniformity",
            "The economic necessity of bullion hoarding to sustain a powerful standing national army",
            "The absolute supremacy of parliamentary mandates over local colonial town charters"
        ],
        "answer": 0,
        "explanation": "Locke's social contract theory held that individuals possess inherent natural rights (life, liberty, property) and form governments to safeguard these rights. If government fails to protect them, citizens retain the right to alter or overthrow it—ideas that heavily influenced Benjamin Franklin, Thomas Jefferson, and the American Revolution.",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.7 Colonial Society and Culture"
    },
    {
        "id": "ap-ush-019",
        "type": "mcq",
        "subtopic": "Transatlantic Slave Trade & Middle Passage (Period 2: 1607–1754)",
        "difficulty": "Medium",
        "question": "Which of the following commodities formed the foundation of the triangular trade connecting New England, the West Indies, and West Africa?",
        "options": [
            "New England rum traded for enslaved Africans, who were transported to the Caribbean and exchanged for molasses and sugar",
            "Chesapeake tobacco shipped directly to West Africa in exchange for manufactured textiles",
            "Pennsylvania grain traded to Spain in exchange for silver bullion sent to New England",
            "Carolina indigo exchanged in London for tea shipped directly to Boston"
        ],
        "answer": 0,
        "explanation": "The classic triangular trade route linked New England (which distilled rum from Caribbean molasses), West Africa (where rum and manufactured goods were traded for captured Africans), and the West Indies (where enslaved survivors of the Middle Passage were sold to sugar plantations).",
        "citation": "College Board AP® U.S. History CED — Unit 2: Topic 2.4 Transatlantic Trade"
    },
    {
        "id": "ap-ush-020",
        "type": "mcq",
        "subtopic": "Pre-Columbian Native Environments (Period 1: 1491–1607)",
        "difficulty": "Medium",
        "question": "Before European contact, indigenous societies in the Great Plains, such as the Arapaho and Cheyenne, adapted to their arid environment primarily by:",
        "options": [
            "Practicing mobile, nomadic hunter-gatherer lifeways centered on following migratory bison herds",
            "Constructing complex multi-story cliff dwellings with extensive canal irrigation systems",
            "Establishing permanent urban ceremonial mounds such as Cahokia",
            "Relying exclusively on deep-sea whaling and cedar totem craftsmanship"
        ],
        "answer": 0,
        "explanation": "In the vast, semi-arid grasslands of the Great Plains, Native groups organized mobile hunting bands that followed bison migrations. Cliff dwellings with irrigation belonged to the Southwest (Pueblo/Anasazi), ceremonial mounds to the Mississippi Valley (Cahokia), and whaling/totems to the Pacific Northwest (Chinook).",
        "citation": "College Board AP® U.S. History CED — Unit 1: Topic 1.2 Native American Societies Before European Contact"
    }
]

# -------------------------------------------------------------
# SET 2: Periods 3 & 4 (1754–1848) — 20 Questions
# -------------------------------------------------------------
set2_questions = [
    {
        "id": "ap-ush-021",
        "type": "mcq",
        "subtopic": "The French and Indian War (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "What was the most significant geopolitical transformation in North America resulting from the Treaty of Paris of 1763?",
        "options": [
            "France ceded all of its mainland North American territorial claims east of the Mississippi River to Great Britain",
            "Spain surrendered all of its Caribbean and South American holdings to the British Empire",
            "The British crown granted complete independence and sovereign neutrality to the Iroquois Confederacy",
            "The American colonies were granted direct representation in the British House of Commons"
        ],
        "answer": 0,
        "explanation": "The Treaty of Paris (1763) ended the French and Indian War (Seven Years' War). France was virtually driven from the mainland of North America, ceding Canada and all lands east of the Mississippi to Great Britain, and Louisiana west of the Mississippi to Spain.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.2 The Seven Years' War (The French and Indian War)"
    },
    {
        "id": "ap-ush-022",
        "type": "mcq",
        "subtopic": "Proclamation of 1763 & Stamp Act (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "“And we do hereby strictly forbid, on Pain of our Displeasure, all our loving Subjects from making any Purchases or Settlements whatever, or taking Possession of any of the Lands above reserved, without our especial leave and licence...”\n— King George III, Royal Proclamation of 1763\n\nThe British crown issued the proclamation excerpted above primarily to:",
        "options": [
            "Prevent costly and violent clashes between westward-moving colonial settlers and Native American tribes (such as Pontiac's War)",
            "Reserve the Ohio River Valley exclusively for French Roman Catholic fur-trading corporations",
            "Punish Massachusetts merchants for smuggling molasses into Boston harbor",
            "Force colonists to relocate into industrial manufacturing centers along the Atlantic seaboard"
        ],
        "answer": 0,
        "explanation": "Following Pontiac's Rebellion in 1763, the British government sought to stabilize the western frontier and avoid expensive military engagements by barring colonists from settling west of the Appalachian Mountains, deeply angering land speculators and frontier farmers.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.3 Taxation Without Representation"
    },
    {
        "id": "ap-ush-023",
        "type": "mcq",
        "subtopic": "Stamp Act Crisis & Resistance (Period 3: 1754–1800)",
        "difficulty": "Hard",
        "question": "Colonial opposition to the Stamp Act of 1765 focused primarily on which constitutional principle?",
        "options": [
            "Parliament had no legitimate constitutional authority to impose internal taxes on colonies that had no actual direct representation in Westminster",
            "The crown had no authority to collect external duties regulating transatlantic maritime commerce",
            "Colonial assemblies possessed the legal power to veto imperial declarations of foreign war",
            "All taxation violated the English common law tradition and the Magna Carta"
        ],
        "answer": 0,
        "explanation": "Colonists distinguished between external taxes (mercantilist tariffs to regulate imperial trade) and internal taxes (like the Stamp Act, levying taxes directly on internal paper transactions). Led by figures like Patrick Henry and the Stamp Act Congress, they argued 'No taxation without representation.'",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.3 Taxation Without Representation"
    },
    {
        "id": "ap-ush-024",
        "type": "mcq",
        "subtopic": "Common Sense & Ideology (Period 3: 1754–1800)",
        "difficulty": "Easy",
        "question": "“A government of our own is our natural right: And when a man reflects on the precariousness of human affairs, he will become convinced, that it is infinitely wiser and safer, to form a constitution of our own in a cool deliberate manner... than to trust such an interesting event to time and chance.”\n— Thomas Paine, Common Sense, January 1776\n\nThomas Paine's pamphlet Common Sense was uniquely influential in the colonies because it:",
        "options": [
            "Used plain, accessible language and biblical allegories to persuade ordinary colonists that complete independence from monarchy was both rational and inevitable",
            "Proposed a compromise restoring colonial dominion under a reformed British Board of Trade",
            "Argued that the colonies should seek military integration into the Spanish Empire",
            "Advocated for the establishment of an American hereditary aristocracy"
        ],
        "answer": 0,
        "explanation": "Paine avoided dense Latinate legal prose and spoke plainly to the common farmer and artisan. He attacked the institution of hereditary monarchy itself (calling George III the 'Royal Brute of Great Britain') and made a compelling moral and practical case for immediate American independence.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.4 Philosophical Foundations of the American Revolution"
    },
    {
        "id": "ap-ush-025",
        "type": "mcq",
        "subtopic": "The American Revolutionary War (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "The Battle of Saratoga (1777) is widely regarded by historians as the turning point of the American Revolutionary War because it:",
        "options": [
            "Convinced the French monarchy to enter into a formal diplomatic and military alliance with the United States",
            "Forced the immediate British surrender of their primary naval base at New York Harbor",
            "Led to the immediate capture and trial of British General Lord Cornwallis",
            "Caused the British Parliament to unilaterally repeal the Declaration of Independence"
        ],
        "answer": 0,
        "explanation": "American victory over General Burgoyne at Saratoga demonstrated that the Continental Army could defeat a major British force in open field combat. This gave Benjamin Franklin the diplomatic leverage needed to negotiate the Franco-American Alliance of 1778, securing French naval, financial, and troops support.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.5 The American Revolution"
    },
    {
        "id": "ap-ush-026",
        "type": "mcq",
        "subtopic": "Articles of Confederation & Shays' Rebellion (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "Which of the following events most directly convinced national political leaders such as Alexander Hamilton and James Madison that the Articles of Confederation needed urgent constitutional revision?",
        "options": [
            "Shays' Rebellion (1786–1787) in western Massachusetts, which exposed the central government's inability to maintain domestic order or levy taxes",
            "The Whiskey Rebellion in western Pennsylvania against federal excise taxes",
            "The Hartford Convention's declaration opposing the War of 1812",
            "The Nullification Crisis in South Carolina over federal protective tariffs"
        ],
        "answer": 0,
        "explanation": "Shays' Rebellion—an armed revolt of debt-ridden Massachusetts farmers shut down courts to prevent farm foreclosures—showed that the Confederation Congress lacked the authority to maintain an army or assist states during domestic insurrection, spurring calls for the 1787 Constitutional Convention in Philadelphia.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.7 The Articles of Confederation"
    },
    {
        "id": "ap-ush-027",
        "type": "mcq",
        "subtopic": "Northwest Ordinance of 1787 (Period 3: 1754–1800)",
        "difficulty": "Hard",
        "question": "The Northwest Ordinance of 1787 was one of the most enduring legislative achievements of the Confederation Congress because it:",
        "options": [
            "Established a structured pathway for newly settled territories to enter the Union as equal states and prohibited slavery in the Northwest Territory",
            "Allowed individual states to annex western lands without federal approval",
            "Permanently recognized indigenous territorial sovereignty across the entire Ohio Valley",
            "Granted women the right to vote in all newly organized territorial elections"
        ],
        "answer": 0,
        "explanation": "The Northwest Ordinance established that territories would transition through stages of self-government until achieving statehood on an equal footing with existing states. Crucially, Article VI prohibited slavery north of the Ohio River, establishing an important precedent for federal regulation of slavery in territories.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.7 The Articles of Confederation"
    },
    {
        "id": "ap-ush-028",
        "type": "mcq",
        "subtopic": "The Great Compromise (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "At the Constitutional Convention of 1787, the Connecticut (Great) Compromise resolved the bitter impasse between large and small population states by creating:",
        "options": [
            "A bicameral national legislature with equal state representation in the Senate and population-proportional representation in the House of Representatives",
            "A single executive chosen directly by a popular majority vote across all states",
            "A unicameral legislature where each state delegation possessed exactly one collective vote",
            "A system in which state supreme courts held the power of judicial review over federal laws"
        ],
        "answer": 0,
        "explanation": "Roger Sherman's Connecticut Compromise blended the Virginia Plan (proportional representation favored by populous states) and the New Jersey Plan (equal representation favored by small states), establishing a bicameral Congress consisting of the Senate (2 senators per state) and the House of Representatives (based on population).",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.8 The Constitutional Convention and Debates over Ratification"
    },
    {
        "id": "ap-ush-029",
        "type": "mcq",
        "subtopic": "Federalist No. 10 & Republicanism (Period 3: 1754–1800)",
        "difficulty": "Hard",
        "question": "“Among the numerous advantages promised by a well constructed Union, none deserves to be more accurately developed than its tendency to break and control the violence of faction... Extend the sphere, and you take in a greater variety of parties and interests; you make it less probable that a majority of the whole will have a common motive to invade the rights of other citizens...”\n— James Madison, The Federalist No. 10, 1787\n\nIn the excerpt, Madison refutes which classical political assumption held by Anti-Federalists?",
        "options": [
            "The belief that stable republican liberty could only survive within small, homogeneous geographic polities",
            "The belief that a powerful standing army was essential for defending civil liberties",
            "The idea that checks and balances between branches were unnecessary in a republic",
            "The belief that pure direct democracy was preferable to representative government"
        ],
        "answer": 0,
        "explanation": "Anti-Federalists, drawing on Montesquieu, argued that republics could only endure in small, culturally homogeneous societies. In Federalist No. 10, Madison brilliantly turned this on its head, arguing that an 'extended republic' with numerous competing factions prevented any single majority faction from tyrannizing the minority.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.8 The Constitutional Convention and Debates over Ratification"
    },
    {
        "id": "ap-ush-030",
        "type": "mcq",
        "subtopic": "Washington's Farewell Address (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "“The great rule of conduct for us in regard to foreign nations is in extending our commercial relations to have with them as little political connection as possible... It is our true policy to steer clear of permanent alliances with any portion of the foreign world.”\n— George Washington, Farewell Address, 1796\n\nPresident Washington's advice in the excerpt was primarily motivated by his desire to:",
        "options": [
            "Protect the young, economically vulnerable United States from becoming entangled in destructive European conflicts between Britain and revolutionary France",
            "Encourage the immediate territorial conquest of Spanish Florida and British Canada",
            "Prevent American merchants from conducting commercial trade across the Atlantic Ocean",
            "Force the United States to join the Holy Alliance of European monarchies"
        ],
        "answer": 0,
        "explanation": "Washington issued his 1793 Proclamation of Neutrality and reiterated in his 1796 Farewell Address that the fragile American republic needed decades of peace to consolidate its institutions, economy, and military before becoming drawn into European wars.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.10 Shaping a New Republic"
    },
    {
        "id": "ap-ush-031",
        "type": "mcq",
        "subtopic": "Hamilton vs. Jefferson (Period 3: 1754–1800)",
        "difficulty": "Medium",
        "question": "The constitutional debate between Alexander Hamilton and Thomas Jefferson over the creation of the First Bank of the United States in 1791 centered on:",
        "options": [
            "Whether Congress could exercise implied powers under the 'necessary and proper' clause, or whether it was strictly limited to enumerated powers",
            "Whether the federal capital should be moved permanently to Philadelphia or New York",
            "Whether individual states possessed the authority to print their own international gold currency",
            "Whether the Supreme Court had the constitutional power to appoint Treasury cabinet secretaries"
        ],
        "answer": 0,
        "explanation": "Jefferson argued for 'strict construction'—the Constitution did not explicitly grant Congress power to charter a bank. Hamilton argued for 'loose construction'—the 'elastic clause' (Article I, Section 8) gave Congress implied powers to establish a bank to carry out enumerated fiscal duties (tax collection, borrowing, defense).",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.10 Shaping a New Republic"
    },
    {
        "id": "ap-ush-032",
        "type": "mcq",
        "subtopic": "Alien & Sedition Acts / Kentucky Resolutions (Period 3: 1754–1800)",
        "difficulty": "Hard",
        "question": "The Virginia and Kentucky Resolutions of 1798, authored secretly by James Madison and Thomas Jefferson, asserted that:",
        "options": [
            "Individual states had entered into a compact to form the Union and possessed the authority to nullify federal laws deemed unconstitutional",
            "The President possessed emergency wartime authority to suspend the writ of habeas corpus indefinitely",
            "The Supreme Court had sole jurisdiction to determine the constitutional boundaries of free speech",
            "Immigrants from European nations should be permanently barred from naturalized citizenship"
        ],
        "answer": 0,
        "explanation": "Passed in response to the Federalist Alien and Sedition Acts, the Kentucky and Virginia Resolutions articulated the 'compact theory' of the Constitution, arguing that states formed the federal government and had the inherent right to judge and nullify unconstitutional federal overreach—a doctrine later invoked by Southern secessionists.",
        "citation": "College Board AP® U.S. History CED — Unit 3: Topic 3.11 Developing an American Identity"
    },
    {
        "id": "ap-ush-033",
        "type": "mcq",
        "subtopic": "Marbury v. Madison (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "The landmark Supreme Court ruling in Marbury v. Madison (1803), written by Chief Justice John Marshall, was foundational to the American constitutional order because it established:",
        "options": [
            "The principle of judicial review, establishing the Supreme Court's authority to declare acts of Congress unconstitutional",
            "The absolute supremacy of state legislation over federal judicial mandates",
            "The doctrine of executive privilege during congressional investigations",
            "The right of the President to remove federal judges without Senate confirmation"
        ],
        "answer": 0,
        "explanation": "Chief Justice John Marshall struck down Section 13 of the Judiciary Act of 1789 as unconstitutional, establishing that the Supreme Court possesses the definitive authority to review legislative acts and nullify statutes that conflict with the U.S. Constitution (judicial review).",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.2 The Rise of Political Parties and the Era of Jefferson"
    },
    {
        "id": "ap-ush-034",
        "type": "mcq",
        "subtopic": "The Louisiana Purchase (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "President Thomas Jefferson experienced significant personal philosophical conflict regarding the Louisiana Purchase (1803) because:",
        "options": [
            "As a strict constructionist, he recognized that the Constitution did not explicitly grant the executive the power to purchase foreign territory",
            "He believed the purchase would permanently impoverish American agricultural exports",
            "He was committed to an alliance with Great Britain against Napoleonic France",
            "He believed the Rocky Mountains were uninhabitable by agrarian republican farmers"
        ],
        "answer": 0,
        "explanation": "Jefferson had consistently advocated for strict interpretation of the Constitution, which contained no specific clause authorizing treaties to buy land from foreign nations. However, recognizing the enormous strategic and economic benefits of securing New Orleans and doubling the size of the nation, he pragmatically utilized the presidential treaty-making power.",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.2 The Rise of Political Parties and the Era of Jefferson"
    },
    {
        "id": "ap-ush-035",
        "type": "mcq",
        "subtopic": "The Monroe Doctrine (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "“The American continents, by the free and independent condition which they have assumed and maintain, are henceforth not to be considered as subjects for future colonization by any European powers...”\n— President James Monroe, Annual Message to Congress, December 1823\n\nThe Monroe Doctrine declared which of the following core foreign policy positions?",
        "options": [
            "The Western Hemisphere was closed to future European colonization, and European intervention in independent American nations would be viewed as an act of hostility",
            "The United States pledged to militarily assist European monarchies in reconquering former South American colonies",
            "The United States claimed imperial sovereignty over all Latin American nations",
            "The United States would unilaterally annex Cuba and Central America"
        ],
        "answer": 0,
        "explanation": "Drafted largely by Secretary of State John Quincy Adams, the Monroe Doctrine warned European powers against establishing new colonies or attempting to reassert control over newly independent Latin American republics, in exchange for American non-interference in existing European colonies and wars.",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.4 America on the World Stage"
    },
    {
        "id": "ap-ush-036",
        "type": "mcq",
        "subtopic": "The Market Revolution (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "Which of the following technological and infrastructural developments contributed most directly to the Market Revolution of the early nineteenth century?",
        "options": [
            "The construction of internal canals (such as the Erie Canal), steamboats, and early railroads linking western agricultural markets to eastern urban centers",
            "The widespread introduction of steam-powered combine harvesters across the Great Plains",
            "The laying of the transatlantic telegraph cable connecting New York directly to London",
            "The federal government's total nationalization of interstate turnpikes and river navigation"
        ],
        "answer": 0,
        "explanation": "The Market Revolution transformed the US economy from local subsistence farming into a national commercial market network. The opening of the Erie Canal (1825), Robert Fulton's steamboat, turnpikes, and early railroads drastically slashed transportation freight costs, connecting Midwestern farms to northeastern cities.",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.5 Market Revolution: Industrialization"
    },
    {
        "id": "ap-ush-037",
        "type": "mcq",
        "subtopic": "The Missouri Compromise (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "Under the terms of the Missouri Compromise of 1820, orchestrated by Henry Clay:",
        "options": [
            "Missouri was admitted as a slave state, Maine was admitted as a free state, and slavery was prohibited in the Louisiana Territory north of latitude 36°30'",
            "Slavery was banned in all territories acquired from Mexico",
            "Popular sovereignty was established to determine slavery in all western territories",
            "A national referendum was scheduled to decide the emancipation of enslaved laborers"
        ],
        "answer": 0,
        "explanation": "To preserve the delicate 11-to-11 Senate balance between free and slave states, Henry Clay crafted the Missouri Compromise: Maine entered as a free state, Missouri as a slave state, and all remaining Louisiana Purchase territory north of 36°30' north latitude was closed to slavery.",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.3 Politics and Regional Interests"
    },
    {
        "id": "ap-ush-038",
        "type": "mcq",
        "subtopic": "Jacksonian Democracy & Indian Removal (Period 4: 1800–1848)",
        "difficulty": "Hard",
        "question": "How did President Andrew Jackson respond to Chief Justice John Marshall's Supreme Court ruling in Worcester v. Georgia (1832), which recognized Cherokee sovereignty over their ancestral lands?",
        "options": [
            "He refused to enforce the Supreme Court decision, facilitating the state of Georgia's dispossession of the Cherokee and the subsequent 'Trail of Tears'",
            "He deployed federal troops to Georgia to arrest state officials who violated Cherokee rights",
            "He negotiated an amendment to the U.S. Constitution granting Native Americans full citizenship",
            "He petitioned Congress to impeach Chief Justice John Marshall for judicial overreach"
        ],
        "answer": 0,
        "explanation": "In Worcester v. Georgia (1832), Marshall ruled that Georgia state laws had no force on sovereign Cherokee lands. Andrew Jackson famously disregarded the ruling ('John Marshall has made his decision; now let him enforce it'), paving the way for the forced removal of thousands of Cherokee along the Trail of Tears (1838–1839).",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.8 Jackson and Federal Power"
    },
    {
        "id": "ap-ush-039",
        "type": "mcq",
        "subtopic": "The Second Great Awakening & Reform (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "The Second Great Awakening sparked numerous social reform movements in the 1830s and 1840s primarily through its theological emphasis on:",
        "options": [
            "Moral perfectionism and the individual duty to actively eradicate societal sins, including alcohol abuse and human enslavement",
            "Strict Calvinist predestination that discouraged human attempts to reform social institutions",
            "The unquestioned subordination of women to male religious and legal authorities",
            "The separation of moral principles from civic and political participation"
        ],
        "answer": 0,
        "explanation": "Evangelical leaders like Charles Grandison Finney preached free will and moral perfectionism—the idea that individuals could achieve salvation and had a moral obligation to purge society of vices. This inspired an explosion of antebellum reform crusades: temperance, abolitionism, public asylum reform (Dorothea Dix), and women's rights.",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.10 The Second Great Awakening"
    },
    {
        "id": "ap-ush-040",
        "type": "mcq",
        "subtopic": "Seneca Falls Convention (Period 4: 1800–1848)",
        "difficulty": "Medium",
        "question": "“We hold these truths to be self-evident: that all men and women are created equal; that they are endowed by their Creator with certain inalienable rights; that among these are life, liberty, and the pursuit of happiness...”\n— Declaration of Sentiments, Seneca Falls Convention, 1848\n\nThe authors of the Declaration of Sentiments intentionally modeled their manifesto on the Declaration of Independence in order to:",
        "options": [
            "Highlight the stark contradiction between foundational American democratic ideals and the widespread legal disenfranchisement and subjugation of women",
            "Propose the immediate secession of northern women from the federal union",
            "Demand the establishment of a female monarchy to govern the United States",
            "Argue that women should abandon civic engagement to focus entirely on the domestic sphere"
        ],
        "answer": 0,
        "explanation": "Organized by Elizabeth Cady Stanton and Lucretia Mott in 1848, the Seneca Falls Convention used Jefferson's iconic prose to expose American hypocrisy: women paid taxes and obeyed laws yet were denied voting rights, property ownership upon marriage (coverture), and access to higher education and professions.",
        "citation": "College Board AP® U.S. History CED — Unit 4: Topic 4.11 An Expanding Democracy & Women's Rights"
    }
]

# -------------------------------------------------------------
# SET 3: Periods 5 & 6 (1844–1898) — 20 Questions
# -------------------------------------------------------------
set3_questions = [
    {
        "id": "ap-ush-041",
        "type": "mcq",
        "subtopic": "Manifest Destiny & Mexican-American War (Period 5: 1844–1877)",
        "difficulty": "Medium",
        "question": "The political slogan 'Fifty-Four Forty or Fight!' during the 1844 presidential election reflected:",
        "options": [
            "American expansionist demands for the entire Oregon Country up to the border with Russian Alaska",
            "The proposed latitude line separating slave and free territory in the Mexican Cession",
            "The total number of electoral votes needed to enact the annexation of Texas",
            "The boundary line established between the United States and Spanish Florida"
        ],
        "answer": 0,
        "explanation": "Democratic candidate James K. Polk capitalized on popular Manifest Destiny enthusiasm by demanding all of Oregon up to latitude 54°40'. Once in office, however, Polk compromised with Great Britain in the Oregon Treaty of 1846, dividing the territory peacefully at the 49th parallel to avoid a two-front war with Britain and Mexico.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.2 Manifest Destiny"
    },
    {
        "id": "ap-ush-042",
        "type": "mcq",
        "subtopic": "The Wilmot Proviso (Period 5: 1844–1877)",
        "difficulty": "Hard",
        "question": "Although it was never passed into law by the U.S. Senate, the Wilmot Proviso of 1846 escalated sectional tensions because it proposed to:",
        "options": [
            "Prohibit slavery in any territory acquired from the Republic of Mexico as a result of the Mexican-American War",
            "Extend the Missouri Compromise line 36°30' all the way to the Pacific Coast",
            "Immediately abolish slavery in the District of Columbia and border states",
            "Repeal the Fugitive Slave Clause of the United States Constitution"
        ],
        "answer": 0,
        "explanation": "David Wilmot attached a rider to a wartime appropriations bill proposing that slavery be banned in any land taken from Mexico. It passed the northern-dominated House repeatedly but stalled in the southern-balanced Senate, dividing political parties strictly along geographic rather than partisan lines.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.3 The Mexican-American War"
    },
    {
        "id": "ap-ush-043",
        "type": "mcq",
        "subtopic": "The Compromise of 1850 (Period 5: 1844–1877)",
        "difficulty": "Medium",
        "question": "Which component of the Compromise of 1850 provoked the fiercest moral outrage and widespread civil disobedience among northern abolitionists and moderates?",
        "options": [
            "A stringent new Fugitive Slave Law that required northern citizens to assist federal marshals in capturing accused runaway slaves and denied accused runaways a jury trial",
            "The admission of California into the Union as an unrestricted slave state",
            "The complete prohibition of all internal interstate slave trade between southern states",
            "The immediate annexation of Cuba as an American slave territory"
        ],
        "answer": 0,
        "explanation": "The Fugitive Slave Act of 1850 outraged Northerners because it federalized the slave-catching apparatus on free soil, denied accused fugitives habeas corpus and trial by jury, penalized citizens who harbored runaways, and spurred northern states to pass 'personal liberty laws'.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.4 The Compromise of 1850"
    },
    {
        "id": "ap-ush-044",
        "type": "mcq",
        "subtopic": "The Kansas-Nebraska Act (Period 5: 1844–1877)",
        "difficulty": "Hard",
        "question": "The Kansas-Nebraska Act of 1854, sponsored by Senator Stephen A. Douglas, fundamentally destabilized national politics because it:",
        "options": [
            "Effectively repealed the 1820 Missouri Compromise ban on slavery north of 36°30' by instituting popular sovereignty in the territories",
            "Declared that the federal government possessed no authority to construct a transcontinental railroad",
            "Unconditionally outlawed slavery throughout all western territories",
            "Permanently dissolved the United States Supreme Court"
        ],
        "answer": 0,
        "explanation": "To secure southern support for a northern transcontinental railroad route departing Chicago, Douglas organized Kansas and Nebraska under 'popular sovereignty'—allowing territorial voters to decide slavery for themselves. This repealed the Missouri Compromise of 1820, provoked 'Bleeding Kansas', and gave rise to the anti-slavery Republican Party.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.5 Sectional Conflict: Regional Differences"
    },
    {
        "id": "ap-ush-045",
        "type": "mcq",
        "subtopic": "Dred Scott v. Sandford (Period 5: 1844–1877)",
        "difficulty": "Hard",
        "question": "“They had for more than a century before been regarded as beings of an inferior order, and altogether unfit to associate with the white race... and so far inferior, that they had no rights which the white man was bound to respect...”\n— Chief Justice Roger B. Taney, Dred Scott v. Sandford, 1857\n\nIn addition to ruling that African Americans were not citizens, Chief Justice Taney's decision declared that:",
        "options": [
            "Congress had no constitutional power to ban slavery in federal territories, rendering the Missouri Compromise unconstitutional under the Fifth Amendment",
            "States had no legal authority to emancipate enslaved persons residing within their own borders",
            "Popular sovereignty was the sole constitutional method for settling territorial disputes",
            "Enslaved people automatically attained freedom if their enslavers transported them across international borders"
        ],
        "answer": 0,
        "explanation": "Taney ruled that Black Americans (free or enslaved) were not U.S. citizens and had no standing to sue in federal court. Furthermore, he ruled that the Fifth Amendment protected property rights, meaning Congress could not deprive slaveholders of their enslaved 'property' in territories, striking down the Missouri Compromise.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.6 Failure of Compromise"
    },
    {
        "id": "ap-ush-046",
        "type": "mcq",
        "subtopic": "Election of 1860 & Secession (Period 5: 1844–1877)",
        "difficulty": "Medium",
        "question": "The election of Abraham Lincoln to the presidency in November 1860 triggered South Carolina's immediate declaration of secession primarily because:",
        "options": [
            "Lincoln was elected on a Republican platform explicitly committed to halting the expansion of slavery into all federal territories, despite winning zero southern electoral votes",
            "Lincoln had promised in his campaign to immediately sign an executive order emancipating all southern slaves",
            "The Republican Party advocated for the total expulsion of southern states from the Union",
            "Lincoln vowed to impose a 100% export tariff on raw southern cotton shipped to Great Britain"
        ],
        "answer": 0,
        "explanation": "Lincoln won the presidency with a plurality of the popular vote and a clear majority in the Electoral College without carrying a single slave state. Southern slaveholding elites viewed the Republican 'free soil' platform as an existential threat to the long-term political survival and western spread of slavery.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.7 Election of 1860 and Secession"
    },
    {
        "id": "ap-ush-047",
        "type": "mcq",
        "subtopic": "The Emancipation Proclamation (Period 5: 1844–1877)",
        "difficulty": "Medium",
        "question": "President Abraham Lincoln issued the preliminary Emancipation Proclamation following the Battle of Antietam in September 1862. What was its most profound diplomatic effect?",
        "options": [
            "It transformed the Union war effort into an explicit moral crusade against slavery, making British or French diplomatic recognition of the Confederacy politically impossible",
            "It compelled the immediate surrender of Confederate forces stationed in Virginia",
            "It persuaded Confederate leaders to abolish slavery voluntarily in exchange for peace",
            "It led to the immediate military intervention of the Russian Empire on the Confederate side"
        ],
        "answer": 0,
        "explanation": "By linking the preservation of the Union directly to the abolition of slavery, Lincoln aligned the Union cause with the deeply anti-slavery working classes of Great Britain and France, ensuring European powers could not intervene to aid the Confederacy without defending human bondage.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.8 Military Conflict in the Civil War"
    },
    {
        "id": "ap-ush-048",
        "type": "mcq",
        "subtopic": "The Reconstruction Amendments (Period 5: 1844–1877)",
        "difficulty": "Medium",
        "question": "Which Reconstruction Amendment guaranteed birthright citizenship and prohibited states from denying any person 'due process of law' or 'the equal protection of the laws'?",
        "options": [
            "The Fourteenth Amendment",
            "The Thirteenth Amendment",
            "The Fifteenth Amendment",
            "The Sixteenth Amendment"
        ],
        "answer": 0,
        "explanation": "The Fourteenth Amendment (1868) directly overturned the Dred Scott ruling by establishing birthright citizenship. Its Due Process and Equal Protection clauses placed constitutional limitations on state actions, designed originally to dismantle southern 'Black Codes'.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.10 Reconstruction"
    },
    {
        "id": "ap-ush-049",
        "type": "mcq",
        "subtopic": "Sharecropping & Economic Realities (Period 5: 1844–1877)",
        "difficulty": "Medium",
        "question": "In the post-Civil War South, the system of sharecropping functioned primarily to:",
        "options": [
            "Keep freed African Americans and impoverished whites trapped in a cycle of perpetual debt and economic dependence on landowning elites",
            "Facilitate the rapid transition of former slaves into prosperous, debt-free landowning yeomen farmers",
            "Diversify the southern economy away from cotton and toward industrial automobile production",
            "Provide universal high-wage employment under strict federal military oversight"
        ],
        "answer": 0,
        "explanation": "Lacking capital and land, freedpeople exchanged their labor for a share of the crop. High interest rates charged by local merchants for tools, seed, and provisions under the 'crop-lien' system meant that sharecroppers rarely generated a surplus, tying them to the land in an inescapable cycle of debt peonage.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.10 Reconstruction"
    },
    {
        "id": "ap-ush-050",
        "type": "mcq",
        "subtopic": "The Compromise of 1877 (Period 5: 1844–1877)",
        "difficulty": "Hard",
        "question": "The Compromise of 1877 effectively brought an end to Radical Reconstruction primarily through which political agreement?",
        "options": [
            "Southern Democrats consented to the certification of Republican Rutherford B. Hayes as president in exchange for the withdrawal of remaining federal troops from the South",
            "Republicans agreed to repeal the 13th, 14th, and 15th Amendments in their entirety",
            "Federal authorities recognized the Confederate debt as a national liability",
            "The Supreme Court declared the Reconstruction Acts unconstitutional"
        ],
        "answer": 0,
        "explanation": "Following the disputed 1876 presidential election between Hayes and Samuel Tilden, an informal bipartisan deal gave Hayes the contested electoral votes. In return, Hayes withdrew federal troops from South Carolina and Louisiana, allowing white 'Redeemer' Democrats to reclaim state governments and establish Jim Crow regimes.",
        "citation": "College Board AP® U.S. History CED — Unit 5: Topic 5.11 Failure of Reconstruction"
    },
    {
        "id": "ap-ush-051",
        "type": "mcq",
        "subtopic": "Gilded Age Industrialization (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "Andrew Carnegie's business strategy of 'vertical integration' in the steel industry involved:",
        "options": [
            "Controlling every phase of the manufacturing process from iron ore mining and railroad transportation to steel smelting and finished distribution",
            "Forming secret collusive pools with competing steel manufacturers to fix consumer market prices",
            "Buying up and merging with all horizontal competitor steel mills across Pennsylvania",
            "Relying exclusively on municipal contracts and federal steel subsidies"
        ],
        "answer": 0,
        "explanation": "Vertical integration (pioneered by Carnegie Steel) consolidated control of all stages of production—from raw iron and coal extraction to rail transport and blast furnaces. This eliminated middlemen, cut costs, and achieved unmatched operational efficiencies.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.2 Westward Expansion: Economic Development"
    },
    {
        "id": "ap-ush-052",
        "type": "mcq",
        "subtopic": "The Dawes Severalty Act (Period 6: 1865–1898)",
        "difficulty": "Hard",
        "question": "The primary objective of the Dawes Severalty Act of 1887 was to:",
        "options": [
            "Assimilate Native Americans into mainstream white agrarian society by breaking up tribal communal lands into individual family allotments",
            "Recognize tribal reservations as sovereign, autonomous foreign nations exempt from federal law",
            "Restore ancestral lands in the Black Hills to the Lakota Sioux nation",
            "Fund the relocation of Native tribes into industrial urban centers in the Northeast"
        ],
        "answer": 0,
        "explanation": "Reflecting paternalistic assimilation policies, the Dawes Act broke up communal tribal lands into individual 160-acre parcels. Unallocated 'surplus' lands were sold off to white settlers and railroad corporations, resulting in Native Americans losing over 60% of their land base between 1887 and 1934.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.3 Westward Expansion: Social and Cultural Development"
    },
    {
        "id": "ap-ush-053",
        "type": "mcq",
        "subtopic": "Gospel of Wealth vs. Social Darwinism (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "“The man who dies leaving behind him millions of available wealth, which was his to administer during life, will pass away 'unwept, unhonored, and unsung'... The man of wealth thus becoming the mere agent and trustee for his poorer brethren...”\n— Andrew Carnegie, The Gospel of Wealth, 1889\n\nIn the excerpt, Andrew Carnegie argues that wealthy industrialists have a moral obligation to:",
        "options": [
            "Use their surplus personal fortunes for philanthropic projects that provide lasting opportunities for community self-improvement (such as libraries and universities)",
            "Distribute cash handouts equally to all factory workers through federal welfare offices",
            "Surrender their private corporations to state-managed trade unions",
            "Lobby the federal government to establish a 100% inheritance tax on large estates"
        ],
        "answer": 0,
        "explanation": "Carnegie's 'Gospel of Wealth' asserted that extreme inequality was an inevitable byproduct of industrial capitalism, but argued that wealthy tycoons should act as responsible 'trustees' of society by funding public institutions (e.g. over 2,500 public libraries, colleges, concert halls) to help the ambitious help themselves.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.6 The Rise of Industrial Capitalism"
    },
    {
        "id": "ap-ush-054",
        "type": "mcq",
        "subtopic": "Labor Movements: Haymarket to Pullman (Period 6: 1865–1898)",
        "difficulty": "Hard",
        "question": "The 1886 Haymarket Square Riot in Chicago damaged the mainstream labor movement primarily because it:",
        "options": [
            "Linked organized labor in the public mind with foreign anarchism and violent radicalism, precipitating the rapid decline of the Knights of Labor",
            "Resulted in the federal government nationalizing all privately owned rail networks",
            "Forced the American Federation of Labor to adopt Marxist revolutionary syndicalism",
            "Prompted the immediate outlawing of all peaceful assembly in urban centers"
        ],
        "answer": 0,
        "explanation": "During a labor rally in Chicago's Haymarket Square, a dynamite bomb exploded, killing police officers. Although the bomber was never identified, public backlash and media hysteria associated labor unions—particularly the inclusive Knights of Labor—with violent anarchism and terrorism, leading to the Knights' collapse.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.7 Labor in the Gilded Age"
    },
    {
        "id": "ap-ush-055",
        "type": "mcq",
        "subtopic": "Immigration & Urbanization (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "The 'New Immigrants' who arrived in the United States in massive numbers during the late nineteenth century differed from earlier waves of immigrants primarily because they:",
        "options": [
            "Originated predominantly from Southern and Eastern Europe (Italy, Poland, Russia, Greece) and were largely Catholic, Jewish, or Eastern Orthodox",
            "Migrated predominantly from Protestant countries in Northern and Western Europe with high levels of English fluency",
            "Settled almost exclusively on western homestead farms rather than northeastern urban industrial centers",
            "Arrived with substantial personal investment capital to launch small manufacturing enterprises"
        ],
        "answer": 0,
        "explanation": "Unlike the 'Old Immigrants' (Irish, Germans, British, Scandinavians) of the 1840s–1870s, the 'New Immigrants' of 1880–1920 came from Southern and Eastern Europe. They were culturally, linguistically, and religiously distinct, settled heavily in industrial cities, and faced intense nativist backlash.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.8 Immigration and Migration in the Gilded Age"
    },
    {
        "id": "ap-ush-056",
        "type": "mcq",
        "subtopic": "Plessy v. Ferguson & Jim Crow (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "The Supreme Court's landmark decision in Plessy v. Ferguson (1896) had what profound impact on American racial jurisprudence?",
        "options": [
            "It established the legal doctrine of 'separate but equal', constitutionally sanctioning state-mandated racial segregation across the South",
            "It overturned all southern state poll taxes and grandfather clauses",
            "It declared that the Fourteenth Amendment applied exclusively to federal territories",
            "It mandated the racial integration of all interstate railway passenger cars"
        ],
        "answer": 0,
        "explanation": "In an 8–1 decision (with Justice John Marshall Harlan dissenting), the Supreme Court ruled that state laws requiring racial segregation in public facilities did not violate the Fourteenth Amendment's Equal Protection Clause as long as facilities were 'equal', legally legitimizing Jim Crow segregation.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.13 Continuity and Change in the Gilded Age"
    },
    {
        "id": "ap-ush-057",
        "type": "mcq",
        "subtopic": "The Populist (People's) Party (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "The Omaha Platform of 1892 established the Populist Party's reform agenda, which included which of the following central economic demands?",
        "options": [
            "The unlimited, free coinage of silver at a 16-to-1 ratio, government ownership of railroads and telegraphs, and a graduated income tax",
            "A strict return to a pure international gold standard and the deregulation of interstate freight rates",
            "The privatization of federal postal delivery systems and the elimination of greenbacks",
            "The abolition of the direct election of United States Senators"
        ],
        "answer": 0,
        "explanation": "The Populists (representing struggling agrarian farmers suffering from debt and deflation) sought bimetallism ('Free Silver') to inflate the currency supply and raise crop prices, along with nationalization of railroads to stop extortionate shipping rates, a graduated income tax, and direct election of senators.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.12 The Rise of the Populist Party"
    },
    {
        "id": "ap-ush-058",
        "type": "mcq",
        "subtopic": "Cross of Gold & 1896 Election (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "“Having behind us the producing masses of this nation and the world... we will answer their demand for a gold standard by saying to them: You shall not press down upon the brow of labor this crown of thorns; you shall not crucify mankind upon a cross of gold.”\n— William Jennings Bryan, Democratic National Convention Speech, 1896\n\nIn the speech excerpted above, Bryan was advocating for:",
        "options": [
            "Free and unlimited coinage of silver to ease the debt burden on working farmers and industrial laborers",
            "The immediate elimination of all paper currency in favor of British gold sovereigns",
            "The establishment of a high protective tariff on European grain imports",
            "The dissolution of all private commercial banks in the United States"
        ],
        "answer": 0,
        "explanation": "Bryan's electrifying 'Cross of Gold' speech won him the 1896 Democratic nomination (and Populist endorsement). He attacked the rigid gold standard as an instrument of eastern banking elites that crushed debt-strapped farmers and laborers through deflation.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.12 The Rise of the Populist Party"
    },
    {
        "id": "ap-ush-059",
        "type": "mcq",
        "subtopic": "Jane Addams & Settlement Houses (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "Jane Addams' Hull House in Chicago was emblematic of the Settlement House Movement because it:",
        "options": [
            "Provided direct social services, English language instruction, daycare, and vocational training to poor immigrant working-class families in urban slums",
            "Functioned as an undercover political headquarters for the Tammany Hall political machine",
            "Operated exclusively as an evangelical church focused on overseas Christian proselytizing",
            "Advocated for the immediate cessation of all European immigration into the United States"
        ],
        "answer": 0,
        "explanation": "Jane Addams and Ellen Gates Starr founded Hull House in 1889. Educated middle-class reformers lived in working-class immigrant neighborhoods, offering kindergarten, adult classes, cultural events, and health clinics, while gathering sociology data to advocate for child labor and sanitation laws.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.9 Responses to Immigration in the Gilded Age"
    },
    {
        "id": "ap-ush-060",
        "type": "mcq",
        "subtopic": "The Social Gospel Movement (Period 6: 1865–1898)",
        "difficulty": "Medium",
        "question": "The Social Gospel movement of the late nineteenth century, championed by ministers like Walter Rauschenbusch, urged Christians to:",
        "options": [
            "Apply Christian ethical teachings directly to social problems such as poverty, slum housing, income inequality, and child labor",
            "Focus exclusively on personal spiritual salvation while withdrawing completely from political and civic life",
            "Embrace Social Darwinist theories that justified the exploitation of impoverished workers as natural selection",
            "Endorse monopolies and corporate trusts as divine manifestations of providential favor"
        ],
        "answer": 0,
        "explanation": "The Social Gospel movement insisted that true Christianity required reforming social structures and addressing Gilded Age social injustices (slums, unsafe factories, poverty, child labor). It provided an important moral foundation for early twentieth-century Progressivism.",
        "citation": "College Board AP® U.S. History CED — Unit 6: Topic 6.11 Social and Cultural Movements in the Gilded Age"
    }
]

# -------------------------------------------------------------
# SET 4: Periods 7 & 8 (1890–1980) — 20 Questions
# -------------------------------------------------------------
set4_questions = [
    {
        "id": "ap-ush-061",
        "type": "mcq",
        "subtopic": "American Imperialism & Spanish-American War (Period 7: 1890–1945)",
        "difficulty": "Medium",
        "question": "Which of the following was an immediate territorial outcome of the Spanish-American War under the 1898 Treaty of Paris?",
        "options": [
            "The United States acquired Puerto Rico, Guam, and the Philippines from Spain, while Cuba attained nominal independence subject to U.S. oversight",
            "The United States purchased Alaska and Hawaii directly from the Spanish crown",
            "Spain retained sovereignty over the Philippines in exchange for relinquishing all Caribbean claims",
            "The United States surrendered its naval claims in Guantanamo Bay"
        ],
        "answer": 0,
        "explanation": "The 'splendid little war' marked America's emergence as an overseas imperial power. Under the Treaty of Paris (1898), Spain ceded Puerto Rico, Guam, and sold the Philippines for $20 million. Cuba gained independence, but the Platt Amendment gave the US right of military intervention.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.2 Imperialism: Debates"
    },
    {
        "id": "ap-ush-062",
        "type": "mcq",
        "subtopic": "The Progressive Era & Muckrakers (Period 7: 1890–1945)",
        "difficulty": "Easy",
        "question": "The publication of Upton Sinclair's 1906 novel The Jungle contributed most directly to which federal legislative reform under President Theodore Roosevelt?",
        "options": [
            "The passage of the Pure Food and Drug Act and the Meat Inspection Act of 1906",
            "The establishment of the Federal Reserve banking system",
            "The passage of the Clayton Antitrust Act protecting labor unions from prosecution",
            "The ratification of the Eighteenth Amendment establishing national Prohibition"
        ],
        "answer": 0,
        "explanation": "Although Sinclair intended to generate public sympathy for exploited socialist factory workers, readers were horrified by his visceral descriptions of unsanitary Chicago meatpacking plants. President Theodore Roosevelt investigated and pushed Congress to pass the Meat Inspection Act and Pure Food and Drug Act.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.4 The Progressives"
    },
    {
        "id": "ap-ush-063",
        "type": "mcq",
        "subtopic": "WWI & The League of Nations Debate (Period 7: 1890–1945)",
        "difficulty": "Hard",
        "question": "Why did the United States Senate, led by Senator Henry Cabot Lodge, ultimately reject the Treaty of Versailles in 1919 and 1920?",
        "options": [
            "Senators feared that Article X of the League of Nations Covenant would draw the U.S. into foreign wars without the constitutional consent of Congress",
            "President Woodrow Wilson refused to grant women the right to vote in the treaty text",
            "The treaty failed to impose any financial war reparations upon Germany",
            "The treaty granted Great Britain exclusive sovereign control over the Panama Canal"
        ],
        "answer": 0,
        "explanation": "Article X of the League Covenant pledged member nations to respect and preserve the territorial integrity of all members against external aggression. 'Reservationists' (led by Lodge) and 'Irreconcilables' feared this collective security clause infringed upon Congress's constitutional authority to declare war.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.6 World War I: Home Front and Aftermath"
    },
    {
        "id": "ap-ush-064",
        "type": "mcq",
        "subtopic": "The First Red Scare & Nativism (Period 7: 1890–1945)",
        "difficulty": "Medium",
        "question": "The Palmer Raids of 1919–1920 and the Immigration Act of 1924 (National Origins Act) reflected which pervasive post-World War I societal sentiment?",
        "options": [
            "A surge in nativism and anti-radical hysteria fueled by fears of Bolshevik communism and foreign anarchist revolutions",
            "A broad national consensus favoring open borders to satisfy post-war industrial labor shortages",
            "A bipartisan rejection of protective tariffs and a revival of free trade internationalism",
            "A universal federal commitment to desegregate public accommodations in urban centers"
        ],
        "answer": 0,
        "explanation": "Following the 1917 Bolshevik Revolution and mail-bomb attacks in 1919, Attorney General A. Mitchell Palmer directed raids arresting and deporting suspected radical immigrants without warrants. This nativist climate culminated in the National Origins Act of 1924, establishing strict nationality quotas targeting Southern and Eastern Europeans.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.8 1920s: Cultural and Political Controversies"
    },
    {
        "id": "ap-ush-065",
        "type": "mcq",
        "subtopic": "The Harlem Renaissance (Period 7: 1890–1945)",
        "difficulty": "Medium",
        "question": "The Harlem Renaissance of the 1920s is best characterized as:",
        "options": [
            "A vibrant literary, musical, and artistic flourishing that celebrated African American cultural identity and challenged racial stereotypes",
            "A mass migration movement advocating for the physical return of African Americans to Liberia",
            "A political party that won legislative majorities across northern urban districts",
            "An exclusively religious crusade that sought to establish independent churches in the rural South"
        ],
        "answer": 0,
        "explanation": "Fueled by the Great Migration, Harlem became the vibrant cultural capital of Black America. Figures like Langston Hughes, Zora Neale Hurston, Duke Ellington, and Louis Armstrong produced groundbreaking literature, poetry, and jazz that expressed Black pride, resilience, and resistance to white racism.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.8 1920s: Cultural and Political Controversies"
    },
    {
        "id": "ap-ush-066",
        "type": "mcq",
        "subtopic": "The Great Depression Causes (Period 7: 1890–1945)",
        "difficulty": "Medium",
        "question": "Which of the following was a primary structural cause of the Great Depression preceding the stock market crash of October 1929?",
        "options": [
            "Excessive consumer credit speculation, severe income inequality, and agricultural overproduction resulting in chronically depressed commodity prices",
            "The complete absence of protective tariffs on imported foreign goods",
            "Overly generous federal social welfare expenditures that bankrupted the national treasury",
            "A dramatic shortage of manufactured industrial goods relative to consumer demand"
        ],
        "answer": 0,
        "explanation": "Beneath 1920s prosperity lay deep structural weaknesses: American farmers had suffered from overproduction and plummeting prices since WWI; wealth was intensely concentrated; consumers relied on installment debt; and banks engaged in reckless, unregulated margin lending for stock speculation.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.9 The Great Depression"
    },
    {
        "id": "ap-ush-067",
        "type": "mcq",
        "subtopic": "FDR & The New Deal (Period 7: 1890–1945)",
        "difficulty": "Medium",
        "question": "The Social Security Act of 1935 represented a fundamental transformation in American governance primarily because it:",
        "options": [
            "Established a permanent federal responsibility to provide a social safety net, including old-age pensions, unemployment insurance, and aid to dependent children",
            "Nationalized all private commercial banks and placed them under federal ownership",
            "Guaranteed every American citizen a federally subsidized home mortgage",
            "Abolished all private employer pension plans in favor of military-style pensions"
        ],
        "answer": 0,
        "explanation": "A cornerstone of the Second New Deal, the Social Security Act marked a dramatic shift from laissez-faire governance to the modern American welfare state, codifying the federal government's legal duty to safeguard citizens against the economic hazards of old age, disability, and unemployment.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.10 The New Deal"
    },
    {
        "id": "ap-ush-068",
        "type": "mcq",
        "subtopic": "WWII Home Front & Executive Order 9066 (Period 7: 1890–1945)",
        "difficulty": "Hard",
        "question": "What was the constitutional significance of the Supreme Court's decision in Korematsu v. United States (1944)?",
        "options": [
            "The Court upheld the forced internment of over 110,000 Japanese Americans, ruling that wartime military necessity superseded constitutional civil liberties",
            "The Court ruled that President Roosevelt had exceeded his executive authority under Article II",
            "The Court held that citizens of Japanese ancestry were entitled to immediate monetary reparations",
            "The Court struck down the military draft as an unconstitutional violation of the Thirteenth Amendment"
        ],
        "answer": 0,
        "explanation": "In Korematsu v. U.S., Justice Hugo Black wrote for the 6–3 majority that the exclusion and forced internment of Japanese Americans under Executive Order 9066 was a constitutional exercise of emergency wartime powers, despite zero evidence of espionage or disloyalty among the interned population.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.12 World War II: Mobilization"
    },
    {
        "id": "ap-ush-069",
        "type": "mcq",
        "subtopic": "Cold War: Containment & Truman Doctrine (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "“It must be the policy of the United States to support free peoples who are resisting attempted subjugation by armed minorities or by outside pressures.”\n— President Harry S. Truman, Address to Congress, March 1947\n\nThe policy enunciated in the excerpt became known as the Truman Doctrine and was initially implemented to provide financial and military aid to:",
        "options": [
            "Greece and Turkey to prevent communist takeovers backed by the Soviet Union",
            "South Korea following the invasion by North Korean military forces",
            "Nationalist Chinese forces retreating to Taiwan",
            "West Berlin during the Soviet blockade of road and rail corridors"
        ],
        "answer": 0,
        "explanation": "When Britain announced in 1947 that it could no longer financially support the Greek monarchy against communist insurgents, Truman requested $400 million in aid for Greece and Turkey. This established the Truman Doctrine and containment as the defining framework of American Cold War foreign policy.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.2 The Cold War from 1945 to 1980"
    },
    {
        "id": "ap-ush-070",
        "type": "mcq",
        "subtopic": "The Marshall Plan (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "The European Recovery Program (Marshall Plan) approved by Congress in 1948 aimed primarily to:",
        "options": [
            "Rebuild war-torn Western European economies to restore prosperity, stabilize democratic institutions, and blunt the political appeal of communism",
            "Establish permanent American colonial protectorates across Central Europe",
            "Fund the rearmament of the West German military into an independent nuclear force",
            "Force Western European countries to dismantle their national public healthcare systems"
        ],
        "answer": 0,
        "explanation": "Secretary of State George Marshall proposed spending over $13 billion to reconstruct Western European infrastructure and industry. By revitalizing European commerce, it spurred demand for American goods and eliminated the economic desperation that fostered communist political electoral gains in Italy and France.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.2 The Cold War from 1945 to 1980"
    },
    {
        "id": "ap-ush-071",
        "type": "mcq",
        "subtopic": "Brown v. Board of Education (Period 8: 1945–1980)",
        "difficulty": "Easy",
        "question": "The Supreme Court's unanimous ruling in Brown v. Board of Education of Topeka (1954), delivered by Chief Justice Earl Warren, held that:",
        "options": [
            "Racial segregation in public schools was inherently unequal, violating the Equal Protection Clause of the Fourteenth Amendment",
            "Racial quotas must be implemented immediately across all higher education admissions",
            "State legislatures possessed the sovereign right to interpose state authority against federal court orders",
            "School segregation was constitutional provided both white and black schools received identical per-pupil funding"
        ],
        "answer": 0,
        "explanation": "Overturning the 1896 Plessy v. Ferguson 'separate but equal' precedent, Chief Justice Earl Warren declared that segregating children in public schools based on race generated feelings of inferiority that could never be undone, establishing that 'separate educational facilities are inherently unequal.'",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.10 The African American Civil Rights Movement (1960s)"
    },
    {
        "id": "ap-ush-072",
        "type": "mcq",
        "subtopic": "1950s Suburbia & Affluence (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "The rapid expansion of suburban housing developments, such as Levittown, in the 1950s was facilitated most directly by:",
        "options": [
            "Federal Housing Administration (FHA) and GI Bill low-interest guaranteed mortgages, combined with mass assembly-line home construction and automobile ownership",
            "The complete nationalization of suburban land development by the Department of Housing and Urban Development",
            "The total elimination of racial covenants in all private real estate contracts nationwide",
            "A steep decline in birth rates that reduced household sizes across the country"
        ],
        "answer": 0,
        "explanation": "The post-WWII baby boom, high union wages, mass-production building techniques (William Levitt), affordable cars, the 1956 Interstate Highway Act, and government-backed FHA and VA mortgage loans made suburban homeownership attainable for millions of white working- and middle-class families.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.4 The Red Scare and Affluence"
    },
    {
        "id": "ap-ush-073",
        "type": "mcq",
        "subtopic": "The Cuban Missile Crisis (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "During the Cuban Missile Crisis of October 1962, President John F. Kennedy resolved the dangerous nuclear confrontation with Soviet Premier Nikita Khrushchev by:",
        "options": [
            "Imposing a naval 'quarantine' (blockade) of Cuba, while privately agreeing to withdraw American Jupiter missiles from Turkey in exchange for Soviet missile removal from Cuba",
            "Launching an immediate preemptive air strike to destroy all Soviet missile sites in Cuba",
            "Ordering a full-scale amphibious military invasion of Havana by U.S. Marines",
            "Agreeing to surrender West Berlin to the Soviet Union"
        ],
        "answer": 0,
        "explanation": "Rejecting calls from military chiefs for immediate air strikes or invasion, JFK enacted a naval quarantine around Cuba. In back-channel diplomacy, Khrushchev agreed to dismantle the missiles under UN inspection in exchange for an American public pledge not to invade Cuba and a secret pledge to remove obsolete US missiles from Turkey.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.7 America as a World Power"
    },
    {
        "id": "ap-ush-074",
        "type": "mcq",
        "subtopic": "Civil Rights Act of 1964 & Voting Rights Act of 1965 (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "The Voting Rights Act of 1965 dismantled decades of southern voter suppression primarily by:",
        "options": [
            "Outlawing literacy tests and establishing federal oversight and preclearance over voter registration in jurisdictions with historical disenfranchisement",
            "Lowering the federal voting age from twenty-one to eighteen across all states",
            "Requiring all voters to pass a standardized federal civics examination before casting a ballot",
            "Mandating compulsory voting in all federal presidential elections"
        ],
        "answer": 0,
        "explanation": "Catalyzed by the Selma-to-Montgomery march, the Voting Rights Act of 1965 banned literacy tests, authorized federal registrars to register eligible Black voters in counties where discrimination was rampant, and required covered states to get federal 'preclearance' before altering voting procedures.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.10 The African American Civil Rights Movement (1960s)"
    },
    {
        "id": "ap-ush-075",
        "type": "mcq",
        "subtopic": "LBJ's Great Society (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "President Lyndon B. Johnson's 'Great Society' legislative agenda created which of the following landmark public health programs?",
        "options": [
            "Medicare (health insurance for elderly Americans) and Medicaid (health coverage for low-income families)",
            "The Affordable Care Act and individual health insurance exchanges",
            "The Civilian Conservation Corps and Works Progress Administration",
            "The Occupational Safety and Health Administration (OSHA)"
        ],
        "answer": 0,
        "explanation": "Signed into law by LBJ in 1965 as part of his Great Society 'War on Poverty', Medicare (Title XVIII) provided hospital and medical insurance to Americans aged 65 and older, while Medicaid (Title XIX) provided government-funded healthcare for low-income citizens and families.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.9 The Great Society"
    },
    {
        "id": "ap-ush-076",
        "type": "mcq",
        "subtopic": "Gulf of Tonkin Resolution & Vietnam War (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "The Gulf of Tonkin Resolution, passed overwhelmingly by Congress in August 1964, was historically significant because it:",
        "options": [
            "Authorized the President to take 'all necessary measures to repel any armed attack', effectively granting LBJ a blank check to escalate U.S. military involvement in Vietnam without a formal declaration of war",
            "Mandated the immediate withdrawal of all American military advisors from South Vietnam",
            "Declared war formally against the Soviet Union and the People's Republic of China",
            "Prohibited the deployment of ground combat troops in mainland Southeast Asia"
        ],
        "answer": 0,
        "explanation": "Following disputed naval skirmishes in the Gulf of Tonkin, Congress granted Johnson broad executive authority to conduct military operations in Southeast Asia without an official congressional declaration of war, leading to the deployment of over 500,000 ground troops by 1968.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.8 The Vietnam War"
    },
    {
        "id": "ap-ush-077",
        "type": "mcq",
        "subtopic": "The Tet Offensive & Public Opinion (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "Although the January 1968 Tet Offensive was a severe tactical military defeat for the Viet Cong and North Vietnamese Army, it proved to be a decisive psychological turning point in the United States because it:",
        "options": [
            "Shattered public faith in administration claims that the war was being won, creating a massive 'credibility gap' and intensifying anti-war sentiment",
            "Resulted in the immediate capture of the South Vietnamese capital of Saigon",
            "Forced the United States to deploy nuclear weapons in Southeast Asia",
            "Led to the immediate impeachment and removal of General William Westmoreland"
        ],
        "answer": 0,
        "explanation": "Prior to Tet, the Johnson administration assured the American public that enemy strength was waning and there was 'light at the end of the tunnel'. The simultaneous, coordinated attacks on over 100 South Vietnamese cities and the US Embassy in Saigon broadcast on TV destroyed public confidence and prompted LBJ not to seek re-election.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.8 The Vietnam War"
    },
    {
        "id": "ap-ush-078",
        "type": "mcq",
        "subtopic": "Second-Wave Feminism & Environmentalism (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "The modern environmental movement gained widespread national momentum in the 1960s primarily sparked by:",
        "options": [
            "Rachel Carson's publication of Silent Spring (1962), which documented the lethal ecological consequences of synthetic pesticides like DDT",
            "The immediate economic collapse of the American automotive industry",
            "The passage of the Homestead Act opening Alaskan wilderness to strip mining",
            "The total prohibition of oil extraction on federal lands by executive order"
        ],
        "answer": 0,
        "explanation": "Carson's groundbreaking work Silent Spring exposed how indiscriminate chemical pesticide spraying entered the food chain, decimated bird populations, and posed severe human cancer risks. It galvanized public activism, culminating in the first Earth Day in 1970 and the creation of the Environmental Protection Agency (EPA).",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.13 The Environment and Natural Resources"
    },
    {
        "id": "ap-ush-079",
        "type": "mcq",
        "subtopic": "Nixon's Foreign Policy & Détente (Period 8: 1945–1980)",
        "difficulty": "Medium",
        "question": "President Richard Nixon and National Security Advisor Henry Kissinger pursued the diplomatic strategy of 'détente' primarily to:",
        "options": [
            "Ease Cold War tensions through diplomatic negotiations, culminating in historic summits in Beijing and Moscow and the Strategic Arms Limitation Talks (SALT I)",
            "Unilaterally disband the North Atlantic Treaty Organization (NATO)",
            "Form a military alliance with the Soviet Union to invade mainland China",
            "Cut all international trade ties with European and Asian powers"
        ],
        "answer": 0,
        "explanation": "Détente was a pragmatic realpolitik approach aimed at reducing superpower confrontation. By opening diplomatic relations with communist China in 1972, Nixon exploited the Sino-Soviet split, pressuring Moscow to negotiate arms limitation treaties (SALT I) and trade agreements.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.7 America as a World Power"
    },
    {
        "id": "ap-ush-080",
        "type": "mcq",
        "subtopic": "Watergate Scandal & War Powers Act (Period 8: 1945–1980)",
        "difficulty": "Hard",
        "question": "The constitutional crisis surrounding the Watergate scandal (1972–1974) and the Supreme Court's ruling in United States v. Nixon affirmed that:",
        "options": [
            "Executive privilege is not absolute and cannot be used to withhold evidence relevant to criminal court proceedings, establishing that the President is not above the law",
            "The President possesses absolute immunity from congressional subpoena and judicial oversight",
            "The House of Representatives cannot initiate impeachment proceedings against an incumbent president during wartime",
            "Audio tape recordings made in the Oval Office are the personal private property of the president"
        ],
        "answer": 0,
        "explanation": "When Nixon cited executive privilege to withhold Oval Office tape recordings from Special Prosecutor Leon Jaworski, the Supreme Court ruled unanimously in U.S. v. Nixon that executive privilege does not shield communications in criminal cases. Facing certain impeachment and conviction, Nixon resigned on August 9, 1974.",
        "citation": "College Board AP® U.S. History CED — Unit 8: Topic 8.14 Society in Transition"
    }
]

# -------------------------------------------------------------
# SET 5: Period 9 & Thematic Comprehensive Review (1980–Present) — 20 Questions
# -------------------------------------------------------------
set5_questions = [
    {
        "id": "ap-ush-081",
        "type": "mcq",
        "subtopic": "Reagan Revolution & Conservatism (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "“Government is not the solution to our problem; government is the problem. From time to time we've been tempted to believe that society has become too complex to be managed by self-rule... It is my intention to curb the size and influence of the Federal establishment...”\n— President Ronald Reagan, First Inaugural Address, January 1981\n\nThe economic philosophy championed by President Reagan in his inaugural address—often called 'Reaganomics' or supply-side economics—prioritized:",
        "options": [
            "Broad federal tax cuts, reduction of government regulatory oversight on corporations, and domestic spending cuts combined with increased military expenditures",
            "Massive expansion of federal entitlement programs and higher corporate tax brackets",
            "The nationalization of major commercial airlines and energy telecommunication companies",
            "The total elimination of the U.S. military budget to achieve an immediate balanced budget"
        ],
        "answer": 0,
        "explanation": "Supply-side economics argued that cutting corporate and marginal income taxes (such as the Economic Recovery Tax Act of 1981) and slashing federal regulations would stimulate private capital investment, increase productivity, and spur economic growth, though it substantially expanded national debt due to historic defense spending increases.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.2 The Reagan Revolution"
    },
    {
        "id": "ap-ush-082",
        "type": "mcq",
        "subtopic": "End of the Cold War (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "Which of the following factors contributed most directly to the dissolution of the Soviet Union in December 1991 and the formal conclusion of the Cold War?",
        "options": [
            "Severe internal Soviet economic stagnation, the burden of the Afghan War, and Mikhail Gorbachev's reform policies of glasnost (openness) and perestroika (restructuring)",
            "A successful NATO ground invasion of Eastern European satellite nations",
            "The total refusal of the United States to negotiate bilateral nuclear arms treaties with Moscow",
            "The military unification of East and West Germany under Soviet political domination"
        ],
        "answer": 0,
        "explanation": "The Soviet system was crippled by structural economic inefficiencies, excessive military spending, and popular unrest. General Secretary Mikhail Gorbachev introduced glasnost (political transparency) and perestroika (economic restructuring), which inadvertently unleashed nationalist independence movements across Eastern Europe and Soviet republics, culminating in the USSR's collapse in 1991.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.3 The End of the Cold War"
    },
    {
        "id": "ap-ush-083",
        "type": "mcq",
        "subtopic": "The Persian Gulf War (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "Operation Desert Storm (1991), authorized by President George H.W. Bush under a United Nations mandate, was launched to:",
        "options": [
            "Expel Iraqi military forces from Kuwait following Saddam Hussein's unprovoked invasion and safeguard Persian Gulf oil supplies",
            "Overthrow the Ba'athist government in Baghdad and establish an American military occupation in Iraq",
            "Dismantle terrorist training camps in rural eastern Afghanistan",
            "Annex Kuwait as an overseas naval territory of the United States"
        ],
        "answer": 0,
        "explanation": "After Saddam Hussein invaded and annexed neighboring Kuwait in August 1990, President George H.W. Bush built a 34-nation international coalition backed by UN Security Council resolutions. Operation Desert Storm liberated Kuwait in a lightning 100-hour ground campaign while deliberately stopping short of toppling Hussein's regime.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.3 The End of the Cold War"
    },
    {
        "id": "ap-ush-084",
        "type": "mcq",
        "subtopic": "Globalization & NAFTA (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "The North American Free Trade Agreement (NAFTA), signed into law by President Bill Clinton in 1993, aimed to:",
        "options": [
            "Eliminate tariffs and trade barriers between the United States, Canada, and Mexico to create a continental free-trade zone",
            "Establish a single shared currency modeled on the European euro across North America",
            "Prohibit American manufacturers from relocating factory operations outside U.S. borders",
            "Impose strict protective import quotas on Mexican and Canadian agricultural goods"
        ],
        "answer": 0,
        "explanation": "NAFTA eliminated tariffs and trade restrictions among the US, Mexico, and Canada. Proponents argued it boosted economic efficiency and exports; critics (including labor unions) argued it accelerated the outsourcing of American manufacturing jobs to lower-wage Mexican maquiladoras.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.4 A Changing Economy"
    },
    {
        "id": "ap-ush-085",
        "type": "mcq",
        "subtopic": "The Dot-Com Boom & Technological Revolution (Period 9: 1980–Present)",
        "difficulty": "Easy",
        "question": "The rapid economic expansion of the late 1990s under the Clinton administration was driven primarily by:",
        "options": [
            "The emergence of personal computing, the commercialization of the Internet and World Wide Web, and unprecedented productivity gains in telecommunications",
            "A return to strict international mercantilist trade monopolies",
            "Massive federal government infrastructure construction comparable to the New Deal",
            "Unprecedented spikes in international crude oil prices"
        ],
        "answer": 0,
        "explanation": "The 1990s witnessed the birth of the digital 'New Economy'. Proliferation of personal computers, the Internet, e-commerce, and software innovation dramatically raised worker productivity, fueled surging tech stock markets, and contributed to federal budget surpluses from 1998 to 2001.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.4 A Changing Economy"
    },
    {
        "id": "ap-ush-086",
        "type": "mcq",
        "subtopic": "The 2000 Presidential Election & Bush v. Gore (Period 9: 1980–Present)",
        "difficulty": "Hard",
        "question": "In the controversial Supreme Court decision Bush v. Gore (2000), the Court halted manual recounts in Florida on the grounds that:",
        "options": [
            "The differing recount standards used by individual Florida counties violated the Equal Protection Clause of the Fourteenth Amendment",
            "State courts had no constitutional authority to hear election dispute lawsuits",
            "The Electoral College system had been superseded by popular vote majorities",
            "Presidential elections could only be decided by the House of Representatives"
        ],
        "answer": 0,
        "explanation": "In a 5–4 per curiam ruling, the Supreme Court held that the absence of uniform statewide recount standards across Florida counties violated the Fourteenth Amendment's Equal Protection Clause. Because Florida's statutory recount deadline had arrived, the Court halted the recount, effectively awarding Florida's 25 electoral votes and the presidency to George W. Bush.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.5 Migration and Immigration in the 1990s and 2000s"
    },
    {
        "id": "ap-ush-087",
        "type": "mcq",
        "subtopic": "Post-9/11 & The War on Terror (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "In the immediate aftermath of the terrorist attacks of September 11, 2001, the United States launched Operation Enduring Freedom in Afghanistan primarily to:",
        "options": [
            "Overthrow the fundamentalist Taliban regime that had harbored Osama bin Laden and al-Qaeda's terrorist network",
            "Secure Iraqi oil pipelines leading to the Persian Gulf",
            "Enforce United Nations weapons inspections on Saddam Hussein's chemical stockpiles",
            "Retaliate against Iranian naval incursions in the Strait of Hormuz"
        ],
        "answer": 0,
        "explanation": "Following 9/11, President George W. Bush demanded that Afghanistan's ruling Taliban surrender Osama bin Laden and shut down al-Qaeda training camps. When the Taliban refused, a US-led coalition launched military strikes, swiftly toppling the Taliban regime and initiating America's longest war.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.5 Migration and Immigration in the 1990s and 2000s"
    },
    {
        "id": "ap-ush-088",
        "type": "mcq",
        "subtopic": "The USA PATRIOT Act & Civil Liberties (Period 9: 1980–Present)",
        "difficulty": "Hard",
        "question": "The USA PATRIOT Act, passed overwhelmingly by Congress in October 2001, sparked intense national debate over the balance between national security and constitutional civil liberties primarily because it:",
        "options": [
            "Expanded federal law enforcement and intelligence surveillance powers, including roving wiretaps, bulk record collection, and delayed-notice search warrants without traditional probable cause",
            "Mandated the internment of foreign-born non-citizens in federal detention facilities",
            "Suspended all federal elections during declared periods of elevated homeland security threats",
            "Abolished the Fourth Amendment right against unreasonable searches in all circumstances"
        ],
        "answer": 0,
        "explanation": "While supporters argued the PATRIOT Act was essential to prevent future terrorist attacks by tearing down walls between foreign intelligence and domestic law enforcement, civil libertarians contended it undermined Fourth Amendment privacy rights and Fourth Amendment checks on government surveillance.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.5 Challenges of the 21st Century"
    },
    {
        "id": "ap-ush-089",
        "type": "mcq",
        "subtopic": "The 2003 Invasion of Iraq (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "The Bush administration's primary stated justification for launching the preemptive invasion of Iraq (Operation Iraqi Freedom) in March 2003 was:",
        "options": [
            "The allegation that Saddam Hussein's regime possessed stockpiles of weapons of mass destruction (WMDs) and had operational links to global terrorist networks",
            "Iraq's refusal to supply crude oil to international markets",
            "An unprovoked Iraqi naval attack on American destroyers in the Persian Gulf",
            "A direct military request from the United Nations General Assembly to depose Hussein"
        ],
        "answer": 0,
        "explanation": "The Bush administration articulated a doctrine of 'preemptive war', asserting that waiting for imminent threats was too dangerous in the post-9/11 era. Citing intelligence that Saddam Hussein possessed weapons of mass destruction (WMDs) and was seeking nuclear capability—claims that post-war inspections proved unfounded—the US and coalition allies invaded Iraq.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.5 Challenges of the 21st Century"
    },
    {
        "id": "ap-ush-090",
        "type": "mcq",
        "subtopic": "The 2008 Financial Crisis & Great Recession (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "The Great Recession of 2007–2009 was triggered primarily by which financial development?",
        "options": [
            "The collapse of the American housing bubble fueled by subprime mortgage lending, complex mortgage-backed securities, and unregulated credit default swaps",
            "A catastrophic hyperinflation crisis caused by the sudden abandonment of the fiat dollar",
            "The imposition of 50% tariffs on imported electronics from Asian manufacturing hubs",
            "The federal government's default on its national treasury bond obligations"
        ],
        "answer": 0,
        "explanation": "Widespread issuance of risky subprime home mortgages, securitized by Wall Street investment banks into complex debt instruments (MBS, CDOs), collapsed when housing prices fell. Major financial institutions (Lehman Brothers, Bear Stearns, AIG) faced insolvency, triggering a credit freeze and the worst economic crisis since the 1930s.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.4 A Changing Economy"
    },
    {
        "id": "ap-ush-091",
        "type": "mcq",
        "subtopic": "The Affordable Care Act (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "The Patient Protection and Affordable Care Act (ACA), signed into law by President Barack Obama in 2010, aimed to achieve near-universal health coverage primarily through:",
        "options": [
            "An individual mandate, health insurance exchanges with federal subsidies, Medicaid expansion, and prohibiting insurers from denying coverage for pre-existing conditions",
            "The creation of a single-payer healthcare system where the federal government directly employs all doctors and hospitals",
            "The total elimination of private employer-sponsored health insurance plans",
            "Abolishing Medicare and Medicaid in favor of private health savings accounts"
        ],
        "answer": 0,
        "explanation": "The ACA significantly reformed American healthcare by creating state health insurance marketplaces with income-based tax credits, expanding Medicaid, allowing young adults to stay on parents' plans until 26, and preventing insurers from excluding people with pre-existing conditions.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.6 Society in the 21st Century"
    },
    {
        "id": "ap-ush-092",
        "type": "mcq",
        "subtopic": "Demographic Shifts & Immigration (Period 9: 1980–Present)",
        "difficulty": "Medium",
        "question": "Since the passage of the Immigration and Nationality Act of 1965, the demographic composition of immigration to the United States has shifted dramatically, with the overwhelming majority of new immigrants arriving from:",
        "options": [
            "Latin America and Asia",
            "Northern and Western Europe",
            "The Russian Federation and Eastern Europe",
            "Australia and New Zealand"
        ],
        "answer": 0,
        "explanation": "The landmark 1965 Immigration Act abolished the discriminatory 1924 national origins quota system that favored northwestern Europe, replacing it with preferences for family reunification and skilled employment. Over the ensuing decades, millions of immigrants arrived from Latin America (especially Mexico) and Asia, transforming American demographics.",
        "citation": "College Board AP® U.S. History CED — Unit 9: Topic 9.5 Migration and Immigration in the 1990s and 2000s"
    },
    {
        "id": "ap-ush-093",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Federal Power vs. States' Rights",
        "difficulty": "Hard",
        "question": "Which of the following historical pairs represents a continuity in debates over federal power versus states' rights across different centuries?",
        "options": [
            "The Kentucky and Virginia Resolutions (1798) and the South Carolina Nullification Crisis (1832–1833)",
            "The Northwest Ordinance (1787) and the Kansas-Nebraska Act (1854)",
            "The Monroe Doctrine (1823) and the Truman Doctrine (1947)",
            "The Dawes Act (1887) and the Social Security Act (1935)"
        ],
        "answer": 0,
        "explanation": "Both the Kentucky and Virginia Resolutions (challenging the Alien & Sedition Acts) and John C. Calhoun's South Carolina Exposition and Protest during the Nullification Crisis asserted the compact theory of the Constitution—arguing that sovereign states had the authority to nullify federal statutes they deemed unconstitutional.",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Continuity and Change Over Time"
    },
    {
        "id": "ap-ush-094",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Reform Movements",
        "difficulty": "Hard",
        "question": "The reform strategies of the Civil Rights Movement of the 1950s and 1960s were most philosophically and tactically similar to which earlier nineteenth-century movement?",
        "options": [
            "The antebellum nonviolent moral suasion and direct action employed by Christian abolitionists like William Lloyd Garrison and Frederick Douglass",
            "The violent labor insurrectionism of the Molly Maguires in Pennsylvania coal mines",
            "The nativist political agitation of the Know-Nothing Party in the 1850s",
            "The imperialist expansionism advocated by the Yellow Journalists in the 1890s"
        ],
        "answer": 0,
        "explanation": "Dr. Martin Luther King Jr. and the SCLC rooted their nonviolent civil disobedience in Christian moral teachings, mirroring the antebellum abolitionist movement's conviction that unjust, discriminatory human laws violated a higher moral law and must be peacefully resisted through public witness.",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Comparison"
    },
    {
        "id": "ap-ush-095",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Foreign Policy Shifts",
        "difficulty": "Hard",
        "question": "The foreign policy posture advocated in George Washington's 1796 Farewell Address was most directly challenged and permanently abandoned by the United States during which historical development?",
        "options": [
            "The ratification of the North Atlantic Treaty in 1949, committing the United States to a permanent peacetime military alliance in Europe (NATO)",
            "The purchase of the Louisiana Territory from France in 1803",
            "The declaration of the Monroe Doctrine in 1823",
            "The passage of the Neutrality Acts of 1935–1937"
        ],
        "answer": 0,
        "explanation": "Washington warned the young nation against 'permanent alliances with any portion of the foreign world.' While the US maintained non-entanglement for 150 years, the creation of NATO in 1949 marked America's first peacetime military alliance, formally discarding isolationist tradition in favor of collective security.",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Continuity and Change Over Time"
    },
    {
        "id": "ap-ush-096",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Economic Crises",
        "difficulty": "Hard",
        "question": "How did the federal government's policy response to the 2008 Great Recession fundamentally differ from its initial response to the onset of the Great Depression under President Herbert Hoover in 1929–1931?",
        "options": [
            "In 2008, the federal government and Federal Reserve deployed unprecedented emergency fiscal stimulus (ARRA) and multitrillion-dollar liquidity interventions (TARP, Quantitative Easing), whereas Hoover relied largely on voluntary cooperation and balanced budgets",
            "In 2008, the government raised protective tariffs to record highs, mimicking the Smoot-Hawley Tariff",
            "In 2008, the Federal Reserve raised interest rates to historic highs to crush inflation",
            "In 2008, the federal government nationalized all American agricultural farms"
        ],
        "answer": 0,
        "explanation": "Herbert Hoover initially resisted direct federal relief and deficit spending, relying on voluntary private business pledges and balanced budgets. In 2008, the Federal Reserve slashed rates to zero and launched Quantitative Easing, while Congress passed the $700 billion TARP bank rescue and an $800+ billion fiscal stimulus package.",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Comparison"
    },
    {
        "id": "ap-ush-097",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Expansion of Democracy",
        "difficulty": "Hard",
        "question": "The expansion of the franchise in the United States occurred in distinct historical waves. Which of the following correctly pairs an era with the primary group whose voting rights were constitutionally recognized?",
        "options": [
            "Progressive Era (1920) — Women (Nineteenth Amendment)",
            "Jacksonian Era (1828) — Enslaved African Americans",
            "Reconstruction (1870) — Native Americans living on reservations",
            "New Deal (1936) — Eighteen-to-twenty-year-old citizens"
        ],
        "answer": 0,
        "explanation": "The Nineteenth Amendment (ratified in 1920 during the Progressive Era) prohibited the denial of the right to vote on the basis of sex. Enslaved persons were emancipated and Black men franchised in Reconstruction (15th Amendment, 1870); 18-to-20-year-olds gained voting rights during the Vietnam War era (26th Amendment, 1971).",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Chronological Reasoning"
    },
    {
        "id": "ap-ush-098",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Labor & Industry",
        "difficulty": "Hard",
        "question": "The Wagner Act (National Labor Relations Act of 1935) altered the legal standing of American labor unions in contrast to the late nineteenth century Gilded Age primarily by:",
        "options": [
            "Legally guaranteeing workers the right to join unions and engage in collective bargaining, while prohibiting employer unfair labor practices and establishing the NLRB",
            "Outlawing union strikes in all essential transportation and mining industries",
            "Repealing the Sherman Antitrust Act's application to corporate monopolies",
            "Requiring all industrial factory workers to join the American Federation of Labor"
        ],
        "answer": 0,
        "explanation": "In the Gilded Age, the federal government repeatedly intervened with troops and court injunctions (Pullman Strike 1894) to crush strikes. The New Deal's Wagner Act of 1935 put the power of the federal government behind workers, protecting the right to organize and bargain collectively through the National Labor Relations Board (NLRB).",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Causation & Continuity"
    },
    {
        "id": "ap-ush-099",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Environmental Policy",
        "difficulty": "Medium",
        "question": "The conservationist philosophy of President Theodore Roosevelt and Gifford Pinchot in the early 1900s differed from preservationists like John Muir primarily because Roosevelt and Pinchot advocated for:",
        "options": [
            "The scientific management and sustainable commercial utilization of public natural resources ('wise use'), rather than the complete, untouched preservation of wilderness",
            "The immediate sale of all national forest lands to private timber corporations",
            "The total prohibition of all human entry and recreational tourism in national parks",
            "The transfer of all federal lands to individual state jurisdiction"
        ],
        "answer": 0,
        "explanation": "Roosevelt and his Chief Forester Gifford Pinchot were conservationists who believed public lands should be scientifically managed for long-term sustainable multi-use (timber, water, grazing). Preservationists like John Muir (founder of the Sierra Club) argued for leaving wilderness pristine and untouched by commercial development.",
        "citation": "College Board AP® U.S. History CED — Unit 7: Topic 7.4 The Progressives"
    },
    {
        "id": "ap-ush-100",
        "type": "mcq",
        "subtopic": "Thematic Synthesis: Supreme Court Eras",
        "difficulty": "Hard",
        "question": "The jurisprudence of the Warren Court (1953–1969) was characterized primarily by which judicial philosophy?",
        "options": [
            "Judicial activism aimed at expanding civil rights, individual liberties, and protections for criminal defendants (e.g., Gideon v. Wainwright, Miranda v. Arizona, Loving v. Virginia)",
            "Strict originalism that limited the application of the Bill of Rights to the federal government alone",
            "Consistently striking down congressional regulations of interstate commerce as unconstitutional",
            "Deference to state supreme courts on all constitutional questions regarding racial segregation"
        ],
        "answer": 0,
        "explanation": "Under Chief Justice Earl Warren, the Supreme Court issued a flurry of landmark liberal decisions that desegregated public schools (Brown), established rights for criminal defendants (Gideon, Miranda, Mapp), outlawed state bans on interracial marriage (Loving), and established the right to privacy (Griswold).",
        "citation": "College Board AP® U.S. History CED — Historical Thinking Skills: Contextualization & Synthesis"
    }
]

# Write all 5 sets to disk
sets_data = [
    ("ap_us_history_set1.json", set1_questions),
    ("ap_us_history_set2.json", set2_questions),
    ("ap_us_history_set3.json", set3_questions),
    ("ap_us_history_set4.json", set4_questions),
    ("ap_us_history_set5.json", set5_questions),
]

for filename, q_list in sets_data:
    filepath = os.path.join(OUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({"questions": q_list}, f, indent=2, ensure_ascii=False)
    print(f"Generated {filename}: {len(q_list)} questions.")

print("All 5 AP US History sets generated successfully!")
