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
        Dialog.resize(690, 549)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 500, 631, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Help|QDialogButtonBox.Ok)
        self.groupBoxDetalle = QGroupBox(Dialog)
        self.groupBoxDetalle.setObjectName(u"groupBoxDetalle")
        self.groupBoxDetalle.setGeometry(QRect(410, 20, 261, 451))
        self.tablaDetalleIngreso = QTableWidget(self.groupBoxDetalle)
        if (self.tablaDetalleIngreso.columnCount() < 3):
            self.tablaDetalleIngreso.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaDetalleIngreso.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaDetalleIngreso.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaDetalleIngreso.setHorizontalHeaderItem(2, __qtablewidgetitem2)
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
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaProdDisponibles.setHorizontalHeaderItem(3, __qtablewidgetitem6)
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
        self.btnEliminarProd.setText(QCoreApplication.translate("Dialog", u"Eliminar del ingreso", None))
        self.groupBoxProductos.setTitle(QCoreApplication.translate("Dialog", u"Productos registrados de <distribuidor>", None))
        ___qtablewidgetitem3 = self.tablaProdDisponibles.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem4 = self.tablaProdDisponibles.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n", None));
        ___qtablewidgetitem5 = self.tablaProdDisponibles.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Stock actual", None));
        ___qtablewidgetitem6 = self.tablaProdDisponibles.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Stock Minimo", None));
        self.btnRegistrarProd.setText(QCoreApplication.translate("Dialog", u"Registrar un producto nuevo", None))
        self.btnRegistrarProd_2.setText(QCoreApplication.translate("Dialog", u"A\u00f1adir", None))
        self.lblFecha.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Fecha</p></body></html>", None))
        self.lblDistr.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Distribuidor</p></body></html>", None))
        self.lblFechaValor.setText(QCoreApplication.translate("Dialog", u"<fecha>", None))
        self.lblProveedorValor.setText(QCoreApplication.translate("Dialog", u"<distribuidor>", None))
    # retranslateUi

