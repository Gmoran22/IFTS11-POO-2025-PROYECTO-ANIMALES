class Perros(object):
    
    def __init__(self, nombre, raza, edad, estado_salud, tamaño, vacunado, estado_adopcion, temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.estado_salud = estado_salud
        self.tamaño = tamaño
        self.vacunado = vacunado
        self.estado_adopcion = estado_adopcion
        self.temperamento = temperamento
        self.id = id
    
    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["disponible" , "reservado", "adoptado"]:
            self.estado_adopcion = nuevo_estado
            print("Estado actualizado")
        else:
            print("Estado invalido")


    def mostrar_informacion(self):
        return  {
            "Nombre": self.nombre,
            "Raza": self.raza,
            "Edad": self.edad,
            "Estado de Salud": self.estado_salud,
            "Tamaño": self.tamaño,
            "Vacunado": self.vacunado,
            "Estado de Adopción": self.estado_adopcion,
            "Temperamento": self.temperamento,
            "ID": self.id
        }
        

class UsuarioAdoptante(object):
    def __init__(self, preferencias=None, historial_adopciones=None):
        
        self.nombre = None
        self.apellido= None
        self.dni = None
        self.email= None
        self.telf= None
        self.preferencias = preferencias or []
        self.historial_adopciones = historial_adopciones or []
        
    
    def registrar_usuario(self, nombre, apellido, dni, email, telf, contraseña):
        if not all ([nombre, apellido, dni, email, telf, contraseña]):
            return "Debe llenar todos los campos"
        
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        self.telf = telf
        self.contraseña = contraseña
        
        return {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "DNI": self.dni ,
            "Email": self.email,
            "Telefono": self.telf,
            "Contraseña": self.contraseña,
        }
        
    
    def Modificar_Datos(self, nuevo_email=None, nuevo_telefono=None, nueva_contraseña=None):
        if nuevo_email:
            self.email = nuevo_email
        
        if nuevo_telefono:
            self.telf = nuevo_telefono
        
        if nueva_contraseña:
            self.contraseña = nueva_contraseña
        
        return "Los datos fueron modificados correctamente."
    
    def datos_usuario(self):
        
        datos = {
            
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Email": self.email,
            "Teléfono": self.telf,
            "DNI": self.dni,
            "Contraseña": self.contraseña,
        }
        
        return datos
    
    def ver_historial(self):
        if not self.historial_adopciones:
            return "Este usuario no tiene historial de adopciones."
        return self.historial_adopciones
        
  

class SistemaAdopcion(object):
    
    def __init__(self):
        self.perros = []
        self.usuarios = []
         
    def cargar_perro(self, nuevo_perro):
        
        self.perros.append(nuevo_perro)
        return "El perro se cargo correctamente."
    
    def eliminar_perro(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                self.perros.remove(perro)
                return "El perro fue removido correctamente."
        return "Este perro no existe."
    
    
                       
    def registrar_usuario(self,usuario):
        self.usuarios.append(usuario)
        return "El usuario se registro correctamente."
    
    
    
    def confirmar_adopcion(self, id_perro, usuario):
        for perro in self.perros:
            if perro.id == id_perro:
                if perro.estado_adopcion == "disponible":
                    perro.cambiar_estado("adoptado")
                    usuario.historial_adopciones.append(perro)
                    return "Felicidades!, el perro ha sido adoptado."
                else:
                    return "Este perro no esta disponible en este momento para ser adoptado."
        return "Este perro no existe."
    
    
    def sugerir_perros(self, usuario):
        sugerencia = []
        for perros in self.perros:
            if (
                perros.temperamento in usuario.preferencias or 
                perros.raza in usuario.preferencias or 
                perros.tamaño in usuario.preferencias or
                perros.edad in usuario.preferencias
            ):
                if perros not in sugerencia:
                    sugerencia.append(perros.mostrar_informacion())
        if not sugerencia:
            return "No hay perros que coincidan con las preferencias del usuario."
        return sugerencia
        
    
    def listado_perros_disponibles(self):
        disponibles = [perro.mostrar_informacion() for perro in self.perros if perro.estado_adopcion == "disponible"]
        if not disponibles:
            return "No hay perros disponibles en este momento."
        return disponibles
    
    def listado_perros_por_estado(self, estado):
        if estado not in ["disponible", "reservado", "adoptado"]:
            return "Este estado no es valido."
        
        estado_perros= [perro.mostrar_informacion() for perro in self.perros if perro.estado_adopcion == estado]
        return estado_perros
    
    def listado_perros_por_usuario(self, usuario):
        for usua in self.usuarios:
            if usua.nombre == usuario.nombre and usua.dni == usuario.dni:
                return usua.ver_historial()
        return "Este usuario no existe o no tiene historial de adopciones."