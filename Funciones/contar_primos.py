def es_primo(numero):
    if numero < 2:
        return False
    divisores = 0
    for j in range(1, numero + 1):
        if numero / j == numero // j:
            divisores += 1
    return divisores == 2

def mostrar_todos_los_primos(numero):
    cantidad_primos = 0
    for i in range(1, numero + 1):
        if es_primo(i):
            print(i)
            cantidad_primos += 1     
    return cantidad_primos

numero_ingresado = int(input("Ingrese un número: "))
total_primos = mostrar_todos_los_primos(numero_ingresado)
print("Cantidad de primos:", total_primos)