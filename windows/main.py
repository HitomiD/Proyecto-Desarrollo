import sqlite3
from PySide6.QtWidgets import QApplication
import sys
from ventanas import *         

dbconnection = sqlite3.connect("database.db")
try:
    dbconnection.execute("""
                        CREATE TABLE Proveedores (
                            CUIL_CUIT INTEGER PRIMARY KEY NOT NULL,
                            razonsocial TEXT NOT NULL,
                            direccion TEXT,
                            telefono INTEGER,
                            email TEXT
                        );
                        """)
    
    dbconnection.execute("""
                        CREATE TABLE Productos (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            descripcion TEXT NOT NULL,
                            stock INTEGER NOT NULL DEFAULT '0',
                            stock_minimo INTEGER,
                            precio_venta FLOAT,
                            CUIL_CUIT_proveedor INTEGER NOT NULL,
                            FOREIGN KEY(CUIL_CUIT_proveedor) REFERENCES Proveedores(CUIL_CUIT)
                        );
                        """)
except Exception as err:
        print(str(err))
dbconnection.close()

def run():
    app = QApplication([])
    ej = VentanaPrincipal()
    ej.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()