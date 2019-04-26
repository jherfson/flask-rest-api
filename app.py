from flask import (render_template, Flask)
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/home/", methods=('GET',))
def home():
    return render_template('home.html')
