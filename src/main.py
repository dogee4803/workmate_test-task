"""Main script for brand analysis."""
import argparse
import sys

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
    
    # TODO: Реализовать логику отчетов
    
if __name__ == '__main__':
    main()