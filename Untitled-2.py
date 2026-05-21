def mostrar_precios(lista):
    print('LISTADO DE PRECIOS') # Imprime un título estético.
    for i in range(len(lista)):             # 'len(lista)' cuenta cuántos hay. 'range' genera números desde 0 hasta ese total.
        # 'i' es el índice actual.
        # 'lista[i]' es el valor guardado en esa posición.
        print(f'{i}: ${lista[i]}')


def buscar_mas_caro(lista):
    mayor = lista[0]      # "Caja" donde guardamos el más grande. Empezamos con el primero de la lista.
    for j in lista:       # Recorremos cada precio 'j' de la lista.
        if j > mayor:     # ¿Es el precio actual más grande que el que teníamos guardado?
            mayor = j     # Si sí, lo reemplazamos. Ahora este es nuestro nuevo "campeón".
    print('El precio más caro es:', mayor)



def agregar_precio():

    nuevo_precio = int(input('Ingrese nuevo precio: '))

    juegos.precios.append(nuevo_precio)

    print('Precio agregado correctamente')


# --------------------------------
# ELIMINAR PRECIO
# --------------------------------

def eliminar_precio():

    print('\nLISTA DE PRECIOS:\n')

    for i in range(len(juegos.precios)):

        print(i, '-', juegos.precios[i])


    indice = int(input('Ingrese índice a eliminar: '))

    juegos.precios.pop(indice)

    print('Precio eliminado correctamente')


# --------------------------------
# MOSTRAR VIDEOJUEGOS
# --------------------------------

def mostrar_videojuegos():

    print('\nLISTA DE VIDEOJUEGOS:\n')

    for juego in juegos.videojuegos:

        print('Juego:', juego[0])
        print('Precio:', juego[1])
        print('----------------')


# --------------------------------
# AGREGAR VIDEOJUEGO
# --------------------------------

def agregar_videojuego():

    nombre = input('Ingrese nombre del videojuego: ')

    precio = int(input('Ingrese precio: '))

    nuevo_juego = [nombre, precio]

    juegos.videojuegos.append(nuevo_juego)

    print('Videojuego agregado correctamente')


# --------------------------------
# ELIMINAR VIDEOJUEGO POR ÍNDICE
# --------------------------------

def eliminar_videojuego_indice():

    print('\nLISTA DE VIDEOJUEGOS:\n')

    for i in range(len(juegos.videojuegos)):

        print(i, '-', juegos.videojuegos[i][0])


    indice = int(input('Ingrese índice a eliminar: '))

    juegos.videojuegos.pop(indice)

    print('Videojuego eliminado correctamente')


# --------------------------------
# ELIMINAR VIDEOJUEGO POR NOMBRE
# --------------------------------

def eliminar_videojuego_nombre():

    nombre = input('Ingrese nombre del videojuego: ')

    for juego in juegos.videojuegos:

        if juego[0] == nombre:

            juegos.videojuegos.remove(juego)

            print('Videojuego eliminado correctamente')

            break