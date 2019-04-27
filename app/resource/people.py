from flask import (Flask, make_response, Blueprint)

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET"])
def get():
    return "Return All Peoples"
