NumeroSecreto= 25
numero= int(input('Adivina el Numero Entre 1 y 30: '))
while numero != NumeroSecreto:

    if numero >= 1 and numero <= 10:
        print('Muy Bajo')
    
    elif numero >= 11 and numero <= 20:
        print('Cerca')

    elif numero >= 21 and numero <= 24:
        print('Muy Cerca, Es Mayor')

    elif numero >= 26 and numero <= 30:
        print('Te Pasaste, Es Menor')
    elif numero > 30:
        print('Te Pasaste de 30')

    numero= int(input('Adivina el Numero Entre 1 y 30: '))

else:
    print('Adivinaste!')