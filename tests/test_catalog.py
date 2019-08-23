import json


def test_extra_spaces_are_ignored(client):
    result = client.get('/catalog/search?q=%20+san+%20')
    assert result.status_code == 200
    assert len(json.loads(result.data)) == 1


def test_special_chars_are_ignored(client):
    result = client.get('/catalog/search?q=*+san#+&&')
    assert result.status_code == 200
    assert len(json.loads(result.data)) == 1
