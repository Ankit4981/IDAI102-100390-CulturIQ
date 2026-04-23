"""
CulturIQ – app.py

Local run:
    python app.py
    → http://localhost:5000

Production:
    gunicorn app:app
"""

import sys
import os
from flask import Flask, Response, render_template

# Ensure UTF-8 output (safe for logs)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Initialize Flask
app = Flask(__name__, template_folder="templates")

# Path to HTML (fallback method)
_HTML_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")


def _read_html() -> str:
    """Read HTML file directly (fallback if template fails)."""
    try:
        with open(_HTML_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"<h1>Error loading UI</h1><pre>{e}</pre>"


@app.route("/")
def index():
    """
    Serve main frontend.
    Uses render_template first (preferred),
    falls back to manual file read if needed.
    """
    try:
        return render_template("index.html")
    except Exception:
        return Response(_read_html(), mimetype="text/html")


@app.route("/health")
def health():
    """Health check endpoint (useful for deployment platforms)."""
    return {"status": "ok"}


@app.route("/favicon.ico")
def favicon():
    """Prevent favicon 404 errors."""
    return Response(status=204)


# Entry point (only for local development)
if __name__ == "__main__":
    print("[CulturIQ] Running locally at http://localhost:5000")
    print("Frontend: templates/index.html")
    app.run(debug=False)
