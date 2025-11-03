# Controle de Gastos Mensais

Sistema simples de gerenciamento de gastos mensais com interface gráfica, armazenamento em JSON e geração de relatórios em PDF.

---

## Funcionalidades

- **Adicionar gasto:**  
  Permite adicionar gastos com valor, descrição e categoria. IDs são atribuídos automaticamente.  

- **Deletar gasto por ID:**  
  Permite remover um gasto específico informando o ID.  

- **Deletar todos os gastos:**  
  Remove todos os registros do sistema de forma rápida.  

- **Gerar relatório em PDF:**  
  Cria um PDF listando todos os gastos e o somatório total, organizado por ID, descrição, valor e categoria.  

- **Validação de entradas:**  
  Garante que valores, descrições e categorias sejam válidos antes de salvar.  

- **Visualização em tempo real:**  
  Lista todos os gastos registrados em uma Listbox na interface gráfica.  

---

## Tecnologias e Bibliotecas

- **Python 3.10+**  
- **Tkinter** – Interface gráfica simples e responsiva  
- **ReportLab** – Geração de PDFs  
- **Pathlib** – Manipulação de caminhos de arquivos  
- **JSON** – Armazenamento persistente dos dados  
- **Dataclasses** – Estrutura de dados para gastos (Expense)  
- **Validator** – Validação customizada de entradas  

---
## Como usar

1. **Instalar dependências:**  

```bash
pip install -r requirements.txt 
```
2. **Rodar o programa**
```bash
python app.py 
```
---
## Criar um executável (.exe) - OPCIONAL
1. **Instale as depedências:**
```bash
pip install pyinstaller
```
2. **Rode o seguinte código:**
```bash
pyinstaller --onefile --noconsole app.py
```
- O executável será gerado na pasta dist.
- Os relátórios e os gastos do JSON serão gerados nela também.
---
## Requisitos / Considerações
 - O JSON será criado automaticamente se não existir.
 - O PDF é gerado como **relatorio.pdf** no diretório do projeto.
 - Categorias devem ser informadas pelo ID mostrado na interface.
 - IDs dos gastos são únicos e atribuídos automaticamente.
 - O PDF inclui o somatório total dos gastos.
 ---
 ## Autor
 **José Wendel**

