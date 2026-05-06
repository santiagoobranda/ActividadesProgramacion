total_bruto = 0
total_final = 0
total_dias = 0
contador_urgencia = 0
contador_control = 0
contador_cirugia = 0
max_costo = 0
paciente_mas_caro = ''
suma_edades = 0
contador_pacientes = 0
contador_efectivo = 0
contador_tarjeta = 0
contador_transferencia = 0
pacientes_mas_10_dias = 0

seguir = 'si'



while seguir == 'si':
    nombre = input('Nombre del paciente: ')
    edad = int(input('Edad: '))
    
    tipo = input('Tipo de atención (urgencia/control/cirugia): ')
    dias = int(input('Días internado: '))
    costo_dia = float(input('Costo por día: '))
    
    obra_social = input('Tiene obra social (si/no): ')
    pago = input('Forma de pago (efectivo/tarjeta/transferencia): ')

    while edad < 0 or edad > 100:
        edad = int(input('Edad inválida, reingrese: '))

    while dias < 1 or dias > 60:
        dias = int(input('Días inválidos, reingrese: '))

    while costo_dia <= 0:
        costo_dia = float(input('Costo inválido, reingrese: '))

    costo_total = dias * costo_dia
    total_bruto += costo_total

    if obra_social == 'si':
        costo_total = costo_total * 0.8

    total_dias += dias

    if tipo == 'urgencia':
        contador_urgencia += 1
    elif tipo == 'control':
        contador_control += 1
    else:
        contador_cirugia += 1

    if costo_total > max_costo:
        max_costo = costo_total
        paciente_mas_caro = nombre

    suma_edades += edad
    contador_pacientes += 1

    if pago == 'efectivo':
        contador_efectivo += 1
    elif pago == 'tarjeta':
        contador_tarjeta += 1
    else:
        contador_transferencia += 1

    if dias > 10:
        pacientes_mas_10_dias += 1

    total_final += costo_total

    seguir = input('Seguir cargando? (si/no): ')

if total_dias > 500:
    total_final = total_final * 0.9

print('Total bruto:', total_bruto)
print('Total final:', total_final)

print('Urgencia:', contador_urgencia)
print('Control:', contador_control)
print('Cirugia:', contador_cirugia)

print('Paciente más caro:', paciente_mas_caro)

if contador_pacientes > 0:
    print('Promedio edad:', suma_edades / contador_pacientes)

if contador_efectivo > contador_tarjeta and contador_efectivo > contador_transferencia:
    print('Forma de pago más usada: efectivo')
elif contador_tarjeta > contador_transferencia:
    print('Forma de pago más usada: tarjeta')
else:
    print('Forma de pago más usada: transferencia')

print('Pacientes con más de 10 días:', pacientes_mas_10_dias)