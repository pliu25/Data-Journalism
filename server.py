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
    
    zip_pop = data["macro"]
    zipcode_color = {}

    for key, value in zip_pop.items(): 
        if value < 1:
            zipcode_color[key]= "white"
        elif value <= 2:
            zipcode_color[key] = "240, 212, 255"
        elif value <= 98:
            zipcode_color[key] = "223, 169, 252"
        elif value <= 360:
            zipcode_color[key] = "202, 109, 252"
        elif value <= 655:
            zipcode_color[key] = "180, 59, 245"
        elif value <= 2380:
            zipcode_color[key] = "129, 4, 196"
    print(zipcode_color) 
    #use jinja templating to pass in zip, the use javascript 
    return render_template('macro.html', requested_zip = requested_zip, all_zips = all_zips, zipcode_color = zipcode_color)

@app.route('/micro')
def micro():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    all_zips = sorted(list(data["macro"].keys()))
    requested_zip = request.args.get("zipcode")
    zipcode = request.query_string.decode()
    breeds_dict = data["micro"][zipcode]

    return render_template('micro.html', requested_zip = requested_zip, all_zips = all_zips, zipcode = zipcode, breeds_dict = breeds_dict)

app.run(debug=True) 