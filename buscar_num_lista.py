def buscar_numero(lista, numero):
    for i in lista:
        if i == numero:
            return True
    return False

numeros = [1, 5, 8, 10]
print(buscar_numero(numeros, 5))