contador_elite_plano = 0
menor_edad = None
nombre_menor = ''
categoria_menor = ''
contador_experto = 0
total_jugadores = 0
suma_edades_avanzado = 0
contador_avanzado = 0
contador_plano = 0
contador_liftado = 0
contador_cortado = 0


seguir = 'si'

while seguir == 'si':
    nombre = input('Ingrese nombre: ')

    edad = int(input('Ingrese edad: '))
    while edad < 0:
        edad = int(input('Error. Reingrese edad: '))

    puntos = int(input('Ingrese puntos: '))
    while puntos < 0 or puntos > 60:
        puntos = int(input('Error. Reingrese puntos: '))

    ganados = int(input('Ingrese partidos ganados: '))
    while ganados < 0 or ganados > 35:
        ganados = int(input('Error. Reingrese partidos ganados: '))

    saque = input('Ingrese tipo de saque (plano/liftado/cortado): ')
    while saque != 'plano' and saque != 'liftado' and saque != 'cortado':
        saque = input('Error. Reingrese saque: ')
    
    categoria = input('Ingrese categoría (elite/experto/avanzado): ')
    while categoria != 'elite' and categoria != 'experto' and categoria != 'avanzado':
        categoria = input('Error. Reingrese categoría: ')

    total_jugadores += 1

    if categoria == 'elite' and saque == 'plano' and edad >= 19 and edad <= 25:
        contador_elite_plano += 1

    if puntos > 50:
        if menor_edad == None or edad < menor_edad:
            menor_edad = edad
            nombre_menor = nombre
            categoria_menor = categoria

    if categoria == 'experto':
        contador_experto += 1

    if categoria == 'avanzado':
        suma_edades_avanzado += edad
        contador_avanzado += 1

    if categoria == 'elite':

        if saque == 'plano':
            contador_plano += 1

        elif saque == 'liftado':
            contador_liftado += 1

        else:
            contador_cortado += 1

    seguir = input('¿Desea ingresar otro jugador? (si/no): ')


print('Cantidad elite con saque plano entre 19 y 25 años:', contador_elite_plano)

if menor_edad != None:
    print('Jugador de menor edad con más de 50 puntos:', nombre_menor)
    print('Categoría:', categoria_menor)

else:
    print('No hay jugadores con más de 50 puntos.')

if total_jugadores > 0:
    porcentaje = contador_experto * 100 / total_jugadores
    print('Porcentaje de expertos:', porcentaje, '%')

if contador_avanzado > 0:
    promedio = suma_edades_avanzado / contador_avanzado
    print('Promedio de edad de avanzados:', promedio)

else:
    print('No hay jugadores avanzados.')

if contador_plano > contador_liftado and contador_plano > contador_cortado:
    print('El saque más usado por elite es: plano')

elif contador_liftado > contador_cortado:
    print('El saque más usado por elite es: liftado')

else:
    print('El saque más usado por elite es: cortado')