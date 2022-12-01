from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton,QMessageBox
from ui_main import Ui_MainWindow
import sys

class MainWindow(QMainWindow) :
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
def run():
    app = QApplication([])
    ej = MainWindow()
    ej.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()