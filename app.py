from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from cadastrar import cadastro
from consultar import consulta
from alterar import altera
from deletar import deleta
import os

#Clear console
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

console = Console(width=70, height=10)
layout = Layout()

layout.split(
    Layout(name="header", size=3),
    Layout(name="menu", size=7)
)

layout["header"].size= 3
text = Text()
layout["header"].update(Panel(Text("IMOBILIÁRIA HTT - INÍCIO", justify="center", style="bold #FFD700")))

while True:

    layout["menu"].update(Panel("""1- Cadastrar
2- Consultar
3- Alterar
4- Deletar
5- Sair""", title="Seleciona uma opção:", title_align="left"))
    console.print(layout)

    opcao = input(">> ")
    while opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        print("Escolha uma opção válida!")
        opcao = input(">> ")
    
    opc_int = int(opcao)
 
    if opc_int == 1:
        clear()
        cadastro()
    elif opc_int == 2:
        clear()
        consulta()
    elif opc_int == 3:
        clear()
        altera()
    elif opc_int == 4:
        clear()
        deleta()
    elif opc_int == 5:
        clear()
        print("\nSaindo do sistema...")
        break
