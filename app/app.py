from gettext import Catalog
import flask
from flask import Response, request

from catalogue import Catalogue

app = flask.Flask(__name__)

catalogue = Catalogue()


@app.route("/checkout", methods=["POST"])
def checkout():
    """
    checkout
    request params: list of watch IDs e.g: ["001","002","001"]
    """
    watch_ids_json = request.get_json() or []
    try:
        final_price = catalogue.calculate_final_price(watch_ids_json)
        return {"price": final_price}
    except KeyError as e:
        return Response(str(e), status=400)


app.run(host="0.0.0.0")
