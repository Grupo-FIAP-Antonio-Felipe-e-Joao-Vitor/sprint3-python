from src.menu.cabecalho import cabecalho
from src.menu.menuEntrar import usuarioLogado
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.dados.usuarios import usuarios

def menuPrincipal():
    contaAdm = usuarios[0]
    nome = usuarioLogado[0][0]

    conta = usuarioLogado[0]
    if conta == contaAdm:
        cabecalho(f"BEM-VINDO DE VOLTA {nome.upper()}")
        print("[1] Mostrar usuários cadastrados")
        print("[2] Monitorar torneios")
        print("[Q] Sair")
        escolha = str(input("O que quer fazer: "))
        gerenciarEscolha(escolha, "painelADM")
    else:
        cabecalho(f"BEM-VINDO DE VOLTA {nome.upper()}")
        print("[1] Sobre torneios")
        print("[2] Se inscrever em torneios")
        print("[Q] Sair")
        escolha = str(input("O que quer fazer: "))
        gerenciarEscolha(escolha, "menuPrincipal")