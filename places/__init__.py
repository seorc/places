import os
from flask import Flask
from . import catalog


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='topsecretmboy')

    if test_config is None:
        app.config.from_envvar('PLACES_CFG', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints
    app.register_blueprint(catalog.bp)

    return app
