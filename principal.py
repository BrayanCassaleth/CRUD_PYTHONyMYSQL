from database.conexion import DAO
import funciones
from mysql.connector import Error

def menbuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while (not opcionCorrecta):
            print ("")
            print ("===== MENU PRINCIPAL =====")
            print ("1- Mostrar los cursos.")
            print ("2- Registrar cursos.")
            print ("3- Actualizar cursos.")
            print ("4- Eliminar cursos.")
            print ("5- Salir.")
            print ("==========================")
            print ("")
            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 5:
                print("")
                print ("*** Opcion incorrecta, seleccione nuevamente ***")
                print("")

            elif opcion == 5:
                continuar = False
                print ("\n Gracias por usar el sistema.")
                break

            else:
                opcionCorrecta = True   
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            cursos = dao.ConsultaCursos()
            if len(cursos) > 0:
                funciones.mostrar_cursos(cursos)
            else:
                print("No se encontraron cursos")
        except:
            print ("Ocurrio un error")

    elif opcion == 2:
        curso = funciones.RegistroCurso()
        try:
            dao.registroCurso(curso)
        except:
            print ("Ocurrio un error")
    elif opcion == 3:
        try:
            cursos = dao.ConsultaCursos()
            if len(cursos) > 0:
                curso = funciones.datosActualizarCurso(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print ("Codigo de  curso a actualizar no encontrado.....\n")
        except:
            print ("Ocurrio un error")

    elif opcion == 4:
        try:
            cursos = dao.ConsultaCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.eliminarCurso(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print ("Codigo de curso no encontrado....\n")
        except:
            print ("Ocurrio un error") 
    else:
        print ("Opcion no valida")
    

menbuPrincipal()