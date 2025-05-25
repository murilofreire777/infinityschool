# app/__init__.py
from flask import Flask
from .extensions import jwt
from .Controller.blueprints.auth import auth_bp
from .Controller.blueprints.items import items_bp
from os import getenv


def create_app():
    app = Flask(__name__)
    #app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['JWT_SECRET_KEY'] = getenv('API_SECRET_KEY')
    jwt.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    return app