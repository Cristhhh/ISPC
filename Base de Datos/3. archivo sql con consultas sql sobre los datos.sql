
-- 1. Una sola tabla (mostrando todos los datos):

SELECT * FROM CLIENTES; -- Selecciona todos los datos de la tabla CLIENTES

-- 2. Una sola tabla (mostrando algunas columnas):

SELECT idCLIENTES, NOMBRE_CLI, APELLIDO FROM CLIENTES; -- Selecciona solo algunas columnas de la tabla CLIENTES

-- 3. Una sola tabla con WHERE:

SELECT * FROM PRODUCTOS WHERE STOCK_PROD > 30; -- Selecciona todos los productos con un stock mayor a 30

-- 4. Una sola tabla con WHERE utilizando BETWEEN:

SELECT * FROM PEDIDOS WHERE MONTO_PEDIDO BETWEEN 100 AND 500; -- Selecciona todos los pedidos cuyo monto está entre 100 y 500

-- 5. Una sola tabla con WHERE utilizando LIMIT:

SELECT * FROM CLIENTES LIMIT 2; -- Selecciona los primeros 2 clientes

-- 6. Más de 1 tabla con INNER JOIN:

SELECT P.*, C.NOMBRE_CLI -- Combina datos de las tablas PEDIDOS y CLIENTES basado en la relación idCLIENTES
FROM PEDIDOS P
INNER JOIN CLIENTES C ON P.idCLIENTES = C.idCLIENTES;

-- 7. Más de 1 tabla con INNER JOIN y con filtros:

SELECT P.*, C.NOMBRE_CLI -- Combina datos de las tablas PEDIDOS y CLIENTES y filtra por pedidos con monto mayor a 200
FROM PEDIDOS P
INNER JOIN CLIENTES C ON P.idCLIENTES = C.idCLIENTES
WHERE P.MONTO_PEDIDO > 200;


-- Opcionales:

-- 8. Una sola tabla con WHERE con operador lógico:

SELECT * FROM PEDIDOS WHERE idPEDIDOS = 1 AND MONTO_PEDIDO > 100; -- Selecciona pedidos con id igual a 1 y monto mayor a 100

-- 9. Una sola tabla con WHERE con operador de comparación:

SELECT * FROM PRODUCTOS WHERE PRECIO_PROD <= 50; -- Selecciona productos con precio igual o menor a 50

-- 10. Una sola tabla con GROUP BY:

SELECT idCATEGORIAS, COUNT(*) AS NUMERO_DE_PRODUCTOS -- Agrupa productos por categoría y cuenta la cantidad de productos en cada categoría
FROM PRODUCTOS
GROUP BY idCATEGORIAS;

-- 11. Una sola tabla con GROUP BY usando alguna función agregada:

SELECT idCATEGORIAS, AVG(PRECIO_PROD) AS PRECIO_PROMEDIO -- Agrupa productos por categoría y calcula el precio promedio en cada categoría
FROM PRODUCTOS
GROUP BY idCATEGORIAS;

-- 12. Más de 1 tabla sin JOIN (solo FROM):

SELECT P.*, D.* -- Combina datos de las tablas PEDIDOS y PEDIDOS_DETALLES basado en la relación idPEDIDOS
FROM PEDIDOS P, PEDIDOS_DETALLES D
WHERE P.idPEDIDOS = D.idPEDIDOS;


