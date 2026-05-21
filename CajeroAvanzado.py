PIN= '1234'
SaldoDisponible= 10000

for i in range (3):
    IngresePin= input('Ingrese su PIN: ')
    if IngresePin == PIN:
        print(f'Ingresaste, tu saldo es de ${SaldoDisponible}')
        dinero= int(input('Cuanto dinero desea retirar: '))
        resultado= SaldoDisponible - dinero
        if dinero <= 0:
            print('Cantidad Invalida')
        elif dinero < SaldoDisponible:
            print(f'Retiro Exitoso. Te quedan ${resultado}')
        elif dinero > SaldoDisponible:
            print('Saldo Insuficiente')
        elif dinero == SaldoDisponible:
            print('Retiro exitoso, te quedaste sin saldo')

        seguir= input('Seguis? Si/No: ')
        if seguir.lower() == 'no':
            break
    else:
        print('Datos Incorrectos')

if i == 2:
    print ('Datos Incorrectos, Tarjeta Bloqueada')