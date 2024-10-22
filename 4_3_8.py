lista = []
dict1 = {
    'dias': {
        'lunes',
        'martes',
        'miercoles'
    }
}
dict2 = {
    'milanesa': 'si'
}
lista.append(dict1)
lista.append(dict2)
def listaValoresClave(lista,clave):
    listaSalida = []
    for i in range(len(lista)):
        if 'dias' in lista[i]:
            listaSalida.append((lista[i])[clave])
    return listaSalida
#print(listaValoresClave(lista,'dias'))