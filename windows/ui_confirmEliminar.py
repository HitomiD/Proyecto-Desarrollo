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

class Ui_confirmEliminar(object):
    def setupUi(self, confirmElimProducto):
        if not confirmElimProducto.objectName():
            confirmElimProducto.setObjectName(u"confirmElimProducto")
        confirmElimProducto.resize(400, 169)
        self.buttonBox = QDialogButtonBox(confirmElimProducto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 120, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(confirmElimProducto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 291, 16))

        self.retranslateUi(confirmElimProducto)
        self.buttonBox.accepted.connect(confirmElimProducto.accept)
        self.buttonBox.rejected.connect(confirmElimProducto.reject)

        QMetaObject.connectSlotsByName(confirmElimProducto)
    # setupUi

    def retranslateUi(self, confirmElimProducto):
        confirmElimProducto.setWindowTitle(QCoreApplication.translate("confirmElim", u"Eliminar item", None))
        self.label.setText(QCoreApplication.translate("confirmElim", u"Esta seguro de que desea eliminar el item seleccionado?", None))
    # retranslateUi

