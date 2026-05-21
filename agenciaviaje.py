nombre1= input('ingrese su nombre')
edad1= int(input('ingrese su edad'))
peso1= float(input('ingrese su peso'))
nombre2= input('ingrese su nombre')
edad2=int(input('ingrese su edad'))
peso2= float(input('ingrese su peso'))
sumapesos= peso1+peso2
promedioedad= (edad1+edad2)/2
preciokilo= (peso1*1000)+(peso2*1000)
print(f'Hola, {nombre1}, y, {nombre2}, sus pesos son {peso1} y {peso2} kilos respectivamente, y sumados da, {sumapesos} kilos, el promedio de edad es {promedioedad} años, y su viaje vale, {preciokilo} pesos')