def mostrar_tablas_para():
    print('Hola! Esto es Tablas de Multiplicar')
    n1 = input('Ingrese un numero o "X" para salir: ')
    while(n1 != 'X'):
        n1 = int(n1)
        if(n1<0) or (n1>10):
            print('Error: El numero debe ser positivo y estar entre 1 y 10')
        else:
            for i in range(1,11,1):
                resultado = (n1 * i)
                print('%s x %s = %s'%(n1,i,resultado))
        n1 = input('Ingrese un numero o "X" para salir: ')
    print('Adios')