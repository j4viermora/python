nombre = input( '¿Cual es tu nombre?:\r\n' )
calificacion = 0
mensajeInicial = f'Hola {nombre} contesta a todas las preguntas solo con si o no'  

print( mensajeInicial )

pregunta1 = input( '¿2 es mayor que 1?:\r\n' )
pregunta2 = input( '¿3 es menor que 2?:\r\n' )
pregunta3 = input( '¿2 es mayor que 10?:\r\n' )

respuesta1 = pregunta1.lower()

respuesta2 = pregunta2.lower()

respuesta3 = pregunta3.lower()

#print(respuesta)


if respuesta1 == 'si':
    calificacion += 1
if respuesta2 =='no':
    calificacion += 1
if respuesta3 == 'no' :
    calificacion += 1
else:
    print( 'No es una respuesta valida' )

print( f'Has finalizado el examen {nombre} tu calificacón es: { calificacion }' )

if calificacion >= 2:
    print( 'Felicidades has aprovado el examen' )
else:
    print( f'Lo siento mucho { nombre } no has aprobado el examen' )