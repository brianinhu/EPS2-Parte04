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
        print("ID\tCódigo\tNombre\tPrecio")
        print("-"*50)
        for producto in productos:
            print(producto[0], producto[1], producto[2], producto[3], sep="\t")


def registrar_producto(codigo, nombre, precio):
    sql = "INSERT INTO producto(codigo, nombre, precio) VALUES(?,?,?)"
    with sqlite3.connect("AsuncionPomasonco_almacen.db") as con:
        cursor = con.cursor()
        cursor.execute(sql, (codigo, nombre, precio))
        con.commit()
        print("Producto registrado con éxito")

# Registrar 10 productos
def registrar_10_productos():
    productos = [
        ("P001", "Café Tunki", 25.00),
        ("P002", "Chocolates La Iberica", 15.50),
        ("P003", "Pisco Portón", 80.00),
        ("P004", "Aceitunas Botija", 12.00),
        ("P005", "Chicha Morada", 5.00),
        ("P006", "Cerveza Cusqueña", 8.00),
        ("P007", "Inka Kola", 3.50),
        ("P008", "Papa Seca", 6.00),
        ("P009", "Leche Gloria", 4.50),
        ("P010", "Cuy Asado", 30.00)
    ]
    sql = "INSERT INTO producto (codigo, nombre, precio) VALUES (?,?,?)"
    with sqlite3.connect("AsuncionPomasonco_almacen.db") as con:
        cursor = con.cursor()
        cursor.executemany(sql, productos)
        print("10 productos insertados con éxito")


# while True:
#     menu()
#     opcion = int(input("Seleccionar una opción: "))

registrar_10_productos()