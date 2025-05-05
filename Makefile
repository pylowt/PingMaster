SHELL := bash

.PHONY: test
test: ci_test
	poetry run pytest -v --tb=short

.PHONY: lint
lint:
	poetry run ruff check .

.PHONY: format
format:
	poetry run ruff format .

.PHONY: ci_test
ci_test:
	poetry install
	poetry run uvicorn app.ci_server:app --reload &
