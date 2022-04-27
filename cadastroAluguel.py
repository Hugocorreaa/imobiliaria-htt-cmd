from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from cadastros import id_imoveis, id_inquilinos, id_alugueis, alugueis
from consultas import consultar_imoveis, consultar_inquilinos
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def cadastro_aluguel():
    if len(id_imoveis) == 0 or len(id_inquilinos) == 0:
        clear()
        print("Operação Inacessível! Não há nenhum Imóvel ou Iniquilino Cadastrado.")
    else:

        consultar_imoveis()
        consultar_inquilinos()
        
        id_provisorio = ""
        
        if len(id_inquilinos) == 0:
            id_provisorio = 1
        else:
            id_provisorio = len(id_alugueis) + 1

        id_imovel = ""
        id_inquilino = ""
        
        qtdImoveis = len(id_imoveis)
        imoveisListTemp = []

        for i in range(qtdImoveis):
            imoveisListTemp.append(str(i+1))

        qtdInquilinos = len(id_inquilinos)
        inquilinosListTemp = []

        for i in range(qtdInquilinos):
            inquilinosListTemp.append(str(i+1))
        
        while True:
            id_imovel = input("\nCadastre o Id do Imóvel: ")
            while id_imovel == "" or id_imovel not in imoveisListTemp:
                print("Imóvel não encontrado!")
                id_imovel = input("\nCadastre o Id do Imóvel: ")
                
            id_inquilino = input("Cadastre o Id do Inquilino: ")
            while id_inquilino == "" or id_inquilino not in inquilinosListTemp:
                print("Inquilino não encontrado!")
                id_inquilino = input("Cadastre o Id do Inquilino: ")

            registro = {
                'ID': id_provisorio,
                'Id Imóvel': id_imovel,
                'Id Inquilino': id_inquilino
            }

            console = Console(width=70, height=10)
            layout = Layout() 

            layout.split(
            Layout(name="header", size=3),
            Layout(name="menu", size=3)
            )

            print("\nOs dados estão corretos?\n")
            tableDados = Table(title="Aluguel Cadastrado")

            for item in registro:
                tableDados.add_column(f"{item}", justify="center", style="cyan")

            tableDados.add_row(f"{id_provisorio}",f"{id_imovel}",f"{id_inquilino}")

            console.print(tableDados)


            print("\n1- Sim")
            print("2- Não")

            guardar = input(">> ")
            while guardar != "1" and guardar != "2":
                print("Escolha uma opção válida!")
                guardar = input(">> ")
            
            guar_int = int(guardar)

            if guar_int == 1:
                alugueis.append(registro)
                id_alugueis.append(id_provisorio)
                clear()
                print("\n==== Cadastrado com sucesso! ====" )
                break
            else:
                id_imovel = ""
                id_inquilino = ""
        return alugueis