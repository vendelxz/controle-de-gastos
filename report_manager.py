# Em um novo arquivo, ex: report_manager.py
from pathlib import Path 
from storage import StorageManager
from pdf_exporter import PDFGenerator
from models import Category

class GeradorRelatoriosCategoria:
    def __init__(self, storage: StorageManager):
        self.storage = storage
        # 1. Definir o nome do diretório
        self.diretorio_relatorios = Path("relatorios_por_categoria")

    def _preparar_diretorio(self):
        """Cria o diretório de relatórios se ele não existir."""
        try:
            self.diretorio_relatorios.mkdir(exist_ok=True)
        except Exception as e:
            # Lida com um possível erro de permissão
            raise IOError(f"Não foi possível criar o diretório {self.diretorio_relatorios}: {e}")

    def gerar_todos_os_relatorios(self) -> int:
        # 2. Garante que o diretório exista antes de começar
        self._preparar_diretorio()
        
        todos_os_gastos = self.storage.load_all() #
        contador_relatorios = 0

        for categoria in Category: #
            gastos_da_categoria = [
                gasto for gasto in todos_os_gastos 
                if gasto.categoria == categoria.value
            ]

            if gastos_da_categoria:
                # 3. Usa o operador / do pathlib para montar o caminho
                nome_arquivo = f"relatorio_{categoria.name.lower()}.pdf"
                caminho_completo = self.diretorio_relatorios / nome_arquivo
                
                # 4. Passa o caminho completo para o gerador
                # É importante converter para string, pois o PDFGenerator espera uma string
                gerador_pdf_especifico = PDFGenerator(filename=str(caminho_completo)) 
                
                try:
                    gerador_pdf_especifico.generate_pdf(gastos_da_categoria) #
                    contador_relatorios += 1
                except Exception as e:
                    print(f"Erro ao gerar {caminho_completo}: {e}")
        
        return contador_relatorios