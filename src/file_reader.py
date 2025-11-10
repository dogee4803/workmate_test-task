"""CSV file reader module."""
import csv
import os


def read_csv_files(file_paths):
    """Reads data from csv files and retuns List[Dict]."""

    all_data = []

    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            required_columns = ('name', 'brand', 'price', 'rating')
            if not all(col in reader.fieldnames for col in required_columns):
                raise ValueError(
                    f"Файл {file_path} не содержит нужные колонки: {required_columns}"
                )

            for row in reader:
                all_data.append(row)

    return all_data
