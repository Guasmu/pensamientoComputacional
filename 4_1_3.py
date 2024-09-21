def esPalindromo(string1):
    return (string1 == string1[::-1])
#print(esPalindromo('menem'))
def listaCapicua(list1):
    return list(filter(esPalindromo,list1))
#print(listaCapicua(['menem','ana','colon','neuquen']))
