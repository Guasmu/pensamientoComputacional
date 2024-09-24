def consonante(x):
    vocales = ('aeiou')
    return not(x in vocales)

def tupla(x):
    return 

def esConsonante(string1):
    listaSalida = tuple(filter(consonante, string1))
    return listaSalida
#print(esConsonante('terminal'))
def esConsonanteM(string1):
    listaSalida = map(consonante,string1)
    return tuple(map(tupla,listaSalida))
print(esConsonanteM('terminal'))