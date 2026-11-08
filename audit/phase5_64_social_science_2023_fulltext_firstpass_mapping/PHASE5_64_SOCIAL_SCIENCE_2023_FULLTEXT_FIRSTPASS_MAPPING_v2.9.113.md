# Phase 5.64 — Social Science 2023 full-text first-pass mapping

**Candidate:** v2.9.113 (audit-only)  
**Baseline:** v2.9.112 / Phase 5.63  
**Scope:** 80 questions labelled 2023; 15 English paper sets and available 2023 marking schemes.

## Text coverage established

- 15 English paper PDFs inventoried across code families 32/1, 32/2, 32/4, 32/5 and 32/6.
- Full document text is available for **11 of 15** sets: 9 PDFs with embedded text and 2 scanned PDFs processed with Tesseract OCR.
- **2 additional sets** have only partial OCR artifacts; **2 sets** still lack full-document OCR.
- Punjabi and Urdu PDFs were not used for the English-language question-bank match.

## Automated first-pass screening

All 80 2023-labelled dataset questions were screened against the 11 full-text English sets plus the two sets with partial OCR text, using normalized token-set similarity. The two partial sets are supplemental evidence only; they are not complete paper coverage. This is a triage method only; it is not an authentication algorithm.

- High-score candidates (score >=82): **7**.
- Lower-confidence topic/phrase overlaps (65–81.9): **31**.
- No strong automated overlap (<65): **42**.
- The seven high-score candidates were manually inspected. They contain overlap in component phrases or subject concepts, but the complete question structure and task do not match the official paper item. They are therefore **not certified as exact or paraphrased PYQs**.
- No new item-level paper match or official marking-scheme answer match is certified in this phase.

## Important limits

- The full-text screen is incomplete because four English sets do not yet have complete searchable text (two partial OCR, two not fully OCR processed).
- Similarity scores can be inflated by short repeated textbook phrases and answer-option fragments. They must not be interpreted as match probabilities.
- Official marking schemes are available, but without a confirmed paper-code/question-number mapping, a key line cannot be attributed to a dataset item safely.
- The earlier separately recorded 2023 paper 32/5/2 Q4 / 59% candidate remains in the prior evidence trail; this phase does not broaden or silently alter that finding.

## Disposition

- 80 questions remain independent practice items, not authenticated PYQs.
- No question text, options, answer indexes, explanations, IDs, citations or public claims were changed.
- No runtime, SEO or production files were modified.
- No staging or production deployment performed.

## Next steps

1. Complete full-page OCR for the remaining four English sets (two partial and two not processed).
2. Review all 80 items against all 15 paper sets using page-level evidence and controlled paraphrase adjudication.
3. Only after a paper-code/question-number match, pair the exact final marking-scheme PDF and record accepted answer evidence.
4. Escalate any year mismatch or paraphrase candidate to the Social Science SME; retain public practice-only claims until sign-off.

**Release decision:** audit-only checkpoint; not approved for staging or production.
