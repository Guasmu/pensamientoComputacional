def count(dirArchivo):
    archivo = open(dirArchivo,'r')
    return len(archivo.readlines())
