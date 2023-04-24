from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton,QMessageBox
from PySide6.QtCore import Signal, QLocale
from PySide6.QtGui import QDoubleValidator,QIntValidator
from windows.ui_datosInvalidos import Ui_popupDatosInvalidos
from windows.ui_main import Ui_MenuPrincipal
from windows.ui_newproducto import Ui_newProducto
from windows.ui_confirmEliminar import Ui_confirmEliminar
from windows.ui_newproveedor import Ui_newProveedor

from dbModel import Productos,Proveedores
import crud

#Este archivo contiene las definiciones de todas las ventanas (y sus funciones) del sistema

#Las funciones asociadas a eventos deben estar definidas dentro de la misma definicion de la ventana, sino no funcionan.


#Ventana formulario para modificar/añadir producto
class formularioProducto(QDialog) :
    #La señal de guardado se emite en un guardado exitoso para disparar la actualizacion de la tabla.
    guardado = Signal()
    
    def __init__(self):
        super(formularioProducto,self).__init__()
        self.ui = Ui_newProducto()
        self.ui.setupUi(self)
        #Validadores para campos:
        self.floatValidator = QDoubleValidator()
        self.floatValidator.setBottom(0)
        self.floatValidator.setDecimals(2)
        self.floatValidator.setLocale(QLocale.Language.Spanish)
        self.floatValidator.setNotation(QDoubleValidator.StandardNotation)
        self.ui.lnEditPrecio.setValidator(self.floatValidator)
        self.intValidator = QIntValidator()
        self.intValidator.setBottom(0)
        self.intValidator.setLocale(QLocale.Language.Spanish)
        self.ui.lnEditStockMinimo.setValidator(self.intValidator)
        #Fin Validadores
        self.comboBoxSetup()

    def comboBoxSetup(self):
        listaProveedores = crud.listaProveedores()
        for index,proveedor in enumerate(listaProveedores):
            self.ui.comboxDistr.addItem(proveedor.razonsocial) 
    
    #Validacion de datos en los campos
    def fieldCheckProducto(self):
        if self.ui.lnEditPrecio.hasAcceptableInput():
            print ("el precio es valido")
            if self.ui.lnEditNombre.text() != "":
                print ("la descripción es válida")
                if self.ui.lnEditStockMinimo.text() != "":
                    print("El stock mínimo es válido")
                    if self.ui.comboxDistr.currentText() != "":
                        print("El distribuidor es válido. Todos los datos son válidos.")
                        return "ok"
        #Si alguno de los datos es incorrecto se falla el check
        self.popupDatosInv = popupDatosInvalidos()
        self.popupDatosInv.exec_()

#Popup nuevo producto
class VentanaNewProducto(formularioProducto):
    def __init__(self):
        super(VentanaNewProducto,self).__init__()
        self.ui.buttonBox.accepted.connect(self.guardarProducto)
    
    #Guardar producto
    def guardarProducto(self):
        if self.fieldCheckProducto() == "ok":
            nuevoProducto = Productos() #"Productos" es el nombre del modelo de la tabla
            
            #Se extraen los datos de los campos de la ventana
            nuevoProducto.descripcion = self.ui.lnEditNombre.text()
            precio = self.ui.lnEditPrecio.text().replace(",",".") #se reemplaza la coma por el punto para que el interprete lo reconozca como float
            nuevoProducto.precio_venta = precio
            nuevoProducto.stock_minimo = int(self.ui.lnEditStockMinimo.text())
            cuil_cuit_proveedor = Proveedores.select(Proveedores.cuil_cuit).where(self.ui.comboxDistr.currentText() == Proveedores.razonsocial).get()
            nuevoProducto.cuil_cuit_proveedor = cuil_cuit_proveedor
            
            nuevoProducto.save()
            
            self.guardado.emit()
            self.accept()
        
class VentanaEditProducto(formularioProducto):
    def __init__(self):
        super(VentanaEditProducto,self).__init__()
        self.ui.buttonBox.accepted.connect(self.comprobarCampos)

    def comprobarCampos(self):
        if self.fieldCheckProducto() == "ok":
            #print (self.fieldCheckProducto())
            self.guardado.emit()
            self.accept()

class FormularioProveedor(QDialog):
    
    guardado = Signal()
    
    def __init__(self):
        super(FormularioProveedor, self).__init__()
        self.ui = Ui_newProveedor()
        self.ui.setupUi(self)
        #Validadores para campos:
        self.doubleValidator = QDoubleValidator()
        self.doubleValidator.setBottom(0)
        self.doubleValidator.setTop(999999999999)
        self.doubleValidator.setDecimals(0)
        self.doubleValidator.setLocale(QLocale.Language.Spanish)
        self.ui.lnEditTelefono.setValidator(self.doubleValidator)
        self.ui.lnEditCUIT.setValidator(self.doubleValidator)
        #Fin Validadores
    
    #Validacion de datos en los campos
    def fieldCheckProveedor(self):
        if self.ui.lblRazonSocial.text() != "":
            if self.ui.lnEditDireccion.text() != "":
                print("direccion valida")
                if self.ui.lnEditTelefono.hasAcceptableInput():
                    print("telefono valido")
                    if self.ui.lnEditCUIT.hasAcceptableInput():
                        print("El CUIT/CUIL es válido. Todos los datos son válidos")
                    return "ok"
        #Si alguno de los datos es incorrecto se falla el check
        self.popupDatosInv = popupDatosInvalidos()
        self.popupDatosInv.exec_()

