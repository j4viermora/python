lenguajes = [ 'python',  'kotlin',  'java',  'javascript']

lenguajes.sort()

aprendiendo = f'estoy aprendiendo { lenguajes[0] }'

print( aprendiendo )

# remplazando valors de un arreglo 

lenguajes[2] = 'PHP'

print( lenguajes )

# agregar valores a una lista 

lenguajes.append('RUBY')
print( lenguajes )

# eliminar de una lista 

del lenguajes[ 0 ]

print( lenguajes )

# eliminar de una lista elimina el ultmo elemento de a lista


lenguajes.pop()
print( lenguajes )


# eliminar una posicion especifica tiene que pasarle un argunemteo al metod pop

lenguajes.pop( 2 )
print( lenguajes )

# eliminar por nombre de elemento de la lista es así 

lenguajes.remove( 'PHP' )
print( lenguajes )