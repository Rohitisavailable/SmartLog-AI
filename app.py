from flask import Flask , render_template, request, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save(os.path.join(
            'uploads/',
            secure_filename(file.filename)
        ))

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)