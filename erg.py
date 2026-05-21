#Ingreso de datos
def pedir_numero (mensaje):
    num = float(input(mensaje))
    while num <= 0:
        num = float(input('error, ingrese valor mator a 0: '))
    return num

#Calculo de datos
def calcular_total(precio, metros):
    return precio * metros

def aplicar_descuento(total):
    if total 