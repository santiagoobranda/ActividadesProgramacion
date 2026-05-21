ronda1 = False
ronda2 = False
ronda3 = False


NumeroSecreto1 = 10

for z in range(3):
    numero = int(input('Adivina el 1er Numero del 1 al 10: '))
    if numero == NumeroSecreto1:
        print('Correcto')
        ronda1 = True
        break
    else:
        print('Incorrecto')


NumeroSecreto2 = 4

for y in range(3):
    numero = int(input('Adivina el 2do Numero del 1 al 10: '))
    if numero == NumeroSecreto2:
        print('Correcto')
        ronda2 = True
        break
    else:
        print('Incorrecto')


NumeroSecreto3 = 7

for v in range(3):
    numero = int(input('Adivina el 3er Numero del 1 al 10: '))
    if numero == NumeroSecreto3:
        print('Correcto')
        ronda3 = True
        break
    else:
        print('Incorrecto')


print("Resultados:")

if ronda1:
    print("Ronda 1 acertada")
else:
    print("Ronda 1 fallada")

if ronda2:
    print("Ronda 2 acertada")
else:
    print("Ronda 2 fallada")

if ronda3:
    print("Ronda 3 acertada")
else:
    print("Ronda 3 fallada")