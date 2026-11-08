# Phase 5.60 — Social Science Official Marking-Scheme Archive Review

**Candidate build:** v2.9.109 (audit-only)  
**Baseline:** v2.9.108 / Phase 5.59  
**Scope:** 160 2023-/2024-labelled Social Science practice records; newly supplied official source archives.

## Archive integrity and inventory

All three newly uploaded archives pass ZIP integrity testing (no corrupt member detected):

| Archive | Contents | PDFs | Integrity |
|---|---|---:|---|
| `Social_Science (4).zip` | 2024 marking schemes, English and Hindi | 30 | PASS |
| `Social_Science_English_Medium (1).zip` | 2023 marking schemes, English and Hindi | 30 | PASS |
| `SOCIAL_SCIENCE (3).zip` | 2024 question papers, English/Punjabi/Urdu | 21 | PASS |

The 2024 question-paper package contains 15 English papers for codes 32/1, 32/2, 32/4, 32/5 and 32/6, plus 3 Punjabi and 3 Urdu papers. The 2024 marking-scheme archive contains English and Hindi versions across 15 paper codes. The 2023 marking-scheme archive contains English and Hindi versions; the English filenames identify paper-code families 32/1, 32/2, 32/4, 32/5 and 32/6. See the source catalogue for SHA-256 hashes and exact package URLs.

## 2024 item-level key cross-check

The previously identified candidate `cbse10-pyq2024-sst-044` was checked against 2024 paper 32/5/2 and its corresponding marking-scheme PDF. The question paper's Question 4 has option C = 59%, which matches the dataset's selected answer text (59%) after option reordering. However, the marking-scheme PDF for code 32/5/2 prints Question 4 as `(C) I, II, IV, III`, a value-point description that does not correspond to the Belgium percentage question. The answer letter agrees, but the value-point text conflicts. **Classification: unresolved source/key discrepancy; not certified as an official answer-key match.** This item remains a paraphrased concept/option-overlap candidate, not an authenticated exact PYQ.

No exact item-level matches have been established for the remaining 2024 practice questions. A marking-scheme answer cannot be assigned to a practice question solely because it covers the same topic or shares a concept; an exact question/paper mapping is required.

## 2023 status

The 2023 marking-scheme archive is now valid and available. However, the 2023 question-paper ZIP remains missing/incomplete. Without the corresponding question papers, the 2023 marking-scheme entries cannot be reliably paired to the 80 practice questions by paper code and question number. All 80 remain unauthenticated and their official answer-key status remains unverified.

## Dataset and release controls

- All 160 questions retain their existing stems, options, answer indexes, explanations and stable IDs.
- No official PYQ claim is restored. Public wording remains independent CBSE-aligned practice, not authenticated as an exact board PYQ.
- No runtime code, page content, routes, scoring, SEO, sitemap, robots, analytics or advertising settings changed.
- No staging or production deployment performed.
- Human Social Science SME sign-off remains pending.

## Remaining evidence and next actions

1. Obtain the complete 2023 Class X Social Science question-paper ZIP from CBSE.
2. Resolve the 2024 32/5/2 Q4 marking-scheme text discrepancy using an independent official source or manual SME review; do not silently assume the key is correct based on the matching option letter.
3. Complete item-level matching for all 160 questions, then independently verify every selected answer and explanation.
4. Retain practice-only public claims until exact provenance and academic SME approval are documented.

**Release decision:** v2.9.109 is an audit-only candidate. Not approved for deployment.
