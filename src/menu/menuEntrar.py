from src.menu.cabecalho import cabecalho
from src.dados.usuarios import emailUsuarios, senhaUsuarios, usuarioLogado, usuarios
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.menu.limparTerminal import limparTerminal


def menuEntrar() -> None:
    """
        Exibe o menu de login, solicitando email e senha do usuário.
        Valida as credenciais inseridas e, caso estejam corretas, autentica o usuário
        no sistema e redireciona para o menu principal.

        :return: None
    """
    cabecalho("ENTRAR")

    print("[V] - Voltar para o menu inicial")
    email = str(input("Digite seu email: "))
    gerenciarEscolha(email, "menuEntrar")

    while email not in emailUsuarios:
        print("Email não cadastrado.")
        email = str(input("Digite seu email: "))
        gerenciarEscolha(email, "menuEntrar")

    senha = str(input("Digite sua senha: "))
    gerenciarEscolha(senha, "menuEntrar")

    indiceUsuario = emailUsuarios.index(email)
    while senha != senhaUsuarios[indiceUsuario]:
        print("Senha incorreta.")
        senha = str(input("Digite sua senha: "))
        gerenciarEscolha(senha, "menuEntrar")

    usuarioLogado.append(usuarios[indiceUsuario])
    limparTerminal()

    from src.menu.menuPrincipal import menuPrincipal
    menuPrincipal()