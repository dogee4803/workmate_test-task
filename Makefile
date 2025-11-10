ifeq ($(OS),Windows_NT)
	ACTIVATE = . venv\Scripts\activate
else
	ACTIVATE = . venv/bin/activate
endif

venv:
	python3 -m venv venv

install: venv
	@echo "Installing dependencies..."
	$(ACTIVATE) && pip install -r requirements.txt

lint:
	@echo "Running pylint..."
	$(ACTIVATE) && pylint main.py src/ tests/

test:
	@echo "Running tests..."
	$(ACTIVATE) && pytest tests/ -v

coverage:
	@echo "Running tests with coverage..."
	$(ACTIVATE) && pytest tests/ --cov=src --cov-report=term-missing

run:
	@echo "Running script with example data... "
	$(ACTIVATE) && python main.py --files data/products1.csv data/products2.csv --report average-rating

help:
	@echo "Available commands:"
	@echo "  make venv      - Create virtual environment"
	@echo "  make install   - Install dependencies"
	@echo "  make test      - Run tests"
	@echo "  make lint      - Run pylint"
	@echo "  make coverage  - Run tests with coverage"
	@echo "  make run       - Run the script with example data"