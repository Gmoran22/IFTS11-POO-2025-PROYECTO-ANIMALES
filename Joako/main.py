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
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Estado salud: {self.estado_salud}")
        print(f"Vacunado: {self.vacunado}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")


'''2.Clase UsuarioAdoptante
● Atributos: nombre, dni, email, preferencias (raza, edad, tamaño),
historial_adopciones.
● Métodos: registrarse, modificar datos, ver historial, etc.'''

class UsuarioAdoptante(object):
    def __init__(self, preferencias=None, historial_adopciones=None):
        
        self.nombre = None
        self.apellido = None
        self.dni = None
        self.email = None
        self.telf = None
        self.preferencias = preferencias or []
        self.historial_adopciones = historial_adopciones or []
        
    def registrarse(self, nombre, apellido, dni, email, telf):
        
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
        
    def modificar_datos(self, nuevo_nombre=None, nuevo_dni=None, nuevo_email=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_dni:
            self.dni = nuevo_dni
        if nuevo_email:
            self.email = nuevo_email
        return "Los datos fueron modificados correctamente"

    def datosUsuario(self):
        
        datos = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "DNI": self.dni,
            "Email": self.email,
            "Preferencias": self.preferencias,
            "Historial de adopciones": self.historial_adopciones,
        }
        return datos
    
