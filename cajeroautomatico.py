SaldoDisponible= 10500
retiro = float(input('Que cantidad de dinero deseas retirar: '))
resultado= SaldoDisponible - retiro
if retiro <= 0:
    print('Cantidad Invalida')
elif retiro < SaldoDisponible:
    print(f'Retiro Exitoso. Te quedan ${resultado}')
elif retiro > SaldoDisponible:
    print('Saldo Insuficiente')
elif retiro == SaldoDisponible:
    print('Retiro exitoso, te quedaste sin saldo')