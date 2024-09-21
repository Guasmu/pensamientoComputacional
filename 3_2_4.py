def cobro(monto):
    print('Su total a pagar es: %s'%monto)
    pago = int(input('Ingrese el monto a pagar\n'))
    montoRestante = (monto - pago)
    while(montoRestante>0):
        print('pendientes: %s'%montoRestante)
        pago = int(input('Ingrese el monto a pagar:\n'))
        montoRestante = (montoRestante - pago)
    print('pendientes: 0. Gracias por su compra.')

def cobroConVuelto(monto):
    print('Su total a pagar es: %s'%monto)
    pago = int(input('Ingrese el monto a pagar\n'))
    montoRestante = (monto - pago)
    while(montoRestante>0):
        print('pendientes: %s'%montoRestante)
        pago = int(input('Ingrese el monto a pagar:\n'))
        montoRestante = (montoRestante - pago)
    montoRestante = int((montoRestante ** 2)**(1/2))
    print('pendientes: 0. Su vuelto es: %s Gracias por su compra.'%montoRestante)