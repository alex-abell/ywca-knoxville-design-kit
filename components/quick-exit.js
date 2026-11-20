(function () {
  'use strict';
  // YWCA Knoxville design system (unofficial draft). The components are plain HTML and CSS.
  // This file names them and carries the one piece of behavior the system needs: Quick Escape.
  var names = ["Button", "ActionTile", "QuickExit", "CallToActionStrip", "MissionHeadline", "PhotoBand", "ValueTrio", "LocationCard", "SlideTitle", "StatTile", "HighlightBar", "DataTable", "PrivacyNotice", "TextField", "NewsletterBand", "SiteFooter"];
  var api = { version: '5', components: names };
  names.forEach(function (n) { api[n] = { name: n, kind: 'html-css' }; });

  // quickExit(url): leave the site at once. Replaces the page so Back does not return to it.
  api.quickExit = function (url) {
    try { window.location.replace(url || 'https://www.weather.gov/'); } catch (e) { /* blocked in a sandbox */ }
  };
  // bindQuickExit(button, url): wires a button, plus three quick presses of Shift.
  api.bindQuickExit = function (button, url) {
    if (button) { button.addEventListener('click', function () { api.quickExit(url); }); }
    var presses = 0, timer = null;
    document.addEventListener('keyup', function (ev) {
      if (ev.key !== 'Shift') { presses = 0; return; }
      presses += 1;
      clearTimeout(timer);
      timer = setTimeout(function () { presses = 0; }, 1500);
      if (presses >= 3) { presses = 0; api.quickExit(url); }
    });
  };
  window.YWCAKnox = api;
})();
