from flask import Flask , render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    file.save(f'uploads/{file.filename}')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)