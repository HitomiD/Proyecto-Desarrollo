BEGIN TRANSACTION;

INSERT INTO productos (descripcion,stock,stock_minimo,precio_venta) VALUES('Coca-Coca 1L','30','25','200');
INSERT INTO productos (descripcion,stock,stock_minimo,precio_venta) VALUES('Esprait 1L','50','25','200');
INSERT INTO productos (descripcion,stock,stock_minimo,precio_venta) VALUES('Kilmes 1L','60','20','250');

INSERT INTO proveedores (CUIL_CUIT,razonsocial,direccion,telefono,email,nota) VALUES ('20237852347','Juan pablo','salta 234','2478342344','juanpablo@mail.com','bebidas');

INSERT INTO ingresos (CUIL_CUIT_proveedor,fecha) VALUES('20237852347','12/12/22');

INSERT INTO Productos_por_Ingreso(ID_producto,num_ingreso,precio_unitario_compra,cantidad) VALUES ('1', '1','150','50');
END TRANSACTION;