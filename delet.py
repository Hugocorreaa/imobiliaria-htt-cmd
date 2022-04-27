from cadastros import id_imoveis, imoveis, inquilinos, id_inquilinos, id_alugueis, alugueis
from consultas import consultar_alugueis, consultar_imoveis, consultar_inquilinos

import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def deleta_imovel():
    if len(imoveis) == 0:
        clear()
        print("Operação Inacessível! Não há nenhum Imóvel Cadastrado.")

    else:
        consultar_imoveis()

        print('Escolha um imóvel para alterar, pelo ID!')
        opcao = input(">> ")

        qtdImoveis = len(imoveis)
        listTemp = []

        for teste in range(qtdImoveis):
            listTemp.append(str(teste+1))
        
        while opcao not in listTemp:
            print("Escolha uma opção válida!")
            opcao = input(">> ")
        
        opc_int = int(opcao)

        imoveis.pop(opc_int-1)
        clear()
        print(id_imoveis)
        print('Deletado com sucesso!') 



def deleta_inquilino():
    print('teste')

def deleta_aluguel():
    print('teste')