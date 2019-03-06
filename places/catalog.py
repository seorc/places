from flask import (
    Blueprint, request, make_response
)
from places.db import get_db

bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.route('/')
def hello():
    return 'Here we show the index, perhaps the API help.'


@bp.route('/load', methods=['POST'])
def load():
    return 'Here we refersh the catalog.'


@bp.route('/search')
def search():
    pattern = request.args.get('q', '').strip()
    limit = request.args.get('limit', 100)
    db = get_db()
    results = db.execute(
        """
        SELECT json FROM places
        WHERE document MATCH ?
        ORDER BY rank DESC
        LIMIT ?;
        """,
        (fts_pattern(pattern), limit)
    ).fetchall()

    resp = make_response(
        "[{}]".format(','.join([doc['json'] for doc in results]))
    )
    resp.headers['Content-Type'] = 'application/json'
    return resp


def fts_pattern(pattern):
    fts = [f'{patt}*' for patt in pattern.split(' ')]
    print(fts)
    return ' '.join(fts)
