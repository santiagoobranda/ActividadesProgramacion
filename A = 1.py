contador_jugadores = 0
distancia_maxima = 0
jugador_maximo = 0

while contador_jugadores < 5:
    distancia = int(input("¿A qué distancia pateaste?: "))

    if distancia > distancia_maxima:
        distancia_maxima = distancia
        jugador_maximo = contador_jugadores + 1

    contador_jugadores = contador_jugadores + 1

print("El jugador que pateó más lejos fue:", jugador_maximo)
print(distancia_maxima)