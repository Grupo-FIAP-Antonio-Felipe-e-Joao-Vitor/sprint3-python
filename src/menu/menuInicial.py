from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha

def menuInicial() -> None:
    """
        Exibe o menu inicial do sistema, permitindo que o usuário escolha entre
        cadastrar-se, entrar ou sair do sistema.

        :return: None
    """
    cabecalho("CADASTRE-SE OU ENTRE")
    print("[1] - Cadastrar")
    print("[2] - Entrar")
    print("[Q] - Sair do sistema")
    escolha = str(input("O que quer fazer: "))
    gerenciarEscolha(escolha, "menuInicial")