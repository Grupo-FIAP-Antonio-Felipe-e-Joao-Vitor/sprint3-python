def nomeValido(nome: str) -> bool:
    """
        Verifica se o nome fornecido possui pelo menos duas palavras
        (nome e sobrenome).

        :param nome: Nome a ser validado.
        :return: True se o nome for válido (pelo menos duas palavras), False caso contrário.
    """
    nomeFormatado = nome.strip()
    nomeSeparado = nomeFormatado.split()
    if len(nomeSeparado) < 2:
        return False
    else:
        return True