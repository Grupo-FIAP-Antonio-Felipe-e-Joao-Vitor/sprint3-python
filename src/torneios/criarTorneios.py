from src.menu.cabecalho import cabecalho
from src.dados.torneios import torneios
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.torneios.qtdValida import qtdValida


def criarTorneios():
    cabecalho("CRIAR TORNEIO")

    print("[V] - Voltar para o menu inicial")

    qtdTimes = str(input("Digite a quantidade de times que deseja: "))
    gerenciarEscolha(qtdTimes, "criarTorneios")
    while qtdValida(qtdTimes) == False:
        qtdTimes = str(input("Digite uma quantidade de times válida (ex: 8): "))
        gerenciarEscolha(qtdTimes, "criarTorneios")

    qtdJogadoras = str(input("Digite a quantidade de jogadores que deseja por time: "))
    gerenciarEscolha(qtdJogadoras, "criarTorneios")
    while qtdValida(qtdJogadoras) == False:
        qtdJogadoras = str(input("Digite uma quantidade de jogadores válida (ex: 5): "))
        gerenciarEscolha(qtdJogadoras, "criarTorneios")

    novoTorneioId = len(torneios) + 1

    novoTorneio = [novoTorneioId, qtdTimes, qtdJogadoras, True]
    torneios.append(novoTorneio)

    print("Torneio criado com sucesso!")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "criarTorneios")