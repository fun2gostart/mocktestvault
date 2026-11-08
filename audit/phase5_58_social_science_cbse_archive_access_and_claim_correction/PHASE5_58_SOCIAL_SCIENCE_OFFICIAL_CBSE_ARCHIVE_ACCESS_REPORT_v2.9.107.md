# Phase 5.58 — Social Science Official CBSE Archive Access & PYQ Claim Correction

**Build:** v2.9.107  
**Baseline:** v2.9.106  
**Scope:** 2023- and 2024-labelled Social Science 80-question datasets (160 records)

## Outcome

The official CBSE previous-question-paper archive and marking-scheme archive were located. Their Class X Social Science entries and package URLs were verified from the CBSE archive pages. The actual archive assets are ZIP packages. The browser fetch rejected the question-paper ZIPs as unsupported compressed content, and direct runtime download attempts failed. The packages therefore could not be extracted or inspected.

**No individual question is authenticated as a PYQ in this phase.** No paper/set code, question number, or official marking-scheme answer match has been assigned. Five exact-phrase searches across selected representative stems returned no indexed results; this is recorded as inconclusive and is not treated as evidence that the questions never appeared.

## Dataset audit

- 2023-labelled dataset: 80 questions
- 2024-labelled dataset: 80 questions
- Total records: 160
- Exact official paper matches established: 0
- Official answer-key matches established: 0
- Records remaining unauthenticated: 160
- Question stems/options/answer indices/explanations changed: **0**

## Metadata and public-claim correction

For all 160 questions, legacy citation wording that implied an official CBSE board-paper source was withdrawn. Each record now explicitly says it is an independent CBSE-aligned practice question and is not authenticated as an exact CBSE board PYQ. The dataset-level `exam` labels were changed to year-labelled independent practice sets. Existing stable IDs, page routes and question content were retained.

The practice pages already described themselves as practice drills and their meta descriptions already disclosed that original paper and marking-scheme matches had not been completed; those page contents were not changed.

## Official source catalogue

| Year | Official question paper ZIP | Official marking scheme ZIP |
|---|---|---|
| 2023 | `https://www.cbse.gov.in/cbsenew/question-paper/2023/X/SOCIAL_SCIENCE.zip` | `https://www.cbse.gov.in/cbsenew/Marking-Scheme/2023/X/Social_Science_English_Medium.zip` |
| 2024 | `https://www.cbse.gov.in/cbsenew/question-paper/2024/X/SOCIAL_SCIENCE.zip` | `https://www.cbse.gov.in/cbsenew/Marking-Scheme/2024/X/Social_Science.zip` |

Official archive landing pages: `https://www.cbse.gov.in/cbsenew/question-paper.html` and `https://www.cbse.gov.in/cbsenew/marking-scheme.html`.

## Remaining blocker / next action

To complete exact authentication, the official ZIP packages must be retrieved and extracted. Then each question must be compared with all relevant paper sets, with the paper/set code and question number recorded, and answer choices checked against the corresponding official marking scheme. The 160 questions remain practice questions until that evidence exists. Human SME sign-off remains pending.

## Validation

- 80 + 80 question records confirmed.
- All 160 question IDs preserved.
- All question stems, options, answer indices and explanations preserved byte-for-byte at the field-value level.
- JSON parses successfully.
- ZIP integrity and archive entry-count checks performed after build.
- No deployment performed.
