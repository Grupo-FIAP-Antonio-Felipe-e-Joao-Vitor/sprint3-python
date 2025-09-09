from src.menu.cabecalho import cabecalho
from src.dados.torneios import torneios
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.torneios.dataValida import dataValida
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

    ocorreraEm = str(input("Digite a data em que o torneio ocorrerá (dia/mês): "))
    gerenciarEscolha(ocorreraEm, "criarTorneios")
    while dataValida(ocorreraEm) == False:
        ocorreraEm = str(input("Digite uma data válida (ex: 8/4): "))
        gerenciarEscolha(ocorreraEm, "criarTorneios")

    novoTorneioId = len(torneios) + 1

    novoTorneio = {"id": novoTorneioId, "times": qtdTimes, "jogadoras": qtdJogadoras, "ativo": True, "ocorreraEm": ocorreraEm, "usuariosInscritos": []}
    torneios.append(novoTorneio)

    print("Torneio criado com sucesso!")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "criarTorneios")