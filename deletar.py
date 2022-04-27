from delet import deleta_aluguel, deleta_imovel, deleta_inquilino, deleta_aluguel
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def deleta():
    console = Console(width=70, height=9)
    layout = Layout()   

    layout.split(
    Layout(name="header", size=3),
    Layout(name="menu", size=6)
    )

    layout["header"].update(Panel(Text("IMOBILIÁRIA HTT - DELETAR", justify="center", style="bold #FFD700")))
    layout["menu"].update(Panel("""1 - Deletar Imovel
2 - Deletar Inquilino
3 - Deletar Aluguel
4 - Voltar""", title="Seleciona uma opção:", title_align="left"))
    console.print(layout)

    opcao = input(">> ")
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
        print("Escolha uma opção válida!")
        opcao = input(">> ")

    opc_int = int(opcao)

    if opc_int == 1:
        deleta_imovel()
    elif opc_int == 2: 
        deleta_inquilino()
    elif opc_int == 3:
        deleta_aluguel()
    else:
        clear()