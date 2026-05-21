while True:
    numero= int(input('Ingresa un Numero: '))
    if numero < 0:
        print('Negativo')
    elif numero > 0:
        print('Positivo')
    elif numero ==0:
        print('Es Cero')
    
    seguir= input('Seguis? Si/No: ')
    if seguir== 'No' or 'no':
        break