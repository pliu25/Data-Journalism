from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def about():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    return render_template('about.html', zipcodes = sorted(data["macro"].keys()))

@app.route('/macro')
def macro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    return render_template('macro.html')

@app.route('/micro')
def micro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    return render_template('micro.html')

app.run(debug=True)