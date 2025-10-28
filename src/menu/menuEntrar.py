from src.menu.cabecalho import cabecalho
from src.dados.data import lerInfos, usuarioLogado
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

    usuarios = lerInfos("src/dados/usuarios.json")

    print("[V] - Voltar para o menu inicial")
    email = str(input("Digite seu email: "))
    gerenciarEscolha(email, "menuEntrar")

    emailUsado = next((u for u in usuarios if u["email"] == email), None)

    while not emailUsado:
        print("Email não cadastrado.")
        email = str(input("Digite seu email: "))
        emailUsado = next((u for u in usuarios if u["email"] == email), None)
        gerenciarEscolha(email, "menuEntrar")

    usuario = next((u for u in usuarios if u["email"] == email), None)

    senha = str(input("Digite sua senha: "))
    gerenciarEscolha(senha, "menuEntrar")

    while senha != usuario["senha"]:
        print("Senha incorreta.")
        senha = str(input("Digite sua senha: "))
        gerenciarEscolha(senha, "menuEntrar")

    usuarioLogado.append(usuario)
    limparTerminal()

    from src.menu.menuPrincipal import menuPrincipal
    menuPrincipal()