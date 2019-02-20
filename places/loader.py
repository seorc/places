import csv
import json
import click
from places.db import get_db
from flask.cli import with_appcontext


def load_file(file):
    with open(file, encoding='iso-8859-1') as contents:
        # Throw  the first line, which is a comment.
        next(contents)

        reader = csv.DictReader(contents, delimiter='|')
        db = get_db()

        for row in reader:
            ins = """
                INSERT INTO places (document, json)
                VALUES (?, ?);
            """
            values = join_row(row), to_json(row)
            db.execute(ins, values)

        db.commit()


def join_row(row):
    keys = [
        'd_codigo',
        'd_asenta',
        'd_tipo_asenta',
        'D_mnpio',
        'd_estado',
        'd_ciudad',
    ]
    return ' '.join([row[k] for k in keys])


def to_json(row):
    mappings = [
        ('d_codigo', 'postal_code'),
        ('d_asenta', 'neighborhood'),
        ('d_tipo_asenta', 'neighborhood_type'),
        ('D_mnpio', 'municipality'),
        ('d_estado', 'state'),
        ('d_ciudad', 'city'),
        ('d_zona', 'zone'),
        ('c_estado', 'state_code'),
        ('iso', 'state_iso_code'),
    ]
    row['iso'] = state_to_iso(row['c_estado'])
    return json.dumps(dict([(m[1], row[m[0]]) for m in mappings]))


def state_to_iso(state_code):
    mappings = {
        '01': 'AGU',
        '02': 'BCN',
        '03': 'BCS',
        '04': 'CAM',
        '07': 'CHP',
        '08': 'CHH',
        '09': 'CMX',
        '05': 'COA',
        '06': 'COL',
        '10': 'DUR',
        '11': 'GUA',
        '12': 'GRO',
        '13': 'HID',
        '14': 'JAL',
        '15': 'MEX',
        '16': 'MIC',
        '17': 'MOR',
        '18': 'NAY',
        '19': 'NLE',
        '20': 'OAX',
        '21': 'PUE',
        '22': 'QUE',
        '23': 'ROO',
        '24': 'SLP',
        '25': 'SIN',
        '26': 'SON',
        '27': 'TAB',
        '28': 'TAM',
        '29': 'TLA',
        '30': 'VER',
        '31': 'YUC',
        '32': 'ZAC',
    }
    return 'MX-{}'.format(mappings[state_code])


@click.command('load-file')
@click.argument('file')
@with_appcontext
def load_file_command(file):
    "Load data from a SEPOMEX pipe separated database."
    load_file(file)
    click.echo('Done!')


def init_app(app):
    app.cli.add_command(load_file_command)
