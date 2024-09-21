def esBisiesto(year):
    if ((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
        return(True)
    if ((year % 4 == 0) and (year % 100 == 0)):
        return(False)
    if (year % 4 == 0):
        return (True)
    return(False)

def cantidadDias():
    month= int(input('Ingrese el mes a calcular en numero, por ejemplo, febrero = 2 \n'))
    year = int(input('Ingrese el año a calcular \n'))
    if (esBisiesto(year) == True) and (month == 2):
        print('La cantidad de dias en el mes %s de %s es 29' %(month, year))
        return(0) 
    elif (esBisiesto(year) == False) and (month == 2):
        print('La cantidad de dias en el mes %s de %s es 28' %(month, year))
        return(0)
    for i in range(4,7,2):
        if (i == month):
            print('la cantidad de dias en el mes %s de %s es 30'%(month ,year))
            return(0)
    for i in range(1,8,2):
        if (i == month):
            print('la cantidad de dias en el mes %s de %s es 31'%(month ,year))
            return(0)
    for i in range(8,13,2):
        if (i == month):
            print('la cantidad de dias en el mes %s de %s es 31'%(month ,year))
            return(0)
    for i in range(9,12,2):
        if (i == month):
            print('la cantidad de dias en el mes %s de %s es 30'%(month ,year))
            return(0)

def signoZodiaco():
    day = int(input('Ingrese su dia de nacimiento\n'))
    month = int(input('Ingrese su mes de nacimiento\n'))
    if((day >= 21) and (month == 3)) or ((day<=20) and (month == 4)):
        print('Usted es Aries')
    elif((day >= 21) and (month == 4)) or ((day<=20) and (month == 5)):
        print('Usted es Tauro')
    elif((day >= 21) and (month == 5)) or ((day<=22) and (month == 6)):
        print('Usted es Geminis')
    elif((day >= 22) and (month == 6)) or ((day<=23) and (month == 7)):
        print('Usted es Cancer')
    elif((day >= 24) and (month == 7)) or ((day<=23) and (month == 8)):
        print('Usted es Leo')
    elif((day >= 24) and (month == 8)) or ((day<=23) and (month == 9)):
        print('Usted es Virgo')
    elif((day >= 24) and (month == 9)) or ((day<=22) and (month == 10)):
        print('Usted es Libra')
    elif((day >= 23) and (month == 10)) or ((day<=22) and (month == 11)):
        print('Usted es Escorpio')
    elif((day >= 23) and (month == 11)) or ((day<=21) and (month == 12)):
        print('Usted es Sagitario')
    elif((day >= 22) and (month == 12)) or ((day<=20) and (month == 1)):
        print('Usted es Capricornio')
    elif((day >= 21) and (month == 1)) or ((day<=19) and (month == 2)):
        print('Usted es Acuario')
    elif((day >= 20) and (month == 2)) or ((day<=20) and (month == 3)):
        print('Usted es Piscis')