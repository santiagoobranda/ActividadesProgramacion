def pedir_nombres():
    lista = []
    for i in range(10):
        nombre = input("Ingrese un nombre: ")
        lista.append(nombre)
    return lista

nombres = pedir_nombres()
print(nombres)
