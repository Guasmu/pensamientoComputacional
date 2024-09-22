def ultimosNumeros(lista1,numero):
    numero = len(lista1)-numero
    print(lista1[:numero-1:-1])
    return lista1[:numero:1]
#print(ultimosNumeros([1,2,3,4,5],4))