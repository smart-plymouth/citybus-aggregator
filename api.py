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
    return None
