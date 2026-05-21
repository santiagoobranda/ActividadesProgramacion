from precios import precios, juegos

ejecutando = True

while ejecutando:

    print("\n========== MENÚ ==========")
    print("1 - Ver todos los precios")
    print("2 - Ver precio más caro")
    print("3 - Agregar juego nuevo")
    print("4 - Eliminar precio por índice")
    print("0 - Salir")

    opcion = input("\nIngrese una opción: ")

    if opcion == "1":

        print("\n===== LISTA DE PRECIOS =====")

        for i in range(len(precios)):

            print(i, "- $", precios[i])

    elif opcion == "2":

        mayor = precios[0]

        for precio in precios:

            if precio > mayor:

                mayor = precio

        print("\nEl precio más caro es: $", mayor)

    elif opcion == "3":

        nombre = input("\nIngrese el nombre del juego: ")

        precio = int(input("Ingrese el precio: "))

        precios.append(precio)

        videojuegos.append([nombre, precio])

        print("Juego agregado correctamente.")

    elif opcion == "4":

        print("\n===== LISTA DE PRECIOS =====")

        for i in range(len(precios)):

            print(i, "- $", precios[i])

        indice = int(input("\nIngrese el índice a eliminar: "))

        if indice >= 0 and indice < len(precios):

            precios.pop(indice)

            videojuegos.pop(indice)

            print("Precio eliminado correctamente.")

        else:

            print("Índice inválido.")

    elif opcion == "0":

        print("\nPrograma finalizado.")

        ejecutando = False

    else:

        print("\nOpción inválida.")