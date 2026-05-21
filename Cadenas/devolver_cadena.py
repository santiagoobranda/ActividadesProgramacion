def subcadena(cadena, inicio, fin):
    if inicio < 0 or fin >= len(cadena) or inicio > fin:
        return 'Error: índices inválidos'
    resultado = ''
    for i in range(inicio, fin + 1):
        resultado += cadena[i]
    return resultado


texto = input("Ingrese una palabra: ")
inicio = int(input("Ingrese índice inicial: "))
fin = int(input("Ingrese índice final: "))
print(subcadena(texto, inicio, fin))
