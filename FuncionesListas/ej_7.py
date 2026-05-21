from nombres_ej6 import nombres, telefonos, mails, country, edades, postalZip


def importar_listas():
    return nombres, telefonos, mails, country, edades, postalZip


def usuarios_mexico(nombres, country):
    for i in range(len(nombres)):
        if country[i] == "Mexico":
            print(nombres[i])


def usuarios_brasil(nombres, mails, telefonos, country):
    for i in range(len(nombres)):
        if country[i] == "Brazil":
            print(nombres[i], mails[i], telefonos[i])


def usuarios_mas_jovenes(nombres, edades):
    menor = edades[0]

    for e in edades:
        if e < menor:
            menor = e

    for i in range(len(edades)):
        if edades[i] == menor:
            print(nombres[i], edades[i])


def promedio_edad(edades):
    suma = 0

    for e in edades:
        suma += e

    return suma / len(edades)


def mayor_brasil(nombres, edades, country):
    mayor = -1

    for i in range(len(edades)):
        if country[i] == "Brazil":
            if edades[i] > mayor:
                mayor = edades[i]

    for i in range(len(edades)):
        if country[i] == "Brazil" and edades[i] == mayor:
            print(nombres[i], edades[i])


def mexico_brasil_cp(nombres, country, postalZip):
    for i in range(len(nombres)):
        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:
            print(nombres[i], country[i], postalZip[i])


def italianos_mayores(nombres, mails, telefonos, country, edades):
    for i in range(len(nombres)):
        if country[i] == "Italy" and edades[i] > 40:
            print(nombres[i], mails[i], telefonos[i])
