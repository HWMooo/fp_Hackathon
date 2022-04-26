from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug import exceptions
import requests
app = Flask(__name__, template_folder='./template')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    print(variable)
    data = requests.get('https://www.omdbapi.com/?apikey=6f6461a4&s=' + variable)
    data = data.json()
    print(data['Search'])
    return render_template('films.html', mylist=data['Search'])


if __name__ == '__main__':
    app.run()