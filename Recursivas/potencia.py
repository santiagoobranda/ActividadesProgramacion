def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    return base * calcular_potencia(base, exponente - 1)

base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
resultado = calcular_potencia(base, exponente)
print('El resultado es:', resultado)
