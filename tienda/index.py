from tienda.tienda import Tienda

def main():
    tienda = Tienda()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Mostrar inventario")
        print("4. Salir")
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
            tienda.cerrar_conexion()
            print("Conexión cerrada. Adiós!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == '__main__':
    main()

