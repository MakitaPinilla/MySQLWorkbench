# EVALUACIÓN DE PORTAFOLIO MÓDULO 5: DB INVENTARIO

# -------------------------------
# 1. CREACIÓN DE LA BASE DE DATOS
# -------------------------------

# Se crea una base de datos llamada "inventario"
# CREATE DATABASE IF NOT EXISTS inventario
# USE inventario

# --------------------------------
# ENTIDAD: proveedores
# - Esta tabla almacena los datos de los proveedores de productos
# - PK (clave primaria): id_proveedor
# --------------------------------
# CREATE TABLE proveedores (
#     id_proveedor INT AUTO_INCREMENT PRIMARY KEY,  # PK
#     nombre VARCHAR(45) NOT NULL,
#     direccion VARCHAR(150),
#     telefono VARCHAR(20),
#     email VARCHAR(45)
# )

# --------------------------------
# ENTIDAD: productos
# - Representa los productos disponibles en la tienda
# - PK: id_producto
# --------------------------------
# CREATE TABLE productos (
#     id_producto INT AUTO_INCREMENT PRIMARY KEY,  # PK
#     nombre VARCHAR(45) NOT NULL,
#     descripcion TEXT,
#     precio DECIMAL(10, 2) NOT NULL,
#     cantidad INT NOT NULL
# )

# --------------------------------
# ENTIDAD RELACIONAL: transacciones
# - Registra compras y ventas de productos
# - PK: id_transaccion
# - FK: id_producto → productos
# - FK: id_proveedor → proveedores
# --------------------------------
# CREATE TABLE transacciones (
#     id_transaccion INT AUTO_INCREMENT PRIMARY KEY,  # PK
#     tipo ENUM('compra', 'venta') NOT NULL,  # Tipo de operación
#     fecha DATE NOT NULL,
#     cantidad INT NOT NULL,
#     id_producto INT NOT NULL,  # FK hacia productos
#     id_proveedor INT NOT NULL,  # FK hacia proveedores
#     FOREIGN KEY(id_producto) REFERENCES productos(id_producto),
#     FOREIGN KEY(id_proveedor) REFERENCES proveedores(id_proveedor)
# )

# USE inventario  # Asegura que se esté usando la base de datos

# -------------------------------
# 2. INSERTAR DATOS (POBLAR TABLAS)
# -------------------------------

# Insertar datos de ejemplo en proveedores
# INSERT INTO proveedores (nombre, direccion, telefono, email)
# VALUES
# ('Distribuidora ChileSur', 'Av. Providencia 1234, Santiago', '987654321', 'contacto@chilesur.cl'),
# ('Importadora Andes', 'Av. Los Leones 432, Viña del Mar', '912345678', 'ventas@andesimport.cl'),
# ('TecnoPro S.A.', 'Calle Colón 987, Concepción', '965432189', 'info@tecnopro.cl')

# Insertar productos
# INSERT INTO productos (nombre, descripcion, precio, cantidad)
# VALUES
# ('Notebook Lenovo', 'Notebook 15.6", Intel Core i5, 8GB RAM, 256GB SSD', 499990, 20),
# ('Monitor LG 24"', 'Monitor LED Full HD 24 pulgadas', 129990, 35),
# ('Mouse inalámbrico Logitech', 'Mouse inalámbrico con receptor USB', 14990, 100)

# Insertar transacciones (compras y ventas)
# INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
# VALUES
# ('compra', '2025-09-01', 10, 1, 1),
# ('venta', '2025-09-02', 2, 1, 1),
# ('compra', '2025-09-03', 50, 3, 2),
# ('venta', '2025-09-05', 5, 3, 2),
# ('compra', '2025-09-07', 15, 2, 3)

# -------------------------------
# 3. CONSULTAS BÁSICAS EN SQL
# -------------------------------

# Mostrar toda la información de las tres tablas
# SELECT * FROM proveedores
# SELECT * FROM productos
# SELECT * FROM transacciones

# Calcular el total de productos comprados
# SELECT SUM(cantidad) AS total_comprados
# FROM transacciones
# WHERE tipo = 'compra'

# Registrar nueva venta de 3 notebooks (id_producto = 1)
# INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
# VALUES ('venta', '2025-09-11', 3, 1, 1)

# Actualizar el stock del producto después de la venta
# UPDATE productos
# SET cantidad = cantidad - 3
# WHERE id_producto = 1

# -------------------------------
# 4. TRANSACCIONES EN SQL
# -------------------------------

# Iniciar una transacción para realizar una compra
# START TRANSACTION

# Insertar compra de 5 monitores (id_producto = 2)
# INSERT INTO transacciones (tipo, fecha, cantidad, id_producto, id_proveedor)
# VALUES ('compra', '2025-09-11', 5, 2, 1)

# Actualizar stock del producto comprado
# UPDATE productos
# SET cantidad = cantidad + 5
# WHERE id_producto = 2

# Confirmar cambios si todo está bien
# COMMIT

# Revertir los cambios si hay un error antes del commit
# ROLLBACK

# -------------------------------
# 5. CONSULTAS COMPLEJAS
# -------------------------------

# 5.1 Total de ventas del producto con ID 1 durante el mes anterior
# SELECT
#     id_producto,
#     SUM(cantidad) AS total_vendido
# FROM
#     transacciones
# WHERE
#     tipo = 'venta'
#     AND MONTH(fecha) = MONTH(CURDATE() - INTERVAL 1 MONTH)
#     AND id_producto = 1
# GROUP BY id_producto

# 5.2 JOIN: Total de compras del mes anterior del producto con ID 1
# SELECT
#     p.nombre AS producto,
#     SUM(t.cantidad) AS total_comprado
# FROM
#     transacciones t
# JOIN
#     productos p ON t.id_producto = p.id_producto  # Relación por FK
# WHERE
#     t.tipo = 'compra'
#     AND MONTH(t.fecha) = MONTH(CURDATE() - INTERVAL 1 MONTH)
#     AND p.id_producto = 1
# GROUP BY
#     p.nombre

# 5.3 SUBCONSULTA: Mostrar nombres de productos que tuvieron ventas el mes pasado
# SELECT
#     nombre
# FROM
#     productos
# WHERE
#     id_producto IN (
#         SELECT id_producto
#         FROM transacciones
#         WHERE tipo = 'venta'
#         AND MONTH(fecha) = MONTH(CURDATE() - INTERVAL 1 MONTH)
#     )

# -------------------------------
# 6. NORMALIZACIÓN (HASTA 3FN)
# -------------------------------

# - La tabla productos tiene cada atributo en su propia columna (1FN)
# - Todos los campos dependen de su clave primaria y no de partes de ella (2FN)
# - No hay campos que dependan de otros campos no clave (3FN)
# - Las claves foráneas (FK) permiten relacionar las tablas sin duplicar datos
# - Resultado: base de datos más ordenada, sin redundancias, y fácil de mantener
