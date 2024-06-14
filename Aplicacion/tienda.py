import mysql.connector
from config import DB_CONFIG


#clase principal
class Tienda:
    # creamos el constructor
    # en esta mejora hacemos control de exepciones
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(**DB_CONFIG)
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            self.conexion = None
            self.cursor = None
# metodos de nuestro CRUD            

    def agregar_producto(self, nombre, precio, cantidad):
        if self.conexion and self.cursor:
            try:
                # introducimos todas las consultas atravez de tuplas
                self.cursor.execute("SELECT cantidad, precio FROM productos WHERE nombre = %s", (nombre,))
                resultado = self.cursor.fetchone()
                if resultado:
                    nueva_cantidad = resultado[0] + cantidad
                    self.cursor.execute(
                        "UPDATE productos SET cantidad = %s, precio = %s, fecha_ingreso = NOW() WHERE nombre = %s",
                        (nueva_cantidad, precio, nombre)
                    )
                else:
                    self.cursor.execute(
                        "INSERT INTO productos (nombre, precio, cantidad, fecha_ingreso) VALUES (%s, %s, %s, NOW())",
                        (nombre, precio, cantidad)
                    )
                self.conexion.commit()
                print(f"Producto agregado: {nombre}, Precio: {precio}, Cantidad: {cantidad}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.conexion.rollback()

    def vender_producto(self, nombre, cantidad):
        if self.conexion and self.cursor:
            try:
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
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.conexion.rollback()

    def mostrar_inventario(self):
        if self.conexion and self.cursor:
            try:
                self.cursor.execute("SELECT nombre, precio, cantidad, fecha_ingreso FROM productos")
                productos = self.cursor.fetchall()
                print("Inventario de la tienda:")
                for producto in productos:
                    nombre, precio, cantidad, fecha_ingreso = producto
                    print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Fecha de ingreso: {fecha_ingreso}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
    
    # Nuevas funciones para manejar clientes, medios de pago, y pedidos
    def agregar_cliente(self, nombre, apellido=None, email=None, direccion=None, telefono=None):
        if self.conexion and self.cursor:
            try:
                self.cursor.execute(
                    "INSERT INTO CLIENTES (NOMBRE_CLI, APELLIDO, EMAIL_CLI, DIRECCION_CLI, TELEFONO_CLI) VALUES (%s, %s, %s, %s, %s)",
                    (nombre, apellido, email, direccion, telefono)
                )
                self.conexion.commit()
                print(f"Cliente agregado: {nombre}")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.conexion.rollback()

    def mostrar_clientes(self):
        if self.conexion and self.cursor:
            try:
                self.cursor.execute("SELECT * FROM CLIENTES")
                clientes = self.cursor.fetchall()
                print("Clientes:")
                for cliente in clientes:
                    print(cliente)
            except mysql.connector.Error as err:
                print(f"Error: {err}")

    def actualizar_cliente(self, id_cliente, nombre=None, apellido=None, email=None, direccion=None, telefono=None):
        if self.conexion and self.cursor:
            try:
                campos = []
                valores = []
                if nombre:
                    campos.append("NOMBRE_CLI = %s")
                    valores.append(nombre)
                if apellido:
                    campos.append("APELLIDO = %s")
                    valores.append(apellido)
                if email:
                    campos.append("EMAIL_CLI = %s")
                    valores.append(email)
                if direccion:
                    campos.append("DIRECCION_CLI = %s")
                    valores.append(direccion)
                if telefono:
                    campos.append("TELEFONO_CLI = %s")
                    valores.append(telefono)
                valores.append(id_cliente)
                
                self.cursor.execute(
                    f"UPDATE CLIENTES SET {', '.join(campos)} WHERE idCLIENTES = %s",
                    valores
                )
                self.conexion.commit()
                print(f"Cliente con ID {id_cliente} actualizado")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.conexion.rollback()

 # Ultima mejora agregamos la funcion eliminar               

    def eliminar_cliente(self, id_cliente):
        if self.conexion and self.cursor:
            try:
                self.cursor.execute("DELETE FROM CLIENTES WHERE idCLIENTES = %s", (id_cliente,))
                self.conexion.commit()
                print(f"Cliente con ID {id_cliente} eliminado")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                self.conexion.rollback()
