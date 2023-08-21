install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

install_test:
	pip install pytest

test:
	poetry run pytest --cov=gendiff --cov-report xml

test-coverage:
	coverage report