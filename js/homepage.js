/**
 * MockTestVault — Global Homepage Interactive Controller
 * Real-time search, category filtering, Web Audio synthesizer, and live teaser widget
 */

document.addEventListener('DOMContentLoaded', () => {
  // --------------------------------------------------------------------------
  // 1. Theme Management (Syncs across all sub-apps)
  // --------------------------------------------------------------------------
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const htmlRoot = document.documentElement;

  function initTheme() {
    const urlTheme = new URLSearchParams(window.location.search).get('theme');
    const savedTheme = urlTheme || localStorage.getItem('mtv_theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    htmlRoot.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
  }

  function updateThemeIcon(theme) {
    if (!themeToggleBtn) return;
    themeToggleBtn.textContent = theme === 'dark' ? '☀️' : '🌙';
    themeToggleBtn.setAttribute('title', theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode');
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const current = htmlRoot.getAttribute('data-theme') || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      htmlRoot.setAttribute('data-theme', next);
      localStorage.setItem('mtv_theme', next);
      updateThemeIcon(next);
      playTone('click');
    });
  }

  initTheme();

  // --------------------------------------------------------------------------
  // 2. Web Audio Synthesizer (Zero asset dependencies)
  // --------------------------------------------------------------------------
  function playTone(type) {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain);
      gain.connect(ctx.destination);

      if (type === 'click') {
        osc.frequency.setValueAtTime(480, ctx.currentTime);
        gain.gain.setValueAtTime(0.04, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.06);
        osc.start();
        osc.stop(ctx.currentTime + 0.06);
      } else if (type === 'correct') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
        osc.frequency.setValueAtTime(659.25, ctx.currentTime + 0.08); // E5
        gain.gain.setValueAtTime(0.06, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.25);
        osc.start();
        osc.stop(ctx.currentTime + 0.25);
      } else if (type === 'wrong') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(260, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(180, ctx.currentTime + 0.2);
        gain.gain.setValueAtTime(0.05, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.2);
        osc.start();
        osc.stop(ctx.currentTime + 0.2);
      }
    } catch (e) {
      // Audio context restricted or unsupported
    }
  }

  // --------------------------------------------------------------------------
  // 3. Interactive Teaser Mini-Widget ("Try 1 Question Now")
  // --------------------------------------------------------------------------
  const teaserQuestions = [
    {
      id: 'ssc_quant_1',
      badge: 'SSC CGL Tier 1 • Quant Drill',
      time: '45s target',
      title: 'A train 180 m long passes a pole in 9 seconds. How long (in seconds) will it take to cross a platform 360 m long at the same speed?',
      options: [
        '18 seconds',
        '27 seconds',
        '24 seconds',
        '30 seconds'
      ],
      correctIndex: 1, // 27 seconds
      explanation: 'Speed of train = Distance / Time = 180 m / 9 s = 20 m/s. Total distance to cross platform = Length of train + Length of platform = 180 + 360 = 540 m. Time required = 540 / 20 = 27 seconds.',
      citation: 'Official SSC CGL Tier 1 2024 Past Year Speed Drill Benchmark',
      fullLink: 'ssc-cgl/mock-01.html',
      fullText: 'Launch Full SSC CGL Mock 01 (100 Qs) →'
    },
    {
      id: 'cbse_sci_1',
      badge: 'CBSE Class 10 • Science Drill',
      time: '30s target',
      title: 'When lead nitrate Pb(NO₃)₂ crystals are strongly heated in a dry boiling tube, which of the following observations is correct?',
      options: [
        'White fumes of oxygen gas are evolved',
        'Brown fumes of nitrogen dioxide (NO₂) gas are released',
        'A greenish yellow gas with choking smell appears',
        'No gas is evolved; only a yellow residue remains'
      ],
      correctIndex: 1, // Brown fumes of NO2
      explanation: '2Pb(NO₃)₂(s) —Δ→ 2PbO(s) [yellow residue] + 4NO₂(g) [brown fumes] + O₂(g). The pungent brown gas evolved is nitrogen dioxide (NO₂).',
      citation: 'NCERT Class 10 Science, Chapter 1, Activity 1.5, Page 8',
      fullLink: 'cbse-class-10/science/ch01_chemical_reactions.html',
      fullText: 'Open CBSE Class 10 Science Chapter 1 Mock →'
    },
    {
      id: 'ssc_reasoning_1',
      badge: 'General Intelligence • Reasoning Drill',
      time: '25s target',
      title: 'In a certain code language, "FLOWER" is written as "UOLDVI". How will "GARDEN" be written in that same code language?',
      options: [
        'TZIVWM',
        'TZIVWN',
        'TYIUMM',
        'SZJUVM'
      ],
      correctIndex: 0, // TZIVWM (Opposite letters)
      explanation: 'The code uses opposite alphabet pairs (sum of positions = 27): F↔U, L↔O, O↔L, W↔D, E↔V, R↔I. Applying this to GARDEN: G↔T, A↔Z, R↔I, D↔W, E↔V, N↔M. Result: TZIVWM.',
      citation: 'SSC CGL Sectional Reasoning Pattern Analysis',
      fullLink: 'ssc-cgl/sectional-reasoning-01.html',
      fullText: 'Take 25-Q Sectional Reasoning Speed Drill →'
    },
    {
      id: 'sat_math_1',
      badge: '🇺🇸 Digital SAT® • Math Module',
      time: '40s target',
      title: 'If 3x - y = 12, what is the numerical value of (8ˣ) / (2ʸ)?',
      options: [
        '2¹²',
        '4⁴',
        '8²',
        'The value cannot be determined from the information given'
      ],
      correctIndex: 0, // 2^12 (4096)
      explanation: 'Rewrite 8 in base 2: 8ˣ = (2³)ˣ = 2³ˣ. Thus (8ˣ)/(2ʸ) = (2³ˣ)/(2ʸ) = 2^(3x - y). Since 3x - y = 12, the expression equals 2¹² = 4,096.',
      citation: 'CollegeBoard Digital SAT® Math High-Yield Exponent Properties',
      fullLink: 'us/sat/math-practice-01.html',
      fullText: 'Launch Digital SAT® Math Simulator →'
    },
    {
      id: 'ielts_reading_1',
      badge: '🌐 IELTS® Academic • Reading Drill',
      time: '60s target',
      title: 'Passage statement: "Global geothermal power plants currently generate over 16,000 MW, with Iceland generating 66% of its primary energy from geothermal sources." Question: According to the passage, is Iceland the world\'s single largest aggregate producer of geothermal electricity in gross megawatt capacity?',
      options: [
        'TRUE — The statement agrees with the information',
        'FALSE — The statement directly contradicts the information',
        'NOT GIVEN — There is no information on this in the passage',
        'PARTIALLY TRUE — It applies only during winter seasons'
      ],
      correctIndex: 2, // NOT GIVEN
      explanation: 'NOT GIVEN. The text mentions that Iceland generates 66% of its own primary energy from geothermal, but gives no comparative data regarding whether Iceland is the world\'s largest aggregate producer in gross megawatt volume (the US holds the largest total capacity at ~3,700 MW). Because the passage neither confirms nor denies this aggregate rank, the answer is NOT GIVEN.',
      citation: 'Cambridge IELTS Academic Reading Test Standards (Passage 1)',
      fullLink: 'global/ielts/reading-practice-01.html',
      fullText: 'Launch IELTS® Reading Drill (Band 7.5–9.0) →'
    }
  ];

  let currentTeaserIdx = 0;
  const teaserBadge = document.getElementById('teaser-badge');
  const teaserMeta = document.getElementById('teaser-meta');
  const teaserTitle = document.getElementById('teaser-title');
  const teaserOptionsList = document.getElementById('teaser-options-list');
  const teaserExplBox = document.getElementById('teaser-expl-box');
  const teaserExplText = document.getElementById('teaser-expl-text');
  const teaserCitation = document.getElementById('teaser-citation');
  const teaserNextBtn = document.getElementById('teaser-next-btn');
  const teaserFullLink = document.getElementById('teaser-full-link');

  function renderTeaser(idx) {
    if (!teaserTitle || !teaserOptionsList) return;
    const q = teaserQuestions[idx % teaserQuestions.length];

    teaserBadge.textContent = q.badge;
    teaserMeta.innerHTML = `<span>⏱️</span> ${q.time}`;
    teaserTitle.textContent = q.title;
    teaserExplBox.classList.remove('show');
    teaserExplText.textContent = q.explanation;
    teaserCitation.textContent = `Source: ${q.citation}`;
    if (teaserFullLink) {
      teaserFullLink.href = q.fullLink;
      teaserFullLink.textContent = q.fullText;
    }

    teaserOptionsList.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];

    q.options.forEach((optText, optIdx) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'teaser-option-btn';
      btn.innerHTML = `<span class="teaser-key-badge">${letters[optIdx]}</span> <span>${optText}</span>`;
      btn.addEventListener('click', () => handleTeaserAnswer(optIdx, q.correctIndex));
      teaserOptionsList.appendChild(btn);
    });
  }

  function handleTeaserAnswer(selectedIndex, correctIndex) {
    const optionBtns = teaserOptionsList.querySelectorAll('.teaser-option-btn');
    optionBtns.forEach(btn => btn.disabled = true);

    if (selectedIndex === correctIndex) {
      optionBtns[selectedIndex].classList.add('correct');
      playTone('correct');
    } else {
      optionBtns[selectedIndex].classList.add('wrong');
      optionBtns[correctIndex].classList.add('correct');
      playTone('wrong');
    }

    teaserExplBox.classList.add('show');
  }

  if (teaserNextBtn) {
    teaserNextBtn.addEventListener('click', () => {
      currentTeaserIdx++;
      renderTeaser(currentTeaserIdx);
      playTone('click');
    });
  }

  // Initialize first teaser
  renderTeaser(currentTeaserIdx);

  // --------------------------------------------------------------------------
  // 4. Live Search & Category Filter Engine
  // --------------------------------------------------------------------------
  const searchInput = document.getElementById('global-search-input');
  const searchClearBtn = document.getElementById('search-clear-btn');
  const examCards = document.querySelectorAll('.exam-card');
  const filterChips = document.querySelectorAll('.filter-chip');
  const catalogTabs = document.querySelectorAll('.catalog-tab-btn');
  const noResultsBox = document.getElementById('no-results-box');

  let currentCategory = 'all';
  let searchQuery = '';

  function applyFilters() {
    let visibleCount = 0;
    const q = searchQuery.toLowerCase().trim();

    examCards.forEach(card => {
      const category = card.getAttribute('data-category') || '';
      const textContent = card.innerText.toLowerCase();

      const matchesCategory = (currentCategory === 'all' || category === currentCategory || category.split(' ').includes(currentCategory));
      const matchesSearch = (!q || textContent.includes(q));

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (noResultsBox) {
      noResultsBox.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      if (searchClearBtn) {
        searchClearBtn.style.display = searchQuery ? 'block' : 'none';
      }
      applyFilters();
    });
  }

  if (searchClearBtn) {
    searchClearBtn.addEventListener('click', () => {
      searchInput.value = '';
      searchQuery = '';
      searchClearBtn.style.display = 'none';
      searchInput.focus();
      applyFilters();
      playTone('click');
    });
  }

  // Sync category selection between hero chips and catalog tabs
  function setCategory(cat) {
    currentCategory = cat;

    filterChips.forEach(chip => {
      chip.classList.toggle('active', chip.getAttribute('data-category') === cat);
    });

    catalogTabs.forEach(tab => {
      tab.classList.toggle('active', tab.getAttribute('data-category') === cat);
    });

    applyFilters();
  }

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const cat = chip.getAttribute('data-category');
      setCategory(cat);
      playTone('click');
    });
  });

  catalogTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const cat = tab.getAttribute('data-category');
      setCategory(cat);
      playTone('click');
    });
  });

  // Global Keyboard Shortcut: "/" or "Cmd+K" focuses any search input
  window.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
    if ((e.key === '/' || (e.key === 'k' && (e.metaKey || e.ctrlKey)))) {
      const activeSearch = document.getElementById('global-search-input') || 
                           document.getElementById('chapter-search') || 
                           document.querySelector('input[type="search"]') ||
                           document.querySelector('.search-filter-box input');
      if (activeSearch) {
        e.preventDefault();
        activeSearch.focus();
        activeSearch.select();
      }
    }
  });

  // --------------------------------------------------------------------------
  // 5. Interactive FAQ Accordion
  // --------------------------------------------------------------------------
  const accordionQuestions = document.querySelectorAll('.faq-accordion-question, .faq-question');
  accordionQuestions.forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-accordion-item, .faq-item');
      if (!item) return;
      const wasActive = item.classList.contains('active');

      // Close other items in the same container for clean accordion UX
      const container = item.closest('.faq-accordion, .faq-section');
      if (container) {
        container.querySelectorAll('.faq-accordion-item.active, .faq-item.active').forEach(openItem => {
          if (openItem !== item) {
            openItem.classList.remove('active');
            const q = openItem.querySelector('.faq-accordion-question, .faq-question');
            if (q) q.setAttribute('aria-expanded', 'false');
          }
        });
      }

      item.classList.toggle('active', !wasActive);
      btn.setAttribute('aria-expanded', String(!wasActive));
      playTone('click');
    });
  });

  // --------------------------------------------------------------------------
  // 6. Service Worker PWA Registration
  // --------------------------------------------------------------------------
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then((reg) => {
          reg.update().catch(() => {});
          console.log('MockTestVault PWA active:', reg.scope);
        })
        .catch((err) => console.debug('SW registration skipped:', err));
    });
  }

  // --------------------------------------------------------------------------
  // 7. Student Local Progress Tracker & Dynamic Attempt Badges
  // --------------------------------------------------------------------------
  function renderStudentProgress() {
    try {
      const raw = localStorage.getItem('mtv_attempt_history');
      if (!raw) return;
      const history = JSON.parse(raw);
      if (!Array.isArray(history) || history.length === 0) return;

      // Group attempts by test identifier
      const bestAttempts = {};
      history.forEach(h => {
        if (!h.path) return;
        const filename = h.path.split('/').pop().split('?')[0];
        const existing = bestAttempts[filename];
        if (!existing || (h.scorePct || 0) > (existing.scorePct || 0)) {
          bestAttempts[filename] = h;
        }
        bestAttempts[h.path] = bestAttempts[filename];
      });

      // Find all test links/cards
      const cards = document.querySelectorAll('.chapter-card, .exam-card, a.test-link, a.card-action-btn');
      let attemptedOnPage = 0;
      let totalTestsOnPage = 0;
      let scoreSum = 0;

      cards.forEach(card => {
        let href = card.getAttribute('href');
        if (!href) {
          const innerLink = card.querySelector('a[href*=".html"]');
          if (innerLink) href = innerLink.getAttribute('href');
        }
        if (!href || href === '#' || href.endsWith('index.html') || href.includes('formulas') || href.includes('strategy')) return;

        totalTestsOnPage++;
        const filename = href.split('/').pop().split('?')[0];
        const best = bestAttempts[filename] || bestAttempts[href];

        if (best) {
          attemptedOnPage++;
          scoreSum += (best.scorePct || 0);

          let metaBox = card.querySelector('.card-top-meta') || card.querySelector('.card-footer') || card.querySelector('.exam-badge-row') || card;
          if (metaBox && !card.querySelector('.card-progress-pill')) {
            const pill = document.createElement('span');
            const pct = Math.round(best.scorePct || 0);
            pill.className = `card-progress-pill ${pct >= 60 ? 'completed' : 'needs-revision'}`;
            pill.innerHTML = `✓ ${pct}% (${best.marksObtained !== undefined ? best.marksObtained : best.correct}/${best.maxMarks !== undefined ? best.maxMarks : best.total})`;
            pill.title = `Attempted on ${best.date || 'previously'} (${pct}% accuracy)`;
            metaBox.appendChild(pill);
          }
        }
      });

      // If page has test cards, render or update the Student Progress Banner
      if (totalTestsOnPage > 0 && attemptedOnPage > 0) {
        let banner = document.getElementById('student-progress-banner');
        if (!banner) {
          banner = document.createElement('div');
          banner.id = 'student-progress-banner';
          banner.className = 'student-progress-banner';
          const targetParent = document.querySelector('.curriculum-catalog') || document.querySelector('.catalog-section') || document.querySelector('main') || document.body;
          if (targetParent) {
            targetParent.insertBefore(banner, targetParent.firstChild);
          }
        }

        const completionPct = Math.round((attemptedOnPage / totalTestsOnPage) * 100);
        const avgAccuracy = Math.round(scoreSum / attemptedOnPage);

        banner.innerHTML = `
          <div class="student-progress-header">
            <span class="student-progress-title">
              <span>🎯</span> <span>Your Practice Progress</span>
            </span>
            <span class="student-progress-stats">${attemptedOnPage} of ${totalTestsOnPage} Tests Completed (${completionPct}%)</span>
          </div>
          <div class="student-progress-bar-track">
            <div class="student-progress-bar-fill" style="width: ${Math.max(completionPct, 4)}%;"></div>
          </div>
          <div class="student-progress-footer">
            <span>Overall Average Accuracy: <strong style="color:var(--text-color);">${avgAccuracy}%</strong></span>
            <span>All progress saved 100% locally in browser</span>
          </div>
        `;
      }
    } catch (e) {
      console.debug('Progress tracker init skipped:', e);
    }
  }

  renderStudentProgress();
});
