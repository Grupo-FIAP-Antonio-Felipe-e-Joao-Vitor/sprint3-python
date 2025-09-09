def idadeValida(idade: str | int) -> bool:
    """
        Verifica se a idade fornecida é um número inteiro positivo.

        :param idade: Valor da idade a ser verificado.
        :return: True se a idade for válida (inteiro positivo), False caso contrário.
    """
    try:
        idade = int(idade)
        if idade > 0:
            return True
        else:
            return False
    except ValueError:
        return False