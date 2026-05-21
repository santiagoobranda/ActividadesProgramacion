def es_par(numero):
    return numero / 2 == numero // 2

num= int(input("Ingrese un número: "))
if es_par(num):
    print(True)
else:
    print(False)