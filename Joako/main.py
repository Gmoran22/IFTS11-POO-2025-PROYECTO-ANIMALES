'''1. Clase Perro
● Atributos: nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado
('disponible', 'reservado', 'adoptado'), temperamento, id.
● Métodos: cambiar estado, mostrar información, etc.'''

class Perro(object):
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.id = id
        
    def cambiarEstado(self,nuevo_estado):
        if nuevo_estado in ["disponible", "reservado", "adoptado"]:
            self.estado = nuevo_estado
            print("Estado actualizado")
        else:
            print("Estado inválido") 
    
    def mostrar_informacion(self):
        """
        es para mostrar la informacion del perro en la consola
        
        ejemplo para usarlo:
            perro.mostrar_informacion()
        """
        return {
        "Nombre": self.nombre,
        "Raza": self.raza,
        "Edad": self.edad,
        "Tamaño": self.tamaño,
        "Peso": self.peso,
        "Estado salud": self.estado_salud,
        "Vacunado": self.vacunado,
        "Estado": self.estado,
        "Temperamento": self.temperamento,
        "ID": self.id,
    }


'''2.Clase UsuarioAdoptante
● Atributos: nombre, dni, email, preferencias (raza, edad, tamaño),
historial_adopciones.
● Métodos: registrarse, modificar datos, ver historial, etc.'''

class UsuarioAdoptante(object):
    
    def __init__(self, preferencias=None, historial_adopciones=None):
        """
        Pongo los datos con None porque en teoria todavia el usuario no se registro, entonces no hay datos"
        
        """
        
        self.nombre = None
        self.apellido = None
        self.dni = None
        self.email = None
        self.telf = None
        self.preferencias = preferencias or []
        self.historial_adopciones = historial_adopciones or []
        
    def registrarse(self, nombre, apellido, dni, email, telf):
        """ pongo que cuando se registre la persona, si no llenaron todos los campos
        salte un error y que tenga que llenar todos los datos para poder registrarse.
        
        Con el return te da un diccionario con todos los datos del usuario.
        
        Para usarlo seria por ej:
        usuario.registrarse("Joaquin", "Fernandez, "47573299", "joaquinfernandezds@gmail.com, "1144005923")"""
        
        if not all ([nombre, apellido, dni, email, telf]):
            raise ValueError("Llenar todos los campos")
        
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telf = telf
        
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "email": self.email,
            "telf": self.telf,
        }
        
    def modificar_datos(self, nuevo_nombre=None, nuevo_apellido=None, nuevo_telf=None, nuevo_dni=None, nuevo_email=None):
        """ modifico los datos del usuario, actualizo sus atributos.
        Si hay un nuevo valor para algun atributo, se actualiza y retorna un mensaje diciendo que fueron modificados, y si no se pasa
        un valor, los datos no se modifican.
        
        Por defecto los datos son None
        
        por ej para usarlo seria:
        usuario.modificar_datos(nuevo_nombre="Pepocho", nuevo_apellido="blablabla", y asi con los otros datos)"""
        
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_apellido:
            self.apellido = nuevo_apellido
        if nuevo_dni:
            self.dni = nuevo_dni
        if nuevo_email:
            self.email = nuevo_email
        if nuevo_telf:
            self.telf = nuevo_telf
        return "Los datos fueron modificados correctamente"

    def datosUsuario(self):
        """organiza los datos del usuario en un diccionario, con su:
        - nombre, apellido, DNI, email
        - preferencias del usuario
        - historial de adopciones
        
        esta bueno para acceder a toda la información del usuario por asi decirlo de manera estructurada
        y reutilizarla en otras partes del programa, como mostrarla en una interfaz
        gráfica o guardarla en una base de datos ponele
        
        para usarlo:
        datos = usuario.datosUsuario()
        print(datos["Nombre"])  # accederia al nombre del usuario"""
        
        datos = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "DNI": self.dni,
            "Email": self.email,
            "Preferencias": self.preferencias,
            "Historial de adopciones": self.historial_adopciones,
        }
        return datos
    
