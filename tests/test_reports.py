"""Tests for reports module."""
from src.reports.average_rating_report import AverageRatingReport


def test_average_rating_report_empty_data():
    """Test report with empty data."""

    report = AverageRatingReport()
    result = report.generate([])

    assert result['headers'] == ['Бренд', 'Средний рейтинг']
    assert result['rows'] == []


def test_average_rating_report_single_brand():
    """Test report with single brand and multiple products."""

    test_data = [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'iphone 14', 'brand': 'apple', 'price': '799', 'rating': '4.7'},
    ]

    report = AverageRatingReport()
    result = report.generate(test_data)

    assert len(result['rows']) == 1
    assert result['rows'][0][0] == 'apple'
    assert result['rows'][0][1] == 4.8


def test_average_rating_report_multiple_brands():
    """Test report with multiple brands."""

    test_data = [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23', 'brand': 'samsung', 'price': '899', 'rating': '4.7'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.5'},
        {'name': 'iphone 14', 'brand': 'apple', 'price': '799', 'rating': '4.8'},
    ]

    report = AverageRatingReport()
    result = report.generate(test_data)

    assert len(result['rows']) == 3

    ratings = [row[1] for row in result['rows']]
    assert ratings == sorted(ratings, reverse=True)

    apple_rating = next(row[1] for row in result['rows'] if row[0] == 'apple')
    assert apple_rating == 4.85


def test_average_rating_report_invalid_ratings():
    """Test report with invalid rating values."""

    test_data = [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'invalid product', 'brand': 'apple', 'price': '999', 'rating': 'invalid'},
        {'name': 'another invalid', 'brand': 'samsung', 'price': '899', 'rating': ''},
        {'name': 'zero rating', 'brand': 'samsung', 'price': '899', 'rating': '0'},
    ]

    report = AverageRatingReport()
    result = report.generate(test_data)

    assert len(result['rows']) == 2
    apple_row = next(row for row in result['rows'] if row[0] == 'apple')
    samsung_row = next(row for row in result['rows'] if row[0] == 'samsung')
    assert apple_row[1] == 4.9
    assert samsung_row[1] == 0.0


def test_average_rating_report_rating_precision():
    """Test that ratings are properly rounded."""

    test_data = [
        {'name': 'product1', 'brand': 'apple', 'price': '999', 'rating': '4.666'},
        {'name': 'product2', 'brand': 'apple', 'price': '899', 'rating': '4.777'},
        {'name': 'product3', 'brand': 'samsung', 'price': '799', 'rating': '3.333'},
        {'name': 'product4', 'brand': 'samsung', 'price': '699', 'rating': '3.334'},
    ]

    report = AverageRatingReport()
    result = report.generate(test_data)

    apple_rating = next(row[1] for row in result['rows'] if row[0] == 'apple')
    samsung_rating = next(row[1] for row in result['rows'] if row[0] == 'samsung')

    assert apple_rating == 4.72
    assert samsung_rating == 3.33


def test_average_rating_report_missing_rating_field():
    """Test report with missing rating field in some rows."""

    test_data = [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'iphone 14', 'brand': 'apple', 'price': '799'},  # missing rating
        {'name': 'galaxy s23', 'brand': 'samsung', 'price': '899', 'rating': '4.7'},
    ]

    report = AverageRatingReport()
    result = report.generate(test_data)

    assert len(result['rows']) == 2
    apple_rating = next(row[1] for row in result['rows'] if row[0] == 'apple')
    samsung_rating = next(row[1] for row in result['rows'] if row[0] == 'samsung')
    assert apple_rating == 4.9
    assert samsung_rating == 4.7


def test_average_rating_report_single_product_per_brand():
    """Test report where each brand has only one product."""

    test_data = [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23', 'brand': 'samsung', 'price': '899', 'rating': '4.7'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.5'},
    ]

    report = AverageRatingReport()
    result = report.generate(test_data)

    assert len(result['rows']) == 3
    ratings = [row[1] for row in result['rows']]
    assert ratings == [4.9, 4.7, 4.5]


def test_average_rating_report_display_empty():
    """Test display method with empty result."""

    report = AverageRatingReport()

    report.display({'headers': ['Бренд', 'Средний рейтинг'], 'rows': []})


def test_average_rating_report_display_normal():
    """Test display method with normal data."""

    report = AverageRatingReport()
    result = {
        'headers': ['Бренд', 'Средний рейтинг'],
        'rows': [['apple', 4.8], ['samsung', 4.6]]
    }

    report.display(result)
