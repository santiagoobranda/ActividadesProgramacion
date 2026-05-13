def pedir_numero(desde, hasta):
    numero = int(input('Ingrese un numero: '))
    while numero < desde or numero > hasta:
        print('Error. Numero fuera de rango.')
        numero = int(input('Ingrese un numero: '))
    return numero

def mostrar_numero(numero):
    print('El numero es:', numero)

valor = pedir_numero(1, 10)
mostrar_numero(valor)