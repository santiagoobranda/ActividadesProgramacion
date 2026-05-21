def contar_subcadena(cadena, subcadena):
    largo_cadena = len(cadena)
    largo_sub = len(subcadena)
    contador = 0
    
    if largo_sub == 0 or largo_sub > largo_cadena:
        return 0
        
    for i in range(largo_cadena - largo_sub + 1):
        fragmento = cadena[i : i + largo_sub]
        if fragmento == subcadena:
            contador += 1
    return contador

texto_principal = input("Ingrese la cadena principal (Ej: El pan del panadero): ")
texto_buscar = input("Ingrese la subcadena a buscar (Ej: pan): ")
total_coincidencias = contar_subcadena(texto_principal, texto_buscar)
print(f"La subcadena aparece {total_coincidencias} veces.")