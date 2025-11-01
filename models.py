from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass
class Expense:
    """Representa um gasto individual do usuário."""
    id: int
    valor: float
    descricao: str
    categoria: int
    data: datetime

    def to_dict(self) -> dict:
        """Converte o objeto Expense em um dicionário para salvar em JSON."""
        pass

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Cria um objeto Expense a partir de um dicionário carregado do JSON."""
        pass


class Category(Enum):
    """Enumeração de categorias pré-definidas."""
    ALIMENTOS = 1
    LAZER = 2
    TRANSPORTE = 3
    CONTAS = 4
    OUTROS = 5

    @staticmethod
    def get_label(category_id: int) -> str:
        """Retorna o nome da categoria dado o ID."""
        pass

    @staticmethod
    def list_all() -> dict[int, str]:
        """Retorna todas as categorias em formato {id: nome}."""
        pass
