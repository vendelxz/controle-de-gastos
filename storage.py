# storage.py
import json
from pathlib import Path
from typing import List
from models import Expense


class StorageManager:
    """Gerencia a persistência dos gastos em um arquivo JSON."""

    def __init__(self, path: Path):
        self.path = path
        if not self.path.exists():
            self._save_all([])  # Cria JSON vazio se não existir

    def _save_all(self, data: List[dict]):
        """Salva uma lista de dicionários no arquivo JSON."""
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise IOError(f"Erro ao salvar JSON: {e}")

    def load_all(self) -> List[Expense]:
        """Carrega todos os gastos do JSON como objetos Expense."""
        if not self.path.exists():
            return []
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Expense.from_dict(d) for d in data]
        except json.JSONDecodeError:
            # JSON corrompido → reseta
            self._save_all([])
            return []
        except Exception as e:
            raise IOError(f"Erro ao carregar JSON: {e}")

    def append(self, expense: Expense):
        """Adiciona um novo gasto, atribuindo ID automaticamente se necessário."""
        expenses = self.load_all()
        if expense.id is None:
            expense.id = self._get_next_id(expenses)
        expenses.append(expense)
        self._save_all([e.to_dict() for e in expenses])

    def delete_by_id(self, id: int) -> bool:
        """Deleta um gasto pelo ID. Retorna True se algo foi removido."""
        expenses = self.load_all()
        new_expenses = [e for e in expenses if e.id != id]
        removed = len(new_expenses) != len(expenses)
        self._save_all([e.to_dict() for e in new_expenses])
        return removed

    def delete_all(self) -> int:
        """Deleta todos os gastos. Retorna o número de registros removidos."""
        count = len(self.load_all())
        self._save_all([])
        return count

    def _get_next_id(self, expenses: List[Expense]) -> int:
        """Retorna o próximo ID disponível, garantindo unicidade."""
        if not expenses:
            return 1
        return max(e.id for e in expenses if e.id is not None) + 1
