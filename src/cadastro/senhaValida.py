import string

def senhaValida(senha):
    letrasMaiusculas = tuple(string.ascii_uppercase)
    letrasMinusculas = tuple(string.ascii_lowercase)
    numeros = tuple(string.digits)
    simbolos = tuple(string.punctuation)

    possuiMaiusculas = False
    possuiMinusculas = False
    possuiNumeros = False
    possuiSimbolos = False
    if len(senha) < 8:
        return False
    for letra in letrasMaiusculas:
        if letra in senha:
            possuiMaiusculas = True
    for letra in letrasMinusculas:
        if letra in senha:
            possuiMinusculas = True
    for numero in numeros:
        if numero in senha:
            possuiNumeros = True
    for simbolo in simbolos:
        if simbolo in senha:
            possuiSimbolos = True

    if possuiMaiusculas and possuiMinusculas and possuiNumeros and possuiSimbolos:
        return True
    if not possuiMaiusculas or not possuiMinusculas or not possuiNumeros or not possuiSimbolos:
        return False