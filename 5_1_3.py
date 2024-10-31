def head(file,n):
    with open(file,'r') as file:
        list1 = file.readlines()
    return list(map(lambda x: x.strip(), list1))[:n]
#print(head('./Ejemplos Archivos/archivo1.txt',5))

