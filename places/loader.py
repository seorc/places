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
    ]
    return json.dumps(dict([(m[1], row[m[0]]) for m in mappings]))


@click.command('load-file')
@click.argument('file')
@with_appcontext
def load_file_command(file):
    "Load data from a SEPOMEX pipe separated database."
    load_file(file)
    click.echo('Done!')


def init_app(app):
    app.cli.add_command(load_file_command)
