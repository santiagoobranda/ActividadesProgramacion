NumeroS1 = 6
NumeroS2 = 4
NumeroS3 = 1

for i in range(3):

    if i == 0:
        NumeroSecreto = NumeroS1
        texto = 'primer'

    elif i == 1:
        NumeroSecreto = NumeroS2
        texto = 'segundo'

    else:
        NumeroSecreto = NumeroS3
        texto = 'tercer'


    gano = False

    for intento in range(3):

        numero = int(input(f'Adivina el {texto} numero: '))

        if numero == NumeroSecreto:
            print('Ganaste la ronda')
            gano = True
            break
        else:
            print('Incorrecto')


    if gano == False:
        print('Perdiste la ronda')





gano= False

NumeroS1= 1
NumeroS2= 2
NumeroS3= 3

for i in range (3):
    if i == 0:
        