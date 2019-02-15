from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Here we show the index, perhaps some help.'


@app.route('/load', methods=['POST'])
def load():
    return 'Here we refersh the catalog.'


@app.route('/search')
def search():
    pattern = request.args.get('q', 'NO_PATTERN')
    return f'Searching by {pattern}.'
