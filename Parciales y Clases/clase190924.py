def filtro6(x):
    return (x % 6 == 0)
def multiplosDeSeis(n1,n2):
    l1 = list(range(n1,n2+1))
    return tuple(filter(filtro6,l1))
#print(multiplosDeSeis(4,24))

def lowerUpperTuple(string1):
    listTuple = []
    for i in string1:
        tuple1 = (i,i.upper())
        listTuple.append(tuple1)
    return listTuple
#print(lowerUpperTuple('alto'))

def lowerUpperTupleF(i):
    return (i,i.upper())

def lowerUpperTuple1(string1):
    return list(map(lowerUpperTupleF,string1))
print(lowerUpperTuple1('alto'))

def lista_personas(cadena):
    lista = []
    personas = cadena.split(';')
    for persona in personas:
        lista.append(tuple(persona.split('-')))
    return lista