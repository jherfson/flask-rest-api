from flask import (make_response, Blueprint, request)
from ..controller import people as people
import simplejson

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET", ])
@bp.route("/<string:person_id>", methods=["GET", ])
def get(person_id: int = None):

    if person_id is None:
        data = people.read_all()
    else:
        data = people.read_one(person_id)
        if data == {}:
            data = {"message": "The Person with ID {person_id} not found".format(person_id=person_id)}
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
            "message": "{lname} successfully created".format(lname=person.get("lname", None)),
            "data": data
        },
        "fail": {
            "message": "Person with last name {lname} already exists".format(lname=person.get("lname", None))
        },
    }

    if data is False:
        # Otherwise, they exist, that's an error
        response = make_response(simplejson.dumps(message["fail"], ensure_ascii=False), 406)
        response.headers['Content-Type'] = 'application/json'

    else:
        response = make_response(simplejson.dumps(message["success"], ensure_ascii=False), 406)
        response.headers['Content-Type'] = 'application/json'
        return response

    return response


@bp.route("/<string:person_id>", methods=["PUT", ])
def put(person_id: int = None):
    person = request.form
    data = people.update(person_id, person)

    message = {
        "success": {
            "message": "{lname} successfully updated".format(lname=person.get("lname", None)),
            "data": data
        },
        "fail": {
            "message": "The Person with ID {person_id} not found".format(person_id=person_id)
        }
    }

    if data is False:
        response = make_response(simplejson.dumps(message["fail"], ensure_ascii=False), 404)
        response.headers['Content-Type'] = 'application/json'
    else:
        response = make_response(simplejson.dumps(message["success"], ensure_ascii=False), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    return response


@bp.route("/<string:person_id>", methods=["DELETE", ])
def delete(person_id: int = None):
    data = people.delete(person_id)

    message = {
        "success": {
            "message": "{person_id} successfully deleted".format(person_id=person_id),
            "data": data
        },
        "fail": {
            "message": "The Person with ID {person_id} not found".format(person_id=person_id)
        },
    }

    if data is None:
        # Otherwise, nope, person to delete not found
        response = make_response(simplejson.dumps(message["fail"], ensure_ascii=False), 404)
        response.headers['Content-Type'] = 'application/json'

    else:
        response = make_response(simplejson.dumps(message["success"], ensure_ascii=False), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    return response
