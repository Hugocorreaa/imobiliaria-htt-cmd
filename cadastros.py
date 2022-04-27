from rich.console import Console
from rich.table import Table
from rich.layout import Layout
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

id_imoveis = []
id_inquilinos = []
id_alugueis = []
imoveis = []
inquilinos = []
alugueis = []

def cadastro_imovel():
    id_provisorio = ""
    
    if len(id_imoveis) == 0:
        id_provisorio = 1
    else:
        id_provisorio = len(id_imoveis) + 1

    logradouro = ""
    cep = ""
    bairro = ""
    cidade = ""

    while True: 
        while logradouro == "" :
            logradouro = input("\nCadastre o logradouro: ")
        while cep == "":
            cep = input("Cadastre o CEP: ")
        while bairro == "":
            bairro = input("Cadastre o bairro: ")
        while cidade == "":
            cidade = input("Cadastre a cidade: ")


        registro = {
            'ID': id_provisorio,
            'Logradouro': logradouro,
            'CEP': cep,
            'Bairro': bairro,
            'Cidade': cidade,
        }

        console = Console(width=70, height=10)
        layout = Layout() 

        layout.split(
        Layout(name="header", size=3),
        Layout(name="menu", size=3)
        )

        clear()
        print("\nOs dados estão corretos?\n")
        tableDados = Table(title="Imóvel Cadastrado")

        for item in registro:
            tableDados.add_column(f"{item}", justify="center", style="cyan")

        tableDados.add_row(f"{id_provisorio}",f"{logradouro}",f"{cep}",f"{bairro}",f"{cidade}")

        console.print(tableDados)


        print("\n1- Sim")
        print("2- Não")

        guardar = input(">> ")
        while guardar != "1" and guardar != "2":
            print("Escolha uma opção válida!")
            guardar = input(">> ")
        
        guar_int = int(guardar)

        if guar_int == 1:
            imoveis.append(registro)
            id_imoveis.append(id_provisorio)    

            clear()
            print("\n==== Cadastrado com sucesso! ====" )
            break
        else:
            logradouro = ""
            cep = ""
            bairro = ""
            cidade = ""
    return imoveis

def cadastro_inquilino():
    id_provisorio = ""
    
    if len(id_inquilinos) == 0:
        id_provisorio = 1
    else:
        id_provisorio = len(id_inquilinos) + 1

    nome = ''
    data_nascimento = ""

    while True:
        while nome == "" :
            nome = input("\nCadastre o nome do inquilino: ")
        while data_nascimento == "":
            data_nascimento = input("Cadastre a data de nascimento: ")
        
        registro = {
            'ID': id_provisorio,
            'Nome': nome,
            'Data de Nascimento': data_nascimento
        }

        console = Console(width=70, height=10)
        layout = Layout() 

        layout.split(
        Layout(name="header", size=3),
        Layout(name="menu", size=3)
        )

        clear()
        print("\nOs dados estão corretos?\n")
        tableDados = Table(title="Inquilino Cadastrado")

        for item in registro:
            tableDados.add_column(f"{item}", justify="center", style="cyan")

        tableDados.add_row(f"{id_provisorio}",f"{nome}",f"{data_nascimento}")

        console.print(tableDados)

        print("\n1- Sim")
        print("2- Não")

        guardar = input(">> ")
        while guardar != "1" and guardar != "2":
            print("Escolha uma opção válida!")
            guardar = input(">> ")
        
        guar_int = int(guardar)

        if guar_int == 1:
            inquilinos.append(registro)
            id_inquilinos.append(id_provisorio)
            clear()
            print("\n==== Cadastrado com sucesso! ====" )
            break
        else:
            nome = ""
            data_nascimento = ""
    return inquilinos








