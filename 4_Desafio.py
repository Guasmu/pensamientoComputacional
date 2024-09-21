def devolverIniciales(string):
    palabras = string.split()
    iniciales = ""
    for i in palabras:
        iniciales += i[0]
    return iniciales.upper()

def devolverIniciales2(string):
    iniciales = string[0]
    for i in string:
        if(i-1 = ''):
            