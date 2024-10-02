import random
def tirarDado(n):
    i = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    diccionarioSalida = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    while n > i:
        aleatorio = random.randint(1,6)
        if aleatorio == 1:
            c1 += 1
            diccionarioSalida[aleatorio]=c1
        elif aleatorio == 2:
            c2 += 1
            diccionarioSalida[aleatorio]=c2
        elif aleatorio == 3:
            c3 += 1
            diccionarioSalida[aleatorio]=c3
        elif aleatorio == 4:
            c4 += 1
            diccionarioSalida[aleatorio]=c4
        elif aleatorio == 5:
            c5 += 1
            diccionarioSalida[aleatorio]=c5
        elif aleatorio == 6:
            c6 += 1
            diccionarioSalida[aleatorio]=c6
        i += 1
    return diccionarioSalida
#print(tirarDado(100000000))
def tirar2Dados(n):
    i = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    c10 = 0
    c11 = 0
    c12 = 0
    diccionarioSalida = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
    }
    while n > i:
        aleatorio = random.randint(1,6)+random.randint(1,6)
        if aleatorio == 1:
            c1 += 1
            diccionarioSalida[aleatorio]=c1
        elif aleatorio == 2:
            c2 += 1
            diccionarioSalida[aleatorio]=c2
        elif aleatorio == 3:
            c3 += 1
            diccionarioSalida[aleatorio]=c3
        elif aleatorio == 4:
            c4 += 1
            diccionarioSalida[aleatorio]=c4
        elif aleatorio == 5:
            c5 += 1
            diccionarioSalida[aleatorio]=c5
        elif aleatorio == 6:
            c6 += 1
            diccionarioSalida[aleatorio]=c6
        elif aleatorio == 7:
            c7 += 1
            diccionarioSalida[aleatorio]=c7
        elif aleatorio == 8:
            c8 += 1
            diccionarioSalida[aleatorio]=c8
        elif aleatorio == 9:
            c9 += 1
            diccionarioSalida[aleatorio]=c9
        elif aleatorio == 10:
            c10 += 1
            diccionarioSalida[aleatorio]=c10
        elif aleatorio == 11:
            c11 += 1
            diccionarioSalida[aleatorio]=c11
        elif aleatorio == 12:
            c12 += 1
            diccionarioSalida[aleatorio]=c12
        i += 1
    return diccionarioSalida
print(tirar2Dados(10000))
#ambos fueron hechos de la manera mas simple posible, queda optimizarlo.