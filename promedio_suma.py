suma = 0
contador = 0

for i in range(10):
    numero = int(input("Ingrese un número: "))

    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador

    print("Suma:", suma)
    print("Promedio:", promedio)

else:
    print("No se ingresaron números.")