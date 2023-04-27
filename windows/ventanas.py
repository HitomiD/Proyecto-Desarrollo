from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton,QMessageBox
from PySide6.QtCore import Signal, QLocale
from PySide6.QtGui import QDoubleValidator,QIntValidator
from windows.ui_datosInvalidos import Ui_popupDatosInvalidos
from windows.ui_main import Ui_MenuPrincipal
from windows.ui_newproducto import Ui_newProducto
from windows.ui_confirmEliminar import Ui_confirmEliminar
from windows.ui_newproveedor import Ui_newProveedor
from windows.error_ui import Ui_ErrorDialog
from windows.AltaIngresoInicio_ui import Ui_InicioNuevoIngreso
from windows.AltaIngreso_ui import Ui_ventanaNuevoIngreso

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

#Popup inicial de alta de ingreso
class PopupIngresoNuevo(QDialog):
    
    proveedorGuardado = Signal()
    productoGuardado = Signal()
    
    def __init__(self):
        super(PopupIngresoNuevo,self).__init__()
        self.ui = Ui_InicioNuevoIngreso()
        self.ui.setupUi(self)
        self.ui.btnNuevoProveedor.clicked.connect(self.showNewProvIngreso)
        self.ui.buttonBox.accepted.connect(self.showNewIngreso)

        self.comboBoxSetup()
    #Aca no se obtiene la fecha, eso esta declarado en AltaIngresoInicio_ui.py
            
    def showNewProvIngreso(self):
        self.newProv = VentanaNewProveedor()
        #Se vuelve a la ventana si:
        self.newProv.guardado.connect(self.show) #Se completa el guardado
        self.newProv.rejected.connect(self.show) #Se cancela el guardado
        self.newProv.accepted.connect(self.proveedorGuardado.emit)
        self.proveedorGuardado.connect(self.comboBoxSetup) #Si se completa se actualiza el combobox
        #self.newProv.guardado.connect(self.proveedorGuardado)
        self.hide()
        self.newProv.show()
        
        #Implementar si se puede algo que seleccione automáticamente en
        # el combobox el proveedor recien registrado
        
    
    #LLamada a la siguiente ventana
    def showNewIngreso(self):
        self.hide()
        self.ventanaNuevoIngreso = VentanaNuevoIngreso()
        #Se pasa la señal de nuevo Ingreso a nuevo Ingreso popup para registrarla en ventanaPrincipal
        #y actualizar la tabla de proveedores
        razonSocial = self.ui.comboxDistr.currentText()
        self.ventanaNuevoIngreso.productoGuardado.connect(self.productoGuardado.emit)
        self.ventanaNuevoIngreso.rejected.connect(self.show)
        fecha = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        self.ventanaNuevoIngreso.ui.lblFechaValor.setText(fecha)
        self.ventanaNuevoIngreso.ui.lblProveedorValor.setText(razonSocial)
        self.ventanaNuevoIngreso.accepted.connect(self.accept)
        #Guardar el ingreso
        #self.ventanaNuevoIngreso.accepted.connect(self.guardarIngreso)
        #Poblar tabla desde la base de datos
        #crud.poblarTablaProductosIngreso(self.ventanaNuevoIngreso.ui.tablaProdDisponibles,self.ventanaNuevoIngreso.ui.lblProveedorValor.text())
        
        #Poblar tabla usando una lista de productos de la propia clase
        self.ventanaNuevoIngreso.listaProductos = crud.listaProductosDeProveedor(razonSocial)
        crud.poblarTablaProductosIng(self.ventanaNuevoIngreso.ui.tablaProdDisponibles,self.ventanaNuevoIngreso.listaProductos)
        
        self.ventanaNuevoIngreso.show()
        
    
    #setup combox proveedores
    def comboBoxSetup(self):
        listaProveedores = crud.listaProveedores()
        for index,proveedor in enumerate(listaProveedores):
            self.ui.comboxDistr.addItem(proveedor.razonsocial)
    
    

