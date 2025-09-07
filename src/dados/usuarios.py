usuarios = [
    # Nome    # Idade     # Email    # Senha    #role     #torneio
    ["admin", 18, "admin@admin.com", "Admin@1234", "adm", None],
    ["admin", 18, "adm", "adm", "adm", None],
    ["user", 18, "user@user.com", "user@1234", "user", 1],
]

emailUsuarios = []
for usuario in usuarios:
    emailUsuarios.append(usuario[2])


senhaUsuarios = []
for usuario in usuarios:
    senhaUsuarios.append(usuario[3])

usuarioLogado = []