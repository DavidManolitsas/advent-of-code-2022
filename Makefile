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

all: check day-1 day-2 day-3

check: format lint

format:
	isort --line-length $(LINE_LENGTH) --profile black day_*/
	black --line-length $(LINE_LENGTH) day_*/
	sort-requirements requirements.txt

lint:
	flake8 --verbose --ignore E203 day_*/**
	pylint --verbose day_*/**

day-1:
	python3 -m day_1 -f day_1/resources/input.txt -s 3

day-2:
	python3 -m day_2 -f day_2/resources/input.txt

day-3:
	python3 -m day_3 -f day_3/resources/input.txt

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
