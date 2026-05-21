# Ingresar Datos
edad = int(input('Ingrese su edad: '))
while edad <= 0:
    print('Edad invalida, introducir edad mayor a 0')
    edad = int(input('Ingrese su edad: '))


ingresos_familiares = int(input('Ingrese sus ingresos familiares: '))
while ingresos_familiares <= 0:
    print('Ingresos invalidos, deben ser mayor a 0')
    ingresos_familiares = int(input('Ingrese sus ingresos familiares: '))


materias_aprobadas = int(input('Materias aprobadas: '))
while materias_aprobadas <= 0:
    print('Cantidad de materias invalidad, deben ser mayor a 0')
    materias_aprobadas = int(input('Materias aprobadas: '))


total_materias = int(input('Cantidad total de materias: '))
while total_materias <= 0 or total_materias < materias_aprobadas:
    print('Total de materias invalidas')
    total_materias = int(input('Cantidad total de materias: '))


promedio = materias_aprobadas / total_materias * 10


mensaje = 'No recibe beca'

# Calculo Datos
if promedio >= 8.5 and ingresos_familiares < 300000 and edad < 18:
    mensaje = "Recibe Beca completa"

elif (7 <= promedio <= 8 and edad < 18) or (promedio >= 8.5 and ingresos_familiares >= 300000):
    mensaje = "Recibe Media beca"

elif ingresos_familiares < 200000 and promedio >= 6 and edad <= 18:
    mensaje = "Recibe Beca con ayuda económica"

print (mensaje)

# Evitar que la maquina se rompa si alguien pone 0 materias, 0 de edad, etc.
# hacerla mas legible.