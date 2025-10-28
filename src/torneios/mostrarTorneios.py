from src.menu.cabecalho import cabecalho
from src.dados.data import lerInfos
from src.menu.gerenciarEscolha import gerenciarEscolha


def mostrarTorneios(painelADM: bool = False) -> None:
    """
        Exibe uma lista de todos os torneios cadastrados, mostrando informações
        como ID, número de times, quantidade de jogadoras por time, status, data
        do torneio e inscritos. Permite retornar ao menu anterior, diferenciado
        entre painel de administrador e usuário comum.

        :param painelADM: Define se a visualização é no painel do administrador.
        :return: None
    """

    cabecalho("TORNEIOS")

    torneios = lerInfos("src/dados/torneios.json")

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