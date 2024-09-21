def ingresoFichas(cantFichas):
    ingreso = input('Ingrese %s fichas para comenzar '%cantFichas)
    fichas = 0
    if(ingreso == 'F'):
        fichas +=1
    while(cantFichas!=fichas):
        ingreso = input('Ingrese %s fichas para comenzar '%cantFichas)
        if(ingreso == 'F'):
            fichas +=1
        else:    
            ingreso = input('Ingrese %s fichas para comenzar '%cantFichas)
    print('A jugar!')
        
def ingresoFichasConCantidad(cantFichas):
    ingreso = input('Ingrese %s fichas para comenzar '%cantFichas)
    fichas = 0
    restanteFichas = cantFichas
    if(ingreso == 'F'):
        fichas +=1
        restanteFichas -=1
    while(cantFichas!=fichas):
        ingreso = input('Ingrese %s fichas para comenzar '%restanteFichas)
        if(ingreso == 'F'):
            fichas +=1
            restanteFichas -=1
        else:    
            ingreso = input('Ingrese %s fichas para comenzar '%restanteFichas)
    print('A jugar!')