from flask import (Flask)
from .model.db import db
from flask_cors import CORS
import simplejson


def create_app(test_config=None):

    # Cria a configura a aplicação
    app = Flask(__name__, instance_relative_config=True)

    # Criando instancia do banco de dados
    db.init_app(app)

    # Aplicando regras de CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    return app
