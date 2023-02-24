import DB_setup
from PySide6.QtWidgets import QApplication
import sys
from windows.ventanas import *
from dbModel import prueba

DB_setup.setup()

prueba()

def run():
    app = QApplication([])
    ej = VentanaPrincipal()
    ej.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
    