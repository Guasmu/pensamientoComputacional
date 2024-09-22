def paisesMundiales(tuple1):
    n = 0
    while (len(tuple1)>n):
        tupla1 = tuple1[n]
        if(n == 0):
            print("pais: Argentina⭐⭐⭐ - Copas: %s"%tupla1[1])
        else:
            print('pais: %s - Copas: %s'%(tupla1[0],tupla1[1]))
        n +=1
tupla = [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]
#paisesMundiales(tupla)
def contarMundiales(tuple1):
    n = 0
    cantMundiales = 0
    while(len(tuple1)>n):
        tupla1 = tuple1[n]
        cantMundiales = tupla1[1]+cantMundiales
        n +=1
    return cantMundiales

#print(contarMundiales(tupla))
def paisesMundialesOrdenados(tuple1):
    tuple1.sort(key = lambda x: x[1],reverse=True) #Creo una funcion con lambda, sliceo con x: y elijo el segundo termino de x (los numeros en la lista), ordeno de manera descendente.
    return tuple1
#print(paisesMundialesOrdenados(tupla))
def mayorA1(tuple):
    return (tuple[1]>1)

def esPar(tuple):
    return (tuple[1] % 2 == 0)

def paisesMundialesMayorA1(tuple1):
    listaMayorA1 = list(filter(mayorA1,tuple1))
    listaPar = list(map(esPar,listaMayorA1))
    return listaMayorA1 + listaPar
#print(paisesMundialesMayorA1(tupla))