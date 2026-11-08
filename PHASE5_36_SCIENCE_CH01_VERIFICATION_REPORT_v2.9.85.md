# Phase 5.36 – Chapter 1 independent academic verification

- Baseline: v2.9.84
- Output: v2.9.85
- Scope: active quiz sets 1–3, 20 questions each (60 total).
- Method: independent chemistry/stoichiometry/Assertion–Reason review of each stem, option set, selected key and explanation; correction and recheck where required.

## Results

| Measure | Result |
|---|---:|
| Questions reviewed | 60 |
| Verified without content change | 46 |
| Distinct questions corrected | 14 |
| Field-level corrections | 20 |
| Answer-key corrections | 1 |
| Human academic sign-off pending | 60 |
| Official PYQ authentication pending | 60 |

## Material corrections

1. `cbse10-sci-ch01-s3-002`: corrected the Assertion–Reason key. Water's formula represents an atomic ratio, not a gas-volume ratio; the 2:1 gas-volume result follows from the balanced electrolysis equation.
2. `cbse10-sci-ch01-014`: corrected lead(II) chloride product state and solubility explanation (sparingly soluble solid).
3. `cbse10-sci-ch01-s2-014`: corrected the anode explanation: water is oxidised to oxygen; oxide ions are not the explanatory species in acidified aqueous electrolysis.
4. `cbse10-sci-ch01-s2-020`: replaced an oversimplified bond-energy explanation with the photosensitivity distinction between AgBr and NaCl.
5. `cbse10-sci-ch01-s3-012`: removed unsafe smell-identification wording for SO₂/SO₃ and substituted a moist-blue-litmus observation with a safety note.
6. `cbse10-sci-ch01-s3-020`: corrected the distinction between oxidative rancidity products and butyric acid, which is commonly associated with hydrolytic rancidity.
7. Additional wording/explanation refinements address quicklime suspension, nitrogen flushing, tin coating rationale, and imprecise superlative/terminology claims.

## Release controls and limitations

- Only the three active Chapter 1 set JSON files were changed. The chapter HTML loads these exact set files.
- The separate aggregate `science_ch01_chemical_reactions.json` was not changed because the active chapter UI references the three set files; it remains a separate legacy/aggregate artifact for a later source reconciliation.
- All 60 records are marked AI-assisted independently reviewed; human academic sign-off remains pending.
- NCERT topic references do not establish exact PYQ provenance. All 60 remain unauthenticated as official PYQs unless matched to original CBSE papers/marking schemes.
- This review does not constitute teacher/SME sign-off.
- No deployment performed.
