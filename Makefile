start:
	./scripts/start_project.sh

format:
	echo "FORMATTING CODE USING BLACK"
	@black app/

lint:
	python3.10 -m flake8 app/ --config=.flake8
	python3.10 -m pylint app/ --rcfile=.pylintrc

tests:
	@echo "RUNNING TESTS WITH PYTEST"
	@python -m pytest -vv

coverage:
	python -m pytest -vv --cov=. --cov-report=html --cov-config=.coveragerc

deploy: lint tests coverage

run:
	@echo "RUNNING APP"
	@cd app && python -m run

## remove build artifacts
clean-build:
	@echo "CLEANING BUILD ARTIFACTS"
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

## remove Python file artifacts
clean-pyc:
	@echo "CLEANING PYTHON FILE ARTIFACTS"
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

## remove test and coverage artifacts
clean-test:
	@echo "CLEANING TEST AND COVERAGE ARTIFACTS"
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

## remove all build, test, coverage and Python artifacts
clean: clean-build clean-pyc clean-test
	@echo "CLEANED ALL ARTIFACTS"
