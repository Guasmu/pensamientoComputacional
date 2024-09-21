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
    n = 0
    cantMundiales = 0
    while (len(tuple1)>n):
        tupla1 = tuple1[n]
        if cantMundiales > tupla1[1]:

        n +=1
tupla = [("Argentina", 3), ("España",1), ("Uruguay", 2), ("Francia",2)]
#paisesMundiales(tupla)