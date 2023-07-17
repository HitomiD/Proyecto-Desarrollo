import sqlite3


#setup
def setup():
    dbconnection = sqlite3.connect("database.db")
    try:
        #Crear tablas
        dbconnection.execute("""
                            CREATE TABLE Proveedores (
                                CUIL_CUIT INTEGER PRIMARY KEY NOT NULL,
                                razonsocial TEXT NOT NULL,
                                direccion TEXT,
                                telefono INTEGER,
                                email TEXT,
                                nota TEXT,
                                num_ultimo_ingreso INTEGER,
                                FOREIGN KEY(num_ultimo_ingreso) REFERENCES Ingresos(num_ingreso)

                            );
                            """)
        dbconnection.execute("""
                            CREATE TABLE Productos (
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                descripcion TEXT NOT NULL,
                                stock INTEGER NOT NULL DEFAULT '0',
                                stock_minimo INTEGER,
                                precio_venta FLOAT,
                                CUIL_CUIT_proveedor INTEGER,
                                FOREIGN KEY(CUIL_CUIT_proveedor) REFERENCES Proveedores(CUIL_CUIT)
                            );
                            """)
        dbconnection.execute("""
                            CREATE TABLE Ingresos (
                                num_ingreso INTEGER PRIMARY KEY AUTOINCREMENT,
                                CUIL_CUIT_proveedor NOT NULL,
                                razonsocial_proveedor NOT NULL,
                                telefono_proveedor INTEGER,
                                fecha DATE NOT NULL
                            );
                            """)
        dbconnection.execute("""
                            CREATE TABLE Productos_por_Ingreso(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                ID_producto INTEGER NOT NULL,
                                descripcion NOT NULL,
                                num_ingreso INTEGER NOT NULL,
                                cantidad INTEGER NOT NULL,
                                FOREIGN KEY(ID_producto) REFERENCES Productos(ID),
                                FOREIGN KEY(num_ingreso) REFERENCES Ingresos(num_ingreso) 
                            );
                            """)
        dbconnection.execute("""
                            CREATE TABLE Usuarios(
                                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                usuario NOT NULL UNIQUE,
                                nombre NOT NULL,
                                apellido NOT NULL,
                                password NOT NULL
                            );
                            """)
        #Fin crear tablas
        
        #Triggers de actualización ante nuevo ingreso
        dbconnection.execute("""
                            CREATE TRIGGER actualizar_stock_y_proveedor AFTER INSERT ON Productos_por_Ingreso
                            BEGIN
                                UPDATE Productos SET stock = stock + NEW.cantidad, CUIL_CUIT_proveedor = (SELECT CUIL_CUIT_proveedor FROM Ingresos WHERE num_ingreso = NEW.num_ingreso) WHERE ID = NEW.ID;
                            END;
                            """)
        dbconnection.execute("""
                             CREATE TRIGGER actualizar_ultimo_ingreso_asociado AFTER INSERT ON Ingresos
                                BEGIN
                                    UPDATE Proveedores SET num_ultimo_ingreso = NEW.num_ingreso WHERE CUIL_CUIT = NEW.CUIL_CUIT_proveedor;
                                END;
                             """)
        #Fin triggers

    except Exception as err:
        print(str(err))
    dbconnection.close()
#fin setup