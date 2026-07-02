estudiantes = []

#validacion
def validar_nombre():
    nombre = input("Ingrese nombre completo: ").strip()
    if nombre == "":
        return None
    return nombre

def validar_edad():
    try:
        edad = int(input("Ingrese edad: "))
        if edad > 0:
            return edad
    except ValueError:
        pass
    return None

def validar_nota():
    try:
        nota = float(input("Ingrese nota (1.0 - 7.0): "))
        if nota >= 1.0 and nota <= 7.0:
            return nota
    except ValueError:
        pass
    return None


#datos del estudiante
def agregar_estudiante(lista_estudiantes):
    print("\n--- Agregar Estudiante ---")
    
    nombre = validar_nombre()
    if nombre is None:
        print("Error: El nombre no puede estar vacio.")
        return

    edad = validar_edad()
    if edad is None:
        print("Error: La edad debe ser un numero entero mayor que cero.")
        return

    nota = validar_nota()
    if nota is None:
        print("Error: La nota debe ser un numero decimal entre 1.0 y 7.0.")
        return

    #diccionario
    nuevo_estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota,
        "aprobado": False
    }
    
    lista_estudiantes.append(nuevo_estudiante)
    print("Estudiante registrado con exito.")


#buscar estudiante
def buscar_estudiante(lista_estudiantes, nombre_buscar):
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i]["nombre"].lower() == nombre_buscar.lower():
            return i  # Retorna la posicion (indice)
    return -1


#eliminar estudiante
def eliminar_estudiante(lista_estudiantes):
    print("\n--- Eliminar Estudiante ---")
    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ").strip()
    
    posicion = buscar_estudiante(lista_estudiantes, nombre_eliminar)
    
    if posicion != -1:
        lista_estudiantes.pop(posicion)
        print("Estudiante eliminado con exito.")
    else:
        print(f"El estudiante '{nombre_eliminar}' no se encuentra registrado.")


#actualizar estados
def actualizar_estados(lista_estudiantes):
    for e in lista_estudiantes:
        if e["nota"] >= 4.0:
            e["aprobado"] = True
        else:
            e["aprobado"] = False


#mostrar estudiantes
def mostrar_estudiantes(lista_estudiantes):
    print("\n=== LISTA DE ESTUDIANTES ===")
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    #actualizar antes de listar
    actualizar_estados(lista_estudiantes)
    
    for e in lista_estudiantes:
        if e["aprobado"]:
            estado_texto = "APROBADO"
        else:
            estado_texto = "REPROBADO"
            
        print(f"Nombre: {e['nombre']}")
        print(f"Edad: {e['edad']}")
        print(f"Nota: {e['nota']:.1f}")
        print(f"Estado: {estado_texto}")
        print("*******************************************")


#menu
def mostrar_menu():
    print("\n========== MENU PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("====================================")

def solicitar_opcion():
    try:
        opcion = int(input("Seleccione una opcion: "))
        return opcion
    except ValueError:
        return -1


#programa principal
def iniciar_programa():
    while True:
        mostrar_menu()
        op = solicitar_opcion()
        
        if op == 1:
            agregar_estudiante(estudiantes)
            
        elif op == 2:
            print("\n--- Buscar Estudiante ---")
            nombre_buscar = input("Ingrese el nombre a buscar: ").strip()
            posicion = buscar_estudiante(estudiantes, nombre_buscar)
            
            if posicion != -1:
                estudiante = estudiantes[posicion]
                print(f"\nEstudiante encontrado en la posicion {posicion}:")
                print(f"Nombre: {estudiante['nombre']} | Edad: {estudiante['edad']} | Nota: {estudiante['nota']}")
            else:
                print("Estudiante no encontrado.")
                
        elif op == 3:
            eliminar_estudiante(estudiantes)
            
        elif op == 4:
            actualizar_estados(estudiantes)
            print("Estados de aprobacion actualizados correctamente.")
            
        elif op == 5:
            mostrar_estudiantes(estudiantes)
            
        elif op == 6:
            print('\n"Gracias por usar el sistema. Vuelva Pronto"')
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

#ejecucion
if __name__ == "__main__":
    iniciar_programa()
