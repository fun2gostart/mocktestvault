# Phase 5.61 — Social Science 2023 Official Question-Paper Archive Intake

**Candidate build:** v2.9.110 (audit-only)  
**Baseline:** v2.9.109 / Phase 5.60  
**Scope:** Intake of the missing 2023 Class X Social Science question-paper archive and update of the 160-item evidence register.

## Archive integrity and inventory

The newly uploaded `SOCIAL_SCIENCE (5).zip` passes ZIP integrity testing (`ZipFile.testzip() = None`).

- ZIP size: 40,693,057 bytes
- SHA-256: `fb78dcf753a676f9b1a2a6a7125b568854b6c98606703d74355dcec9bab7f22f`
- Entries: 22 (one directory plus 21 PDFs)
- English-medium papers: 15 across codes 32/1, 32/2, 32/4, 32/5 and 32/6 (three sets per family)
- Punjabi papers: 3 (42/2/1–42/2/3)
- Urdu papers: 3 (48-4-1–48-4-3)
- The English PDFs report 23–32 pages each. Metadata includes March 15, 2023 creation dates for most files; the 32/4 files show January 12, 2023 metadata. File metadata is corroborative only and is not treated as proof of official provenance by itself.

Official package URL: https://www.cbse.gov.in/cbsenew/question-paper/2023/X/SOCIAL_SCIENCE.zip

## Effect on the 160-item review

The missing-source blocker is resolved: the 2023 question-paper archive is now available alongside the 2023 and 2024 marking-scheme archives and the 2024 question-paper archive.

However, archive receipt is not item-level authentication. The 80 records labelled 2023 are now marked as having a valid official-source archive supplied, but exact set/code and question-number matching remain pending. Official final-key matches also remain pending until each practice question is mapped to its exact paper item and corresponding marking-scheme row.

The 80 records labelled 2024 retain their Phase 5.60 classifications, including the unresolved 32/5/2 Question 4 marking-scheme discrepancy for `cbse10-pyq2024-sst-044`. No answer-key match is promoted on topic similarity or answer-letter coincidence alone.

## Data and claim controls

- No question stems, options, answer indexes, explanations or IDs changed.
- No PYQ authentication claim was added.
- Public descriptions remain independent practice / not authenticated as exact CBSE PYQs.
- Human SME sign-off remains pending.
- No runtime, SEO, routing, deployment or production files changed.
- No production or staging deployment performed.

## Next verification steps

1. OCR and compare all 15 English 2023 paper sets against the 80 2023 practice questions, recording exact paper code, question number and match class.
2. Pair only established question matches to the corresponding 2023 official marking-scheme code and row.
3. Resolve the 2024 32/5/2 Q4 value-point discrepancy against an authoritative corrected/final source or keep it unresolved.
4. Run a second-person academic SME review before changing any public PYQ claim.
