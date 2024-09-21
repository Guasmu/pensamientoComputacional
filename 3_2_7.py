import random
def adivinarNumero1a10(numero):
    intento = int(input('Adivine el numero entre el 1 y el 10 '))
    while(intento != numero):
        if(intento>numero):
            print('Ese no es, es menor')
        elif(intento<numero):
            print('Ese no es, es mayor')
        intento = int(input('Intente de nuevo '))
    print('Correcto, %s es el numero a adivinar'%numero)

def adivinarNumero1a10Intentos(numero):
    intento = int(input('Adivine el numero entre el 1 y el 10 '))
    cantIntentos=2
    while(intento != numero) and (cantIntentos>0):
        if(intento>numero):
            print('Ese no es, es menor')
        elif(intento<numero):
            print('Ese no es, es mayor')
        intento = int(input('Intente de nuevo '))
        cantIntentos-=1
    if (cantIntentos==0) and (intento != numero):
        print('Te has quedado sin intentos')
    else:
        print('Correcto, %s es el numero a adivinar'%numero)

def adivinarNumero1a10Intentos():
    numero = random.randint(1,10)
    intento = int(input('Adivine el numero entre el 1 y el 10 '))
    cantIntentos=2
    while(intento != numero) and (cantIntentos>0):
        if(intento>numero):
            print('Ese no es, es menor')
        elif(intento<numero):
            print('Ese no es, es mayor')
        intento = int(input('Intente de nuevo '))
        cantIntentos-=1
    if (cantIntentos==0) and (intento != numero):
        print('Te has quedado sin intentos')
    else:
        print('Correcto, %s es el numero a adivinar'%numero)