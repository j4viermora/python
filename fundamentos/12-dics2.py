# inicar un diccionario vacío
jugador = {  }
print( jugador )

# para asignarle elementos al objeto

jugador['nombre'] = 'javier'
jugador['puntaje'] = 1000
print( jugador )

# reasignar un valoor dell diccionario 

jugador[ 'puntaje' ] = 2000
print(jugador)

# acceder a un element del diccionario 
mensajeDeError = ' no hay un valor que retornar'
jugadoractivo = jugador.get( 'nombre', mensajeDeError)
print(jugadoractivo)

#iterar en el diccionario

for llave, valor in jugador.items():
    print(llave)
    print(valor)
