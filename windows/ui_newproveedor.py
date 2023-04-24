# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newproveedor.ui'
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
    QFormLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_newProveedor(object):
    def setupUi(self, newProveedor):
        if not newProveedor.objectName():
            newProveedor.setObjectName(u"newProveedor")
        newProveedor.resize(382, 212)
        newProveedor.setMaximumSize(QSize(409, 212))
        icon = QIcon()
        icon.addFile(u"../assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        newProveedor.setWindowIcon(icon)
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
        font.setPointSize(9)
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
        self.lblRazonSocial.setFont(font)
        self.lblRazonSocial.setStyleSheet(u"margin-left:20px;")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lblRazonSocial)

        self.lineEdit_9 = QLineEdit(newProveedor)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(200, 22))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)

        self.lblDireccion = QLabel(newProveedor)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(u"margin-left:20px;")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lblDireccion)

        self.lineEdit_10 = QLineEdit(newProveedor)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(200, 22))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_10)

        self.lblTelefono = QLabel(newProveedor)
        self.lblTelefono.setObjectName(u"lblTelefono")
        self.lblTelefono.setFont(font)
        self.lblTelefono.setStyleSheet(u"margin-left:20px;")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lblTelefono)

        self.lineEdit_11 = QLineEdit(newProveedor)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(200, 22))

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(newProveedor)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMaximumSize(QSize(200, 22))

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_12)

        self.lblEmail = QLabel(newProveedor)
        self.lblEmail.setObjectName(u"lblEmail")
        self.lblEmail.setFont(font)
        self.lblEmail.setStyleSheet(u"margin-left:20px;")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.lblEmail)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Ayuda = QDialogButtonBox(newProveedor)
        self.Ayuda.setObjectName(u"Ayuda")
        self.Ayuda.setMaximumSize(QSize(75, 24))
        self.Ayuda.setLayoutDirection(Qt.LeftToRight)
        self.Ayuda.setOrientation(Qt.Horizontal)
        self.Ayuda.setStandardButtons(QDialogButtonBox.Help)

        self.horizontalLayout.addWidget(self.Ayuda)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(newProveedor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(newProveedor)
        self.buttonBox.accepted.connect(newProveedor.accept)
        self.buttonBox.rejected.connect(newProveedor.reject)

        QMetaObject.connectSlotsByName(newProveedor)
    # setupUi

    def retranslateUi(self, newProveedor):
        newProveedor.setWindowTitle(QCoreApplication.translate("newProveedor", u"Nuevo Proveedor", None))
        self.label_15.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Ingrese los datos solicitados:</p></body></html>", None))
        self.lblRazonSocial.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Raz\u00f3n social<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lineEdit_9.setText("")
        self.lblDireccion.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Direcci\u00f3n<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblTelefono.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Tel\u00e9fono<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblEmail.setText(QCoreApplication.translate("newProveedor", u"E-Mail", None))
    # retranslateUi

