# Academic Subject Matter Expert (SME) Sign-Off Gate
**Document Reference:** `MTV-QA-GATE-v2.9.115`  
**Target Platform:** MockTestVault (`mocktestvault.com`)  
**Status:** **GATE ACTIVE (PRODUCTION BLOCKED PENDING SME CERTIFICATION)**  
**Technical Status:** **PASSED (100% Verified on Staging)**  

---

## 1. Executive Protocol: Two-Gate Architecture

MockTestVault strictly enforces a decoupled release policy separating **Technical Production Readiness** from **Academic Content Certification**. Production deployment is strictly conditional upon passing both independent gates:

```
+-------------------------------------------------------------+
|             GATE 1: TECHNICAL DEPLOYMENT READINESS           |
|  - Headless Browser Testing & Zero Console Errors           |
|  - Single H1 Hierarchy & Schema.org JSON-LD Validation       |
|  - Google Consent Mode v2 & CMP Preference Triggers         |
|  - 0 Broken Internal Links Across 160 HTML Pages            |
|  - Hostinger LiteSpeed .htaccess, Rewrites & Cache Rules   |
|  - Mobile Viewport (375px) Zero-Overflow Validation         |
+-------------------------------------------------------------+
                              |
                     [ STATUS: PASSED ]
                              |
                              v
+-------------------------------------------------------------+
|           GATE 2: ACADEMIC SME CONTENT-CERTIFICATION         |
|  - NCERT 2026-27 Rationalized Curriculum Congruence        |
|  - 6,404 Question Bank Factual Correctness & Answer Keys    |
|  - PYQ Authenticity & Shift-Label Disclaimers               |
|  - Assertion-Reasoning Explanation Directionality            |
|  - Marking Scheme & Formula Step Concordance                |
+-------------------------------------------------------------+
                              |
                     [ STATUS: PENDING ]
                              |
                              v
                [ FINAL PRODUCTION DEPLOYMENT ]
```

---

## 2. Gate 1: Technical Production Readiness (PASSED)

The technical infrastructure for baseline `v2.9.115` has been audited, patched, regression-tested in headless Google Chrome, and deployed to the isolated Hostinger staging target (`domains/mocktestvault.com/public_html/staging`):

| Technical Requirement | Audit Target | Result | Evidence |
| :--- | :--- | :---: | :--- |
| **HTML Hierarchy** | 160 HTML Files | **100% PASS** | Exactly 1 `<h1>` tag on every page; zero missing headings |
| **Internal Linking** | All Internal Links | **100% PASS** | 0 broken relative or absolute internal links |
| **Privacy Compliance** | Google Consent Mode v2 | **100% PASS** | `consent.js` present on all 160 pages; CMP modal operational |
| **Footer Preferences** | Cookie Settings Trigger | **100% PASS** | 160/160 pages feature `.open-cookie-preferences` link |
| **Viewport & Mobile** | 375px Viewport Emulation | **100% PASS** | Missing viewport added to `progress.html`; zero horizontal overflow |
| **JSON Question Banks**| 337 JSON Files | **100% PASS** | 0 syntax errors; all 337 files valid UTF-8 JSON |
| **Web Server Config** | LiteSpeed `.htaccess` | **100% PASS** | Staging `noindex` guard active; internal dev CSVs blocked |
| **Browser Runtime** | Chrome CDP Headless | **100% PASS** | 9/9 core test suites passed with 0 console errors |

---

## 3. Gate 2: Academic SME Content-Certification Scope

Before releasing version `v2.9.115` from Staging to Production, academic Subject Matter Experts must review and sign off on the 5 subject streams comprising the active question banks:

### Scope of Academic Certification:
1. **CBSE Class 10 Science (13 Chapters, 39 Sets, 780 Questions):**
   - **SME Task:** Validate NCERT 2026–27 alignment. Confirm that rationalized chapters (Periodic Classification, Sources of Energy, Sustainable Management) remain omitted from active chapter rosters.
   - **Assertion-Reasoning:** Verify that directionality in Section A items follows the standard 4-option rubric (Option A: Both true and Reason is correct explanation; Option B: Both true but Reason is NOT correct explanation; Option C: True/False; Option D: False/True).
   - **Reactions & Equations:** Confirm state symbols `(s)`, `(l)`, `(g)`, `(aq)` and stoichiometry in Chapter 1 & 2 explanation popups.

2. **CBSE Class 10 Mathematics (14 Chapters, 42 Sets, 840 Questions):**
   - **SME Task:** Validate that quadratic equations, trigonometry, statistics, and circles solutions use current NCERT formulas.
   - **Unit vs Chapter Weightage:** Confirm that chapter cards do not publish misleading rigid chapter-wise marks, but reflect official CBSE unit marks distributions.

3. **CBSE Class 10 Social Science (21 Chapters, 63 Sets, 1,260 Questions):**
   - **SME Task:** Verify history, geography, political science, and economics questions against revised NCERT editions.
   - **Map Items & Statistics:** Verify economic data points (World Bank per-capita income figures, HDI parameters) are explicitly cited with publication years.

4. **SSC CGL Tier 1 Full Mocks & Sectional Banks (1,800 Questions):**
   - **SME Task:** Review shift-labelled 2023 items. Verify that the disclaimer on `question-sources-review.html` correctly classifies unverified shift items as practice material rather than authenticated verbatim Commission papers.
   - **Answer Keys:** Audit quantitative aptitude and reasoning keys against standard mathematical proofs.

5. **US & Global Standards (SAT Math, AP, IELTS, GRE - 1,724 Questions):**
   - **SME Task:** Review Digital SAT Math practice sets against College Board specifications (Algebra, Advanced Math, Problem-Solving, Geometry & Trigonometry).

---

## 4. SME Review Registers & Working Backlog

Academic reviewers must record all findings and approvals in the standardized audit registers:

1. `QUESTION_ANSWER_VERIFICATION_REGISTER_v2.9.csv` (Overall Answer Key Register)
2. `PYQ_AUTHENTICATION_REGISTER_v2.9.csv` (Source & Past-Year Paper Provenance)
3. `QUESTION_REVIEW_BACKLOG_BY_FILE_v2.9.csv` (Chapter-by-Chapter Review Log)
4. `QUESTION_DUPLICATE_REVIEW_REGISTER_v2.9.csv` (Near-Duplicate Item Adjudications)
5. `QUESTION_EXPLANATION_VARIANCE_REGISTER_v2.9.csv` (NCERT Explanation Concordance)

---

## 5. Production Unblock Criteria

The production deployment script `./deploy_mocktestvault.sh` and GitHub Pages `main` branch sync remain **LOCKED** until the following certification block is signed by the Lead Academic Reviewer:

```
=====================================================================
            ACADEMIC CONTENT SIGN-OFF CERTIFICATION
=====================================================================
I hereby certify that I have reviewed the question banks, answer keys,
explanations, and curriculum alignments for MockTestVault v2.9.115.

Academic Lead Name: _____________________________________________
Institution / Specialization: ___________________________________
Date of Sign-off: _______________________________________________
Approved Scope: [ ] CBSE 10  [ ] CBSE 12  [ ] SSC CGL  [ ] SAT/Global
Sign-off Signature / Token: ____________________________________
=====================================================================
```

Once this certification is countersigned, proceed to Section 4 of `mocktestvault_v2.9.115_staging_and_production_readiness.md` to trigger the production deployment.
