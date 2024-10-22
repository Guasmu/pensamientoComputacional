def head(rutaArchivo,n):
    lista = []
    archivo = open(rutaArchivo,'r')
    for i in range(n):
        fila = archivo.readline()
        lista.append(fila)
    return lista
def head1(rutaArchivo,n):
    lista = []
    archivo = open(rutaArchivo,'r')
    lista = archivo.readlines()
    return lista[:n]
def tails(rutaArchivo,n):
    lista = []
    archivo = open(rutaArchivo,'r')
    lista = archivo.readlines()
    return lista[len(lista)-n:]