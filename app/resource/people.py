from flask import (make_response, Blueprint, request)
from controller import people as people
import simplejson

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET", ])
@bp.route("/<string:fname>", methods=["GET", ])
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
    response = people.create(request.form)
    return response


@bp.route("/<string:lname>", methods=["PUT", ])
def put(lname: str = None):
    data = people.update(lname, request.form)
    response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@bp.route("/<string:lname>", methods=["DELETE", ])
def delete(lname: str = None):
    response = people.delete(lname)
    # response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    # response.headers['Content-Type'] = 'application/json'
    return response
