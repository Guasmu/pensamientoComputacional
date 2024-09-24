def separarListaA(articulos):
    return articulos.split(',')
#print(separarListaA('pan, arroz, pescado, jugo, fideos'))
def juntarListaPrecios(articulos,precios):
    lista = []
    listaArticulos = articulos.split(',')
    listaPrecios = precios.split(',')
    for i in range(len(listaArticulos)):
        tupla = (listaArticulos[i],listaPrecios[i])
        lista.append(tupla)
    return lista

articulos = 'pan, arroz, pescado, jugo, fideos'
precios = '100, 50, 200, 80, 30'
#print(juntarListaPrecios(articulos,precios))

def precioTotalC(lista):
    total = 0
    for i in lista:
       precio = i[1]
       total += int(precio)
    return total
print(precioTotalC(juntarListaPrecios(articulos,precios)))