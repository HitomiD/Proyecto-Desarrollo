from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton,QMessageBox
from ui_main import Ui_MenuPrincipal
from ui_newproducto import Ui_newProducto

#DEFINICIONES DE VENTANAS


#Nuevo producto
class VentanaCarga(QDialog) :
    def __init__(self):
        super(VentanaCarga,self).__init__()
        self.ui = Ui_newProducto()
        self.ui.setupUi(self)
        
#Ventana principal
class VentanaPrincipal(QMainWindow) :
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MenuPrincipal()
        self.ui.setupUi(self)
        
    #VENTANA PRUEBA
    #     self.w = None
    #     #BOTONES INVENTARIO
    #     #Abrir ventana de carga
    #     self.ui.btnNuevoProducto.clicked.connect(self.nuevoProducto)
        
    # def nuevoProducto(self):
    #     self.w = VentanaCarga()
    #     self.w.show()
    #FIN VENTANA PRUEBA     
        

