costo_bruto_total = 0
total_metros = 0
total_costo_metro = 0
flag = True
metros_algodon_minimo = 0
costo_metro_algodon_minimo = 0
contador_lotes = 0
contador_mezcla = 0
contador_primera = 0
contador_generica = 0

while True:
    tipo_tela = input('Ingrese tipo de tela (algodon/poliester/mezcla): ')
    while tipo_tela != 'algodon' and tipo_tela != 'poliester' and  tipo_tela != 'mezcla':
        tipo_tela = input('Dato invalido, Que tipo de tela (algodon/poliester/mezcla): ') 

    metros = float(input('Ingrese cantidad producida de metros (entre 100 y 5000): '))
    while metros <= 100 or metros >= 5000:
        metros = float(input('Ingrese cantidad valida producida de metros (entre 100 y 5000): '))

    costo_metro = float(input('Ingrese costo por metro (mayor a 0): '))
    while costo_metro <= 0:
        costo_metro = float(input('Ingrese costo valido por metro (mayor a 0): '))
    
    calidad = input('Ingrese tipo de tela (primera/generica)')
    while calidad != 'primera' and calidad != 'generica':
        calidad = input('Dato invalido, Que tipo de calidad (primera/generica')
    
    

    contador_lotes += 1
    total_metros += metros
    total_costo_metro += costo_metro

    precio_lote = metros * costo_metro

    if calidad == 'primera':
        precio_lote *= 0.90
        contador_primera += 1
    else:
        contador_generica += 1

    costo_bruto_total += precio_lote

    if tipo_tela == 'algodon':
        if flag == True or metros < metros_algodon_minimo:
            metros_algodon_minimo = metros
            costo_metro_algodon_minimo = costo_metro
            flag = False

    if tipo_tela == 'mezcla':
        contador_mezcla += 1

    continuar = input('ingresar otro lote? (si/no): ')
    if continuar == 'no':
        break


promedio_costo = total_costo_metro / contador_lotes
costo_final = costo_bruto_total

mensaje = ''



if promedio_costo > 50:
    costo_final += (costo_bruto_total * 0.10)
    mensaje += 'recargo del 10%.'

if total_metros > 30000:
    costo_final += (costo_bruto_total * 0.10)
    mensaje += 'recargo del 10%.'



print(f'Costo Total Bruto con descuentos: {costo_bruto_total}')
if mensaje != '':
    print(mensaje)
else:
    print('No se aplicaron recargos adicionales.')
print(f'Costo total final con impuestos: {costo_final}')


if flag == False:
    print(f'Costo por metro del lote de algodón más corto:{costo_metro_algodon_minimo}')
else:
    print('No se ingresaron lotes de algodón.')


porcentaje_mezcla = (contador_mezcla / contador_lotes) * 100
print(f'Porcentaje de lotes de mezcla: {porcentaje_mezcla}%')


if contador_primera > contador_generica:
    print('Se produjeron más lotes de calidad PRIMERA.')
elif contador_generica > contador_primera:
    print('Se produjeron más lotes de calidad GENÉRICA.')
else:
    print('Se produjo la misma cantidad de lotes de Primera y Genérica.')


print(f'Total de lotes de calidad primera: {contador_primera}')