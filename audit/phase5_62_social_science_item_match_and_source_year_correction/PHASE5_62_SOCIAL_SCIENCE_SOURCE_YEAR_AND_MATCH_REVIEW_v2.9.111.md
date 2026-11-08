# Phase 5.62 — Social Science source-year reconciliation and item-level evidence checkpoint

**Candidate:** v2.9.111 (audit-only)  
**Baseline:** v2.9.110 / Phase 5.61  
**Scope:** Reconcile uploaded CBSE source archives, correct a prior year attribution, and verify the strongest candidate against the corresponding paper and marking scheme.

## Critical source-year correction

A fresh inspection of PDF contents and metadata shows that the 21-PDF archive uploaded as `SOCIAL_SCIENCE (5).zip` (and duplicate `SOCIAL_SCIENCE (3).zip`) is the **2023 question-paper archive**, not a 2024 archive. The English papers carry 2023 paper codes and the inspected 32/5/2 paper title page identifies Q.P. Code 32/5/2; its PDF creation date is March 2023. The `Social_Science_English_Medium (1).zip` archive contains **2023 marking schemes**. The `Social_Science (4).zip` archive contains **2024 marking schemes**.

**No valid 2024 question-paper archive is present in the currently uploaded files.** Accordingly, the earlier Phase 5.59/5.60 descriptions that treated the 2023 paper PDFs as 2024 papers are superseded by this correction. Phase 5.61's statement that the new upload resolved 2023 question-paper availability is correct in substance, but the earlier source-role interpretation in Phase 5.60 must not be relied on for 2024 question-paper availability.

## Verified item-level finding

The prior candidate `cbse10-pyq2024-sst-044` is demonstrably aligned to a **2023** official item, not a 2024 item:

- Official paper: Class X Social Science, Q.P. Code **32/5/2**, Question **4**.
- Official paper wording: asks what percentage of Belgium's population lives in the Flemish region.
- Dataset wording: asks what percentage of the total population lives in the Flemish region and speaks Dutch; options are reordered.
- Official 2023 marking scheme for Set 32/5/2, Question 4: **(c) 59%**.
- Dataset selected answer text: **59 percent**.

Classification: **strong paraphrased source match with correct official key, but year-label mismatch**. This is not verbatim reproduction and must not be represented as an exact PYQ until an academic SME confirms the paraphrase and approves any year/provenance correction. The stable ID contains `2024`; no ID or question data was silently changed.

Three other earlier topic-overlap flags (2024-labelled IDs 001, 012 and 064) are now understood to have been compared against the supplied **2023** papers. They remain topic-only overlaps, not item matches.

## Coverage status

- 2023 question papers: valid archive received, 15 English papers across code families 32/1, 32/2, 32/4, 32/5 and 32/6, plus 3 Punjabi and 3 Urdu versions.
- 2023 marking schemes: valid archive received, English and Hindi versions.
- 2024 marking schemes: valid archive received, English and Hindi versions.
- 2024 question papers: **not received in a valid archive**.
- 160-item complete mapping: **not complete**. Full OCR, question-number mapping, code-by-code key pairing, and answer/explanation review remain pending. The 2023 paper PDFs are image-based scans; partial OCR was used to confirm the 32/5/2 Q4 match. Do not treat the single verified match as a full-bank audit.

## Release controls

- All public labels remain practice-only / not authenticated as exact CBSE PYQs.
- No question stems, options, answer indexes, explanations or IDs were changed.
- No runtime, SEO, routing, scoring or site files were changed.
- No staging or production deployment performed.
- Human Social Science SME sign-off remains pending.

## Required next work

1. Complete OCR and item-level matching of all 80 2023-labelled questions against the 15 English 2023 papers and matching code-specific marking schemes.
2. Obtain the official 2024 Class X Social Science question-paper archive before assessing the 80 2024-labelled questions as 2024 items.
3. Review the `cbse10-pyq2024-sst-044` year/provenance discrepancy with an academic SME; preserve the stable ID unless a controlled migration is approved.
4. Verify all answer indexes and explanations independently before changing any answer or public PYQ claim.

**Release decision:** audit-only candidate; not approved for staging or production.
