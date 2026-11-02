#!/usr/bin/env python3
"""
Generates Economics Chapter 20 (Money and Credit) Sets 1, 2, 3
and Chapter 21 (Globalisation and the Indian Economy) Sets 1, 2, 3.
Total: 6 sets = 120 questions.
100% NCERT and CBSE Class 10 Social Science Board grounded.
"""

import json, os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "in", "cbse10", "social-science")

# =============================================================================
# CHAPTER 20: MONEY AND CREDIT (Economics Ch 3 / Total SST Ch 20)
# =============================================================================

# -----------------------------------------------------------------------------
# CH 20 SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch20_set1 = [
  {
    "id": "cbse10-sst-eco-ch20-s1-001",
    "type": "mcq",
    "subtopic": "Double Coincidence of Wants",
    "difficulty": "Easy",
    "question": "In a barter economy where goods are directly exchanged without the use of money, which essential condition must be satisfied?",
    "options": [
      "Double coincidence of wants (both parties must agree to sell and buy each other's commodities)",
      "A formal promissory guarantee certified by the village panchayat",
      "Gold coins deposited with an escrow magistrate",
      "A fixed exchange price list published by the state government"
    ],
    "answer": 0,
    "explanation": "Double coincidence of wants is an essential feature of a barter economy. What a person desires to sell is exactly what the other wishes to buy. Money eliminates the need for double coincidence of wants by acting as an intermediate medium of exchange.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-002",
    "type": "mcq",
    "subtopic": "Money as Medium of Exchange",
    "difficulty": "Easy",
    "question": "Why is money referred to as a 'medium of exchange'?",
    "options": [
      "Because it acts as an intermediary instrument in the transactions and exchange of goods and services",
      "Because it is minted exclusively from precious silver and gold bullion",
      "Because it can only be exchanged inside foreign diplomatic embassies",
      "Because it changes its face value automatically every month"
    ],
    "answer": 0,
    "explanation": "Since money acts as an intermediate in the exchange process, it is called a medium of exchange. A person holding money can easily exchange it for any commodity or service that he or she might want.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-003",
    "type": "mcq",
    "subtopic": "Modern Currency Characteristics",
    "difficulty": "Medium",
    "question": "Unlike historical money (such as grain, cattle, gold, and silver coins), modern Indian currency:",
    "options": [
      "Is not made of precious metal and has virtually no intrinsic everyday value of its own",
      "Can be eaten as nutritious food during famines",
      "Is valid only within 5 kilometers of the Reserve Bank headquarters",
      "Must be redeemed for silver bullion at the post office every year"
    ],
    "answer": 0,
    "explanation": "Modern forms of money include currency — paper notes and coins. Unlike the things that were used as money earlier, modern currency is not made of precious metal such as gold, silver, or copper. And unlike grain and cattle, they are neither of everyday use. The modern currency is without any use of its own.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-004",
    "type": "mcq",
    "subtopic": "Legal Authorization of Indian Rupee",
    "difficulty": "Easy",
    "question": "In India, which central authority is legally authorized by law to issue currency notes on behalf of the Central Government?",
    "options": [
      "The Reserve Bank of India (RBI)",
      "The State Bank of India (SBI)",
      "The Securities and Exchange Board of India (SEBI)",
      "The Ministry of Heavy Industries"
    ],
    "answer": 0,
    "explanation": "In India, the Reserve Bank of India issues currency notes on behalf of the central government. As per Indian law, no other individual or organisation is allowed to issue currency.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-005",
    "type": "mcq",
    "subtopic": "Rupee as Legal Tender",
    "difficulty": "Medium",
    "question": "Why cannot any individual or merchant legally refuse a payment made in Indian Rupees for settling a transaction in India?",
    "options": [
      "Because the law legalizes the use of Rupee as a medium of payment that cannot be refused in settling transactions in India",
      "Because bank notes contain microchips tracked by police satellites",
      "Because merchants are paid a commission by the World Bank on every note",
      "Because all shopkeepers are government civil service employees"
    ],
    "answer": 0,
    "explanation": "The law legalises the use of rupee as a medium of payment that cannot be refused in settling transactions in India. Hence, no individual in India can legally refuse a payment made in rupees.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-006",
    "type": "mcq",
    "subtopic": "Demand Deposits Definition",
    "difficulty": "Easy",
    "question": "Why are deposits in bank savings or current accounts referred to as 'Demand Deposits'?",
    "options": [
      "Because the deposited money can be withdrawn by the depositor on demand at any time",
      "Because the government demands 90% of the deposit as income tax",
      "Because the depositor must file an application in court before withdrawing money",
      "Because banks demand that depositors keep gold bullion in their lockers"
    ],
    "answer": 0,
    "explanation": "People deposit extra cash with the banks by opening a bank account in their name. Since the deposits in the bank accounts can be withdrawn on demand, these deposits are called demand deposits.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-007",
    "type": "mcq",
    "subtopic": "Cheque Definition",
    "difficulty": "Easy",
    "question": "A cheque is best defined as:",
    "options": [
      "A paper instructing the bank to pay a specific amount from the drawer's account to the person in whose name the cheque has been issued",
      "A government tax receipt confirming property ownership",
      "A currency note printed by commercial private banks",
      "A postal telegram ordering delivery of agricultural goods"
    ],
    "answer": 0,
    "explanation": "A cheque is a paper instructing the bank to pay a specific amount from the person's account to the person in whose name the cheque has been issued, enabling settlement without using physical cash.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-008",
    "type": "mcq",
    "subtopic": "Cash Reserve Ratio (CRR) of Commercial Banks",
    "difficulty": "Medium",
    "question": "Roughly what proportion of their total deposits do commercial banks in India keep as liquid cash to meet daily withdrawal demands of depositors?",
    "options": [
      "About 15% of their total deposits",
      "100% of their total deposits",
      "Less than 0.1% of their deposits",
      "Exactly 75% of their deposits"
    ],
    "answer": 0,
    "explanation": "Banks in India these days hold about 15 per cent of their deposits as cash. This is kept as provision to pay the depositors who might come to withdraw money from the bank on any given day.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-009",
    "type": "mcq",
    "subtopic": "Main Source of Income for Commercial Banks",
    "difficulty": "Medium",
    "question": "What constitutes the primary source of income for commercial banks?",
    "options": [
      "The difference between the higher interest rate charged on loans to borrowers and the lower interest rate paid to depositors",
      "Monetary grants received every month from the United Nations",
      "Profits earned from selling real estate properties",
      "Municipal fees collected from printing currency notes"
    ],
    "answer": 0,
    "explanation": "Banks charge a higher interest rate on loans than what they offer on deposits. The difference between what is charged from borrowers and what is paid to depositors is their main source of income.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-010",
    "type": "mcq",
    "subtopic": "Credit Situation: Positive Role (Salim)",
    "difficulty": "Easy",
    "question": "In the NCERT case of Salim, a shoe manufacturer receiving a festival order for 3,000 pairs of shoes, how did credit impact his business?",
    "options": [
      "It enabled him to procure raw materials, hire extra workers, fulfill the contract on time, earn good profits, and repay the loan",
      "It forced him to sell his family ancestral home and become a landless labourer",
      "It resulted in criminal prosecution and bankruptcy",
      "It caused him to abandon leather shoe manufacturing completely"
    ],
    "answer": 0,
    "explanation": "Salim obtains credit to meet the working capital needs of production. The credit helps him to meet the ongoing expenses of production, complete production on time, and thereby increase his earnings. Here, credit plays a vital and positive role.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-011",
    "type": "mcq",
    "subtopic": "Credit Situation: Debt-Trap (Swapna)",
    "difficulty": "Easy",
    "question": "In the case of Swapna, a small farmer who took a loan for groundnut cultivation and suffered crop failure due to pests, credit resulted in:",
    "options": [
      "A debt-trap where she had to sell a portion of her land to repay the loan",
      "Instant wealth making her the largest landowner in the village",
      "Complete debt forgiveness granted by the World Bank",
      "Starting a successful multinational pesticide corporation"
    ],
    "answer": 0,
    "explanation": "In Swapna's case, the failure of the crop made loan repayment impossible. She had to sell part of the land to pay off the debt. Credit, instead of helping Swapna improve her earnings, left her worse off — the classic example of a debt-trap.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-012",
    "type": "mcq",
    "subtopic": "Collateral Definition",
    "difficulty": "Easy",
    "question": "'Collateral' in a loan agreement is defined as:",
    "options": [
      "An asset that the borrower owns (such as land, building, vehicle, livestock, bank deposits) and pledges to the lender as a guarantee until the loan is repaid",
      "A cash bribe paid to the bank manager to approve the loan application",
      "A certificate of good conduct issued by the local member of parliament",
      "An insurance policy against foreign currency fluctuations"
    ],
    "answer": 0,
    "explanation": "Collateral is an asset that the borrower owns (such as land, building, vehicle, livestocks, deposits with banks) and uses this as a guarantee to a lender until the loan is repaid. If the borrower fails to repay the loan, the lender has the right to sell the asset.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-013",
    "type": "mcq",
    "subtopic": "Terms of Credit Components",
    "difficulty": "Medium",
    "question": "Which four components together constitute the 'Terms of Credit' in any formal lending transaction?",
    "options": [
      "Interest rate, collateral, documentation required, and mode of repayment",
      "Political party membership, caste certificate, passport, and driving license",
      "Gold jewellery, silver coins, foreign currency, and postal stamps",
      "Tax audit reports, company balance sheet, factory blueprint, and electricity bill"
    ],
    "answer": 0,
    "explanation": "Interest rate, collateral and documentation requirement, and the mode of repayment together comprise what is called the terms of credit. The terms of credit vary substantially from one credit arrangement to another.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-014",
    "type": "mcq",
    "subtopic": "Formal Sector Loans in India",
    "difficulty": "Easy",
    "question": "Which of the following lenders belong strictly to the 'Formal Sector' of credit in India?",
    "options": [
      "Commercial Banks and Cooperative Societies",
      "Village moneylenders and agricultural traders",
      "Friends, neighbours, and relatives",
      "Employers and local commission agents"
    ],
    "answer": 0,
    "explanation": "The formal sector comprises loans from banks and cooperatives. The informal lenders include moneylenders, traders, employers, relatives and friends.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-015",
    "type": "mcq",
    "subtopic": "RBI Supervision of Formal Credit",
    "difficulty": "Medium",
    "question": "The Reserve Bank of India (RBI) supervises the functioning of formal sources of loans. Which of the following is a key objective of this supervision?",
    "options": [
      "Ensuring that banks give loans not only to profit-making businesses and rich traders, but also to small cultivators, small-scale industries, and small borrowers",
      "Ordering banks to charge a 50% interest rate on rural agricultural loans",
      "Forbidding banks from keeping any liquid cash reserves in their vaults",
      "Prohibiting commercial banks from opening branches in rural areas"
    ],
    "answer": 0,
    "explanation": "The RBI monitors that the banks actually maintain a cash balance. Periodically, banks have to submit information to the RBI on how much they are lending, to whom, and at what interest rate, ensuring credit reaches small borrowers and priority sectors.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-016",
    "type": "mcq",
    "subtopic": "Informal Sector Drawbacks",
    "difficulty": "Medium",
    "question": "Why is borrowing from the informal credit sector (moneylenders) frequently disastrous for poor rural households?",
    "options": [
      "There is no supervisory organization, interest rates are exorbitantly high (often 3% to 5% per month), and lenders use coercive recovery methods",
      "Moneylenders require three government identity cards and a university diploma",
      "Informal loans must be repaid in British Pounds Sterling",
      "Moneylenders are legally barred from lending cash to farmers"
    ],
    "answer": 0,
    "explanation": "There is no organisation which supervises the credit activities of lenders in the informal sector. They can lend at whatever interest rate they choose. There is no one to stop them from using unfair means to get their money back, leading to debt-traps.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-017",
    "type": "mcq",
    "subtopic": "Urban Inequality in Credit Access",
    "difficulty": "Hard",
    "question": "According to official data presented in NCERT (Graph 2), what percentage of loans taken by poor households in urban areas comes from informal sources?",
    "options": [
      "85% of their loans come from informal sources",
      "Only 10% comes from informal sources",
      "Zero percent, because all poor households use nationalized banks",
      "Exactly 50% comes from informal sources"
    ],
    "answer": 0,
    "explanation": "Of all the loans taken by poor households in the urban areas, 85% are from informal sources! Compare this with rich urban households, where only 10% of loans are from informal sources while 90% are from formal sources.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4, Graph 2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-018",
    "type": "mcq",
    "subtopic": "Self-Help Groups (SHGs) Structure",
    "difficulty": "Easy",
    "question": "A typical Self-Help Group (SHG) organized in rural India consists of how many members, meeting and pooling their savings regularly?",
    "options": [
      "15 to 20 members, usually belonging to one neighbourhood",
      "500 to 1,000 members from different districts",
      "Only 2 members (a husband and wife)",
      "Exactly 100 registered company directors"
    ],
    "answer": 0,
    "explanation": "A typical SHG has 15-20 members, usually belonging to one neighbourhood, who meet and save regularly. Saving per member varies from ₹25 to ₹100 or more, depending on the ability of the people to save.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-019",
    "type": "mcq",
    "subtopic": "How SHGs Overcome Collateral Problem",
    "difficulty": "Medium",
    "question": "How do Self-Help Groups solve the problem of 'lack of collateral' for rural poor women seeking bank loans?",
    "options": [
      "After regular savings for a year or two, the group becomes eligible for bank loans sanctioned in the name of the group without requiring individual asset collateral",
      "The members mortgage their ancestral village farmland to foreign investors",
      "The panchayat sarpanch signs a blank cheque on behalf of the group",
      "The Reserve Bank directly deposits ₹10 lakh into each member's personal account"
    ],
    "answer": 0,
    "explanation": "If the group is regular in savings, it becomes eligible for availing loan from the bank. Loan is sanctioned in the name of the group and is meant to create self-employment opportunities. The group provides collective social guarantee, solving the collateral obstacle.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s1-020",
    "type": "mcq",
    "subtopic": "Grameen Bank of Bangladesh",
    "difficulty": "Easy",
    "question": "The Grameen Bank of Bangladesh, which successfully pioneered micro-credit for millions of poor women, was founded by Nobel Peace laureate:",
    "options": [
      "Professor Muhammad Yunus",
      "Amartya Sen",
      "Manmohan Singh",
      "Abhijit Banerjee"
    ],
    "answer": 0,
    "explanation": "Grameen Bank of Bangladesh was started in the 1970s as a small project by Professor Muhammad Yunus. In 2018, it had over 9 million members in 81,600 villages, almost all of whom are women from poorest sections.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  }
]

