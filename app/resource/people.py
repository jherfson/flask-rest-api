from flask import (make_response, Blueprint, request)
from ..controller import people as people
from . import ReturnMessage
import simplejson

bp = Blueprint('people', __name__, url_prefix='/people')


@bp.route("/", methods=["GET", ])
@bp.route("/<int:person_id>", methods=["GET", ])
def person_get(person_id: int = None):

    if person_id is None:
        data = people.read_all()
    else:
        data = people.read_one(person_id)
        if data == {}:
            data = {"message": ReturnMessage.GET_MESSAGE.format(person_id=person_id)}
            response = make_response(simplejson.dumps(data, ensure_ascii=False), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    response = make_response(simplejson.dumps(data, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@bp.route("/", methods=["POST", ])
def person_post():
    person = request.form
    data = people.create(person)

    message = {
        "success": {
            "message": ReturnMessage.POST_SUCCESS_MESSAGE.format(lname=person.get("lname", None)),
            "data": data
        },
        "fail": {
            "message": ReturnMessage.POST_FAIL_MESSAGE.format(lname=person.get("lname", None))
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


@bp.route("/<int:person_id>", methods=["PUT", ])
def person_put(person_id: int = None):
    person = request.form
    data = people.update(person_id, person)

    message = {
        "success": {
            "message": ReturnMessage.PUT_SUCCESS_FULL.format(lname=person.get("lname", None)),
            "data": data
        },
        "fail": {
            "message": ReturnMessage.NOT_FOUND_MESSAGE.format(person_id=person_id)
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


@bp.route("/<int:person_id>", methods=["DELETE", ])
def person_delete(person_id: int = None):
    data = people.delete(person_id)

    message = {
        "success": {
            "message": ReturnMessage.DELETED_SUCCESS_FULL.format(person_id=person_id),
            "data": data
        },
        "fail": {
            "message": ReturnMessage.NOT_FOUND_MESSAGE.format(person_id=person_id)
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


@bp.route("/<int:person_id>/notes", methods=["GET", ])
@bp.route("/<int:person_id>/notes/<int:note_id>", methods=["GET", ])
def note_get(person_id:int = None, note_id:int = None):
    pass


@bp.route("</int:person_id>/notes", methods=['POST', ])
def note_post(person_id:int = None):
    pass


@bp.route("/<int:person_id>/notes/<int:note_id>", methods=['PUT', ])
def note_put(person_id:int = None, note_id:int = None):
    pass


@bp.route("/api/people/<int:person_id>/notes/<int:note_id>", methods=['DELETE', ])
def note_delete(person_id:int = None, note_id:int = None):
    pass
