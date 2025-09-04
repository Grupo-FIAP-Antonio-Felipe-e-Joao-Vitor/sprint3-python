def idadeValida(idade):
    try:
        idade = int(idade)
        return True
    except ValueError:
        return False

print(idadeValida(""))