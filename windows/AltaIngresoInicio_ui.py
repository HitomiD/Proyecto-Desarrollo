# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AltaIngresoInicio.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_InicioNuevoIngreso(object):
    def setupUi(self, InicioNuevoIngreso):
        if not InicioNuevoIngreso.objectName():
            InicioNuevoIngreso.setObjectName(u"InicioNuevoIngreso")
        InicioNuevoIngreso.resize(320, 231)
        self.buttonBox = QDialogButtonBox(InicioNuevoIngreso)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 180, 281, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget_2 = QWidget(InicioNuevoIngreso)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 70, 271, 61))
        self.formLayout_2 = QFormLayout(self.layoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, 0, 15, 0)
        self.lblIngreso = QLabel(self.layoutWidget_2)
        self.lblIngreso.setObjectName(u"lblIngreso")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblIngreso)

        self.lblDistr = QLabel(self.layoutWidget_2)
        self.lblDistr.setObjectName(u"lblDistr")
        font = QFont()
        font.setPointSize(9)
        self.lblDistr.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblDistr)

        self.comboxDistr = QComboBox(self.layoutWidget_2)
        self.comboxDistr.addItem("")
        self.comboxDistr.addItem("")
        self.comboxDistr.setObjectName(u"comboxDistr")
        self.comboxDistr.setMaximumSize(QSize(220, 22))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboxDistr)

        self.dateEdit = QDateEdit(self.layoutWidget_2)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDisplayFormat("dd.MM.yyyy")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.Cartelito_NewProducto = QLabel(InicioNuevoIngreso)
        self.Cartelito_NewProducto.setObjectName(u"Cartelito_NewProducto")
        self.Cartelito_NewProducto.setGeometry(QRect(30, 30, 156, 14))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cartelito_NewProducto.sizePolicy().hasHeightForWidth())
        self.Cartelito_NewProducto.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.Cartelito_NewProducto.setFont(font1)
        self.btnNuevoProveedor = QPushButton(InicioNuevoIngreso)
        self.btnNuevoProveedor.setObjectName(u"btnNuevoProveedor")
        self.btnNuevoProveedor.setGeometry(QRect(70, 140, 171, 23))

        self.retranslateUi(InicioNuevoIngreso)
        self.buttonBox.accepted.connect(InicioNuevoIngreso.accept)
        self.buttonBox.rejected.connect(InicioNuevoIngreso.reject)

        QMetaObject.connectSlotsByName(InicioNuevoIngreso)
    # setupUi

    def retranslateUi(self, InicioNuevoIngreso):
        InicioNuevoIngreso.setWindowTitle(QCoreApplication.translate("InicioNuevoIngreso", u"Nuevo Ingreso", None))
        self.lblIngreso.setText(QCoreApplication.translate("InicioNuevoIngreso", u"<html><head/><body><p>Fecha de ingreso<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblDistr.setText(QCoreApplication.translate("InicioNuevoIngreso", u"<html><head/><body><p>Proveedor <span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.comboxDistr.setItemText(0, QCoreApplication.translate("InicioNuevoIngreso", u"Juan", None))
        self.comboxDistr.setItemText(1, QCoreApplication.translate("InicioNuevoIngreso", u"Pedro", None))

        self.Cartelito_NewProducto.setText(QCoreApplication.translate("InicioNuevoIngreso", u"<html><head/><body><p><span style=\" font-weight:400;\">Ingrese los datos solicitados:</span></p></body></html>", None))
        self.btnNuevoProveedor.setText(QCoreApplication.translate("InicioNuevoIngreso", u"A\u00f1adir un proveedor", None))
    # retranslateUi

