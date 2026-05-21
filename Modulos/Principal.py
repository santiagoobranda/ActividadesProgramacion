import Validacion
import Calculos

def iniciar_programa():
    contador_alumnos = 0
    contador_aprobados = 0
    suma_total_notas = 0

    while True:
        nombre = input('Ingrese nombre del alumno (o ''terminado'' para terminar): ')
        if nombre == 'terminado':
            break
        
        edad_ingreso = int(input('Ingrese su edad: '))
        edad = Validacion.validar_edad(edad_ingreso)

        nota_mat = int(input('Ingrese su nota de matematica: '))
        nota_mat = Validacion.validar_nota(nota_mat, 'Matematica')

        nota_lec = int(input('Ingrese su nota de lectura: '))
        nota_lec = Validacion.validar_nota(nota_lec, 'Lectura')

        nota_prog = int(input('Ingrese su nota de programacion: '))
        nota_prog = Validacion.validar_nota(nota_prog, 'Programacion')


