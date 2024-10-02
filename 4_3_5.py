def mostrarPalabraLarga(string1):
    outputDict = {}
    matchList = []
    for i in string1:
        list1 = string1.split()
        for word in list1:
            if i in word:
                matchList.append(word)
                matchList = sorted(matchList, key=len, reverse=True)
                outputDict[i]=matchList[0]
        matchList.clear()
    return outputDict
#print(mostrarPalabraLarga('hola buenos dias '))


