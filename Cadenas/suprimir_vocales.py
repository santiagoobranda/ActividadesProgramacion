def suprimir_vocales(cadena):
    resultado = ""
    vocales = "aeiouAEIOU"
    
    for caracter in cadena:
        es_vocal = False
        for v in vocales:
            if caracter == v:
                es_vocal = True
        if not es_vocal:
            resultado += caracter
    return resultado

texto_original = input("Ingrese un texto para remover sus vocales: ")
texto_sin_vocales = suprimir_vocales(texto_original)
print(f"Resultado sin vocales: {texto_sin_vocales}")