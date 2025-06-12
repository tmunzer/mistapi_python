.PHONY: help init install install-prod test test-cov test-unit test-integration lint format build clean publish publish-test generate deps update sync

# Use bash as shell
SHELL := /bin/bash

# Project name (from top-level directory name)
PROJECT_NAME ?= $(shell basename $(CURDIR))

# Version for code generation (can be overridden)
VERSION ?= 0.55.14

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

init: ## Development setup
	uv sync

install: ## Install project in development mode
	uv sync

install-prod: ## Install project for production
	uv sync --no-dev

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=src/mistapi --cov-report=html --cov-report=term-missing

test-unit: ## Run specific test markers - unit tests
	uv run pytest -m unit

test-integration: ## Run specific test markers - integration tests
	uv run pytest -m integration

lint: ## Check code quality
	uv run ruff check src tests
	uv run ruff format --check src tests

format: ## Format code
	uv run ruff format src tests

build: ## Build package
	uv build

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov/ .coverage .pytest_cache/

publish-test: clean build ## Publish to test PyPI
	uv run twine upload --repository testpypi dist/*

publish: clean build ## Publish to PyPI
	uv run twine upload dist/*

generate: ## Run the code generation script
	uv run python generate_from_openapi.py $(VERSION)

deps: ## Show dependency tree
	uv tree

update: ## Update dependencies
	uv sync --upgrade

sync: ## Sync dependencies
	uv sync

pre-commit: ## Run pre-commit on all files
	uvx pre-commit run --all-files

pre-commit-install: ## Install pre-commit hooks
	uvx pre-commit install

pre-commit-update: ## Update pre-commit hooks
	uvx pre-commit autoupdate

check: clean format lint pre-commit test ## Run all checks and tests
