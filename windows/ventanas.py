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

import datetime
import dbModel
from dbModel import Productos,Proveedores,Ingresos, ProductosPorIngreso
import crud

#Este archivo contiene las definiciones de todas las ventanas (y sus funciones) del sistema

#Las funciones asociadas a eventos deben estar definidas dentro de la misma definicion de la ventana, sino no funcionan.


#Ventana formulario para modificar/añadir producto
class FormularioProducto(QDialog) :
    #La señal de guardado se emite en un guardado exitoso para disparar la actualizacion de la tabla.
    saved_signal = Signal()
    
    def __init__(self):
        super(FormularioProducto,self).__init__()
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
        lista_proveedores = crud.listaProveedores()
        for index,proveedor in enumerate(lista_proveedores):
            self.ui.comboxDistr.addItem(proveedor.razonsocial) 
    
    #Validacion de datos en los campos
    def fieldCheckProducto(self):
        if self.ui.lnEditPrecio.hasAcceptableInput():
            print ("el precio es valido")   #Mensajes para depuración via consola
            if self.ui.lnEditNombre.text() != "":
                print ("la descripción es válida")
                if self.ui.lnEditStockMinimo.text() != "":
                    print("El stock mínimo es válido")
                    if self.ui.comboxDistr.currentText() != "":
                        print("El distribuidor es válido. Todos los datos son válidos.")
                        return "ok" #Esto es una crotada.
        #Si el check falla:
        self.popup_datos_invalidos = PopupDatosInvalidos()
        self.popup_datos_invalidos.exec_()

#Popup nuevo producto
class VentanaNewProducto(FormularioProducto):
    def __init__(self):
        super(VentanaNewProducto,self).__init__()
        self.ui.buttonBox.accepted.connect(self.guardarProducto)
    
    #Guardar producto
    def guardarProducto(self):
        if self.fieldCheckProducto() == "ok": #Reitero, crotada.
            producto_nuevo = dbModel.Productos() #Model de tabla
            
            #Se extraen los datos de los campos de la ventana
            producto_nuevo.descripcion = self.ui.lnEditNombre.text()
            precio = self.ui.lnEditPrecio.text().replace(",",".") #se reemplaza la coma por el punto para que el interprete lo reconozca como float
            producto_nuevo.precio_venta = precio
            producto_nuevo.stock_minimo = int(self.ui.lnEditStockMinimo.text())
            cuil_cuit_proveedor = Proveedores.select(Proveedores.cuil_cuit).where(self.ui.comboxDistr.currentText() == Proveedores.razonsocial).get()
            producto_nuevo.cuil_cuit_proveedor = cuil_cuit_proveedor
            
            producto_nuevo.save()
            
            self.saved_signal.emit()
            self.accept()
        
class VentanaEditProducto(FormularioProducto):
    def __init__(self):
        super(VentanaEditProducto,self).__init__()
        self.ui.buttonBox.accepted.connect(self.comprobarCampos)

    def comprobarCampos(self): #Totalmente redundante existiendo fieldCheckProducto(), revisar.
        if self.fieldCheckProducto() == "ok": #REITERO NUEVAMENTE, CROTADA.
            self.saved_signal.emit()
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
                print("direccion valida") #Mensajes para depurar via consola.
                if self.ui.lnEditTelefono.hasAcceptableInput():
                    print("telefono valido")
                    if self.ui.lnEditCUIT.hasAcceptableInput():
                        print("El CUIT/CUIL es válido. Todos los datos son válidos")
                    return "ok"
        #Si falla el check:
        self.popupDatosInv = PopupDatosInvalidos()
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
            proveedor_nuevo = dbModel.Proveedores()
            #Se extraen los datos de los campos de la ventana
            proveedor_nuevo.razonsocial = self.ui.lnEditRazonSocial.text()
            proveedor_nuevo.direccion = self.ui.lnEditDireccion.text()
            proveedor_nuevo.email = self.ui.lnEditEmail.text()
            telefono = int(self.ui.lnEditTelefono.text())
            proveedor_nuevo.telefono = telefono
            CUIL_CUIT = int(self.ui.lnEditCUIT.text())
            proveedor_nuevo.cuil_cuit = CUIL_CUIT
            proveedor_nuevo.nota = self.ui.lnEditNota.text()
            proveedor_nuevo.save(force_insert=True)
            
            self.guardado.emit()
            self.accept()

