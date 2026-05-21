def ver_entero(cadena):
    es_numero = True
    for caracter in cadena:
        if caracter < "0" or caracter > "9":
            es_numero = False
    return es_numero


texto = input("Ingrese un valor: ")
print(ver_entero(texto))