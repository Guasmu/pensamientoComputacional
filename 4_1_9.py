def caracteresDiferentes(string1,string2):
    lista = []
    for i in string1:
        if (i not in string2):
            lista.append(i)
    for i in string2:
        if (i not in string1):
            lista.append(i)
    return lista
print(caracteresDiferentes('python','hola'))