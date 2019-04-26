from flask import (Flask)
import simplejson


def create_app(test_config=None):

    # Cria a configura a aplicação
    app = Flask(__name__, instance_relative_config=True)

    return app
