import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def Guardar(self):
        sql = "INSERT INTO notas VALUES (null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        try:
            cursor.execute(sql, nota)
            database.commit()
            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        return result

    def Listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        try:
            cursor.execute(sql)
            database.commit()
            result = cursor.fetchall()

        except:
            result = 0
        
        return result

    def Borrar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"

        try:
            cursor.execute(sql)
            database.commit()
            result = [cursor.rowcount, self]

        except:
            result = [0, self]

        return result

    def Actualizar(self, titulo, descripcion):
        sql = f"UPDATE notas SET titulo = '{titulo}', descripcion = '{descripcion}' WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"

        try:
            cursor.execute(sql)
            database.commit()
            result = [cursor.rowcount, self]
        
        except:
            result = [0, self]

        return result

        