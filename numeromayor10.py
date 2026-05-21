PedirNumero= int(input('Ingresa un numero mayor o igual a 10: '))
while PedirNumero < 10:
    print('Incorrecto')
    PedirNumero= int(input('Ingresa un numero mayor o igual a 10: '))
else:
    print(f'Correcto, {PedirNumero} es mayor o igual a 10')