# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmElimProd.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_confirmElimProducto(object):
    def setupUi(self, confirmElimProducto):
        if not confirmElimProducto.objectName():
            confirmElimProducto.setObjectName(u"confirmElimProducto")
        confirmElimProducto.resize(333, 103)
        icon = QIcon()
        icon.addFile(u"../assets/Warning-icon-isolated-on-transparent-background-PNG.png", QSize(), QIcon.Normal, QIcon.Off)
        confirmElimProducto.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(confirmElimProducto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 60, 311, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(confirmElimProducto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 301, 16))
        self.img = QLabel(confirmElimProducto)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(10, 10, 61, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setMaximumSize(QSize(167777, 167777))
        self.img.setTextFormat(Qt.PlainText)
        self.img.setPixmap(QPixmap(u"../assets/Exclamation.png"))

        self.retranslateUi(confirmElimProducto)
        self.buttonBox.accepted.connect(confirmElimProducto.accept)
        self.buttonBox.rejected.connect(confirmElimProducto.reject)

        QMetaObject.connectSlotsByName(confirmElimProducto)
    # setupUi

    def retranslateUi(self, confirmElimProducto):
        confirmElimProducto.setWindowTitle(QCoreApplication.translate("confirmElimProducto", u"[Alerta] Eliminar producto", None))
        self.label.setText(QCoreApplication.translate("confirmElimProducto", u"<html><head/><body><p align=\"center\">\u00bfEsta seguro de que desea eliminar el producto?</p></body></html>", None))
        self.img.setText("")
    # retranslateUi

