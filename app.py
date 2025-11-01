from pathlib import Path
from storage import StorageManager
from pdf_exporter import PDFExporter
from validator import Validator
from gui import AppGUI


def main():
    """Função principal que inicializa o sistema."""
    storage = StorageManager(Path("gastos.json"))
    pdf_exporter = PDFExporter(Path("relatorio_gastos.pdf"))
    validator = Validator()
    app = AppGUI(storage, pdf_exporter, validator)
    app.run()


if __name__ == "__main__":
    main()
