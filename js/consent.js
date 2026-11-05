/**
 * MockTestVault — Consent Management & Google Consent Mode v2 Interface
 * Complies with GDPR, ePrivacy Directive, and Google Consent Mode specifications.
 */
(function() {
  window.dataLayer = window.dataLayer || [];
  function gtag(){ window.dataLayer.push(arguments); }

  const storedChoice = localStorage.getItem('mtv_consent_choice');

  // 1. Google Consent Mode v2 Default Settings
  gtag('consent', 'default', {
    'analytics_storage': storedChoice === 'essential' ? 'denied' : 'granted',
    'ad_storage': storedChoice === 'accepted' ? 'granted' : 'denied',
    'ad_user_data': storedChoice === 'accepted' ? 'granted' : 'denied',
    'ad_personalization': storedChoice === 'accepted' ? 'granted' : 'denied'
  });

  function applyConsent(choice) {
    localStorage.setItem('mtv_consent_choice', choice);
    if (choice === 'accepted') {
      gtag('consent', 'update', {
        'analytics_storage': 'granted',
        'ad_storage': 'granted',
        'ad_user_data': 'granted',
        'ad_personalization': 'granted'
      });
    } else {
      gtag('consent', 'update', {
        'analytics_storage': 'denied',
        'ad_storage': 'denied',
        'ad_user_data': 'denied',
        'ad_personalization': 'denied'
      });
    }
    const banner = document.getElementById('mtv-consent-banner');
    if (banner) banner.style.display = 'none';
  }

  function showBanner() {
    let banner = document.getElementById('mtv-consent-banner');
    if (!banner) {
      banner = document.createElement('div');
      banner.id = 'mtv-consent-banner';
      banner.setAttribute('role', 'region');
      banner.setAttribute('aria-label', 'Privacy and Cookie Preferences');
      banner.innerHTML = `
        <div class="mtv-consent-content">
          <div class="mtv-consent-text">
            <strong>🔒 Privacy &amp; Cookie Preferences</strong>
            <p>MockTestVault uses browser local storage exclusively for your test progress, dark/light theme, and bookmarks. Anonymous telemetry (Google Analytics 4) helps evaluate simulator stability. No individual test scores or answers are stored on our servers.</p>
          </div>
          <div class="mtv-consent-actions">
            <button id="mtv-consent-essential" class="mtv-consent-btn mtv-btn-subtle" type="button">Essential Only</button>
            <button id="mtv-consent-accept" class="mtv-consent-btn mtv-btn-primary" type="button">Accept All</button>
            <a href="/privacy.html" class="mtv-consent-link">Privacy Policy</a>
          </div>
        </div>
      `;
      document.body.appendChild(banner);

      document.getElementById('mtv-consent-accept').addEventListener('click', function() {
        applyConsent('accepted');
      });
      document.getElementById('mtv-consent-essential').addEventListener('click', function() {
        applyConsent('essential');
      });
    }
    banner.style.display = 'block';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    if (!storedChoice) {
      showBanner();
    }
    document.querySelectorAll('.open-cookie-preferences, #btn-cookie-preferences').forEach(el => {
      el.addEventListener('click', function(e) {
        e.preventDefault();
        showBanner();
      });
    });
  }

  window.openConsentPreferences = showBanner;
})();
