def stringALista(string1):
    return string1.upper()

def stringAListaUpper(string1):
    return list(map(stringALista, string1))
print(stringAListaUpper('output'))