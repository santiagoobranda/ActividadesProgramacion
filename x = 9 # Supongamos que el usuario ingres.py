materias = int(input("Ingrese el número de materias del semestre: "))
promedio = float(input("Ingrese su promedio de calificaciones: "))
desempeno = input("Ingrese su tipo de desempeño (alto/medio/bajo): ")

horas_estudio = 0

if materias > 5:
    horas_estudio = 1

if promedio >= 8 and desempeno == "alto":
    horas_estudio = 5
elif promedio < 8 and desempeno == "medio":
    horas_estudio = 7
elif desempeno == "bajo":
    horas_estudio = 10

total_horas = horas_estudio * materias

print(f"Debe estudiar {horas_estudio} horas por materia por semana.")
print(f"El total de horas de estudio por semana es {total_horas}.")