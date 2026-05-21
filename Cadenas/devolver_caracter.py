def char_at(cadena, indice):
    if indice < 0 or indice >= len(cadena):
        return "Error: índice inválido"
    return cadena[indice]

texto = input("Ingrese una palabra: ")
indice = int(input("Ingrese una posición: "))
print(char_at(texto, indice))
