from flask import Flask

from .ffdecks import bp as ffdecks_bp


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.register_blueprint(ffdecks_bp)

    return app
