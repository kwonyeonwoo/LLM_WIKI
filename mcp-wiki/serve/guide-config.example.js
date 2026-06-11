// Optional override for the in-site chatbot. NO API KEY anywhere.
// The chatbot talks to a LOCAL bridge (serve/guide_bridge.py) that reuses the
// logged-in `claude` CLI (your subscription) — keyless. Default: localhost:8765.
//
// Only set this if your bridge runs on a different host/port. Copy to guide-config.js:
//     cp guide-config.example.js guide-config.js
// build_site.py copies guide-config.js into site/ (falls back to this example).
//
// You can also change the bridge URL at runtime in the site's ⚙ settings.

window.GUIDE_CONFIG = {
  bridge: "http://localhost:8765"
};
