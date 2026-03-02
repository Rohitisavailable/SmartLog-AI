from flask import Flask , render_template, request, redirect
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

import os

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 #5 MB
app.config['ALLOWED_EXTENSIONS'] = ['.log', '.txt', '.csv']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        
        if file:
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

if __name__ == '__main__':
    app.run(debug=True)