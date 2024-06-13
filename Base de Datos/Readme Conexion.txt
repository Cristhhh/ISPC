Proyecto de una app de escritorio de tienda virtual de electrodomesticos Grupo Booleano

1_  crear la base de datos  en workbench 'CREATE DATABASE IF NOT EXISTS tienda_db' y despues 'USE tienda_db
2_  crear las tablas '

-- Crear la tabla CLIENTES
CREATE TABLE IF NOT EXISTS CLIENTES (
  idCLIENTES INT NOT NULL AUTO_INCREMENT,  -- Id �nico para cada cliente, se incrementa autom�ticamente
  NOMBRE_CLI VARCHAR(45) NOT NULL,         -- Nombre del cliente, obligatorio
  APELLIDO VARCHAR(45) DEFAULT NULL,       -- Apellido del cliente, opcional
  EMAIL_CLI VARCHAR(45) DEFAULT NULL,      -- Email del cliente, opcional
  DIRECCION_CLI VARCHAR(45) DEFAULT NULL,  -- Direcci�n del cliente, opcional
  TELEFONO_CLI INT DEFAULT NULL,           -- Tel�fono del cliente, opcional
  PRIMARY KEY (idCLIENTES)                 -- Llave primaria, identificador �nico de cada cliente
);

-- Crear la tabla MEDIOS_DE_PAGOS
CREATE TABLE IF NOT EXISTS MEDIOS_DE_PAGOS (
  idMDP INT NOT NULL AUTO_INCREMENT,       -- Ident �nico para cada medio de pago, se incrementa autom�ticamente
  TIPO_MDP VARCHAR(45) NOT NULL,           -- Tipo de medio de pago, obligatorio
  DESCRIPCION_MDP VARCHAR(45) DEFAULT NULL,-- Descripci�n del medio de pago, opcional
  PRIMARY KEY (idMDP)                      -- Llave primaria, identificador �nico de cada medio de pago
);
		
-- Crear la tabla PEDIDOS
CREATE TABLE IF NOT EXISTS PEDIDOS (
  idPEDIDOS INT NOT NULL AUTO_INCREMENT,    -- ID �nico para cada pedido
  MONTO_PEDIDO DECIMAL(10,2) NOT NULL,     -- Monto del pedido, obligatorio
  idCLIENTES INT NOT NULL,                 -- ID del cliente que realiza el pedido
  idMDP INT NOT NULL,                      -- ID del medio de pago utilizado
  FECHA_PEDIDO DATETIME,                   -- Fecha del pedido
  PRIMARY KEY (idPEDIDOS),                 -- PK, identificador �nico de cada pedido
  CONSTRAINT fk_PEDIDOS_CLIENTES
    FOREIGN KEY (idCLIENTES)               -- FK que referencia a CLIENTES
    REFERENCES CLIENTES (idCLIENTES)
    ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT fk_PEDIDOS_MEDIOS_DE_PAGOS
    FOREIGN KEY (idMDP)                    -- FK que referencia a MEDIOS_DE_PAGOS
    REFERENCES MEDIOS_DE_PAGOS (idMDP)
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Crear la tabla CATEGORIAS
CREATE TABLE IF NOT EXISTS CATEGORIAS (
  idCATEGORIAS INT NOT NULL AUTO_INCREMENT, -- ID �nico para cada categor�a
  NOMBRE_CAT VARCHAR(45) NOT NULL,         -- Nombre de la categor�a, obligatorio
  PRIMARY KEY (idCATEGORIAS)               -- PK, identificador �nico de cada categor�a
);

-- Crear la tabla PRODUCTOS
CREATE TABLE IF NOT EXISTS PRODUCTOS (
  idPRODUCTOS INT NOT NULL AUTO_INCREMENT,   -- ID �nico para cada producto
  DESCRIPCION_PROD VARCHAR(45) DEFAULT NULL, -- Descripci�n del producto, opcional
  idCATEGORIAS INT NOT NULL,               -- ID de la categor�a del producto
  STOCK_PROD INT NOT NULL,                 -- Cantidad de productos en stock, obligatorio
  PRECIO_PROD DECIMAL(10,2) NOT NULL,      -- Precio del producto, obligatorio
  PRIMARY KEY (idPRODUCTOS),               -- PK, identificador �nico de cada producto
  CONSTRAINT fk_PRODUCTOS_CATEGORIAS
    FOREIGN KEY (idCATEGORIAS)             -- FK que referencia a CATEGORIAS
    REFERENCES CATEGORIAS (idCATEGORIAS)
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- Crear la tabla PEDIDOS_DETALLES
CREATE TABLE IF NOT EXISTS PEDIDOS_DETALLES (
  idDETALLE INT NOT NULL AUTO_INCREMENT,   -- ID �nico para cada detalle de pedido
  idPEDIDOS INT NOT NULL,                  -- ID del pedido al que pertenece el detalle
  idPRODUCTOS INT NOT NULL,                -- ID del producto en el pedido
  CANTIDAD_PRODUCTOS INT DEFAULT NULL,     -- Cantidad de productos en el detalle, opcional
  PRECIO_EN_FECHA DECIMAL(10,2) DEFAULT NULL COMMENT 'Precio del producto en la fecha del pedido', -- Precio en la fecha del pedido, opcional
  PRIMARY KEY (idDETALLE),                 -- PK, identificador �nico de cada detalle
  CONSTRAINT fk_PEDIDOS_DETALLES_PEDIDOS
    FOREIGN KEY (idPEDIDOS)                -- FK que referencia a PEDIDOS
    REFERENCES PEDIDOS (idPEDIDOS)
    ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT fk_PEDIDOS_DETALLES_PRODUCTOS
    FOREIGN KEY (idPRODUCTOS)              -- FK que referencia a PRODUCTOS
    REFERENCES PRODUCTOS (idPRODUCTOS)
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

3_ en visual levantar el proyecto y en la terminal insertar el conector 
    'pip install mysql-connector-python'

4_ en config.py cambiar las credenciales que tienen en su Mysql 

# Configuraci�n de la base de datos importante poner sus credenciales de Mysql workbench
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '****',
    'database': 'tienda_db'
}

5- ejecutar index.py   