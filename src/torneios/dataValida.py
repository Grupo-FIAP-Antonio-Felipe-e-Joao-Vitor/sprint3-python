def dataValida(data: str) -> bool:
    """
        Verifica se uma string de data está no formato válido "dia/mês" e se os
        valores de dia e mês são possíveis.

        :param data: String representando a data no formato "dia/mês".
        :return: True se a data for válida, False caso contrário.
    """
    if not "/" in data:
        return False
    dataSeparada = data.split("/")
    if len(dataSeparada) > 2:
        return False
    try:
        dataSeparada[0] = int(dataSeparada[0])
        dataSeparada[1] = int(dataSeparada[1])
        pass
    except:
        return False
    if dataSeparada[0] < 1 or dataSeparada[0] > 31:
        return False
    if dataSeparada[1] < 1 or dataSeparada[1] > 12:
        return False
    return True