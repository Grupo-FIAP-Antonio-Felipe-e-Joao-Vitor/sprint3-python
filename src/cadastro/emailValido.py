def emailValido(email: str) -> bool:
    """
        Verifica se um email possui um formato válido, contendo '@', ponto no
        domínio e final '.com'.

        :param email: Email a ser validado.
        :return: True se o email for válido, False caso contrário.
    """

    emailFormatado = email.strip()
    if not "@" in emailFormatado:
        return False
    emailSeparado = emailFormatado.split('@')
    if emailSeparado[0] == "" or emailSeparado[1] == "":
        return False
    if not "." in emailSeparado[1]:
        return False
    dominioEmail = emailSeparado[1].split(".")
    if dominioEmail[0] == "" or dominioEmail[1] == "":
        return False
    if not "com" in dominioEmail[1]:
        return False
    return True