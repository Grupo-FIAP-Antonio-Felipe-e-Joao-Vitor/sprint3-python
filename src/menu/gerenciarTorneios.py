from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def gerenciarTorneios() -> None:
    """
        Exibe o menu de gerenciamento de torneios e direciona a escolha do usuário
        para a ação correspondente (listar, criar, encerrar ou voltar ao menu inicial).

        :return: None
    """

    cabecalho("TORNEIOS")

    print("[1] - Torneios")
    print("[2] - Criar torneio")
    print("[3] - Encerrar torneio")
    print("[V] - Voltar para o menu inicial")
    escolha = str(input("O que quer fazer: "))
    gerenciarEscolha(escolha, "gerenciarTorneios")