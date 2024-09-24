def agendaSimplificada(cadena,lista):
    lista1 = []
    n = 0
    for i in lista:
        lista1.append(lista[n][0])
        n += 1
    return ''.join(lista1).find(cadena)
cadena = 'alvarez'
lista = [('ramirez',2555),('gonzalez',2512),('alvarez',8432),]
print(agendaSimplificada(cadena,lista))