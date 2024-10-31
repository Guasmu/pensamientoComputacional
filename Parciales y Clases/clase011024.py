#clase 11 parcial1
def asignarAulas(lista):
    listaSalida= []
    for estudiante in lista:
        apellido = estudiante[0]
        fecha = estudiante[1]
        if fecha >= '20/03/2020' and fecha <= '01/12/2021':
            aula = 106
        else:
            aula = 1
        listaSalida.append(apellido,fecha,aula)
    return listaSalida
#punto 4.3.1
def tuplasDiccionarios(listaTuplas):
    diccionario = {}
    for tupla in listaTuplas:
        clave, dato = tupla
        if clave in diccionario:
            diccionario[clave].append(dato)
        else:
            diccionario[clave] = [dato]
    return diccionario
