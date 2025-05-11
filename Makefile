SHELL := bash

.PHONY: test
test: unit_test integration_test

.PHONY: lint
lint:
	poetry run ruff check .

.PHONY: format
format:
	poetry run ruff format .

.PHONY: integration_test
integration_test:
	poetry run pytest -vs tests/integration --tb=short

.PHONY: unit_test
unit_test:
	poetry run pytest -vs tests/unit --tb=short
