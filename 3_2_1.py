def listarNumerosA():
    for i in range(10,21,1):
        print(i)
def saludarPersonasB():
    for i in ['Flaminia','Serena','Agustina','Priscila','Sol','Agostina','Iara','Lu']:
        print('Hola %s! Vamos a aprender a programar'%i)
def sumar5NumerosC():
    numero1 = int(input('Ingrese un numero\n'))
    numero2 = int(input('Ingrese otro numero\n'))
    numero3 = int(input('Ingrese otro numero\n'))
    numero4 = int(input('Ingrese otro numero\n'))
    numero5 = int(input('Ingrese el ultimo numero\n'))
    print(numero1 + numero2 + numero3 + numero4 + numero5)
def nDivisiblesPor7D():
    for i in range(105,200,7):
        print(i)

def recorrerNumerosE(n1,n2):
    for i in range(n1,n2+1,1):
        if(i % 2 == 0):
            print('%s es par'% i)
        else:
            print('%s es impar'% i)
