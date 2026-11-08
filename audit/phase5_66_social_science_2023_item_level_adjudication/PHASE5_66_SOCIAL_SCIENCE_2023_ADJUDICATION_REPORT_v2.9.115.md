# Phase 5.66 — Social Science 2023 item-level adjudication queue

**Candidate:** v2.9.115 (audit-only)
**Baseline:** v2.9.114 / Phase 5.65

## Work completed

- Re-screened all 80 2023-labelled Social Science questions against the full-text/OCR corpus for all 15 English paper sets (code families 32/1, 32/2, 32/4, 32/5 and 32/6).
- Generated the top-five source-text candidate passages for each item (400 retrieval candidates) to support human page-level review.
- Added an 80-item manual adjudication queue and carried candidate file/score into the 160-item evidence register.
- Kept paper question number, exact match, paraphrased match and answer-key pairing unassigned unless a full item-level comparison can be made.

## Findings and controls

- This retrieval pass is a navigation aid, not proof of source. Character n-gram similarity is particularly vulnerable to common assertion/reason answer-option boilerplate and repeated curriculum terminology.
- The top candidate scores are generally low; the highest scores are still not sufficient to certify a PYQ.
- **No new exact or paraphrased PYQ matches are authenticated in this phase.**
- The 2023 marking-scheme archive is available, but official key pairing cannot be safely done until the matching paper code and question number are established.
- The 2024 question-paper archive remains unavailable; 2024-labelled questions remain unauthenticated.
- No question stems, options, answer indexes, explanations, IDs, runtime files, SEO pages or public claims were changed.
- No staging or production deployment. Human Social Science SME sign-off remains pending.

## Next required action

Review candidate passages against rendered PDF pages, question-by-question and set-by-set. Record the actual paper code, question number, exact/paraphrased/related-topic/no-match classification, then pair the corresponding marking-scheme entry and verify the dataset answer independently.

**Disposition:** 80-item 2023 visual adjudication remains open; all public labels remain independent practice, not authenticated PYQ.
