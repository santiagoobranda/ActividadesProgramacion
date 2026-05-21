def verificar_par_impar_mensaje(numero):
    if (numero // 2) * 2 == numero:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

num = int(input("Ingrese un número para verificar si es par o impar: "))
verificar_par_impar_mensaje(num)