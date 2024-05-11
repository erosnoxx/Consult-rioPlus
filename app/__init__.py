from flask import Flask
from dynaconf import FlaskDynaconf


def create_app(app):
    """
    Cria uma instância da aplicação Flask.

    Esta função cria e retorna uma instância da aplicação Flask. Além disso, ela ativa as configurações
    dinâmicas do Dynaconf, que são definidas no arquivo Settings.toml localizado na pasta raiz do sistema.

    Returns:
        Flask: Uma instância da aplicação Flask configurada.
    """
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list=True)
    return app
