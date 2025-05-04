SHELL := bash

.PHONY: test
test:
	poetry run pytest -v --tb=short

.PHONY: lint
lint:
	poetry run ruff check .

.PHONY: format
format:
	poetry run ruff format .