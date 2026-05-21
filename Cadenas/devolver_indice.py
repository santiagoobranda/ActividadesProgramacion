def encontrar_indice_caracter(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i  
            
    return -1  

texto_input = input("Ingrese una cadena de texto: ")
buscar_caracter = input("Ingrese el carácter que desea buscar: ")

if len(buscar_caracter) == 1:
    indice = encontrar_indice_caracter(texto_input, buscar_caracter)
    print(f"Resultado del índice: {indice}")
else:
    print("Error: Debe ingresar solamente un único carácter para buscar.")