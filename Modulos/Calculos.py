def obtener_promedio_individual(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def obtener_estado_alumno(n1, n2, n3):
    if n1 >= 6 and n2 >= 6 and n3 >= 6:
        return 'Aprobado'
    else:
        return 'Desaprobado'

def calcular_porcentaje(aprobados, total):
    if total == 0:
        return 0
    return (aprobados / total) * 100

def calcular_promedio_grupal(suma_total, total_alumnos):
    if total_alumnos == 0:
        return 0
    return suma_total / (total_alumnos * 3)