def separarListaA(string1):
    return string1.split(',')
#print(separarListaA('pan, arroz, pescado, jugo, fideos'))
def juntarListaPrecios(string1,precios):
    lista = []
    listaArticulos = string1.split(',')
    listaPrecios = precios.split(',')
    for i in range(len(listaArticulos)):
        listaArticulos.extend(listaPrecios)
    return listaArticulos
articulos = 'pan, arroz, pescado, jugo, fideos'
precios = '100, 50, 200, 80, 30'
print(juntarListaPrecios(articulos,precios))
