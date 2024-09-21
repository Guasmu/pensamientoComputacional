def password(password):
    passwordGuess = input('Ingrese la contraseña ')
    while(passwordGuess != password):
        passwordGuess = input('Contraseña incorrecta. Ingrese la contraseña ')
    print('Bienvenido')
def passwordWithAttempts(password):
    passwordGuess = input('Ingrese la contraseña ')
    attempts = 2
    while(passwordGuess != password) and (attempts>0):
        passwordGuess = input('Contraseña incorrecta. Ingrese la contraseña ')
        attempts -= 1
    if (attempts == 0):
        print('Te has quedado sin intentos')
    else:
        print('Bienvenido')
def passwordWithAttemptsBool(password):
    passwordGuess = input('Ingrese la contraseña ')
    attempts = 2
    while(passwordGuess != password) and (attempts>0):
        passwordGuess = input('Contraseña incorrecta. Ingrese la contraseña ')
        attempts -= 1
    if (attempts == 0):
        return(False)
    else:
        return(True)