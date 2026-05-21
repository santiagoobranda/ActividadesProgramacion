NumeroSecreto= 1-50
for i in range (3):
    numero= int(input('Adivina el Numero: '))
    if numero== NumeroSecreto:
        print('Correcto, Ganaste')
        break
    else:
        print('Incorrecto')
    if i == 2:
        print('Perdiste')