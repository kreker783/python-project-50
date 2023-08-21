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
	coverage run -m pytest

test-coverage:
	coverage report
