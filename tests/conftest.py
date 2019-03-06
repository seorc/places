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
def sample_file_row():
    return {
        'd_codigo': '01000',
        'd_asenta': 'San Ángel',
        'd_tipo_asenta': 'Colonia',
        'D_mnpio': 'Álvaro Obregón',
        'd_estado': 'Ciudad de México',
        'd_ciudad': 'Ciudad de México',
        'd_CP': '01001',
        'c_estado': '09',
        'c_oficina': '01001',
        'c_CP': '',
        'c_tipo_asenta': '09',
        'c_mnpio': '010',
        'id_asenta_cpcons': '0001',
        'd_zona': 'Urbano',
        'c_cve_ciudad': '01',
    }


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
def preloaded_app(app, test_file_path):
    with app.app_context():
        load_file(test_file_path)
    yield app


@pytest.fixture
def client(preloaded_app):
    return preloaded_app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
