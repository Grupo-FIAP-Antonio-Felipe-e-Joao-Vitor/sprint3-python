def cabecalho(mensagem: str) -> None:
    """
        Exibe um cabeçalho formatado com a mensagem centralizada entre linhas de traços.

        :param mensagem: Texto que será exibido no centro do cabeçalho.
        :return: None
    """
    print(f"{20 * '-'} {mensagem} {20 * '-'}")
