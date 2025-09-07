from src.menu.cabecalho import cabecalho
from src.dados.usuarios import usuarioLogado
from src.menu.gerenciarEscolha import gerenciarEscolha

def menuPrincipal():
    contaAdm = True if usuarioLogado[0][4] == "adm" else False
    nome = usuarioLogado[0][0]

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