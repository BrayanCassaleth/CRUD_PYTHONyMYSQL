import mysql.connector
from mysql.connector import Error

class DAO():# Data Access Object

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect( # Conexion a la base de datos
                user = "root",
                password = "123456",
                database = "universidad",
                host = "localhost",
                port = "3306"
            )
        except Error as er:
            print("Error al intentar la conexion:",er)
    
    def ConsultaCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")# Imprimir los cursos de manera ascendente
                result = cursor.fetchall()
                return result

            except Error as er:
                print("Error al intentar la conexion:",er)     

    def registroCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso VALUES ('{0}','{1}',{2})"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print ("")
                print ("--- Curso registrado con exito! ---\n")
            except Error as er:
                print("Error al intentar la conexion:",er)
    
    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print ("")
                print ("--- Curso actualizado con exito! ---\n")
            except Error as er:
                print("Error al intentar la conexion:",er)
        
    def eliminarCurso(self,codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE Codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print ("")
                print ("--- Curso eliminado! ---\n")
            except Error as er:
                print("Error al intentar la conexion:",er)      
