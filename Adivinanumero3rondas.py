NumeroRandom1 = 1
numero = int(input('Adivina el Numero del 1 al 10: '))

while numero != NumeroRandom1:
    print('Incorrecto')
    numero = int(input('Adivina el 1er Numero del 1 al 10: '))
else:
    print('Correcto')

NumeroRandom2 = 5
numero = int(input('Adivina el 2do Numero del 1 al 10: '))

while numero != NumeroRandom2:
    print('Incorrecto')
    numero = int(input('Adivina el 2do Numero del 1 al 10: '))
else:
    print('Correcto')

NumeroRandom3 = 10
numero = int(input('Adivina el 3er Numero del 1 al 10: '))

while numero != NumeroRandom3:
    print('Incorrecto')
    numero = int(input('Adivina el 3er Numero del 1 al 10: '))
else:
    print('Correcto, Ganaste!')