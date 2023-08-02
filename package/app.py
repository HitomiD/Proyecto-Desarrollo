from . import DB_setup
from PySide6.QtWidgets import QApplication
import sys
from .ventanas import *

#falta comprobar si el archivo existe antes de crearlo
DB_setup.setup()

def run():
    app = QApplication([])
    ej = VentanaPrincipal()
    ej.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
    