# pdf_generator.py
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from typing import List
from models import Expense, Category

class PDFGenerator:
    """Classe responsável por gerar PDF a partir de uma lista de gastos usando ReportLab."""

    def __init__(self, filename: str = "relatorio.pdf"):
        self.filename = filename

    def generate_pdf(self, expenses: List[Expense]) -> None:
        """
        Gera um PDF com os gastos informados.
        - expenses: lista de objetos Expense
        """
        doc = SimpleDocTemplate(str(self.filename), pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()
        
        # Cabeçalho
        elements.append(Paragraph("Relatório de Gastos Mensais", styles['Title']))
        elements.append(Spacer(1, 12))
        
        # Monta dados da tabela
        data = [["ID", "Data", "Descrição", "Categoria", "Valor (R$)"]]
        total = 0.0
        for e in expenses:
            data.append([
                str(e.id),
                e.data.strftime("%d/%m/%Y"),
                e.descricao,
                Category(e.categoria).name,
                f"{e.valor:.2f}"
            ])
            total += e.valor
        
        # Adiciona linha de total
        data.append(["", "", "", "Total Geral", f"{total:.2f}"])
        
        # Cria tabela
        table = Table(data, colWidths=[30, 70, 200, 100, 60])
        style = TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.gray),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('ALIGN', (2,1), (2,-2), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,-1), (-1,-1), colors.lightgrey)
        ])
        table.setStyle(style)
        
        elements.append(table)
        
        # Salva PDF
        doc.build(elements)


