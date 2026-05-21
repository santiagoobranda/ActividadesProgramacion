bc = float(input("Ingrese la medida del lado menor BC: "))
cd = float(input("Ingrese la medida de la diagonal menor CD: "))
da = float(input("Ingrese la medida del lado mayor DA: "))
ab = da + bc
perimetro = (bc * 2) + (da * 2)
varillasporcometa = perimetro + ab + cd
totalvarillasmts = (varillasporcometa * 10) / 100
areacuerpo = (ab * cd) / 2
areaconcola = areacuerpo * 1.10  
totalpapelmts2 = (areaconcola * 10) / 10000
print("\n MATERIALES NECESARIOS PARA 10 COMETAS ")
print("Total de varillas de plástico:", totalvarillasmts, "metros")
print("Total de papel de alta resistencia:", totalpapelmts2, "metros cuadrados")