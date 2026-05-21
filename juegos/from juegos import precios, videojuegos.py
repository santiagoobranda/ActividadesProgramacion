from precios import precios, juegos


def mostrar_precios():
    print("LISTA DE PRECIOS")
    for i in range(len(precios)):
        print(i, "- $", precios[i])


def buscar_caro():
    mayor = precios[0]
    for j in precios:
        if j > mayor:
            mayor = j
    print("El precio más caro es: $", mayor)


def agregar_juego(nombre, precio):
    juegos.append([nombre, precio])
    precios.append(precio)
    print("Juego agregado correctamente.")



def eliminar_precio():
    mostrar_precios()
    indice = int(input("Ingrese el índice a eliminar: "))
    if indice >= 0 and indice < len(precios):
        precios.pop(indice)
        juegos.pop(indice)
        print("Precio eliminado correctamente.")
    else:
        print("Índice inválido.")



def ver_menu():
    ejecutando = True
    while ejecutando:

        print("MENÚ")
        print("1 - Ver todos los precios")
        print("2 - Ver precio más caro")
        print("3 - Agregar juego nuevo")
        print("4 - Eliminar precio por índice")
        print("0 - Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_precios()

        elif opcion == "2":
            buscar_caro()

        elif opcion == "3":
            nombre = input("Ingrese el nombre del juego: ")
            precio = int(input("Ingrese el precio: "))
            agregar_juego(nombre, precio)
            

        elif opcion == "4":
            eliminar_precio()
            mostrar_precios()
        elif opcion == "0":
            print("Programa finalizado.")
            ejecutando = False

        else:
            print("Opción inválida.")

ver_menu()