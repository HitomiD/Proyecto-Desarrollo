from peewee import *

#Este archivo contiene el modelo de DB de peewee

## Modelos generados automáticamente por pwiz ##
database = SqliteDatabase('database.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

#A esta clase se le asocian las definiciones de tablas posteriores.
class BaseModel(Model):
    class Meta:
        database  =  database
        #   ^           ^
        #atributo    nombre del
        #de clase    archivo

class Ingresos(BaseModel):
    cuil_cuit_proveedor = BareField(column_name='CUIL_CUIT_proveedor')
    fecha = DateField()
    num_ingreso = AutoField(null=True)

    class Meta:
        table_name = 'Ingresos'

class Proveedores(BaseModel):
    #cuil_cuit = AutoField(column_name='CUIL_CUIT')
    cuil_cuit = IntegerField(primary_key=True)
    direccion = TextField(null=True)
    email = TextField(null=True)
    nota = TextField(null=True)
    num_ultimo_ingreso = ForeignKeyField(column_name='num_ultimo_ingreso', field='num_ingreso', model=Ingresos, null=True)
    razonsocial = TextField()
    telefono = IntegerField(null=True)

    class Meta:
        table_name = 'Proveedores'

class Productos(BaseModel):
    cuil_cuit_proveedor = ForeignKeyField(column_name='CUIL_CUIT_proveedor', field='cuil_cuit', model=Proveedores, null=True)
    id = AutoField(column_name='ID', null=True)
    descripcion = TextField()
    precio_venta = FloatField(null=True)
    stock = IntegerField(constraints=[SQL("DEFAULT '0'")])
    stock_minimo = IntegerField(null=True)

    class Meta:
        table_name = 'Productos'

class ProductosPorIngreso(BaseModel):
    id = AutoField(column_name='ID', null=True)
    id_producto = ForeignKeyField(column_name='ID_producto', field='id', model=Productos)
    cantidad = IntegerField()
    num_ingreso = ForeignKeyField(column_name='num_ingreso', field='num_ingreso', model=Ingresos)
    precio_unitario_compra = FloatField()

    class Meta:
        table_name = 'Productos_por_Ingreso'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False
## Fin modelos generados automáticamente por pwiz ##
