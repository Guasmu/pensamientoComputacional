def multiplos7(n1,n2):
    suma = 0
    for i in range (n1,n2+1,1):
        if (i % 7 == 0):
            suma += i
    print(suma)

def multiplos7Promedio(n1,n2):
    suma = 0
    promedio = 0
    for i in range (n1,n2+1,1):
        if (i % 7 == 0):
            suma += i
            promedio += 1
    print(suma/promedio)

def multiplos7Promedio3Multiplos(n1,n2):
    suma = 0
    promedio = 0
    for i in range (n1,n2+1,1):
        if (i % 7 == 0) and (promedio<3):
            suma += i
            promedio += 1
    print(suma/promedio)

def multiplos7PromedioNoMultiplo2(n1,n2):
    suma = 0
    promedio = 0
    for i in range (n1,n2+1,1):
        if (i % 7 == 0) and (i % 2 != 0):
            suma += i
            promedio += 1
    print(suma/promedio)