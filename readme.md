**Project

- **Name:** User Management (Flask example)
- **Description:** Small Flask-based user management example with templates and static assets. Ready for local development and testing.

**Requirements

- **Python:** 3.8+
- **Python packages:** Flask (install with `pip install Flask`) or `pip install -r requirements.txt` if a `requirements.txt` is provided.

**Setup

- **Create venv:** `python -m venv .venv`
- **Activate (PowerShell):** `.venv\Scripts\Activate.ps1`
- **Install deps:** `pip install -r requirements.txt` or `pip install Flask`

**Run

- **Direct:** `python app.py`
- **Flask CLI (Windows PowerShell):**
  - `$env:FLASK_APP = "app.py"`
  - `flask run`

**Testing

- **Run tests:** `pytest`

**Project Structure

- **Entry point:** [app.py](app.py)
- **Tests:** [test_app.py](test_app.py)
- **Instance folder (config):** [instance](instance)
- **Templates:** [templates](templates)
- **Static files:** [static/style.css](static/style.css)

**Notes**

- The app uses the `instance/` folder for runtime configuration.
- Edit templates in the `templates` directory and styles in `static/style.css`.
- If you want, I can add a `requirements.txt` and a brief `README` run example for Docker.
