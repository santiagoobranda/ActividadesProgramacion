bc = float(input("Ingrese la medida del lado menor BC en cm: "))
cd = float(input("Ingrese la medida de la diagonal menor CD en cm: "))
da = float(input("Ingrese la medida del lado mayor DA en cm: "))
ab = bc + da
perimetro = (bc * 2) + (da * 2)
varillasporcometa = perimetro + ab + cd
totalvarillas = (varillasporcometa * 10) / 100
area = (ab * cd) / 2
areaconcola = area * 1.10
totalpapel = (areaconcola * 10) / 10000
print('\n Materiales necesarios ')
print("Total de varillas de plastico:", totalvarillas, "metros")
print("Total de papel de alta resistencia:", totalpapel, "metros cuadrados")