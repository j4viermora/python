#nombre = input( '¿cual es tu nombre?: \r\n' )

#print( f'hola {nombre}' )

# leer datos que serán numeros

edad = input( '¿cual es tu edad?: \r\n')

# convertir stg a entero, las entradas de datos siempre vienen como string

edad = int( edad )

if edad >= 18:
    print( 'puedes votar' )
else:
    print('aun no tienes a edad necesaria para botar')

# mezclarlo con operadores
numero = input( 'dime un numero y te dire si es par o no: \r\n' )
numero = int( numero )

if numero % 2 == 0:
    print(' el numero es par')
else:
    print( 'el numero es in par' )