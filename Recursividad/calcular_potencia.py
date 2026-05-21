def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    return base * calcular_potencia(base, exponente - 1)
