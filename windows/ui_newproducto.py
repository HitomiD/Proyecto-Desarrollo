# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newproducto.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_newProducto(object):
    def setupUi(self, newProducto):
        if not newProducto.objectName():
            newProducto.setObjectName(u"newProducto")
        newProducto.resize(309, 182)
        newProducto.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout = QVBoxLayout(newProducto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lblNombre_2 = QLabel(newProducto)
        self.lblNombre_2.setObjectName(u"lblNombre_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblNombre_2)

        self.lnEditNombre_2 = QLineEdit(newProducto)
        self.lnEditNombre_2.setObjectName(u"lnEditNombre_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lnEditNombre_2)

        self.lblPrecio_2 = QLabel(newProducto)
        self.lblPrecio_2.setObjectName(u"lblPrecio_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblPrecio_2)

        self.lnEditPrecio_2 = QLineEdit(newProducto)
        self.lnEditPrecio_2.setObjectName(u"lnEditPrecio_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lnEditPrecio_2)

        self.lblDistr_2 = QLabel(newProducto)
        self.lblDistr_2.setObjectName(u"lblDistr_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lblDistr_2)

        self.comboxDistr_2 = QComboBox(newProducto)
        self.comboxDistr_2.setObjectName(u"comboxDistr_2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.comboxDistr_2)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(newProducto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(newProducto)
        self.buttonBox.accepted.connect(newProducto.accept)
        self.buttonBox.rejected.connect(newProducto.reject)

        QMetaObject.connectSlotsByName(newProducto)
    # setupUi

    def retranslateUi(self, newProducto):
        newProducto.setWindowTitle(QCoreApplication.translate("newProducto", u"Nuevo Proveedor", None))
        self.lblNombre_2.setText(QCoreApplication.translate("newProducto", u"Nombre", None))
        self.lblPrecio_2.setText(QCoreApplication.translate("newProducto", u"Precio unitario", None))
        self.lblDistr_2.setText(QCoreApplication.translate("newProducto", u"Distribuidor", None))
    # retranslateUi

