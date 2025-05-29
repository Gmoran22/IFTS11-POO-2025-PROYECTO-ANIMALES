''' Clase Perro
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
        
'''2. Clase UsuarioAdoptante
● Atributos: nombre, dni, email, preferencias (raza, edad, tamaño),
historial_adopciones.
● Métodos: registrarse, modificar datos, ver historial, etc.'''
        
class Adoptante(object):
    def __init__(self, nombre, dni, email, preferencias, historial_adopciones):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias
        self.historial_adopciones = historial_adopciones
        
    def preferencias(self, raza=None, edad=None, tamaño=None):
        if raza:
            self.preferencias["raza"] = raza
        if edad:
            self.preferencias["edad"] = edad
        if tamaño:
            self.preferencias["tamaño"] = tamaño
        print("Preferencias actualizadas")
        
    def registrarse(self, nombre, apellido, dni, email, telf):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telf = telf
        print(f"nombre. {self.nombre}", f"apellido: {self.apellido}", f"email: {self.email}", f"Telf: {self.telf}")
    
    def modificarDatos(self, nuevo_nombre, nuevo_apellido, nuevo_dni, nuevo_email, nuevo_telf, nueva_preferencia):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        self.dni = nuevo_dni
        self.email = nuevo_email
        self.telf = nuevo_telf
        self.preferencias = nueva_preferencia
        print("Datos actualizados correctamente")
    
    def mostrarDatosUsuario(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print( f"Dni: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Telf: {self.telf}")
        print( f"Preferencias: {self.preferencias}")
        if self.historial_adopciones:
            print("Perros adoptados:")
            for perro in self.historial_adopciones:
                print(perro.nombre, perro.raza)
        else:
            print("Aún no ha adoptado ningún perro")
    
    def verHistorial(self):
        print(self.historial_adopciones)
        
'''3. Clase SistemaAdopcion
● Métodos para:
○ Cargar y eliminar perros
○ Registrar usuarios  ????
○ Postular a un perro
○ Confirmar adopción
○ Sugerir perros según preferencias
○ Mostrar listados (perros disponibles, por estado, por usuario)'''

class SistemaAdopcion:
    def __init__(self, perros, usuarios):
        self.perros=[]
        self.usuarios= []
        
    def cargarPerro(self,nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"{self.perros}")
        
    def eliminar_perro(self, id):  #METODO A REVISAR
        for perro in self.perros:
            if perro.id == id:
                self.perros.remove(perro)
                print("Perro eliminado")
                return
        print("Perro no encontrado")
    def eliminarPerros(self, nombre): #lo hice con nombre pero estaria mejor con id porque nombres puede haber iguales
         for perro in self.perros: #busco el nombre del perro en la lista de perros
             if perro.nombre == nombre: #si el nombre que puse esta en la lista de perros
               self.perros.remove(perro) #lo elimino
               print(f"Perro {nombre} eliminado.") 
               break # una vez que lo encontré rompo el programa porque si no lo hago, seguiria buscando 
         else:
    
            print("No se encontró un perro con ese nombre.")
         print(f"{self.perros}")
    def registrarUsuario(self,nuevo_usuario):
        self.usuarios.append(nuevo_usuario)
    def postularPerro(self,id):
        for perro in self.perros:
            if perro.id == id:
                if perro.estado== "Disponible":
                    perro.cambiarEstado("Reservado")
                    print(f"Perro {id} reservado con éxito!")
                    return perro
                else:
                    print(f"Este perro {id} se encuentra reservado, no es posible postularse")
                    return None
        print(f"No se encontró ningun perro con el ID {id}")
        return None
        
    