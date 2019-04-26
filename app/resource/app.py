from flask import (Flask, render_template, make_response)
import simplejson

app = Flask(__name__)


@app.route("/")
def hello():
    data = {"message": "Hello World!"}
    response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route("/home/", methods=('GET',))
def home():
    return render_template('home.html')
