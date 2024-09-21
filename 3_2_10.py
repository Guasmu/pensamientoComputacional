def esPrimo(numero):
    nPrimo = 0
    for i in range(1,numero+1,1):
        if (numero % i == 0):
            nPrimo +=1
    if(nPrimo == 2):
        return True
    else:
        return False

def numPrimosHastaN(N):
    for i in range(0,N+1,1):
        if (esPrimo(i) == True):
            print(i)