import os
from flask import Flask
from . import catalog
from . import db
from . import loader


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='topsecretmboy',
        DATABASE=os.path.join(app.instance_path, 'places.sqlite')
    )

    if test_config is None:
        app.config.from_envvar('PLACES_CFG', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints.
    app.register_blueprint(catalog.bp)

    # Setup database access.
    db.init_app(app)
    loader.init_app(app)

    return app
