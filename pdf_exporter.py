from pathlib import Path
from models import Expense


class PDFExporter:
    """Gera um relatório em PDF a partir da lista de gastos."""

    def __init__(self, output_path: Path):
        self.output_path = output_path

    def export(self, expenses: list[Expense]) -> None:
        """Gera o arquivo PDF com os gastos."""
        pass

    def calculate_total(self, expenses: list[Expense]) -> float:
        """Calcula o valor total dos gastos."""
        pass

    def format_line(self, expense: Expense) -> str:
        """Formata uma linha de gasto para o PDF."""
        pass
