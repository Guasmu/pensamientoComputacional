def filas(cantElementos,nroFila):
    fila = []
    for i in range(cantElementos):
        if nroFila == i:
            fila.append(1)
        else:
            fila.append(0)
    return fila
def matriz(n):
    matriz = []
    for i in range(n):
        fila = filas(n,i)
        matriz.append(fila)
    return matriz
#print(matriz(4))
def matrizTamanio(tamanio):
    matriz = []
    for i in range(tamanio):
        fila = []
        for c in range(tamanio):
            if i == c:
                fila.append(1)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz
#print(matrizTamanio(5))