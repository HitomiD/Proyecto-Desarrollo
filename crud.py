from dbModel import *
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

#Este modulo contiene todas las interacciones directas con la base de datos.

#Poblar tabla inventario
def poblarQTableInventario(tabla):
    
    #settear cantidad de lineas para la tabla
    totalRegistros = Productos.select().count()
    tabla.setRowCount(totalRegistros)
    #El select incluye un join para incluir la razón social del proveedor asociado a cada producto.
    listaProductos = (Productos
                      .select(Productos.id,Productos.descripcion,Productos.stock,Productos.stock_minimo,Productos.precio_venta, Proveedores.razonsocial)
                      .join(Proveedores, JOIN.LEFT_OUTER, on=(Productos.cuil_cuit_proveedor == Proveedores.cuil_cuit))
                      .namedtuples()) #namedtuples() es para retornar un diccionario.

    for index, producto in enumerate(listaProductos):
        itemId = QTableWidgetItem()
        itemId.setData(0,producto.id)
        tabla.setItem(index,0,itemId)
        
        #En caso de ser un string se puede omitir la funcion setData de la siguiente forma
        tabla.setItem(index,1,QTableWidgetItem(producto.descripcion))
        
        itemStock = QTableWidgetItem()
        itemStock.setData(0,producto.stock)
        tabla.setItem(index,2,itemStock)
        
        itemStockMin = QTableWidgetItem()
        itemStockMin.setData(0,producto.stock_minimo)
        tabla.setItem(index,3,itemStockMin)
        
        itemPrecio = QTableWidgetItem()
        itemPrecio.setData(0,producto.precio_venta)
        tabla.setItem(index,4,itemPrecio)
        
        itemProveedor = QTableWidgetItem()
        itemProveedor.setData(0,producto.razonsocial)
        tabla.setItem(index,5,itemProveedor)
    
        #Completar mas adelante con la fecha del último ingreso 
        
def poblarQTableProveedores(tabla):
    
    #settear cantidad lineas
    totalRegistros = Proveedores.select().count()
    tabla.setRowCount(totalRegistros)
    listaProveedores = Proveedores.select()
    
    for index, proveedor in enumerate(listaProveedores):
        
        itemId = QTableWidgetItem()
        itemId.setData(0,proveedor.cuil_cuit)
        tabla.setItem(index,0,itemId)
        
        tabla.setItem(index,1,QTableWidgetItem(proveedor.razonsocial))
        
        itemStock = QTableWidgetItem()
        itemStock.setData(0,proveedor.telefono)
        tabla.setItem(index,2,itemStock)
        
        tabla.setItem(index,3,QTableWidgetItem(proveedor.email))
        
        tabla.setItem(index,4,QTableWidgetItem(proveedor.direccion))
        
        tabla.setItem(index,5,QTableWidgetItem(proveedor.nota))

def poblarQTableIngresos(tabla):
    
    #settear cantidad lineas
    totalRegistros = Ingresos.select().count()
    tabla.setRowCount(totalRegistros)
    listaIngresos = Ingresos.select()
    
    for index, ingreso in enumerate(listaIngresos):
        
        itemId = QTableWidgetItem()
        itemId.setData(0,ingreso.num_ingreso)
        tabla.setItem(index,0,itemId)
        
        itemId = QTableWidgetItem()
        itemId.setData(0,ingreso.fecha)
        tabla.setItem(index,1,itemId)
        
        itemStock = QTableWidgetItem()
        itemStock.setData(0,"nombre proveedor") #placeholder
        tabla.setItem(index,2,itemStock)

#Retorna una lista de proveedores para la comboBox de la ventana para añadir un producto.
def listaProveedores():
    listaProveedores = (Proveedores
                      .select(Proveedores.cuil_cuit,Proveedores.razonsocial)
                      .namedtuples()) #namedtuples() es para retornar un diccionario.
    return listaProveedores

def eliminarProducto(idProducto):
    qry=Productos.delete().where(Productos.id == idProducto)
    qry.execute()
    
def eliminarProveedor(cuilProveedor):
    qry = Proveedores.delete().where(Proveedores.cuil_cuit == cuilProveedor)
    qry.execute()


