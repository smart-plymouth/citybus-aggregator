import requests
import json

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
    url = "http://flaresolverr:8191/v1"

    payload = json.dumps({
        "cmd": "request.get",
        "url": "https://www.plymouthbus.co.uk/_ajax/vehicles",
        "maxTimeout": 60000
    })
    headers = {
        'Content-Type': 'application/json'
    }

    resp = requests.request("POST", url, headers=headers, data=payload)

    print("Proxy result: %s - %s" % (resp.status_code, resp.text))
    data = json.loads(resp.text)
    response = data.get('solution').get('response').replace('<html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
    response = response.replace('</pre></body></html>', '')
    return jsonify(json.loads(response))


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')

