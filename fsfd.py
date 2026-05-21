def pedir_numero(mensaje):
    num = int(input(mensaje))
    while num < 10 or num > 100:
        num = int(input("Error. Ingrese un número entre 10 y 100: "))
    return num


def pedir_operacion():
    ope = input("Ingrese operación ('s' para sumar, 'r' para restar): ")
    while ope != 's' and ope != 'r':
        ope = input("Error. Ingrese 's' o 'r': ")
    return ope


def calcular(num1, num2, operacion):
    if operacion == 's':
        return num1 + num2
    else:
        return num1 - num2



numero1 = pedir_numero("Ingrese número 1: ")
numero2 = pedir_numero("Ingrese número 2: ")
operacion = pedir_operacion()

resultado = calcular(numero1, numero2, operacion)

print(resultado)