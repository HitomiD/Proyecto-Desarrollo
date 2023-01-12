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
        newProveedor.resize(309, 230)
        self.verticalLayout = QVBoxLayout(newProveedor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_11 = QLabel(newProveedor)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_9 = QLineEdit(newProveedor)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)

        self.label_12 = QLabel(newProveedor)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_10 = QLineEdit(newProveedor)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_10)

        self.label_13 = QLabel(newProveedor)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.lineEdit_11 = QLineEdit(newProveedor)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(newProveedor)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_12)

        self.label_14 = QLabel(newProveedor)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(newProveedor)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"display: flex;\n"
"background-color: transparent;\n"
"color: black;\n"
"align-items: center;")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_15)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.buttonBox = QDialogButtonBox(newProveedor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(newProveedor)
        self.buttonBox.accepted.connect(newProveedor.accept)
        self.buttonBox.rejected.connect(newProveedor.reject)

        QMetaObject.connectSlotsByName(newProveedor)
    # setupUi

    def retranslateUi(self, newProveedor):
        newProveedor.setWindowTitle(QCoreApplication.translate("newProveedor", u"Nuevo Proveedor", None))
        self.label_11.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Raz\u00f3n social<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Direcci\u00f3n<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("newProveedor", u"<html><head/><body><p>Tel\u00e9fono<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("newProveedor", u"E-Mail", None))
        self.label_15.setText(QCoreApplication.translate("newProveedor", u"Agregar Proveedor", None))
    # retranslateUi

