toneladas= float(input('ingrese la cantidad de toneladas necesarias de materiales a transportar'))
kilos= toneladas*1000
import math
cantidadecamiones= math.ceil(kilos/3500)
kilometros= float(input('ingrese la cantidad de kilometros que deben recorrer los camiones'))
tiempo= kilometros/90
print('\n--- Datos Camiones --- ')
print(f'La cantidad de camiones necesarios para mover {toneladas} toneladas, es de {cantidadecamiones}')
print(f'Los camiones llegaran al destino en {tiempo} horas')