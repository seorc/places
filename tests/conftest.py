import os
import tempfile

import pytest
from places import create_app
from places.db import init_db
from places.loader import load_file


@pytest.fixture
def test_file_path():
    return os.path.join(os.path.dirname(__file__), 'test_data.txt')


@pytest.fixture
def app():
    db_file, db_path = tempfile.mkstemp()

    _app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with _app.app_context():
        init_db()

    yield _app

    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
