def chequear_cupo(lista,cupo):
    rechazados = lista[cupo:]
    return rechazados
#print(chequear_cupo(['agustina','iara','priscila','carlos'],3))
def chequear_cupoB(lista,cupo):
    ultimoAceptado = lista[cupo-1:cupo]
    return ultimoAceptado
#print(chequear_cupoB(['agustina','iara','priscila','carlos'],3))
