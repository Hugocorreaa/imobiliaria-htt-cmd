
from consultas import consultar_imoveis, consultar_inquilinos, consultar_alugueis
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def consulta():

    console = Console(width=70, height=11)
    layout = Layout()   

    layout.split(
    Layout(name="header", size=3),
    Layout(name="menu", size=8)
    )

    while True:
        layout["header"].update(Panel(Text("IMOBILIÁRIA HTT - CONSULTAR", justify="center", style="bold #FFD700")))
        layout["menu"].update(Panel("""1 - Consultar Imóveis
2 - Consultar Inquilinos
3 - Consultar Alugueis
4 - Voltar""", title="Seleciona uma opção:", title_align="left"))
        console.print(layout)

        opcao = input(">> ")
        while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
            print("Escolha uma opção válida!")
            opcao = input(">> ")
        
        opc_int = int(opcao)

        if opc_int == 1:
            clear()
            consultar_imoveis()
            break
        elif opc_int == 2:
            clear()
            consultar_inquilinos()
            break
        elif opc_int == 3:
            clear()
            consultar_alugueis()
            break
        elif opc_int == 4:
            clear()
            break