def poblarTablaProductosIngreso(tabla,razonSocial):
        
    query = (Proveedores
                 .select(Proveedores.cuil_cuit)
                 .where(Proveedores.razonsocial == razonSocial))
    #Si se le asigna la query en si directamente a cuilCuitProveedor no funciona (¿?).
    cuilCuitProveedor = query  
    
    
    listaProductos = (Productos
                      .select(Productos.id,Productos.descripcion,Productos.stock,Productos.stock_minimo)
                      .where(Productos.cuil_cuit_proveedor == cuilCuitProveedor)
                      .namedtuples()) #namedtuples() es para retornar un diccionario.
    
    
    #settear cantidad de lineas para la tabla
    query = (Productos
             .select(Productos.id,Productos.descripcion,Productos.stock,Productos.stock_minimo,)
            .where(Productos.cuil_cuit_proveedor == cuilCuitProveedor))
    
    totalRegistros = (Productos
                    .select(Productos.id)
                    .where(Productos.cuil_cuit_proveedor == cuilCuitProveedor).count())
    tabla.setRowCount(totalRegistros)

    #id,descripcion,stock,stock minimo
    for index, producto in enumerate(listaProductos):
        #id
        itemId = QTableWidgetItem()
        itemId.setData(0,producto.id)
        tabla.setItem(index,0,itemId)
        
        #Descripcion
        #En caso de ser un string se puede omitir la funcion setData de la siguiente forma
        tabla.setItem(index,1,QTableWidgetItem(producto.descripcion))
        
        #Stock
        itemStock = QTableWidgetItem()
        itemStock.setData(0,producto.stock)
        tabla.setItem(index,2,itemStock)
        
        #Stock minimo
        itemStockMin = QTableWidgetItem()
        itemStockMin.setData(0,producto.stock_minimo)
        tabla.setItem(index,3,itemStockMin)
        
def listaProductosDeProveedor(razonSocial):
    
    query = (Proveedores
                 .select(Proveedores.cuil_cuit)
                 .where(Proveedores.razonsocial == razonSocial))
    #Si se le asigna la query en si directamente a cuilCuitProveedor no funciona (¿?).
    cuilCuitProveedor = query  
    
    
    lista = (Productos
            .select(Productos.id,Productos.descripcion,Productos.stock,Productos.stock_minimo)
            .where(Productos.cuil_cuit_proveedor == cuilCuitProveedor)
            .namedtuples()) #namedtuples() es para retornar un diccionario.
    
    return list(lista)


def poblarTablaProductosIng(tabla,listaProductos):
    
    totalRegistros = len(listaProductos)
    tabla.setRowCount(totalRegistros)

    #id,descripcion,stock,stock minimo
    for index, producto in enumerate(listaProductos):
        #id
        itemId = QTableWidgetItem()
        itemId.setData(0,producto.id)
        tabla.setItem(index,0,itemId)
        
        #Descripcion
        #En caso de ser un string se puede omitir la funcion setData de la siguiente forma
        tabla.setItem(index,1,QTableWidgetItem(producto.descripcion))
        
        #Stock
        itemStock = QTableWidgetItem()
        itemStock.setData(0,producto.stock)
        tabla.setItem(index,2,itemStock)
        
        #Stock minimo
        itemStockMin = QTableWidgetItem()
        itemStockMin.setData(0,producto.stock_minimo)
        tabla.setItem(index,3,itemStockMin)
        
def poblarTablaProdSeleccionados(tabla,listaProductos):
    
    totalRegistros = len(listaProductos)
    tabla.setRowCount(totalRegistros)

    #id,descripcion,stock,stock minimo
    for index, producto in enumerate(listaProductos):

        #id
        itemId = QTableWidgetItem()
        itemId.setData(0,producto.ID)
        tabla.setItem(index,0,itemId)
        
        #Descripcion
        #En caso de ser un string se puede omitir la funcion setData de la siguiente forma
        tabla.setItem(index,1,QTableWidgetItem(producto.descripcion))
        
        #Stock
        itemCantidad = QTableWidgetItem()
        itemCantidad.setData(0,producto.cantidad)
        tabla.setItem(index,2,itemCantidad)    