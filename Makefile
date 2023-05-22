#!/usr/bin/env make
LINE_LENGTH	  := 79
PYTHON        := python3
.DEFAULT_GOAL := help

.PHONY: all check clean clean-all format help lint

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo
	@echo "  all:    style and test"
	@echo "  preen:  format and lint"
	@echo "  format: format code, sort imports and requirements"
	@echo "  lint:   check code"
	@echo "  clean:  delete all generated files"
	@echo
	@echo "Initialise virtual environment (venv) with:"
	@echo
	@echo "  pip3 install virtualenv"
	@echo "  python3 -m virtualenv venv"
	@echo "  source venv/bin/activate"
	@echo "  pip3 install -Ur requirements.txt"
	@echo
	@echo "Start virtual environment (venv) with:"
	@echo
	@echo "  source venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "  deactivate"
	@echo

all: check

check: format lint

format:
	isort --line-length $(LINE_LENGTH) --profile black day_*/
	black --line-length $(LINE_LENGTH) day_*/
	sort-requirements requirements.txt

lint:
	flake8 --verbose day_*/**
	pylint  --verbose day_*/**

clean:
	# clean generated artefacts
	$(RM) -r **/__pycache__/ **/*/__pycache__/
	$(RM) -r .coverage
	$(RM) -r .hypothesis/
	$(RM) -r .pytest_cache/
	$(RM) -r public/

clean-all: clean
	# clean development environment
	$(RM) -r .venv/
	$(RM) -r .idea/
