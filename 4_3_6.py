'''
dict1 = {
    'nombre': 'Violeta',
    'apellido': 'Perez',
    'dni':42000000,
    'carrera':'Informatica'
}
estudiantes = []
estudiantes.append(dict1)
'''
#b
dict1 = {
    'nombre': 'Violeta',
    'apellido': 'Perez',
    'dni':42000000,
    'carrera':'Informatica',
    'notas':
        {
        'Algoritmos y Programacion III': 'nota',
        'Analisis Matematico II': 'nota'
        }
}
dict2 = {
    'nombre': 'Violeta',
    'apellido': 'Gutierrez',
    'dni':42000000,
    'carrera':'Informatica',
    'notas':
        {
        'Algoritmos y Programacion III': 5,
        'Analisis Matematico II': 8,
        'Analisis Matematico I': 8,
        }
}
dict3 = {
    'nombre': 'Analia',
    'apellido': 'Gutierrez',
    'dni':42000000,
    'carrera':'Informatica',
    'notas':
        {
        'Algoritmos y Programacion III': 5,
        'Analisis Matematico II': 8,
        'Analisis Matematico I': 8,
        'Analisis Matematico III': 8,
        }
}
estudiantes = []
estudiantes.append(dict1)
estudiantes.append(dict2)
estudiantes.append(dict3)
dict1['notas']['Algoritmos y Programacion III'] = 7
dict1['notas']['Analisis Matematico II'] = 4

def buscarMayorCantNotas(estudiantes):
    longitudPrevia = 0
    for i in estudiantes:
        if len(i['notas']) > longitudPrevia:
            longitudPrevia = len(i['notas'])
            dictPrevio = i
    print(dictPrevio)

print(buscarMayorCantNotas(estudiantes))