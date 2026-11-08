# MockTestVault – Phase 5.55 Social Science Source-Hold and Scope Resolution

Version: v2.9.104  
Baseline: v2.9.103  
Date: 2026-11-08

## Executive result

Phase 5.55 reconciled all **56 previously flagged Social Science records**. The 1,260-question bank and all 63 active sets were preserved. Targeted corrections were made to 28 question records; no question IDs were deleted or added.

- Flagged records adjudicated: **56/56**
- Prior supplementary flags reviewed and retained in the bank as enrichment (not Board-core): **40**
- Source/discrepancy flags adjudicated from Phase 5.54: **17**; three record-level residuals remain explicitly visible (two Gendathur aggregate records and one rice-ranking source conflict)
- Prior SME holds: **8** (six source/wording issues narrowed with evidence; two Civics items remain explicitly subject to human SME review)
- Historical-context flags: **6**
- Targeted content records amended: **28**
- Active Social Science questions: **1260**
- Active sets: **63**, all with 20 questions

## What was resolved

1. **IUCN category definition:** Updated the Endangered definition to the formal IUCN 'very high risk of extinction in the wild' definition.
2. **Endemic species:** Replaced the non-endemic Nicobar pigeon in the keyed pair with the Andaman wood pigeon; BirdLife/State of India's Birds identifies the latter as endemic to the Andaman and Nicobar archipelago.
3. **IUCN Vulnerable category:** Corrected the keyed pair to snow leopard and greater one-horned rhinoceros. The former Gangetic dolphin/Asian elephant pair is Endangered, not Vulnerable.
4. **Threatened plants:** Retained the original Madhuca insignis/Hubbardia heptaneuron pair after checking current evidence: World Flora Online's IUCN-sourced data lists M. insignis as Critically Endangered, and a 2015 BSI-authored field assessment classified H. heptaneuron as Critically Endangered after rediscovery.
5. **Consumption and environmental impact:** Removed the unsupported richest-5%-versus-poorest-25% comparison and the inaccurate claim that affluent groups bear almost no responsibility. The revised item tests the general link between high material consumption and environmental footprint.
6. **Forest diversion:** Reworded the Narmada Sagar item to use the Government of India-approved diversion figure of 41,111.97 hectares, rather than implying that the whole figure is the exact submerged area.
7. **Global water distribution:** Added UNEP support for the rounded 2.5% freshwater share and 68.7% of freshwater held in ice, glaciers and permanent snow.
8. **Hydropower share:** Preserved 22% only as an older NCERT textbook statement. CEA 2024–25 data report hydro at 8.15% of utility generation.
9. **Bamboo-drip irrigation:** Verified the approximate age, gravity-fed design, flow-rate examples, and crop pairing through Government of Meghalaya and NITI for States material. Corrected the confusion between betel vine and arecanut, and removed any implication that the system needs no maintenance.
10. **Gendathur:** Removed unsupported rainfall/collection-efficiency inputs from the question. The active item tests the textbook's per-household estimate only; the NCERT village aggregate remains flagged because it is arithmetically inconsistent.
11. **Tehri Dam:** Verified that the dam is on the Bhagirathi River through THDC; its CBSE map-work relevance is distinguished from an actual map-pointing question.
12. **Agriculture and manufacturing historical claims:** Added current context to the rice-ranking, Oil India, small-enterprise threshold, and National Jute Policy items. The old textbook values remain only where the stem explicitly asks for historical textbook recall.
13. **Civics wording:** Narrowed the endogamy and women's dignity Assertion–Reason items to align more closely with NCERT wording. Both remain pending human SME approval.

## CBSE 2026–27 scope decisions

The official CBSE Class X Social Science 2026–27 curriculum states: The Age of Industrialisation is Periodic Assessment only; Geography Chapters 2–6 are in Board course structure; Geography Chapter 7 (Lifelines of National Economy) is only map-pointing in the Board examination; Political Science chapters including Gender, Religion and Caste and Outcomes of Democracy are included; Economics Chapter 4 has only “What is Globalisation?” and “Factors that have enabled Globalisation” for Board evaluation, with the remaining listed themes assigned to interdisciplinary project work; Consumer Rights is project work.

For this Phase 5.55 set of 56 flagged records, all 40 records previously identified as supplementary are retained outside Board-core. In total, 47 flagged items are classified as supplementary or historical enrichment; three are retained as Board-theory historical textbook snapshots, two as Board-theory contextual case studies, two as Board-theory items pending SME review, one as Periodic Assessment only, and one as map-work-linked context that is not itself a map-pointing question. Chapter-level Board inclusion is not treated as proof that every related enrichment MCQ is itself Board-core. The Age of Industrialisation item remains Periodic Assessment only. Tehri's river association is retained as supplementary context. The embedded CBSE map-work table is labelled 2025–26, so exact 2026–27 map inclusion is not claimed.

The PDF's map-work table is explicitly headed 'CLASS X (2025–26)'; it is not used here as proof of a 2026–27 item-level map list.

Source: CBSE Class X Social Science (087), 2026–27 official curriculum PDF: https://cbseacademic.nic.in/web_material/CurriculumMain27/SecPart1/SocialScience_SecP1X_2026-27.pdf (course structure, PDF pp. 1–2; chapter learning outcomes, pp. 3–6; map work, pp. 6–7).

## Explicit unresolved controls

- **Human academic sign-off:** still pending for all 1,260 Social Science questions. No SME hold is treated as a human approval.
- **Official CBSE PYQ authentication:** not performed. Original paper/year/set/question-number and official marking-scheme matching remain separate work.
- **Human SME holds:** the endogamy and women's dignity Assertion–Reason items were narrowed to NCERT-aligned wording but remain pending human review; no AI source check is treated as a human sign-off.
- **Gendathur source inconsistency:** the textbook's 1,00,000-litre village aggregate for 200 houses conflicts with its approximately 50,000-litre per-household estimate. The aggregate was not used.
- **Rice-ranking source conflict:** two Government of India publications give different world-rank descriptions for India's 2024–25 rice output; the item remains supplementary historical textbook recall and is not a current ranking claim.
- **Current-statistic caveat:** historical textbook values (22% hydropower, second-place rice ranking, ₹1 crore small-industry threshold, old workforce share, old Oil India joint-sector classification) must not be represented as current data.
- **Supplementary material:** retained in the bank for enrichment; not promoted to current Board-core without item-level SME review.

## Technical validation

- ZIP integrity: passed (`testzip()` returned no errors).
- Active question sets: 63/63 parsed; each contains 20 questions.
- Active questions: 1260/1,260 parsed.
- Unique active IDs: 1,260/1,260.
- Answer indexes within option bounds: 1,260/1,260.
- Required stem/options/explanation fields: present across all active questions.
- Content corrections: 28 question records. All answer indexes remained unchanged; the vulnerable-species item's option at its existing keyed index was replaced with the correct Vulnerable pair.
- No scoring engine, login, payment, analytics, SEO, sitemap, robots or production deployment changes.

## Change control

The only source question-set JSON files modified were those containing the targeted flagged items. All other original archive entries were preserved byte-for-byte at the uncompressed file-content level. The service-worker cache identifier was advanced from `mtv-cbt-v86` to `mtv-cbt-v87` to invalidate stale cached question data.
