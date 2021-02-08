def app():

    with open( 'test.txt' ) as archivo:
        for contenido in archivo:
            print( contenido.rstrip() )

app()