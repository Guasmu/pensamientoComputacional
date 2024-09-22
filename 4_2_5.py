def dominoEncajanA(ficha1,ficha2):
    return ((ficha1[0] == ficha2[0]) or (ficha1[0] == ficha2[1]) or (ficha1[1] == ficha2[0]) or (ficha1[1] == ficha2[1]))
#print(dominoEncajanA((3,4),(5,5)))
def dominoEncajanB(ficha1,ficha2):
    return ((ficha1[0] == ficha2[0]) or (ficha1[0] == ficha2[2]) or (ficha1[2] == ficha2[0]) or (ficha1[2] == ficha2[2]))
#print(dominoEncajanB('3-2','5-4'))