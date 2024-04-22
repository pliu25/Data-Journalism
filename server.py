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

    requested_zip = request.args.get("zip")
    all_zips = sorted(list(data["macro"].keys()))

    return render_template('about.html', requested_zip = requested_zip, all_zips = all_zips)

@app.route('/macro')
def macro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    requested_zip = request.args.get("zip")
    all_zips = sorted(list(data["macro"].keys()))

    return render_template('macro.html', requested_zip = requested_zip, all_zips = all_zips)

@app.route('/micro')
def micro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    all_zips = sorted(list(data["macro"].keys()))
    requested_zip = request.args.get("micro")

    return render_template('micro.html', requested_zip = requested_zip, all_zips = all_zips)

app.run(debug=True)