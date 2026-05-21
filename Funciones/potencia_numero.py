def calcular_potencia(base, exponente):
    return base ** exponente

base = float(input("Ingrese la base: "))
exp = float(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exp)
print(f"El resultado de la potencia es: {resultado}")