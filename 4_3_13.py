listaMaratonistas = [
{
    'nombre': 'Eliud',
    'DNI': 12000000,
    'maratones':{
        'Buenos Aires':{
            'año':2024,
            'puesto':1,
            'tiempo':15
        }
    }
},
{
    'nombre': 'Aragorn',
    'DNI': 12000000,
    'maratones':{
        'Buenos Aires':{
            'año':2024,
            'puesto':1,
            'tiempo':14
        },
        'Sao Paulo':{
            'año':2024,
            'puesto':1,
            'tiempo':24
        }
    }
}]

def ordenarAlfabeticamente(lista):
    return sorted(lista, key=lambda x: x['nombre'])

def ordenarPorTiempo(lista):

print(ordenarPorTiempo(listaMaratonistas))