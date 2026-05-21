def contar_letra(cadena, letra):
    contador = 0
    for i in cadena:
        if i == letra:
            contador += 1

    return contador


texto = input("Ingrese una palabra o frase: ")
letra = input("Ingrese una letra: ")
resultado = contar_letra(texto, letra)
print("La letra aparece:", resultado, "veces")
