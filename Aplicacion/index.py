from tienda import Tienda

def main():
    tienda = Tienda()
# Atravez de un while recorremos las opciones en un bucle la unica forma de salir es atravez de 
# un break que es la opcion 8
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Mostrar inventario")
        print("4. Agregar cliente")
        print("5. Mostrar clientes")
        print("6. Actualizar cliente")
        print("7. Eliminar cliente")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            tienda.agregar_producto(nombre, precio, cantidad)
        elif opcion == '2':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a vender: "))
            tienda.vender_producto(nombre, cantidad)
        elif opcion == '3':
            tienda.mostrar_inventario()
        elif opcion == '4':
            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            email = input("Email del cliente: ")
            direccion = input("Dirección del cliente: ")
            telefono = input("Teléfono del cliente: ")
            tienda.agregar_cliente(nombre, apellido, email, direccion, telefono)
        elif opcion == '5':
            tienda.mostrar_clientes()
        elif opcion == '6':
            id_cliente = int(input("ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre del cliente (dejar vacío para no cambiar): ")
            apellido = input("Nuevo apellido del cliente (dejar vacío para no cambiar): ")
            email = input("Nuevo email del cliente (dejar vacío para no cambiar): ")
            direccion = input("Nueva dirección del cliente (dejar vacío para no cambiar): ")
            telefono = input("Nuevo teléfono del cliente (dejar vacío para no cambiar): ")
            tienda.actualizar_cliente(id_cliente, nombre or None, apellido or None, email or None, direccion or None, telefono or None)
        elif opcion == '7':
            id_cliente = int(input("ID del cliente a eliminar: "))
            tienda.eliminar_cliente(id_cliente)
        elif opcion == '8':
            tienda.cerrar_conexion()
            print("Conexión cerrada. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == '__main__':
    main()
