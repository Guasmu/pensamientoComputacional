def estaListaEsPar(list1):
    return ((len(list1) % 2) == 0)
#print(estaListaEsPar([1,2,3]))
def maximoYMinimo(list1):
    lista = []
    lista.append(max(list1))
    lista.append(min(list1))
    return lista

def listaOrdenadaAscendente(list1):
    return sorted(list1)
#print(listaOrdenadaAscendente([4,2,7,1]))