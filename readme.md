# User Management (Flask example)--

A minimal Flask-based user management example with templates and static assets. Designed for local development and simple testing.

## Features

- Minimal user management routes and templates
- Example test using `pytest`
- Uses `instance/` for runtime configuration

## Prerequisites

- Python 3.8 or newer
- (Optional) Git

## Quick Setup

1. Create a virtual environment:

```powershell
python -m venv .venv
```

2. Activate the virtual environment (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt  # if provided
pip install Flask                # otherwise
```

## Run

Start the app directly:

```powershell
python app.py
```

Or use the Flask CLI (PowerShell):

```powershell
$env:FLASK_APP = "app.py"
flask run
```

Open http://127.0.0.1:5000 in your browser.

## Tests

Run the test suite with:

```powershell
pytest
```

## Project Structure

- `app.py` — application entrypoint
- `test_app.py` — tests
- `instance/` — runtime configuration
- `templates/` — Jinja2 templates
- `static/style.css` — styles

## Notes & Next Steps

- Add a `requirements.txt` to pin dependencies (I can create one).
- I can also add Docker support or CI configuration on request.

---

Updated README — concise setup, run, and test instructions.
