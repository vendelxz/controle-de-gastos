# gui.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from storage import StorageManager
from validator import Validator
from pdf_exporter import PDFGenerator
from models import Expense, Category


class AppGUI:
    """Interface gráfica principal do sistema de gastos."""

    def __init__(self, storage: StorageManager, pdf_generator: PDFGenerator, validator: Validator):
        self.storage = storage
        self.pdf_generator = pdf_generator
        self.validator = validator

        self.root = tk.Tk()
        self.root.title("Controle de Gastos Mensais")

        # --- Campos da GUI ---
        # Valor
        tk.Label(self.root, text="Valor:").grid(row=0, column=0, sticky="w")
        self.valor_entry = tk.Entry(self.root)
        self.valor_entry.grid(row=0, column=1)

        # Descrição
        tk.Label(self.root, text="Descrição:").grid(row=1, column=0, sticky="w")
        self.descricao_entry = tk.Entry(self.root, width=40)
        self.descricao_entry.grid(row=1, column=1)

        # Categoria
        tk.Label(self.root, text="Categoria (ID):").grid(row=2, column=0, sticky="w")
        categorias_str = "\n".join([f"{c.value} - {c.name}" for c in Category])
        tk.Label(self.root, text=categorias_str).grid(row=2, column=1, sticky="w")
        self.categoria_entry = tk.Entry(self.root)
        self.categoria_entry.grid(row=3, column=1)

        # ID para deletar (campo separado)
        tk.Label(self.root, text="ID para deletar:").grid(row=4, column=0, sticky="w")
        self.id_delete_entry = tk.Entry(self.root)
        self.id_delete_entry.grid(row=4, column=1)

        # Botões
        tk.Button(self.root, text="Adicionar Gasto", command=self.add_expense).grid(row=5, column=0, pady=5)
        tk.Button(self.root, text="Deletar por ID", command=self.delete_by_id).grid(row=5, column=1, pady=5)
        tk.Button(self.root, text="Deletar Todos", command=self.delete_all).grid(row=6, column=0, pady=5)
        tk.Button(self.root, text="Gerar PDF", command=self.generate_pdf).grid(row=6, column=1, pady=5)

        # Lista de gastos
        self.gastos_listbox = tk.Listbox(self.root, width=80)
        self.gastos_listbox.grid(row=7, column=0, columnspan=2, pady=10)

        self.refresh_listbox()

    # --- Funções principais ---
    def refresh_listbox(self):
        """Atualiza a Listbox com os gastos atuais."""
        self.gastos_listbox.delete(0, tk.END)
        for e in self.storage.load_all():
            categoria_nome = Category(e.categoria).name if e.categoria in [c.value for c in Category] else "Desconhecida"
            self.gastos_listbox.insert(
                tk.END,
                f"ID={e.id} | {e.descricao} | R$ {e.valor:.2f} | {categoria_nome}"
            )

    def add_expense(self):
        """Adiciona um novo gasto."""
        try:
            valor_input = self.valor_entry.get()
            descricao_input = self.descricao_entry.get()
            categoria_input = self.categoria_entry.get()

            # Validação
            valor = self.validator.validate_valor(valor_input)
            descricao = self.validator.validate_descricao(descricao_input)
            categoria = self.validator.validate_categoria(categoria_input)

            # Cria Expense com id=None (StorageManager atribui ID)
            expense = Expense(
                id=None,
                valor=valor,
                descricao=descricao,
                categoria=categoria,
                data=datetime.now()
            )

            self.storage.append(expense)
            self.refresh_listbox()
            messagebox.showinfo("Sucesso", f"Gasto adicionado com ID {expense.id}!")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def delete_by_id(self):
        """Deleta o gasto pelo ID informado pelo usuário."""
        id_str = self.id_delete_entry.get()
        try:
            if not id_str.strip():
                raise ValueError("Informe um ID para deletar.")
            id_int = int(id_str)
            removed = self.storage.delete_by_id(id_int)
            if removed:
                messagebox.showinfo("Sucesso", f"Gasto ID {id_int} removido.")
            else:
                messagebox.showwarning("Aviso", f"ID {id_int} não encontrado.")
            self.refresh_listbox()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def delete_all(self):
        """Deleta todos os gastos."""
        count = self.storage.delete_all()
        messagebox.showinfo("Sucesso", f"{count} registros removidos.")
        self.refresh_listbox()

    def generate_pdf(self):
        """Gera o PDF do relatório de gastos."""
        gastos = self.storage.load_all()
        self.pdf_generator.generate_pdf(gastos)
        messagebox.showinfo("PDF Gerado", "Relatório gerado com sucesso!")

    def run(self):
        """Inicia o loop principal da GUI."""
        self.root.mainloop()
