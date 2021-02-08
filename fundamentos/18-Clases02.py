class Restaurant:

    #Constructor el se ejecuta una vez se crea la instancia de una clase, por lo tanto podemos pasarle argumentos al momento de instaciar la clase.
    def __init__( self, nombre, categoria, precio ):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # def agregar_restaurant( self, nombre ):
    #     self.nombre = nombre

    def mostrar_infomracion( self ):
        print( f'Nombre: {self.nombre},{ self.categoria }, { self.precio }' )


restaurant: Restaurant

restaurant = Restaurant( 'Pizzeria mexico' , 'Pasta mexicana', 150 )
restaurant.mostrar_infomracion()



# restaurant.agregar_restaurant( 'Pizzeria Mexico bonito' )

# restaurantDos = Restaurant()
# restaurantDos.agregar_restaurant( 'hamburguesas python' )

#  restaurant.mostrar_infomracion()
