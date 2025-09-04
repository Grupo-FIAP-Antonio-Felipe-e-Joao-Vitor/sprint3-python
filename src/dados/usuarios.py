usuarios = [
    # Nome    # Idade     # Email    # Senha
    ["admin", 18, "admin@admin.com", "Admin@1234"],
]

emailUsuarios = []
for usuario in usuarios:
    emailUsuarios.append(usuario[2])


senhaUsuarios = []
for usuario in usuarios:
    senhaUsuarios.append(usuario[3])

usuarioLogado = []