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


#funciones del estudiante

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


def actualizar_estados(lista_estudiantes):
    for e in lista_estudiantes:
        if e["nota"] >= 4.0:
            e["aprobado"] = True
        else:
            e["aprobado"] = False


def mostrar_estudiantes(lista_estudiantes):
    print("\n=== LISTA DE ESTUDIANTES ===")
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
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
    print("1. agregar estudiante")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    print("5. mostrar estudiantes")
    print("6. salir")
    print("====================================")

def solicitar_opcion():
    try:
        opcion = int(input("Seleccione una opcion: "))
        return opcion
    except ValueError:
        return -1


#programa

def iniciar_programa():
    while True:
        mostrar_menu()
        op = solicitar_opcion()
        
        if op == 1:
            agregar_estudiante(estudiantes)
        elif op in [2, 3, 4]:
            print("Opcion en desarrollo.")
        elif op == 5:
            mostrar_estudiantes(estudiantes)
        elif op == 6:
            print('\n"Gracias por usar el sistema. Vuelva pronto"')
            break
        else:
            print("Opcion invalida. intente de nuevo")

#ejecucion
if __name__ == "__main__":
    iniciar_programa()
