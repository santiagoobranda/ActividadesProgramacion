numero1= float(input('ingrese un numero: '))
numero2= float(input('ingrese otro numero: '))
op= input('ingrese la operacion (+ - / *)')
if op== '+':
    resultado=numero1+numero2
elif op== '-':
    resultado=numero1-numero2
elif op== '/':
    resultado=numero1/numero2
elif op== '*':
    resultado=numero1*numero2
print('Resultado: ', resultado)