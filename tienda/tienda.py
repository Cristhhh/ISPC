import mysql.connector
from tienda.config import DB_CONFIG

class Tienda:
    def __init__(self):
        self.conexion = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conexion.cursor()

    def agregar_producto(self, nombre, precio, cantidad):
        self.cursor.execute("SELECT cantidad, precio FROM productos WHERE nombre = %s", (nombre,))
        resultado = self.cursor.fetchone()
        if resultado:
            nueva_cantidad = resultado[0] + cantidad
            self.cursor.execute("UPDATE productos SET cantidad = %s, precio = %s, fecha_ingreso = NOW() WHERE nombre = %s",
                                (nueva_cantidad, precio, nombre))
        else:
            self.cursor.execute("INSERT INTO productos (nombre, precio, cantidad, fecha_ingreso) VALUES (%s, %s, %s, NOW())",
                                (nombre, precio, cantidad))
        self.conexion.commit()
        print(f"Producto agregado: {nombre}, Precio: {precio}, Cantidad: {cantidad}")

    def vender_producto(self, nombre, cantidad):
        self.cursor.execute("SELECT cantidad, precio FROM productos WHERE nombre = %s", (nombre,))
        resultado = self.cursor.fetchone()
        if resultado:
            stock_actual, precio = resultado
            if stock_actual >= cantidad:
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
        self.cursor.execute("SELECT nombre, precio, cantidad, fecha_ingreso FROM productos")
        productos = self.cursor.fetchall()
        print("Inventario de la tienda:")
        for producto in productos:
            nombre, precio, cantidad, fecha_ingreso = producto
            print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Fecha de ingreso: {fecha_ingreso}")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
