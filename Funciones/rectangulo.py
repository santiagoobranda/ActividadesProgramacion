def calcular_area_rectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
resultado = calcular_area_rectangulo(base, altura)
print(f"El área del rectángulo es: {resultado}")