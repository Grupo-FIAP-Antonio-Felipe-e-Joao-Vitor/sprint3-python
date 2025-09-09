from src.menu.cabecalho import cabecalho
from src.dados.torneios import torneios
from src.menu.gerenciarEscolha import gerenciarEscolha


def mostrarTorneios(painelADM = False):
    cabecalho("TORNEIOS")

    if len(torneios) > 0:
        print(f"{"ID":<10} {"TIMES":<10} {"JOGADORAS POR TIME":<25} {"STATUS":<15} {"DATA DO TORNEIO":<20} {"INSCRITOS":<15} ")
        print("-" * 80)
        for torneio in torneios:
            status = "Em andamento" if torneio["ativo"] == 1 else "Finalizado"
            inscritos = torneio["usuariosInscritos"] if len(torneio["usuariosInscritos"]) > 0 else "Nenhum usuario inscrito"
            print(f"{torneio["id"]:<10} {torneio["times"]:<10} {torneio["jogadoras"]:<25} {status:<15} {torneio['ocorreraEm']:<15} {inscritos}")
    else:
        print("Nenhum torneio foi encontrado.")

    input("Pressione <ENTER> para voltar")
    if painelADM:
        gerenciarEscolha("v", "mostrarTorneiosADM")
    else:
        gerenciarEscolha("v", "mostrarTorneiosUSER")