# ISPC

README.md

Datos de los Integrantes del Grupo

1. Nombre: Melina 
   - Apellido: Hatchikian
   - DNI: 35531226
   - Correo Electrónico: Melihatchi@gmail.com
   - GitHub: https://github.com/MHatchikian

2. Nombre: Miguel 
   - Apellido:Rodriguez Saquilan
   - DNI: 18889456
   - Correo Electrónico: miguelr.s77@gmail.com
   - GitHub: https://github.com/miguelrs77

3. Nombre: Cristhian Sebastian
   - Apellido: Sosa
   - DNI: 33314167
   - Correo Electrónico: sosacristhiansebas@gmail.com
   - GitHub: https://github.com/users/Cristhhh

Descripción de la Propuesta de Proyecto Elegida

Nuestro proyecto consiste en desarrollar una plataforma de comercio electrónico (eCommerce) que permita a los usuarios comprar productos de manera eficiente y segura. El objetivo principal es crear una aplicación intuitiva y fácil de usar que ofrezca una experiencia de compra agradable tanto para compradores como para el vendedor.

Características principales del proyecto:

- Catálogo de productos: Detalles como nombre, descripción, precio, y fotos.
- Carrito de compras: Los compradores pueden añadir productos a un carrito virtual y gestionar sus compras antes de finalizar la transacción.
- Procesamiento de pagos: Implementación de pasarelas de pago seguras para facilitar las transacciones.
- Sistema de usuarios: Registro y gestión de cuentas de usuarios, con rol para compradores.
- Sistema de opiniones y calificaciones: Los compradores pueden dejar opiniones y calificaciones sobre los productos adquiridos.
- Notificaciones: Alertas y notificaciones tanto para vendedor (cuando se realiza una venta) como para compradores (estado de sus pedidos).


Nuestro objetivo es que esta plataforma no solo sea funcional y eficiente, sino también escalable, permitiendo futuras expansiones y mejoras en la funcionalidad y la experiencia del usuario.

Detalle breve de lo que contienen los archivos .py:

- index.py es el archivo fuente principal donde se encuentra el menú de opciones de la aplicación. Permite agregar productos, vender productos, y mostrar el inventario a través de un menú de opciones.

- tienda.py conexión con la base de datos que permite agregar, vender, mostrar el inventario actual de los productos y cerrar la conexión a la base de datos.

- config.py archivo para realizar configuraciones donde se ingresan las credenciales que nos vinculan con las Base de Datos.

Estructura del Repositorio

Explicación de lo que contiene cada carpeta y archivo en el repositorio.

Carpetas
-README/:Proporciona una introducción al proyecto y la presentación del equipo.

-Aplicación/:Encontramos los archivos Python que conforman la funcionalidad principal de nuestra aplicación..
  config.py/: Este archivo contiene la configuración necesaria para conectar la aplicación a una base de datos MySQL
  index.py/: Este archivo contiene el punto de entrada principal para la aplicación. Aquí se define la función main, la cual inicia una instancia de la clase Tienda y proporciona un menú interactivo para que el usuario pueda realizar diversas operaciones relacionadas con la gestión de productos y clientes.
  tienda.py/: Este archivo contiene la clase Tienda, la cual implementa la lógica principal de la aplicación. La clase proporciona métodos para gestionar productos y clientes en una base de datos MySQL, incluyendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
  readme/: Este archivo contiene la configuración de la base de datos, incluyendo las credenciales necesarias para conectar a MySQL Workbench y asegurar que la base de datos tienda_db esté disponible. 

-Base de datos:Contiene los scripts DDL y DML. Aquí definimos la estructura de la base de datos..
  archivo sql de la estructura.sql/:Archivo principal donde definimos la creación de la base de datos, su uso y creación de tablas con sus PK y FK .
  archivo sql con datos.sql/: En este archivo se generaron los insert necesarios para poblar nuestra base de datos..
  archivo sql con consultas sobre los datos.sql/: en este archivos encontramos todas las consultas DML realizadas a la BBDD.

-Wiki/: En esta instancia se discutieron temas como la privacidad del usuario, protección de datos y otras consideraciones éticas importantes para nuestro proyecto.

Breve Descripción de la Aplicación
La aplicación es una tienda virtual de electrodomésticos que permite gestionar productos y clientes mediante una base de datos MySQL. Los usuarios pueden realizar diversas operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para administrar tanto el inventario de productos como la información de los clientes.

