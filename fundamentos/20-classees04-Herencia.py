class Restaurant:

    def __init__( self, nombre, categoria, precio ):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio # Default: public ,  PROTECTED (CON UN GUION BAJO LA CONVERTIMOS), PRIVATE SE LOGRA CON DOBRE GUION BAJO

    def mostrar_infomracion( self ):
        print( f'Nombre: {self.nombre},{ self.categoria }, { self.precio }' )

        #Getters and setters get obtiene y set cambia o pone un valor 

    def get_precio( self ):
        print( self.__precio )

    def set_precio( sel, precio ):
        self.__precio = precio

class Hotel(Restaurant):
    def __init__( self, nombre, categoria, precio ):
        super().__init__( nombre, categoria, precio )

hotel = Hotel( 'Hotel Java', 'Caribeño', 800 )

hotel.mostrar_infomracion()

