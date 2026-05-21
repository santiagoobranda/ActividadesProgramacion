def pedir_numero(mensaje):
    num = float(input(mensaje))
    while num <= 0:
        num = float(input('Error, ingrese numero mayor a 0: '))
    return num


def calculo_total(precio, cantidad):
    return precio * cantidad


def descuento_aplicado(total):
    if total > 200:
        descuento = 0.20
    else:
        descuento = 0

    precio_final = total - (total * descuento)
    return precio_final


precio = pedir_numero('ingrese precio: ')
cantidad = pedir_numero('ingrese cantidad: ')
total = calculo_total(precio, cantidad) 
precio_final = descuento_aplicado(total) 
print("Precio final: ", precio_final)