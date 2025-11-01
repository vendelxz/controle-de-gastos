import tkinter as tk
from tkinter import messagebox
from models import Expense, Category
from storage import StorageManager
from pdf_exporter import PDFExporter
from validator import Validator


class AppGUI:
    """Interface gráfica principal do sistema."""

    def __init__(self, storage: StorageManager, pdf_exporter: PDFExporter, validator: Validator):
        self.root = tk.Tk()
        self.storage = storage
        self.pdf_exporter = pdf_exporter
        self.validator = validator

        self.root.title("Controle de Gastos Mensais")
        self.root.geometry("500x500")

        self._build_interface()

    def _build_interface(self):
        """Cria e organiza os componentes da interface."""
        pass

    def on_add_click(self):
        """Adiciona um novo gasto após validação."""
        pass

    def refresh_list(self):
        """Atualiza a listagem de gastos exibida."""
        pass

    def on_export_click(self):
        """Gera o PDF com os gastos."""
        pass

    def show_message(self, msg: str, tipo="info"):
        """Mostra mensagens para o usuário."""
        if tipo == "erro":
            messagebox.showerror("Erro", msg)
        else:
            messagebox.showinfo("Informação", msg)

    def run(self):
        """Executa o loop principal da aplicação."""
        self.root.mainloop()
