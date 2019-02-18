import os
import tempfile

import pytest
from places import create_app
from places.db import init_db
from places.loader import load_file

TEST_FILE = os.path.join(os.path.dirname(__file__), 'test_data.txt')


@pytest.fixture
def app():
    db_file, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        load_file(TEST_FILE)

    yield app

    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
