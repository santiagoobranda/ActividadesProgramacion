def suprimir_repetidos(cadena):
    if len(cadena) == 0:
        return ""
        
    resultado = cadena[0]
    
    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i - 1]:
            resultado += cadena[i]
            
    return resultado

texto_repetido = input("Ingrese un texto con caracteres repetidos (Ej: Holaaa): ")
texto_filtrado = suprimir_repetidos(texto_repetido)
print(f"Resultado sin repetidos: {texto_filtrado}")