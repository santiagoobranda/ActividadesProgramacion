contador_alta = 0
contador_baja = 0
peso_gesell = 0
dias_madryn = 0
dias_gesell = 0
dias_cordoba = 0
suma_importes_total = 0

while True:
    nombre = input('Ingresar nombre del titular: ')

    lugar = input('Ingrese destino (Puerto Madryn, Villa Gessel o Córdoba): ')
    while lugar != 'puerto madryn' and lugar != 'villa gesell' and lugar != 'cordoba':
        lugar = input('Error, Ingrese un lugar válido: ')

    temporada = input('Temporada baja o alta: ')
    while temporada != 'alta' and temporada != 'baja':
        temporada = input('Error, Ingrese alta o baja: ')

    dias = int(input('Cuantos dias dura el viaje: '))

    importe = float(input("Importe del viaje: "))

    altura = float(input('Ingrese altura del pasajero: '))

    peso =  float(input('Ingrese peso del pasajero: '))

    sexo = input('f, m, nb')
    while sexo != 'f' and sexo != 'm' and sexo != 'nb':
        sexo = input("Error, Ingrese f, m o nb: ")

    equipaje = input('Tiene equipaje de mano (si/no): ')

    pago = input('Con que paga (mercado , tarjeta o efectivo): ')
    while pago != 'mercado' and pago != 'tarjeta' and pago != 'efectivo':
        pago = input("Error, Medio inválido: ")

    if temporada == 'alta':
        contador_alta += 1
    else:
        contador_baja += 1
        
    if lugar == 'villa gesell':
        peso_gesell += peso
        
    if lugar == 'puerto madryn':
        dias_madryn += dias
    elif lugar == 'villa gesell':
        dias_gesell += dias
    else: 
        dias_cordoba += dias
        
    suma_importes_total += importe

    seguir = input('Cargar otra estadía? (si/no): ')
    if seguir == 'no':
        break


if dias_madryn > dias_gesell and dias_madryn > dias_cordoba:
    lugar_mas_dias = 'Puerto Madryn'
elif dias_gesell > dias_madryn and dias_gesell > dias_cordoba:
    lugar_mas_dias = 'Villa Gesell'
elif dias_cordoba > dias_madryn and dias_cordoba > dias_gesell:
    lugar_mas_dias = 'Córdoba'

print(f'Personas en temporada Alta: {contador_alta}')
print(f'Personas en temporada Baja: {contador_baja}')
print(f'Peso acumulado en Villa Gesell: {peso_gesell} kg')
print(f'Lugar con más días acumulados: {lugar_mas_dias}')
print(f'Suma total de importes: {suma_importes_total}')