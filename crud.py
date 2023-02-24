from dbModel import *
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
#Insertar X objeto en Y tabla
    

#Actualizar x objeto en Y tabla

#Eliminar X objeto de Y tabla

#Poblar tabla inventario
def poblarQTableInventario(tabla):
    
    #settear cantidad lineas
    totalRegistros = Productos.select().count()
    tabla.setRowCount(totalRegistros)
    #El select incluye un join para incluir la razón social del proveedor asociado a cada producto.
    listaProductos = (Productos
                      .select(Productos.id,Productos.descripcion,Productos.stock,Productos.stock_minimo,Productos.precio_venta, Proveedores.razonsocial)
                      .join(Proveedores, JOIN.LEFT_OUTER, on=(Productos.cuil_cuit_proveedor == Proveedores.cuil_cuit))
                      .namedtuples()) #Esto evita que se retorne un objeto de tipo "Productos".


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
        
#actualizar tabla