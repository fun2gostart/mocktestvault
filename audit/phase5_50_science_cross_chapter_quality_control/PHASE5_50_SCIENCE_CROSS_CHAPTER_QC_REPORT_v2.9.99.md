# Phase 5.50 – Science Cross-Chapter Quality Control

**Revision:** v2.9.99  
**Baseline:** v2.9.98  
**Scope:** 780 active Science question records across 13 chapters and 39 set files.  
**Content changes:** None. This is an audit-only revision; question content and answer keys were not modified.

## 1. Integrity and structural checks

- Active set files: **39/39**; each contains 20 questions.
- Questions: **{len(rows)}/780**; unique IDs: **{len(set(r["id"] for r in rows))}**.
- Exact duplicate normalized question stems across chapters: **{len(exact)} groups**.
- Structural failures (four options, valid zero-based answer index, non-empty explanation): **{len(bad)}**.
- Missing topic-level citation field: **{len(missing_cite)}**.
- Missing subtopic field: **{len(missing_topic)}**.

## 2. Near-duplicate candidate screening

- Cross-chapter candidate pairs at character n-gram cosine similarity >= 0.78: **0**.
- These are automated lexical candidates only, not confirmed duplicates. They require manual semantic review before merging or deleting anything.
- No content was removed or rewritten on the basis of similarity alone.

## 3. Answer-position distribution

- Across all 780 questions, answer positions A/B/C/D: **287/156/170/167**.
- Individual set distributions are in the attached CSV. Sets with any one answer position at >=50% are flagged for review. This is a test-design risk indicator, not evidence of wrong answer keys.

## 4. Metadata reconciliation warning

The active set files carry inconsistent `quality_review.answer_accuracy_status` values across chapters. The counts below reproduce the status actually stored in the 780 active set records; they do not override the chapter audit registers. This is a metadata governance issue and should be reconciled before treating the master tracker as authoritative.

- Chapter 01: ai_assisted_independent_solution_verified_human_signoff_pending: 60
- Chapter 02: pending_independent_subject_matter_verification: 60
- Chapter 03: pending_independent_subject_matter_verification: 60
- Chapter 04: ai_assisted_independent_subject_matter_reviewed: 60
- Chapter 05: ai_assisted_independent_solution_match_human_signoff_pending: 60
- Chapter 06: ai_assisted_independent_concept_check_passed: 60
- Chapter 07: ai_assisted_independent_solution_match_human_signoff_pending: 60
- Chapter 08: pending_independent_subject_matter_verification: 60
- Chapter 09: ai_assisted_independent_solution_verified: 60
- Chapter 10: ai_assisted_independent_answer_review_completed_human_signoff_pending: 60
- Chapter 11: ai_assisted_independent_answer_review_pass_human_academic_signoff_pending: 60
- Chapter 12: independently_reviewed_consistent: 45; independently_reviewed_corrected: 15
- Chapter 13: independently_reviewed_answer_key_consistent: 60

## 5. Aggregate/compatibility JSON comparison

The following unsuffixed chapter JSON files are present alongside the 39 active `_set1/_set2/_set3` files. They are not a complete 60-question union in this archive; the comparison below records their actual overlap and content drift. A source-code search did not find literal references to these filenames, but this alone does not prove they are unused. Do not overwrite/delete them without tracing runtime loading paths.

- `ch01_chemical_reactions.json`: 20 rows vs 60 rows across its three sets; missing from unsuffixed file 40; extra 0; differing shared records 20.
- `ch02_acids_bases_salts.json`: 20 rows vs 60 rows across its three sets; missing from unsuffixed file 40; extra 0; differing shared records 20.
- `ch03_metals_non_metals.json`: 20 rows vs 60 rows across its three sets; missing from unsuffixed file 40; extra 0; differing shared records 0.
- `ch04_carbon_compounds.json`: 20 rows vs 60 rows across its three sets; missing from unsuffixed file 40; extra 0; differing shared records 0.
- `ch05_life_processes.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch06_control_coordination.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch07_how_organisms_reproduce.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch08_heredity.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch09_light_reflection_refraction.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 0.
- `ch10_human_eye_colourful_world.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch11_electricity.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch12_magnetic_effects_electric_current.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 5.
- `ch13_our_environment.json`: 5 rows vs 60 rows across its three sets; missing from unsuffixed file 55; extra 0; differing shared records 0.

## 6. Question type and difficulty metadata

- Question type counts: mcq: 558, assertion_reasoning: 154, case_study: 8, case-study: 60.
- Difficulty labels: Easy: 217, Medium: 311, Hard: 146, Board Standard: 106.
- The `case-study` and `case_study` labels are inconsistent and should be normalised only after confirming the frontend schema accepts one canonical value.

## 7. Recommended actions

1. Manually adjudicate the near-duplicate candidate CSV; preserve legitimate context variations.
2. Reconcile all 780 `quality_review` statuses against the chapter registers and maintain a single canonical status vocabulary.
3. Review answer-position distributions flagged at >=50%; shuffle options only after independently revalidating each key and explanation.
4. Trace whether unsuffixed JSON files are loaded by any route, build script, or fallback; if active, regenerate them from the authoritative sets and run regression tests.
5. Normalise question-type labels after code/schema trace.
6. Continue to keep human academic sign-off and exact official CBSE PYQ authentication as separate gates.

## 8. Limitations

This phase performs structural, metadata, lexical-overlap and distribution checks. It does not independently solve all 780 questions again, authenticate exact CBSE PYQ provenance, or constitute human academic sign-off. No live site or deployment environment was accessed.