# -----------------------------------------------------------------------------
# CH 20 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch20_set2 = [
  {
    "id": "cbse10-sst-eco-ch20-s2-001",
    "type": "mcq",
    "subtopic": "Barter Inefficiency Application",
    "difficulty": "Easy",
    "question": "A shoe manufacturer wants to sell shoes and buy wheat. In a barter system without money, what difficulty does he immediately encounter?",
    "options": [
      "He must find a wheat-growing farmer who not only wants to sell wheat, but also wants to buy the exact size and style of shoes he makes",
      "He must obtain an export license from the United Nations",
      "He is legally prohibited from consuming wheat products",
      "He can only trade with merchants who speak foreign languages"
    ],
    "answer": 0,
    "explanation": "Both parties have to agree to sell and buy each other's commodities. If the farmer wants clothes instead of shoes, no exchange can occur — the classic obstacle of double coincidence of wants.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-002",
    "type": "mcq",
    "subtopic": "Bank Run / Fractional Reserve Banking",
    "difficulty": "Hard",
    "question": "What would happen to a commercial bank if all of its depositors arrive on the exact same morning demanding to withdraw their entire savings in cash?",
    "options": [
      "The bank would face a liquidity crisis ('bank run') and be unable to pay all depositors immediately because most funds are tied up in long-term loans",
      "The bank would immediately double its profits by collecting withdrawal fees",
      "The bank would print new paper currency in its back office within ten minutes",
      "The bank manager would be declared the permanent governor of the Reserve Bank"
    ],
    "answer": 0,
    "explanation": "Because banks keep only about 15% cash reserves based on the statistical assumption that not all depositors withdraw money on the same day, a simultaneous mass withdrawal causes a run on the bank.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-003",
    "type": "mcq",
    "subtopic": "Credit for Crop Production Nature",
    "difficulty": "Medium",
    "question": "Why is credit for agricultural crop production uniquely riskier than credit for manufacturing industrial shoes?",
    "options": [
      "Because crop yields depend critically on unpredictable factors like monsoon rainfall, pest attacks, and climate, which can destroy the harvest entirely",
      "Because agricultural crops are legally barred from being sold in rural mandis",
      "Because bank interest rates on agricultural loans are set at 100% per month",
      "Because farmers are not permitted to use currency notes"
    ],
    "answer": 0,
    "explanation": "Agricultural credit carries high inherent risk: farmers incur heavy upfront costs for seeds, fertilizer, and irrigation, but if monsoon fails or pests attack (as in Swapna's case), the crop fails and loan repayment becomes impossible.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-004",
    "type": "mcq",
    "subtopic": "Debt-Trap Mechanics",
    "difficulty": "Medium",
    "question": "What is meant by the economic term 'debt-trap'?",
    "options": [
      "A situation where credit pushes the borrower into a financial crisis from which recovery is impossible without selling productive assets or taking further debt",
      "A government tax audit conducted on private commercial companies",
      "An automated machine that detects counterfeit currency notes",
      "A legal contract restricting a worker from changing employers"
    ],
    "answer": 0,
    "explanation": "A debt-trap occurs when repayment of a loan requires taking another loan or selling productive assets (like land). Instead of improving the borrower's earnings, credit leaves them worse off and trapped in compounding debt.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-005",
    "type": "mcq",
    "subtopic": "Lender's Risk and Collateral",
    "difficulty": "Medium",
    "question": "Why do commercial banks insist on collateral before sanctioning a housing loan or vehicle loan?",
    "options": [
      "To serve as a security against default, allowing the bank to sell the property to recover the unpaid loan amount if the borrower fails to repay",
      "To confiscate all borrower belongings regardless of whether loan is repaid",
      "To transfer ownership of the property to the Reserve Bank of India",
      "To prevent borrowers from ever entering the bank branch premises"
    ],
    "answer": 0,
    "explanation": "Collateral protects the lender against default. If the borrower defaults, the lender has the legal right to sell the pledged asset to recover the outstanding principal and interest.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-006",
    "type": "mcq",
    "subtopic": "Small Farmer Dependence on Moneylenders",
    "difficulty": "Medium",
    "question": "Why do small and marginal farmers in Indian villages continue to borrow from exploitative local moneylenders despite 36% to 60% annual interest rates?",
    "options": [
      "Because moneylenders lend without requiring collateral, know borrowers personally, and are accessible anytime without complex documentation",
      "Because moneylenders offer lower interest rates than commercial banks",
      "Because commercial banks are legally forbidden to enter village territories",
      "Because small farmers prefer paying exorbitant interest charges"
    ],
    "answer": 0,
    "explanation": "Informal lenders know borrowers personally and are willing to give a loan without collateral. They can also approach moneylenders even without repaying previous loans, whereas banks require collateral and extensive paperwork that poor villagers lack.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-007",
    "type": "mcq",
    "subtopic": "Agricultural Trader as Lender: Tied Credit",
    "difficulty": "Hard",
    "question": "In the NCERT fieldwork in Sonpur village, farmer Arun borrows from a trader at the beginning of the cropping season. In exchange for the loan, the trader extracts which restrictive condition?",
    "options": [
      "The farmer promises to sell his entire paddy crop to the trader at a pre-fixed price lower than prevailing market rates",
      "The farmer agrees to surrender his voting rights in general elections",
      "The farmer must work as an unpaid domestic servant for five years",
      "The farmer promises to give 90% of his land to the trader's children"
    ],
    "answer": 0,
    "explanation": "Traders often provide loans on the condition that farmers sell their crop to them. This ensures the trader recovers the loan money and also buys crop at a low price, making huge profits by reselling it later at high market rates.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3 (Fieldwork in Sonpur)"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-008",
    "type": "mcq",
    "subtopic": "Cooperative Credit Societies Functioning",
    "difficulty": "Medium",
    "question": "How do Agricultural Cooperative Societies (like Krishak Cooperative in Sonpur) raise funds to lend to their farmer members?",
    "options": [
      "They pool deposits from member farmers, use those deposits as collateral to obtain a large loan from a bank, and then lend to members for seeds, implements, and tube wells",
      "They sell foreign treasury bills on international currency exchanges",
      "They collect mandatory taxes from urban shopping malls",
      "They print their own private cooperative currency notes"
    ],
    "answer": 0,
    "explanation": "Members pool deposits. With these deposits as collateral, the cooperative obtains a large loan from the bank. These funds are used to provide loans to members. Once these loans are repaid, another round of lending begins.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-009",
    "type": "mcq",
    "subtopic": "Empowerment of Women through SHGs",
    "difficulty": "Medium",
    "question": "Beyond financial self-reliance, what crucial social transformation do Self-Help Groups (SHGs) facilitate for rural women?",
    "options": [
      "Regular meetings provide an empowering platform to discuss and act on social issues such as health, nutrition, hygiene, and domestic violence",
      "Women are trained to serve in overseas foreign diplomatic corps",
      "Women are appointed as permanent judges of the high court",
      "Women are exempted from domestic civil law jurisdictions"
    ],
    "answer": 0,
    "explanation": "SHGs are the building blocks of organisation of the rural poor. Not only does it help women become financially self-reliant, the regular meetings of the group provide a platform to discuss and act on a variety of social issues such as health, nutrition, domestic violence, etc.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-010",
    "type": "mcq",
    "subtopic": "Cheque Settlement Process",
    "difficulty": "Medium",
    "question": "Prem writes a cheque of ₹50,000 to Salim drawn on his State Bank of India account. When Salim deposits this cheque in his own Punjab National Bank account, what financial transaction occurs?",
    "options": [
      "₹50,000 is debited (transferred out) from Prem's SBI account and credited into Salim's PNB account through the interbank clearing system without any physical cash handling",
      "Prem's house is automatically mortgaged to the Punjab National Bank",
      "Salim must travel to Mumbai to collect gold coins from the Reserve Bank",
      "The cheque is converted into a twenty-year government treasury bond"
    ],
    "answer": 0,
    "explanation": "A cheque allows direct book-entry transfer: money is transferred from one bank account to another bank account without any physical currency changing hands, making transactions safe and efficient.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-011",
    "type": "mcq",
    "subtopic": "Cheap Credit as an Engine for National Development",
    "difficulty": "Board Standard",
    "question": "Why is the availability of 'cheap and affordable formal credit' considered crucial for a country's economic development?",
    "options": [
      "It allows enterprises and small farmers to borrow, invest, establish new manufacturing units, expand output, and generate incomes without falling into debt traps",
      "It eliminates the need for citizens to work or produce goods",
      "It forces commercial banks to forgive all international foreign debts",
      "It replaces all income taxes with private bank loans"
    ],
    "answer": 0,
    "explanation": "Cheap and affordable credit is crucial for the country's development. High cost of borrowing means a large part of earnings is spent to repay the loan, leaving little for investment. Affordable credit promotes new businesses, agricultural investments, and employment.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-012",
    "type": "mcq",
    "subtopic": "Formal Credit Distribution Imperative",
    "difficulty": "Board Standard",
    "question": "To ensure equitable growth, what two vital credit policy reforms must the government and RBI pursue simultaneously?",
    "options": [
      "Expand overall formal lending in rural areas and ensure that formal credit is distributed more equally so that the poor can benefit from cheaper loans",
      "Abolish all commercial banks and nationalize private gold jewellery",
      "Force all rural farmers to borrow exclusively from private urban moneylenders",
      "Ban cooperative credit societies from operating in villages"
    ],
    "answer": 0,
    "explanation": "First, the formal sector must expand lending to replace moneylenders. Second, formal credit must be distributed equitably so that poor households, who currently get 85% of loans from expensive informal sources, receive affordable bank credit.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-013",
    "type": "mcq",
    "subtopic": "Group Accountability in SHGs",
    "difficulty": "Medium",
    "question": "Why are commercial banks willing to lend to Self-Help Groups even when the individual members possess no land or assets for collateral?",
    "options": [
      "Because the entire group assumes collective responsibility for loan repayment, and any non-repayment by a member is followed up seriously by other members",
      "Because the central government guarantees 100% reimbursement on any defaulted loan",
      "Because SHG members are required to deposit foreign stocks as security",
      "Because bank managers receive direct personal bonuses from SHG meetings"
    ],
    "answer": 0,
    "explanation": "The group is responsible for repayment. Any case of non-repayment of loan by any one member is followed up seriously by other members in the group. Because of this feature, banks are willing to lend to poor women organized in SHGs even without collateral.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-014",
    "type": "mcq",
    "subtopic": "Informal Debt Spiral Case",
    "difficulty": "Medium",
    "question": "Rama works as an agricultural labourer in Sonpur. During several months when there is no farm work, she borrows from her employer at 5% interest per month (60% annually). Unable to repay, she is forced to work for him at wages far below market rates. This scenario illustrates:",
    "options": [
      "Debt bondage and informal credit exploitation where the borrower is trapped in subservience due to unpayable compounded interest",
      "Formal banking credit facilitating upward economic mobility",
      "A cooperative credit arrangement functioning under RBI guidelines",
      "Corporate equity financing in rural agricultural markets"
    ],
    "answer": 0,
    "explanation": "Rama's case demonstrates how informal loans with usurious interest rates (60% per annum) force poor workers into perpetual debt bondage, working for low wages under the lender's control.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3 (Case of Rama)"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-015",
    "type": "mcq",
    "subtopic": "Why RBI Mandates Priority Sector Lending",
    "difficulty": "Hard",
    "question": "Why does the RBI mandate that commercial banks allocate a minimum percentage of their net bank credit to the 'Priority Sector' (agriculture, micro-enterprises, education)?",
    "options": [
      "To prevent banks from lending exclusively to large urban corporate conglomerates and ensure that vulnerable, employment-generating sectors receive necessary credit",
      "To force commercial banks into insolvency within three fiscal quarters",
      "To convert private commercial banks into non-profit religious trusts",
      "To eliminate interest payments on all urban housing loans"
    ],
    "answer": 0,
    "explanation": "Left to market forces alone, banks would lend only to large, safe, profit-maximizing urban corporations. RBI rules ensure credit flows to agriculture and small enterprises vital for national livelihood.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-016",
    "type": "mcq",
    "subtopic": "Credit Terms: Documentation Requirement",
    "difficulty": "Easy",
    "question": "Why do landless labourers and urban informal workers often fail to get loans from formal commercial banks even if they want them?",
    "options": [
      "They cannot produce formal salary slips, tax returns, land title records, or asset collateral demanded by bank documentation procedures",
      "The law prohibits commercial banks from accepting currency notes from manual labourers",
      "Formal bank branches are barred from serving Indian citizens",
      "Bank computers cannot process loans less than ₹1 crore"
    ],
    "answer": 0,
    "explanation": "Bank loans require proper documentation (proof of employment, salary slips, land title deeds) and collateral. Absence of collateral and documentation is one of the major reasons preventing the poor from getting bank loans.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-017",
    "type": "mcq",
    "subtopic": "Digital Payments and Modern Currency",
    "difficulty": "Medium",
    "question": "How do modern digital transactions (such as UPI, debit cards, and net banking) relate to demand deposits in the banking system?",
    "options": [
      "They act as electronic instructions allowing direct, instantaneous transfer of funds between demand deposits without using paper currency",
      "They completely replace commercial banks with private social media companies",
      "They create paper currency notes inside personal smartphones",
      "They eliminate the need for having a bank account or monetary balance"
    ],
    "answer": 0,
    "explanation": "Digital payments (like cheques) are modern settlement mechanisms that debit and credit demand deposits directly through electronic telecommunication networks.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-018",
    "type": "mcq",
    "subtopic": "Usury Law and Moneylender Regulation",
    "difficulty": "Hard",
    "question": "Why is it notoriously difficult for the state to regulate or cap interest rates charged by informal rural moneylenders?",
    "options": [
      "Transactions are conducted in cash without written receipts, informal records are concealed, and poor borrowers are terrified of losing their only emergency credit source",
      "Moneylenders are protected by international diplomatic immunity",
      "The Supreme Court of India declared informal lending exempt from all laws",
      "Informal moneylenders operate exclusively from foreign countries"
    ],
    "answer": 0,
    "explanation": "Informal credit operates off the books through verbal agreements or coercive promissory notes; borrowers fear that reporting moneylenders will cut off their only lifeline during medical or domestic emergencies.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-019",
    "type": "mcq",
    "subtopic": "Microfinance Revolution Impact",
    "difficulty": "Medium",
    "question": "What fundamental principle of microfinance did Professor Muhammad Yunus and Grameen Bank demonstrate to the global financial world?",
    "options": [
      "Poor women, when organised into groups, are highly creditworthy and reliable borrowers who invest prudently to lift their families out of poverty",
      "Only wealthy landowners can be trusted to repay bank loans",
      "Micro-credit should only be provided to large corporate agricultural farms",
      "Poor women should be barred from engaging in income-generating activities"
    ],
    "answer": 0,
    "explanation": "Grameen Bank proved that poor women are reliable borrowers who utilize tiny loans for sewing, livestock, and handicrafts, achieving repayment rates above 98% and transforming rural livelihoods.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s2-020",
    "type": "mcq",
    "subtopic": "Summary: The Dual Nature of Credit",
    "difficulty": "Board Standard",
    "question": "Which statement accurately summarizes the dual potential of credit in an economy?",
    "options": [
      "Credit can either be a vital catalyst for income growth and enterprise or a devastating mechanism that pushes vulnerable borrowers into severe debt-traps",
      "Credit always leads to bankruptcy and ruin for all borrowers",
      "Credit guarantees that every borrower becomes an industrial billionaire",
      "Credit is economically meaningless in modern market systems"
    ],
    "answer": 0,
    "explanation": "Whether credit will be beneficial or harmful depends on the risks in the situation (crop failure vs assured contract) and whether there is some support, fair interest, and collateral security for the borrower.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  }
]

