numero = int(input("Ingrese un número: "))
cantidad_primos = 0
for i in range(1, numero + 1):
    divisores = 0
    for j in range(1, i + 1):
        if i / j == i // j:
            divisores += 1
    if divisores == 2:
        print(i)
        cantidad_primos += 1

print("Cantidad de primos:", cantidad_primos)