class VentanaEditProveedor(FormularioProveedor):
    def __init__(self):
        super(VentanaEditProveedor,self).__init__()
        self.ui.buttonBox.accepted.connect(self.comprobarCampos)

    def comprobarCampos(self):
        if self.fieldCheckProveedor() == "ok":
            self.guardado.emit()
            self.accept()


class VentanaNewProveedor(FormularioProveedor):
    def __init__(self):
        super(VentanaNewProveedor, self).__init__()
        self.ui.buttonBox.accepted.connect(self.guardarProveedor)
    
    #Guardar producto
    def guardarProveedor(self):
        if self.fieldCheckProveedor() == "ok":
            nuevoProveedor = Proveedores() #"Proveedores" es el nombre del modelo de la tabla
            #Se extraen los datos de los campos de la ventana
            nuevoProveedor.razonsocial = self.ui.lnEditRazonSocial.text()
            nuevoProveedor.direccion = self.ui.lnEditDireccion.text()
            nuevoProveedor.email = self.ui.lnEditEmail.text()
            telefono = int(self.ui.lnEditTelefono.text())
            nuevoProveedor.telefono = telefono
            CUIL_CUIT = int(self.ui.lnEditCUIT.text())
            nuevoProveedor.cuil_cuit = CUIL_CUIT
            nuevoProveedor.nota = self.ui.lnEditNota.text()
            nuevoProveedor.save(force_insert=True)
            
            self.guardado.emit()
            self.accept()
        
