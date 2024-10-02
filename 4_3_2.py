def cantPalabras(cadena):
    diccionarioSalida = {}
    lista = cadena.split()
    for i in range(len(lista)):
        diccionarioSalida[lista[i]]=[lista.count(lista[i])]
    return diccionarioSalida
#cadena1 = 'que lindo dia que hace hoy'
#print(cantPalabras(cadena1))
def cantCaracteres(cadena):
    diccionarioSalida = {}
    for i in cadena:
        diccionarioSalida[i]=[cadena.count(i)]
    return diccionarioSalida
#print(cantCaracteres(cadena1))