-- Insertar registros en la tabla CLIENTES
INSERT INTO CLIENTES (NOMBRE_CLI, APELLIDO, EMAIL_CLI, DIRECCION_CLI, TELEFONO_CLI, idCLIENTES) VALUES
('Melina', 'Hatchikian', 'm.hat@example.com', 'Calle Falsa 123', 351687982,1),
('Miguel', 'Rodriguez', 'm.rodriguez@example.com', 'Avenida Siempre Viva 456',261489675,2),
('Christian', 'Sosa', 'm.rodriguez@example.com', 'Bv. Gurro 789', 3512348765,3);

SHOW COLUMNS FROM CLIENTES LIKE 'TELEFONO_CLI';  -- se muestra tipo de dato de la columna telefono, ya que me da error al insetar los datos -
ALTER TABLE CLIENTES MODIFY TELEFONO_CLI VARCHAR(20); -- se modifica el tipo de dato

-- Insertar registros en la tabla MEDIOS_DE_PAGOS
INSERT INTO MEDIOS_DE_PAGOS (TIPO_MDP, DESCRIPCION_MDP) 
VALUES
('Tarjeta de Crédito', 'Visa'),
('Transferencia Bancaria', 'Banco M'),
('Efectivo', 'EFVO');

-- Insertar registros en la tabla PEDIDOS
INSERT INTO PEDIDOS (MONTO_PEDIDO, idCLIENTES, idMDP, FECHA_PEDIDO) 
VALUES
(150.50, 1, 1, '2024-06-01'),
(300.75, 2, 2, '2024-07-08'),
(978.00, 3, 3, '2024-05-02');

UPDATE PEDIDOS SET FECHA_PEDIDO ='2024-06-05' WHERE IdCLIENTES=3; -- Se modifica la fecha de pedido referenciada al idCliente 3

SELECT * FROM PEDIDOS; -- se consulta la tabla pedidos

DELETE FROM PEDIDOS WHERE IdPEDIDOS >4; -- Se eliminan registros duplicados.

-- Insertar registros en la tabla CATEGORIAS
INSERT INTO CATEGORIAS (NOMBRE_CAT) 
VALUES
('Audio'),
('Entretenimiento'),
('Linea Blanca');

-- Insertar registros en la tabla PRODUCTOS
INSERT INTO PRODUCTOS (DESCRIPCION_PROD, idCATEGORIAS, STOCK_PROD, PRECIO_PROD) VALUES
('Parlante', 1, 10, 199.99),
('TV 45"', 2, 50, 969.99),
('Heladera', 3, 20, 889.99);

-- Insertar registros en la tabla PEDIDOS_DETALLES
INSERT INTO PEDIDOS_DETALLES (idPEDIDOS, idPRODUCTOS, CANTIDAD_PRODUCTOS, PRECIO_EN_FECHA) VALUES
(1, 1, 1, 199.99),
(2, 2, 2, 969.99),
(3, 3, 3, 889.99);