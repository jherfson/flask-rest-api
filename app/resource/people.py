from flask import (Flask, make_response, Blueprint, request)
from controller import people as people
import simplejson

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET"])
@bp.route("/<string:fname>", methods=["GET"])
def get(fname: str = None):

    if fname is None:
        data = people.read_all()
    else:
        data = people.read_one(fname)

    response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@bp.route("/", methods=["POST", ])
def post():
    data = people.create(request.form)
    # response = make_response(simplejson.dumps("", ensure_ascii=False), 200)
    # response.headers['Content-Type'] = 'application/json'
    return data


@bp.route("/<int:id>", methods=["PUT"])
def put(id:int=None):
    return "Update People"


@bp.route("/<int:id>", methods=["DELETE"])
def delete(id:int=None):
    return "Delete People"
