from src.dados.usuarios import usuarios
from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def mostrarUsuarios():
    cabecalho("USUARIOS CADASTRADOS")
    print(f"{"NOME":<20}{"IDADE":<6}{"EMAIL":<20}{"TIPO DE USUARIO":<20}{"INSCRIÇÕES":<20}")
    print("-"*80)
    for usuario in usuarios:
        if usuario[5] != None:
            print(f"{usuario[0]:<20}{usuario[1]:<6}{usuario[2]:20}{usuario[4].upper():<20}{f"Inscrito no torneio de ID {usuario[5]}":<20}")
        else:
            print(f"{usuario[0]:<20}{usuario[1]:<6}{usuario[2]:20}{usuario[4].upper():<20}{"Não está inscrito em torneios":<20}")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "mostrarUsuarios")