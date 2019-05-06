import os
import simplejson
from flask import (Flask, make_response)
from flask_cors import CORS
from .model import (db, ma)
from .config import TestingConfig, DevelopmentConfig, ProductionConfig

SET_CONFIG = {
    "test": TestingConfig,
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}


def create_app():

    # Cria a configura a aplicação
    app = Flask(__name__, instance_relative_config=True)

    flask_config = os.getenv('FLASK_CONFIG', 'default')
    app.config.from_object(SET_CONFIG[flask_config])

    # Criando instancia do banco de dados
    db.init_app(app)

    # Initialize Marshmallow
    ma.init_app(app)

    # Aplicando regras de CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.add_url_rule('/', 'root_route', root_route)

    # registrar Blueprints
    from .resource.people import bp as bp_people
    from .resource.note import bp as bp_note
    app.register_blueprint(bp_people)
    app.register_blueprint(bp_note)

    return app


# defino a funcao que retorna a rota principal da minha API
def root_route():

    resposta = {
        "message": """Bem Vindo(a) a API Backend com Flask do FLISOL 2019."""
    }

    response = make_response(simplejson.dumps(resposta, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
