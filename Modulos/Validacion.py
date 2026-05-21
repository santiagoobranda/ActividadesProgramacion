def validar_edad(edad):
    while edad < 18:
        edad = int(input('Edad invalida, debe ser mayor: '))
    return edad

def validar_nota(nota, materia):
    while nota < 0 or nota > 10:
        nota = int(input(f'Nota de {materia} invalida: '))
    return nota