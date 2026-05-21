marca= input('ingrese la marca de la lampara: ')
cantidad= int(input('ingrese la cantidad de lamparas: '))
precio= 800
totalpreciosindescuento= precio*cantidad
descuento= 0
if cantidad >= 6:
    descuento= 0.50
elif cantidad == 5:
    if marca == 'argentinaluz':
        descuento= 0.40
    else:
        descuento= 0.30
elif cantidad== 4:
    if marca== 'argentinaluz' or marca== 'felipelamparas':
        descuento= 0.25
    else:
        descuento= 0.20
elif cantidad== 3:
    if marca == 'argentinaluz':
        descuento= 0.15
    elif marca== 'felipelamparas':
        descuento= 0.10
    else:
        descuento= 0.05
preciocondescuento= totalpreciosindescuento - (totalpreciosindescuento*descuento)
descuentoadicional= 0
if preciocondescuento > 4000:
        descuentoadicional= 0.05
        preciocondescuento = preciocondescuento - (preciocondescuento*descuentoadicional)
totalapagar = preciocondescuento
print('\n Recibo ')
print('Marca:', marca)
print('Cantidad de lámparas:', cantidad)
print('Total sin descuento: $', totalpreciosindescuento)
print('Descuento obtenido: $', totalpreciosindescuento * descuento)
print('Descuento adicional: $ ', (totalpreciosindescuento - (totalpreciosindescuento * descuento)) * descuentoadicional)
print('Total a pagar con descuento: $', totalapagar)