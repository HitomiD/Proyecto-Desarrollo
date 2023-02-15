# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Confirmacion.ui'
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
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(506, 178)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(280, 130, 221, 41))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 501, 41))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.inputPassword = QLineEdit(Dialog)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setGeometry(QRect(200, 60, 180, 22))
        self.inputPassword.setMinimumSize(QSize(150, 0))
        self.inputPassword.setMaximumSize(QSize(300, 16777215))
        self.inputPassword.setEchoMode(QLineEdit.Password)
        self.LabelUsuario = QLabel(Dialog)
        self.LabelUsuario.setObjectName(u"LabelUsuario")
        self.LabelUsuario.setGeometry(QRect(90, 60, 100, 27))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelUsuario.sizePolicy().hasHeightForWidth())
        self.LabelUsuario.setSizePolicy(sizePolicy)
        self.LabelUsuario.setFont(font)
        self.LabelUsuario.setAlignment(Qt.AlignCenter)
        self.CONTRASENA = QLabel(Dialog)
        self.CONTRASENA.setObjectName(u"CONTRASENA")
        self.CONTRASENA.setGeometry(QRect(80, 90, 110, 27))
        sizePolicy.setHeightForWidth(self.CONTRASENA.sizePolicy().hasHeightForWidth())
        self.CONTRASENA.setSizePolicy(sizePolicy)
        self.CONTRASENA.setFont(font)
        self.CONTRASENA.setAlignment(Qt.AlignCenter)
        self.CasillaUsuario = QLineEdit(Dialog)
        self.CasillaUsuario.setObjectName(u"CasillaUsuario")
        self.CasillaUsuario.setEnabled(True)
        self.CasillaUsuario.setGeometry(QRect(200, 90, 180, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CasillaUsuario.sizePolicy().hasHeightForWidth())
        self.CasillaUsuario.setSizePolicy(sizePolicy1)
        self.CasillaUsuario.setMinimumSize(QSize(180, 0))
        self.CasillaUsuario.setMaximumSize(QSize(150, 16777215))
        self.CasillaUsuario.setBaseSize(QSize(0, 0))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">Para confirmar el cambio, ingrese su <span style=\" font-style:italic; color:#000000;\">usuario</span> y <span style=\" font-style:italic;\">contrase\u00f1a</span></p></body></html>", None))
        self.inputPassword.setInputMask("")
        self.LabelUsuario.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Usuario: </p></body></html>", None))
        self.CONTRASENA.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Contrase\u00f1a: </p></body></html>", None))
    # retranslateUi

