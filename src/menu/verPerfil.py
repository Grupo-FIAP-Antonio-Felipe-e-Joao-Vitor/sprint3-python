from src.dados.usuarios import usuarioLogado
from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def verPerfil():
    cabecalho("PERFIL")

    nome = usuarioLogado[0][0]
    idade = usuarioLogado[0][1]
    email = usuarioLogado[0][2]
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "verPerfil")