from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug import exceptions
import requests
app = Flask(__name__, template_folder='./template')

@app.route('/')
def index():
    return render_template('index.html')

def Get_Films(variable):
    data = requests.get('https://www.omdbapi.com/?apikey=6f6461a4&s=' + variable)
    data = data.json()
    data = data['Search']
    return data

@app.route('/', methods=['POST'])
def my_form_post():
    global variable
    variable = request.form['variable']
    data = Get_Films(variable)
    print(data)
    return render_template('films.html', mylist=data)



@app.route('/<string:film_id>', methods=['GET', 'POST'])
def film_handler(film_id):
    the_id = ""
    data = Get_Films(variable)
    for id in data:
        if id['imdbID']  == film_id:
            the_id = id['imdbID']
            fns = {
                'GET': id,
                'POST': variable
                }
            return render_template('afilm.html', single_film=id)




if __name__ == '__main__':
    app.run()