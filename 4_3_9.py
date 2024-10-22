art1 = {
    'nombre': 'papa',
    'precio': 20,
    'cantidad': 1
}
art2 = {
    'nombre': 'cebolla',
    'precio': 30,
    'cantidad': 4
}
ticket = []
ticket.append(art1)
ticket.append(art2)
def totalAPagar(ticket):
    precioTotal = 0
    for i in range(len(ticket)):
        precioArticulo = (ticket[i])['precio']*(ticket[i])['cantidad']
        precioTotal = precioArticulo + precioTotal
    return precioTotal
print(totalAPagar(ticket))
