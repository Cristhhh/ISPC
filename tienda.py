import mysql.connector
from config import DB_CONFIG


# Establecemos la conexión con la base de datos MySQL

class Tienda:
    def __init__(self):
        self.conexion = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conexion.cursor()

 # Funcion para Verificar si el producto ya existe en el inventario
    def agregar_producto(self, nombre, precio, cantidad):
        self.cursor.execute("SELECT cantidad FROM productos WHERE nombre = %s", (nombre,))
        resultado = self.cursor.fetchone()
        if resultado:
            # Si el producto existe, actualiza la cantidad
            nueva_cantidad = resultado[0] + cantidad
            self.cursor.execute("UPDATE productos SET cantidad = %s WHERE nombre = %s", (nueva_cantidad, nombre))
        else:
            # Si el producto no existe, lo inserta en la base de datos
            self.cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)",
                                (nombre, precio, cantidad))
        self.conexion.commit()
        print(f"Producto agregado: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

    def vender_producto(self, nombre, cantidad):
        # Verificamos si el producto existe y vemos cantidad y precio
        self.cursor.execute("SELECT cantidad, precio FROM productos WHERE nombre = %s", (nombre,))
        resultado = self.cursor.fetchone()
        if resultado:
            stock_actual, precio = resultado
            if stock_actual >= cantidad:
                # Si hay suficiente stock, actualiza la cantidad y calcula el total de la venta
                nueva_cantidad = stock_actual - cantidad
                self.cursor.execute("UPDATE productos SET cantidad = %s WHERE nombre = %s", (nueva_cantidad, nombre))
                self.conexion.commit()
                total_venta = cantidad * precio
                print(f"Producto vendido: {nombre}, Cantidad: {cantidad}, Total: {total_venta}")
            else:
                print("Cantidad insuficiente en inventario.")
        else:
            print("Producto no encontrado en el inventario.")

    def mostrar_inventario(self):
        # Recuperamos y muestramos todos los productos en el inventario
        self.cursor.execute("SELECT nombre, precio, cantidad FROM productos")
        productos = self.cursor.fetchall()
        print("Inventario de la tienda:")
        for producto in productos:
            nombre, precio, cantidad = producto
            print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")


        # cerramos la conexion

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
