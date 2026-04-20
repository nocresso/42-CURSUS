VENV = venv
NAME = a_maze_ing.py
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
REQ_FILE = requirements.txt
CONFIG_FILE = config.txt

all: install run

install: $(VENV)/bin/activate

$(VENV)/bin/activate: $(REQ_FILE)
	python3 -m venv $(VENV)
	$(PIP) install -r $(REQ_FILE)
	touch $(VENV)/bin/activate

run:
	$(PYTHON) $(NAME) $(CONFIG_FILE)

debug:
	$(PYTHON) -m pdb $(NAME) $(CONFIG_FILE)

lint:
	$(PYTHON) -m flake8 . --exclude=$(VENV)
	$(PYTHON) -m mypy . --exclude $(VENV) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	rm -rf $(VENV)

.PHONY: all run clean lint debug build