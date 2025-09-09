def qtdValida(qtd: str | int) -> bool:
    """
        Verifica se a quantidade fornecida é um número inteiro positivo.

        :param qtd: Valor a ser verificado.
        :return: True se a quantidade for válida (inteiro positivo), False caso contrário.
    """

    try:
        qtd = int(qtd)
        if (qtd > 0):
            return True
        else:
            return False
    except ValueError:
        return False