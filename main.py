from api import Stations
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def stations_simple(request):
    stations = Stations()
    orig, dest = (
        request.args.get('orig', default=None, type=str),
        request.args.get('dest', default=None, type=str)
    )
    if not orig or not dest:
        return render_template('index.html')
    response = jsonify(dict(dist=stations.api(orig, dest)))
    response.headers.add('Access-Control-Allow-Origin', 'https://psyaro.github.io')
    return response

@app.route("/2451/", methods=["GET"])
def stations2451(request):
    stations = Stations()
    sta = request.args.get('sta', default=None, type=str)
    x, y = stations.return2451(sta)
    response = jsonify(dict(x=x, y=y))
    response.headers.add('Access-Control-Allow-Origin', 'https://psyaro.github.io')
    return response
