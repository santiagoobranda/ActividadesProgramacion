BC = float(input("Ingrese medida BC (lado menor) en cm: "))
CD = float(input("Ingrese medida CD (diagonal menor) en cm: "))
DA = float(input("Ingrese medida DA (lado mayor) en cm: "))
AB = DA + BC
perimetro = (BC * 2) + (DA * 2)
varillascm = perimetro + AB + CD
area = (AB * CD) / 2
papelcm2 = area + (area * 0.10)
varillastotalcm = varillascm * 10
papeltotalcm2 = papelcm2 * 10
varillasmetros = varillastotalcm / 100
print("\n Materiales para 10 cometas ")
print("Metros de varillas necesarias:", varillasmetros)
print("Centímetros cuadrados de papel necesarios:", papeltotalcm2)