# models.py
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional


ISO_FMT = "%Y-%m-%dT%H:%M:%S"  # padrão para serializar datas


@dataclass
class Expense:
    """
    Representa um gasto individual.
    - id: identificador único (pode ser None até o StorageManager atribuir).
    - valor: float (positivo).
    - descricao: string não-vazia.
    - categoria: int (deve corresponder a Category).
    - data: datetime (momento do registro).
    """
    id: Optional[int]
    valor: float
    descricao: str
    categoria: int
    data: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        # Normalizações e validações leves para evitar erros bobos
        if isinstance(self.data, str):
            try:
                self.data = datetime.strptime(self.data, ISO_FMT)
            except Exception as exc:
                raise ValueError(f"Formato de data inválido: {self.data!r}. Deve ser ISO '{ISO_FMT}'.") from exc

        # valor deve ser numérico e não-negativo
        try:
            self.valor = float(self.valor)
        except Exception as exc:
            raise ValueError(f"Valor inválido para 'valor': {self.valor!r}. Deve ser numérico.") from exc
        if self.valor < 0:
            raise ValueError("Valor do gasto não pode ser negativo.")

        # descrição não pode ser vazia
        if not isinstance(self.descricao, str) or not self.descricao.strip():
            raise ValueError("Descrição deve ser uma string não-vazia.")

        # categoria deve ser um int (validação sem checar se existe no Enum aqui)
        try:
            self.categoria = int(self.categoria)
        except Exception as exc:
            raise ValueError(f"Categoria inválida: {self.categoria!r}. Deve ser um inteiro.") from exc

    def to_dict(self) -> Dict[str, Any]:
        """
        Converte o Expense para dict pronto para JSON.
        - data é serializada em ISO (YYYY-MM-DDTHH:MM:SS)
        - valor é convertido para float com 2 casas (para leitura humana).
        """
        return {
            "id": self.id,
            "valor": round(float(self.valor), 2),
            "descricao": self.descricao.strip(),
            "categoria": int(self.categoria),
            "data": self.data.strftime(ISO_FMT),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Expense":
        """
        Cria um Expense a partir de um dicionário (por exemplo, carregado do JSON).
        Espera chaves: id (opcional), valor, descricao, categoria, data (ISO string ou datetime).
        Lança ValueError com mensagem clara se algo estiver faltando/errado.
        """
        if not isinstance(data, dict):
            raise ValueError("from_dict espera um dicionário.")

        # campos obrigatórios: valor, descricao, categoria
        missing = [k for k in ("valor", "descricao", "categoria") if k not in data]
        if missing:
            raise ValueError(f"Campos faltando para criar Expense: {missing}")

        id_ = data.get("id")
        valor = data["valor"]
        descricao = data["descricao"]
        categoria = data["categoria"]
        data_field = data.get("data", datetime.now())
        # Se data for string, deixamos que __post_init__ a converta; aqui passamos como está.

        return cls(id=id_, valor=valor, descricao=descricao, categoria=categoria, data=data_field)


class Category(Enum):
    """Enumeração simples de categorias com helpers para exibição e listagem."""

    ALIMENTOS = 1
    LAZER = 2
    TRANSPORTE = 3
    CONTAS = 4
    OUTROS = 5

    @staticmethod
    def get_label(category_id: int) -> str:
        """
        Retorna o rótulo amigável para um category_id.
        Lança ValueError se o id for inválido.
        """
        try:
            cid = int(category_id)
        except Exception as exc:
            raise ValueError(f"category_id inválido: {category_id!r}") from exc

        for member in Category:
            if member.value == cid:
                # transforma ALIMENTOS -> "Alimentos"
                return member.name.capitalize()
        raise ValueError(f"Categoria com id {cid} não existe.")

    @staticmethod
    def list_all() -> Dict[int, str]:
        """Retorna um dicionário {id: label} com todas as categorias."""
        return {member.value: member.name.capitalize() for member in Category}


# --- bloco de testes simples para rodar localmente ---
#if __name__ == "__main__":
    # Testes manuais básicos para garantir que o esqueleto se comporta bem.
  ##  print("Testando models.py ...")

    # criação válida
  ##  e = Expense(id=None, valor=12.5, descricao="Pão e leite", categoria=1)
  ##  print("Expense criado:", e)
  ##  d = e.to_dict()
   ## print("to_dict:", d)

    # reconstrução via from_dict com data string
   ## d2 = {
     ##   "id": 5,
      ##  "valor": "45.70",
      ## "descricao": "Cinema",
      ###  "categoria": 2,
      ##  "data": datetime.now().strftime(ISO_FMT),
  ##  }
    ##e2 = Expense.from_dict(d2)
   ## print("from_dict:", e2)
   ## print("Categorias disponíveis:", Category.list_all())
   ## print("Label categoria 2:", Category.get_label(2))

    # erros esperados (descomentar para testar)
    # Expense(id=None, valor="-5", descricao="negativo", categoria=1)  # -> ValueError
    # Expense(id=None, valor="abc", descricao="x", categoria=1)       # -> ValueError
    # Category.get_label(999)                                         # -> ValueError

    ##print("models.py OK")##
