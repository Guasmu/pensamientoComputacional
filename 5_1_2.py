def cat(file):
    with open(file,'r') as file:
        file1 = file.read()
    print (file1)
    return None
#cat('./Ejemplos Archivos/archivo1.txt')