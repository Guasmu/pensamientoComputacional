#ejercicio 1
def calculadoraPagos(monto):
    acumuladoPagos = 0
    cantGente = 1
    montoRestante = monto
    acumuladoPagos = int(input('Total %s, ingrese un monto: '%monto))
    while monto>acumuladoPagos:
        montoRestante = montoRestante - acumuladoPagos
        acumuladoPagos = acumuladoPagos + int(input('Total %s, ingrese un monto '%montoRestante))
        cantGente += 1
    promedio = acumuladoPagos / cantGente
    vuelto = acumuladoPagos - monto
    print('Monto alcanzado ')
    print('Promedio de pagos %s'%promedio)
    print('El vuelto es %s'%vuelto)
#calculadoraPagos(25000) 
#ejercicio 2
def listaAreaTriangulos(listaTuplas):
    listaAreas= []

    for tupla in listaTuplas:
        if tupla[0]>0 and tupla[1]>0:
            area = (tupla[0]*tupla[1])/2
            listaAreas.append(area)
        else:
            return listaAreas
    return listaAreas
#ejercicio 3
def calcularDeterminante(matriz):
    if len(matriz) != 4:
        return None
    a,b,c,d = matriz
    return a*d-b*c