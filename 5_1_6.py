def wc(textFile):
    with open(textFile,'r') as textFile:
        textLines = textFile.readlines()
    Lines = len(textLines)
    Chars = len(''.join(textLines))
    Words = len(''.join(textLines).split())
    return Lines,Words,Chars
#print(wc('./Ejemplos Archivos/archivo1.txt'))