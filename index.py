agenda = []

while True:
    print("----> Menú de la Agenda <----")
    print("1 - Agregar nombre")
    print("2 - Eliminar nombre")
    print("3 - Modificar nombre")
    print("4 - Mostrar nombres")
    print("5 - Mostrar Todos los nombres y datos")
    print("6 - Eliminar Todos los nombres con datos ")
    print("0 - Salir")

    opc = input("Seleccione una opción: ")

    if opc == "1":
        nombre = input("Ingrese el nombre : ")
        apellido = input("Ingrese el apellido : ")
        edad = int(input("Ingrese la edad : "))
        telefono = input("Ingrese el teléfono : ")
        dni = input("Ingrese el DNI : ")
        direccion = input("Ingrese la dirección: ")

        usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "telefono": telefono,
            "dni": dni,
            "direccion": direccion
        }

        agenda.append(usuario)
        print("Agregado con éxito.")

    elif opc == "2":
        dni = input("Ingrese el DNI que desea eliminar: ")

        usuarios_a_eliminar = []
        for usuario in agenda:
            if usuario["dni"] == dni:
                usuarios_a_eliminar.append(usuario)

        if usuarios_a_eliminar:
            for usuario in usuarios_a_eliminar:
                agenda.remove(usuario)
            print(f"{usuario} eliminado con éxito.")
        else:
            print("No se encontró con el DNI proporcionado.")

    elif opc == "3":
        dni = input("Ingrese el DNI  que desea modificar: ")

        usuario_ubicau = None
        for usuario in agenda:
            if usuario["dni"] == dni:
                usuario_ubicau = usuario
        usuario_ubicau
        if usuario_ubicau:
            print("Datos actuales del usuario:")
            print(usuario_ubicau)
            print("Ingrese los nuevos datos:")

            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            edad = int(input("Nueva edad: "))
            telefono = input("Nuevo teléfono: ")
            direccion = input("Nueva dirección: ")

            usuario_ubicau["nombre"] = nombre
            usuario_ubicau["apellido"] = apellido
            usuario_ubicau["edad"] = edad
            usuario_ubicau["telefono"] = telefono
            usuario_ubicau["direccion"] = direccion

            print(" Modificado con éxito.")
        else:
            print("No se encontró ningún Nombre con ese DNI")

    elif opc == "4":
        dni = input("Ingrese el DNI de la persona que desea mostrar: ")

        usuario_ubicau = None
        for usuario in agenda:
            if usuario["dni"] == dni:
                usuario_ubicau = usuario
                break

        if usuario_ubicau:
            print("Datos agendado ")
            print(usuario_ubicau)
        else:
            print("No se encontró ningún Nombre con ese DNI")

    elif opc == "5":
        print("Todos los Nombres de la agenda:")
        for usuario in agenda:
            print(usuario)

    elif opc == "6":
        agenda.clear()
        print("Se eliminaron todos los Datos de la agenda.")

    elif opc == "0":
        print("Saliendo de la agenda.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
