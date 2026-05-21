def calcular_area_circulo(radio):
    return 3.14 * (radio ** 2)


radio = float(input("Ingrese el radio del círculo: "))
resultado = calcular_area_circulo(radio)
print(f"El área del círculo es: {resultado}")