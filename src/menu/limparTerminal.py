import os

def limparTerminal() -> None:
    """
        Limpa o terminal de acordo com o sistema operacional utilizado
        (Windows ou Unix-like).

        :return: None
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")