def nomeValido(nome):
    nomeFormatado = nome.strip()
    nomeSeparado = nomeFormatado.split()
    if len(nomeSeparado) < 2:
        return False
    else:
        return True