#Popup inicial (fecha y proveedor) de alta de ingreso
class PopupIngresoNuevo(QDialog):
    
    signal_prov_guardado = Signal()
    signal_prod_guardado = Signal()
    
    def __init__(self):
        super(PopupIngresoNuevo,self).__init__()
        self.ui = Ui_InicioNuevoIngreso()
        self.ui.setupUi(self)
        self.ui.btnNuevoProveedor.clicked.connect(self.showNewProvIngreso)
        self.ui.buttonBox.accepted.connect(self.showNewIngreso)

        self.comboBoxSetup()
        #La fecha actual se obtiene en AltaIngresoInicio_ui.py
            
    #Anyadir un proveedor desde la ventana de ingresos:
    def showNewProvIngreso(self):
        self.ventana_nuevo_proveedor = VentanaNewProveedor()
        #Conexiones a señales
        self.ventana_nuevo_proveedor.guardado.connect(self.show)
        self.ventana_nuevo_proveedor.rejected.connect(self.show)
        self.ventana_nuevo_proveedor.accepted.connect(self.signal_prov_guardado.emit)
        self.signal_prov_guardado.connect(self.comboBoxSetup)
        
        #Ocultar ingresos y mostrar ventana proveedor
        self.hide()
        self.ventana_nuevo_proveedor.show()
        
        #Implementar si se puede algo que seleccione automáticamente en
        # el combobox el proveedor recien registrado
    
    #Crear y mostrar VentanaNuevoIngreso
    def showNewIngreso(self):
        self.hide()
        self.ventana_nuevo_ingreso = VentanaNuevoIngreso()
        #Se pasa la señal de nuevo Ingreso a nuevo Ingreso popup para registrarla en ventanaPrincipal
        #y actualizar la tabla de proveedores
        razonSocial = self.ui.comboxDistr.currentText()
        self.ventana_nuevo_ingreso.productoGuardado.connect(self.signal_prod_guardado.emit)
        self.ventana_nuevo_ingreso.rejected.connect(self.show)
        fecha = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        self.ventana_nuevo_ingreso.ui.lblFechaValor.setText(fecha)
        self.ventana_nuevo_ingreso.ui.lblProveedorValor.setText(razonSocial)
        self.ventana_nuevo_ingreso.accepted.connect(self.accept)
        #Guardar el ingreso
        #self.ventanaNuevoIngreso.accepted.connect(self.guardarIngreso)
        #Poblar tabla desde la base de datos
        #crud.poblarTablaProductosIngreso(self.ventanaNuevoIngreso.ui.tablaProdDisponibles,self.ventanaNuevoIngreso.ui.lblProveedorValor.text())
        
        #Poblar tabla usando una lista de productos de la propia clase
        self.ventana_nuevo_ingreso.listaProductos = crud.listaProductosDeProveedor(razonSocial)
        crud.poblarTablaProductosIng(self.ventana_nuevo_ingreso.ui.tablaProdDisponibles,self.ventana_nuevo_ingreso.listaProductos)
        
        self.ventana_nuevo_ingreso.show()
        
    #setup combox proveedores
    def comboBoxSetup(self):
        lista_proveedores = crud.listaProveedores()
        for index,proveedor in enumerate(lista_proveedores):
            self.ui.comboxDistr.addItem(proveedor.razonsocial)
    
    

