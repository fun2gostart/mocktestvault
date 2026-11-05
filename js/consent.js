/*
 * MockTestVault — privacy-first consent handling.
 * Google Analytics is not requested from the network until the visitor chooses
 * "Accept All". The page head establishes Consent Mode defaults before config.
 */
(function () {
  'use strict';

  var GA_ID = 'G-05SFM1Q4MV';
  var STORAGE_KEY = 'mtv_consent_choice';
  var storedChoice = null;
  var tagLoadStarted = false;

  try { storedChoice = localStorage.getItem(STORAGE_KEY); } catch (e) {}

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  function consentValues(granted) {
    var value = granted ? 'granted' : 'denied';
    return {
      analytics_storage: value,
      ad_storage: value,
      ad_user_data: value,
      ad_personalization: value,
      personalization_storage: value,
      functionality_storage: 'granted',
      security_storage: 'granted'
    };
  }

  function persistChoice(choice) {
    try { localStorage.setItem(STORAGE_KEY, choice); } catch (e) {}
    storedChoice = choice;
  }

  function loadGoogleTag() {
    if (tagLoadStarted || document.querySelector('script[data-mtv-google-tag="true"]')) return;
    tagLoadStarted = true;

    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(GA_ID);
    script.setAttribute('data-mtv-google-tag', 'true');
    script.onload = function () {
      window.gtag('event', 'page_view', {
        page_title: document.title,
        page_location: window.location.href
      });
    };
    script.onerror = function () {
      tagLoadStarted = false;
      script.remove();
    };
    document.head.appendChild(script);
  }

  function applyConsent(choice) {
    if (choice !== 'accepted' && choice !== 'essential') return;

    persistChoice(choice);
    window.gtag('consent', 'update', consentValues(choice === 'accepted'));

    if (choice === 'accepted') loadGoogleTag();

    var banner = document.getElementById('mtv-consent-banner');
    if (banner) banner.style.display = 'none';
  }

  function showBanner() {
    var banner = document.getElementById('mtv-consent-banner');
    if (!banner) {
      banner = document.createElement('div');
      banner.id = 'mtv-consent-banner';
      banner.setAttribute('role', 'region');
      banner.setAttribute('aria-label', 'Privacy and cookie preferences');
      banner.innerHTML = `
        <div class="mtv-consent-content">
          <div class="mtv-consent-text">
            <strong>Privacy &amp; Cookie Preferences</strong>
            <p>Essential browser storage keeps preferences, bookmarks and practice history on this device. Google Analytics is not loaded unless you select Accept All. Essential Only keeps analytics and advertising consent denied. Contact and question-discrepancy reports are prepared as email drafts; MockTestVault does not save their text or email address in browser storage.</p>
          </div>
          <div class="mtv-consent-actions">
            <button id="mtv-consent-essential" class="mtv-consent-btn mtv-btn-subtle" type="button">Essential Only</button>
            <button id="mtv-consent-accept" class="mtv-consent-btn mtv-btn-primary" type="button">Accept All</button>
            <a href="/privacy.html" class="mtv-consent-link">Privacy Policy</a>
          </div>
        </div>
      `;
      document.body.appendChild(banner);

      document.getElementById('mtv-consent-accept').addEventListener('click', function () {
        applyConsent('accepted');
      });
      document.getElementById('mtv-consent-essential').addEventListener('click', function () {
        applyConsent('essential');
      });
    }
    banner.style.display = 'block';
  }

  function init() {
    if (storedChoice === 'accepted') {
      window.gtag('consent', 'update', consentValues(true));
      loadGoogleTag();
    } else if (storedChoice === 'essential') {
      window.gtag('consent', 'update', consentValues(false));
    } else {
      showBanner();
    }

    document.querySelectorAll('.open-cookie-preferences, #btn-cookie-preferences').forEach(function (el) {
      el.addEventListener('click', function (event) {
        event.preventDefault();
        showBanner();
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }

  window.openConsentPreferences = showBanner;
})();
