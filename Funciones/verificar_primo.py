def es_primo(numero):
    if numero < 2:
        return False
    divisores = 0
    for j in range(1, numero + 1):
        if numero / j == numero // j:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False

num = int(input("Ingrese un número para saber si es primo: "))
if es_primo(num):
    print(True)
else:
    print(False)