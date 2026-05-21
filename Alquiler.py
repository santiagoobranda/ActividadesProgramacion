total_bruto = 0
total_final = 0
contador_auto = 0
contador_camioneta = 0
contador_moto = 0
max_dias = 0
cliente_mas_dias = ''
suma_km = 0
contador_alquileres = 0
km_auto = 0
km_camioneta = 0
km_moto = 0
contador_tarjeta = 0
max_importe = 0
cliente_mayor_importe = ''
total_km_general = 0

seguir = 'si'



while seguir == 'si':
    nombre = input('Nombre del cliente: ')
    tipo = input('Tipo de vehículo (auto/camioneta/moto): ')
    dias = int(input('Días de alquiler: '))
    precio_dia = float(input('Precio por día: '))
    km = int(input('Kilómetros recorridos: '))
    pago = input('Forma de pago (efectivo/tarjeta/transferencia): ')
    frecuente = input('Cliente frecuente (si/no): ')

    while dias < 1 or dias > 30:
        dias = int(input('Días inválidos, reingrese: '))

    while precio_dia <= 0:
        precio_dia = float(input('Precio inválido, reingrese: '))

    while km < 0 or km > 5000:
        km = int(input('KM inválidos, reingrese: '))

    costo = dias * precio_dia
    total_bruto += costo

    if tipo == 'camioneta':
        costo = costo * 1.2

    if frecuente == 'si':
        costo = costo * 0.85

    total_final += costo

    if tipo == 'auto':
        contador_auto += 1
        km_auto += km
    elif tipo == 'camioneta':
        contador_camioneta += 1
        km_camioneta += km
    else:
        contador_moto += 1
        km_moto += km

    if dias > max_dias:
        max_dias = dias
        cliente_mas_dias = nombre

    suma_km += km
    contador_alquileres += 1

    total_km_general += km

    if pago == 'tarjeta':
        contador_tarjeta += 1

    if costo > max_importe:
        max_importe = costo
        cliente_mayor_importe = nombre

    seguir = input('¿Seguir cargando? (si/no): ')



if total_km_general > 20000:
    total_final = total_final * 1.1

print('Total bruto:', total_bruto)
print('Total final:', total_final)

if contador_auto > contador_camioneta and contador_auto > contador_moto:
    print('Más alquilado: auto')
elif contador_camioneta > contador_moto:
    print('Más alquilado: camioneta')
else:
    print('Más alquilado: moto')

print('Cliente con más días:', cliente_mas_dias)

if contador_alquileres > 0:
    print('Promedio KM:', suma_km / contador_alquileres)

if km_auto > km_camioneta and km_auto > km_moto:
    print('Más KM: auto')
elif km_camioneta > km_moto:
    print('Más KM: camioneta')
else:
    print('Más KM: moto')

print('Pagos con tarjeta:', contador_tarjeta)
print('Mayor importe:', cliente_mayor_importe, max_importe)