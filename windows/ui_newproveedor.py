# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newproveedor.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_newProveedor(object):
    def setupUi(self, newProveedor):
        if not newProveedor.objectName():
            newProveedor.setObjectName(u"newProveedor")
        newProveedor.resize(409, 270)
        self.verticalLayout = QVBoxLayout(newProveedor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, -1, 20, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.label_15 = QLabel(newProveedor)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"display: flex;\n"
"background-color: transparent;\n"
"color: black;\n"
"align-items: center;")

        self.verticalLayout_2.addWidget(self.label_15)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lblRazonSocial = QLabel(newProveedor)
        self.lblRazonSocial.setObjectName(u"lblRazonSocial")
        font1 = QFont()
        font1.setPointSize(10)
        self.lblRazonSocial.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lblRazonSocial)

        self.lnEditRazonSocial = QLineEdit(newProveedor)
        self.lnEditRazonSocial.setObjectName(u"lnEditRazonSocial")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lnEditRazonSocial)

        self.lblDireccion = QLabel(newProveedor)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setFont(font1)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lblDireccion)

        self.lnEditDireccion = QLineEdit(newProveedor)
        self.lnEditDireccion.setObjectName(u"lnEditDireccion")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lnEditDireccion)

        self.lblTelefono = QLabel(newProveedor)
        self.lblTelefono.setObjectName(u"lblTelefono")
        self.lblTelefono.setFont(font1)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.lblTelefono)

        self.lnEditTelefono = QLineEdit(newProveedor)
        self.lnEditTelefono.setObjectName(u"lnEditTelefono")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lnEditTelefono)

        self.lnEditEmail = QLineEdit(newProveedor)
        self.lnEditEmail.setObjectName(u"lnEditEmail")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.lnEditEmail)

        self.lblEmail = QLabel(newProveedor)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setFont(font1)
        self.lblEmail.setStyleSheet(u"")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.lblEmail)

        self.labelCUIT = QLabel(newProveedor)
        self.labelCUIT.setObjectName(u"labelCUIT")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.labelCUIT)

        self.lnEditCUIT = QLineEdit(newProveedor)
        self.lnEditCUIT.setObjectName(u"lnEditCUIT")

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.lnEditCUIT)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(newProveedor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(newProveedor)
        #self.buttonBox.accepted.connect(newProveedor.accept)
        self.buttonBox.rejected.connect(newProveedor.reject)

        QMetaObject.connectSlotsByName(newProveedor)
    # setupUi

    def retranslateUi(self, newProveedor):
        newProveedor.setWindowTitle(QCoreApplication.translate("newProveedor", u"Nuevo Proveedor", None))
        self.label_15.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Ingrese los <span style=\" font-weight:700;\">datos</span> solicitados:</p></body></html>", None))
        self.lblRazonSocial.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Raz\u00f3n social<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblDireccion.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Direcci\u00f3n<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblTelefono.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Tel\u00e9fono<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblEmail.setText(QCoreApplication.translate("newProveedor", u"E-Mail", None))
        self.labelCUIT.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>CUIL/CUIT<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
    # retranslateUi

