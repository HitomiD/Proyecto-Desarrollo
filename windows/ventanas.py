from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton,QMessageBox
from PySide6.QtCore import Signal,Slot, QLocale
from PySide6.QtGui import QDoubleValidator
from windows.ui_main import Ui_MenuPrincipal
from windows.ui_newproducto import Ui_newProducto
from dbModel import Productos
import crud

#Este archivo contiene las definiciones de todas las ventanas (y sus funciones) del sistema

#DEFINICIONES DE VENTANAS


#Nuevo producto
class VentanaCarga(QDialog) :
    
    guardado = Signal()
    
    def __init__(self):
        super(VentanaCarga,self).__init__()
        self.ui = Ui_newProducto()
        self.ui.setupUi(self)
        self.floatValidator = QDoubleValidator()
        self.floatValidator.setBottom(0)
        self.floatValidator.setDecimals(2)
        self.floatValidator.setLocale(QLocale.Language.Spanish)
        self.ui.lnEditPrecio.setValidator(self.floatValidator)
        #self.accepted.connect(print("se ha tocado el boton aceptar"))
        #self.rejected.connect(print("se toco el boton cancelar"))
        self.ui.buttonBox.accepted.connect(self.guardarProveedor)
    
    #las funciones asociadas a eventos deben estar todas definidas dentro de la misma definicion de la clase de la ventana.
    def guardarProveedor(self):
        if self.ui.lnEditPrecio.hasAcceptableInput():
            print ("el precio es valido")
        else:
            print("el precio es inválido")
        nuevoProducto = Productos
        nuevoProducto.descripcion = self.ui.lnEditNombre.text()
        precio = self.ui.lnEditPrecio.text()
        nuevoProducto.precio_venta = float(precio)
        #proveedor de prueba hasta que se implemente el dropdown
        nuevoProducto.cuil_cuit_proveedor = 20237852347
        #No se va a implementar el guardado hasta que se haya implementado un control de datos ingresados
        #nuevoProducto.save()
        self.guardado.emit()
        
    
    #Guardar producto en la base de datos
    
        
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
        self.ui.btnNuevoProducto.clicked.connect(self.nuevoProducto)
        
    def nuevoProducto(self):
        self.w = VentanaCarga()
        self.w.guardado.connect(self.actualizarTabla)
        #self.w.guardado.connect(crud.poblarQTableIngresos(self.ui.tablaIngresos))
        self.w.show()
    
    def actualizarTabla(self):
        print("actualizar tabla lol")
    #FIN VENTANA PRUEBA     
        

