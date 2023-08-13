# Proyecto-Desarrollo
Proyecto final para la materia "Proyecto de Desarrollo" de la carrera Licenciatura en Informática de la Universidad Nacional de San Antonio de Areco (Buenos Aires, Argentina) realizado en el segundo cuatrimestre de 2022. Consiste en un sistema a medida para un establecimiento gastronómico de la localidad de Capitán Sarmiento.
# Sobre el sistema
Esto es un sistema local de gestión de inventario escrito en Python para administrar la siguiente información del modelo de negocio del establecimiento:
- Productos
  - Descripción
  - Stock actual y mínimo
  - Proveedor
  - Precio de venta
  - Fecha de último ingreso
- Proveedores
  - Razón social
  - Contacto (teléfono y correo electrónico)
  - Direccion
  - Descripcion
- Ingresos
  - Fecha
  - Productos
  - Proveedor
# Librerías:
- Pyside6 (GUI)
- SQLite (base de datos)
- Peewee (ORM)

# Construir un ejecutable:
Se recomienda construir el ejecutable con PyInstaller porque permite generarlo para cualquier sistema operativo (siempre y cuando se lo construya desde el SO objetivo). Para esto simplemente se debe utilizar el comando pyinstaller con la ruta correspondiente al archivo main.py de la raíz del proyecto.

Ejemplo en linux:
```
pyinstaller <Ruta del fichero>/Proyecto-Desarrollo/main.py
```
