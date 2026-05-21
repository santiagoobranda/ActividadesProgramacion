def hacer_palindromo(palabra):
    palindromo = ''
    for i in range(len(palabra)-1, -1, -1): #si ponemos hola, len vale 4, pero como empieza en 0, la ultima letra esta en indice 3
        palindromo += palabra[i]
    if palabra == palindromo:
        return True
    else:
        return False

palabra = input('Ingrese una palabra: ')
print(hacer_palindromo(palabra))