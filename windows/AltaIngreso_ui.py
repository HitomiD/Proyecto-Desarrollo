# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AltaIngreso.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QFrame, QGroupBox, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_ventanaNuevoIngreso(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(698, 549)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 500, 651, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Help|QDialogButtonBox.Ok)
        self.groupBoxDetalle = QGroupBox(Dialog)
        self.groupBoxDetalle.setObjectName(u"groupBoxDetalle")
        self.groupBoxDetalle.setGeometry(QRect(420, 20, 261, 451))
        self.tablaDetalleIngreso = QTableWidget(self.groupBoxDetalle)
        if (self.tablaDetalleIngreso.columnCount() < 3):
            self.tablaDetalleIngreso.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaDetalleIngreso.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaDetalleIngreso.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaDetalleIngreso.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tablaDetalleIngreso.rowCount() < 7):
            self.tablaDetalleIngreso.setRowCount(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaDetalleIngreso.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaDetalleIngreso.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaDetalleIngreso.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaDetalleIngreso.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaDetalleIngreso.setItem(1, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaDetalleIngreso.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaDetalleIngreso.setItem(2, 2, __qtablewidgetitem15)
        self.tablaDetalleIngreso.setObjectName(u"tablaDetalleIngreso")
        self.tablaDetalleIngreso.setGeometry(QRect(10, 30, 241, 381))
        self.btnEliminarProd = QPushButton(self.groupBoxDetalle)
        self.btnEliminarProd.setObjectName(u"btnEliminarProd")
        self.btnEliminarProd.setGeometry(QRect(50, 420, 151, 23))
        self.groupBoxProductos = QGroupBox(Dialog)
        self.groupBoxProductos.setObjectName(u"groupBoxProductos")
        self.groupBoxProductos.setGeometry(QRect(20, 100, 361, 371))
        self.tablaProdDisponibles = QTableWidget(self.groupBoxProductos)
        if (self.tablaProdDisponibles.columnCount() < 4):
            self.tablaProdDisponibles.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        if (self.tablaProdDisponibles.rowCount() < 5):
            self.tablaProdDisponibles.setRowCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tablaProdDisponibles.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tablaProdDisponibles.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablaProdDisponibles.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tablaProdDisponibles.setVerticalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tablaProdDisponibles.setVerticalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(0, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(0, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(0, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(0, 3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(1, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(1, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(1, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(2, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(2, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(2, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(2, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(3, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(3, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(3, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(3, 3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(4, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(4, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(4, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tablaProdDisponibles.setItem(4, 3, __qtablewidgetitem44)
        self.tablaProdDisponibles.setObjectName(u"tablaProdDisponibles")
        self.tablaProdDisponibles.setGeometry(QRect(10, 30, 341, 301))
        self.btnRegistrarProd = QPushButton(self.groupBoxProductos)
        self.btnRegistrarProd.setObjectName(u"btnRegistrarProd")
        self.btnRegistrarProd.setGeometry(QRect(10, 340, 181, 23))
        self.btnRegistrarProd_2 = QPushButton(self.groupBoxProductos)
        self.btnRegistrarProd_2.setObjectName(u"btnRegistrarProd_2")
        self.btnRegistrarProd_2.setGeometry(QRect(200, 340, 111, 23))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 241, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 241, 53))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, 0, 15, 0)
        self.lblFecha = QLabel(self.layoutWidget)
        self.lblFecha.setObjectName(u"lblFecha")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblFecha)

        self.lblDistr = QLabel(self.layoutWidget)
        self.lblDistr.setObjectName(u"lblDistr")
        font = QFont()
        font.setPointSize(9)
        self.lblDistr.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblDistr)

        self.lblFechaValor = QLabel(self.layoutWidget)
        self.lblFechaValor.setObjectName(u"lblFechaValor")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lblFechaValor)

        self.lblProveedorValor = QLabel(self.layoutWidget)
        self.lblProveedorValor.setObjectName(u"lblProveedorValor")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lblProveedorValor)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBoxDetalle.setTitle(QCoreApplication.translate("Dialog", u"Detalle de ingreso", None))
        ___qtablewidgetitem = self.tablaDetalleIngreso.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tablaDetalleIngreso.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None));
        ___qtablewidgetitem2 = self.tablaDetalleIngreso.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Cantidad", None));

        __sortingEnabled = self.tablaDetalleIngreso.isSortingEnabled()
        self.tablaDetalleIngreso.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tablaDetalleIngreso.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Producto 1", None));
        ___qtablewidgetitem4 = self.tablaDetalleIngreso.item(0, 2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"40", None));
        ___qtablewidgetitem5 = self.tablaDetalleIngreso.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Producto 3", None));
        ___qtablewidgetitem6 = self.tablaDetalleIngreso.item(1, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"50", None));
        ___qtablewidgetitem7 = self.tablaDetalleIngreso.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"producto 4", None));
        ___qtablewidgetitem8 = self.tablaDetalleIngreso.item(2, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"30", None));
        self.tablaDetalleIngreso.setSortingEnabled(__sortingEnabled)

        self.btnEliminarProd.setText(QCoreApplication.translate("Dialog", u"Eliminar del ingreso", None))
        self.groupBoxProductos.setTitle(QCoreApplication.translate("Dialog", u"Productos registrados de <distribuidor>", None))
        ___qtablewidgetitem9 = self.tablaProdDisponibles.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem10 = self.tablaProdDisponibles.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None));
        ___qtablewidgetitem11 = self.tablaProdDisponibles.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Stock actual", None));
        ___qtablewidgetitem12 = self.tablaProdDisponibles.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"Stock Minimo", None));

        __sortingEnabled1 = self.tablaProdDisponibles.isSortingEnabled()
        self.tablaProdDisponibles.setSortingEnabled(False)
        ___qtablewidgetitem13 = self.tablaProdDisponibles.item(0, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"234", None));
        ___qtablewidgetitem14 = self.tablaProdDisponibles.item(0, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"Producto 1", None));
        ___qtablewidgetitem15 = self.tablaProdDisponibles.item(0, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"100", None));
        ___qtablewidgetitem16 = self.tablaProdDisponibles.item(0, 3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"90", None));
        ___qtablewidgetitem17 = self.tablaProdDisponibles.item(1, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"5314", None));
        ___qtablewidgetitem18 = self.tablaProdDisponibles.item(1, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"Producto 2", None));
        ___qtablewidgetitem19 = self.tablaProdDisponibles.item(1, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"56", None));
        ___qtablewidgetitem20 = self.tablaProdDisponibles.item(1, 3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"40", None));
        ___qtablewidgetitem21 = self.tablaProdDisponibles.item(2, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"423", None));
        ___qtablewidgetitem22 = self.tablaProdDisponibles.item(2, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"Producto 3", None));
        ___qtablewidgetitem23 = self.tablaProdDisponibles.item(2, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"67", None));
        ___qtablewidgetitem24 = self.tablaProdDisponibles.item(2, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"67", None));
        ___qtablewidgetitem25 = self.tablaProdDisponibles.item(3, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"5443", None));
        ___qtablewidgetitem26 = self.tablaProdDisponibles.item(3, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"Producto 4", None));
        ___qtablewidgetitem27 = self.tablaProdDisponibles.item(3, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"48", None));
        ___qtablewidgetitem28 = self.tablaProdDisponibles.item(3, 3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"73", None));
        ___qtablewidgetitem29 = self.tablaProdDisponibles.item(4, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"645", None));
        ___qtablewidgetitem30 = self.tablaProdDisponibles.item(4, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Dialog", u"Producto 5 ", None));
        ___qtablewidgetitem31 = self.tablaProdDisponibles.item(4, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Dialog", u"74", None));
        ___qtablewidgetitem32 = self.tablaProdDisponibles.item(4, 3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Dialog", u"14", None));
        self.tablaProdDisponibles.setSortingEnabled(__sortingEnabled1)

        self.btnRegistrarProd.setText(QCoreApplication.translate("Dialog", u"Registrar un producto nuevo", None))
        self.btnRegistrarProd_2.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir", None))
        self.lblFecha.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Fecha</p></body></html>", None))
        self.lblDistr.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Distribuidor</p></body></html>", None))
        self.lblFechaValor.setText(QCoreApplication.translate("Dialog", u"<fecha>", None))
        self.lblProveedorValor.setText(QCoreApplication.translate("Dialog", u"<distribuidor>", None))
    # retranslateUi

