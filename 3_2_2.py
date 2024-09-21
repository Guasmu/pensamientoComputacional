def mostrar_tablas_para(n1):
    if(n1<0) or (n1>10):
        print('Error: El numero debe ser positivo y estar entre 1 y 10')
        return(0)
    for i in range(1,11,1):
        resultado = (n1 * i)
        print('%s x %s = %s'%(n1,i,resultado))