flask-run:
	FLASK_APP=app/api.py flask run --host=0.0.0.0 --port=9785

coverage:
	coverage run --source app -m unittest tests/*.py tests/**/*.py

coverage-report:
	coverage run --source app -m unittest tests/*.py tests/**/*.py && coverage report -m