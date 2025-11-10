"""Brands' average rating report module."""
from collections import defaultdict
from src.reports.base_report import BaseReport


class AverageRatingReport(BaseReport):
    """Class for generating AverageRatingReport"""
    def generate(self, data):
        if not data:
            return {'headers': ['Бренд', 'Средний рейтинг'], 'rows': []}

        brand_ratings = defaultdict(list)

        for row in data:
            brand = row['brand']
            try:
                rating = float(row['rating'])
                brand_ratings[brand].append(rating)
            except (ValueError, KeyError):
                continue

        results = []
        for brand, ratings in brand_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            results.append({
                'brand': brand,
                'average_rating': round(avg_rating, 2)
            })

        results.sort(key=lambda x: x['average_rating'], reverse=True)

        rows = [[item['brand'], item['average_rating']] for item in results]

        return {
            'headers': ['Бренд', 'Средний рейтинг'],
            'rows': rows
        }
