from flask import (make_response, Blueprint, request)
from ..controller import note as note
from . import ReturnMessage
import simplejson

bp = Blueprint('note', __name__, url_prefix='/note')


@bp.route("/people/")
def get():
    return "Hello Work"


def post():
    pass


def put():
    pass


def delete():
    pass