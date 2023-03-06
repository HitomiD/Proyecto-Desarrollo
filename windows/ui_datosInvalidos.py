# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datosInvalidos.ui'
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
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_popupDatosInvalidos(object):
    def setupUi(self, popupDatosInvalidos):
        if not popupDatosInvalidos.objectName():
            popupDatosInvalidos.setObjectName(u"popupDatosInvalidos")
        popupDatosInvalidos.resize(400, 134)
        self.verticalLayout = QVBoxLayout(popupDatosInvalidos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(popupDatosInvalidos)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(popupDatosInvalidos)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(popupDatosInvalidos)
        self.buttonBox.accepted.connect(popupDatosInvalidos.accept)
        self.buttonBox.rejected.connect(popupDatosInvalidos.reject)

        QMetaObject.connectSlotsByName(popupDatosInvalidos)
    # setupUi

    def retranslateUi(self, popupDatosInvalidos):
        popupDatosInvalidos.setWindowTitle(QCoreApplication.translate("popupDatosInvalidos", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("popupDatosInvalidos", u"Los datos ingresados no son v\u00e1lidos.", None))
    # retranslateUi

