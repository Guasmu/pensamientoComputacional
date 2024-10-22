def listaPeliculasPiolas(lista):
    listaSalida = []
    for i in lista:
        if i['puntuacion']>7:
            listaSalida.append(i)
    return listaSalida
