numero= int(input('Ingresa un Numero entre 1 y 50: '))
while numero <1 or numero >50:
    print(f'{numero} No esta dentro del rango pedido')
    numero= int(input('Ingresa un Numero entre 1 y 50: '))
print('Bien')