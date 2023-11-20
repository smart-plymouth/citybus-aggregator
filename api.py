import requests

from flask import Flask
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def get_app_version():
    app_data = {
        "service": "CityBus Aggregator API",
        "version": 1.0
    }
    return jsonify(app_data)


@app.route("/proxy/vehicles")
def proxy_vehicles():
    resp = requests.get('https://www.plymouthbus.co.uk/_ajax/vehicles')
    print("Proxy result: %s - %s" % (resp.status_code, resp.text))
    return resp.json()
