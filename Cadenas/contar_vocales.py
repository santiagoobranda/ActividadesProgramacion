def contar_vocales(cadena):
    texto = cadena.lower()
    matriz_vocales = [
        ["a", 0],
        ["e", 0],
        ["i", 0],
        ["o", 0],
        ["u", 0]
    ]
    
    for fila in matriz_vocales:
        vocal = fila[0]
        for caracter in texto:
            if caracter == vocal:
                fila[1] += 1
                
    return matriz_vocales

texto = input("Ingrese una cadena para contar sus vocales: ")
resultado = contar_vocales(texto)
print("\nResultado:")
for fila in resultado:
    print(f"'{fila[0]}' {fila[1]}")