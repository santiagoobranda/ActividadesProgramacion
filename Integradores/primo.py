numero = int(input("Ingrese un número: "))
contador = 0
for i in range(1, numero + 1):
    if numero / i == numero // i:
        contador += 1
if contador == 2:
    print("Es primo")
else:
    print("No es primo")
