from src.dados.usuarios import usuarioLogado
from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def verPerfil():
    cabecalho("PERFIL")

    nome = usuarioLogado[0]["nome"]
    idade = usuarioLogado[0]["idade"]
    email = usuarioLogado[0]["email"]
    inscrito = usuarioLogado[0]["inscrito"]
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")
    if inscrito != None:
        print(f"Participando no torneio de ID {inscrito}")
    else:
        print("Não está participando de nenhum torneio")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "verPerfil")