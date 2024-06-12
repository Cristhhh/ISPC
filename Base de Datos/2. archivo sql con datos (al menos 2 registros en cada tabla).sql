-- Insertar registros en la tabla CLIENTES
INSERT INTO CLIENTES (NOMBRE_CLI, APELLIDO, EMAIL_CLI, DIRECCION_CLI, TELEFONO_CLI) VALUES
('Melina', 'Hatchikian', 'm.hat@example.com', 'Calle Falsa 123', 351687982),
('Miguel', 'Rodriguez', 'm.rodriguez@example.com', 'Avenida Siempre Viva 456', 261489675);

-- Insertar registros en la tabla MEDIOS_DE_PAGOS
INSERT INTO MEDIOS_DE_PAGOS (TIPO_MDP, DESCRIPCION_MDP) 
VALUES
('Tarjeta de Crédito', 'Visa'),
('Transferencia Bancaria', 'Banco M');

-- Insertar registros en la tabla PEDIDOS
INSERT INTO PEDIDOS (MONTO_PEDIDO, idCLIENTES, idMDP) 
VALUES
(150.50, 1, 1),
(300.75, 2, 2);

-- Insertar registros en la tabla CATEGORIAS
INSERT INTO CATEGORIAS (NOMBRE_CAT) 
VALUES
('Audio'),
('Ilumincacion');

-- Insertar registros en la tabla PRODUCTOS
INSERT INTO PRODUCTOS (DESCRIPCION_PROD, idCATEGORIAS, STOCK_PROD, PRECIO_PROD) VALUES
('Parlante', 1, 10, 999.99),
('Luces LED', 2, 50, 19.99);

-- Insertar registros en la tabla PEDIDOS_DETALLES
INSERT INTO PEDIDOS_DETALLES (idPEDIDOS, idPRODUCTOS, CANTIDAD_PRODUCTOS, PRECIO_EN_FECHA) VALUES
(1, 1, 1, 999.99),
(2, 2, 2, 19.99);