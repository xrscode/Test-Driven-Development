#################################################################################
#
# Makefile to build the project
#
#################################################################################

PROJECT_NAME = test-driven-development 
PYTHON_INTERPRETER = python3.12
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip
ROOT_DIR := $(shell pwd)
ACTIVATE_ENV := source venv/bin/activate

# Install Dependencies
DEPENDENCIES_DIR = src/python/lib/python3.12/site-packages
install-dependencies:
	pip install -r requirements.txt -r ./requirements.txt

## Create python interpreter environment.
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> check python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up VirtualEnv."
	( \
		export PYTHONPATH=$(ROOT_DIR);\
	    $(PIP) install -q virtualenv virtualenvwrapper; \
	    virtualenv venv --python=$(PYTHON_INTERPRETER); \
		${ACTIVATE_ENV}; \
	)

# Execute python related functionalities from within the project's environment
define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

## Build the environment requirements
requirements: create-environment
	$(call execute_in_env, $(PIP) install -r ./requirements.txt)

################################################################################################################

# ## Run the flake8 code check
run-flake:
	$(call execute_in_env, flake8  ./katas/*.py)

run-autopep8:
	$(call execute_in_env, autopep8 --in-place --aggressive --aggressive  ./katas/*.py)
	

# ## Run the all unit tests
run-unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)

set_path:
	export PYTHONPATH=$(pwd)

