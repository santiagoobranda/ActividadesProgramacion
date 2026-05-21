numero = int(input('Ingrese numero para sacar factorial: '))

def sacar_factorial(num):
    if num <= 0:  #linea 4 y 5 se tiene q parar la recursividad
        return 1
    else:
        return num * sacar_factorial(num - 1)
    
resultado = sacar_factorial(numero)
print(resultado)