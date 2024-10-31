def preguntaRespuesta(pregunta):
    file2 = 'respuesta.txt'
    with open(pregunta,'r') as file:
        file1 = file.read()
    input1 = str(input(file1))
    with open(file2,'w') as file:
        file.write(input1)
#preguntaRespuesta('./Ejemplos Archivos/archivo1.txt')