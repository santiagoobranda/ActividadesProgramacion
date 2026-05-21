def cargar_rango(minimo, maximo):
    lista = []
    while len(lista) < 10:
        num = int(input(f"Ingrese número entre {minimo} y {maximo}: "))
        if minimo <= num <= maximo:
            lista.append(num)
        else:
            print("Número fuera de rango")
    return lista

lista = cargar_rango(1, 100)
print(lista) 
