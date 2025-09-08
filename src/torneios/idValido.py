from src.dados.torneios import torneios


def idValido(id):

    try:
        id = int(id)
        for torneio in torneios:
            if torneio["id"] == id:
                return True
        return False
    except:
        return False