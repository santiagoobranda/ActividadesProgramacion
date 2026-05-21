def imprimir_tabla(numero, inicio=1, fin=10):
    print(f"--- Tabla del {numero} (Rango: {inicio} al {fin}) ---")
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")

num_tabla = int(input("Ingrese numero del que quiera la tabla: "))

opcion = input("¿Quiere personalizar el rango? (s/n): ").lower()
if opcion == 's':
    rango_inicio = int(input("Ingrese el número de inicio: "))
    rango_fin = int(input("Ingrese el número de fin: "))
    imprimir_tabla(num_tabla, rango_inicio, rango_fin)
else:
    imprimir_tabla(num_tabla) # Usa el rango por defecto del 1 al 10