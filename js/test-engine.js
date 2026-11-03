/**
 * MockTestVault — Advanced Interactive CBT Test Engine
 * Incorporating Industry Best Practices from Testbook (TCS iON), Quizlet & Brilliant.org
 */

class MockTestEngine {
  constructor(options = {}) {
    const urlParams = (typeof window !== 'undefined' && window.location) ? new URLSearchParams(window.location.search) : null;
    const setParam = urlParams ? urlParams.get('set') : null;
    this.setSources = options.setSources || {
      set1: 'data/in/cbse10/science_ch01_chemical_reactions_set1.json',
      set2: 'data/in/cbse10/science_ch01_chemical_reactions_set2.json',
      set3: 'data/in/cbse10/science_ch01_chemical_reactions_set3.json'
    };
    if (setParam && (setParam === 'random' || this.setSources[setParam])) {
      this.currentSet = setParam;
    } else {
      this.currentSet = options.initialSet || 'set1';
    }
    this.dataSource = this.currentSet === 'random' ? null : this.setSources[this.currentSet];
    this.timeLimitMinutes = options.timeLimitMinutes || 20;
    this.randomSampleSize = options.randomSampleSize || 20;
    this.markingScheme = options.markingScheme || { correct: 1, wrong: 0 };
    this.examType = options.examType || 'board'; // 'board' or 'competitive'
    this.questions = [];
    
    // State
    this.currentIndex = 0;
    this.userAnswers = [];
    this.reviewedFlags = [];
    this.visitedFlags = [];
    this.mode = 'exam'; // 'exam' or 'practice'
    this.timeRemaining = this.timeLimitMinutes * 60;
    this.timerInterval = null;
    this.isSubmitted = false;
    this.startTime = null;
    this.currentReviewFilter = 'all';

    // User Preferences
    this.soundEnabled = localStorage.getItem('mtv_sound') !== 'false';
    this.fontSizeScale = parseFloat(localStorage.getItem('mtv_font_scale')) || 1.0;

    // Offline Question Bookmarking & Attempt History State
    this.bookmarkStorageKey = 'mtv_bookmarks';
    this.historyStorageKey = 'mtv_attempt_history';
    this.bookmarkedSet = this.loadStoredBookmarks();

    // DOM Elements with dual fallback selectors
    this.dom = {
      questionCard: document.getElementById('question-card'),
      qNumber: document.getElementById('q-number') || document.getElementById('q-number-badge'),
      qBadges: document.getElementById('q-badges') || document.getElementById('q-meta-group'),
      qSubtopicBadge: document.getElementById('q-subtopic-badge'),
      qDiffBadge: document.getElementById('q-diff-badge'),
      qTitle: document.getElementById('q-title') || document.getElementById('q-text'),
      optionsList: document.getElementById('options-list') || document.getElementById('options-group'),
      explanationBox: document.getElementById('explanation-box'),
      explanationText: document.getElementById('explanation-text') || document.getElementById('exp-text'),
      citationTag: document.getElementById('citation-tag') || document.getElementById('exp-citation'),
      
      prevBtn: document.getElementById('btn-prev'),
      nextBtn: document.getElementById('btn-next'),
      reviewBtn: document.getElementById('btn-review'),
      clearBtn: document.getElementById('btn-clear'),
      submitBtn: document.getElementById('btn-submit'),
      openSubmitBtn: document.getElementById('btn-open-submit'),
      
      paletteGrid: document.getElementById('palette-grid'),
      paletteAnsweredCount: document.getElementById('count-answered'),
      paletteNotAnsweredCount: document.getElementById('count-not-answered'),
      paletteReviewedCount: document.getElementById('count-reviewed'),
      paletteAnsReviewedCount: document.getElementById('count-ans-reviewed'),
      paletteUnvisitedCount: document.getElementById('count-unvisited'),
      paletteSummary: document.getElementById('palette-summary'),
      
      timerBox: document.getElementById('timer-box'),
      timerDisplay: document.getElementById('timer-display'),
      progressBarFill: document.getElementById('progress-bar-fill'),
      progressText: document.getElementById('progress-text'),
      
      modePracticeBtn: document.getElementById('mode-practice-btn'),
      modeExamBtn: document.getElementById('mode-exam-btn'),
      themeToggleBtn: document.getElementById('theme-toggle-btn'),
      fontDecBtn: document.getElementById('btn-font-dec'),
      fontIncBtn: document.getElementById('btn-font-inc'),
      soundToggleBtn: document.getElementById('btn-sound-toggle'),
      fullscreenToggleBtn: document.getElementById('btn-fullscreen-toggle'),
      
      testLayout: document.getElementById('test-layout'),
      scorecardView: document.getElementById('scorecard-view'),
      scoreHero: document.getElementById('score-hero'),
      statsGrid: document.getElementById('stats-grid'),
      masteryContainer: document.getElementById('mastery-container'),
      reviewList: document.getElementById('review-list'),
      
      filterAllBtn: document.getElementById('filter-all'),
      filterWrongBtn: document.getElementById('filter-wrong') || document.getElementById('filter-incorrect'),
      filterReviewedBtn: document.getElementById('filter-reviewed'),
      filterCorrectBtn: document.getElementById('filter-correct'),
      
      retakeBtn: document.getElementById('btn-retake'),
      printBtn: document.getElementById('btn-print') || document.getElementById('btn-print-sheet'),
      statusContainer: document.getElementById('exam-status-bar')
    };

    this.init();
  }

  async init() {
    this.setupTheme();
    this.setupFontSize();
    this.updateSoundIcon();
    this.bindEvents();
    this.syncActiveSetButton();
    this.setupServiceWorker();
    this.setupNetworkMonitor();
    await this.loadQuestions();
  }

