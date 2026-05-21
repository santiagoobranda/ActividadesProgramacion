total_bruto_acumulado = 0
total_unidades_acumuladas = 0
venta_mas_cara_tarjeta = 0
suma_precios_unitarios = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0


for i in range(25):
    print('--- Registro de la venta numero', i + 1, '---')
    
    
    tipo = input('Ingrese tipo (alimento, limpieza, perfumeria): ')
    while tipo != 'alimento' and tipo != 'limpieza' and tipo != 'perfumeria':
        tipo = input('Error. Reingrese tipo (alimento, limpieza, perfumeria): ')
    
    
    cantidad = int(input('Ingrese cantidad (1 a 20): '))
    while cantidad < 1 or cantidad > 20:
        cantidad = int(input('Error. Reingrese cantidad (1 a 20): '))
        
    
    precio = float(input('Ingrese precio unitario (mayor a 0): '))
    while precio <= 0:
        precio = float(input('Error. Reingrese precio (mayor a 0): '))
        
    
    forma_pago = input('Ingrese forma de pago (efectivo, tarjeta, transferencia): ')
    while forma_pago != 'efectivo' and forma_pago != 'tarjeta' and forma_pago != 'transferencia':
        forma_pago = input('Error. Reingrese forma de pago: ')

    
    subtotal_venta = cantidad * precio
    total_bruto_acumulado = total_bruto_acumulado + subtotal_venta
    total_unidades_acumuladas = total_unidades_acumuladas + cantidad
    suma_precios_unitarios = suma_precios_unitarios + precio

    
    if forma_pago == 'efectivo':
        subtotal_venta = subtotal_venta * 0.95
        contador_efectivo = contador_efectivo + 1
    elif forma_pago == 'tarjeta':
        contador_tarjeta = contador_tarjeta + 1
        
        if subtotal_venta > venta_mas_cara_tarjeta:
            venta_mas_cara_tarjeta = subtotal_venta
    else:
        contador_transferencia = contador_transferencia + 1




descuento_volumen = 0
if total_unidades_acumuladas > 400:
    descuento_volumen = total_bruto_acumulado * 0.20
elif total_unidades_acumuladas > 200:
    descuento_volumen = total_bruto_acumulado * 0.10

importe_final = total_bruto_acumulado - descuento_volumen


promedio_precio = suma_precios_unitarios / 25


if contador_efectivo > contador_tarjeta and contador_efectivo > contador_transferencia:
    forma_mas_usada = 'efectivo'
elif contador_tarjeta > contador_transferencia:
    forma_mas_usada = 'tarjeta'
else:
    forma_mas_usada = 'transferencia'


print('1. Importe total bruto: ', total_bruto_acumulado)
print('2. Importe total final: ', importe_final)
print('3. Venta mas cara con tarjeta: ', venta_mas_cara_tarjeta)
print('4. Promedio de precio unitario: ', promedio_precio)
print('5. Forma de pago mas utilizada: ', forma_mas_usada)