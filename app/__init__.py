from flask import (Flask, make_response)
from .model import (db, ma)
from flask_cors import CORS
import simplejson


def create_app():

    # Cria a configura a aplicação
    app = Flask(__name__, instance_relative_config=True)

    # Criando instancia do banco de dados
    db.init_app(app)

    # Initialize Marshmallow
    ma.init_app(app)

    # Aplicando regras de CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.add_url_rule('/', 'root_route', root_route)

    # registrar Blueprints
    from .resource.people import bp as bp_people
    app.register_blueprint(bp_people)

    return app


# defino a funcao que retorna a rota principal da minha API
def root_route():

    resposta = {
        "message": """Bem Vindo(a) a API Backend com Flask do FLISOL 2019."""
    }

    response = make_response(simplejson.dumps(resposta, ensure_ascii=False), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
