from places.db import get_db

def test_load_file(app, runner, test_file_path):
    runner.invoke(args=['load-file', test_file_path])

    with app.app_context():
        assert get_db().execute(
            'select count(*) from places'
        ).fetchone()[0] == 3

