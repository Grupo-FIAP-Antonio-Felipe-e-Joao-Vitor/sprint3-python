usuarios = [
    {"nome": "admin", "idade": 18, "email": "admin@admin.com", "senha": "Admin@1234", "role": "adm", "inscrito": None},
]

emailUsuarios = []
for usuario in usuarios:
    emailUsuarios.append(usuario["email"])


senhaUsuarios = []
for usuario in usuarios:
    senhaUsuarios.append(usuario["senha"])

usuarioLogado = []