#Ventana de ingreso (seleccion productos)
class VentanaNuevoIngreso(QDialog):
    
    productoGuardado = Signal()
    listaProdSeleccionados = [] #Lista de seleccionados
    listaProductosEscondidos = []
    def __init__(self):
        super(VentanaNuevoIngreso,self).__init__()
        self.ui = Ui_ventanaNuevoIngreso()
        self.ui.setupUi(self)
        self.ui.btnRegistrarProd.clicked.connect(self.showNewProdIngreso)
        #Actualiza la tabla completa desde la base de datos.        
        self.productoGuardado.connect(self.updateTablaProductosIngreso)
        self.ui.btnAgregarSeleccionado.clicked.connect(self.seleccionarProducto)
        self.ui.btnEliminarProd.clicked.connect(self.quitarProducto)
        self.ui.buttonBox.accepted.connect(self.guardarIngreso)
        
    
    def showNewProdIngreso(self):
        
        razonSocial = self.ui.lblProveedorValor.text()
        
        self.newProd = VentanaNewProducto()
        self.newProd.ui.comboxDistr.setCurrentText(razonSocial)
        self.newProd.ui.comboxDistr.setDisabled(True)
        #Se vuelve a la ventana si:
        self.newProd.saved_signal.connect(self.show) #Se completa el guardado
        self.newProd.rejected.connect(self.show) #Se cancela el guardado
        #Se pasa la señal de guardado de la ventana de proveedor a la ventana anterior (IngresoInicio)
        self.newProd.accepted.connect(self.productoGuardado.emit)
        
        self.hide()
        self.newProd.show()
        
    def seleccionarProducto(self):
        
        row = self.ui.tablaProdDisponibles.currentRow()
        if row == -1:
            popup = PopupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        if int(self.ui.spinBox.text()) == 0:
            popup = PopupError()
            popup.ui.label.setText("No se ha indicado la cantidad.")
            popup.exec()
            return
        
        idSeleccionado = int(self.ui.tablaProdDisponibles.item(row,0).text())
        
        class productoSeleccionado():
            ID = int
            descripcion = str
            cantidad = int
        
        #Buscar producto seleccionado de la lista en memoria
        for index,producto in enumerate(self.listaProductos):
            if producto.id == idSeleccionado:
                productoMover = producto
                del self.listaProductos[index]
        productoSelec = productoSeleccionado()
        productoSelec.descripcion = productoMover.descripcion
        productoSelec.ID = productoMover.id
        productoSelec.cantidad = int(self.ui.spinBox.text())
        #Se envía el producto seleccionado a otra lista para no perder info de stock
        self.listaProdSeleccionados.append(productoSelec)
        #Se envía el producto seleccionado a otra lista para no perder info de stock
        self.listaProductosEscondidos.append(productoMover)
        self.updateTablaProductosIngreso()
        self.updateTablaProdSeleccionados()
        
    def quitarProducto(self):
        row = self.ui.tablaDetalleIngreso.currentRow()
        if row == -1:
            popup = PopupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        
        idSeleccionado = int(self.ui.tablaDetalleIngreso.item(row,0).text())   
    
        #Eliminar el producto seleccionado
        for index,producto in enumerate(self.listaProdSeleccionados):
            if producto.ID == idSeleccionado:
                del self.listaProdSeleccionados[index]
                break
        #Se mueve el producto de la lista oculta a la original
        for ind,prod in enumerate(self.listaProductosEscondidos):
            if prod.id == idSeleccionado:
                prodd = prod
                self.listaProductos.append(prodd)
                del self.listaProductosEscondidos[ind]
                break
            
        #Actualización de ambas tablas
        self.updateTablaProductosIngreso()
        self.updateTablaProdSeleccionados()
        
    def updateTablaProductosIngreso(self):
        crud.poblarTablaProductosIng(self.ui.tablaProdDisponibles,self.listaProductos)
    
    def updateTablaProdSeleccionados(self):
        crud.poblarTablaProdSeleccionados(self.ui.tablaDetalleIngreso,self.listaProdSeleccionados)

    def guardarIngreso(self):
        if not self.listaProdSeleccionados:
            popup = PopupError()
            popup.ui.label.setText("No se ha añadido ningún producto.")
            popup.exec()
            return
        else:
            ingreso = Ingresos()
            query = (Proveedores
                    .select(Proveedores.cuil_cuit,Proveedores.telefono)
                    .where(Proveedores.razonsocial == self.ui.lblProveedorValor.text()))
                    #Si se le asigna la query en si directamente a cuilCuitProveedor no funciona (¿?).
            for indice, proveedor in enumerate(query): 
                ingreso.cuil_cuit_proveedor = proveedor.cuil_cuit
                ingreso.telefono_proveedor = proveedor.telefono
            fechaIngreso = datetime.datetime.strptime(self.ui.lblFechaValor.text(), "%d/%m/%Y")
            ingreso.fecha = fechaIngreso
            ingreso.razonsocial_proveedor = self.ui.lblProveedorValor.text()
            #guardar ingreso
            ingreso.save()
                                    
            
            #Insertar productos en productos por ingreso
            for index, producto in enumerate(self.listaProdSeleccionados):
                prod = ProductosPorIngreso()
                prod.num_ingreso = ingreso.get_id()
                prod.id_producto = producto.ID
                prod.cantidad = producto.cantidad
                prod.descripcion = producto.descripcion
                prod.save()
            
            self.accept()
        
