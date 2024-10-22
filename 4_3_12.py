articulos = {
    'art1':{
        'fecha de vencimiento': 2025,
        'calidad': 'no'
    },
    'art2':{
        'fecha de vencimiento': 2025,
        'calidad': 'si'
    }
}
lista = []
lista.append(articulos)
def filtrarPorCalidad(lista):
    listaSalida = []
    for i in range(len(lista)):
        for clave in lista[i]:
            if ((lista[i][clave])['calidad']) == 'no':
                productoEliminado = {clave}
                listaSalida.append(productoEliminado)
    return listaSalida
print(filtrarPorCalidad(lista))
