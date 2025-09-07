def qtdValida(qtd):
    try:
        qtd = int(qtd)
        if (qtd > 0):
            return True
        else:
            return False
    except ValueError:
        return False