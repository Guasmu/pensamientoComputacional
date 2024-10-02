def agenda(diccionario):
    nuevoDiccionario = diccionario
    ingreso = input('Ingrese un nombre ')
    while ingreso != 'EXIT':
        if ingreso in diccionario:
            print(diccionario[ingreso])
        else:
            telefono = input('Ingrese el telefono de %s '%ingreso)
            nuevoDiccionario[ingreso]=telefono
        ingreso = input('Ingrese un nombre ')
    return nuevoDiccionario
#dic1 = {'jorge': 42, 'hernan': 25, 'julio': 85}
#agenda(dic1) 