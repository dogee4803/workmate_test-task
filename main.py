"""Main script for brand analysis."""
import argparse
import sys

from src.file_reader import read_csv_files
from src.reports.average_rating_report import AverageRatingReport

def main():
    parser = argparse.ArgumentParser(description='Анализ рейтинга брендов')
    parser.add_argument('--files', nargs='+', required=True,
                       help='Пути к CSV файлам с данными')
    parser.add_argument('--report', required=True,
                       choices=['average-rating'],
                       help='Тип отчета для генерации')

    args = parser.parse_args()

    print(f"Files: {args.files}")
    print(f"Report: {args.report}")

    try:
        data = read_csv_files(args.files)

        if args.report == 'average-rating':
            report = AverageRatingReport()
            result = report.generate(data)
            report.display(result)
        else:
            print(f"Неизвестный тип отчета: {args.report}")
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: Неверный формат данных - {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
