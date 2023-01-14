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
                            email TEXT,
                            nota TEXT
                        );
                        """)
    
    dbconnection.execute("""
                        CREATE TABLE Productos (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            descripcion TEXT NOT NULL,
                            stock INTEGER NOT NULL DEFAULT '0',
                            stock_minimo INTEGER,
                            precio_venta FLOAT,
                            num_ultimo_ingreso INTEGER,
                            FOREIGN KEY(num_ultimo_ingreso) REFERENCES Ingresos(num_ingreso)
                        );
                        """)
    dbconnection.execute("""
                         CREATE TABLE Ingresos (
                             num_ingreso INTEGER PRIMARY KEY AUTOINCREMENT,
                             CUIL_CUIT_proveedor NOT NULL,
                             fecha DATE NOT NULL
                         );
                         """)
    dbconnection.execute("""
                         CREATE TABLE Productos_por_Ingreso(
                             ID INTEGER PRIMARY KEY AUTOINCREMENT,
                             ID_producto INTEGER NOT NULL,
                             num_ingreso INTEGER NOT NULL,
                             precio_unitario_compra FLOAT NOT NULL,
                             cantidad INTEGER NOT NULL,
                             FOREIGN KEY(ID_producto) REFERENCES Productos(ID),
                             FOREIGN KEY(num_ingreso) REFERENCES Ingresos(num_ingreso) 
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