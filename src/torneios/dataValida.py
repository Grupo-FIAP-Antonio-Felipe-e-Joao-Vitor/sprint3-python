def dataValida(data):
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