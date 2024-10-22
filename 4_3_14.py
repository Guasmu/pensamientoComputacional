listaDictLaura = [
    {
        'año': 2020,
        'seniority': 'trainee',
        'sueldo': 200000,
        'bono' : 10000
    },
    {
        'año': 2021,
        'seniority': 'junior',
        'sueldo': 250000,
        'bono' : 20000
    },
    {
        'año': 2022,
        'seniority': 'semi-senior',
        'sueldo': 500000,
        'bono' : 260000
    },

]
# porcentaje bono = (sueldo/bono)*100
def convertirBonoAPorcentaje(lista):
    for i in range(len(lista)):
        sueldo = (lista[i])['sueldo']
        bono = (lista[i])['bono']
        porcentaje = (bono/sueldo)*100
        (lista[i])['bono'] = porcentaje
    return lista
    
convertirBonoAPorcentaje(listaDictLaura)

def filtrar50(lista):
    return list(filter(lambda x:(x['bono']>50),lista))
print(filtrar50(listaDictLaura))