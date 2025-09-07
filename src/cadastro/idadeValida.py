def idadeValida(idade):
    try:
        idade = int(idade)
        if idade > 0:
            return True
        else:
            return False
    except ValueError:
        return False

print(idadeValida(""))