from xml.etree.ElementTree import TreeBuilder


def mostrar_cursos(cursos):
    print ("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} Creditos)"
        print (datos.format(contador,cur[0],cur[1],cur[2]))
        contador += 1
    print ("")

def RegistroCurso():
    codigoCorrecto = False
    while (not codigoCorrecto):
        Codigo = input("Ingrese el codigo: ")
        if len(Codigo) == 6:
            codigoCorrecto = True
        else:
            print("Codigo incorrecto-> debe de ser de 6 digitos.....")
            
    Nombre = input("Digite el nombre del curso: ")

    creditosCorrectos = False
    while(not creditosCorrectos):
        Creditos = input("Digite los creditos del curso: ")
        if Creditos.isnumeric():
            if int(Creditos) > 0:
                creditosCorrectos = True
                Creditos = int(Creditos)
            else:
                print("Creditos incorrectos-> Debe ser mayor que cero....")
        else:
            print ("Creditos incorrectos-> Debe ser un numero....")

    curso = (Codigo, Nombre, Creditos)
    return curso

def datosActualizarCurso(cursos):
    mostrar_cursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el codigo del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
    
    if existeCodigo:
        Nombre = input("Digite el nombre del curso a modificar: ")
        creditosCorrectos = False
        while(not creditosCorrectos):
            Creditos = input("Digite los creditos del curso a modificar: ")
            if Creditos.isnumeric():
                if int(Creditos) > 0:
                    creditosCorrectos = True
                    Creditos = int(Creditos)
                else:
                    print("Creditos incorrectos-> Debe ser mayor que cero....")
            else:
                print ("Creditos incorrectos-> Debe ser un numero....")

        curso = (codigoEditar, Nombre, Creditos)
    else:
        curso = None

    return curso

def eliminarCurso(cursos):
    mostrar_cursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el codigo del curso a elimiar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""
    
    return codigoEliminar