from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton,QMessageBox
from PySide6.QtCore import Signal,Slot, QLocale
from PySide6.QtGui import QDoubleValidator,QIntValidator
from windows.ui_datosInvalidos import Ui_popupDatosInvalidos
from windows.ui_main import Ui_MenuPrincipal
from windows.ui_newproducto import Ui_newProducto
from windows.ui_confirmElimProd import Ui_confirmElimProducto

from dbModel import Productos,Proveedores
import crud

#Este archivo contiene las definiciones de todas las ventanas (y sus funciones) del sistema

#Las funciones asociadas a eventos deben estar definidas dentro de la misma definicion de la ventana, sino no funcionan.


#Popup nuevo producto
class VentanaCarga(QDialog) :
    
    #La señal de guardado se emite en un guardado exitoso para disparar la actualizacion de la tabla.
    guardado = Signal()
    
    def __init__(self):
        super(VentanaCarga,self).__init__()
        self.ui = Ui_newProducto()
        self.ui.setupUi(self)
        #Validadores para campos:
        self.floatValidator = QDoubleValidator()
        self.floatValidator.setBottom(0)
        self.floatValidator.setDecimals(2)
        self.floatValidator.setLocale(QLocale.Language.Spanish)
        self.ui.lnEditPrecio.setValidator(self.floatValidator)
        self.intValidator = QIntValidator()
        self.intValidator.setBottom(0)
        self.intValidator.setLocale(QLocale.Language.Spanish)
        self.ui.lnEditStockMinimo.setValidator(self.intValidator)
        #Fin Validadores
        self.comboBoxSetup()
        self.ui.buttonBox.accepted.connect(self.guardarProducto)

    def comboBoxSetup(self):
        listaProveedores = crud.listaProveedores()
        for index,proveedor in enumerate(listaProveedores):
            self.ui.comboxDistr.addItem(proveedor.razonsocial)
        
    
    #Guardar proveedor
    def guardarProducto(self):
        if self.fieldCheckProducto() == "ok":
            nuevoProducto = Productos() #"Productos" es el nombre del modelo de la tabla
            
            #Se extraen los datos de los campos de la ventana
            nuevoProducto.descripcion = self.ui.lnEditNombre.text()
            precio = self.ui.lnEditPrecio.text()
            nuevoProducto.precio_venta = float(precio)
            nuevoProducto.stock_minimo = int(self.ui.lnEditStockMinimo.text())
            cuil_cuit_proveedor = Proveedores.select(Proveedores.cuil_cuit).where(self.ui.comboxDistr.currentText() == Proveedores.razonsocial).get()
            nuevoProducto.cuil_cuit_proveedor = cuil_cuit_proveedor
            
            nuevoProducto.save()
            
            self.guardado.emit()
            self.accept()
    
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
        self.popupDatosInv =popupDatosInvalidos()
        self.popupDatosInv.show()
        
        
#Ventana principal
class VentanaPrincipal(QMainWindow) :
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MenuPrincipal()    
        self.ui.setupUi(self)
        
    #VENTANA PRUEBA
    #   self.w = None
    #     #BOTONES INVENTARIO
    #     #Abrir ventana de carga
    
        #Conectar botones
        self.ui.btnNuevoProducto.clicked.connect(self.nuevoProducto)
        self.ui.btnElimProducto.clicked.connect(self.eliminarProducto)
        
    def nuevoProducto(self):
        self.w = VentanaCarga()
        self.w.guardado.connect(self.actualizarTabla)
        #self.w.guardado.connect(crud.poblarQTableIngresos(self.ui.tablaIngresos))
        self.w.show()
    
    #Muestra el popup de confirmacion para eliminar
    def eliminarProducto(self):
        self.popupConfirmacion = popupConfirmElim()
        self.popupConfirmacion.accepted.connect(self.eliminarProductoConfirmado)
        self.popupConfirmacion.exec_()
    
    #Elimina el producto si el proceso se confirma
    def eliminarProductoConfirmado(self):
        row = self.ui.tablaInventario.currentRow()
        idProducto = int(self.ui.tablaInventario.item(row,0).text())
        crud.eliminarProducto(idProducto)
        self.actualizarTabla()
    
    #Actualiza tabla
    def actualizarTabla(self):
        crud.poblarQTableInventario(self.ui.tablaInventario)
        
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
        self.ui = Ui_confirmElimProducto()
        self.ui.setupUi(self)