from src.dados.usuarios import usuarios
from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha


def mostrarUsuarios():
    cabecalho("USUARIOS CADASTRADOS")
    print(f"{"NOME":<30}{"IDADE":<10}{"EMAIL":<30}")
    print("-"*50)
    for usuario in usuarios:
        print(f"{usuario[0]:<30}{usuario[1]:<10}{usuario[2]:<30}")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "mostrarUsuarios")