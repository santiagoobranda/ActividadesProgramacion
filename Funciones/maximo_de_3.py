def maximo_de_tres(n1, n2, n3):
    mayor = n1
    if n2 > mayor:
        mayor = n2
    if n3 > mayor:
        mayor = n3
    return mayor

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor_num = maximo_de_tres(num1, num2, num3)
print(f"El número más grande es: {mayor_num}")