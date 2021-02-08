def app():

    archivo =open( 'test.txt', 'w' ) # si no existe lo va a generar

    for indice in range( 0, 10 ):
        archivo.write( f'Esta es la linea concatenada mejor { str(indice) } \r\n ' )

    archivo.close()


app()