#Ventana de ingreso (seleccion productos)
class VentanaNuevoIngreso(QDialog):
    
    productoGuardado = Signal()
    listaProdSeleccionados = [] #Lista de seleccionados
    listaProductosEliminados = []
    def __init__(self):
        super(VentanaNuevoIngreso,self).__init__()
        self.ui = Ui_ventanaNuevoIngreso()
        self.ui.setupUi(self)
        self.ui.btnRegistrarProd.clicked.connect(self.showNewProdIngreso)
        #Actualiza la tabla completa desde la base de datos.        
        self.productoGuardado.connect(self.updateTablaProductosIngreso)
        self.ui.btnAgregarSeleccionado.clicked.connect(self.seleccionarProducto)
        
    
    def showNewProdIngreso(self):
        
        razonSocial = self.ui.lblProveedorValor.text()
        
        self.newProd = VentanaNewProducto()
        self.newProd.ui.comboxDistr.setCurrentText(razonSocial)
        self.newProd.ui.comboxDistr.setDisabled(True)
        #Se vuelve a la ventana si:
        self.newProd.guardado.connect(self.show) #Se completa el guardado
        self.newProd.rejected.connect(self.show) #Se cancela el guardado
        #Se pasa la señal de guardado de la ventana de proveedor a la ventana anterior (IngresoInicio)
        self.newProd.accepted.connect(self.productoGuardado.emit)
        
        self.hide()
        self.newProd.show()
        
    def seleccionarProducto(self):
        
        row = self.ui.tablaProdDisponibles.currentRow()
        if row == -1:
            popup = popupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        if int(self.ui.spinBox.text()) == 0:
            popup = popupError()
            popup.ui.label.setText("No se ha indicado la cantidad.")
            popup.exec()
            return
        
        idSeleccionado = int(self.ui.tablaProdDisponibles.item(row,0).text())
        
        class productoSeleccionado():
            ID = int
            descripcion = str
            cantidad = int
        
        #Buscar y eliminar producto seleccionado de la lista en memoria
        for index,producto in enumerate(self.listaProductos):
            if producto.id == idSeleccionado:
                productoMover = producto
                del self.listaProductos[index]
        productoSelec = productoSeleccionado()
        productoSelec.descripcion = productoMover.descripcion
        productoSelec.ID = productoMover.id
        productoSelec.cantidad = int(self.ui.spinBox.text())
        self.listaProdSeleccionados.append(productoSelec)
        print(self.listaProdSeleccionados[0].descripcion)
        self.updateTablaProductosIngreso()
        self.updateTablaProdSeleccionados()
        
        

        
    def updateTablaProductosIngreso(self):
        crud.poblarTablaProductosIng(self.ui.tablaProdDisponibles,self.listaProductos)
    
    def updateTablaProdSeleccionados(self):
        crud.poblarTablaProdSeleccionados(self.ui.tablaDetalleIngreso,self.listaProdSeleccionados)
        
#Ventana principal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MenuPrincipal()   
        self.ui.setupUi(self)
        #poblado inicial tablas
        crud.poblarQTableInventario(self.ui.tablaInventario)
        crud.poblarQTableProveedores(self.ui.tablaProveedores) 

        #Conectar botones
        self.ui.btnNuevoProducto.clicked.connect(self.showNewProd)
        self.ui.btnElimProducto.clicked.connect(self.showEliminarProd)
        self.ui.btnModProducto.clicked.connect(self.showEditProd)
        
        self.ui.btnNuevoProveedor.clicked.connect(self.showNewProv)
        self.ui.btnElimProveedor.clicked.connect(self.showEliminarProv)
        self.ui.btnModProveedor.clicked.connect(self.showEditProv)
        
        self.ui.btnNuevoIngreso.clicked.connect(self.showNewIngresoInicio)
        
    def showNewProd(self):
        self.w = VentanaNewProducto()
        self.w.guardado.connect(self.updateTablaInventario)
        self.w.show()
    
    def showEliminarProd(self):
        
        #comprobar si hay un elemento seleccionado
        row = self.ui.tablaInventario.currentRow()
        if row == -1:
            popup = popupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        
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
        
        row = self.ui.tablaInventario.currentRow()
        if row == -1:
            popup = popupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        
        self.modProductWindow = VentanaEditProducto()
        self.modProductWindow.setWindowTitle("Editar producto")
        self.modProductWindow.guardado.connect(self.updateTablaInventario)
        
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
        
        #comprobar si hay un elemento seleccionado
        row = self.ui.tablaProveedores.currentRow()
        if row == -1:
            popup = popupError()
            popup.ui.label.setText("No se ha seleccionado ningún proveedor.")
            popup.exec()
            return
        
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
        
        #comprobar si hay un elemento seleccionado
        row = self.ui.tablaProveedores.currentRow()
        if row == -1:
            popup = popupError()
            popup.ui.label.setText("No se ha seleccionado ningún proveedor.")
            popup.exec()
            return
        
        self.modProvWindow = VentanaEditProveedor()
        self.modProvWindow.setWindowTitle("Editar proveedor")
        self.modProvWindow.guardado.connect(self.updateTablaProveedores)
        
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
    
    def showNewIngresoInicio(self):
        self.newIngresoWindow = PopupIngresoNuevo()
        #Al registrar la señal de guardado se llama a un update de la tabla
        self.newIngresoWindow.proveedorGuardado.connect(self.updateTablaProveedores)
        self.newIngresoWindow.productoGuardado.connect(self.updateTablaInventario)

        self.newIngresoWindow.exec()
    
    
    
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
        
#Popup error
class popupError(QDialog) :

    def __init__(self):
        super(popupError,self).__init__()
        self.ui = Ui_ErrorDialog()
        self.ui.setupUi(self)

#Popup confirmacion eliminar producto
class popupConfirmElim(QDialog) :
        
    def __init__(self):
        super(popupConfirmElim,self).__init__()
        self.ui = Ui_confirmEliminar()
        self.ui.setupUi(self)