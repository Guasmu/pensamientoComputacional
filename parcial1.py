#Tema 2 2024 
# Escribir un programa que reciba el nivel de lluvia por el usuario, sume cada instancia e imprima el resultado final al momento que usuario salga del programa ingresando *
def sumaNivelLluvias():
    nivelTotal = 0
    nivelLluvias = input('Ingrese un nivel de lluvias en mm: ')
    while nivelLluvias != '*':
        nivelLluvias = int(nivelLluvias)
        if nivelLluvias < 0:
            print('Ingreso invalido. El valor debe ser positivo')
            nivelLluvias = input('Ingrese un nivel de lluvias en mm: ')
        else:
            nivelTotal = nivelTotal + nivelLluvias
            nivelLluvias = input('Ingrese un nivel de lluvias en mm: ')
    print('El total ingresado es %s mm'%nivelTotal)
    print('adios')
#sumaNivelLluvias()
# 2 Hacer una lista de tuplas con una lista de entrada, concatenando las listas elemento por elemento. traducir_al_ingles traduce palabra por palabra la lista.
def traducir_al_ingles(x):
    return '1'
def traducirPalabraPorPalabra(lista):
    listaSalida = []
    listaEnIngles = list(map(traducir_al_ingles,lista))
    for i in range(len(lista)):
        tupla = tuple(lista[i]+listaEnIngles[i])
        listaSalida.append(tupla)
    return listaSalida
#print(traducirPalabraPorPalabra(['A','B','C','D']) )
# 3 Hacer la sumatoria del reciproco de k, desde 1 hasta k inclusive
def sumatoriaReciprocos(k):
    sumaTotal = 0
    for i in range(1,k+1):
        sumaTotal = sumaTotal + 1/i
    return sumaTotal
#print(sumatoriaReciprocos(4))