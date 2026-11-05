# MockTestVault – Question Accuracy & PYQ Provenance Audit v2.7
Audit date: 5 November 2026
Input: mocktestvault.com_organic_seo_v2.6.zip

## Headline result
- Question records: 6,404
- JSON files: 287
- Records structurally validated: 6,404
- Explicit explanation lines matching stored selected option: 392
- Explicit answer-label lines flagged for manual comparison: 0
- Records independently re-solved by a qualified subject reviewer in this pass: 0
- Records with an item-level official source URL present in the JSON: 0
- Year/shift-labelled records whose provenance is not authenticated in this release: 954

## What was checked
1. Every JSON file parsed.
2. Every question record has question text, an options array, an in-range answer index, and a non-empty explanation.
3. Where the explanation begins with an explicit `**Correct Answer: ...**` label, its text was compared to the stored selected option. 392 passed this internal consistency check. This does not validate the content against an external authority.
4. Existing targeted corrections from earlier releases were retained.

## Why full answer verification remains open
A source citation note such as a textbook chapter, syllabus topic or examination name does not prove an answer is correct. The current source ZIP contains no item-level direct source URLs, original question-paper files, official answer-key files, reviewer identity, or verification date for the majority of items. It would be misleading to mark 6,404 answers as independently verified from these fields alone.

Every question JSON object now includes `quality_review` metadata:
- `structural_validation`: passed
- `answer_accuracy_status`: pending independent subject-matter verification (unless it has a targeted correction note)
- `explanation_option_consistency`: result of the explicit answer-label consistency check
- `source_provenance_status`: source/provenance category
- `authority_reference_url`: authority reference where relevant; not an item-level authentication link
- `item_level_source_url_present`: false

## PYQ / board-paper authentication
The supplied release included SSC CGL 2023 shift-labelled data sets and CBSE 2023/2024 board-year-labelled data sets. The original SSC response sheets and final answer-key files are not included in the website ZIP. SSC's official 1 August 2023 notice states that candidate response sheets and tentative answer keys were made available through registered login credentials and would not remain available after the time window. The SSC Answer Key archive contains an entry for final answer keys and candidate response sheets for CGL Tier-I 2023. These official notices support that the process occurred; they do not prove that each question in the supplied JSON is an exact match to the original paper/key.

For CBSE year-labelled banks, official CBSE sample-paper archives are linked as exam-format/marking-scheme references. They do not validate the year-labelled records as exact questions from the actual annual board examination.

The affected citations and page language have therefore been changed to identify these records as year/shift-labelled practice material with unverified item-level provenance. Original citation notes are preserved in `legacy_citation_note` for audit history.

## Registers
- `QUESTION_ANSWER_VERIFICATION_REGISTER_v2.7.csv`: one row per question record.
- `PYQ_AUTHENTICATION_REGISTER_v2.7.csv`: year/shift-labelled records needing original-paper/key matching.
- `QUESTION_REVIEW_BACKLOG_BY_FILE_v2.7.csv`: file-level review queue.

## What is needed to close the remaining work
For a genuinely completed independent answer review, each item needs:
1. A trusted source document/official paper or textbook passage.
2. A direct source URL or archived document identifier and exact page/question reference.
3. A re-solved answer with reasoning.
4. Reviewer identity/role and review date.
5. A recorded outcome: verified, corrected, ambiguous, or source unavailable.

For SSC CGL 2023 items, original candidate response-sheet/question-paper exports and final answer-key records are required. For CBSE board-year-labelled banks, the exact paper set/code and official marking scheme for the year/subject are required. Without those artifacts, exact PYQ authenticity cannot be certified.

## Conclusion
v2.7 improves traceability and removes unsupported authentication claims. It does NOT claim that all 6,404 answers have been independently verified. That work remains open until authoritative item-level sources and subject review evidence exist.
