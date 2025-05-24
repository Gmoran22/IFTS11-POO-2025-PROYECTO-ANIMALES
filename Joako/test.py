from main import UsuarioAdoptante

usuario = UsuarioAdoptante()

usuario.nombre = "Joaquin"
usuario.apellido = "Fernandez"
usuario.dni = "47573299"
usuario.email= "joaquinfernandezds@gmail.com"

print(usuario.modificar_datos(nuevo_dni="12345678"))

datos = usuario.datosUsuario()
print("Datos del Usuario:")
for clave, valor in datos.items():
    print(f"{clave}: {valor}")
