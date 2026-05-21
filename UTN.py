contador_masculino_iot_ia = 0
contador_punto_2 = 0
nombre_masculino_mayor = 'No hubo'
tecnologia_masculino_mayor = 'Ninguna'
edad_masculino_mayor = 0


for i in range(10):
    print('--- Encuesta numero', i + 1, '---')
    
    nombre = input('Ingrese nombre del empleado: ')
    
    edad = int(input('Ingrese edad (no menor a 18): '))
    while edad < 18:
        edad = int(input('Error. Ingrese una edad valida (18 o mas): '))
        
    genero = input('Ingrese genero (Masculino - Femenino - Otro): ')
    while genero != 'Masculino' and genero != 'Femenino' and genero != 'Otro':
        genero = input('Error. Reingrese genero: ')
        
    tecnologia = input('Ingrese tecnologia (IA, RV/RA, IOT): ')
    while tecnologia != 'IA' and tecnologia != 'RV/RA' and tecnologia != 'IOT':
        tecnologia = input('Error. Reingrese tecnologia: ')

   
    if genero == 'Masculino':
        if tecnologia == 'IOT' or tecnologia == 'IA':
            if edad >= 25 and edad <= 50:
                contador_masculino_iot_ia = contador_masculino_iot_ia + 1

   
    if tecnologia != 'IA':
        if genero != 'Femenino' or (edad >= 33 and edad <= 40):
            contador_punto_2 = contador_punto_2 + 1

    
    if genero == 'Masculino':
        if edad > edad_masculino_mayor:
            edad_masculino_mayor = edad
            nombre_masculino_mayor = nombre
            tecnologia_masculino_mayor = tecnologia



porcentaje_punto_2 = (contador_punto_2 / 10) * 100


print('1. Cantidad de hombres (25-50 años) que votaron IOT o IA:', contador_masculino_iot_ia)
print('2. Porcentaje de empleados que cumplen la condicion 2:', porcentaje_punto_2, '%')
print('3. Empleado masculino de mayor edad:')
print('   Nombre:', nombre_masculino_mayor)
print('   Tecnologia:', tecnologia_masculino_mayor)