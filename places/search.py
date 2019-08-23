import re

from unidecode import unidecode

from places.db import get_db


def fts_pattern(pattern):
    """Convert a pattern to an fts representation."""
    fts = [f'{patt}*' for patt in pattern.split(' ') if patt]
    return ' '.join(fts)


def search_by_pattern(pattern, limit=20):
    """Perform a search for pattern."""
    pattern_ = normalize_pattern(pattern)
    db = get_db()
    results = db.execute(
        """
        SELECT json FROM places
        WHERE document MATCH ?
        ORDER BY rank DESC
        LIMIT ?;
        """,
        (fts_pattern(pattern_), limit)
    ).fetchall()

    return "[{}]".format(','.join([doc['json'] for doc in results]))


def normalize_pattern(pattern):
    """Transliterate and clean pattern.

    This function removes any special chars in the pattern, leaving only
    lowcased alphanumeric elemtnts.
    """
    return re.sub(r'[^a-z0-9 ]', '', unidecode(pattern).lower())
