# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newproducto.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_newProducto(object):
    def setupUi(self, newProducto):
        if not newProducto.objectName():
            newProducto.setObjectName(u"newProducto")
        newProducto.resize(389, 231)
        newProducto.setMaximumSize(QSize(389, 231))
        newProducto.setFocusPolicy(Qt.StrongFocus)
        icon = QIcon()
        icon.addFile(u"windows/assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        newProducto.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(newProducto)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 0, -1, 0)
        self.Cartelito_NewProducto = QLabel(newProducto)
        self.Cartelito_NewProducto.setObjectName(u"Cartelito_NewProducto")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cartelito_NewProducto.sizePolicy().hasHeightForWidth())
        self.Cartelito_NewProducto.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.Cartelito_NewProducto.setFont(font)

        self.gridLayout_2.addWidget(self.Cartelito_NewProducto, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(20, -1, 15, -1)
        self.lblNombre = QLabel(newProducto)
        self.lblNombre.setObjectName(u"lblNombre")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblNombre.sizePolicy().hasHeightForWidth())
        self.lblNombre.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(9)
        self.lblNombre.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lblNombre)

        self.lnEditNombre = QLineEdit(newProducto)
        self.lnEditNombre.setObjectName(u"lnEditNombre")
        self.lnEditNombre.setMaximumSize(QSize(220, 22))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lnEditNombre)

        self.lblPrecio = QLabel(newProducto)
        self.lblPrecio.setObjectName(u"lblPrecio")
        self.lblPrecio.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lblPrecio)

        self.lnEditPrecio = QLineEdit(newProducto)
        self.lnEditPrecio.setObjectName(u"lnEditPrecio")
        self.lnEditPrecio.setMaximumSize(QSize(220, 22))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lnEditPrecio)

        self.label = QLabel(newProducto)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label)

        self.lnEditStockMinimo = QLineEdit(newProducto)
        self.lnEditStockMinimo.setObjectName(u"lnEditStockMinimo")
        self.lnEditStockMinimo.setMaximumSize(QSize(220, 22))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lnEditStockMinimo)

        self.lblDistr = QLabel(newProducto)
        self.lblDistr.setObjectName(u"lblDistr")
        self.lblDistr.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lblDistr)

        self.comboxDistr = QComboBox(newProducto)
        self.comboxDistr.setObjectName(u"comboxDistr")
        self.comboxDistr.setMaximumSize(QSize(220, 22))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.comboxDistr)


        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(25, 0, 10, 10)
        self.buttonBox = QDialogButtonBox(newProducto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(75, 24))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Help)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(newProducto)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(newProducto)

        #self.buttonBox.accepted.connect(newProducto.accept)
        self.buttonBox.rejected.connect(newProducto.reject)
        
        QMetaObject.connectSlotsByName(newProducto)
    # setupUi

    def retranslateUi(self, newProducto):
        newProducto.setWindowTitle(QCoreApplication.translate("newProducto", u"Nuevo Producto", None))
        self.Cartelito_NewProducto.setText(QCoreApplication.translate("newProducto", u"<html><head/><body><p><span style=\" font-weight:400;\">Ingrese los datos solicitados:</span></p></body></html>", None))
        self.lblNombre.setText(QCoreApplication.translate("newProducto", u"<html><head/><body><p>Nombre<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblPrecio.setText(QCoreApplication.translate("newProducto", u"<html><head/><body><p>Precio unitario<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("newProducto", u"<html><head/><body><p>Stock minimo<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.lblDistr.setText(QCoreApplication.translate("newProducto", u"<html><head/><body><p>Distribuidor <span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
    # retranslateUi