#Ventana principal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MenuPrincipal()   
        self.ui.setupUi(self)
        #poblado inicial tablas
        crud.poblarQTableInventario(self.ui.tablaInventario)
        crud.poblarQTableProveedores(self.ui.tablaProveedores) 
        crud.poblarQTableIngresos(self.ui.tablaIngresos)

        #Conectar botones
        self.ui.btnNuevoProducto.clicked.connect(self.showNewProd)
        self.ui.btnElimProducto.clicked.connect(self.showEliminarProd)
        self.ui.btnModProducto.clicked.connect(self.showEditProd)
        
        self.ui.filtroProveedor.currentTextChanged.connect(self.filtrarProdProveedores)
        self.poblarComboxFiltroProveedores()
        
        self.ui.btnNuevoProveedor.clicked.connect(self.showNewProv)
        self.ui.btnElimProveedor.clicked.connect(self.showEliminarProv)
        self.ui.btnModProveedor.clicked.connect(self.showEditProv)
        
        self.ui.btnNuevoIngreso.clicked.connect(self.showNewIngresoInicio)
        self.ui.tablaIngresos.clicked.connect(self.mostrarDetallesIngreso)
        
    def poblarComboxFiltroProveedores(self):
        listaProveedores = crud.listaProveedores()
        
        for index, proveedor in enumerate(listaProveedores):
            self.ui.filtroProveedor.addItem(proveedor.razonsocial)
        
    
    def filtrarProdProveedores(self):
        razonSocial = self.ui.filtroProveedor.currentText()
        if razonSocial == "Todos":
            crud.poblarQTableInventario(self.ui.tablaInventario)
        else:
            prov = (Proveedores
                    .select()
                    .where(Proveedores.razonsocial == razonSocial))
            for index,proveedor in enumerate(prov):
                cuil = proveedor.cuil_cuit
            
            listaFiltrada = (Productos
                             .select()
                             .where(Productos.cuil_cuit_proveedor == cuil))

            prov = (Proveedores
                    .select()
                    .where(Proveedores.razonsocial == razonSocial))
            for index,proveedor in enumerate(prov):
                cuil = proveedor.cuil_cuit

            crud.poblarTablaInventarioLista(self.ui.tablaInventario, prov)
        
        
    def showNewProd(self):
        self.w = VentanaNewProducto()
        self.w.saved_signal.connect(self.updateTablaInventario)
        self.w.show()
    
    def showEliminarProd(self):
        
        #comprobar si hay un elemento seleccionado
        row = self.ui.tablaInventario.currentRow()
        if row == -1:
            popup = PopupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        
        self.popupConfirmacion = PopupConfirmElim()
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
            popup = PopupError()
            popup.ui.label.setText("No se ha seleccionado ningún producto.")
            popup.exec()
            return
        
        self.modProductWindow = VentanaEditProducto()
        self.modProductWindow.setWindowTitle("Editar producto")
        self.modProductWindow.saved_signal.connect(self.updateTablaInventario)
        
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
        self.newProv.guardado.connect(self.poblarComboxFiltroProveedores)
        self.newProv.show()
    
    def showEliminarProv(self):
        
        #comprobar si hay un elemento seleccionado
        row = self.ui.tablaProveedores.currentRow()
        if row == -1:
            popup = PopupError()
            popup.ui.label.setText("No se ha seleccionado ningún proveedor.")
            popup.exec()
            return
        
        self.popupConfirmacion = PopupConfirmElim()
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
            popup = PopupError()
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
        self.newIngresoWindow.signal_prov_guardado.connect(self.updateTablaProveedores)
        self.newIngresoWindow.signal_prod_guardado.connect(self.updateTablaInventario)
        self.newIngresoWindow.accepted.connect(self.updateTablaIngresos)
        self.newIngresoWindow.exec()
    
    def mostrarDetallesIngreso(self):
        row = self.ui.tablaIngresos.currentRow()
        if row == None:
            return
        numIngreso = int(self.ui.tablaIngresos.item(row,0).text())

        crud.poblarTablaDetalle(self.ui.tablaIngresosDetalle, numIngreso)
        tupla = (Ingresos
                 .select()
                 .where(Ingresos.num_ingreso == numIngreso)
                 .namedtuples())
        for index, ingreso in enumerate(tupla):
            self.ui.nombreProveedor.setText(ingreso.razonsocial_proveedor)
            self.ui.cuilProveedor.setText(str(ingreso.cuil_cuit_proveedor))
            self.ui.telefonoProveedor.setText(str(ingreso.telefono_proveedor))
    
    #Actualiza tabla Inventario en main window
    def updateTablaInventario(self):
        crud.poblarQTableInventario(self.ui.tablaInventario)
    
    def updateTablaProveedores(self):
        crud.poblarQTableProveedores(self.ui.tablaProveedores)
    
    def updateTablaIngresos(self):
        crud.poblarQTableIngresos(self.ui.tablaIngresos)
  
#Popup datos ingresados inválidos
class PopupDatosInvalidos(QDialog) :
        
    def __init__(self):
        super(PopupDatosInvalidos,self).__init__()
        self.ui = Ui_popupDatosInvalidos()
        self.ui.setupUi(self)
        
#Plantilla popup de error
class PopupError(QDialog) :

    def __init__(self):
        super(PopupError,self).__init__()
        self.ui = Ui_ErrorDialog()
        self.ui.setupUi(self)

#Popup confirmacion eliminar producto
class PopupConfirmElim(QDialog) :
        
    def __init__(self):
        super(PopupConfirmElim,self).__init__()
        self.ui = Ui_confirmEliminar()
        self.ui.setupUi(self)