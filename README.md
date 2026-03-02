# SmartLog-AI

Simple Flask app to upload log/text files and view their content directly in the browser.

## Features

- Upload files with allowed extensions: `.log`, `.txt`, `.csv`
- Max upload size: `5 MB`
- List uploaded files on the home page
- Click a file to display its content on the same page

## Project Structure

- `app.py` - Flask routes and upload/view logic
- `templates/index.html` - UI for upload, file list, and file content display
- `static/style.css` - Styles
- `uploads/` - Saved uploaded files

## Requirements

- Python 3.9+
- pip

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install flask werkzeug
```

## Run the App

From the project root:

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000/
```

## How to Use

1. Choose a `.log`, `.txt`, or `.csv` file.
2. Click **Upload**.
3. In **Uploaded Files**, click the filename.
4. File content appears below in the content panel.

## Routes

- `GET /` - Home page with file list; optional `?file=<name>` to display content
- `POST /upload` - Upload a file
- `GET /view/<filename>` - Validate file and redirect to `/?file=<filename>`
- `GET /serve-image/<filename>` - Serve a file from uploads (legacy route)

## Notes

- File content is read as UTF-8 with replacement for unsupported characters.
- Only files in `uploads/` with allowed extensions are listed and viewable.
- If a file is missing or blocked by extension rules, the app shows an error message.

## Future Plan

SmartLog-AI will evolve from a file viewer into a deployed incident-analysis web application where users upload server logs and receive:

- Error summary
- Root cause explanation
- Severity classification
- Fix suggestions
- Preventive recommendations

### Product Experience

Target user flow:

`Upload Log → Filter Errors → AI Analysis → Dashboard Result → Incident Report`

The goal is a simple, reliable, and professional workflow that is easy to demo and practical for real troubleshooting.

### Planned Stack

- **Backend:** Python 3.10+ with Flask
- **Frontend:** Jinja templates + Bootstrap CDN (no React)
- **AI:** DigitalOcean Gradient AI API using prompt/response only
- **Deployment:** DigitalOcean Droplet (Ubuntu 22.04), Gunicorn, optional Nginx reverse proxy
- **Submission:** Devpost

### Planned Architecture

Proposed project layout for maintainability:

- `app.py`, `requirements.txt`, `.env`
- `templates/` (`base.html`, `index.html`, `result.html`)
- `static/style.css`
- `utils/log_parser.py`, `utils/ai_client.py`, `utils/pdf_report.py`
- `uploads/`

This separation keeps upload, parsing, AI calls, and reporting logic isolated for easier debugging and iteration.

### Feature Roadmap (No Timeline)

1. **Analysis pipeline**
	- Accept `.log`, `.txt`, `.csv` uploads (optional later: `.json`)
	- Enforce `MAX_CONTENT_LENGTH` at 5 MB
	- Route `/analyze` to validate file, parse logs, call AI, and render results

2. **Log parsing layer (`utils/log_parser.py`)**
	- Filter only important lines using keywords such as `error`, `failed`, `exception`, `timeout`, `critical`, `500`, `refused`, `crash`
	- Normalize text to lowercase before matching
	- Limit extracted lines (about 200–300) to control token usage and improve signal quality

3. **AI analysis layer (`utils/ai_client.py`)**
	- Load API key from `.env`
	- Send filtered logs to DigitalOcean Gradient AI with a structured DevOps-focused prompt
	- Return structured output fields: `root_cause`, `severity`, `fix_steps`, `prevention`

4. **Result UI (`result.html`)**
	- Summary card
	- Severity badge (`HIGH`, `MEDIUM`, `LOW`)
	- Clear sections for root cause, fix commands/steps, and prevention advice

5. **Incident report export (`utils/pdf_report.py`)**
	- Generate downloadable PDF with timestamp, severity, root cause, and fixes
	- Use `reportlab` for PDF generation

6. **Deployment hardening**
	- Run with Gunicorn on a DigitalOcean Droplet
	- Optional Nginx setup and custom domain
	- Keep IP-based access acceptable for submission demo

### Error Handling Goals

Planned user-facing handling with Flask flash messages for:

- Missing file upload
- Unsupported extension
- Empty file
- No relevant errors found in logs

### Demo and Submission Readiness

- Short demo flow: problem context, upload, AI output, fix guidance, infrastructure mention
- README will be expanded with problem statement, architecture diagram, screenshots, demo link, and full setup instructions

### Scope Guardrails

To keep solo execution realistic and submission-ready, avoid adding:

- Authentication systems
- Databases
- Chat features
- React frontend

Focus remains on reliable log-to-insight analysis with clean deployment and presentation.