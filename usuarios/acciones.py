import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def Registro(self):
        print("\nOk!! Vaos a registrarte en el sistema...")

        nombre = input("\n¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.Registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
    
        else:
            print("\nNo te has registrado correctamente!!!")

    def Login(self):
        print("\nVale!! Identificate en el sistema...")
        
        try:
            email = input("\nIntroduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.Identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.ProximasAcciones(login)

        except:
            print("Login incorrecto!! Intentalo mas tarde")

    def ProximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Actualizar nota (actualizar)
            - Salir (salir)
        """)

        accion = input("¿Que quieres hacer?: ")
        accionm = accion.lower()

        hazEl = notas.acciones.Acciones()

        if accionm == "crear":
            hazEl.Crear(usuario)
            self.ProximasAcciones(usuario)

        elif accionm == "mostrar":
            hazEl.Mostrar(usuario)
            self.ProximasAcciones(usuario)

        elif accionm == "eliminar":
            hazEl.Eliminar(usuario)
            self.ProximasAcciones(usuario)

        elif accionm == "actualizar":
            hazEl.Modificar(usuario)
            self.ProximasAcciones(usuario)

        elif accionm == "salir":
            print(f"Ok {usuario[1]}, hasta pronto !!!")