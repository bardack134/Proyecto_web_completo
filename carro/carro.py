class Carro:
    #constructor de la clase,  Se ejecuta automáticamente cuando se crea un nuevo objeto de la clase "carrito".
    def __init__(self, request):
        #atributos del constructor, session, request, carro

        #En esta línea, se asigna el valor del parámetro "request" que se recibió en el constructor al atributo "request" del objeto "carro".
        self.request=request

        #Aquí, se asigna el atributo "session" del objeto "request" al atributo "session" del objeto "carro". El atributo "session" es un objeto que representa la sesión actual de Django y se utiliza para almacenar información entre solicitudes HTTP.
        self.session=request.session

        #.get('carro'): get() es un método que se puede utilizar en diccionarios (y en este caso, el objeto de sesión se comporta como un diccionario). Recibe un argumento que es la clave que queremos buscar en el diccionario y devuelve el valor asociado con esa clave. Si la clave no existe en el diccionario, en lugar de arrojar un error, retorna None o un valor predeterminado que se puede proporcionar como segundo argumento de get() (en este caso no se proporciona, por lo que si no encuentra la clave, el valor será None).
        carro=self.session.get('carro')

        #: Esta línea verifica si la variable carro es None o si está vacía (es decir, si no tiene ningún valor). En Python, un valor None, una lista vacía ([]), un diccionario vacío ({}) y otros tipos de datos vacíos se consideran falsos cuando se evalúan en un contexto booleano. Por lo tanto, if not carro: se evaluará como True si carro no tiene un valor.
        if not carro:

        #se está asignando un nuevo diccionario vacío a dos variables al mismo tiempo: carro y self.session['carro'].
        # 
        # Esta linea crea un nuevo diccionario vacío {} y lo asigna a la clave 'carro' dentro del objeto de sesión (self.session).  
            carro=self.session['carro']={}
        
        

        #Con esta linea de codigo siempre se crea el carro independiente de todo lo detras
        self.carro=carro
    
  # Función para agregar productos al carro, recibe 2 parámetros: self y el producto que queremos agregar al carro
    def agregar(self, producto):

        # Comprobamos el id del producto que queremos agregar con el id de los productos en el diccionario self.carro.
        # La función keys() nos permite obtener los ids de los productos ya agregados al carro.
        # (self.carro) En este diccionario, se almacenan los productos agregados al carro, donde la clave es el ID del    producto y el valor es otro diccionario que contiene información del producto.

        if str(producto.id) not in self.carro.keys():
            # Si el id del producto no está en el diccionario self.carro, significa que el producto no ha sido agregado     previamente al carro.
            # En ese caso, añadimos el producto al carro en forma de un diccionario con la siguiente información:
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        
        # Si el producto ya se encuentra en el carro,  Es decir, el ID del producto ya está presente en las claves del diccionario self.carro.
        else:
            # Un bucle que recorre todas las clave, valor del diccionario self.carro
            for key, value in self.carro.items():

                #Por cada iteración del bucle, se verifica si la clave del diccionario (key) coincide con el ID del producto que queremos agregar (str(producto.id)).
                if key==str(producto.id):

                    # Incrementamos la cantidad del producto en 1, ya que el producto ya existe en el carro.
                    #Esto se hace actualizando el valor correspondiente en el diccionario self.carro. La cantidad del producto se encuentra dentro del diccionario interno bajo la clave "cantidad".
                    value["cantidad"]=value["cantidad"]+1

                    # Suma el precio actual del producto almacenado en el diccionario "value" con el precio del producto "producto" y actualiza el campo "precio" en el diccionario "value".
                    value["precio"] = float(value["precio"]) + producto.precio


                    # Rompemos el bucle, ya que hemos encontrado el producto en el carro y ya hemos actualizado la cantidad
                    break
                
        # Llamamos al método guardar_session() para guardar los cambios en la sesión
        self.guardar_carro()


    # Función que nos permite guardar la sesión
    def guardar_carro(self):
        # Guardamos el diccionario self.carro en la sesión con la clave 'carro'
        #Esto asegura que los datos del carro se conserven entre las solicitudes HTTP y estén disponibles para el usuario en futuras interacciones con la aplicación.
        self.session['carro'] = self.carro

        # Indicamos que la sesión ha sido modificada, para asegurarnos de que los cambios se guarden correctamente

        #Esta configuración es necesaria para que Django sepa que se han realizado cambios en la sesión y que estos cambios deben ser guardados en el almacenamiento persistente (por ejemplo, en una base de datos o en la memoria del servidor) al finalizar la solicitud HTTP. Si no establecemos self.session.modified = True, los cambios en la sesión podrían no guardarse correctamente.
        self.session.modified = True


    # Esta función se encarga de eliminar un producto específico del carro de compras.
    def eliminar(self, producto):

        producto.id=str(producto.id)

        # verifica si el id del producto que queremos eliminar está presente como una clave en el diccionario self.carro. Si es así, significa que el producto está en el carro y podemos proceder a eliminarlo.
        if  producto.id in self.carro:

            # Si el producto está en el carro, lo eliminamos usando la función `del`
            #Usamos str(producto.id) como clave para acceder al elemento específico en el diccionario y eliminarlo.
            del self.carro[producto.id]

            # Guardamos los cambios en la sesión después de eliminar el producto
            #Esto asegura que los cambios en el carro se conserven y estén disponibles en futuras interacciones del usuario con la aplicación.
            self.guardar_carro()

    def restar_producto(self, producto):
            
        # Un bucle que recorre todas las clave, valor del diccionario self.carro
            for key, value in self.carro.items():

                #Por cada iteración del bucle, se verifica si la clave del diccionario (key) coincide con el ID del producto que queremos agregar (str(producto.id)).
                if key == str(producto.id):

                    # disminuimos la cantidad del producto en 1, ya que el producto ya existe en el carro.
                    #Esto se hace actualizando el valor correspondiente en el diccionario self.carro. La cantidad del producto se encuentra dentro del diccionario interno bajo la clave "cantidad".
                    value["cantidad"] = value["cantidad"] - 1

                    # Resta el precio actual del producto almacenado en el diccionario "value" con el precio del producto llamado "producto" y actualiza el campo "precio" en el diccionario "value".
                    value["precio"] = float(value["precio"]) - producto.precio

                    if value["cantidad"]<1:

                        self.eliminar(producto)
                     

                    # Rompemos el bucle, ya que hemos encontrado el producto en el carro y ya hemos actualizado la cantidad
                    break

            # Guardamos los cambios en la sesión después de eliminar el producto
            #Esto asegura que los cambios en el carro se conserven y estén disponibles en futuras interacciones del usuario con la aplicación.
            self.guardar_carro()


    # Con esta función buscamos eliminar todos los productos que se encuentren en el carro de compras
    def limpiar_carro(self):
        # Vaciamos el diccionario `self.carro` asignándole un diccionario vacío
        self.session['carro'] = {}
    
        # Esta configuración es necesaria para que Django sepa que se han realizado cambios en la sesión y que estos    cambios deben ser guardados en el almacenamiento persistente (por ejemplo, en una base de datos o en la memoria    del servidor) al finalizar la solicitud HTTP. Si no establecemos `self.session.modified = True`, los cambios en    la sesión podrían no guardarse correctamente.
        self.session.modified = True







    






