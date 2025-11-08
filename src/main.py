"""Main script for brand analysis."""
import argparse

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Анализ рейтинга брендов')
    parser.add_argument('--files', nargs='+', required=True,
                       help='Пути к CSV файлам с данными')
    parser.add_argument('--report', required=True,
                       choices=['average-rating'],
                       help='Тип отчета для генерации')

    args = parser.parse_args()

    print(f"Files: {args.files}")
    print(f"Report: {args.report}")

    # Checking existing of files
    for file_path in args.files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline()
                print(f"Файл {file_path} доступен, первая строка: {first_line.strip()}")
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")

if __name__ == '__main__':
    main()
