from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def menuTorneios():
    cabecalho("TORNEIOS")
    print("[1] Ver torneios")
    print("[2] Se inscrever em um torneio")
    print("[V] Voltar para o menu inicial")
    escolha = str(input("O que quer fazer: "))
    gerenciarEscolha(escolha, "menuTorneios")