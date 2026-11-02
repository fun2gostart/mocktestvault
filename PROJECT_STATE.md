# MockTestVault (`mocktestvault.com`) — Technical Architecture & Project State Specification

> **Live Production URL:** [https://mocktestvault.com/](https://mocktestvault.com/)  
> **Repository:** `fun2gostart/mocktestvault` (Branch: `main`)  
> **Global Edge CDN:** GitHub Pages Global CDN  
> **Production Cloud VPS:** Hostinger Cloud VPS (`46.202.161.192:65002`)  
> **Target Path on Server:** `domains/mocktestvault.com/public_html/`  
> **Automated Deployers:** `./deploy_to_github.sh` & `./deploy_mocktestvault.sh`  
> **Status:** 100% Operational & Live in Production  
> **Current Scale:** 90 Production Routes | 3,870+ Ground-Truth Verified Questions across 3 Focus Pillars | 4 Dynamic Shuffled Random Mock Simulators | 5 Legal Trust Hubs  

---

## 1. Executive Summary & Philosophy

**MockTestVault** is a free, open-access, distraction-free Computer-Based Testing (CBT) mock examination simulator engineered for secondary school curriculums, national competitive exams, and global standardized tests.

### The Distraction-Free Academic Architecture
Unlike traditional commercial test portals plagued with auto-playing video interstitials, paid subscription paywalls, and incorrect user-submitted keys:
1. **Focused Examination Environment:** Zero video popups, zero countdown locks, and clean non-disruptive test layouts. Equipped with pre-engineered zero-CLS display ad wrappers ready for clean post-approval monetization.
2. **Authentic CBT Engines:** Faithful reproduction of official testing interfaces (TCS iON for India, College Board / Desmos methods for US, Cambridge IELTS pattern for Global).
3. **Statutory NCERT & Board Grounding:** Every question is cross-referenced against statutory textbooks with chapter and page citations.
4. **100% In-Browser Privacy:** Runs entirely in browser memory with client-side state machines. No mandatory registration or phone number harvesting.

---

## 2. 3-Pillar Regional Topology

MockTestVault deploys a structured 3-pillar international architecture with dedicated regional hubs and localized scoring engines:

| Regional Pillar | Dedicated Hub URL | Core Exams & Qualifications | Engine Specs & Scoring Rule | Status |
| :--- | :--- | :--- | :--- | :--- |
| **🇺🇸 United States** | [`/us/`](https://mocktestvault.com/us/) | Digital SAT® (Math & Reading), AP® Exams (Calculus, Physics, US History), GRE® | Module timing (32 mins / 20 Qs), 1600-scale conversion, zero negative marking penalty | Live (`200 OK`) |
| **🇮🇳 India** | [`/in/`](https://mocktestvault.com/in/) | CBSE Class 10 Board (48 Chapters), SSC CGL Tier 1 | TCS iON 4-section tabs, official +2.0 / -0.5 negative penalty engine, NCERT citations | Live (`200 OK`) |
| **🌐 Global Standards** | [`/global/`](https://mocktestvault.com/global/) | Cambridge IELTS® Academic, TOEFL® iBT, GRE® General, IB Diploma | True/False/Not Given logic, Heading Matching, Band 7.5 to 9.0 conversion scale | Live (`200 OK`) |

---

## 3. Curriculum & Examination Inventory (2,940+ Questions Live)

### A. CBSE Class 10 Board Vault (100% Complete — 48 Chapters, 2,880 Questions)
Every chapter contains 3 progressive sets of 20 questions (60 Qs/chapter): Set 1 (Core Concepts & Board PYQs), Set 2 (NCERT Exemplar & Numericals), Set 3 (Assertion-Reasoning & Case Studies).

* **Science (13 Chapters — 39 Sets, 780 Questions):**
  * Ch 1: Chemical Reactions & Equations (Pgs 1–16)
  * Ch 2: Acids, Bases & Salts (Pgs 17–36)
  * Ch 3: Metals & Non-Metals (Pgs 37–56)
  * Ch 4: Carbon & Its Compounds (Pgs 57–78)
  * Ch 5: Life Processes (Pgs 79–112)
  * Ch 6: Control & Coordination (Pgs 113–128)
  * Ch 7: How do Organisms Reproduce? (Pgs 129–144)
  * Ch 8: Heredity & Evolution (Pgs 145–158)
  * Ch 9: Light — Reflection & Refraction (Pgs 159–188)
  * Ch 10: Human Eye & Colourful World (Pgs 189–200)
  * Ch 11: Electricity (Pgs 201–222)
  * Ch 12: Magnetic Effects of Electric Current (Pgs 223–240)
  * Ch 13: Our Environment (Pgs 241–250)

* **Mathematics (14 Chapters — 42 Sets, 840 Questions):**
  * Ch 1: Real Numbers (Euclid's & Fundamental Theorem)
  * Ch 2: Polynomials (Zeroes & Coefficients)
  * Ch 3: Linear Equations in Two Variables
  * Ch 4: Quadratic Equations (Roots & Discriminants)
  * Ch 5: Arithmetic Progressions ($a_n$ and $S_n$)
  * Ch 6: Triangles (BPT & Similarity)
  * Ch 7: Coordinate Geometry (Distance & Section Formula)
  * Ch 8: Introduction to Trigonometry
  * Ch 9: Some Applications of Trigonometry (Heights & Distances)
  * Ch 10: Circles (Tangent Theorems 10.1 & 10.2)
  * Ch 11: Areas Related to Circles (Sectors & Segments)
  * Ch 12: Surface Areas & Volumes (Combinations of Solids)
  * Ch 13: Statistics (Mean, Median, Mode)
  * Ch 14: Probability (Classical Probability & Events)

* **Social Science (21 Chapters — 63 Sets, 1,260 Questions):**
  * *History:* Ch 1 (Nationalism in Europe), Ch 2 (Nationalism in India), Ch 3 (Global World), Ch 4 (Age of Industrialisation), Ch 5 (Print Culture).
  * *Geography:* Ch 6 (Resources & Development), Ch 7 (Forest & Wildlife), Ch 8 (Water Resources), Ch 9 (Agriculture), Ch 10 (Minerals & Energy), Ch 11 (Manufacturing Industries), Ch 12 (Lifelines of National Economy).
  * *Political Science:* Ch 13 (Power Sharing), Ch 14 (Federalism), Ch 15 (Gender, Religion & Caste), Ch 16 (Political Parties), Ch 17 (Outcomes of Democracy).
  * *Economics:* Ch 18 (Development), Ch 19 (Sectors of Indian Economy), Ch 20 (Money & Credit), Ch 21 (Globalisation & Indian Economy).

### B. Competitive & Standardized Simulators (620 Questions Live)
* **Staff Selection Commission (SSC CGL Tier 1 — 200 Questions):**
  * Full Mock 01 (100 Questions, 60 Mins, 4 Sections, TCS iON Palette)
  * 4 Sectional Speed Drills: Reasoning (25 Qs), Quant (25 Qs), English (25 Qs), General Awareness (25 Qs)
* **United States Pillar (400 Questions across 24 Production Routes — 100 Questions Per Exam + 4 Dedicated Random Mocks):**
  * **Digital SAT® Math (100 Questions — 5 Modules + Dynamic Random Mock, 32 Mins each, Desmos methods):**
    * Module 01: Core Diagnostic (`sat/math-practice-01.html`)
    * Module 02: Algebra & Functions (`sat/math-practice-02.html`)
    * Module 03: Advanced Math & Geometry (`sat/math-practice-03.html`)
    * Module 04: 700–800 Score Benchmark (`sat/math-practice-04.html`)
    * Module 05: 1600 Master Suite (`sat/math-practice-05.html`)
    * 🎲 **Random 20-Q Mock:** Dynamic shuffled exam sampled from 100-Q pool (`sat/math-practice-random.html`)
  * **Digital SAT® Reading & Writing (100 Questions — 5 Modules + Dynamic Random Mock, 32 Mins each, Passage-based):**
    * Module 01: Core Diagnostic (`sat/reading-practice-01.html`)
    * Module 02: Craft & Structure (`sat/reading-practice-02.html`)
    * Module 03: Information & Ideas (`sat/reading-practice-03.html`)
    * Module 04: Advanced English Conventions (`sat/reading-practice-04.html`)
    * Module 05: High-Percentile Mastery Suite (`sat/reading-practice-05.html`)
    * 🎲 **Random 20-Q Mock:** Dynamic shuffled exam sampled from 100-Q pool (`sat/reading-practice-random.html`)
  * **AP® Calculus AB (100 Questions — 5 Sets + Dynamic Random Mock, 45 Mins each, College Board CED Units 1–8):**
    * Set 01: Limits, Continuity & Core Diagnostic (`ap/calculus-ab-diagnostic-01.html`)
    * Set 02: Derivatives & Differentiability (`ap/calculus-ab-diagnostic-02.html`)
    * Set 03: Applications of Derivatives & MVT (`ap/calculus-ab-diagnostic-03.html`)
    * Set 04: Integration & Accumulation of Change (`ap/calculus-ab-diagnostic-04.html`)
    * Set 05: Differential Equations, Areas & Volumes (`ap/calculus-ab-diagnostic-05.html`)
    * 🎲 **Random 20-Q Mock:** Dynamic shuffled exam sampled from 100-Q pool (`ap/calculus-ab-diagnostic-random.html`)
  * **AP® Physics 1: Algebra-Based (100 Questions — 5 Sets + Dynamic Random Mock, 40 Mins each, College Board CED Units 1–7):**
    * Set 01: Kinematics & Core Physics Diagnostic (`ap/physics-1-diagnostic-01.html`)
    * Set 02: Dynamics, Friction & Newton's Laws (`ap/physics-1-diagnostic-02.html`)
    * Set 03: Circular Motion, Gravity & Work-Energy (`ap/physics-1-diagnostic-03.html`)
    * Set 04: Momentum, Impulse & Collisions (`ap/physics-1-diagnostic-04.html`)
    * Set 05: SHM & Rotational Dynamics (`ap/physics-1-diagnostic-05.html`)
    * 🎲 **Random 20-Q Mock:** Dynamic shuffled exam sampled from 100-Q pool (`ap/physics-1-diagnostic-random.html`)
* **Global Standards (IELTS® Academic — 20 Questions):**
  * Academic Reading Practice 01 (20 Qs, 25 Mins, Band 7.5–9.0 conversion scale)

---

## 4. Technical Architecture & Core Engine (`js/test-engine.js`)

MockTestVault runs on a pure vanilla JavaScript state machine with zero external npm dependencies:

* **TCS iON 5-State Palette:**
  * ⚪ State 1: Not Visited (Gray)
  * 🔴 State 2: Not Answered (Red)
  * 🟢 State 3: Answered (Green)
  * 🟣 State 4: Marked for Review (Purple)
  * 🟣🟢 State 5: Answered & Marked for Review (Purple with Green badge)
* **Web Audio Synthesizer:**
  * Sub-millisecond frequency generation (`triangle` and `sawtooth` oscillators) for correct/wrong feedback. Zero external sound files downloaded over the network.
* **1-Click Printable A4 Study Sheet:**
  * Uses `@media print` CSS rules to hide interactive timers, palettes, and sidebars, outputting a clean, double-column printable study worksheet with answer keys and citations.
* **Dark / Light Mode Synchronizer:**
  * Uses `data-theme` attribute on `<html>` with persistent `localStorage.getItem('mtv_theme')`.
* **Flexible Data Layer:**
  * Supports direct arrays `[...]` or dictionary wrappers `{"questions": [...]}`.
  * Dynamically maps `answer`, `correct`, or `correctAnswer` schema fields.
* **Dynamic Shuffled Random Mock Engine (`currentSet === 'random'`):**
  * Aggregates all sets from `setSources` in browser memory via parallel asynchronous `Promise.all` fetches.
  * Employs Fisher-Yates array shuffling to eliminate question bias and prevent duplicate questions within a test session.
  * Slices a clean sample of 20 randomized questions per attempt from the 100-question pool.
  * Hitting "Retake Test" dynamically re-shuffles a fresh set of 20 questions on the fly without page reloads.

---

## 5. SEO, Schema.org & Google Search Console Verification

* **Google Search Console Ownership:**
  * Verified via HTML file upload: `https://mocktestvault.com/google608ef5b6e1e06db8.html` (HTTP 200).
* **Canonical Topology:**
  * Every page defines a strict `<link rel="canonical" href="...">`.
  * `https://www.mocktestvault.com` 301-redirects to apex `https://mocktestvault.com`.
* **XML Sitemap:**
  * [mocktestvault.com/sitemap.xml](https://mocktestvault.com/sitemap.xml) contains exactly **90 production URLs** (85 Examination Suites + 5 Legal & Trust Hubs).
  * Priority weights: `1.0` (Homepage), `0.95` (Regional Hubs), `0.9` (Primary Simulators & Random Mocks), `0.85` (Progress Hub), `0.8` (Individual Chapter Tests & Legal Hubs).
* **Robots.txt Directives:**
  * Permissive `User-agent: * Allow: /` with explicit sitemap link.
* **Schema.org Structured Data:**
  * `EducationalOrganization` on Homepage and Regional Hubs.
  * Country targeting metadata: `areaServed: "United States"` on `/us/` and `areaServed: "India"` on `/in/`.
  * `AboutPage` and `ContactPage` JSON-LD schemas.
  * `Quiz` and `Question` JSON-LD schemas across test runners.

---

## 6. AdSense Compliance & Legal Trust Infrastructure

In direct alignment with Google AdSense Publisher Policies, Quality Rater Guidelines (QRG), and Help Content Systems, MockTestVault deploys an airtight trust and compliance suite:

* **About Us ([`about.html`](https://mocktestvault.com/about.html)):** Complete academic disclosures regarding our Zero-Distraction Exam Philosophy, statutory NCERT grounding methodologies, progressive 3-set pedagogical strategy, and E-E-A-T editorial verification standards.
* **Privacy Policy ([`privacy.html`](https://mocktestvault.com/privacy.html)):** Comprehensive GDPR, UK Data Protection Act, and CCPA/CPRA disclosures detailing 100% in-browser RAM execution, non-identifying `localStorage` usage, and explicit Google AdSense, DoubleClick DART, and AboutAds/NAI opt-out clauses.
* **Terms of Service ([`terms.html`](https://mocktestvault.com/terms.html)):** Permitted educational licensing, intellectual property safeguards, and clear trademark attributions (CBSE, SSC, College Board, Cambridge, ETS, TCS iON).
* **Academic Disclaimer ([`disclaimer.html`](https://mocktestvault.com/disclaimer.html)):** Educational simulation boundaries, explicit non-affiliation notices, score estimation limits, and statutory board key precedence.
* **Contact & Discrepancy Desk ([`contact.html`](https://mocktestvault.com/contact.html)):** Multi-channel support including dedicated editorial email (`contact@mocktestvault.com`), open GitHub issue tracking, and an interactive discrepancy submission form with a guaranteed 24–48 hour turnaround SLA.
* **Authorized Digital Sellers (`ads.txt`):** Pre-configured `ads.txt` deployed to root domain, ready for immediate AdSense Publisher ID injection upon approval.

---

## 7. Next Expansion Roadmap

1. **United States Pillar (100 Questions Per Exam Completed — 400 Qs Total):**
   * ✅ Digital SAT® Math: Sets 01 to 05 (100 Questions Live across 5 suites).
   * ✅ Digital SAT® Reading & Writing: Sets 01 to 05 (100 Questions Live across 5 suites).
   * ✅ AP® Calculus AB: Sets 01 to 05 (100 Questions Live across 5 suites).
   * ✅ AP® Physics 1: Sets 01 to 05 (100 Questions Live across 5 suites).
   * **Total: 400 Questions across 20 Dedicated Exam Routes.**
2. **Global Standards Pillar (+6 to 8 Pages):**
   * IELTS® Academic Reading Practice Tests 02, 03, 04.
   * GRE® Quantitative Reasoning Drills 01 & 02.
   * GRE® Verbal Reasoning Multi-Blank Drill 01.
   * TOEFL® iBT Academic Reading Diagnostic 01.
3. **India Pillar (+8 to 10 Pages):**
   * SSC CGL Tier 1 Full-Length 100-Q Mocks 02 & 03.
   * SSC CGL Sectional Drills Batch 02 (Reasoning 02, Quant 02, English 02, GA 02).
   * CBSE Class 10 Full 80-Mark Board Mock Papers (Science, Math, SST).

---

## 8. Deployment Protocol

To push updates across all live nodes simultaneously:

```bash
# 1. Push to GitHub Global CDN (triggers automated Pages deploy)
./deploy_to_github.sh "Commit message detailing new test suites"

# 2. Sync to Hostinger Cloud VPS
./deploy_mocktestvault.sh
```
