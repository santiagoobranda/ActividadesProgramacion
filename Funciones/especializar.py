def solicitar_entero(mensaje="Ingrese un número entero: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: El dato ingresado no es un número entero válido. Intente de nuevo.")

def solicitar_flotante(mensaje="Ingrese un número decimal: "):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: El dato ingresado no es un número decimal válido. Intente de nuevo.")

def solicitar_cadena(mensaje="Ingrese un texto: "):
    while True:
        entrada = input(mensaje).strip()
        if len(entrada) == 0:
            print("Error: El campo no puede quedar vacío. Ingrese algún texto.")
        else:
            return entrada


print("--- Probando ingresos validados ---")
edad = solicitar_entero("Introduce tu edad (entero): ")
precio = solicitar_flotante("Introduce un precio (decimal): ")
nombre = solicitar_cadena("Introduce tu nombre (texto): ")

print(f"\nDatos guardados correctamente:\nNombre: {nombre}\nEdad: {edad}\nPrecio: {precio}")