# MockTestVault Question Originality & Answer Review – v2.5

Date: 5 November 2026
Source reviewed: MockTestVault Organic SEO v2.4 ZIP

## Scope inspected
- 287 JSON files parsed successfully.
- 6,404 question-like records identified in the source release.
- Each inspected record had a non-empty question, at least two options, an answer field,
  a non-empty explanation and a non-empty citation field.
- All inspected answer indexes were within their option arrays.
- Exact normalized question-stem repetitions were compared across files.
- Repeated records were not automatically deleted: many are intentional copies between
  sectional question banks and corresponding full mocks, or mirrored data paths.

## Originality changes
Six repeated stems crossing independent practice/PYQ or separate mock-test families
were replaced in the practice mock source and its full-mock copy:
1. Mock 01 English: CANDID synonym → ABUNDANT synonym.
2. Mock 01 English: METICULOUS antonym → RELUCTANT antonym.
3. Mock 01 Reasoning: 15 August 2021 calendar question → 1 January 2024/2025 calendar question.
4. Mock 02 Reasoning: 7, 11, 20, 36, 61 series → 3, 8, 18, 38, 78 series.
5. Mock 03 English: “burn the candle at both ends” → “break the ice”.
6. Mock 03 Reasoning: 15 August 2011/2012 calendar question → 1 March 2023/2024 calendar question.

The existing question IDs and record metadata were retained so the site's test structure
continues to reference the same records.

## Answer/explanation corrections
1. Ferrous sulphate heating:
   - Corrected selected answers in three question-bank/sample-paper records.
   - The correct observation describes loss of water of crystallisation, followed by formation
     of reddish-brown ferric oxide and evolution of sulphur oxides.
   - Updated the explanation and NCERT chapter/activity citation.
2. Pole and shadow:
   - Corrected three explanations that described an unrelated 60-degree/15-metre problem.
   - Correct reasoning: tan(theta) = height/shadow = 1, therefore theta = 45 degrees.

## Validation after edits
- All JSON files parse.
- Question counts and required fields were checked.
- Answer indexes were checked against option counts.
- Edited question IDs were found in each intended source/full-mock file.
- ZIP integrity test passed.

## Important limits
This is a source-level audit and targeted correction pass, not a claim that all 6,404 answers
have been independently re-solved or checked by a qualified subject expert. A non-empty citation
field is not proof that the cited source supports every claim. Questions requiring specialist
knowledge, official exam-paper provenance, or visual diagrams still need subject-matter review.
Verify PYQ labels against original official examination papers before describing an item as an
actual previous-year question.

Exact repeated stems remain where they appear to be intentional sectional/full-mock copies,
mirrored files, or generic prompts with different options. Do not remove these automatically
without checking runtime data references.


Superseded by v2.7: see QUESTION_ACCURACY_AND_PYQ_AUDIT_v2.7.md and the per-question registers. No item is represented as independently verified unless a reviewer/source record supports that status.
