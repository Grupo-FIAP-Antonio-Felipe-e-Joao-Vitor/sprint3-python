from src.dados.data import lerInfos


def idValido(id: str | int) -> bool:
    """
        Verifica se o ID fornecido corresponde a algum torneio existente na lista
        de torneios.

        :param id: ID do torneio a ser verificado.
        :return: True se o ID for válido, False caso contrário.
    """

    torneios = lerInfos("src/dados/torneios.json")

    try:
        id = int(id)
        for torneio in torneios:
            if torneio["id"] == id:
                return True
        return False
    except:
        return False