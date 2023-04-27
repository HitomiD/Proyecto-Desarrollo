# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmElimProd.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_confirmEliminar(object):
    def setupUi(self, confirmElimProducto):
        if not confirmElimProducto.objectName():
            confirmElimProducto.setObjectName(u"confirmElimProducto")
        confirmElimProducto.resize(341, 118)
        confirmElimProducto.setMinimumSize(QSize(341, 118))
        confirmElimProducto.setMaximumSize(QSize(341, 118))
        icon = QIcon()
        icon.addFile(u"windows/assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        confirmElimProducto.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(confirmElimProducto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 70, 311, 32))
        self.buttonBox.setMaximumSize(QSize(16777215, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(confirmElimProducto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 301, 16))
        self.img = QLabel(confirmElimProducto)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(10, 10, 61, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setMaximumSize(QSize(167777, 167777))
        self.img.setTextFormat(Qt.PlainText)
        self.img.setPixmap(QPixmap(u"windows/assets/Alert.png"))
        self.img.setScaledContents(True)

        self.retranslateUi(confirmElimProducto)
        self.buttonBox.accepted.connect(confirmElimProducto.accept)
        self.buttonBox.rejected.connect(confirmElimProducto.reject)

        QMetaObject.connectSlotsByName(confirmElimProducto)
    # setupUi

    def retranslateUi(self, confirmElimProducto):
        confirmElimProducto.setWindowTitle(QCoreApplication.translate("confirmElim", u"[Alerta] Eliminar item", None))
        self.label.setText(QCoreApplication.translate("confirmElimProducto", u"<html><head/><body><p align=\"center\">\u00bfEsta seguro de que desea eliminar el item seleccionado?</p></body></html>", None))
        self.img.setText("")
    # retranslateUi

