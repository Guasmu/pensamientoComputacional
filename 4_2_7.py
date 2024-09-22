def cambiarValorA(tupla,indice,nValor):
    lista = list(tupla)
    lista[indice] = nValor
    return tuple(lista)
#print(cambiarValorA((4,2),1,25))
def cambiarValorB(lista1,indice,nValor):
    lista = lista1
    lista[indice] = nValor
    return lista
#print(cambiarValorB([4,2],1,25))
def cambiarValorC(tupla,vEliminar,nValor):
    n = 0
    nLista = []
    while (len(tupla)>n):
        tupla1 = tupla[n]
        if (tupla1 == vEliminar):
            tupla1 = nValor
            nLista.append(tupla1)
        else:
            nLista.append(tupla1)
        n +=1
    return tuple(nLista)
#print(cambiarValorC((3,5,7),3,2))
def cambiarValorCL(tupla,vEliminar,nValor):
    n = 0
    nLista = []
    while (len(tupla)>n):
        tupla1 = tupla[n]
        if (tupla1 == vEliminar):
            tupla1 = nValor
            nLista.append(tupla1)
        else:
            nLista.append(tupla1)
        n +=1
    return list(nLista)
#print(cambiarValorCL([3,5,7],3,2))