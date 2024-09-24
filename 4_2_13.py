def listaSupermercado():
    lista = []
    entrada = input('Ingrese los articulos a comprar, o X para salir ')
    while entrada.upper() != 'X':
        lista.append(entrada)
        entrada = input('Ingrese los articulos a comprar, o X para salir ')
    return ', '.join(lista)
print(listaSupermercado())