  setupServiceWorker() {
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
          .then((reg) => {
            reg.addEventListener('updatefound', () => {
              const newWorker = reg.installing;
              if (newWorker) {
                newWorker.addEventListener('statechange', () => {
                  if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                    console.log('MockTestVault PWA updated in background.');
                  }
                });
              }
            });
          })
          .catch((err) => console.debug('SW registration skipped:', err));
      });
    }
  }

  setupNetworkMonitor() {
    const updateOnlineStatus = () => {
      const isOnline = navigator.onLine;
      let badge = document.getElementById('network-status-badge');
      if (!isOnline) {
        if (!badge) {
          badge = document.createElement('div');
          badge.id = 'network-status-badge';
          badge.className = 'network-status-badge offline';
          badge.innerHTML = '<span>⚡</span> <span>Offline Mode — Cached Exam Active</span>';
          badge.setAttribute('title', 'Exam questions and calculations run 100% locally in browser memory without internet.');
          const statusBar = document.querySelector('.status-container') || document.getElementById('exam-status-bar') || document.body;
          if (statusBar) statusBar.appendChild(badge);
        }
        badge.style.display = 'inline-flex';
      } else if (badge) {
        badge.className = 'network-status-badge online';
        badge.innerHTML = '<span>✓</span> <span>Online</span>';
        setTimeout(() => { if (badge) badge.style.display = 'none'; }, 2500);
      }
    };

    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
    if (!navigator.onLine) updateOnlineStatus();
  }

  syncActiveSetButton() {
    document.querySelectorAll('.set-btn').forEach(btn => {
      const isMatch = (btn.getAttribute('data-set') === this.currentSet);
      btn.classList.toggle('active', isMatch);
      btn.setAttribute('aria-selected', isMatch);
    });
  }

  /* ==========================================================================
     Theme & Display Settings
     ========================================================================== */
  setupTheme() {
    const savedTheme = localStorage.getItem('mtv_theme') || 
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', savedTheme);
    this.updateThemeIcon(savedTheme);
  }

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('mtv_theme', next);
    this.updateThemeIcon(next);
  }

  updateThemeIcon(theme) {
    if (this.dom.themeToggleBtn) {
      this.dom.themeToggleBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
      this.dom.themeToggleBtn.setAttribute('title', `Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`);
    }
  }

  setupFontSize() {
    document.documentElement.style.fontSize = `${this.fontSizeScale * 100}%`;
  }

  adjustFontSize(delta) {
    this.fontSizeScale = Math.min(1.25, Math.max(0.85, this.fontSizeScale + delta));
    localStorage.setItem('mtv_font_scale', this.fontSizeScale);
    this.setupFontSize();
  }

  toggleSound() {
    this.soundEnabled = !this.soundEnabled;
    localStorage.setItem('mtv_sound', this.soundEnabled);
    this.updateSoundIcon();
    if (this.soundEnabled) this.playTone('click');
  }

  updateSoundIcon() {
    if (this.dom.soundToggleBtn) {
      this.dom.soundToggleBtn.innerHTML = this.soundEnabled ? '🔊' : '🔇';
      this.dom.soundToggleBtn.setAttribute('title', this.soundEnabled ? 'Mute Sound Effects' : 'Enable Sound Effects');
    }
  }

  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) document.exitFullscreen();
    }
  }

  /* ==========================================================================
     Native Web Audio Synthesizer (Instant, Zero External Assets)
     ========================================================================== */
  playTone(type) {
    if (!this.soundEnabled) return;
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) return;
      const ctx = new AudioContext();
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
        osc.type = 'sine';
        osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
        osc.frequency.setValueAtTime(783.99, ctx.currentTime + 0.08); // G5
        gain.gain.setValueAtTime(0.06, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.22);
        osc.start();
        osc.stop(ctx.currentTime + 0.22);
      } else if (type === 'wrong') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(220, ctx.currentTime);
        osc.frequency.setValueAtTime(185, ctx.currentTime + 0.08);
        gain.gain.setValueAtTime(0.06, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.2);
        osc.start();
        osc.stop(ctx.currentTime + 0.2);
      } else if (type === 'fanfare') {
        // Test finished arpeggio
        [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
          const noteOsc = ctx.createOscillator();
          const noteGain = ctx.createGain();
          noteOsc.connect(noteGain);
          noteGain.connect(ctx.destination);
          noteOsc.frequency.setValueAtTime(freq, ctx.currentTime + (i * 0.09));
          noteGain.gain.setValueAtTime(0.05, ctx.currentTime + (i * 0.09));
          noteGain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + (i * 0.09) + 0.18);
          noteOsc.start(ctx.currentTime + (i * 0.09));
          noteOsc.stop(ctx.currentTime + (i * 0.09) + 0.18);
        });
      }
    } catch (e) {
      // AudioContext policy fallback
    }
  }

  /* ==========================================================================
     Chemical Formula Typographic Formatter (Subscript Converter)
     ========================================================================== */
  formatChemicalFormulas(text) {
    if (!text) return '';
    // Escape HTML first
    let s = this.escapeHtml(text);

    // List of common Class 10 chemical formulas to format with exact <sub> tags
    const formulaMap = [
      [/FeSO4·7H2O/g, 'FeSO<sub>4</sub>·7H<sub>2</sub>O'],
      [/FeSO4/g, 'FeSO<sub>4</sub>'],
      [/Fe2O3/g, 'Fe<sub>2</sub>O<sub>3</sub>'],
      [/Fe3O4/g, 'Fe<sub>3</sub>O<sub>4</sub>'],
      [/Ca\(OH\)2/g, 'Ca(OH)<sub>2</sub>'],
      [/CaCO3/g, 'CaCO<sub>3</sub>'],
      [/CuSO4/g, 'CuSO<sub>4</sub>'],
      [/CuCO3·Cu\(OH\)2/g, 'CuCO<sub>3</sub>·Cu(OH)<sub>2</sub>'],
      [/CuCl2/g, 'CuCl<sub>2</sub>'],
      [/H2SO4/g, 'H<sub>2</sub>SO<sub>4</sub>'],
      [/ZnSO4/g, 'ZnSO<sub>4</sub>'],
      [/ZnCl2/g, 'ZnCl<sub>2</sub>'],
      [/Na2SO4/g, 'Na<sub>2</sub>SO<sub>4</sub>'],
      [/BaSO4/g, 'BaSO<sub>4</sub>'],
      [/BaCl2/g, 'BaCl<sub>2</sub>'],
      [/Pb\(NO3\)2/g, 'Pb(NO<sub>3</sub>)<sub>2</sub>'],
      [/Pb\(CH3COO\)2/g, 'Pb(CH<sub>3</sub>COO)<sub>2</sub>'],
      [/PbI2/g, 'PbI<sub>2</sub>'],
      [/Al2O3/g, 'Al<sub>2</sub>O<sub>3</sub>'],
      [/MnO2/g, 'MnO<sub>2</sub>'],
      [/MnCl2/g, 'MnCl<sub>2</sub>'],
      [/C6H12O6/g, 'C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>'],
      [/SO2/g, 'SO<sub>2</sub>'],
      [/SO3/g, 'SO<sub>3</sub>'],
      [/NO2/g, 'NO<sub>2</sub>'],
      [/CO2/g, 'CO<sub>2</sub>'],
      [/H2O\(g\)/g, 'H<sub>2</sub>O(g)'],
      [/H2O/g, 'H<sub>2</sub>O'],
      [/H2S/g, 'H<sub>2</sub>S'],
      [/H2/g, 'H<sub>2</sub>'],
      [/O2/g, 'O<sub>2</sub>'],
      [/N2/g, 'N<sub>2</sub>'],
      [/Cl2/g, 'Cl<sub>2</sub>'],
      [/Br2/g, 'Br<sub>2</sub>'],
      [/Ag2S/g, 'Ag<sub>2</sub>S'],
      [/AgCl/g, 'AgCl'],
      [/AgBr/g, 'AgBr'],
      [/NH4Cl/g, 'NH<sub>4</sub>Cl'],
      [/\(NH4\)2SO4/g, '(NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>'],
      [/SO4²⁻/g, 'SO<sub>4</sub><sup>2-</sup>'],
      [/Ba²⁺/g, 'Ba<sup>2+</sup>'],
      [/Cu²⁺/g, 'Cu<sup>2+</sup>'],
      [/Fe²⁺/g, 'Fe<sup>2+</sup>'],
      [/Pb²⁺/g, 'Pb<sup>2+</sup>'],
      [/H⁺/g, 'H<sup>+</sup>'],
      [/OH⁻/g, 'OH<sup>-</sup>'],
      [/O²⁻/g, 'O<sup>2-</sup>']
    ];

    formulaMap.forEach(([regex, replacement]) => {
      s = s.replace(regex, replacement);
    });

    // Math & Scientific Typography Enhancements
    s = s.replace(/([0-9]+)\s*deg\b/g, '$1°');
    s = s.replace(/\btheta\b/g, 'θ');
    s = s.replace(/\bpi\b/g, 'π');
    s = s.replace(/\+\-/g, '±');
    s = s.replace(/!=/g, '≠');
    s = s.replace(/<=/g, '≤');
    s = s.replace(/>=/g, '≥');
    s = s.replace(/=>/g, '⇒');
    s = s.replace(/sqrt\(([^)]+)\)/g, '√($1)');
    s = s.replace(/sqrt\b/g, '√');
    
    // Exponent Superscripts
    s = s.replace(/\^2\b/g, '²');
    s = s.replace(/\^3\b/g, '³');
    s = s.replace(/\^n\b/g, 'ⁿ');
    s = s.replace(/\^1\b/g, '¹');
    s = s.replace(/\^0\b/g, '⁰');

    // Sequence Subscripts (e.g. a_30 -> a₃₀, x_1 -> x₁)
    const subMap = { '0':'₀', '1':'₁', '2':'₂', '3':'₃', '4':'₄', '5':'₅', '6':'₆', '7':'₇', '8':'₈', '9':'₉', 'n':'ₙ' };
    s = s.replace(/\b([a-zA-Z])_([0-9n]+)\b/g, (match, v, digits) => {
      const subs = digits.split('').map(c => subMap[c] || c).join('');
      return v + subs;
    });

    return s;
  }

  /* ==========================================================================
     Data Loading & Set Management
     ========================================================================== */
  async loadQuestions() {
    if (this.isLoading) return;
    this.isLoading = true;
    try {
      let rawList = [];

      if (this.currentSet === 'random') {
        // Aggregate all available sets into a combined question pool
        const sources = Object.values(this.setSources || {});
        const fetchPromises = sources.map(async src => {
          try {
            const res = await fetch(src);
            if (!res.ok) return [];
            const data = await res.json();
            return Array.isArray(data) ? data : (data.questions || []);
          } catch (e) {
            console.warn('Failed to load set for random pool:', src, e);
            return [];
          }
        });

        const results = await Promise.all(fetchPromises);
        let combinedPool = results.flat();

        if (combinedPool.length === 0) {
          throw new Error('No questions found in question bank for random selection.');
        }

        // Fisher-Yates Shuffle on the combined pool
        for (let i = combinedPool.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [combinedPool[i], combinedPool[j]] = [combinedPool[j], combinedPool[i]];
        }

        // Sample requested number of random questions (default 20)
        const sampleSize = this.randomSampleSize || 20;
        rawList = combinedPool.slice(0, Math.min(sampleSize, combinedPool.length));
      } else {
        if (!this.dataSource) {
          throw new Error(`Data source not configured for set '${this.currentSet}'.`);
        }
        const res = await fetch(this.dataSource);
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        const rawData = await res.json();
        rawList = Array.isArray(rawData) ? rawData : (rawData.questions || []);
      }

      this.questions = rawList.map(q => ({
        ...q,
        answer: q.answer !== undefined ? q.answer : (q.correct !== undefined ? q.correct : q.correctAnswer),
        citation: q.citation || q.ncertRef || 'Official Syllabus Standard'
      }));
      
      // Initialize state arrays
      this.userAnswers = new Array(this.questions.length).fill(null);
      this.reviewedFlags = new Array(this.questions.length).fill(false);
      this.visitedFlags = new Array(this.questions.length).fill(false);
      this.timeRemaining = this.timeLimitMinutes * 60;
      this.currentIndex = 0;
      this.isSubmitted = false;
      this.startTime = Date.now();

      // Mark first question as visited
      this.visitedFlags[0] = true;

      this.renderPalette();
      this.renderQuestion(0);
      this.updateProgress();

      if (this.mode === 'exam') {
        this.startTimer();
      }
    } catch (err) {
      console.error('Failed to load test questions:', err);
      if (this.dom.qTitle) {
        this.dom.qTitle.innerHTML = `<span style="color:red">Failed to load questions: ${err.message}. Please refresh.</span>`;
      }
    } finally {
      this.isLoading = false;
    }
  }

  async switchSet(setKey) {
    if (!setKey) return;
    if (setKey !== 'random' && (this.currentSet === setKey || !this.setSources || !this.setSources[setKey])) return;
    
    if (!this.isSubmitted && this.userAnswers && this.userAnswers.some(a => a !== null)) {
      if (!confirm("Switching test sets will reset your current progress on this test. Continue?")) {
        return;
      }
    }
    
    this.currentSet = setKey;
    if (setKey !== 'random') {
      this.dataSource = this.setSources[setKey];
    }
    
    // Update active button state
    document.querySelectorAll('.set-btn').forEach(btn => {
      const isMatch = (btn.getAttribute('data-set') === setKey);
      btn.classList.toggle('active', isMatch);
      btn.setAttribute('aria-selected', isMatch);
    });

    // Reset view if scorecard is shown
    if (this.dom.scorecardView) this.dom.scorecardView.classList.remove('active');
    if (this.dom.testLayout) this.dom.testLayout.style.display = 'grid';
    if (this.dom.statusContainer) this.dom.statusContainer.style.display = 'block';

    if (this.timerInterval) clearInterval(this.timerInterval);

    await this.loadQuestions();
  }

  /* ==========================================================================
     Event Listeners & Hotkeys
     ========================================================================== */
  bindEvents() {
    if (this.dom.prevBtn) this.dom.prevBtn.addEventListener('click', () => this.prevQuestion());
    if (this.dom.nextBtn) this.dom.nextBtn.addEventListener('click', () => this.nextQuestion());
    if (this.dom.reviewBtn) this.dom.reviewBtn.addEventListener('click', () => this.toggleReview());
    if (this.dom.clearBtn) this.dom.clearBtn.addEventListener('click', () => this.clearResponse());
    if (this.dom.submitBtn) this.dom.submitBtn.addEventListener('click', () => this.confirmSubmit());
    if (this.dom.openSubmitBtn) this.dom.openSubmitBtn.addEventListener('click', () => this.confirmSubmit());
    
    if (this.dom.modePracticeBtn) {
      this.dom.modePracticeBtn.addEventListener('click', () => this.setMode('practice'));
    }
    if (this.dom.modeExamBtn) {
      this.dom.modeExamBtn.addEventListener('click', () => this.setMode('exam'));
    }
    if (this.dom.themeToggleBtn) {
      this.dom.themeToggleBtn.addEventListener('click', () => this.toggleTheme());
    }
    if (this.dom.fontDecBtn) {
      this.dom.fontDecBtn.addEventListener('click', () => this.adjustFontSize(-0.05));
    }
    if (this.dom.fontIncBtn) {
      this.dom.fontIncBtn.addEventListener('click', () => this.adjustFontSize(0.05));
    }
    if (this.dom.soundToggleBtn) {
      this.dom.soundToggleBtn.addEventListener('click', () => this.toggleSound());
    }
    if (this.dom.fullscreenToggleBtn) {
      this.dom.fullscreenToggleBtn.addEventListener('click', () => this.toggleFullscreen());
    }
    if (this.dom.retakeBtn) {
      this.dom.retakeBtn.addEventListener('click', () => this.retakeTest());
    }
    if (this.dom.printBtn) {
      this.dom.printBtn.addEventListener('click', () => window.print());
    }

    // Set Switcher Buttons (Set 1, Set 2, Set 3)
    document.querySelectorAll('.set-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const targetSet = btn.getAttribute('data-set');
        if (!targetSet) return;
        if (btn.tagName === 'A' && btn.getAttribute('href') && btn.getAttribute('href') !== '#') {
          // Allow normal navigation when clicking an <a> tag linking to another runner page
          return;
        }
        e.preventDefault();
        this.switchSet(targetSet);
      });
    });

    // Scorecard Review Filter Buttons
    document.querySelectorAll('.filter-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-filter');
        this.applyReviewFilter(filter);
      });
    });

    // Quizlet-Style Power User Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      // Don't trigger if user is in an input or test is submitted
      if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
      if (this.isSubmitted) return;

      const key = e.key.toUpperCase();

      // Options Selection: A, B, C, D, E or 1, 2, 3, 4, 5
      if (['A', '1'].includes(key)) this.selectOption(0);
      else if (['B', '2'].includes(key)) this.selectOption(1);
      else if (['C', '3'].includes(key)) this.selectOption(2);
      else if (['D', '4'].includes(key)) this.selectOption(3);
      else if (['E', '5'].includes(key)) this.selectOption(4);
      // Navigation: ArrowRight or Enter for Next, ArrowLeft for Prev
      else if (e.key === 'ArrowRight' || e.key === 'Enter') {
        if (this.currentIndex < this.questions.length - 1) this.nextQuestion();
      } else if (e.key === 'ArrowLeft') {
        if (this.currentIndex > 0) this.prevQuestion();
      }
      // Mark for Review: M
      else if (key === 'M') {
        this.toggleReview();
      }
      // Clear Response: C
      else if (key === 'C') {
        this.clearResponse();
      }
    });
  }

  setMode(newMode) {
    if (this.mode === newMode) return;
    this.mode = newMode;
    this.playTone('click');
    
    if (this.dom.modePracticeBtn) this.dom.modePracticeBtn.classList.toggle('active', newMode === 'practice');
    if (this.dom.modeExamBtn) this.dom.modeExamBtn.classList.toggle('active', newMode === 'exam');
    
    if (newMode === 'practice') {
      this.stopTimer();
      if (this.dom.timerBox) this.dom.timerBox.style.display = 'none';
    } else {
      if (this.dom.timerBox) this.dom.timerBox.style.display = 'flex';
      if (!this.isSubmitted) this.startTimer();
    }
    
    this.renderQuestion(this.currentIndex);
  }

  startTimer() {
    this.stopTimer();
    this.updateTimerDisplay();
    this.timerInterval = setInterval(() => {
      this.timeRemaining--;
      this.updateTimerDisplay();
      if (this.timeRemaining <= 0) {
        this.stopTimer();
        alert("Time is up! Your test will now be automatically submitted.");
        this.submitTest();
      }
    }, 1000);
  }

  stopTimer() {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
  }

  updateTimerDisplay() {
    if (!this.dom.timerDisplay) return;
    const mins = Math.floor(this.timeRemaining / 60);
    const secs = this.timeRemaining % 60;
    this.dom.timerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    
    if (this.timeRemaining <= 180) { // under 3 mins
      this.dom.timerBox.classList.add('warning');
    } else {
      this.dom.timerBox.classList.remove('warning');
    }
  }

  /* ==========================================================================
     Question Rendering & Actions
     ========================================================================== */
  renderQuestion(index) {
    if (!this.questions || index < 0 || index >= this.questions.length) return;
    this.currentIndex = index;
    this.visitedFlags[index] = true;
    const q = this.questions[index];

    // 1. Question Number & Badges
    if (this.dom.qNumber) {
      this.dom.qNumber.textContent = `Question ${index + 1} of ${this.questions.length}`;
    }
    
    let chapterBadge = 'CBSE Class 10';
    if (this.examType === 'sat') chapterBadge = 'Digital SAT®';
    else if (this.examType === 'ap') chapterBadge = 'AP® College Board';
    else if (this.examType === 'competitive') chapterBadge = 'SSC CGL Tier 1';
    else if (this.examType === 'ielts') chapterBadge = 'IELTS® Academic';
    else if (this.examType === 'gre') chapterBadge = 'ETS GRE® General';
    else if (this.examType === 'toefl') chapterBadge = 'ETS TOEFL® iBT';
    else if (this.examType === 'gmat') chapterBadge = 'GMAT® Focus Edition';

    let badgesHtml = `<span class="badge badge-chapter">${chapterBadge}</span>`;
    if (this.currentSet === 'random') badgesHtml += `<span class="badge" style="background:linear-gradient(135deg, rgba(99,102,241,0.15), rgba(168,85,247,0.15)); color:#9333ea; font-weight:700; border:1px solid rgba(147,51,234,0.3);">🎲 Shuffled Mock</span>`;
    if (q.subtopic) badgesHtml += `<span class="badge badge-subtopic">${q.subtopic}</span>`;
    if (q.type === 'assertion_reasoning') badgesHtml += `<span class="badge badge-type-ar">Assertion & Reasoning</span>`;
    if (q.difficulty) badgesHtml += `<span class="badge badge-subtopic">${q.difficulty}</span>`;
    
    // Persistent Question Bookmark Toggle
    const qKey = this.getQuestionKey(q, index);
    const isBookmarked = this.bookmarkedSet.has(qKey);
    badgesHtml += `
      <button type="button" 
              class="badge-bookmark ${isBookmarked ? 'active' : ''}" 
              id="btn-q-bookmark" 
              title="${isBookmarked ? 'Remove Bookmark' : 'Bookmark this question for revision'}">
        <span>${isBookmarked ? '★' : '☆'}</span>
        <span>${isBookmarked ? 'Bookmarked' : 'Bookmark'}</span>
      </button>
    `;
    
    if (this.dom.qBadges) {
      this.dom.qBadges.innerHTML = badgesHtml;
      const bmBtn = document.getElementById('btn-q-bookmark');
      if (bmBtn) {
        bmBtn.addEventListener('click', (e) => {
          e.stopPropagation();
          this.toggleBookmark(q, index);
        });
      }
    }
    if (this.dom.qSubtopicBadge) {
      this.dom.qSubtopicBadge.textContent = q.subtopic || 'Core Unit';
    }
    if (this.dom.qDiffBadge) {
      this.dom.qDiffBadge.textContent = q.difficulty || 'Medium';
    }

    // 2. Question Text with Chemical / Math Formatting
    if (this.dom.qTitle) {
      if (q.type === 'assertion_reasoning' && q.question.includes('Assertion (A):')) {
        const parts = q.question.split('\nReason (R):');
        const assertionPart = parts[0].replace('Assertion (A):', '').trim();
        const reasonPart = parts[1] ? parts[1].trim() : '';
        
        this.dom.qTitle.innerHTML = `
          <div style="margin-bottom:8px; font-weight:600;">Direction: The question below consists of an Assertion (A) and a Reason (R). Choose the correct option.</div>
          <div class="ar-highlight-box">
            <p><strong>Assertion (A):</strong> ${this.formatChemicalFormulas(assertionPart)}</p>
            <p style="margin-top:8px;"><strong>Reason (R):</strong> ${this.formatChemicalFormulas(reasonPart)}</p>
          </div>
        `;
      } else {
        this.dom.qTitle.innerHTML = this.formatChemicalFormulas(q.question);
      }
    }

    // 3. Render Options with Shortcuts & Subtle Hover Lift
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    const chosenAnswer = this.userAnswers[index];
    const hasAnswered = chosenAnswer !== null;

    let optionsHtml = '';
    (q.options || []).forEach((optText, optIdx) => {
      let extraClass = '';
      if (chosenAnswer === optIdx) {
        extraClass = 'selected';
      }

      // In Practice mode, give immediate green/red feedback
      if (this.mode === 'practice' && hasAnswered) {
        if (optIdx === q.answer) {
          extraClass = 'correct';
        } else if (chosenAnswer === optIdx) {
          extraClass = 'wrong';
        }
      }

      optionsHtml += `
        <div class="option-item ${extraClass}" data-index="${optIdx}" role="radio" aria-checked="${chosenAnswer === optIdx}">
          <div class="option-key">${letters[optIdx]}</div>
          <div class="option-text">${this.formatChemicalFormulas(optText)}</div>
          <span class="option-shortcut" title="Press key ${letters[optIdx]} on keyboard">${letters[optIdx]}</span>
        </div>
      `;
    });
    if (this.dom.optionsList) {
      this.dom.optionsList.innerHTML = optionsHtml;

      // Attach click listeners to options
      this.dom.optionsList.querySelectorAll('.option-item').forEach(el => {
        el.addEventListener('click', () => {
          const selectedOpt = parseInt(el.getAttribute('data-index'), 10);
          this.selectOption(selectedOpt);
        });
      });
    }

    // 4. Explanation Box (Practice Mode or after test submission)
    if (this.mode === 'practice' && hasAnswered) {
      this.showExplanation(q);
    } else {
      this.hideExplanation();
    }

    // 5. Update Review Button
    if (this.dom.reviewBtn) {
      const isReviewed = this.reviewedFlags[index];
      this.dom.reviewBtn.classList.toggle('active', isReviewed);
      this.dom.reviewBtn.innerHTML = isReviewed ? '<span>🟣</span> Marked for Review' : '<span>🚩</span> Mark for Review';
    }

    // 6. Navigation Buttons
    if (this.dom.prevBtn) this.dom.prevBtn.disabled = (index === 0);
    if (this.dom.nextBtn) this.dom.nextBtn.disabled = (index === this.questions.length - 1);
    if (this.dom.submitBtn) {
      // Keep submit button visible or highlight on final question
      this.dom.submitBtn.style.display = (index === this.questions.length - 1) ? 'inline-flex' : 'inline-flex';
    }

    // 7. Update Palette
    this.renderPalette();
    this.updateProgress();
  }

  selectOption(optIndex) {
    if (this.isSubmitted) return;
    this.userAnswers[this.currentIndex] = optIndex;
    
    // Play subtle audio tone
    if (this.mode === 'practice') {
      const isCorrect = (optIndex === this.questions[this.currentIndex].answer);
      this.playTone(isCorrect ? 'correct' : 'wrong');
    } else {
      this.playTone('click');
    }
    
    this.renderQuestion(this.currentIndex);
  }

  clearResponse() {
    if (this.isSubmitted) return;
    if (this.userAnswers[this.currentIndex] !== null) {
      this.userAnswers[this.currentIndex] = null;
      this.playTone('click');
      this.renderQuestion(this.currentIndex);
    }
  }

  toggleReview() {
    this.reviewedFlags[this.currentIndex] = !this.reviewedFlags[this.currentIndex];
    this.playTone('click');
    this.renderQuestion(this.currentIndex);
  }

  showExplanation(q) {
    if (!this.dom.explanationBox) return;
    if (this.dom.explanationText) {
      this.dom.explanationText.innerHTML = this.formatChemicalFormulas(q.explanation);
    }
    if (this.dom.citationTag) {
      const defaultCitation = (this.examType === 'sat') ? 'College Board SAT' : (this.examType === 'ap' ? 'College Board AP® CED' : (this.examType === 'toefl' ? 'ETS TOEFL® iBT Framework' : (this.examType === 'gmat' ? 'GMAC GMAT Focus Blueprint' : 'Official NCERT Class 10 Syllabus')));
      this.dom.citationTag.textContent = q.citation || defaultCitation;
    }
    this.dom.explanationBox.classList.add('active');
    this.dom.explanationBox.style.display = 'block';
  }

  hideExplanation() {
    if (this.dom.explanationBox) {
      this.dom.explanationBox.classList.remove('active');
      this.dom.explanationBox.style.display = 'none';
    }
  }

  prevQuestion() {
    if (this.currentIndex > 0) {
      this.playTone('click');
      this.renderQuestion(this.currentIndex - 1);
    }
  }

  nextQuestion() {
    if (this.currentIndex < this.questions.length - 1) {
      this.playTone('click');
      this.renderQuestion(this.currentIndex + 1);
    }
  }

  jumpToQuestion(index) {
    if (index >= 0 && index < this.questions.length) {
      this.playTone('click');
      this.renderQuestion(index);
    }
  }

  /* ==========================================================================
     TCS iON 5-State Question Palette Logic
     ========================================================================== */
  renderPalette() {
    if (!this.dom.paletteGrid) return;
    let gridHtml = '';
    
    let countAnswered = 0;
    let countNotAnswered = 0;
    let countReviewed = 0;
    let countAnsReviewed = 0;
    let countUnvisited = 0;

    this.questions.forEach((_, idx) => {
      const isAnswered = this.userAnswers[idx] !== null;
      const isReviewed = this.reviewedFlags[idx];
      const isVisited = this.visitedFlags[idx];
      const isCurrent = (this.currentIndex === idx);

      let statusClass = 'unvisited';

      if (isAnswered && isReviewed) {
        statusClass = 'answered-reviewed';
        countAnsReviewed++;
      } else if (isAnswered) {
        statusClass = 'answered';
        countAnswered++;
      } else if (isReviewed) {
        statusClass = 'reviewed';
        countReviewed++;
      } else if (isVisited) {
        statusClass = 'not-answered';
        countNotAnswered++;
      } else {
        statusClass = 'unvisited';
        countUnvisited++;
      }

      let btnClass = `palette-btn ${statusClass}`;
      if (isCurrent) btnClass += ' current';

      gridHtml += `<button class="${btnClass}" data-jump="${idx}" title="Question ${idx + 1}">${idx + 1}</button>`;
    });

    this.dom.paletteGrid.innerHTML = gridHtml;
    
    // Attach jump listeners
    this.dom.paletteGrid.querySelectorAll('.palette-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const jumpIdx = parseInt(btn.getAttribute('data-jump'), 10);
        this.jumpToQuestion(jumpIdx);
      });
    });

    // Update Counts in Legend
    if (this.dom.paletteAnsweredCount) this.dom.paletteAnsweredCount.textContent = countAnswered;
    if (this.dom.paletteNotAnsweredCount) this.dom.paletteNotAnsweredCount.textContent = countNotAnswered;
    if (this.dom.paletteReviewedCount) this.dom.paletteReviewedCount.textContent = countReviewed;
    if (this.dom.paletteAnsReviewedCount) this.dom.paletteAnsReviewedCount.textContent = countAnsReviewed;
    if (this.dom.paletteUnvisitedCount) this.dom.paletteUnvisitedCount.textContent = countUnvisited;
    if (this.dom.paletteSummary) this.dom.paletteSummary.textContent = `${countAnswered} / ${this.questions.length} Answered`;
  }

  updateProgress() {
    const answeredCount = this.userAnswers.filter(a => a !== null).length;
    const total = this.questions.length;
    const pct = Math.round((answeredCount / total) * 100);

    if (this.dom.progressBarFill) {
      this.dom.progressBarFill.style.width = `${Math.max(pct, 5)}%`;
    }
    if (this.dom.progressText) {
      this.dom.progressText.textContent = `${answeredCount} of ${total} answered (${pct}%)`;
    }
  }

  confirmSubmit() {
    const unanswered = this.userAnswers.filter(a => a === null).length;
    let msg = "Are you sure you want to finish and submit your test?";
    if (unanswered > 0) {
      msg = `You still have ${unanswered} unanswered question(s). Do you want to submit anyway?`;
    }
    if (confirm(msg)) {
      this.submitTest();
    }
  }

  /* ==========================================================================
     Scorecard, Subtopic Mastery & Review Filtering
     ========================================================================== */
  submitTest() {
    this.stopTimer();
    this.isSubmitted = true;
    this.playTone('fanfare');

    // Calculate score
    let correct = 0;
    let wrong = 0;
    let skipped = 0;
    const subtopicScores = {};

    this.questions.forEach((q, idx) => {
      const userChoice = this.userAnswers[idx];
      const sub = q.subtopic || 'General Reactions';
      if (!subtopicScores[sub]) subtopicScores[sub] = { correct: 0, total: 0 };
      subtopicScores[sub].total++;

      if (userChoice === null) {
        skipped++;
      } else if (userChoice === q.answer) {
        correct++;
        subtopicScores[sub].correct++;
      } else {
        wrong++;
      }
    });

    const total = this.questions.length;
    const correctWeight = this.markingScheme.correct;
    const wrongPenalty = this.markingScheme.wrong; // e.g. -0.5
    const marksObtained = Math.max(0, parseFloat(((correct * correctWeight) + (wrong * wrongPenalty)).toFixed(2)));
    const maxMarks = total * correctWeight;
    const scorePct = maxMarks > 0 ? Math.round((marksObtained / maxMarks) * 100) : 0;
    const timeSpentSecs = Math.max(0, (this.timeLimitMinutes * 60) - this.timeRemaining);
    const timeSpentMins = Math.floor(timeSpentSecs / 60);
    const timeSpentRemSecs = timeSpentSecs % 60;

    let rankBadge = "🏆 Distinction!";
    let rankDesc = "Outstanding conceptual clarity! You performed exceptionally well.";
    let predictedGrade = `Predicted Grade: Top Percentile`;

    if (this.examType === 'sat') {
      // Digital SAT scoring: 200 - 800 scaled per section
      const scaledScore = Math.round((correct / Math.max(1, total)) * 600) + 200;
      if (scorePct >= 85) {
        rankBadge = "🏆 99th Percentile Benchmark!";
        rankDesc = "Ivy League / Top 20 competitive score trajectory. Flawless execution across College Board domains.";
        predictedGrade = `Estimated Section Score: ${scaledScore} / 800 (Percentile: 98th-99th)`;
      } else if (scorePct >= 65) {
        rankBadge = "🎯 Competitive College Benchmark";
        rankDesc = "Strong performance. Review the few missed concepts to break into the 750+ score range.";
        predictedGrade = `Estimated Section Score: ${scaledScore} / 800 (Percentile: 85th-92nd)`;
      } else {
        rankBadge = "📈 Diagnostic Baseline";
        rankDesc = "Target core conceptual foundations and timing strategies to improve scaled score.";
        predictedGrade = `Estimated Section Score: ${scaledScore} / 800 (Baseline Tier)`;
      }
    } else if (this.examType === 'ap') {
      // AP Scoring 1 - 5
      let apScore = 1;
      if (scorePct >= 75) apScore = 5;
      else if (scorePct >= 60) apScore = 4;
      else if (scorePct >= 45) apScore = 3;
      else if (scorePct >= 30) apScore = 2;
      else apScore = 1;

      if (apScore === 5) {
        rankBadge = "🏆 AP® Score 5 (Extremely Well Qualified)";
        rankDesc = "Eligible for college credit and advanced placement at the nation's most selective universities.";
        predictedGrade = "Projected College Board AP Score: 5 (Top Tier)";
      } else if (apScore >= 3) {
        rankBadge = `🎯 AP® Score ${apScore} (Qualified for College Credit)`;
        rankDesc = "Meets credit-granting threshold at thousands of US colleges and universities.";
        predictedGrade = `Projected College Board AP Score: ${apScore} (Passing Tier)`;
      } else {
        rankBadge = `⚠️ AP® Score ${apScore} (Needs Review)`;
        rankDesc = "Focus on unit formulas and diagnostic review to reach qualifying score range (3+).";
        predictedGrade = `Projected College Board AP Score: ${apScore} (Revision Needed)`;
      }
    } else if (this.examType === 'competitive') {
      const accuracy = Math.round((correct / Math.max(1, correct + wrong)) * 100);
      if (scorePct >= 70) {
        rankBadge = "🎯 Tier 1 Cutoff Qualified!";
        rankDesc = "Excellent speed and precision. You are well above the expected Tier 1 cutoff marks.";
        predictedGrade = `Raw Score: ${marksObtained} / ${maxMarks} Marks • Accuracy: ${accuracy}%`;
      } else if (scorePct >= 50) {
        rankBadge = "👍 Competitive Attempt — Borderline Cutoff";
        rankDesc = "Good core knowledge. Work on reducing negative marking in reasoning and general awareness to clear the cutoff safely.";
        predictedGrade = `Raw Score: ${marksObtained} / ${maxMarks} Marks • Accuracy: ${accuracy}%`;
      } else {
        rankBadge = "⚠️ Needs Practice & Negative Control";
        rankDesc = "High negative penalties reduced your net score. Focus on high-accuracy attempts and sectional shortcuts.";
        predictedGrade = `Raw Score: ${marksObtained} / ${maxMarks} Marks • Below Cutoff`;
      }
    } else if (this.examType === 'ielts') {
      let band = "5.5";
      let userLevel = "Competent User";
      if (scorePct >= 90) { band = "8.5–9.0"; userLevel = "Expert User (C2 Level)"; }
      else if (scorePct >= 75) { band = "7.5–8.0"; userLevel = "Very Good User (C1/C2 Level)"; }
      else if (scorePct >= 60) { band = "6.5–7.0"; userLevel = "Good User (Global University Admission Standard)"; }
      else if (scorePct >= 45) { band = "5.5–6.0"; userLevel = "Competent User (B2 Level)"; }
      else { band = "< 5.0"; userLevel = "Modest User — Foundation Required"; }

      rankBadge = `🎯 IELTS Reading Band ${band}`;
      rankDesc = `${userLevel}. Calibrated to official Cambridge / British Council assessment rubrics.`;
      predictedGrade = `Estimated Reading Band: Band ${band} • Raw: ${correct} / ${total} Correct`;
    } else if (this.examType === 'gre') {
      const greScaled = Math.round(130 + (correct / Math.max(1, total)) * 40);
      let pctRange = "50th Percentile";
      if (greScaled >= 165) pctRange = "96th–99th Percentile (Top Tier Masters/PhD)";
      else if (greScaled >= 158) pctRange = "80th–92nd Percentile (Competitive Graduate Range)";
      else if (greScaled >= 150) pctRange = "50th–70th Percentile (Baseline Admit Range)";
      else pctRange = "Diagnostic Baseline";

      rankBadge = `🏛️ GRE Scaled Score: ${greScaled} / 170`;
      rankDesc = `Calibrated to official ETS GRE General Test scoring metrics (${pctRange}).`;
      predictedGrade = `Estimated Scaled Score: ${greScaled} / 170 • Raw: ${correct} / ${total} Correct`;
    } else if (this.examType === 'toefl') {
      const toeflScaled = Math.round((correct / Math.max(1, total)) * 30);
      let toeflLevel = "Advanced (24–30)";
      if (toeflScaled >= 24) toeflLevel = "Advanced / CEFR C1–C2 (Top Tier / Direct Academic Admit)";
      else if (toeflScaled >= 18) toeflLevel = "High-Intermediate / CEFR B2 (Standard University Admit)";
      else if (toeflScaled >= 10) toeflLevel = "Low-Intermediate / CEFR B1";
      else toeflLevel = "Below Low-Intermediate";

      rankBadge = `🎧 TOEFL® iBT Scaled Score: ${toeflScaled} / 30`;
      rankDesc = `${toeflLevel}. Calibrated to official ETS TOEFL iBT reading assessment rubrics.`;
      predictedGrade = `Estimated Section Score: ${toeflScaled} / 30 • Raw: ${correct} / ${total} Correct`;
    } else if (this.examType === 'gmat') {
      const gmatSecScaled = Math.round(60 + (correct / Math.max(1, total)) * 30);
      const gmatTotalEst = Math.round(205 + (correct / Math.max(1, total)) * 600);
      let gmatPct = "Top Tier MBA Trajectory";
      if (gmatSecScaled >= 85) gmatPct = "99th Percentile (M7 / Top 10 MBA Competitive)";
      else if (gmatSecScaled >= 80) gmatPct = "85th–95th Percentile (Top 25 MBA Competitive)";
      else if (gmatSecScaled >= 75) gmatPct = "60th–80th Percentile (Good Business School Admit Range)";
      else gmatPct = "Diagnostic Baseline";

      rankBadge = `📊 GMAT® Focus Scaled: ${gmatSecScaled} / 90`;
      rankDesc = `${gmatPct}. Calibrated to official GMAC GMAT Focus Edition scoring benchmarks.`;
      predictedGrade = `Estimated Section Score: ${gmatSecScaled} / 90 • Est Total GMAT: ${gmatTotalEst} / 805`;
    } else {
      // Board default
      if (scorePct < 40) {
        rankBadge = "⚠️ Needs Revision";
        rankDesc = "Review NCERT concepts, definitions, and key textbook examples.";
        predictedGrade = "Predicted CBSE Grade: C1 — Revise Key Activities";
      } else if (scorePct < 75) {
        rankBadge = "👍 Good Foundation!";
        rankDesc = "Solid grasp of core concepts. Practice NCERT Exemplar and Assertion-Reasoning to reach 95%+ marks.";
        predictedGrade = "Predicted CBSE Grade: B1 / A2 Target";
      } else {
        rankBadge = "🏆 Board Distinction!";
        rankDesc = "Outstanding conceptual clarity! Thoroughly prepared for the CBSE Board examination.";
        predictedGrade = "Predicted CBSE Grade: A1 (95%+ Target)";
      }
    }

    // Render Score Hero if element exists
    const scoreCircleHtml = this.examType === 'competitive'
      ? `<span class="score-num">${marksObtained}</span><span class="score-total">/ ${maxMarks} Marks</span>`
      : `<span class="score-num">${correct}</span><span class="score-total">out of ${total}</span>`;

    if (this.dom.scoreHero) {
      this.dom.scoreHero.innerHTML = `
        <div class="score-circle">
          ${scoreCircleHtml}
        </div>
        <h2 class="score-title">${rankBadge} (${scorePct}%)</h2>
        <p style="font-weight:700; color:var(--primary); font-size:0.95rem; margin-bottom:8px;">${predictedGrade}</p>
        <p class="score-desc">${rankDesc}</p>
      `;
    }

    // Render Stats Grid if element exists
    const penaltyCard = wrongPenalty !== 0 ? `
      <div class="stat-card">
        <div class="stat-val" style="color:var(--danger)">${(wrong * Math.abs(wrongPenalty)).toFixed(1)}</div>
        <div class="stat-label">Penalty (-${Math.abs(wrongPenalty)})</div>
      </div>
    ` : `
      <div class="stat-card">
        <div class="stat-val" style="color:var(--danger)">${wrong}</div>
        <div class="stat-label">Incorrect</div>
      </div>
    `;

    if (this.dom.statsGrid) {
      this.dom.statsGrid.innerHTML = `
        <div class="stat-card">
          <div class="stat-val" style="color:var(--success)">${correct}</div>
          <div class="stat-label">Correct (+${correctWeight})</div>
        </div>
        ${penaltyCard}
        <div class="stat-card">
          <div class="stat-val" style="color:var(--text-muted)">${skipped}</div>
          <div class="stat-label">Skipped (0)</div>
        </div>
        <div class="stat-card">
          <div class="stat-val" style="color:var(--primary)">${timeSpentMins}m ${timeSpentRemSecs}s</div>
          <div class="stat-label">Time Taken</div>
        </div>
      `;
    }

    // Support dedicated score tiles if present (US Runners layout)
    const rawEl = document.getElementById('score-raw');
    if (rawEl) rawEl.textContent = `${correct} / ${total}`;
    const pctEl = document.getElementById('score-pct');
    if (pctEl) pctEl.textContent = `${scorePct}%`;
    const scaleEl = document.getElementById('score-sat-scale');
    if (scaleEl) {
      if (this.examType === 'sat') {
        const scaledScore = Math.round((correct / Math.max(1, total)) * 600) + 200;
        scaleEl.textContent = `${scaledScore} / 800`;
      } else if (this.examType === 'ap') {
        let apScore = 1;
        if (scorePct >= 75) apScore = 5;
        else if (scorePct >= 60) apScore = 4;
        else if (scorePct >= 45) apScore = 3;
        else if (scorePct >= 30) apScore = 2;
        scaleEl.textContent = `Score ${apScore} / 5`;
      }
    }
    const timeEl = document.getElementById('score-time');
    if (timeEl) timeEl.textContent = `${timeSpentMins}m ${timeSpentRemSecs}s`;

    // Render Subtopic Mastery Bars
    let masteryHtml = `
      <div class="mastery-card">
        <div class="mastery-card-header">
          <span>📊 Subtopic Mastery Breakdown</span>
          <span style="font-size:0.8rem; color:var(--text-muted); font-weight:normal;">Target: 80%+ per section</span>
        </div>
        <div class="mastery-grid">
    `;

    Object.keys(subtopicScores).forEach(sub => {
      const stats = subtopicScores[sub];
      const subPct = Math.round((stats.correct / stats.total) * 100);
      let fillColor = '#10b981';
      let tag = 'Mastered 🌟';
      if (subPct < 50) {
        fillColor = '#ef4444';
        tag = 'Revise ⚠️';
      } else if (subPct < 80) {
        fillColor = '#3b82f6';
        tag = 'Good 👍';
      }

      masteryHtml += `
        <div class="mastery-row">
          <div class="mastery-meta">
            <span>${this.escapeHtml(sub)} (${stats.correct}/${stats.total})</span>
            <span style="color:${fillColor}">${subPct}% — ${tag}</span>
          </div>
          <div class="mastery-track">
            <div class="mastery-fill" style="width:${subPct}%; background:${fillColor};"></div>
          </div>
        </div>
      `;
    });
    masteryHtml += `</div></div>`;
    if (this.dom.masteryContainer) {
      this.dom.masteryContainer.innerHTML = masteryHtml;
    }

    // Update Filter Pill Counts
    const reviewedCount = this.reviewedFlags.filter(f => f).length;
    const mistakesCount = wrong + skipped;

    const fAll = document.getElementById('filter-count-all');
    if (fAll) fAll.textContent = total;
    const fWrong = document.getElementById('filter-count-wrong') || document.getElementById('filter-count-incorrect');
    if (fWrong) fWrong.textContent = mistakesCount;
    const fRev = document.getElementById('filter-count-reviewed');
    if (fRev) fRev.textContent = reviewedCount;
    const fCorr = document.getElementById('filter-count-correct');
    if (fCorr) fCorr.textContent = correct;
    const fUnans = document.getElementById('filter-count-unanswered');
    if (fUnans) fUnans.textContent = skipped;

    // Render Detailed Question by Question Review List
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    let reviewHtml = '';

    const expTitle = this.examType === 'sat'
      ? 'College Board Answer Rationale & Method'
      : (this.examType === 'ap'
        ? 'AP® CED Formula & Concept Analysis'
        : (this.examType === 'competitive'
          ? 'Official Solution & Shortcut'
          : (this.examType === 'ielts'
            ? 'Band 9 Reading Justification & Lexical Analysis'
            : (this.examType === 'gre'
              ? 'Official GRE Detailed Solution & Etymological Rationale'
              : (this.examType === 'toefl'
                ? 'ETS TOEFL® Official Rationale & Passage Evidence'
                : (this.examType === 'gmat'
                  ? 'GMAC Solution Breakdown & Strategic Analysis'
                  : 'NCERT Conceptual Explanation'))))));

    const defaultCitation = this.examType === 'sat'
      ? 'College Board SAT'
      : (this.examType === 'ap'
        ? 'College Board AP® CED'
        : (this.examType === 'competitive'
          ? 'Official Pattern'
          : (this.examType === 'ielts'
            ? 'Cambridge IELTS Academic Framework'
            : (this.examType === 'gre'
              ? 'ETS GRE General Standard'
              : (this.examType === 'toefl'
                ? 'ETS TOEFL® iBT Official Blueprint'
                : (this.examType === 'gmat'
                  ? 'Official GMAC GMAT Focus Framework'
                  : 'NCERT Class 10'))))));

    this.questions.forEach((q, idx) => {
      const userChoice = this.userAnswers[idx];
      const isCorrect = (userChoice === q.answer);
      const isSkipped = (userChoice === null);
      const isReviewed = this.reviewedFlags[idx];
      
      let itemStatusClass = isCorrect ? 'review-correct' : (isSkipped ? 'review-skipped' : 'review-wrong');
      let statusBadge = isCorrect 
        ? `<span style="color:var(--success); font-weight:700;">✓ Correct (+1)</span>`
        : (isSkipped ? `<span style="color:var(--text-muted); font-weight:700;">— Skipped / Unanswered</span>` : `<span style="color:var(--danger); font-weight:700;">✗ Incorrect (0)</span>`);

      const resultTag = isCorrect ? 'correct' : (isSkipped ? 'unanswered' : 'wrong');

      const qKey = this.getQuestionKey(q, idx);
      const isBookmarked = this.bookmarkedSet.has(qKey);

      reviewHtml += `
        <div class="review-item ${itemStatusClass}" 
             data-result="${resultTag}" 
             data-reviewed="${isReviewed ? 'true' : 'false'}"
             data-bookmarked="${isBookmarked ? 'true' : 'false'}"
             id="review-q-${idx}">
          <div class="review-q-header">
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
              <span>Q${idx + 1}. ${q.subtopic || 'General'} ${isReviewed ? '🟣' : ''}</span>
              <button type="button" 
                      class="btn-review-bookmark ${isBookmarked ? 'active' : ''}" 
                      data-qidx="${idx}" 
                      title="${isBookmarked ? 'Remove Bookmark' : 'Bookmark this question for revision'}">
                <span>${isBookmarked ? '★ Bookmarked' : '☆ Bookmark'}</span>
              </button>
              <button type="button" 
                      class="btn-report-question" 
                      data-qidx="${idx}" 
                      title="Report discrepancy or suggest correction for this question">
                🚩 Report
              </button>
            </div>
            ${statusBadge}
          </div>
          <p style="font-weight:600; margin-bottom:12px; line-height:1.5;">${this.formatChemicalFormulas(q.question)}</p>
          
          <div style="font-size:0.9rem; margin-bottom:12px;">
            ${userChoice !== null ? `
              <div style="margin-bottom:6px;">
                <strong>Your Answer:</strong> (${letters[userChoice]}) ${this.formatChemicalFormulas(q.options[userChoice])}
              </div>
            ` : `<div style="margin-bottom:6px; color:var(--text-muted);"><strong>Your Answer:</strong> Not attempted</div>`}
            
            <div style="color:var(--success-text); font-weight:600;">
              <strong>Correct Answer:</strong> (${letters[q.answer]}) ${this.formatChemicalFormulas(q.options[q.answer])}
            </div>
          </div>
          
          <div class="explanation-box active" style="margin-bottom:0;">
            <div class="explanation-header">
              <span>${expTitle}</span>
              <span class="citation-tag">${q.citation || defaultCitation}</span>
            </div>
            <div class="explanation-text">${this.formatChemicalFormulas(q.explanation)}</div>
          </div>
        </div>
      `;
    });

    if (this.dom.reviewList) {
      this.dom.reviewList.innerHTML = reviewHtml;
      
      // Bind Review Bookmark Buttons
      this.dom.reviewList.querySelectorAll('.btn-review-bookmark').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const qidx = parseInt(btn.getAttribute('data-qidx'), 10);
          const q = this.questions[qidx];
          const qKey = this.getQuestionKey(q, qidx);
          const wasBm = this.bookmarkedSet.has(qKey);
          if (wasBm) {
            this.bookmarkedSet.delete(qKey);
            btn.classList.remove('active');
            btn.innerHTML = '<span>☆ Bookmark</span>';
            const revCard = document.getElementById(`review-q-${qidx}`);
            if (revCard) revCard.setAttribute('data-bookmarked', 'false');
            this.saveBookmarks();
            this.showToast('Question removed from bookmarks.');
          } else {
            this.bookmarkedSet.add(qKey);
            btn.classList.add('active');
            btn.innerHTML = '<span>★ Bookmarked</span>';
            const revCard = document.getElementById(`review-q-${qidx}`);
            if (revCard) revCard.setAttribute('data-bookmarked', 'true');
            this.saveBookmarks();
            this.showToast('⭐ Question bookmarked for revision!');
          }
          this.updateBookmarkedFilterCount();
        });
      });

      this.dom.reviewList.querySelectorAll('.btn-report-question').forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.stopPropagation();
          const qidx = parseInt(btn.getAttribute('data-qidx'), 10);
          this.openReportModal(qidx);
        });
      });
    }

    // Reset filter to 'all'
    this.applyReviewFilter('all');

    // Setup viral scorecard share button
    this.setupShareButton({
      correct,
      total,
      wrong,
      marksObtained,
      maxMarks,
      scorePct,
      examType: this.examType
    });

    // Record Attempt in Local Storage History
    this.recordAttemptHistory({
      path: typeof window !== 'undefined' ? window.location.pathname : 'test',
      title: (document.querySelector('h1')?.textContent || document.title || 'Practice Test').replace(/\s*\|\s*MockTestVault.*$/i, '').trim(),
      marksObtained,
      maxMarks,
      correct,
      total,
      wrong,
      skipped,
      scorePct,
      examType: this.examType,
      timeSpentSeconds: (this.timeLimitMinutes * 60) - this.timeRemaining,
      date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
      time: new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })
    });

    // Render Attempt Progression History Card
    this.renderAttemptHistory();

    // Update Bookmarked Filter Pill Count
    this.updateBookmarkedFilterCount();

    // Switch Views
    if (this.dom.testLayout) this.dom.testLayout.style.display = 'none';
    if (this.dom.statusContainer) this.dom.statusContainer.style.display = 'none';
    if (this.dom.scorecardView) {
      this.dom.scorecardView.classList.add('active');
      this.dom.scorecardView.style.display = 'block';
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  applyReviewFilter(filterType) {
    this.currentReviewFilter = filterType;

    // Update active filter pill
    document.querySelectorAll('.filter-pill').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-filter') === filterType);
    });

    const items = document.querySelectorAll('.review-item');
    items.forEach(el => {
      const res = el.getAttribute('data-result'); // 'correct', 'wrong', 'unanswered'
      const isCorrect = (res === 'correct');
      const isWrong = (res === 'wrong');
      const isUnanswered = (res === 'unanswered');
      const isReviewed = el.getAttribute('data-reviewed') === 'true';

      if (filterType === 'all') {
        el.style.display = 'block';
      } else if (filterType === 'wrong' || filterType === 'incorrect') {
        el.style.display = (isWrong || isUnanswered) ? 'block' : 'none';
      } else if (filterType === 'unanswered' || filterType === 'skipped') {
        el.style.display = isUnanswered ? 'block' : 'none';
      } else if (filterType === 'correct') {
        el.style.display = isCorrect ? 'block' : 'none';
      } else if (filterType === 'reviewed') {
        el.style.display = isReviewed ? 'block' : 'none';
      } else if (filterType === 'bookmarked') {
        const isBookmarked = el.getAttribute('data-bookmarked') === 'true';
        el.style.display = isBookmarked ? 'block' : 'none';
      }
    });
  }

  async retakeTest() {
    if (this.currentSet === 'random') {
      if (this.timerInterval) clearInterval(this.timerInterval);
      if (this.dom.scorecardView) {
        this.dom.scorecardView.classList.remove('active');
        this.dom.scorecardView.style.display = 'none';
      }
      if (this.dom.testLayout) this.dom.testLayout.style.display = 'grid';
      if (this.dom.statusContainer) this.dom.statusContainer.style.display = 'block';
      await this.loadQuestions();
      return;
    }

    this.userAnswers = new Array(this.questions.length).fill(null);
    this.reviewedFlags = new Array(this.questions.length).fill(false);
    this.visitedFlags = new Array(this.questions.length).fill(false);
    this.visitedFlags[0] = true;
    this.timeRemaining = this.timeLimitMinutes * 60;
    this.currentIndex = 0;
    this.isSubmitted = false;

    if (this.dom.scorecardView) {
      this.dom.scorecardView.classList.remove('active');
      this.dom.scorecardView.style.display = 'none';
    }
    if (this.dom.testLayout) this.dom.testLayout.style.display = 'grid';
    if (this.dom.statusContainer) this.dom.statusContainer.style.display = 'block';

    this.renderPalette();
    this.renderQuestion(0);
    this.updateProgress();

    if (this.mode === 'exam') {
      this.startTimer();
    }
  }

  openReportModal(qidx) {
    if (qidx < 0 || qidx >= this.questions.length) return;
    const q = this.questions[qidx];
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    
    // Remove existing modal if any
    const existingOverlay = document.getElementById('mcv-report-modal-overlay');
    if (existingOverlay) existingOverlay.remove();
    
    const examName = document.title ? document.title.split('|')[0].trim() : 'Mock Examination';
    const rawStem = q.question || '';
    const qSnippet = rawStem.length > 140 ? rawStem.substring(0, 140) + '...' : rawStem;
    const qId = q.id || `q_${qidx + 1}`;
    const correctLetter = letters[q.answer] || 'N/A';
    const correctVal = (q.options && q.options[q.answer] !== undefined) ? String(q.options[q.answer]) : '';
    
    const modalHtml = `
      <div id="mcv-report-modal-overlay" class="report-modal-overlay" role="dialog" aria-modal="true" aria-labelledby="report-modal-title">
        <div class="report-modal-card">
          <div class="report-modal-header">
            <div style="display:flex; align-items:center; gap:10px;">
              <span style="font-size:1.4rem;">🚩</span>
              <div>
                <h3 id="report-modal-title" style="margin:0; font-size:1.05rem; font-weight:700; color:var(--text-main);">Suggest Correction / Report Issue</h3>
                <div style="font-size:0.8rem; color:var(--text-muted); margin-top:2px;">
                  Question #${qidx + 1} &bull; ID: <code>${this.escapeHtml(qId)}</code>
                </div>
              </div>
            </div>
            <button type="button" class="report-modal-close" id="mcv-close-report-btn" aria-label="Close modal">&times;</button>
          </div>

          <div class="report-modal-body">
            <div class="report-q-summary">
              <div style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--text-muted); font-weight:700; margin-bottom:4px;">Target Question:</div>
              <p style="margin:0 0 6px; font-size:0.88rem; line-height:1.4; color:var(--text-main);">${this.formatChemicalFormulas(qSnippet)}</p>
              <div style="font-size:0.8rem; color:var(--success-text); font-weight:600;">Current Key: (${correctLetter}) ${this.escapeHtml(correctVal.substring(0, 60))}</div>
            </div>

            <div style="margin-top:14px;">
              <label for="mcv-report-category" style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:6px; color:var(--text-main);">
                Issue Category <span style="color:var(--danger);">*</span>
              </label>
              <select id="mcv-report-category" style="width:100%; padding:8px 12px; border-radius:6px; border:1px solid var(--border-color); background:var(--bg-surface); font-size:0.9rem; color:var(--text-main);">
                <option value="Incorrect Answer Key">Incorrect Answer Key (Marked option is wrong)</option>
                <option value="Mathematical / Scientific Error">Mathematical / Scientific / Factual Error</option>
                <option value="Ambiguous Question">Ambiguous Question / Multiple Plausible Answers</option>
                <option value="Typo / Grammar / Truncation">Typo, Grammar, or Incomplete Text</option>
                <option value="Unclear Explanation">Explanation Contradicts Key or Lacks Clarity</option>
                <option value="Other">Other Discrepancy</option>
              </select>
            </div>

            <div style="margin-top:14px;">
              <label for="mcv-report-details" style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:6px; color:var(--text-main);">
                Describe the Error &amp; Suggested Correction <span style="color:var(--danger);">*</span>
              </label>
              <textarea id="mcv-report-details" rows="3" placeholder="Please describe the discrepancy, formula issue, or correct factual reference..." style="width:100%; padding:8px 12px; border-radius:6px; border:1px solid var(--border-color); background:var(--bg-surface); font-size:0.88rem; font-family:inherit; color:var(--text-main); resize:vertical;"></textarea>
            </div>

            <div style="margin-top:14px;">
              <label for="mcv-report-email" style="display:block; font-size:0.85rem; font-weight:600; margin-bottom:6px; color:var(--text-main);">
                Your Email (Optional, for editorial resolution updates)
              </label>
              <input type="email" id="mcv-report-email" placeholder="student@example.com" style="width:100%; padding:8px 12px; border-radius:6px; border:1px solid var(--border-color); background:var(--bg-surface); font-size:0.88rem; color:var(--text-main);" />
            </div>

            <div id="mcv-report-feedback" style="display:none; margin-top:14px; padding:10px 14px; border-radius:6px; font-size:0.85rem; line-height:1.4;"></div>
          </div>

          <div class="report-modal-footer">
            <button type="button" class="btn btn-secondary" id="mcv-cancel-report-btn" style="padding:8px 16px; font-size:0.88rem;">Cancel</button>
            <button type="button" class="btn btn-primary" id="mcv-submit-report-btn" style="padding:8px 18px; font-size:0.88rem; font-weight:600;">Submit to Editorial Desk</button>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const overlay = document.getElementById('mcv-report-modal-overlay');
    setTimeout(() => overlay.classList.add('active'), 10);

    const closeModal = () => {
      overlay.classList.remove('active');
      setTimeout(() => overlay.remove(), 200);
    };

    document.getElementById('mcv-close-report-btn').addEventListener('click', closeModal);
    document.getElementById('mcv-cancel-report-btn').addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeModal();
    });

    document.getElementById('mcv-submit-report-btn').addEventListener('click', () => {
      const category = document.getElementById('mcv-report-category').value;
      const details = document.getElementById('mcv-report-details').value.trim();
      const email = document.getElementById('mcv-report-email').value.trim();
      const feedback = document.getElementById('mcv-report-feedback');

      if (!details || details.length < 5) {
        feedback.style.display = 'block';
        feedback.style.background = '#fef2f2';
        feedback.style.color = '#dc2626';
        feedback.style.border = '1px solid #fecaca';
        feedback.innerHTML = '⚠️ Please describe the discrepancy or suggested correction in a few words.';
        return;
      }

      // Save to localStorage
      try {
        const storedReports = JSON.parse(localStorage.getItem('mcv_user_discrepancy_reports') || '[]');
        storedReports.push({
          timestamp: new Date().toISOString(),
          exam: examName,
          url: window.location.href,
          questionIndex: qidx + 1,
          questionId: qId,
          category: category,
          details: details,
          userEmail: email || 'anonymous'
        });
        localStorage.setItem('mcv_user_discrepancy_reports', JSON.stringify(storedReports));
      } catch (err) {
        console.warn('LocalStorage save failed:', err);
      }

      // Prepare mailto link for direct submission to editorial desk
      const mailtoSubject = encodeURIComponent(`[Question Discrepancy] ${examName} - Q${qidx + 1} (${qId})`);
      const mailtoBody = encodeURIComponent(
        `Exam: ${examName}\n` +
        `URL: ${window.location.href}\n` +
        `Question #${qidx + 1} (ID: ${qId})\n` +
        `Issue Category: ${category}\n\n` +
        `Details / Correction:\n${details}\n\n` +
        `Reported by: ${email || 'Anonymous Student'}`
      );
      const mailtoUrl = `mailto:contact@mocktestvault.com?subject=${mailtoSubject}&body=${mailtoBody}`;

      feedback.style.display = 'block';
      feedback.style.background = '#ecfdf5';
      feedback.style.color = '#065f46';
      feedback.style.border = '1px solid #a7f3d0';
      feedback.innerHTML = `
        <div style="font-weight:700; margin-bottom:4px;">✓ Report Logged Successfully!</div>
        <div>Thank you for helping maintain exam accuracy. Our editorial desk investigates all reported discrepancies within 24–48 hours.</div>
        <div style="margin-top:8px;">
          <a href="${mailtoUrl}" style="display:inline-block; font-size:0.8rem; font-weight:600; color:#047857; text-decoration:underline;">
            Optional: Click here to also send directly via email &rarr;
          </a>
        </div>
      `;

      // Update button on review card
      const cardBtn = document.querySelector(`.btn-report-question[data-qidx="${qidx}"]`);
      if (cardBtn) {
        cardBtn.innerHTML = '✓ Reported';
        cardBtn.classList.add('reported');
        cardBtn.disabled = true;
      }

      // Change submit button to Close
      const submitBtn = document.getElementById('mcv-submit-report-btn');
      submitBtn.textContent = 'Close';
      submitBtn.onclick = closeModal;
      document.getElementById('mcv-cancel-report-btn').style.display = 'none';
    });
  }

  setupShareButton(scoreData) {
    const actionsContainer = document.querySelector('.scorecard-actions');
    if (!actionsContainer) return;

    let shareBtn = document.getElementById('btn-share-score');
    if (!shareBtn) {
      shareBtn = document.createElement('button');
      shareBtn.id = 'btn-share-score';
      shareBtn.className = 'nav-btn btn-share-score';
      shareBtn.type = 'button';
      actionsContainer.prepend(shareBtn);
    }

    shareBtn.innerHTML = `<span>📤</span> Share Score &amp; Challenge Friends`;

    // Clone to reset previous click listeners
    const freshBtn = shareBtn.cloneNode(true);
    shareBtn.parentNode.replaceChild(freshBtn, shareBtn);

    freshBtn.addEventListener('click', async () => {
      const pageTitle = (document.querySelector('h1')?.textContent || document.title || 'Practice Test')
        .replace(/\s*\|\s*MockTestVault.*$/i, '')
        .replace(/\s*—\s*MockTestVault.*$/i, '')
        .trim();

      const scoreText = scoreData.examType === 'competitive'
        ? `${scoreData.marksObtained}/${scoreData.maxMarks} marks`
        : `${scoreData.correct}/${scoreData.total} (${scoreData.scorePct}%)`;

      const shareUrl = window.location.href.split('#')[0];
      const shareTitle = `I scored ${scoreText} on ${pageTitle}!`;
      const shareMessage = `🎯 I just scored ${scoreText} on "${pageTitle}" on MockTestVault! 🏆 Can you beat my score? Take the free test here: ${shareUrl}`;

      if (navigator.share) {
        try {
          await navigator.share({
            title: shareTitle,
            text: shareMessage,
            url: shareUrl
          });
          return;
        } catch (err) {
          if (err.name === 'AbortError') return;
        }
      }

      // Clipboard fallback with toast notification
      try {
        await navigator.clipboard.writeText(shareMessage);
        this.showToast('🎉 Challenge copied to clipboard! Paste in WhatsApp, Telegram, or Discord to challenge friends.');
      } catch (e) {
        const ta = document.createElement('textarea');
        ta.value = shareMessage;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand('copy');
          this.showToast('🎉 Challenge copied to clipboard! Share with your friends.');
        } catch (copyErr) {
          this.showToast('Score: ' + scoreText + ' — Share: ' + shareUrl);
        }
        document.body.removeChild(ta);
      }
    });
  }

  showToast(message, duration = 3500) {
    let toast = document.getElementById('mtv-global-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'mtv-global-toast';
      toast.className = 'mtv-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    if (this._toastTimer) clearTimeout(this._toastTimer);
    this._toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, duration);
  }

  loadStoredBookmarks() {
    try {
      const raw = localStorage.getItem(this.bookmarkStorageKey);
      if (!raw) return new Set();
      const list = JSON.parse(raw);
      return new Set(Array.isArray(list) ? list : Object.keys(list));
    } catch (e) {
      return new Set();
    }
  }

  saveBookmarks() {
    try {
      localStorage.setItem(this.bookmarkStorageKey, JSON.stringify(Array.from(this.bookmarkedSet)));
    } catch (e) {}
  }

  getQuestionKey(q, index) {
    if (q && q.id) return String(q.id);
    const path = typeof window !== 'undefined' ? window.location.pathname : 'test';
    return `${path}_q${index}`;
  }

  toggleBookmark(q, index) {
    const qKey = this.getQuestionKey(q, index);
    const wasBookmarked = this.bookmarkedSet.has(qKey);
    if (wasBookmarked) {
      this.bookmarkedSet.delete(qKey);
      this.saveBookmarks();
      this.showToast('Question removed from bookmarks.');
    } else {
      this.bookmarkedSet.add(qKey);
      this.saveBookmarks();
      this.showToast('⭐ Question bookmarked for revision!');
    }
    this.renderQuestion(this.currentIndex);
  }

  updateBookmarkedFilterCount() {
    const filterGroup = document.querySelector('.review-filter-group');
    if (!filterGroup) return;

    let bmPill = document.getElementById('filter-bookmarked');
    if (!bmPill) {
      bmPill = document.createElement('button');
      bmPill.id = 'filter-bookmarked';
      bmPill.className = 'filter-pill filter-bookmarked';
      bmPill.setAttribute('data-filter', 'bookmarked');
      bmPill.innerHTML = `⭐ Saved (<span id="filter-count-bookmarked">0</span>)`;
      bmPill.addEventListener('click', () => this.applyReviewFilter('bookmarked'));
      filterGroup.appendChild(bmPill);
    }

    let count = 0;
    this.questions.forEach((q, idx) => {
      if (this.bookmarkedSet.has(this.getQuestionKey(q, idx))) count++;
    });

    const countEl = document.getElementById('filter-count-bookmarked');
    if (countEl) countEl.textContent = count;
  }

  recordAttemptHistory(attemptData) {
    try {
      const raw = localStorage.getItem(this.historyStorageKey);
      let history = raw ? JSON.parse(raw) : [];
      if (!Array.isArray(history)) history = [];
      history.push(attemptData);
      if (history.length > 100) history = history.slice(-100);
      localStorage.setItem(this.historyStorageKey, JSON.stringify(history));
    } catch (e) {}
  }

  getAttemptsForCurrentTest() {
    try {
      const raw = localStorage.getItem(this.historyStorageKey);
      if (!raw) return [];
      const history = JSON.parse(raw);
      if (!Array.isArray(history)) return [];
      const currentPath = typeof window !== 'undefined' ? window.location.pathname : '';
      return history.filter(h => h.path === currentPath);
    } catch (e) {
      return [];
    }
  }

  renderAttemptHistory() {
    let container = document.getElementById('attempt-history-box');
    if (!container) {
      const mastery = document.getElementById('mastery-container');
      container = document.createElement('div');
      container.id = 'attempt-history-box';
      if (mastery && mastery.parentNode) {
        mastery.parentNode.insertBefore(container, mastery.nextSibling);
      } else if (this.dom.scorecardView) {
        this.dom.scorecardView.appendChild(container);
      }
    }

    const attempts = this.getAttemptsForCurrentTest();
    if (!attempts || attempts.length === 0) return;

    const currentAttempt = attempts[attempts.length - 1];
    const prevAttempt = attempts.length > 1 ? attempts[attempts.length - 2] : null;

    let bannerHtml = '';
    if (!prevAttempt) {
      bannerHtml = `
        <div class="history-progression-banner benchmark">
          <span>🎯</span>
          <span><strong>Baseline Benchmark Recorded:</strong> You achieved <strong>${currentAttempt.pct}%</strong> (${currentAttempt.correct}/${currentAttempt.total}). Retake this test in 48–72 hours to test your long-term memory retention!</span>
        </div>
      `;
    } else {
      const diff = currentAttempt.pct - prevAttempt.pct;
      if (diff > 0) {
        bannerHtml = `
          <div class="history-progression-banner gain">
            <span>🚀</span>
            <span><strong>Improvement Detected!</strong> You scored <strong>${currentAttempt.pct}%</strong>, an increase of <strong>+${diff}%</strong> over your previous attempt (${prevAttempt.pct}%). Excellent retention!</span>
          </div>
        `;
      } else if (diff === 0) {
        bannerHtml = `
          <div class="history-progression-banner benchmark">
            <span>⚖️</span>
            <span><strong>Consistent Retention:</strong> Scored exactly <strong>${currentAttempt.pct}%</strong> matching your previous attempt. Review your mistakes below to reach 95%+!</span>
          </div>
        `;
      } else {
        bannerHtml = `
          <div class="history-progression-banner drop">
            <span>⚠️</span>
            <span><strong>Score Variation:</strong> ${currentAttempt.pct}% vs ${prevAttempt.pct}% on last attempt (${diff}%). Focus on the subtopics with warning tags below.</span>
          </div>
        `;
      }
    }

    let rowsHtml = '';
    attempts.slice().reverse().forEach((att, revIdx) => {
      const attNum = attempts.length - revIdx;
      const isCurrent = revIdx === 0;
      const timeMins = Math.floor(att.timeSpentSeconds / 60);
      const timeSecs = att.timeSpentSeconds % 60;
      const scoreStr = att.examType === 'competitive' 
        ? `${att.marksObtained}/${att.maxMarks} marks` 
        : `${att.correct}/${att.total}`;

      rowsHtml += `
        <tr class="${isCurrent ? 'current-attempt-row' : ''}">
          <td><strong>#${attNum}</strong> ${isCurrent ? '<span style="font-size:0.75rem; color:var(--primary); font-weight:700;">(Current)</span>' : ''}</td>
          <td>${att.date} ${att.time || ''}</td>
          <td>${scoreStr}</td>
          <td><strong>${att.pct}%</strong></td>
          <td>${timeMins}m ${timeSecs}s</td>
          <td>${att.pct >= 80 ? '<span style="color:var(--success); font-weight:700;">Mastered ✓</span>' : '<span style="color:var(--text-muted);">Practicing</span>'}</td>
        </tr>
      `;
    });

    container.innerHTML = `
      <div class="attempt-history-card">
        <div class="history-card-header">
          <h3><span>📈</span> Attempt Progression History on this Device</h3>
          <div style="display:flex; align-items:center; gap:10px;">
            <span class="history-badge">Attempt #${attempts.length}</span>
            <button type="button" class="btn-clear-history" id="btn-clear-test-history" title="Clear past history for this test">Reset History</button>
          </div>
        </div>
        ${bannerHtml}
        <div class="history-table-wrapper">
          <table class="history-table">
            <thead>
              <tr>
                <th>Attempt</th>
                <th>Date &amp; Time</th>
                <th>Score</th>
                <th>Accuracy</th>
                <th>Time Spent</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              ${rowsHtml}
            </tbody>
          </table>
        </div>
      </div>
    `;

    const clearBtn = document.getElementById('btn-clear-test-history');
    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        if (confirm('Clear local attempt history for this exam on this device?')) {
          this.clearCurrentTestHistory();
          container.innerHTML = '';
          this.showToast('Test history reset for this device.');
        }
      });
    }
  }

  clearCurrentTestHistory() {
    try {
      const raw = localStorage.getItem(this.historyStorageKey);
      if (!raw) return;
      let history = JSON.parse(raw);
      if (!Array.isArray(history)) return;
      const currentPath = typeof window !== 'undefined' ? window.location.pathname : '';
      history = history.filter(h => h.path !== currentPath);
      localStorage.setItem(this.historyStorageKey, JSON.stringify(history));
    } catch (e) {}
  }

  escapeHtml(text) {
    if (!text) return '';
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }
}
