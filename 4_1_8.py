def buscadorPalabra(palabra,texto):
    return texto.find(palabra)
#print(buscadorPalabra('milanesa','el sanguche de milanesa es el mejor plato de la historia'))
def buscadorPalabraB(palabra,texto):
    cantidad = texto.count(palabra)
    n = 0
    lista = []
    i = int(texto.find(palabra))
    while (cantidad > n):
       lista.append(texto.find(palabra,i))
       i = texto.find(palabra,i+1)
       n += 1
    return lista

print(buscadorPalabraB('al','calcule el precio al valor actual'))
#como costo este
def cantidadOcurrenciasC(palabra,texto):
    return texto.count(palabra)
#print(cantidadOcurrenciasC('al','calcule el precio al valor actual'))
'''
def buscadorPalabraBClase(palabra,texto):
    listaApariciones = []
    i = 0
    listaApariciones.append(texto.find(palabra))
    while(i != -1):
        listaApariciones.append(i)
        i = texto.find(palabra,i+1)        
    return listaApariciones
'''