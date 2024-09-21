def piedraPapelTijera():
    jugada = input('Ingrese su jugada,R para piedra, P para papel o T para tijera. Ingrese X para dejar de jugar ')
    jugada = jugada.upper()
    while(jugada !='X'):
        if((jugada !='X') and (jugada !='R') and (jugada !='P') and (jugada !='T')):
            print('su jugada no esta disponible ')
        elif(jugada == 'T'):
            print('Piedra, gane ')
        elif(jugada == 'P'):
            print('Tijera, gane ')
        elif(jugada == 'R'):
            print('Papel, gane ')
        jugada = input('Ingrese una nueva jugada para comenzar una nueva ronda, o presione X para salir ')
        jugada = jugada.upper()
piedraPapelTijera()