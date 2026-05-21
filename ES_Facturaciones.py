print("Sistema de Facturación")
# Ingreso de datos
precio1= int(input(3000 ))
precio2= int(input(2500))
precio3= int(input(1300))

# Calculos
suma= precio1+precio2+precio3
promedio= suma/3
iva= suma*0.21
total_final = suma + iva


# Resultados
print("\n--- Resultados ---")
print("Suma total:", suma)
print("Promedio:", promedio)
print("Total con IVA (21%):", total_final)