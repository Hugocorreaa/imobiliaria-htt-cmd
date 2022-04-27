from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from alteracoes import alterar_imovel, alterar_aluguel, alterar_inquilino
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def altera():

    console = Console(width=70, height=10)
    layout = Layout()

    layout.split(
        Layout(name="header", size=3),
        Layout(name="menu", size=7)
    )

    layout["header"].size= 3
    text = Text()
    layout["header"].update(Panel(Text("IMOBILIÁRIA HTT - ALTERAR", justify="center", style="bold #FFD700")))


    while True:

        layout["menu"].update(Panel("""1- Imovel
2- Inquilino
3- Aluguel
4- Sair""", title="Seleciona uma opção:", title_align="left"))
        console.print(layout)

        
        opcao = input(">> ")
        while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
            print("Escolha uma opção válida!")
            opcao = input(">> ")
        
        opc_int = int(opcao)
    

        if opc_int == 1:
            clear()
            alterar_imovel()
        elif opc_int == 2:
            clear()
            alterar_inquilino()
        elif opc_int == 3:
            clear()
            alterar_aluguel()
        elif opc_int == 4:
            clear()
            break


