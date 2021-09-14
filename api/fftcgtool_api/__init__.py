import os

import fftcgtool
from flask import Flask
from flask_cors import CORS

from .ffdecks import bp as ffdecks_bp


def create_app() -> Flask:
    app: Flask = Flask(__name__)

    if app.debug:
        # Allow CORS in debug mode
        # production mode will have a reverse proxy
        CORS(app)

    app.register_blueprint(ffdecks_bp)

    fftcgtool.CardDB(os.path.join(app.root_path, "carddb.zip"))

    return app
