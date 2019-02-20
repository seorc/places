import json
from places.db import get_db
from places.loader import join_row, to_json


def test_load_file(app, runner, test_file_path):
    runner.invoke(args=['load-file', test_file_path])

    with app.app_context():
        assert get_db().execute(
            'select count(*) from places'
        ).fetchone()[0] == 3


def test_join_row(sample_file_row):
    expected = '01000 San Ángel Colonia Álvaro Obregón' \
        ' Ciudad de México Ciudad de México'
    assert join_row(sample_file_row) == expected


def test_to_json(sample_file_row):
    expected = json.dumps({
        'postal_code': sample_file_row['d_codigo'],
        'neighborhood': sample_file_row['d_asenta'],
        'neighborhood_type': sample_file_row['d_tipo_asenta'],
        'municipality': sample_file_row['D_mnpio'],
        'state': sample_file_row['d_estado'],
        'city': sample_file_row['d_ciudad'],
        'zone': sample_file_row['d_zona'],
        'state_code': sample_file_row['c_estado'],
    })
    assert to_json(sample_file_row) == expected
