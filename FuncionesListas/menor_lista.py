def menores_edades(edades):
    menor = edades[0]
    for e in edades:
        if e < menor:
            menor = e
    return menor



nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio","Eugenia","Soledad","Mario","Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
menor = menores_edades(edades)

for i in range(len(edades)):
    if edades[i] == menor:
        print(nombres[i], edades[i])
