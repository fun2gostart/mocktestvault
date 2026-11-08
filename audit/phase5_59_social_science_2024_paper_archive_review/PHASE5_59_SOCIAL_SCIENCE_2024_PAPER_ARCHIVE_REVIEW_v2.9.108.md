# Phase 5.59 — Social Science 2024 Official Question-Paper Archive Review

**Build:** v2.9.108 (audit-only candidate)  
**Baseline:** v2.9.107  
**Scope:** 2023- and 2024-labelled Social Science question datasets; 160 records.

## Source package integrity

Four source archives were re-submitted. SHA-256/MD5 comparison against the previous upload batch showed that all four are byte-identical to the earlier files.

- 2024 Social Science question-paper package (`SOCIAL_SCIENCE.zip`): valid ZIP; 21 PDFs extracted successfully.
- 2023 Social Science question-paper package (`SOCIAL_SCIENCE (1).zip`): invalid/incomplete ZIP; no end-of-central-directory record.
- 2023 English-medium marking-scheme package (`Social_Science_English_Medium.zip`): invalid/incomplete ZIP; no end-of-central-directory record.
- 2024 Social Science marking-scheme package (`Social_Science (2).zip`): invalid/incomplete ZIP; no end-of-central-directory record.

The valid question-paper package contains 15 English-medium papers across paper-code families 32/1, 32/2, 32/4, 32/5 and 32/6 (three sets each), plus 3 Punjabi and 3 Urdu versions. All 21 PDF files were extracted and text-inspected. The archive itself passed ZIP integrity testing.

## 2024 paper comparison

- 80 2024-labelled dataset questions compared against the 15 English-medium 2024 paper PDFs.
- No exact verbatim item match was established.
- One strong paraphrased concept/option-overlap candidate was identified:
  - Dataset ID: `cbse10-pyq2024-sst-044`
  - Candidate source: Q.P. Code `32/5/2`, Question 4
  - Paper asks what percentage of Belgium's population lives in the Flemish region; the dataset asks the percentage living in the Flemish region and speaking Dutch.
  - Both include 59% as an answer option, although option ordering differs.
  - Classification: `STRONG_PARAPHRASED_CONCEPT_MATCH_CANDIDATE_NOT_EXACT_PYQ`.
  - This is not certified as an exact PYQ. The 2024 marking-scheme archive was invalid/incomplete, so the official key was not inspected.
- Three additional topic overlaps were recorded but explicitly rejected as item-level matches:
  - French Revolution collective identity (paper 32/4/2 Q25 vs dataset 2024-001).
  - Silk Route advantages (paper 32/4/2; dataset 2024-012 asks a different question).
  - Different developmental goals (paper 32/4/3 Q24 vs dataset 2024-064 asks a different MCQ).
- The remaining 76 questions had no exact item match identified in the reviewed English-medium papers. This is not proof of absence; the comparison was limited to supplied papers and text extraction.

## 2023 status

The 80 2023-labelled records remain unauthenticated. The re-uploaded 2023 paper ZIP is byte-identical to the earlier incomplete file and cannot be extracted. No paper codes, question numbers or answer-key matches were assigned.

## Answer-key status

No official marking-scheme answer match was established for any of the 160 records. Both marking-scheme packages in the upload batch are invalid/incomplete ZIPs. No answer indexes, options, stems, explanations or stable question IDs were changed.

## Public-claim and release controls

- All 160 records retain the corrected public claim: independent CBSE-aligned practice question; not authenticated as an exact CBSE board PYQ.
- The single strong paraphrased candidate is recorded internally only; no PYQ claim is restored.
- No question content, runtime code, page routes, scoring, SEO, sitemap, robots, analytics or ad settings changed.
- No staging or production deployment performed.
- Human SME sign-off remains pending.

## Next required evidence

1. A complete 2023 question-paper ZIP.
2. A complete 2023 English-medium marking-scheme ZIP.
3. A complete 2024 marking-scheme ZIP.
4. After receipt: inspect official keys and resolve candidate matches; retain all public claims as practice-only until exact provenance and SME approval are established.
