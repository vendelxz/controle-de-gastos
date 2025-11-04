from pathlib import Path
from storage import StorageManager
from pdf_exporter import PDFGenerator
from validator import Validator
from gui import AppGUI
# 1. Importe a sua nova classe
from report_manager import GeradorRelatoriosCategoria 


def main():
    """Função principal que inicializa o sistema."""
    storage = StorageManager(Path("gastos.json"))
    pdf_exporter = PDFGenerator(Path("relatorio.pdf"))
    validator = Validator()
    
    # 2. Crie a instância da sua nova classe
    report_manager = GeradorRelatoriosCategoria(storage)

    # 3. Passe a nova instância para a GUI
    app = AppGUI(storage, pdf_exporter, validator, report_manager)
    app.run()


if __name__ == "__main__":
    main()