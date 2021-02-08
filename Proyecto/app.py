import os

DIRECTORIO = 'contactos/'
EXTENCION = '.txt'

class Contacto:
   
    def __init__( self, nombre, telefono, categoria, tipo_de_telefono ):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        self.tipo_de_telefono = tipo_de_telefono
    



def app():
    
    crear_directorio()

    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = input( 'Seleccione una opcion: \r\n' )
        opcion = int( opcion )

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Buscar contacto')
            preguntar = False
        elif opcion == 3:
            print('Eliminar contacto')
            preguntar = False
        elif opcion == 4:
            print('Editar contacto contacto')
            preguntar = False
        elif opcion == 5:
            print('Ver un contacto')
            preguntar = False
        else:
            print('Opcióm no valida sigue intentando')



def agregar_contacto():
   
    print( 'Nombre del contacto a agregar:\r\n' )
    nombre_contacto =  input( 'Nombre: ' )

    with open( DIRECTORIO + nombre_contacto + EXTENCION, 'w' ) as archivo:
        
        telefono_contacto = input( 'agrega telefono\r\n' )
        categoria_contacto = input( 'categoria \r\n' )
        tipo = input( 'Tipo de telefono \r\n' )
        
        # instanciar la clase 

        contacto = Contacto ( nombre_contacto, telefono_contacto, categoria_contacto, tipo )

        archivo.write( 'Nombre: '+ contacto.nombre + '\r\n' )
        archivo.write( 'Telefono: '+ contacto.telefono + '\r\n' )
        archivo.write( 'Categoría: '+ contacto.categoria + '\r\n' )
        archivo.write( 'Tipo: '+ contacto.tipo_de_telefono + '\r\n' )

        # mensaje de exito 

        print(' contacto guardado correctamente ')


def mostrar_menu():
    print('Seleccione del menú lo que desea hacer')
    print('1) Agregar contacto')
    print('2) Buscar contacto')
    print('3) Eliminar contacto')
    print('4) Editar contacto' )
    print('5) Ver un contacto' )


def crear_directorio():
    if not os.path.exists( DIRECTORIO ):
        os.makedirs( DIRECTORIO )


app()