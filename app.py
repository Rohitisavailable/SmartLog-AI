

from flask import Flask , render_template, request, redirect, send_from_directory, abort
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

import os

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 #5 MB
app.config['ALLOWED_EXTENSIONS'] = ['.log', '.txt', '.csv']


def is_allowed_file(filename):
    extension = os.path.splitext(filename)[1].lower()
    return extension in app.config['ALLOWED_EXTENSIONS']


def get_allowed_files():
    files = os.listdir(app.config['UPLOAD_DIRECTORY'])
    return [filename for filename in files if is_allowed_file(filename)]

@app.route('/')
def index():
    filtered_files = get_allowed_files()
    selected_file = request.args.get('file')
    file_content = None
    error_message = None

    if selected_file:
        safe_name = secure_filename(selected_file)
        file_path = os.path.join(app.config['UPLOAD_DIRECTORY'], safe_name)

        if safe_name in filtered_files and os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                    file_content = file.read()
                selected_file = safe_name
            except OSError:
                error_message = 'Unable to read this file.'
        else:
            error_message = 'File not found or not allowed.'

    return render_template(
        'index.html',
        files=filtered_files,
        selected_file=selected_file,
        file_content=file_content,
        error_message=error_message
    )

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1].lower()
        
        if file:
    
            if extension not in app.config['ALLOWED_EXTENSIONS']:
                return 'This File is not allowed'
            file.save(os.path.join(
                app.config['UPLOAD_DIRECTORY'],
                secure_filename(file.filename)
            ))
    except RequestEntityTooLarge:
        return 'File is larger than the 5MB Limit'


    return redirect('/')


@app.route('/view/<filename>', methods=['GET'])
def view_file(filename):
    safe_name = secure_filename(filename)

    if not is_allowed_file(safe_name):
        abort(404)

    file_path = os.path.join(app.config['UPLOAD_DIRECTORY'], safe_name)
    if not os.path.isfile(file_path):
        abort(404)

    return redirect(f'/?file={safe_name}')

@app.route('/serve-image/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename)

if __name__ == '__main__':
    app.run(debug=True)