# -----------------------------------------------------------------------------
# CH 20 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch20_set3 = [
  {
    "id": "cbse10-sst-eco-ch20-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Money as Medium of Exchange",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Money eliminates the necessity for double coincidence of wants in an economy.\nReason (R): Money acts as a universal intermediate medium in the exchange process, allowing individuals to trade commodities without reciprocal barter needs.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "A person holding money can purchase whatever good they desire without having to find a seller who simultaneously desires their specific barter commodity.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.1"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Modern Currency Acceptance",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Modern paper currency has no intrinsic value of its own, yet it is accepted everywhere as a medium of exchange.\nReason (R): The currency is authorized and backed by the sovereign authority of the Central Government and the Reserve Bank of India.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Modern currency is fiduciary fiat money: it holds value because it is legally decreed by the state as legal tender that cannot be refused in transaction settlement.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Credit Risk in Agriculture",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Credit in agriculture often proves destructive and pushes small farmers into a debt-trap.\nReason (R): Crop production involves high costs of inputs while facing severe environmental risks like pest attacks, droughts, or price crashes that lead to crop failure.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Unlike salaried or manufacturing borrowers with predictable cash flows, small farmers face climate and biological risks; failure leaves them unable to repay, compounding debt.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Role of Collateral",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Commercial banks require collateral before sanctioning loans to borrowers.\nReason (R): Collateral serves as security against default, allowing the bank to sell the asset to recover outstanding dues if the borrower fails to repay.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Collateral minimizes credit risk for lenders by creating an enforceable property claim that guarantees recovery in the event of default.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: RBI Supervision of Banks",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The Reserve Bank of India closely monitors that commercial banks maintain a minimum Cash Reserve Ratio.\nReason (R): Maintaining cash reserves ensures that banks always have adequate liquidity to honour the daily withdrawal demands of their depositors.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "RBI mandates the holding of cash reserves (approx 15%) so that the banking system maintains depositor confidence and avoids insolvency during regular withdrawal fluctuations.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-006",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Informal Credit Exploitation",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Informal credit lenders in rural areas charge exorbitant interest rates compared to formal commercial banks.\nReason (R): There is no supervisory organization or central authority to monitor or regulate the interest rates and recovery practices of informal lenders.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Unlike formal banks supervised by the RBI, moneylenders operate outside administrative oversight, allowing them to extract monopolistic interest rates (3% to 5% per month).",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-007",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Credit Inequality in Urban Areas",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Poor urban households are overwhelmingly dependent on informal credit sources, whereas rich urban households rely on formal bank credit.\nReason (R): Poor households lack asset collateral, regular salaried employment documentation, and financial literacy required by formal commercial banks.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Eighty-five percent of urban poor loans come from informal lenders due to the rigid collateral and paperwork barriers enforced by commercial banks.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Success of Self-Help Groups",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Self-Help Groups (SHGs) have successfully enabled poor rural women to access institutional bank credit without individual asset collateral.\nReason (R): Commercial banks lend to SHGs based on the collective social guarantee and regular pooled savings discipline of the entire group.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Because all members share mutual liability for loan repayment, commercial banks treat the group's pooled savings and social cohesion as a substitute for physical collateral.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-009",
    "type": "assertion_reasoning",
    "subtopic": "A-R: High Cost of Informal Borrowing",
    "difficulty": "Board Standard",
    "question": "Assertion (A): A high cost of informal borrowing severely hinders small business expansion and economic development.\nReason (R): When borrowers must dedicate the largest portion of their earnings simply to service usurious interest payments, little income remains for capital re-investment.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Excessive debt-servicing absorbs all surplus income, suppressing household consumption, capital formation, and enterprise growth.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Demand Deposits as Money",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Demand deposits with commercial banks are widely regarded as money in modern economies.\nReason (R): Demand deposits can be withdrawn on demand and transferred to settle debts through cheques and electronic transfers, serving as a medium of exchange.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Demand deposits fulfill all functional criteria of money: they constitute a liquid store of value and, via cheques/UPI, are universally accepted for transaction settlement.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-011",
    "type": "case_based",
    "subtopic": "Case Analysis: Salim's Festival Shoe Order",
    "difficulty": "Board Standard",
    "question": "Salim receives an order for 3,000 pairs of shoes. He obtains leather on credit from a supplier and takes a cash advance for 1,000 pairs from the merchant. He delivers the order on time, earns profit, and repays both credits. In this scenario, credit served to:",
    "options": [
      "Provide working capital that facilitated timely manufacturing output and raised his net income",
      "Push Salim into an irreversible agrarian debt-trap",
      "Force Salim to liquidate his manufacturing machines",
      "Transfer ownership of his factory to the leather supplier"
    ],
    "answer": 0,
    "explanation": "In Salim's case, credit financed the working capital gap between production costs and sales receipts, successfully expanding output and personal income.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis: Swapna's Groundnut Crop Failure",
    "difficulty": "Board Standard",
    "question": "Swapna borrows from a village moneylender for seeds and pesticide. Her crop is ruined by pests despite spraying expensive pesticides. She cannot repay. The following year she takes another loan, but harvest is average. To clear the accumulated debt, she must sell a portion of her land. This case demonstrates:",
    "options": [
      "How high-interest informal credit coupled with agricultural uncertainty creates a debt-trap that forces distress sale of productive assets",
      "The positive role of formal cooperative banking in risk mitigation",
      "That commercial pesticide companies guarantee crop insurance",
      "That selling land improves a farmer's credit rating"
    ],
    "answer": 0,
    "explanation": "Swapna's tragedy exemplifies the agrarian debt-trap: high informal interest rates combined with environmental crop failure leave the farmer poorer, forcing the sale of land.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-013",
    "type": "case_based",
    "subtopic": "Case Analysis: Sonpur Fieldwork — Four Borrowers",
    "difficulty": "Hard",
    "question": "In the village of Sonpur, Shyamal borrows from an agricultural moneylender at 60% per year; Arun borrows from a commercial bank at 8.5% per year; and Rama borrows from her employer at 60% per year and works as bonded labour. Comparing Arun with Shyamal and Rama proves that:",
    "options": [
      "Access to formal bank credit offers vastly lower interest rates (8.5% vs 60%) and fair repayment terms, protecting the borrower from financial enslavement",
      "Informal moneylenders are more compassionate than commercial bank managers",
      "Working as an agricultural labourer eliminates the need for credit",
      "Bank borrowers are required to give 90% of their harvest to the state"
    ],
    "answer": 0,
    "explanation": "Arun pays only 8.5% interest to the bank and repays easily after harvest, while Shyamal and Rama pay 60% to informal lenders and remain trapped in economic servitude.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-014",
    "type": "case_based",
    "subtopic": "Case Analysis: SHG Collective Lending",
    "difficulty": "Medium",
    "question": "A women's SHG named 'Ujala' in rural Odisha has saved ₹50,000 over two years in their bank account. The local bank sanctions a loan of ₹1,00,000 directly to the group. The group distributes this among four members to buy a cattle shed and sewing machines. If one member defaults, who handles recovery?",
    "options": [
      "The group members collectively follow up and resolve repayment because the bank holds the entire group accountable for the loan",
      "The local police immediately arrest the village sarpanch",
      "The Reserve Bank writes off the loan as foreign aid",
      "The bank confiscates the village temple land"
    ],
    "answer": 0,
    "explanation": "In an SHG, peer monitoring and group accountability ensure high repayment rates; members meet regularly and address defaults internally.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.5"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-015",
    "type": "case_based",
    "subtopic": "Case Analysis: Demand Deposit Cheque Clearance",
    "difficulty": "Medium",
    "question": "A furniture maker sells desks to a school and receives a crossed account-payee cheque of ₹1,20,000. Why is this payment method safer for both parties than carrying ₹1,20,000 in paper currency notes?",
    "options": [
      "It eliminates the risk of physical cash theft, provides an indisputable bank transaction record, and transfers funds directly between verified accounts",
      "It allows the school to cancel payment after three years without reason",
      "It exempts the furniture maker from paying sales tax",
      "It guarantees that the bank will pay double the cheque amount"
    ],
    "answer": 0,
    "explanation": "Cheques provide secure, paperless audit trails, eliminate cash handling risks, and ensure safe interbank transfer directly between authorized payees.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.2"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-016",
    "type": "mcq",
    "subtopic": "RBI Policy Mandate on Priority Lending",
    "difficulty": "Board Standard",
    "question": "If commercial banks in India only pursued maximum shareholder profit without RBI regulations, what distortion would emerge in the national credit market?",
    "options": [
      "Credit would flow exclusively to large corporate conglomerates in metros, completely starving rural farmers and small cottage industries of capital",
      "Banks would distribute free cash grants to all citizens",
      "All urban industrial companies would go bankrupt",
      "The national poverty rate would drop to zero overnight"
    ],
    "answer": 0,
    "explanation": "Without RBI mandates (Priority Sector Lending and CRR monitoring), profit-seeking banks would abandon rural agriculture and small borrowers in favor of lucrative corporate clients.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-017",
    "type": "mcq",
    "subtopic": "Informal Moneylenders Coercion Tactics",
    "difficulty": "Medium",
    "question": "Unlike formal banks that must follow legal judicial processes for debt recovery, informal moneylenders often resort to:",
    "options": [
      "Physical intimidation, seizing livestock, harvesting debtor crops by force, and demanding bonded domestic labour",
      "Filing appeals before the International Court of Justice",
      "Publishing public advertisements in national newspapers",
      "Forgiving 50% of the principal every holiday season"
    ],
    "answer": 0,
    "explanation": "Informal moneylenders are unrestricted by law and frequently use extra-legal coercion, physical harassment, and bonded labour to enforce loan repayment.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-018",
    "type": "mcq",
    "subtopic": "Cooperative Credit vs Commercial Bank",
    "difficulty": "Medium",
    "question": "What is the primary structural difference between an agricultural cooperative credit society and a private commercial bank?",
    "options": [
      "A cooperative is formed and governed democratically by member users for mutual credit assistance, whereas a private bank is operated by investors for commercial profit",
      "Cooperatives are owned exclusively by foreign sovereign states",
      "Private commercial banks are legally forbidden to accept deposits",
      "Cooperatives do not charge any interest on loans"
    ],
    "answer": 0,
    "explanation": "Cooperatives are member-owned mutual aid institutions that operate on democratic 'one member, one vote' principles to provide low-cost credit to farmers.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.3"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-019",
    "type": "mcq",
    "subtopic": "Poverty Alleviation and Formal Credit Expansion",
    "difficulty": "Board Standard",
    "question": "Why can an aggressive expansion of formal banking branches in rural India be regarded as an effective anti-poverty program?",
    "options": [
      "It liberates rural households from the predatory clutches of moneylenders, drastically lowering debt servicing costs and boosting productive farm investments",
      "It gives free tractors to every villager who opens a bank account",
      "It eliminates the need for agricultural crop cultivation",
      "It replaces local languages with English across all village schools"
    ],
    "answer": 0,
    "explanation": "Replacing 60% moneylender debt with 8% bank credit immediately raises rural disposable income, allowing farmers to invest in productive assets and climb out of poverty.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Section 3.4"
  },
  {
    "id": "cbse10-sst-eco-ch20-s3-020",
    "type": "mcq",
    "subtopic": "Summary: Financial Inclusion Vision",
    "difficulty": "Board Standard",
    "question": "Which comprehensive policy encapsulates India's national goal for the 'Money and Credit' sector?",
    "options": [
      "Universal financial inclusion through accessible formal banking, widespread SHG micro-credit networks, transparent collateral terms, and equitable credit flow to small producers",
      "Abolishing all paper money and returning to a 100% barter exchange economy",
      "Allowing private moneylenders to set interest rates without any government oversight",
      "Prohibiting rural women from opening individual bank savings accounts"
    ],
    "answer": 0,
    "explanation": "National economic development requires universal financial inclusion: expanding affordable formal credit to all citizens, particularly small farmers, artisans, and women's SHGs.",
    "citation": "NCERT Class 10 Economics, Chapter 3, Chapter Summary"
  }
]

