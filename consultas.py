from cadastros import imoveis, inquilinos, alugueis
from rich.console import Console
from rich.table import Table
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

tableImoveis = Table(title="Imóveis Cadastrado")
tableInquilinos = Table(title="Inquilinos Cadastrados")
tableAlugueis = Table(title="Alugueis Cadastrados")

tableImoveis.add_column(f"ID", justify="center", style="cyan")
tableImoveis.add_column(f"Logradouro", justify="center", style="cyan")
tableImoveis.add_column(f"CEP", justify="center", style="cyan")
tableImoveis.add_column(f"Bairro", justify="center", style="cyan")
tableImoveis.add_column(f"Cidade", justify="center", style="cyan")

tableInquilinos.add_column(f"ID", justify="center", style="cyan")
tableInquilinos.add_column(f"Nome", justify="center", style="cyan")
tableInquilinos.add_column(f"Data de Nascimento", justify="center", style="cyan")

tableAlugueis.add_column(f"ID", justify="center", style="cyan")
tableAlugueis.add_column(f"Imovel", justify="center", style="cyan")
tableAlugueis.add_column(f"Inquilino", justify="center", style="cyan")

console = Console(width=70, height=10)

def consultar_imoveis():
    if len(imoveis) == 0:
        clear()
        print('Nenhum imóvel cadastrado.')
    else:

        tableImoveisNew = Table(title="Imóveis Cadastrado")

        tableImoveisNew.add_column(f"ID", justify="center", style="cyan")
        tableImoveisNew.add_column(f"Logradouro", justify="center", style="cyan")
        tableImoveisNew.add_column(f"CEP", justify="center", style="cyan")
        tableImoveisNew.add_column(f"Bairro", justify="center", style="cyan")
        tableImoveisNew.add_column(f"Cidade", justify="center", style="cyan") 

        for item in imoveis:
            tableImoveisNew.add_row(f"{item['ID']}",f"{item['Logradouro']}",f"{item['CEP']}",f"{item['Bairro']}",f"{item['Cidade']}")

        console.print(tableImoveisNew)

def consultar_inquilinos():
    if len(inquilinos) == 0:
        clear()
        print('Nenhum inquilino cadastrado.')
    else:
        
        tableInquilinosNew = Table(title="Inquilinos Cadastrados")

        tableInquilinosNew.add_column(f"ID", justify="center", style="cyan")
        tableInquilinosNew.add_column(f"Nome", justify="center", style="cyan")
        tableInquilinosNew.add_column(f"Data de Nascimento", justify="center", style="cyan")

        for item in inquilinos:
            tableInquilinosNew.add_row(f"{item['ID']}",f"{item['Nome']}", f"{item['Data de Nascimento']}")

        console.print(tableInquilinosNew)

def consultar_alugueis():
    if len(alugueis) == 0:
        clear()
        print('Nenhum aluguel cadastrado.')
    else:
        tableAlugueisNew = Table(title="Alugueis Cadastrado")

        tableAlugueisNew.add_column(f"ID", justify="center", style="cyan")
        tableAlugueisNew.add_column(f"Id Imóvel", justify="center", style="cyan")
        tableAlugueisNew.add_column(f"Id Inquilino", justify="center", style="cyan")

        for item in alugueis:
            tableAlugueisNew.add_row(f"{item['ID']}", f"{item['Id Imóvel']}", f"{item['Id Inquilino']}")

        console.print(tableAlugueisNew)