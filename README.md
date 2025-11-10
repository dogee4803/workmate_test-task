# Тестовое задание для компании Workmate

## Repository clonning
```sh
git clone https://github.com/dogee4803/workmate_test-task.git

cd workmate_test-task
```

## Installation and commands
- Set up virtual environment `python -m venv venv`
    - For Windows: `venv\Scripts\activate`
    - For Linux, Mac: `source venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run Pylint `pylint main.py src/ tests/`
- Run tests `pytest tests/ -v`
- Run tests with coverage `pytest tests/ --cov=src --cov-report=term-missing`
- Run script with example data `python main.py --files data/products1.csv data/products2.csv --report average-rating`

## Available commands with Make (Also can be seen via `make help`)
```make
make venv      - Create virtual environment
make install   - Install dependencies
make test      - Run tests
make lint      - Run pylint
make coverage  - Run tests with coverage
make run       - Run the script with example data
```

## Для РЕВЬЮ
- Скриншоты работы лежат в папке 'Скриншоты'.
- Есть возможнсоть добавить новые отчёты на основе абстрактного класса BaseReport.