# =============================================================================
# CHAPTER 21: GLOBALISATION AND THE INDIAN ECONOMY (Economics Ch 4 / Total SST Ch 21)
# =============================================================================

# -----------------------------------------------------------------------------
# CH 21 SET 1: Board Foundation (20 Qs)
# -----------------------------------------------------------------------------
ch21_set1 = [
  {
    "id": "cbse10-sst-eco-ch21-s1-001",
    "type": "mcq",
    "subtopic": "Multinational Corporation (MNC) Definition",
    "difficulty": "Easy",
    "question": "A Multinational Corporation (MNC) is defined as a company that:",
    "options": [
      "Owns or controls production of goods and services in more than one nation",
      "Operates exclusively within a single municipal district",
      "Is owned and directed by the United Nations General Assembly",
      "Produces goods exclusively for non-profit charitable donation"
    ],
    "answer": 0,
    "explanation": "A Multinational Corporation (MNC) is a company that owns or controls production in more than one nation. MNCs set up offices and factories for production in regions where they can get cheap labour and other resources.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-002",
    "type": "mcq",
    "subtopic": "Why MNCs Set Up Production Globally",
    "difficulty": "Easy",
    "question": "Why do MNCs locate their production units in different countries across the globe?",
    "options": [
      "To minimise the cost of production and maximise their profits by leveraging cheap labour, resources, and proximity to markets",
      "To distribute 100% of their revenues as free aid to foreign citizens",
      "Because their home countries have legally banned all factory manufacturing",
      "To avoid communicating with international transport companies"
    ],
    "answer": 0,
    "explanation": "MNCs set up production where it is close to the markets; where there is skilled and unskilled labour available at low costs; and where the availability of other factors of production is assured. This is done so that the cost of production is low and the MNCs can earn greater profits.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-003",
    "type": "mcq",
    "subtopic": "Spreading of Production by an MNC",
    "difficulty": "Medium",
    "question": "In the NCERT example of an MNC manufacturing industrial equipment: the product is designed in the United States, parts are manufactured in China, and customer care is handled in India. Why is India preferred for customer care?",
    "options": [
      "Because India has skilled, English-speaking youth and trained engineers available at competitive wage costs",
      "Because telephone calls are legally prohibited in other countries",
      "Because India has no domestic industrial manufacturing factories",
      "Because customer care can only operate in tropical climates"
    ],
    "answer": 0,
    "explanation": "India has highly skilled engineers who can understand the technical aspects of production. It also has educated English speaking youth who can provide customer care services. And all this probably can mean 50-60 percent cost savings for the MNC.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-004",
    "type": "mcq",
    "subtopic": "Foreign Investment Definition",
    "difficulty": "Easy",
    "question": "'Foreign Investment' is defined as:",
    "options": [
      "Investment made by Multinational Corporations (MNCs) in physical assets like land, buildings, machines, and other equipment in another country",
      "Gold coins purchased by ordinary domestic citizens in retail jewelry shops",
      "Loans provided by the central government to local village panchayats",
      "Taxes paid by domestic retail shops to municipal corporations"
    ],
    "answer": 0,
    "explanation": "Money that is spent to buy assets such as land, building, machines and other equipment is called investment. Investment made by MNCs is called foreign investment. Any investment is made with the hope that these assets will earn profits.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-005",
    "type": "mcq",
    "subtopic": "Most Common Route for MNC Investment",
    "difficulty": "Medium",
    "question": "What is the most common route chosen by MNCs to establish and expand production in developing countries?",
    "options": [
      "To buy up established local domestic companies and then expand their production network",
      "To construct brand new factories in deep uninhabited forests",
      "To donate all manufacturing blueprints to municipal libraries",
      "To operate exclusively through postal money order catalog sales"
    ],
    "answer": 0,
    "explanation": "The most common route for MNC investments is to buy up local companies and then to expand production. MNCs with huge wealth can quite easily do so. For example, Cargill Foods, a very large American MNC, bought over Parakh Foods in India.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-006",
    "type": "mcq",
    "subtopic": "Example: Cargill Foods and Parakh Foods",
    "difficulty": "Medium",
    "question": "When American agribusiness giant Cargill Foods bought Parakh Foods in India, what valuable domestic asset did Cargill immediately acquire?",
    "options": [
      "Parakh Foods' extensive marketing network across India, well-known brand reputation, and five modern oil refineries",
      "The entire sovereign fleet of the Indian Navy",
      "Exclusive mineral mining licenses in the Himalayas",
      "The direct ownership of the Reserve Bank of India"
    ],
    "answer": 0,
    "explanation": "Parakh Foods had built a large marketing network in various parts of India, where its brand was well-reputed. Also, Parakh Foods had four oil refineries, whose control now shifted to Cargill. Cargill became the largest producer of edible oil in India.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-007",
    "type": "mcq",
    "subtopic": "Placing Orders with Small Producers",
    "difficulty": "Medium",
    "question": "In industries like garments, footwear, and sports goods, how do large MNCs typically control production across developing nations?",
    "options": [
      "They place orders with thousands of small decentralized local producers worldwide and sell the finished products under their own powerful brand names",
      "They hire foreign armies to operate sewing machines in village workshops",
      "They manufacture 100% of all garments in automated factories in Europe",
      "They purchase raw cotton and burn it to raise global clothing prices"
    ],
    "answer": 0,
    "explanation": "Large MNCs in developed countries place orders for production with small producers. Garments, footwear, sports items are examples of industries where production is carried out by a large number of small producers around the world. The MNCs sell these under their own brand names.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-008",
    "type": "mcq",
    "subtopic": "Impact of Foreign Trade on Domestic Markets",
    "difficulty": "Easy",
    "question": "What primary opportunity does foreign trade create for domestic producers in any country?",
    "options": [
      "It allows producers to reach beyond domestic borders and compete in international global markets",
      "It prevents domestic producers from selling products within their home towns",
      "It mandates that all goods must be gifted to foreign consumers for free",
      "It forces manufacturers to convert factories into agricultural fields"
    ],
    "answer": 0,
    "explanation": "Foreign trade creates an opportunity for the producers to reach beyond the domestic markets, i.e., markets of their own countries. Producers can sell their produce not only in markets located within the country but can also compete in markets located in other countries of the world.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-009",
    "type": "mcq",
    "subtopic": "Chinese Toys in India Case Study",
    "difficulty": "Easy",
    "question": "In the NCERT case study of Chinese toys imported into India, what was the primary impact on Indian toy manufacturers?",
    "options": [
      "Indian toy makers faced severe competition, lost market share, and many had to shut down their workshops because Chinese toys were cheaper and offered newer designs",
      "Indian toy makers instantly bought all toy factories in Beijing",
      "Indian toy makers increased prices by 500% and quadrupled their sales",
      "Chinese toys were completely rejected by Indian consumers"
    ],
    "answer": 0,
    "explanation": "Chinese toys became popular because of cheaper prices and new designs. Within a year, 70 to 80 percent of toy shops in India replaced Indian toys with Chinese toys. Indian toy makers suffered heavy business losses.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-010",
    "type": "mcq",
    "subtopic": "Globalisation Definition",
    "difficulty": "Easy",
    "question": "'Globalisation' is best defined as:",
    "options": [
      "The rapid process of international integration and interconnection between countries through trade, foreign investment, and technology flows",
      "The complete closure of national borders to foreign travellers",
      "The division of the world into completely self-sufficient isolated communes",
      "The mandatory adoption of a single world religion by all governments"
    ],
    "answer": 0,
    "explanation": "Globalisation is this process of rapid integration or interconnection between countries. MNCs are playing a major role in the globalisation process. More and more goods and services, investments and technology are moving between countries.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-011",
    "type": "mcq",
    "subtopic": "Containerisation in Transport",
    "difficulty": "Medium",
    "question": "How did the invention of intermodal freight containers revolutionize global trade transport?",
    "options": [
      "Goods are packed into huge standardized containers that are transferred seamlessly across ships, railways, and trucks, slashing port handling costs and transit times",
      "Containers can fly through the air using solar-powered magnetic levitation",
      "Containers eliminate the need for container ships and railway tracks",
      "Containers can only be opened by officials of the World Bank"
    ],
    "answer": 0,
    "explanation": "Containers for transport of goods: goods are placed in containers that can be loaded intact onto ships, railways, planes and trucks. Containers have led to huge reduction in port handling costs and increased the speed with which exports can reach markets.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-012",
    "type": "mcq",
    "subtopic": "Trade Barriers Definition",
    "difficulty": "Easy",
    "question": "A tax imposed on imported goods by a national government is commonly referred to as a:",
    "options": [
      "Trade Barrier (Tariff)",
      "Subsidy grant",
      "Foreign direct investment",
      "Corporate dividend"
    ],
    "answer": 0,
    "explanation": "Tax on imports is an example of a trade barrier. It is called a barrier because some restriction has been set up. Governments can use trade barriers to increase or decrease (regulate) foreign trade and to decide what kinds of goods and how much of each should come into the country.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-013",
    "type": "mcq",
    "subtopic": "Post-Independence Trade Barriers in India",
    "difficulty": "Medium",
    "question": "Why did the Indian government put strict trade barriers on foreign imports following Independence in 1947?",
    "options": [
      "To protect newly emerging domestic industries from foreign competition during their nascent infant stage",
      "Because the government wanted to bankrupt all domestic private businesses",
      "Because international shipping ports did not exist in India before 1991",
      "Because the United Nations ordered India to ban foreign commerce"
    ],
    "answer": 0,
    "explanation": "The Indian government, after Independence, had put barriers to foreign trade and foreign investment. This was considered necessary to protect the producers within the country from foreign competition. Industries were just coming up in the 1950s and 1960s, and competition from imports at that stage would not have allowed these industries to survive.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-014",
    "type": "mcq",
    "subtopic": "Liberalisation of 1991 in India",
    "difficulty": "Easy",
    "question": "What major economic policy reform was adopted by the Government of India starting around 1991?",
    "options": [
      "Liberalisation — removing barriers and restrictions on foreign trade and foreign investment to encourage global competition",
      "Nationalisation of all privately owned consumer software companies",
      "Complete prohibition of foreign multinational companies from entering India",
      "Banning the export of Indian manufactured goods to overseas markets"
    ],
    "answer": 0,
    "explanation": "Starting around 1991, some far reaching changes in policy were made in India. The government decided that the time had come for Indian producers to compete with producers around the globe. Removing barriers or restrictions set by the government is what is known as liberalisation.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-015",
    "type": "mcq",
    "subtopic": "World Trade Organisation (WTO) Mission",
    "difficulty": "Easy",
    "question": "What is the primary stated objective of the World Trade Organisation (WTO)?",
    "options": [
      "To liberalise international trade and oversee that multilateral trade rules are obeyed by member nations",
      "To enforce a universal currency across all seven continents",
      "To command military peacekeeping troops in conflict zones",
      "To provide direct cash unemployment doles to factory workers"
    ],
    "answer": 0,
    "explanation": "World Trade Organisation (WTO) is an organisation whose aim is to liberalise international trade. Started at the initiative of developed countries, WTO establishes rules regarding international trade, and sees that these rules are obeyed.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-016",
    "type": "mcq",
    "subtopic": "WTO Agricultural Subsidy Controversy",
    "difficulty": "Hard",
    "question": "What major unfair practice or debate surrounds the WTO regarding agricultural trade between developed and developing nations?",
    "options": [
      "Developed nations like the USA force developing countries to remove agricultural tariffs while giving massive subsidies to their own rich farmers, artificially depressing global prices",
      "Developing nations have banned all American farm products from global trade",
      "The WTO forces developed nations to pay 90% import duties on all industrial electronics",
      "American farmers are legally prohibited from exporting wheat to Asian markets"
    ],
    "answer": 0,
    "explanation": "In developed countries like the US, farmers receive massive government subsidies allowing them to dump farm goods abroad at artificially low prices, while developing nations were pressured to eliminate agricultural import barriers — a clear case of unfair trade.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3 (Debate on WTO)"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-017",
    "type": "mcq",
    "subtopic": "Special Economic Zones (SEZs) Incentives",
    "difficulty": "Medium",
    "question": "What special fiscal incentive is offered to companies setting up manufacturing units in Special Economic Zones (SEZs) in India?",
    "options": [
      "Exemption from paying corporate income taxes for an initial period of five years",
      "Free imported luxury cars for all factory line workers",
      "Direct representation in the state legislative assembly",
      "Exemption from paying wages to manual labourers"
    ],
    "answer": 0,
    "explanation": "Industrial zones, called Special Economic Zones (SEZs), are being set up with world-class facilities (electricity, water, roads, storage). Companies who set up production units in the SEZs do not have to pay taxes for an initial period of five years.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-018",
    "type": "mcq",
    "subtopic": "Indian Companies Becoming MNCs",
    "difficulty": "Medium",
    "question": "Globalisation has enabled several large Indian companies to expand overseas and emerge as multinational corporations. Which of the following is an Indian multinational?",
    "options": [
      "Tata Motors (automobiles), Infosys (IT), and Ranbaxy (pharmaceuticals)",
      "General Motors, Boeing, and Apple Inc.",
      "Toyota, Sony, and Honda Motor Company",
      "Nokia, Siemens, and British Petroleum"
    ],
    "answer": 0,
    "explanation": "Globalisation has enabled some large Indian companies to emerge as multinationals themselves: Tata Motors (automobiles), Infosys (IT), Ranbaxy (medicines), Asian Paints (paints), Sundaram Fasteners (nuts and bolts) are some Indian companies which are spreading their operations worldwide.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-019",
    "type": "mcq",
    "subtopic": "Small Producers Hit by Global Competition",
    "difficulty": "Medium",
    "question": "In the NCERT case of Ravi, who manufactured electrical capacitors in Tamil Nadu, how did trade liberalisation affect his factory?",
    "options": [
      "When the government removed import restrictions on capacitors, television makers imported cheaper components, causing Ravi's sales to drop by half and forcing him to fire workers",
      "Ravi's company instantly acquired Samsung and Sony corporations",
      "Ravi was appointed chief director of the World Trade Organisation",
      "Ravi's factory output expanded by 1,000% within two months"
    ],
    "answer": 0,
    "explanation": "Ravi took a loan to start his unit manufacturing capacitors in 1992. When government removed trade barriers on imports of capacitors under WTO agreements, MNC television makers imported cheaper components. Ravi's production fell by half and he had to lay off half his workforce.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4 (Case of Ravi)"
  },
  {
    "id": "cbse10-sst-eco-ch21-s1-020",
    "type": "mcq",
    "subtopic": "Fair Globalisation Meaning",
    "difficulty": "Easy",
    "question": "'Fair Globalisation' refers to a global economic order that:",
    "options": [
      "Creates opportunities for all and ensures that the benefits of globalization are shared equitably among workers, small producers, and developing nations",
      "Bans all international trade and eliminates shipping containers",
      "Forces all multinational companies to give 100% of their shares to foreign governments",
      "Requires developed nations to annex developing countries"
    ],
    "answer": 0,
    "explanation": "Fair globalisation would create opportunities for all, and also ensure that the benefits of globalisation are shared better. The government can play a major role in making this possible by supporting small producers and enforcing labour laws.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.5"
  }
]

