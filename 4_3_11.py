def promedioNotas1(lista):
    sumatoriaNotas = 0
    cantExamenes = 0
    for i in lista:
        if i['intento'] == 1:
            sumatoriaNotas=int(i['nota'])+sumatoriaNotas
            cantExamenes += 1
    return (sumatoriaNotas / cantExamenes)

def promedioNotas2(lista,parcial):
    sumatoriaNotas = 0
    cantExamenes = 0
    for i in lista:
        if i['intento'] == parcial:
            sumatoriaNotas=int(i['nota'])+sumatoriaNotas
            cantExamenes += 1
    return (sumatoriaNotas / cantExamenes)