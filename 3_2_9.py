def esPrimo(numero):
    nPrimo = 0
    for i in range(1,numero+1,1):
        if (numero % i == 0):
            nPrimo +=1
    if(nPrimo == 2):
        return(True)
    else:
        return(False)