from src.menu.cabecalho import cabecalho
from src.menu.gerenciarEscolha import gerenciarEscolha
from src.cadastro.nomeValido import nomeValido
from src.cadastro.emailValido import emailValido
from src.cadastro.senhaValida import senhaValida
from src.cadastro.idadeValida import idadeValida
from src.dados.data import lerInfos, escreverInfos

def menuCadastro() -> None:
    """
        Exibe o menu de cadastro de usuários, coleta as informações necessárias
        (nome, idade, email e senha), valida os dados inseridos e registra um novo
        usuário no sistema caso todas as verificações sejam concluídas com sucesso.

        :return: None
    """
    cabecalho("CADASTRE-SE")

    idade = ""

    usuarios = lerInfos("src/dados/usuarios.json")

    print("[V] - Voltar para o menu inicial")

    nome = str(input("Digite seu nome completo: "))
    gerenciarEscolha(nome, "menuCadastro")
    while (nomeValido(nome) == False):
        nome = str(input("Digite seu nome completo (nome e sobrenome): "))
        gerenciarEscolha(nome, "menuCadastro")


    while (idadeValida(idade) == False):
        idade = str(input("Insira sua idade: "))
        gerenciarEscolha(idade, "menuCadastro")

    email = str(input("Digite seu email: "))
    gerenciarEscolha(email, "menuCadastro")
    while (emailValido(email) == False):
        email = str(input("Digite um email válido (ex: email@email.com): "))
        gerenciarEscolha(email, "menuCadastro")

    emailUsado = next((u for u in usuarios if u["email"] == email), None)

    while (emailUsado):
        print("Este email já está sendo usado.")
        email = input("Digite outro email: ")
        gerenciarEscolha(email, "menuCadastro")
        while (emailValido(email) == False):
            email = str(input("Digite um email válido (ex: email@email.com): "))
            gerenciarEscolha(email, "menuCadastro")
            emailUsado = next((u for u in usuarios if u["email"] == email), None)
        emailUsado = next((u for u in usuarios if u["email"] == email), None)

    senha = str(input("Digite sua senha: "))
    gerenciarEscolha(senha, "menuCadastro")
    while (senhaValida(senha) == False):
        print("Sua senha deve conter no mínimo 8 caracteres, um número, um simbolo, uma letra maiúscula e uma letra minúscula")
        senha = str(input("Digite uma senha forte: "))
        gerenciarEscolha(senha, "menuCadastro")

    novoUsuario = {"nome": nome, "idade": idade, "email": email, "senha": senha, "role": "user", "inscrito": None}
    usuarios.append(novoUsuario)
    escreverInfos("src/dados/usuarios.json", usuarios)
    print("Usuário cadastrado com sucesso!")
    input("Pressione <ENTER> para voltar")
    gerenciarEscolha("v", "menuCadastro")