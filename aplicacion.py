import sqlite3

# # Conexion a base de datos
# conexion = sqlite3.connect("AsuncionPomasonco_almacen.db")
# cursor = conexion.cursor()
# # Crear tabla producto
# tabla_producto = """CREATE TABLE producto(
#                 idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
#                 codigo TEXT UNIQUE,
#                 nombre TEXT UNIQUE,
#                 precio REAL
#                 )"""
# cursor.execute(tabla_producto)
# cursor.close()
# conexion.close()


def menu():
    print("Menú Opciones")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")


def listar_productos():
    sql = "SELECT * FROM producto"
    with sqlite3.connect("AsuncionPomasonco_almacen.db") as con:
        cursor = con.cursor()
        cursor.execute(sql)
        productos = cursor.fetchall()
        print("{:<10} {:<15} {:<40} {:<15}".format("ID", "Código", "Nombre", "Precio"))
        print("-"*80)
        for idproducto, codigo, nombre, precio in productos:
            print("{:<10} {:<15} {:<40} {:<15}".format(
                idproducto, codigo, nombre, precio))


def registrar_producto(codigo, nombre, precio):
    sql = "INSERT INTO producto(codigo, nombre, precio) VALUES(?,?,?)"
    with sqlite3.connect("AsuncionPomasonco_almacen.db") as con:
        cursor = con.cursor()
        cursor.execute(sql, (codigo, nombre, precio))
        con.commit()
        print("Producto registrado con éxito")


def eliminar_producto(idproducto):
    sql = "DELETE FROM producto WHERE idproducto=?"
    with sqlite3.connect("AsuncionPomasonco_almacen.db") as con:
        cursor = con.cursor()
        cursor.execute(sql, (idproducto,))
        print("Producto eliminado con éxito")


def editar_producto(idproducto, codigo, nombre, precio):
    sql = "UPDATE producto SET codigo=?, nombre=?, precio=? WHERE idproducto=?"
    with sqlite3.connect("AsuncionPomasonco_almacen.db") as con:
        cursor = con.cursor()
        cursor.execute(sql, (codigo, nombre, precio, idproducto))
        print("Producto actualizado con éxito")


while True:
    menu()
    opcion = int(input("Seleccionar una opción: "))
    if opcion == 1:
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre: ")
        precio = float(input("Ingrese precio: "))
        registrar_producto(codigo, nombre, precio)
    elif opcion == 2:
        listar_productos()
        idproducto = int(input("Ingrese ID del producto a eliminar: "))
        eliminar_producto(idproducto)
    elif opcion == 3:
        listar_productos()
        idproducto = int(input("Ingrese ID del producto a editar: "))
        codigo = input("Ingrese código: ")
        nombre = input("Ingrese nombre: ")
        precio = float(input("Ingrese precio: "))
        editar_producto(idproducto, codigo, nombre, precio)
    elif opcion == 4:
        listar_productos()
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")

print("Fin del programa")
