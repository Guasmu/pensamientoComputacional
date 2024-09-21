"""
Hacer una funcion que reciba una lista de nombres y un numero, que representa el cupo
La funcion debe imprimir una a una a las personas que entraron en
el cupo en orden alfabetico. Luego, devolver en una lista a los
nombres que no pudieron entrar al curso por falta de cupo
"""
def seleccionarPorCupo(lista,cupo):
    aceptados = lista[:cupo]
    rechazados = lista[cupo:]

    for nombre in sorted(aceptados):
        print(nombre)
    return rechazados
seleccionarPorCupo(['sanchez','gonzalez','villanova'],2)