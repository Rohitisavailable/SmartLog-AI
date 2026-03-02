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