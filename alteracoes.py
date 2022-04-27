from cadastros import id_imoveis, imoveis, inquilinos, id_inquilinos, id_alugueis, alugueis
from consultas import consultar_alugueis, consultar_imoveis, consultar_inquilinos
from rich.console import Console
from rich.layout import Layout
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

console = Console(width=70, height=10)
layout = Layout()


layout.split(
Layout(name="header", size=3),
Layout(name="menu", size=3)
)


def alterar_imovel():
    if len(id_imoveis) == 0:
        clear()
        print("Operação Inacessível! Não há nenhum Imóvel Cadastrado.")
    else:
        consultar_imoveis()

        print('Escolha um imóvel para alterar, pelo ID!')
        opcao = input(">> ")

        qtdImoveis = len(id_imoveis)
        listTemp = []

        for teste in range(qtdImoveis):
            listTemp.append(str(teste+1))
        
        while opcao not in listTemp:
            print("Escolha uma opção válida!")
            opcao = input(">> ")
        
        opc_int = int(opcao)

        new_logra = ""
        new_cep = ""
        new_bairro = ""
        new_cidade = ""

        while new_logra == "" :
             new_logra = input("Cadastre o novo logradouro: ")
        while new_cep == "":
            new_cep = input("Cadastre o novo CEP: ")
        while new_bairro == "":
            new_bairro = input("Cadastre o novo bairro: ")
        while new_cidade == "":
            new_cidade = input("Cadastre a nova cidade: ")

        imoveis[opc_int-1]['Logradouro'] = new_logra
        imoveis[opc_int-1]['CEP'] = new_cep
        imoveis[opc_int-1]['Bairro'] = new_bairro
        imoveis[opc_int-1]['Cidade'] = new_cidade

        clear()
        print('Alterado com sucesso!')        

def alterar_inquilino():
    if len(id_inquilinos) == 0:
        clear()
        print("Operação Inacessível! Não há nenhum inquilino cadastrado.")
    else:
        consultar_inquilinos()

        print('Escolha um inquilino para alterar, pelo ID!')
        opcao = input(">> ")

        qtdInquilinos = len(id_inquilinos)
        listTemp = []

        for teste in range(qtdInquilinos):
            listTemp.append(str(teste+1))
        
        while opcao not in listTemp:
            print("Escolha uma opção válida!")
            opcao = input(">> ")
        
        opc_int = int(opcao)

        new_inquilino = ""
        new_data = ""

        while new_inquilino == "":
            new_inquilino = input("Cadastre o novo nome do inquilino: ")
        while new_data == "":
            new_data = input("Cadastre a nova data de nascimento: ")

        inquilinos[opc_int-1]['Nome'] = new_inquilino
        inquilinos[opc_int-1]['Data de Nascimento'] = new_data

        clear()
        print('Alterado com sucesso!')     

def alterar_aluguel():
    if len(id_alugueis) == 0:
        clear()
        print("Operação Inacessível! Não há nenhum aluguel cadastrado.")
    else:
        consultar_alugueis()
        print('Escolha um aluguel para alterar, pelo ID!')
        opcao = input(">> ")

        qtdAlugueis = len(id_alugueis)
        listTemp = []

        for teste in range(qtdAlugueis):
            listTemp.append(str(teste+1))
        
        while opcao not in listTemp:
            print("Escolha uma opção válida!")
            opcao = input(">> ")
        
        opc_int = int(opcao)

        consultar_imoveis()
        consultar_inquilinos()

        qtdImoveis = len(id_imoveis)
        imoveisListTemp = []

        for i in range(qtdImoveis):
            imoveisListTemp.append(str(i+1))

        qtdInquilinos = len(id_inquilinos)
        inquilinosListTemp = []

        for i in range(qtdInquilinos):
            inquilinosListTemp.append(str(i+1))
        
        new_imovel = input("\nCadastre o Id do Imóvel: ")
        while new_imovel == "" or new_imovel not in imoveisListTemp:
            print("Imóvel não encontrado!")
            new_imovel = input("\nCadastre o Id do Imóvel: ")
            
        new_inquilino = input("Cadastre o Id do Inquilino: ")
        while new_inquilino == "" or new_inquilino not in inquilinosListTemp:
            print("Inquilino não encontrado!")
            new_inquilino = input("Cadastre o Id do Inquilino: ")

        alugueis[opc_int-1]['Id Imóvel'] = new_imovel
        alugueis[opc_int-1]['Id Inquilino'] = new_inquilino

        clear()
        print('Alterado com sucesso!')   