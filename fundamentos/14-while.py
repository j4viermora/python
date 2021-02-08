pregunta = 'Dime un numero y te diré si es par o impar \r\n'
pregunta += '(Escribe "cerrar" para terminar el juego) \r\n'

start = True

while start:

    numero = input( pregunta )

    if numero == "cerrar":
        start = False
    else:
        numero = int( numero )

        if numero % 2 == 0:
            print(' el numero es par')
        else:
            print( 'el numero es impar' )