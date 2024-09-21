def promedioExamen(ejerciciosExamen,porcentajeAprobacion):
    cantidadResuelto = input('Ingrese la cantidad de ejercicios resueltos o presione * para salir ')
    if (cantidadResuelto == '*'):
        return 0
    while(cantidadResuelto != '*'):
        porcentajeAlumno = (int(cantidadResuelto) / ejerciciosExamen)* 100  
        print('el porcentaje que el alumno completo correctamente es %s'%porcentajeAlumno)
        if(porcentajeAlumno >= porcentajeAprobacion):
            print('El alumno aprobo')
        else:
            print('El alumno no aprobo')    
        cantidadResuelto = input('Ingrese la cantidad de ejercicios resueltos o presione * para salir ')

def promedioExamenB(ejerciciosExamen,porcentajeAprobacion):
    cantidadResuelto = input('Ingrese la cantidad de ejercicios resueltos o presione * para salir ')
    if (cantidadResuelto == '*'):
        return 0
    cantidadResuelto = int(cantidadResuelto)
    while(cantidadResuelto != '*'):
        cantidadResuelto = int(cantidadResuelto)
        while((cantidadResuelto>ejerciciosExamen) or (cantidadResuelto<0)):
            cantidadResuelto = int(input('Los datos ingresados son incorrectos, ingreselos de nuevo '))
        porcentajeAlumno = (cantidadResuelto / ejerciciosExamen)* 100  
        print('el porcentaje que el alumno completo correctamente es %s, la cantidad de ejercicios es %s y el porcentaje necesario para aprobar es %s'%(porcentajeAlumno,ejerciciosExamen,porcentajeAprobacion))
        if(porcentajeAlumno >= porcentajeAprobacion):
            print('El alumno aprobo')
        else:
            print('El alumno no aprobo')    
        cantidadResuelto = input('Ingrese la cantidad de ejercicios resueltos o presione * para salir ')
promedioExamenB(10,50)