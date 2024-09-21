def dayYear():
    day = int(input('Ingrese el dia del año\n'))
    if(day % 7 == 0):
        print('Domingo')
    elif(day % 7 == 1):
        print('Lunes')
    elif(day % 7 == 2):
        print('Martes')
    elif(day % 7 == 3):
        print('Miercoles')
    elif(day % 7 == 4):
        print('Jueves')
    elif(day % 7 == 5):
        print('Viernes')
    elif(day % 7 == 6):
        print('Sabado')