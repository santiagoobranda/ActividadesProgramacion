ContraseñaCorrecta= ('1234')
contraseña= input('Ingresa la Contraseña: ')
while contraseña != ContraseñaCorrecta:
    print('Contrsaeña incorrecta')
    contraseña= input('Ingresa la Contraseña: ')
if contraseña== ContraseñaCorrecta:
    print ('Contraseña Correcta')