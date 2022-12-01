# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo-proveedor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFormLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(309, 204)
        Form.setStyleSheet(u".QLabel {\n"
"background-color:transparent;\n"
"color:black;\n"
"font-family:Fira Sans;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"display: flex;\n"
"background-color: transparent;\n"
"color: black;\n"
"align-items: center;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_5)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStyleSheet(u"label{\n"
"background-color:transparent;\n"
"color:white;\n"
"font-family:Fira Sans;\n"
"}")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuevo proveedor", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Raz\u00f3n social<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Direcci\u00f3n<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Tel\u00e9fono<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"E-Mail", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Agregar Proveedor", None))
    # retranslateUi

