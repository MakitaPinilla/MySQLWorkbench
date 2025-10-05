# Proyecto SQL - Inventario Electrónica

Este repositorio contiene un conjunto de consultas y comandos SQL usados para crear y gestionar una base de datos de inventario de una tienda de productos electrónicos.

## Contenido

- Creación de la base de datos y tablas (`proveedores`, `productos`, `transacciones`)
- Inserción de datos de prueba
- Consultas básicas: `SELECT`, `INSERT`, `UPDATE`
- Consultas avanzadas: `JOIN`, subconsultas, `SUM`, `GROUP BY`
- Ejemplo de transacciones con `START TRANSACTION`, `COMMIT`, y `ROLLBACK`
- Explicación de normalización (1FN, 2FN, 3FN)

## Cómo usar en MySQL Workbench

1. **Abrir MySQL Workbench**
2. **Crear una nueva conexión** o usar una existente
3. **Abrir el archivo SQL**:
   - Haz clic en `File > Open SQL Script...`
   - Selecciona el archivo `consultas_inventario.sql` o el nombre que tenga tu archivo
4. **Seleccionar la base de datos** si no está activa:
   - Asegúrate de ejecutar:  
     ```sql
     USE inventario;
     ```
5. **Ejecutar los bloques de código**:
   - Puedes ejecutar línea por línea o por secciones (Ctrl + Enter en Windows, Cmd + Enter en Mac)

> **Nota:** Si copiaste el código dentro de un archivo `.py` como referencia, puedes copiar los bloques de código SQL desde ahí y pegarlos en MySQL Workbench para ejecutarlos.

## Requisitos

- Tener MySQL Server y MySQL Workbench instalados
- Usuario con permisos para crear bases de datos y tablas

## Autor

Proyecto desarrollado como parte del Módulo 5 del curso Full Stack Python.
