NumeroSecreto= int('16')
numero= int(input('Adivina el Numero: '))
while numero != NumeroSecreto:
    print('Numero Incorrecto')
    numero= int(input('Adivina el numero: '))
if numero== NumeroSecreto:
    print('Numero Correcto')