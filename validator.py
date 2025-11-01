class Validator:
    """Classe responsável por validar os dados de entrada do usuário."""

    @staticmethod
    def validate_valor(valor: str) -> float:
        """Valida e converte o valor informado pelo usuário."""
        pass

    @staticmethod
    def validate_descricao(descricao: str) -> str:
        """Valida a descrição do gasto."""
        pass

    @staticmethod
    def validate_categoria(categoria_id: int) -> int:
        """Valida se a categoria é válida."""
        pass

    @staticmethod
    def validate_all(valor: str, descricao: str, categoria_id: int) -> tuple[bool, str]:
        """Executa todas as validações e retorna (ok, mensagem_erro)."""
        pass
