def limpiarDataHumedad(rutaArchivo):
    with open(rutaArchivo,'r') as archivo:
        listaDatos = archivo.readlines()
    
    datosLimpios = []
    datosSucios = []

    for linea in listaDatos[1:]:
        datos = linea.strip('\n').split(';')
        try:
            humedad = float(datos[2])
            datosLimpios.append(linea)
        except:
            datosSucios.append(linea)
    
    with open('data_limpia.csv','w') as archivo:
        archivo.writelines(datosLimpios)
    
    with open('errores.csv','w') as archivo:
        archivo.writelines(datosSucios)
    
    return len(datosSucios) == 0