#Ventana principal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MenuPrincipal()    
        self.ui.setupUi(self)

        #Conectar botones
        self.ui.btnNuevoProducto.clicked.connect(self.showNewProd)
        self.ui.btnElimProducto.clicked.connect(self.showEliminarProd)
        self.ui.btnModProducto.clicked.connect(self.showEditProd)
        
        self.ui.btnNuevoProveedor.clicked.connect(self.showNewProv)
        self.ui.btnElimProveedor.clicked.connect(self.showEliminarProv)
        self.ui.btnModProveedor.clicked.connect(self.showEditProv)
        
    def showNewProd(self):
        self.w = VentanaNewProducto()
        self.w.guardado.connect(self.updateTablaInventario)
        self.w.show()
    
    def showEliminarProd(self):
        self.popupConfirmacion = popupConfirmElim()
        self.popupConfirmacion.accepted.connect(self.eliminarProducto)
        self.popupConfirmacion.ui.label.setText("¿Desea eliminar este producto?")
        self.popupConfirmacion.setWindowTitle("Eliminar producto")
        self.popupConfirmacion.exec_()
    
    #Elimina el producto si el proceso se confirma
    def eliminarProducto(self):
        row = self.ui.tablaInventario.currentRow()
        idProducto = int(self.ui.tablaInventario.item(row,0).text())
        crud.eliminarProducto(idProducto)
        self.updateTablaInventario()
    
    #Mostrar ventana edicion
    def showEditProd(self):
        self.modProductWindow = VentanaEditProducto()
        self.modProductWindow.setWindowTitle("Editar producto")
        self.modProductWindow.guardado.connect(self.updateTablaInventario)
        row = self.ui.tablaInventario.currentRow()
        descActual = self.ui.tablaInventario.item(row,1).text()
        #stockNuevo = int(self.ui.tablaInventario.item(row,2).text()) 
        stockMinActual = int(self.ui.tablaInventario.item(row,3).text())
        precio = self.ui.tablaInventario.item(row,4).text()
        nombreProveedorActual = self.ui.tablaInventario.item(row,5).text()
        
        self.modProductWindow.ui.lnEditNombre.setText(descActual)
        self.modProductWindow.ui.lnEditPrecio.setText(precio.replace(".",","))
        self.modProductWindow.ui.lnEditStockMinimo.setText(str(stockMinActual))
        self.modProductWindow.ui.comboxDistr.setCurrentText(nombreProveedorActual)
        self.modProductWindow.accepted.connect(self.editProducto)
        self.modProductWindow.exec_()
    
    def editProducto(self):
        #Id del producto seleccionado
        row = self.ui.tablaInventario.currentRow()
        idActual = int(self.ui.tablaInventario.item(row,0).text())
        #Obtener datos nuevos
        print("Se ejecuto editConfirmado")
        descNueva = self.modProductWindow.ui.lnEditNombre.text()
        stockMinNuevo = int(self.modProductWindow.ui.lnEditStockMinimo.text())
        precioNuevo = float(self.modProductWindow.ui.lnEditPrecio.text().replace(",","."))
        proveedorNuevo = (Proveedores
                            .select(Proveedores.cuil_cuit)
                            .where(Proveedores.razonsocial == self.modProductWindow.ui.comboxDistr.currentText())
                            .get())
        #Update query
        qry =(Productos
         .update(descripcion = descNueva,stock_minimo = stockMinNuevo,precio_venta = precioNuevo, cuil_cuit_proveedor = proveedorNuevo)
         .where(Productos.id == idActual))
        qry.execute()
        
        self.updateTablaInventario()  
        
    def showNewProv(self):
        self.newProv = VentanaNewProveedor()
        self.newProv.guardado.connect(self.updateTablaProveedores)
        self.newProv.show()
    
    def showEliminarProv(self):
        self.popupConfirmacion = popupConfirmElim()
        self.popupConfirmacion.accepted.connect(self.eliminarProveedor)
        self.popupConfirmacion.ui.label.setText("¿Desea eliminar este proveedor?")
        self.popupConfirmacion.setWindowTitle("Eliminar proveedor")
        self.popupConfirmacion.exec_()
    
    #Elimina el proveedor si el proceso se confirma
    def eliminarProveedor(self):
        row = self.ui.tablaProveedores.currentRow()
        cuilProveedor = int(self.ui.tablaProveedores.item(row,0).text())
        crud.eliminarProveedor(cuilProveedor)
        self.updateTablaProveedores()
    
    def showEditProv(self):
        self.modProvWindow = VentanaEditProveedor()
        self.modProvWindow.setWindowTitle("Editar proveedor")
        self.modProvWindow.guardado.connect(self.updateTablaProveedores)
        
        #comprobar si hay un elemento seleccionado
        row = self.ui.tablaProveedores.currentRow()
        
        cuilActual = self.ui.tablaProveedores.item(row,0).text()
        razonActual = self.ui.tablaProveedores.item(row,1).text()
        telefonoActual = int(self.ui.tablaProveedores.item(row,2).text())
        emailActual = self.ui.tablaProveedores.item(row,3).text()
        direccionActual = self.ui.tablaProveedores.item(row,4).text()
        notaActual = self.ui.tablaProveedores.item(row,5).text()
        
        self.modProvWindow.ui.lnEditCUIT.setText(cuilActual)
        self.modProvWindow.ui.lnEditRazonSocial.setText(razonActual)
        self.modProvWindow.ui.lnEditTelefono.setText(str(telefonoActual))
        self.modProvWindow.ui.lnEditEmail.setText(emailActual)
        self.modProvWindow.ui.lnEditDireccion.setText(direccionActual)
        self.modProvWindow.ui.lnEditNota.setText(notaActual)

        self.modProvWindow.accepted.connect(self.saveEditProveedor)
        self.modProvWindow.exec_()
        
    def saveEditProveedor(self):
        #Id del proveedor seleccionado
        row = self.ui.tablaProveedores.currentRow()
        cuilActual = int(self.ui.tablaProveedores.item(row,0).text())
        #Obtener datos nuevos
        cuilNuevo = int(self.modProvWindow.ui.lnEditCUIT.text())
        razonNueva = self.modProvWindow.ui.lnEditRazonSocial.text()
        telefonoNuevo = int(self.modProvWindow.ui.lnEditTelefono.text())
        emailNuevo = self.modProvWindow.ui.lnEditEmail.text()
        direccionNueva = self.modProvWindow.ui.lnEditDireccion.text()
        notaNueva = self.modProvWindow.ui.lnEditNota.text()
        
        #Update query
        qry =(Proveedores
         .update(cuil_cuit = cuilNuevo, razonsocial = razonNueva,telefono = telefonoNuevo
                 , email = emailNuevo, direccion = direccionNueva, nota = notaNueva)
         .where(Proveedores.cuil_cuit == cuilActual))
        qry.execute()
        
        self.updateTablaProveedores()
    
    #Actualiza tabla Inventario en main window
    def updateTablaInventario(self):
        crud.poblarQTableInventario(self.ui.tablaInventario)
    
    def updateTablaProveedores(self):
        crud.poblarQTableProveedores(self.ui.tablaProveedores)
  
#Popup datos ingresados inválidos
class popupDatosInvalidos(QDialog) :
        
    def __init__(self):
        super(popupDatosInvalidos,self).__init__()
        self.ui = Ui_popupDatosInvalidos()
        self.ui.setupUi(self)
        
#Popup confirmacion eliminar producto
class popupConfirmElim(QDialog) :
        
    def __init__(self):
        super(popupConfirmElim,self).__init__()
        self.ui = Ui_confirmEliminar()
        self.ui.setupUi(self)