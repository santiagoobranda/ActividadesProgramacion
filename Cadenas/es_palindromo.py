def es_palindromo(cadena):
    texto_limpio = ""
    for caracter in cadena.lower():
        if caracter != " ":
            texto_limpio += caracter

    texto_invertido = ""
    for i in range(len(texto_limpio) - 1, -1, -1):
        texto_invertido += texto_limpio[i]
        
    return texto_limpio == texto_invertido

frase = input("Ingrese una palabra o frase para verificar si es palíndromo: ")
if es_palindromo(frase):
    print(True)
else:
    print(False)