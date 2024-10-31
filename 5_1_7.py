def grep(cadena,ruta):
    with open(ruta,'r') as archivo:
        lista = archivo.readlines()
    for linea in lista:
        if cadena in linea:
            print(linea.strip('\n'))
 