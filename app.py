from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug import exceptions
app = Flask(__name__, template_folder='./template')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)