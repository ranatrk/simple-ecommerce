import flask
from flask import request, Response
import json


app = flask.Flask(__name__)


@app.route("/checkout", methods=["POST"])
def checkout():
    """
    checkout
    request params: list of watch IDs
    """
    watch_ids_json = request.get_json()
    # TODO

    return {}


app.run(host="0.0.0.0")
