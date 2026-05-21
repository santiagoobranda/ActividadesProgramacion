def solicitar_entero():
    numero = int(input("Ingrese un número entero: "))
    return numero

resultado = solicitar_entero()
print(f"El número entero ingresado es: {resultado}")