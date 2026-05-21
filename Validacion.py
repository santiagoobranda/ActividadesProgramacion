
edad = int(input('Ingrese su edad: '))

def validar_edad (edad):
    while edad < 18:
        edad = int(input('Edad invalida, debe ser mayor: '))
    return edad

def validar_nota (nota):
    while nota < 0 and nota > 10:
        nota = int(input('Nota invalida, debe ser entre 0 y 10: '))
    return nota


edad = validar_edad(edad)


nota_mat = int(input('Ingrese su nota de matematica: '))
nota_mat = validar_nota(nota_mat)

nota_lec = int(input('Ingrese su nota de lectura: '))
nota_lec = validar_nota(nota_lec)

nota_prog = int(input('Ingrese su nota de programacion: '))
nota_prog = validar_nota(nota_prog)