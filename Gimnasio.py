total_bruto = 0
total_final = 0
contador_mensual = 0
contador_trimestral = 0
contador_anual = 0
contador_mañana = 0
contador_tarde = 0
contador_noche = 0
max_precio = 0
cliente_mas_caro = ''
suma_precios = 0
contador_ventas = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
menores_18 = 0
total_planes = 0

seguir = 'si'


while seguir == 'si':
    nombre = input('Nombre del cliente: ')
    tipo_plan = input('Tipo de plan (mensual/trimestral/anual): ')
    edad = int(input('Edad: '))
    precio = float(input('Precio del plan: '))
    pago = input('Forma de pago (efectivo/tarjeta/transferencia): ')
    turno = input('Turno (mañana/tarde/noche): ')
    nuevo = input('Es alumno nuevo (si/no): ')

    
    while edad < 12 or edad > 80:
        edad = int(input('Edad inválida, reingrese: '))

    while precio <= 0:
        precio = float(input('Precio inválido, reingrese: '))

    
    total_planes += 1
    total_bruto += precio

    
    if tipo_plan == 'anual':
        precio = precio * 1.15

    
    if nuevo == 'si':
        precio = precio * 0.9

    total_final += precio

    
    if tipo_plan == 'mensual':
        contador_mensual += 1
    elif tipo_plan == 'trimestral':
        contador_trimestral += 1
    else:
        contador_anual += 1

    
    if turno == 'mañana':
        contador_mañana += 1
    elif turno == 'tarde':
        contador_tarde += 1
    else:
        contador_noche += 1

    
    if precio > max_precio:
        max_precio = precio
        cliente_mas_caro = nombre

    
    suma_precios += precio
    contador_ventas += 1

    
    if pago == 'efectivo':
        contador_efectivo += 1
    elif pago == 'tarjeta':
        contador_tarjeta += 1
    else:
        contador_transferencia += 1

   
    if edad < 18:
        menores_18 += 1

    seguir = input('Seguir cargando? (si/no): ')


if total_planes > 50:
    total_final = total_final * 0.95


print('Total bruto:', total_bruto)
print('Total final:', total_final)

print('Mensual:', contador_mensual)
print('Trimestral:', contador_trimestral)
print('Anual:', contador_anual)


if contador_mañana > contador_tarde and contador_mañana > contador_noche:
    print('Turno más elegido: mañana')
elif contador_tarde > contador_noche:
    print('Turno más elegido: tarde')
else:
    print('Turno más elegido: noche')

print('Cliente que pagó más caro:', cliente_mas_caro)

if contador_ventas > 0:
    print('Promedio precios:', suma_precios / contador_ventas)


if contador_efectivo > contador_tarjeta and contador_efectivo > contador_transferencia:
    print('Forma de pago más usada: efectivo')
elif contador_tarjeta > contador_transferencia:
    print('Forma de pago más usada: tarjeta')
else:
    print('Forma de pago más usada: transferencia')

print('Menores de 18:', menores_18)