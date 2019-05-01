from flask import (make_response, Blueprint, request, abort)
from controller import people as people
import simplejson

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET", ])
@bp.route("/<string:lname>", methods=["GET", ])
def get(lname: str = None):

    if lname is None:
        data = people.read_all()
    else:
        data = people.read_one(lname)
        if data is None:
            # otherwise, nope, not found
            abort(
                404, "Person with last name {lname} not found".format(lname=lname)
            )

    response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@bp.route("/", methods=["POST", ])
def post():
    person = request.form
    response = people.create(person)
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
    return response
