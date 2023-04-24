# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Confirmacion.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialogo(object):
    def setupUi(self, Dialogo):
        if not Dialogo.objectName():
            Dialogo.setObjectName(u"Dialogo")
        Dialogo.resize(352, 212)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialogo.sizePolicy().hasHeightForWidth())
        Dialogo.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialogo.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(Dialogo)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 351, 196))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(308, 22))
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(45, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.LabelUsuario = QLabel(self.verticalLayoutWidget)
        self.LabelUsuario.setObjectName(u"LabelUsuario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelUsuario.sizePolicy().hasHeightForWidth())
        self.LabelUsuario.setSizePolicy(sizePolicy1)
        self.LabelUsuario.setFont(font)
        self.LabelUsuario.setStyleSheet(u"margin-right:10px;")
        self.LabelUsuario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.LabelUsuario)

        self.inputPassword_2 = QLineEdit(self.verticalLayoutWidget)
        self.inputPassword_2.setObjectName(u"inputPassword_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.inputPassword_2.sizePolicy().hasHeightForWidth())
        self.inputPassword_2.setSizePolicy(sizePolicy2)
        self.inputPassword_2.setMinimumSize(QSize(150, 0))
        self.inputPassword_2.setMaximumSize(QSize(220, 22))
        self.inputPassword_2.setFrame(True)
        self.inputPassword_2.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout.addWidget(self.inputPassword_2)

        self.horizontalSpacer_4 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.CONTRASENA = QLabel(self.verticalLayoutWidget)
        self.CONTRASENA.setObjectName(u"CONTRASENA")
        sizePolicy2.setHeightForWidth(self.CONTRASENA.sizePolicy().hasHeightForWidth())
        self.CONTRASENA.setSizePolicy(sizePolicy2)
        self.CONTRASENA.setMaximumSize(QSize(16777215, 16777215))
        self.CONTRASENA.setFont(font)
        self.CONTRASENA.setStyleSheet(u"margin-right:10px;")
        self.CONTRASENA.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.CONTRASENA)

        self.inputPassword = QLineEdit(self.verticalLayoutWidget)
        self.inputPassword.setObjectName(u"inputPassword")
        sizePolicy2.setHeightForWidth(self.inputPassword.sizePolicy().hasHeightForWidth())
        self.inputPassword.setSizePolicy(sizePolicy2)
        self.inputPassword.setMinimumSize(QSize(150, 0))
        self.inputPassword.setMaximumSize(QSize(220, 22))
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.inputPassword)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Ayuda = QDialogButtonBox(self.verticalLayoutWidget)
        self.Ayuda.setObjectName(u"Ayuda")
        self.Ayuda.setMaximumSize(QSize(330, 30))
        self.Ayuda.setLayoutDirection(Qt.LeftToRight)
        self.Ayuda.setOrientation(Qt.Horizontal)
        self.Ayuda.setStandardButtons(QDialogButtonBox.Help)

        self.horizontalLayout_4.addWidget(self.Ayuda)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMaximumSize(QSize(329, 24))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Dialogo)
        self.buttonBox.accepted.connect(Dialogo.accept)
        self.buttonBox.rejected.connect(Dialogo.reject)

        QMetaObject.connectSlotsByName(Dialogo)
    # setupUi

    def retranslateUi(self, Dialogo):
        Dialogo.setWindowTitle(QCoreApplication.translate("Dialogo", u"[ALERTA] Confirmar Cambios", None))
        self.label.setText(QCoreApplication.translate("Dialogo", u"<html><head/><body><p align=\"center\">Para confirmar el cambio, ingrese su <span style=\" color:#000000;\">usuario</span> y contrase\u00f1a</p></body></html>", None))
        self.LabelUsuario.setText(QCoreApplication.translate("Dialogo", u"<html><head/><body><p>Usuario: </p></body></html>", None))
        self.inputPassword_2.setInputMask("")
        self.inputPassword_2.setText("")
        self.CONTRASENA.setText(QCoreApplication.translate("Dialogo", u"<html><head/><body><p>Contrase\u00f1a: </p></body></html>", None))
        self.inputPassword.setInputMask("")
    # retranslateUi

