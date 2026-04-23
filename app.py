"""
CulturIQ – app.py
Run: python app.py
Then open http://localhost:5000

The HTML/JS frontend lives in templates/index.html.
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from flask import Flask, send_from_directory

app = Flask(__name__, template_folder="templates")

# Path to the pre-built frontend HTML
_HTML_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")


def _read_html() -> str:
    """Read the frontend HTML. Re-reads on every request in debug mode so
    changes to index.html are reflected immediately without restarting Flask."""
    with open(_HTML_PATH, "r", encoding="utf-8") as f:
        return f.read()


@app.route("/")
def index():
    from flask import Response
    return Response(_read_html(), mimetype="text/html")


@app.route("/favicon.ico")
def favicon():
    # Serve a blank 204 response to silence the 404 in logs
    from flask import Response
    return Response(status=204)


if __name__ == "__main__":
    print("[CulturIQ] Running at http://localhost:5000")
    print("  * Frontend: templates/index.html")
    print("  * Real geolocation via browser API")
    print("  * Real place data via OpenStreetMap / Overpass API")
    print("  * Real weather via Open-Meteo API")
    print("  * 360-degree VR: 3D panoramas + Street View toggle")
    app.run(debug=True, port=5000)