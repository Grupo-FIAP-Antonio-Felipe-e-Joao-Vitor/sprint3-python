import os

def limparTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")