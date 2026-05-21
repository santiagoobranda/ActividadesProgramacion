def cargar_lista():
    lista = [0] * 10
    for i in range(5):  
        pos = int(input("Ingrese posición (0-9): "))
        num = int(input("Ingrese número: "))
        if 0 <= pos < 10:
            lista[pos] = num
        else:
            print("Posición inválida")
    return lista

lista = cargar_lista()
print(lista)
