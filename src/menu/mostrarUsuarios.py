from src.dados.usuarios import usuarios
from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def mostrarUsuarios():
    cabecalho("USUARIOS CADASTRADOS")
    print(f"{"NOME":<20}{"IDADE":<6}{"EMAIL":<20}{"TIPO DE USUARIO":<20}{"INSCRIÇÕES":<20}")
    print("-"*80)
    for usuario in usuarios:
        if usuario["inscrito"] != None:
            print(f"{usuario["nome"]:<20}{usuario["idade"]:<6}{usuario["email"]:20}{usuario["role"].upper():<20}{f"Inscrito no torneio de ID {usuario["inscrito"]}":<20}")
        else:
            print(f"{usuario["nome"]:<20}{usuario["idade"]:<6}{usuario["email"]:20}{usuario["role"].upper():<20}{"Não está inscrito em torneios":<20}")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "mostrarUsuarios")