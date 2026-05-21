def ver_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input('Ingrese un numero: '))
resultado = ver_par(numero)
print(resultado)
