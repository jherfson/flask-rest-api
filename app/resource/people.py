from flask import (Flask, make_response, Blueprint)

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET"])
@bp.route("/<int:id>", methods=["GET"])
def get(id:int =None):
    return "Return All Peoples"


@bp.route("/", methods=["POST", ])
def post():
    return "Add People"


@bp.route("/<int:id>", methods=["PUT"])
def put(id:int=None):
    return "Update People"


@bp.route("/<int:id>", methods=["DELETE"])
def delete(id:int=None):
    return "Delete People"
