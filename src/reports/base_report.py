"""Base template class for reports module."""
from abc import ABC, abstractmethod
from tabulate import tabulate


class BaseReport(ABC):
    """Abstract base class for reports."""

    @abstractmethod
    def generate(self, data):
        pass

    def display(self, result):
        if not result:
            print("Нет данных для отображения")
            return

        headers = result.get('headers', [])
        rows = result.get('rows', [])

        print(tabulate(rows, headers=headers, tablefmt='grid'))
