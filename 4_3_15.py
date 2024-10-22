dictEjercicios = {
    '1_1_1' : 'a',
    '1_1_2' : 'b'
}
def programaEjercicios(diccionario):
    try:
        ejercicio = input('Escriba el ejercicio a mostrar ')
        print(diccionario[ejercicio])
    except KeyError:
        print('No existe un ejercicio bajo esa entrada')
#El Try y except es opcional, yo lo hice asi para probarlo