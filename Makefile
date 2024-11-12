build:
	poetry build

install:
	poetry install

lint:
	poetry run flake8 gendiff

clean:
	rm -rf .venv
	poetry install

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report lcov