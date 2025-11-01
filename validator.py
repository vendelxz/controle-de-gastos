# validator.py
from typing import Union
from models import Category

class Validator:
    """Classe responsável por validar dados antes de criar ou manipular gastos."""

    @staticmethod
    def validate_valor(valor: Union[str, float, int]) -> float:
        """
        Valida e converte o valor do gasto.
        - Deve ser numérico e positivo.
        - Retorna float válido.
        """
        try:
            v = float(valor)
        except (ValueError, TypeError):
            raise ValueError(f"Valor inválido: {valor}. Deve ser um número.")
        if v < 0:
            raise ValueError(f"Valor negativo não permitido: {v}.")
        return v

    @staticmethod
    def validate_descricao(descricao: str) -> str:
        """
        Valida a descrição do gasto.
        - Deve ser string não vazia.
        - Retorna a string limpa.
        """
        if not isinstance(descricao, str):
            raise ValueError(f"Descrição inválida: {descricao}. Deve ser uma string.")
        desc = descricao.strip()
        if not desc:
            raise ValueError("Descrição não pode ser vazia.")
        return desc

    @staticmethod
    def validate_categoria(categoria: Union[str, int]) -> int:
        """
        Valida a categoria do gasto.
        - Deve ser um ID válido de Category.
        - Retorna o ID como int.
        """
        try:
            cat_id = int(categoria)
        except (ValueError, TypeError):
            raise ValueError(f"Categoria inválida: {categoria}. Deve ser um número inteiro.")

        if cat_id not in [c.value for c in Category]:
            raise ValueError(f"Categoria inexistente: {cat_id}. Valores válidos: {[c.value for c in Category]}")
        return cat_id


##TESTES


