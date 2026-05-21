PIN = '1234'
saldo_disponible = 10000

for i in range(3):

    ingrese_pin = input('Ingrese su PIN: ')

    if ingrese_pin == PIN:
        print(f'Ingresaste, tu saldo es de ${saldo_disponible}')

        while True:

            dinero = int(input('Cuanto dinero desea retirar: '))

            if dinero <= 0:
                print('Cantidad Invalida')

            elif dinero > saldo_disponible:
                print('Saldo Insuficiente')

            elif dinero == saldo_disponible:
                print('Retiro exitoso, te quedaste sin saldo')
                saldo_disponible = 0

            else:
                saldo_disponible = saldo_disponible - dinero
                print(f'Retiro Exitoso. Te quedan ${saldo_disponible}')

            seguir = input('Seguis? Si/No: ').lower()

            if seguir == 'no':
                break

        break

    else:
        print('Datos Incorrectos')

    if i == 2:
        print('Datos Incorrectos, Tarjeta Bloqueada')