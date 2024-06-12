import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="bdoptica"
)
print("Conexión a la base de datos establecida correctamente")

# Cursor inicial para una consulta preliminar
cursor = conexion.cursor()
cursor.execute("SELECT idEmpleado, Nombres, Apellidos, Cedula, Correo, Contraseña, idRol, Registro FROM tblempleados")

# Leer y mostrar resultados iniciales
empleados = cursor.fetchall()
for idEmpleado, Nombre, Apellidos, Cedula, Correo, Contraseña, idRol, Registro in empleados:
    print(idEmpleado, " | ", Nombre, " | ", Apellidos, " | Cedula =", Cedula, "| Correo= ", Correo, " | ID Rol= ", idRol, " | ", Registro)

# Menú de opciones
print("\n")
print("1: Ver datos de la tabla")
print("2: Crear un nuevo empleado")
print("3: Actualizar dato de empleado")
print("4: Eliminar un empleado")
numOp = int(input("Ingrese opción: "))
print("\n")

# Clase de opciones
class Opciones:
    OPCION_1 = 1
    OPCION_2 = 2
    OPCION_3 = 3
    OPCION_4 = 4

try:
    if numOp == Opciones.OPCION_1:
        print("Datos de los Empleados")
        cursor.execute("SELECT idEmpleado, Nombres, Apellidos, Cedula, Correo, Contraseña, idRol, Registro FROM tblempleados")
        empleados = cursor.fetchall()
        for idEmpleado, Nombre, Apellidos, Cedula, Correo, Contraseña, idRol, Registro in empleados:
            print(idEmpleado, " | ", Nombre, " | ", Apellidos, " | Cedula =", Cedula, "| Correo= ", Correo, " | ID Rol= ", idRol, " | ", Registro)

    elif numOp == Opciones.OPCION_2:
        print("Crear nuevo Empleado")

        def newEmp(new_id, new_nom, new_ape, new_cedu, new_correo, new_pass, new_idRol, new_reg):
            query_new = """
            INSERT INTO tblempleados (
                idEmpleado,
                Nombres,
                Apellidos,
                Cedula,
                Correo,
                Contraseña,
                idRol,
                Registro
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            try:
                cursor.execute(query_new, (new_id, new_nom, new_ape, new_cedu, new_correo, new_pass, new_idRol, new_reg))
                conexion.commit()
                print(f"Se agregó nuevo Empleado {new_nom}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                conexion.rollback()

        # Llamar a la función newEmp con los datos del nuevo empleado
        newEmp(4, "Wilmer", "Loaiza", "123131", "Brenz47@gmail.com", "wilmer123", 1, "2024-06-05 10:28:25")

        cursor.execute("SELECT idEmpleado, Nombres, Apellidos, Cedula, Correo, Contraseña, idRol FROM tblempleados")
        empleados = cursor.fetchall()
        for idEmpleado, Nombre, Apellidos, Cedula, Correo, Contraseña, idRol in empleados:
            print(idEmpleado, " | ", Nombre, " | ", Apellidos, " | ", Cedula, " | ", Correo, " | ", Contraseña, " | ", idRol)

    elif numOp == Opciones.OPCION_3:
        print("Actualizar")

        def update_employee_email(employee_id, new_email):
            update_query = """
            UPDATE tblempleados
            SET Correo = %s
            WHERE idEmpleado = %s
            """
            try:
                cursor.execute(update_query, (new_email, employee_id))
                conexion.commit()
                print(f"Se ha actualizado el correo del empleado con ID: {employee_id}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                conexion.rollback()

        update_employee_email(1, 'Pequelapunada@Gmail.com')

        cursor.execute("SELECT Nombres, Correo FROM tblempleados")
        empleados = cursor.fetchall()
        for Nombre, Correo in empleados:
            print(Nombre, " | Correo= ", Correo)

    elif numOp == Opciones.OPCION_4:
        print("Opción 4 seleccionada")

except ValueError:
    print("Opción no válida")

print("\n")
cursor.close()
conexion.close()
