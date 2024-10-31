def tail(file,n):
    with open(file,'r') as file:
        list1 = file.readlines()
    return list1[len(list1)-n:]
#print(tail('./Ejemplos Archivos/archivo1.txt',6))