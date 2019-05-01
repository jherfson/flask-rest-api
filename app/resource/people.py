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
            data = {"message": "Person with last name {lname} not found".format(lname=lname)}
            response = make_response(simplejson.dumps(data, ensure_ascii=False), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@bp.route("/", methods=["POST", ])
def post():
    person = request.form
    data = people.create(person)

    message = {
        "success": {
            "message": "{lname} successfully created".format(lname=person.get("lname", None))
        },
        "fail": {
            "message": "Person with last name {lname} already exists".format(lname=person.get("lname", None))
        },
    }

    if data is True:
        response = make_response(simplejson.dumps(message["success"], ensure_ascii=False), 201)
        response.headers['Content-Type'] = 'application/json'

    # Otherwise, they exist, that's an error
    else:
        response = make_response(simplejson.dumps(message["fail"], ensure_ascii=False), 406)
        response.headers['Content-Type'] = 'application/json'
        return response

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
