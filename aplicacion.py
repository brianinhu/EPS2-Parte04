import sqlite3

#Conexion a base de datos
conexion = sqlite3.connect("AsuncionPomasonco_almacen.db")
cursor = conexion.cursor()
#Crear tabla producto
tabla_producto = """CREATE TABLE producto(
                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE,
                nombre TEXT UNIQUE,
                precio REAL
                )"""
cursor.execute(tabla_producto)
cursor.close()
conexion.close()

def menu():
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

while True:
    menu()
    opcion = int(input("Seleccionar una opción: "))
