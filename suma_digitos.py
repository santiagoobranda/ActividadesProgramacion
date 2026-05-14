def sumar_digitos(numero: int) -> int:
    if numero < 10:
        return numero
    return (numero % 10) + sumar_digitos(numero // 10)

numero = int(input('Ingrese un numero: '))
resultado = sumar_digitos(numero)
print('La suma de los digitos es:', resultado)