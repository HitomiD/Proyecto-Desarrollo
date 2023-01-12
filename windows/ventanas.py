from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton,QMessageBox
from ui_main import Ui_MainWindow
from ui_newproveedor import Ui_nuevoproveedor

#DEFINICIONES DE VENTANAS
        
#Ventana principal
class VentanaPrincipal(QMainWindow) :
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
