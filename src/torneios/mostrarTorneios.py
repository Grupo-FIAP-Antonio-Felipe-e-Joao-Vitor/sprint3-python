from src.menu.cabecalho import cabecalho
from src.dados.torneios import torneios
from src.menu.gerenciarEscolha import gerenciarEscolha


def mostrarTorneios():
    cabecalho("TORNEIOS")

    print(f"{"ID":<10} {"TIMES":<10} {"JOGADORAS POR TIME":<25} {"STATUS":<10}")
    print("-" * 50)
    for torneio in torneios:
        status = "Em andamento" if torneio[3] == 1 else "Finalizado"
        print(f"{torneio[0]:<10} {torneio[1]:<10} {torneio[2]:<25} {status:<10}")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "mostrarTorneios")