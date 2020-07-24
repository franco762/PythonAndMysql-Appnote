import notas.nota as modelo

class Acciones:
    def Crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota....")

        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.Guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has creado la nota: {nota.titulo}")
        
        else:
            print(f"\nNo se ha guardado a nota, lo siento {usuario[1]}")

    def Mostrar(self, usuario):
        nota = modelo.Nota(usuario[0])
        notas = nota.Listar()

        if notas == 0:
            print(f"\nNo tienes notas para mostrar !!, por favor crea una")
    
        else:
            print(f"\nHola {usuario[1]} estas son tus notas: ")

            for nota in notas:
                print("\n=====================================")
                print(nota[2])
                print(nota[3])
                print("=======================================")

    def Eliminar(self, usuario):
        print(f"\nOk {usuario[1]} vamos a borrar notas")

        titulo = input("\nIntroduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        notas = nota.Borrar()

        if notas[0] >= 1:
            print(f"\nHemos eliminado la nota {nota.titulo} con exito")

        else:
            print(f'\n"{titulo}" no pudo ser eliminada, por que no existe en nuestra db')

    def Modificar(self, usuario):
        print(f"\nOk {usuario[1]} vamos a modificar notas")

        n_nota = input("\nIngresa el nombre de la nota a actualizar: ")

        titulo = input("\nIntroduce un nuevo titulo: ")
        descripcion = input("Introduce una nueva descripción: ")

        nota = modelo.Nota(usuario[0], n_nota)
        notas = nota.Actualizar(titulo, descripcion)

        if notas[0] >= 1:
            print(f"\nActualización completada con exito")

        else:
            print(f"Fallo al intentar actualizar la nota")