contador = 0
peso_total = 0
precio_total = 0
precio_max = 0
peso_animal = 0
variedad_mas_cara = ''
flag = True

while contador < 10:
    peso = int(input('Ingrese el peso del producto: '))
    if peso < 10 or peso > 100:
        peso = int(input("Ingrese peso valido: "))

    precio_kilo = float(input('Ingrese el precio por kilo: '))
    if precio_kilo <= 0:
        precio_kilo = float(input('Ingrese el precio valido: '))
    
    variedad = input('Que tipo de producto (vegetal/animal/mezcla) es: ')
    if variedad != 'vegetal' and variedad != 'animal' and variedad != 'mezcla':
        variedad = input('Ingrese tipo valido: ')

    
    peso_total += peso
    precio_total += peso * precio_kilo

    
    if variedad == 'animal':
        peso_animal += peso

  
    if flag:
        precio_max = precio_kilo
        variedad_mas_cara = variedad
        flag = False
    else:
        if precio_kilo > precio_max:
            precio_max = precio_kilo
            variedad_mas_cara = variedad

    contador += 1


importe_bruto = precio_total


if peso_total > 300:
    descuento = 0.25
elif peso_total > 100:
    descuento = 0.15
else:
    descuento = 0

importe_final = importe_bruto - (importe_bruto * descuento)


porcentaje_animal = (peso_animal / peso_total) * 100


promedio_precio = precio_total / peso_total


print('\nRESULTADOS:')
print('Importe bruto:', importe_bruto)
print('Importe con descuento:', importe_final)
print('Variedad más cara:', variedad_mas_cara)
print('Promedio precio por kilo:', promedio_precio)
print('Porcentaje de animal:', porcentaje_animal)