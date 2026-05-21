UsuarioRegistrado= 'jorge123'
ContraseñaRegistrada= '1432'

for i in range (3):
    Usuario= input('Ingresa tu nombre de usuario: ')
    Contraseña= input('Ingresa tu contraseña: ')

    if Usuario == UsuarioRegistrado and Contraseña == ContraseñaRegistrada:
        print('Bienvenido')
        break
    else:
        print('Datos Incorrectos')

if i == 2:
    print('Cuenta Bloqueada')
