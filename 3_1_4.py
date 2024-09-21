def esVocalA(letra):
    if ((letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u') or (letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or (letra == 'U')):
        return(True)
    return(False)
def esVocalB(letra):
    return(letra in ('aeiou'))
def esVocalC(letra):
    return(letra.lower() in ('aeiou'))