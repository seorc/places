from places.search import normalize_pattern, fts_pattern


def test_normalize_pattern():
    assert normalize_pattern('AbC Def 22') == 'abc def 22'
    assert normalize_pattern('*i Ñ´áabcd/#&') == 'i naabcd'


def test_fts_pattern():
    assert fts_pattern('la  isla bonita  ') == 'la* isla* bonita*'
