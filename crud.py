from dbModel import *
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
#Insertar X objeto en Y tabla
    

#Actualizar x objeto en Y tabla

#Eliminar X objeto de Y tabla
#Carga qtablewidget
    

def poblarQTableInventario(tabla):
    totalRegistros = Productos.select().count()
    tabla.setRowCount(totalRegistros)
    listaProductos = Productos.select()
    
    for index, producto in enumerate(listaProductos):
        itemId = QTableWidgetItem()
        itemId.setData(0,producto.id)
        tabla.setItem(index,0,itemId)
        
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
        #Completar mas adelante con la descripción del proveedor y la fecha del último ingreso
        
#actualizar tabla