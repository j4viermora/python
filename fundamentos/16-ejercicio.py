playlist = {} # diccionario vacío

playlist['canciones'] = [] # lista vacía de canciones


# funcion maestra 

def app():

   agregar_playlist = True

   while agregar_playlist:
        nombre_playlist =input( '¿Como deseas nombrar la playlist?:\n\r' )

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            
            agregar_playlist = False

            agregar_canciones()

def agregar_canciones():
    
    agregar_cancion = True

    while agregar_cancion:
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playlist { nombre_playlist } :\n \r'         
        pregunta += 'Escribe "X" para dejar de agregar canciones:\r\n'

        cancion = input( pregunta )

        if cancion == 'X':

            agregar_cancion = False

            #Mostrar resumen de la playlist 
            mostrar_resumen()

        else:
            playlist['canciones'].append( cancion )

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: { playlist }')
    print( 'Canciones:\r\n' )

    canciones = playlist[ 'canciones' ]

    for cancion in canciones:
        print( cancion )



app()