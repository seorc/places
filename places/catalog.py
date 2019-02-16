from flask import (
    Blueprint, request
)

bp = Blueprint('catalog', __name__, url_prefix='/catalog')


@bp.route('/')
def hello():
    return 'Here we show the index, perhaps the API help.'


@bp.route('/load', methods=['POST'])
def load():
    return 'Here we refersh the catalog.'


@bp.route('/search')
def search():
    pattern = request.args.get('q', 'NO_PATTERN')
    return f'Searching by {pattern}.'
