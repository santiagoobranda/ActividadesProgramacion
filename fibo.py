
def calcular_fibonacci(numero):
    if numero == 1:
        resultado = 1
    elif numero == 0:
        resultado = 0
    else:
        retorno = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
        return retorno
    




numero = int(input('Ingrese numero: '))
resultado = calcular_fibonacci
print(resultado)