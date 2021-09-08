import os

import fftcgtool
from flask import Flask

from .ffdecks import bp as ffdecks_bp


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.register_blueprint(ffdecks_bp)

    fftcgtool.RWCardDB(os.path.join(app.root_path, "carddb.zip"))

    return app