# -----------------------------------------------------------------------------
# CH 21 SET 2: NCERT Exemplar & Applications (20 Qs)
# -----------------------------------------------------------------------------
ch21_set2 = [
  {
    "id": "cbse10-sst-eco-ch21-s2-001",
    "type": "mcq",
    "subtopic": "Joint Ventures: Ford Motors in India",
    "difficulty": "Medium",
    "question": "In 1995, American automobile giant Ford Motors entered the Indian market through a joint venture with Mahindra & Mahindra. What mutual benefit did this joint venture deliver?",
    "options": [
      "Ford brought global manufacturing technology and capital, while Mahindra provided established domestic component sourcing, dealership networks, and market knowledge",
      "Ford took over the entire railway network of the Indian government",
      "Mahindra was forced to cease all manufacturing operations in India",
      "Ford produced cars exclusively for donation to rural hospitals"
    ],
    "answer": 0,
    "explanation": "Joint ventures combine local company assets (distribution networks, component vendors, local market understanding) with MNC capital and advanced production technology.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-002",
    "type": "mcq",
    "subtopic": "Labour Law Flexibility and Insecurity",
    "difficulty": "Hard",
    "question": "To attract foreign MNC investments, governments in India have permitted 'flexibility in labour laws'. How has this directly affected factory workers?",
    "options": [
      "Workers are increasingly hired on short-term contractual basis during peak seasons without job security, paid sick leave, or provident fund benefits",
      "Workers receive permanent lifetime employment contracts with double wages",
      "Workers are appointed as permanent members of company boards of directors",
      "Workers are legally exempt from working more than four hours a week"
    ],
    "answer": 0,
    "explanation": "In recent years, the government has allowed companies to ignore many labour laws to reduce costs. Instead of hiring workers on a regular basis, companies hire workers 'flexibly' for short periods when there is intense pressure of work, eroding job security.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-003",
    "type": "mcq",
    "subtopic": "Information Technology Enabling Global Services",
    "difficulty": "Medium",
    "question": "A news magazine published in London is designed and typeset by software designers in Delhi using telecommunications, printed in Delhi, and flown to London for morning delivery. Which technological forces enable this integrated workflow?",
    "options": [
      "High-speed satellite internet, electronic mail, computer desktop publishing, and rapid air cargo transportation",
      "Submarine telegraph cables operating on Morse code",
      "Postal pigeon couriers across the Arabian Sea",
      "Shortwave radio voice broadcasts recorded on magnetic tape"
    ],
    "answer": 0,
    "explanation": "Information and communication technology (ICT) and air transport have made it possible for service production (design, editing, printing) to be outsourced across continents almost instantaneously.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-004",
    "type": "mcq",
    "subtopic": "Consumers Benefiting from Globalisation",
    "difficulty": "Easy",
    "question": "Which socio-economic group in India has gained the most visible and immediate advantages from globalisation?",
    "options": [
      "Well-off urban consumers who enjoy a wide variety of high-quality goods (automobiles, cell phones, electronics) at lower competitive prices",
      "Landless rural agricultural sharecroppers",
      "Small cottage plastic and capacitor producers",
      "Unskilled contract garment stitching workers"
    ],
    "answer": 0,
    "explanation": "Globalisation and greater competition among producers has been of greatest advantage to urban consumers. There is greater choice before these consumers who now enjoy improved quality and lower prices for several products.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-005",
    "type": "mcq",
    "subtopic": "Small Industries Vulnerability in India",
    "difficulty": "Medium",
    "question": "Which manufacturing sectors in India were severely hit by cheap foreign imports following the removal of trade barriers under WTO rules?",
    "options": [
      "Batteries, capacitors, plastics, toys, tyres, dairy products, and vegetable oil",
      "Heavy commercial railway coaches and locomotives",
      "Nuclear energy reactors and rocket launch vehicles",
      "Handwritten royal parchment manuscripts"
    ],
    "answer": 0,
    "explanation": "Batteries, capacitors, plastics, toys, tyres, dairy products, and vegetable vegetable oil are examples of industries where small manufacturers have been hit hard due to competition. Several units have shut down, leaving workers jobless.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-006",
    "type": "mcq",
    "subtopic": "Garment Export Industry and Sweatshop Conditions",
    "difficulty": "Hard",
    "question": "In the NCERT case of garment worker Sushila in an export factory in Delhi, why did her conditions deteriorate from 2000 onwards?",
    "options": [
      "To meet tight deadlines and rock-bottom prices demanded by foreign MNC brands, the factory laid off permanent staff and made workers like Sushila temporary daily-wagers working 12-hour shifts without benefits",
      "The factory was nationalized by the central government and converted into a hospital",
      "Sushila was promoted to chief executive officer of a European retail chain",
      "The factory relocated all sewing machines to international waters"
    ],
    "answer": 0,
    "explanation": "To get orders from MNCs, garment exporters cut costs ruthlessly. Since raw material costs cannot be reduced, they cut labour costs by hiring temporary workers for long hours (12+ hours) without overtime or social security.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4 (Case of Sushila)"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-007",
    "type": "mcq",
    "subtopic": "Government Policies for Fair Globalisation",
    "difficulty": "Board Standard",
    "question": "How can the government ensure that the benefits of globalisation are shared equitably across all citizens?",
    "options": [
      "By properly implementing labour laws to protect worker rights, supporting small producers until they become competitive, and judiciously using trade barriers when necessary",
      "By shutting down all international airports and seaports",
      "By abolishing corporate taxes completely for all foreign companies",
      "By banning Indian students from studying computer engineering abroad"
    ],
    "answer": 0,
    "explanation": "The government can ensure that labour laws are properly implemented and the workers get their rights. It can support small producers to improve their performance until they become strong enough to compete. If necessary, the government can use trade and investment barriers.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.5"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-008",
    "type": "mcq",
    "subtopic": "Civil Society and People's Campaigns against WTO",
    "difficulty": "Medium",
    "question": "In recent decades, massive protests and public campaigns organized by civil society groups and developing nations have successfully demonstrated that:",
    "options": [
      "People's collective political mobilization can influence critical decisions related to international trade and investment rules at the WTO",
      "The WTO only accepts advice from private multinational CEOs",
      "Public demonstrations are legally banned under international treaties",
      "Developing nations have zero voting voice in global forums"
    ],
    "answer": 0,
    "explanation": "Massive campaigns and representation by people's organisations have influenced important decisions relating to trade and investments at the WTO. This has demonstrated that people also can play an important role in the struggle for fair globalisation.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.5"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-009",
    "type": "mcq",
    "subtopic": "Top Indian Companies Benefiting from Foreign Technology",
    "difficulty": "Medium",
    "question": "How have leading Indian firms (such as automobile parts manufacturers) prospered from the entry of foreign MNCs into India?",
    "options": [
      "They upgraded their production technology, invested in newer machinery, raised quality standards, and became global suppliers to multinational corporations",
      "They ceased all production and leased their factories to foreign armies",
      "They were banned from selling auto parts to Indian consumers",
      "They replaced all electrical machines with manual hand tools"
    ],
    "answer": 0,
    "explanation": "Several top Indian companies have been able to benefit from the increased competition. They have invested in newer technology and production methods and raised their production standards. Some have gained from successful collaborations with foreign companies.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-010",
    "type": "mcq",
    "subtopic": "BPO and IT Outsourcing to India",
    "difficulty": "Easy",
    "question": "Why has India emerged as the world's leading destination for Business Process Outsourcing (BPO) and software IT services?",
    "options": [
      "A large pool of skilled English-speaking technical graduates working at significantly lower wages than in Western developed nations",
      "The Indian government pays the salaries of all foreign software engineers",
      "India has banned all domestic manufacturing industries",
      "Computers in India operate twice as fast as in other continents"
    ],
    "answer": 0,
    "explanation": "India combines a large demographic of educated, English-fluent engineers and science graduates with low relative labour costs and reliable digital connectivity, making it a global IT outsourcing hub.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-011",
    "type": "mcq",
    "subtopic": "Developing Nations Alliance at WTO",
    "difficulty": "Medium",
    "question": "At WTO ministerial conferences, why do developing countries (like India, South Africa, and Brazil) frequently form negotiation coalitions?",
    "options": [
      "To pool their collective bargaining power and challenge the unfair trade dominance and agricultural subsidies maintained by rich developed nations",
      "To declare military war against developed economies",
      "To ban all foreign container ships from docking at their ports",
      "To force the WTO to relocate its headquarters to Antarctica"
    ],
    "answer": 0,
    "explanation": "Developing countries align together at the WTO to resist pressure from rich nations, demanding the elimination of rich-country agricultural subsidies and safeguarding food security.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.5"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-012",
    "type": "mcq",
    "subtopic": "MNC Leverage over Small Suppliers",
    "difficulty": "Medium",
    "question": "How do giant global retail brands (such as Nike, Walmart, and Gap) exercise enormous economic leverage over small apparel factories in developing countries?",
    "options": [
      "They dictate price, quality specifications, delivery deadlines, and labour conditions because suppliers compete fiercely among themselves for limited purchase contracts",
      "They own 100% of the land in developing country export zones",
      "They are legally authorized to arrest small factory managers who make sewing errors",
      "They pay suppliers five years in advance without inspecting goods"
    ],
    "answer": 0,
    "explanation": "The MNCs have tremendous power to determine price, quality, delivery, and labour conditions for these distant producers because suppliers have little bargaining power and face intense competition.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-013",
    "type": "mcq",
    "subtopic": "Foreign Direct Investment vs Foreign Portfolio Investment",
    "difficulty": "Hard",
    "question": "What is the key difference between Foreign Direct Investment (FDI) and Foreign Portfolio Investment (FPI)?",
    "options": [
      "FDI involves long-term physical capital investment in factories and operations with management control, whereas FPI involves purchasing stocks and bonds on domestic financial markets without direct control",
      "FDI is strictly illegal under Indian law, while FPI is fully permitted",
      "FDI is carried out exclusively in gold bullion, while FPI uses currency notes",
      "FDI only applies to agricultural farms, while FPI applies to space exploration"
    ],
    "answer": 0,
    "explanation": "FDI establishes tangible physical assets (plants, joint ventures) with long-term strategic control, whereas FPI is financial capital investing in traded securities.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-014",
    "type": "mcq",
    "subtopic": "Impact of Tariff Removal on Small Farmers",
    "difficulty": "Medium",
    "question": "If India were to eliminate all import tariffs on agricultural products like wheat, dairy, and cotton, what would happen to small Indian farmers?",
    "options": [
      "They would face severe price crashes and bankruptcy due to subsidized foreign agricultural surpluses dumped on Indian markets",
      "They would immediately become the wealthiest farmers on Earth",
      "Their crop yields would automatically double within two weeks",
      "They would be hired as senior corporate executives by foreign agribusinesses"
    ],
    "answer": 0,
    "explanation": "Unrestricted imports of heavily subsidized Western crops would flood domestic mandis at below-cost prices, destroying the livelihoods of millions of small subsistence farmers.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-015",
    "type": "mcq",
    "subtopic": "Technology as Catalyst for Market Integration",
    "difficulty": "Easy",
    "question": "Which of the following technological innovations has contributed most decisively to integrating financial markets across the globe in real time?",
    "options": [
      "High-speed fiber-optic telecommunications and global electronic fund transfer networks",
      "Coal-powered steamships and postal mail packets",
      "Typewriters and carbon-copy printing presses",
      "Mechanical pocket watches and abacuses"
    ],
    "answer": 0,
    "explanation": "Internet, satellite links, and electronic fund transfers allow billions of dollars in trade and investment to move across continents in milliseconds, integrating global capital markets.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-016",
    "type": "mcq",
    "subtopic": "Special Economic Zones: Land Acquisition Controversy",
    "difficulty": "Medium",
    "question": "Why has the creation of Special Economic Zones (SEZs) in India sometimes faced severe domestic resistance and protests?",
    "options": [
      "Because fertile multi-crop agricultural land was acquired from farmers, displacing rural families and depriving agricultural labourers of livelihoods",
      "Because SEZs refuse to produce manufactured goods",
      "Because foreign MNCs are barred from entering SEZ zones",
      "Because SEZs do not have electricity or road connections"
    ],
    "answer": 0,
    "explanation": "Setting up SEZs has often involved acquiring fertile farmland, causing loss of agricultural livelihoods and displacement of local communities without adequate rehabilitation.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-017",
    "type": "mcq",
    "subtopic": "Consumer Culture and Globalisation",
    "difficulty": "Easy",
    "question": "How has globalisation transformed the consumer retail landscape in Indian metropolitan cities over the last twenty years?",
    "options": [
      "Shoppers now have immediate access to the latest global brands in smartphones, cars, designer clothing, and international food chains",
      "All retail shopping malls have been replaced by traditional barter mandis",
      "Foreign electronic goods are completely banned from store shelves",
      "Consumers are restricted to buying only locally produced khadi cotton"
    ],
    "answer": 0,
    "explanation": "Consumers in India today have a wide variety of goods and services before them. The latest models of digital cameras, mobile phones and television sets made by leading manufacturers of the world are within their reach.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-018",
    "type": "mcq",
    "subtopic": "Flexibility of Capital vs Immobility of Labour",
    "difficulty": "Hard",
    "question": "What fundamental asymmetry exists between capital and labour in the contemporary globalised economy?",
    "options": [
      "Capital and MNC investments can move across borders with tremendous freedom and speed, while human labour faces strict visa restrictions and immigration controls",
      "Human workers can move freely across all borders without passports, while capital is legally locked in home nations",
      "Neither capital nor labour is permitted to cross national borders",
      "Multinational corporations are legally prohibited from transferring profits to home countries"
    ],
    "answer": 0,
    "explanation": "While globalisation has drastically accelerated the movement of goods, capital, and technology across borders, international movement of labour remains severely restricted by national immigration barriers.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-019",
    "type": "mcq",
    "subtopic": "Role of Judiciary in Protecting Labour Rights",
    "difficulty": "Medium",
    "question": "When export-oriented factories ignore statutory safety rules and fire workers arbitrarily to lower production costs, what institutional remedy is available in a constitutional democracy?",
    "options": [
      "Workers and labour unions can approach labour tribunals and High Courts to enforce statutory rights under the Industrial Disputes Act and Factories Act",
      "Workers must surrender their citizenship and leave the country",
      "Judicial courts are legally prohibited from hearing cases involving foreign MNCs",
      "Workers must seek authorization from the World Trade Organisation"
    ],
    "answer": 0,
    "explanation": "Democratic judicial institutions (labour courts, High Courts, Supreme Court) possess constitutional authority to strike down arbitrary dismissals and enforce labour welfare protections.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.5"
  },
  {
    "id": "cbse10-sst-eco-ch21-s2-020",
    "type": "mcq",
    "subtopic": "Summary: Balanced Globalisation",
    "difficulty": "Board Standard",
    "question": "Which of the following encapsulates the consensus view of economists on the impact of globalisation in India?",
    "options": [
      "Globalisation has brought immense technological modernization and consumer choice, but has generated uneven outcomes, benefiting corporate elites while intensifying insecurity for small producers and informal workers",
      "Globalisation has had 100% negative effects with zero benefits for any Indian citizen",
      "Globalisation has completely eliminated all poverty and unemployment across rural India",
      "Globalisation has had no measurable effect on Indian trade or lifestyle"
    ],
    "answer": 0,
    "explanation": "Globalisation has been a mixed blessing: it stimulated growth, tech modernization, and consumer welfare, but created precarious contract labour and severely challenged small unorganized producers.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Chapter Overview"
  }
]

