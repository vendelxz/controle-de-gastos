from pathlib import Path
from models import Expense


class StorageManager:
    """Gerencia a leitura e gravação dos gastos em arquivo JSON."""

    def __init__(self, path: Path):
        self.path = path

    def load_all(self) -> list[Expense]:
        """Carrega e retorna todos os gastos salvos no arquivo JSON."""
        pass

    def save_all(self, expenses: list[Expense]) -> None:
        """Salva todos os gastos no arquivo JSON."""
        pass

    def append(self, expense: Expense) -> None:
        """Adiciona um novo gasto e salva imediatamente no arquivo JSON."""
        pass

    def get_total(self) -> float:
        """Retorna o valor total dos gastos registrados."""
        pass
