# Configuración de la base de datos, importante poner sus credenciales de MySQL Workbench
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ADMIN'
)

# aca usamos un diccionario
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ADMIN',
    'database': 'tienda_db'
}

# Crear una instancia del cursor
cursor = conexion.cursor()

# Crear la base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS tienda_db")

# Cerrar la conexión, buena práctica
cursor.close()
conexion.close()
