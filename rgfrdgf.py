

def pedir_numero(mensaje):
    num = float(input(mensaje))
    while num <= 0:
        num = float(input('Error. Ingrese un valor mayor a 0: '))
    return num


def calcular_total(precio, metros):
    return precio * metros


def aplicar_descuento(total):
    descuento = 0
    if total > 500:
        descuento = 0.20
    elif total > 150:
        descuento = 0.10
    
    
    precio_final = total - calcular_total(total, descuento)
    return precio_final



precio = pedir_numero('Ingrese precio por metro: ') 
metros = pedir_numero('Ingrese cantidad de metros: ') 
total = calcular_total(precio, metros) 
precio_final = aplicar_descuento(total) 
print('Precio final: ', precio_final)