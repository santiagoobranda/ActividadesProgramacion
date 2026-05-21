numero = int(input("Ingrese un número: "))
contador = 0
for i in range(1, numero + 1):
    if numero / i == numero // i:
        print(i)
        contador += 1
        
print("Cantidad de divisores:", contador)
