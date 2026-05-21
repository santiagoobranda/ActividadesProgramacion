def sumar_naturales(numero: int) -> int:
    if numero <= 1:
        return numero
    return numero + sumar_naturales(numero - 1)

numero = int(input('Ingrese un numero: '))
resultado = sumar_naturales(numero)
print('La suma es:', resultado)
