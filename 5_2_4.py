def promedioTemperaturas(rutaArchivo):
    try:
        with open(rutaArchivo,'r') as archivo:
            listaTemperaturas = archivo.readlines()
    except:
        return None
    total = len(listaTemperaturas)
    suma = 0
    cantidad = 0
    for temperatura in listaTemperaturas:
        try:
            suma += float(temperatura)
            cantidad += 1
        except:
            pass
    promedio = suma / cantidad
    porcentaje = ((total - cantidad) / total)* 100
    return (promedio,porcentaje)
