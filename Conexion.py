import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="bdoptica"
)

# Cursor inicial para una consulta preliminar
cursor = conexion.cursor()
cursor.execute("SELECT idEmpleado, Nombres, Apellidos, Cedula, Correo, Contraseña, idRol, Registro FROM tblempleados")

empleados = cursor.fetchall()
for idEmpleado, Nombre, Apellidos, Cedula, Correo, Contraseña, idRol, Registro in empleados:
    print(idEmpleado, " | ", Nombre, " | ", Apellidos, " | Cedula =", Cedula, "| Correo= ", Correo, " | ID Rol= ", idRol, " | ", Registro)

print("\n")
print("1: Ver datos de la tabla")
print("2: Crear un nuevo empleado")
print("3: Actualizar dato de empleado")
print("4: Eliminar un empleado")
numOp = int(input("Ingrese opción: "))
print("\n")

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
        inp_id= int(input("Ingrese ID: "))
        inp_nom= str(input("Ingrese el Nombre: "))
        inp_ape= str(input("Ingrese el Apellido: "))
        inp_cedu= str(input("Ingrese el cedula: "))
        inp_correo=str(input("Ingrese la Correo: "))
        inp_pass= str(input("Ingrise contraseña: "))
        inp_idRol=int(input("Ingrese el iD Rol: "))
        inp_reg= str(input("Igrese Fecha de registro: ")) 

        newEmp(inp_id, inp_nom, inp_ape, inp_cedu, inp_correo,  inp_pass, inp_idRol, inp_reg)
        print("\n")

        cursor.execute("SELECT idEmpleado, Nombres, Apellidos, Cedula, Correo, Contraseña, idRol FROM tblempleados")
        empleados = cursor.fetchall()
        for idEmpleado, Nombre, Apellidos, Cedula, Correo, Contraseña, idRol, Registro in empleados:
            print(idEmpleado, " | ", Nombre, " | ", Apellidos, " | ", Cedula, " | ", Correo, " | ", Contraseña, " | ", idRol," | ", Registro)

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

        #Datos de entrada
        inp_modificar = int(input("Ingrese ID a modificar el Correo: "))
        inp_new_Correo= str(input("Ingrese Nuevo Correo: "))
        
        update_employee_email(inp_modificar,inp_new_Correo)

        print("\n")
        cursor.execute("SELECT Nombres, Correo FROM tblempleados")
        empleados = cursor.fetchall()
        for Nombre, Correo in empleados:
            print(Nombre, " | Correo= ", Correo)

    elif numOp == Opciones.OPCION_4:
        print("Eleminar un Empledo ")
        def delete_id_empleado(delete_id):
            delete_query = """
            DELETE FROM tblempleados
            WHERE  idEmpleado = %s
            """
            try:
                cursor.execute(delete_query,(delete_id,))
                conexion.commit()
                print("Registro eleminado")
            except mysql.connector.Error  as  err:
                print(f"Error: {err}")
                conexion.rollback() 

        delete_id = int(input("Ingrese el ID del empleado a eliminar: "))
        delete_id_empleado(delete_id)
        print("\n")
        
        
except ValueError:
    print("Opción no válida")

print("\n")
cursor.close()
conexion.close()