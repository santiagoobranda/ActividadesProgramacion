from ej_7 import *

def menu():
    datos_cargados = False

    while True:
        print("\n--- MENÚ ---")
        print("1- Importar listas")
        print("2- Usuarios de México")
        print("3- Usuarios de Brasil")
        print("4- Usuarios más jóvenes")
        print("5- Promedio de edad")
        print("6- Mayor de Brasil")
        print("7- México y Brasil con CP > 8000")
        print("8- Italianos mayores de 40")
        print("9- Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            nombres, telefonos, mails, country, edades, postalZip = importar_listas()
            datos_cargados = True
            print("Listas importadas")

        elif not datos_cargados:
            print("Primero debe importar las listas")

        elif opcion == "2":
            usuarios_mexico(nombres, country)

        elif opcion == "3":
            usuarios_brasil(nombres, mails, telefonos, country)

        elif opcion == "4":
            usuarios_mas_jovenes(nombres, edades)

        elif opcion == "5":
            print("Promedio:", promedio_edad(edades))

        elif opcion == "6":
            mayor_brasil(nombres, edades, country)

        elif opcion == "7":
            mexico_brasil_cp(nombres, country, postalZip)

        elif opcion == "8":
            italianos_mayores(nombres, mails, telefonos, country, edades)

        elif opcion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


menu()