from src.menu.cabecalho import cabecalho
from src.dados.data import usuarioLogado
from src.menu.gerenciarEscolha import gerenciarEscolha

def menuPrincipal() -> None:
    """
        Exibe o menu principal do sistema, adaptado de acordo com o tipo de conta
        do usuário (administrador ou comum). Usuários administradores podem gerenciar
        torneios e visualizar usuários cadastrados, enquanto usuários comuns podem
        acessar torneios e visualizar o próprio perfil.

        :return: None
    """

    contaAdm = True if usuarioLogado[0]["role"] == "adm" else False
    nome = usuarioLogado[0]["nome"]

    if contaAdm:
        cabecalho(f"BEM-VINDO DE VOLTA {nome.upper()}")
        print("[1] Mostrar usuários cadastrados")
        print("[2] Gerenciar torneios")
        print("[Q] Sair")
        escolha = str(input("O que quer fazer: "))
        gerenciarEscolha(escolha, "painelADM")
    else:
        cabecalho(f"BEM-VINDO DE VOLTA {nome.upper()}")
        print("[1] Torneios")
        print("[2] Ver perfil")
        print("[Q] Sair")
        escolha = str(input("O que quer fazer: "))
        gerenciarEscolha(escolha, "menuPrincipal")