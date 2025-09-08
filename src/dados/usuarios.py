usuarios = [
    # Nome    # Idade     # Email    # Senha    #role     #torneio
    {"nome": "admin", "idade": 18, "email": "admin@admin.com", "senha": "Admin@1234", "role": "adm", "inscrito": None},
    {"nome": "admin", "idade": 18, "email": "adm", "senha": "adm", "role": "adm", "inscrito": None},
    {"nome": "user", "idade": 18, "email": "user@user.com", "senha": "user@1234", "role": "user", "inscrito": 1},
    {"nome": "userTeste", "idade": 18, "email": "user", "senha": "user", "role": "user", "inscrito": None},
]

emailUsuarios = []
for usuario in usuarios:
    emailUsuarios.append(usuario["email"])


senhaUsuarios = []
for usuario in usuarios:
    senhaUsuarios.append(usuario["senha"])

usuarioLogado = []