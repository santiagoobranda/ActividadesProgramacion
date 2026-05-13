def pedir_numero(desde, hasta):
    numero = int(input('Ingrese un numero: '))
    while numero < desde or numero > hasta:
        print('Error. Numero fuera de rango.')
        numero = int(input('Ingrese un numero: '))
    return numero

def realizar_descuento(numero):
    descuento = numero * 0.05
    resultado = numero - descuento
    return resultado

numero1 = pedir_numero(10, 100)
resultado = realizar_descuento(numero1)
print('El numero con descuento es:', resultado)