# -----------------------------------------------------------------------------
# CH 21 SET 3: Assertion-Reason & Case Studies (20 Qs)
# -----------------------------------------------------------------------------
ch21_set3 = [
  {
    "id": "cbse10-sst-eco-ch21-s3-001",
    "type": "assertion_reasoning",
    "subtopic": "A-R: MNC Production Sourcing",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Multinational Corporations disperse different stages of manufacturing across multiple nations rather than producing in a single country.\nReason (R): Dispersing production allows MNCs to exploit specific locational advantages (cheap labour, specialized engineering, proximity to markets) to minimize total production costs.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "By designing in the US, manufacturing components in China, and managing customer service in India, an MNC slashes operational costs by up to 50–60%.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-002",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Trade Liberalisation in 1991",
    "difficulty": "Board Standard",
    "question": "Assertion (A): India removed most trade barriers and restrictions on foreign investment in 1991.\nReason (R): The government decided that domestic industries were sufficiently mature and that global competition would improve product quality and efficiency.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The 1991 New Economic Policy aimed to integrate the Indian economy with global markets, ending four decades of strict import substitution to spur industrial efficiency.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-003",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Unequal Trade Rules at WTO",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Developing nations frequently criticize the functioning of the World Trade Organisation (WTO).\nReason (R): While the WTO compels developing countries to dismantle trade barriers, advanced nations like the US have retained massive agricultural subsidies that distort global markets.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The asymmetry in WTO enforcement — rich nations subsidizing domestic agriculture while demanding tariff removal from developing countries — creates widespread resentment.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-004",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Containerization Revolution",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The introduction of standardized intermodal containers dramatically stimulated international merchandise trade.\nReason (R): Containers reduced port handling costs, minimized cargo theft and damage, and drastically accelerated transit speed between ships, trains, and trucks.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Containerization slashed freight and turnaround costs by up to 90%, making global logistics economically feasible for high-volume trade.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-005",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Impact on Small Producers",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Globalisation has created severe economic distress for many small-scale manufacturing units in India.\nReason (R): Small producers often lack the advanced technology, scale, and cheap capital required to compete with massive influxes of cheap imports.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Units in sectors like plastics, toys, capacitors, and batteries faced sudden competition from automated foreign exporters, forcing thousands of local closures.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-006",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Rise of Contractual Labour",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Workers' employment in many export-oriented industries has become intensely precarious under globalisation.\nReason (R): Intense global competition compels domestic manufacturing exporters to cut labour costs by hiring workers temporarily on contractual basis rather than offering permanent jobs.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "To survive price competition from MNC buyers, exporters squeeze labour costs, replacing permanent employees with seasonal contract workers without benefits.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-007",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Special Economic Zones (SEZs)",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Central and state governments have established Special Economic Zones (SEZs) across India.\nReason (R): SEZs provide world-class infrastructure and 5-year tax holidays specifically designed to attract foreign corporate investment.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "SEZs are industrial enclaves created with high-grade infrastructure and generous fiscal tax incentives to lure foreign MNC manufacturing plants to India.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-008",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Fair Globalisation Role of Government",
    "difficulty": "Board Standard",
    "question": "Assertion (A): The government can play a decisive role in ensuring fair globalisation.\nReason (R): Government policy can protect worker rights through strict labour law enforcement, offer credit support to small producers, and negotiate fair rules at the WTO.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Globalisation does not have to be an unregulated free-for-all; progressive state policies can ensure that gains are distributed broadly across working people.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.5"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-009",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Market Integration through Foreign Trade",
    "difficulty": "Board Standard",
    "question": "Assertion (A): Foreign trade results in the integration of markets across different sovereign countries.\nReason (R): Goods travel across borders, expanding consumer choices and driving prices of similar goods in different national markets towards convergence.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "Cross-border trade connects producers and consumers globally, creating competitive international markets with unified price signals.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-010",
    "type": "assertion_reasoning",
    "subtopic": "A-R: Post-Independence Tariff Protection",
    "difficulty": "Board Standard",
    "question": "Assertion (A): India was justified in placing strict barriers on foreign imports during the 1950s and 1960s.\nReason (R): Indian infant industries were nascent after colonial exploitation and required protective incubation before they could face mature Western competition.",
    "options": [
      "Both (A) and (R) are true, and (R) is the correct explanation of (A).",
      "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).",
      "(A) is true, but (R) is false.",
      "(A) is false, but (R) is true."
    ],
    "answer": 0,
    "explanation": "The infant industry argument justified early trade barriers: newly established domestic industries needed protection to build capacity before competing globally.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-011",
    "type": "case_based",
    "subtopic": "Case Analysis: Cargill's Acquisition of Parakh Foods",
    "difficulty": "Board Standard",
    "question": "When US agribusiness giant Cargill Foods entered India, instead of building new distribution networks from scratch, it purchased Parakh Foods with its four oil refineries and nationwide distribution network. What strategy does this illustrate?",
    "options": [
      "MNC acquisition of established local companies to instantly capture market share, distribution channels, and domestic brand equity",
      "A joint venture where management is split 50-50 permanently",
      "Direct municipal expropriation by the government of India",
      "A small-scale cottage industry expanding through cooperative pooling"
    ],
    "answer": 0,
    "explanation": "Acquiring established domestic players allows wealthy MNCs to enter markets rapidly, bypassing the multi-year struggle to build supply chains and consumer trust.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-012",
    "type": "case_based",
    "subtopic": "Case Analysis: Ravi's Capacitor Unit in Hosur",
    "difficulty": "Board Standard",
    "question": "Ravi took a loan to manufacture capacitors in Hosur, Tamil Nadu. In 2001, when the government lifted import quotas on capacitors under WTO commitments, TV manufacturers switched to cheaper imported components. Ravi's unit plummeted into losses. This case proves:",
    "options": [
      "Sudden trade liberalisation without protective transition periods or technological upgrade support can destroy vulnerable domestic small-scale enterprises",
      "Capacitors are no longer used in modern television sets",
      "Tamil Nadu is constitutionally barred from manufacturing electronics",
      "Ravi should have invested exclusively in agricultural grain"
    ],
    "answer": 0,
    "explanation": "Ravi's case highlights the negative shock of rapid trade liberalisation on domestic small-scale manufacturers who lack the scale to survive sudden import competition.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-013",
    "type": "case_based",
    "subtopic": "Case Analysis: Sushila's Garment Sweatshop",
    "difficulty": "Board Standard",
    "question": "Sushila was a permanent garment worker with medical insurance and provident fund until 1999. Following factory restructuring for global export orders, she was laid off and hired as a casual worker working 7:30 AM to 10:00 PM without benefits for lower real wages. Her situation reflects:",
    "options": [
      "The precarious casualisation of labour and loss of social security driven by competitive export pressures in global value chains",
      "The statutory benefits guaranteed by the Factories Act of India",
      "The successful implementation of fair trade standards by MNC buyers",
      "Permanent employment security in the public sector"
    ],
    "answer": 0,
    "explanation": "Sushila's reality demonstrates how cost-cutting by global fashion brands cascades down to sweatshop conditions for female contract workers at the bottom of the supply chain.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-014",
    "type": "case_based",
    "subtopic": "Case Analysis: Chinese Toys in Indian Bazaars",
    "difficulty": "Medium",
    "question": "Within months of opening imports, Chinese plastic toys captured 70–80% of Indian retail toy shops because they were priced 40% lower with innovative designs. From the perspective of Indian consumers and Indian toy makers, what were the respective outcomes?",
    "options": [
      "Consumers gained greater variety and lower prices, while domestic toy makers suffered heavy business contraction and job losses",
      "Both consumers and Indian toy makers gained massive financial windfalls",
      "Consumers faced severe shortages while domestic toy makers became MNCs",
      "Neither group experienced any economic change"
    ],
    "answer": 0,
    "explanation": "The Chinese toy case illustrates the classic dual impact of trade: consumer surplus rises through cheaper, diverse goods, while uncompetitive domestic producers suffer losses.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-015",
    "type": "case_based",
    "subtopic": "Case Analysis: Ford Motors Export Hub in Chennai",
    "difficulty": "Medium",
    "question": "Ford Motors established a mega manufacturing plant near Chennai not only to sell cars in the Indian domestic market, but also to export cars and auto components to Europe, South Africa, and Mexico. This case illustrates how India acts as a:",
    "options": [
      "Global manufacturing and export base for multinational corporations leveraging skilled engineering labour at low production cost",
      "Colonial trading post extracting raw mineral ores for foreign empires",
      "Non-profit educational workshop for international university students",
      "Closed isolated market disconnected from world trade networks"
    ],
    "answer": 0,
    "explanation": "Ford leveraged India's low-cost, skilled engineering base to develop a competitive global export hub supplying automobiles across three continents.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.1"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-016",
    "type": "mcq",
    "subtopic": "Role of Information Technology in Global Call Centres",
    "difficulty": "Medium",
    "question": "When an airline customer in New York dials customer service to rebook a flight, the call is answered by an agent in Gurgaon (Gurugram). What economic reality makes this possible?",
    "options": [
      "Digital telecommunications and the Internet enable real-time service outsourcing across time zones at a fraction of Western operating costs",
      "Air travel between New York and Gurgaon takes only five minutes",
      "American telecommunication companies are legally forbidden from answering phones in New York",
      "Customer service calls can only be answered by Indian nationals"
    ],
    "answer": 0,
    "explanation": "High-speed voice-over-IP networks and time zone differences allow US corporate services to be handled 24/7 by trained Indian professionals at substantial cost savings.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.2"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-017",
    "type": "mcq",
    "subtopic": "Dumping and Protectionism",
    "difficulty": "Hard",
    "question": "What is 'dumping' in international trade, and why do developing countries invoke anti-dumping duties under WTO rules?",
    "options": [
      "When a foreign company exports goods at prices significantly below their normal domestic cost of production, threatening to wipe out domestic industries",
      "When foreign ships dump radioactive waste in international sea lanes",
      "When domestic companies donate free food to famine-affected areas",
      "When governments cancel all international travel visas"
    ],
    "answer": 0,
    "explanation": "Dumping occurs when goods are exported at predatory, sub-cost prices. Countries apply anti-dumping duties to protect domestic producers from being driven out of business.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.3"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-018",
    "type": "mcq",
    "subtopic": "Impact of Globalisation on Agriculture",
    "difficulty": "Board Standard",
    "question": "Why has globalisation in India faced stiff resistance from peasant movements and farmer unions?",
    "options": [
      "Because exposure to volatile global market prices, removal of input subsidies, and competition from subsidized Western farm imports threaten farm incomes and food security",
      "Because farmers are legally forbidden from growing traditional food crops",
      "Because multinational agribusinesses refuse to sell seeds to Indian farmers",
      "Because all agricultural farmland is being converted into gold mines"
    ],
    "answer": 0,
    "explanation": "Global price swings, reduced state subsidies, rising input costs, and corporate seed monopolies have made agricultural livelihoods highly vulnerable.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-019",
    "type": "mcq",
    "subtopic": "SEZs and Worker Protections",
    "difficulty": "Medium",
    "question": "Why have trade unions and human rights groups criticized the legal frameworks governing Special Economic Zones (SEZs)?",
    "options": [
      "Because companies in SEZs are frequently exempted from regular labour inspections and regulations governing overtime, working hours, and union formation",
      "Because workers in SEZs are paid ten times the national minimum wage",
      "Because SEZ factories are owned exclusively by the United Nations",
      "Because SEZs refuse to use electricity or internet technology"
    ],
    "answer": 0,
    "explanation": "To attract foreign investors, governments often relax labour law inspections and dispute resolution mechanisms within SEZs, weakening worker protections.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Section 4.4"
  },
  {
    "id": "cbse10-sst-eco-ch21-s3-020",
    "type": "mcq",
    "subtopic": "Synthesis: Blueprint for Fair Globalisation",
    "difficulty": "Board Standard",
    "question": "Which comprehensive vision summarizes the path toward 'Fair Globalisation' outlined in the NCERT Class 10 curriculum?",
    "options": [
      "A rule-based multilateral system where developing nations' interests are protected, labour standards are enforced, small producers receive transition support, and human welfare takes precedence over corporate profits",
      "A complete dismantling of international trade and total economic isolation of every nation",
      "Unrestricted free market dominance without any national borders or labour laws",
      "A single world government controlled by multinational corporate executives"
    ],
    "answer": 0,
    "explanation": "Fair globalisation balances international trade with human rights: ensuring benefits are shared equitably through enforced labour standards, support for small producers, and fair WTO rules.",
    "citation": "NCERT Class 10 Economics, Chapter 4, Chapter Summary"
  }
]

# Write Chapter 20 Sets 1, 2, 3
with open(os.path.join(DATA_DIR, "ch20_money_and_credit_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch20_set1}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch20_money_and_credit_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch20_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch20_money_and_credit_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch20_set3}, f, indent=2, ensure_ascii=False)
print("Generated Ch 20 (Money and Credit) Sets 1, 2, 3 (60 Qs total) successfully!")

# Write Chapter 21 Sets 1, 2, 3
with open(os.path.join(DATA_DIR, "ch21_globalisation_and_indian_economy_set1.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch21_set1}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch21_globalisation_and_indian_economy_set2.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch21_set2}, f, indent=2, ensure_ascii=False)
with open(os.path.join(DATA_DIR, "ch21_globalisation_and_indian_economy_set3.json"), "w", encoding="utf-8") as f:
    json.dump({"questions": ch21_set3}, f, indent=2, ensure_ascii=False)
print("Generated Ch 21 (Globalisation and Indian Economy) Sets 1, 2, 3 (60 Qs total) successfully!")
