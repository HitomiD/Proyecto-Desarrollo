# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datosInvalidos.ui'
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

class Ui_popupDatosInvalidos(object):
    def setupUi(self, popupDatosInvalidos):
        if not popupDatosInvalidos.objectName():
            popupDatosInvalidos.setObjectName(u"popupDatosInvalidos")
        popupDatosInvalidos.resize(350, 104)
        icon = QIcon()
        icon.addFile(u"./windows/assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        popupDatosInvalidos.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(popupDatosInvalidos)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 60, 221, 41))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)
        self.img = QLabel(popupDatosInvalidos)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(10, 10, 61, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setMaximumSize(QSize(167777, 167777))
        self.img.setTextFormat(Qt.PlainText)
        self.img.setPixmap(QPixmap(u"./windows/assets/Alert.png"))
        self.img.setScaledContents(True)
        self.label = QLabel(popupDatosInvalidos)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, -5, 261, 81))
        self.label.setStyleSheet(u"background-color:transparent;\n"
"color:black;")
        self.label.setTextFormat(Qt.AutoText)

        self.retranslateUi(popupDatosInvalidos)
        self.buttonBox.accepted.connect(popupDatosInvalidos.accept)
        self.buttonBox.rejected.connect(popupDatosInvalidos.reject)

        QMetaObject.connectSlotsByName(popupDatosInvalidos)
    # setupUi

    def retranslateUi(self, popupDatosInvalidos):
        popupDatosInvalidos.setWindowTitle(QCoreApplication.translate("popupDatosInvalidos", u"[Alerta] Datos Invalidos", None))
        self.img.setText("")
        self.label.setText(QCoreApplication.translate("popupDatosInvalidos", u"Los datos ingresados no son validos o estan fuera de rango.\n"
" Por favor, intente nuevamente.", None))
    # retranslateUi

