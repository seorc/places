# Places

A small service to find data about locations in México (colonies,
municipalities, states, etc.) with the power of full text search.

## Quick start

1. Install the dependencies (preferably in a virtualenv): `pip install -e .`
2. Setup the application environment: `export FLASK_APP=places`.
3. Launch the flask application: `flask run`.
4. Initialize the DB: `flask init-db`
5. Load a database file: `flask load-file /path/to/CPdescarga.txt`. Currently,
   the application has support for a pipe separated database (TXT format) from SEPOMEX
   (https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx).
6. Perform a search: `curl GET
   "localhost:5000/catalog/search?q=tlalpu+mich&limit=3" | jq`

## Testing

1. Install the test extras  `pip install -e .[test]`.
2. Run `pytest` or `coverage run -m pytest` for coverage revision.
