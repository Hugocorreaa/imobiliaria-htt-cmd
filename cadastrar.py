from cadastros import cadastro_imovel, cadastro_inquilino
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from cadastroAluguel import cadastro_aluguel
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def cadastro():

    console = Console(width=70, height=9)
    layout = Layout()   

    layout.split(
    Layout(name="header", size=3),
    Layout(name="menu", size=6)
    )

    layout["header"].update(Panel(Text("IMOBILIÁRIA HTT - CADASTRAR", justify="center", style="bold #FFD700")))
    layout["menu"].update(Panel("""1 - Cadastrar Imóvel
2 - Cadastrar Inquilino
3 - Cadastrar Aluguel
4 - Voltar""", title="Seleciona uma opção:", title_align="left"))
    console.print(layout)

    opcao = input(">> ")
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
        print("Escolha uma opção válida!")
        opcao = input(">> ")
    
    opc_int = int(opcao)

    if opc_int == 1:
        cadastro_imovel()
    elif opc_int == 2: 
        cadastro_inquilino()
    elif opc_int == 3:
        cadastro_aluguel()
    else:
        clear()

