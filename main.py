from api import Stations
import json
from flask import Flask, jsonify, render_template

def stations_simple(request):
    stations = Stations()
    orig, dest = (
        request.args.get('orig', default=None, type=str),
        request.args.get('dest', default=None, type=str)
    )
    if not orig or not dest:
        return render_template('index.html')
    return jsonify(dict(dist=stations.api(orig, dest)))