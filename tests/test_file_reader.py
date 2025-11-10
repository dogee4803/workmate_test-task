"""Tests for file reader module."""
import csv
import pytest
from src.file_reader import read_csv_files


def test_read_csv_files_single_file(tmp_path):
    """Test reading single CSV file."""

    test_file = tmp_path / "test.csv"
    with open(test_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerows([
                    {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
                    {'name': 'Galaxy 11', 'brand': 'samsung', 'price': '599', 'rating': '4.6'},
                    {'name': 'iphone 13', 'brand': 'apple', 'price': '699', 'rating': '4.5'},
                ])

    result = read_csv_files([test_file])
    assert len(result) == 3
    assert result[0]['brand'] == 'apple'
    assert result[0]['rating'] == '4.9'


def test_read_csv_files_multiple_files(tmp_path):
    """Test reading multiple CSV files."""

    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"

    with open(file1, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({
            'name': 'iphone 15 pro',
            'brand': 'apple',
            'price': '999',
            'rating': '4.9'
        })

    with open(file2, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'brand', 'price', 'rating'])
        writer.writeheader()
        writer.writerow({
            'name': 'galaxy s23',
            'brand': 'samsung',
            'price': '899',
            'rating': '4.7'
        })

    result = read_csv_files([file1, file2])
    assert len(result) == 2
    brands = [row['brand'] for row in result]
    assert 'apple' in brands
    assert 'samsung' in brands


def test_read_csv_files_file_not_found():
    """Test handling of non-existent files."""

    with pytest.raises(FileNotFoundError):
        read_csv_files(['nonexistent_file.csv'])


def test_read_csv_files_invalid_format(tmp_path):
    """Test handling of files with invalid format."""

    test_file = tmp_path / "invalid.csv"
    with open(test_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['product', 'company', 'cost', 'score'])
        writer.writeheader()
        writer.writerow({
            'product': 'test',
            'company': 'test',
            'cost': '100',
            'score': '5.0'
        })

    with pytest.raises(ValueError):
        read_csv_files([test_file])
