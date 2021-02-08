# revisar si una revision es mayor a 

balance = 0

if balance > 0:
    print( 'puedes pagar' )
else:
    print('no tienes saldo')

#likes 

likes = 200

if likes >= 200:
    print(f'excelente { likes }')
else:
    print( f'casi llegas a los { likes }')

# para revisar que un lenguaje sea diferente a 

if not likes == 201:
    print('es diferente')
else:
    print( 'son iguales' )

# evaluar boolean

usuario_autenticado = True 


if usuario_autenticado:
    print('acceso al sistema')
else:
    print('acceso denegado')

# evaluar elementor de una lista 

lenguajes = [ 'python',  'kotlin',  'java',  'javascript', 'PHP']

if 'PHP' in lenguajes:
    print('Php es el lenguaje de backend más usado para la web')
else:
    print('no no esta en la lista ')

# if anidados

usuario_autenticado1 = True
usuario_admin =False

if usuario_autenticado1:
    if usuario_admin:
        print('acceso total')
    else:
        print( 'acceso al sistema' )
else:
    print( 'debes iniciar sesión ' )
