from flask import (
    Blueprint, request, make_response
)
from places import search as searchm

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
    limit = request.args.get('limit', 10)
    resp = make_response(searchm.search_by_pattern(pattern, limit))
    resp.headers['Content-Type'] = 'application/json'
    return resp
