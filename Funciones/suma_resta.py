def pedir_numero(desde, hasta):
    numero = int(input('Ingrese un numero: '))
    while numero < desde or numero > hasta:
        print('Error. Numero fuera de rango.')
        numero = int(input('Ingrese un numero: '))
    return numero

def pedir_operacion():
    operacion = input('Ingrese una operacion (s = sumar, r = restar): ')
    while operacion != 's' and operacion != 'r':
        print('Error. Operacion invalida.')
        operacion = input('Ingrese una operacion (s = sumar, r = restar): ')
    return operacion

def calcular(numero1, numero2, operacion):
    if operacion == 's':
        resultado = numero1 + numero2
    else:
        resultado = numero1 - numero2
    return resultado

numero1 = pedir_numero(10, 100)
numero2 = pedir_numero(10, 100)
operacion = pedir_operacion()
resultado = calcular(numero1, numero2, operacion)
print('El resultado es:', resultado)
