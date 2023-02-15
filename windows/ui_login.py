# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import Recursos_rc
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1396, 683)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1371, 695))
        self.TODO = QVBoxLayout(self.verticalLayoutWidget)
        self.TODO.setSpacing(6)
        self.TODO.setObjectName(u"TODO")
        self.TODO.setSizeConstraint(QLayout.SetMaximumSize)
        self.TODO.setContentsMargins(5, 15, 5, 0)
        self.tituloLayout = QHBoxLayout()
        self.tituloLayout.setObjectName(u"tituloLayout")
        self.tituloLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_4)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 200))
        self.label_2.setPixmap(QPixmap(u":/Logos/Cajitas_v2.png"))
        self.label_2.setScaledContents(True)

        self.tituloLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Cantarell"])
        font.setPointSize(35)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.RichText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(0)

        self.tituloLayout.addWidget(self.label_4)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_20)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_18)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tituloLayout.addItem(self.horizontalSpacer_3)


        self.TODO.addLayout(self.tituloLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.TODO.addItem(self.verticalSpacer_4)

        self.LayOutUsuario = QHBoxLayout()
        self.LayOutUsuario.setSpacing(0)
        self.LayOutUsuario.setObjectName(u"LayOutUsuario")
        self.LayOutUsuario.setContentsMargins(-1, -1, -1, 0)
        self.DerSpacer = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutUsuario.addItem(self.DerSpacer)

        self.LayOutInternoUsuario = QVBoxLayout()
        self.LayOutInternoUsuario.setObjectName(u"LayOutInternoUsuario")
        self.LayOutInternoUsuario.setContentsMargins(-1, 0, -1, -1)
        self.LabelUsuario = QLabel(self.verticalLayoutWidget)
        self.LabelUsuario.setObjectName(u"LabelUsuario")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelUsuario.sizePolicy().hasHeightForWidth())
        self.LabelUsuario.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(15)
        self.LabelUsuario.setFont(font1)
        self.LabelUsuario.setAlignment(Qt.AlignCenter)

        self.LayOutInternoUsuario.addWidget(self.LabelUsuario)

        self.LayOutInputUsuario = QHBoxLayout()
        self.LayOutInputUsuario.setSpacing(0)
        self.LayOutInputUsuario.setObjectName(u"LayOutInputUsuario")
        self.LayOutInputUsuario.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_22 = QSpacerItem(140, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutInputUsuario.addItem(self.horizontalSpacer_22)

        self.CasillaUsuario = QLineEdit(self.verticalLayoutWidget)
        self.CasillaUsuario.setObjectName(u"CasillaUsuario")
        self.CasillaUsuario.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CasillaUsuario.sizePolicy().hasHeightForWidth())
        self.CasillaUsuario.setSizePolicy(sizePolicy1)
        self.CasillaUsuario.setMinimumSize(QSize(180, 0))
        self.CasillaUsuario.setMaximumSize(QSize(150, 16777215))
        self.CasillaUsuario.setBaseSize(QSize(0, 0))

        self.LayOutInputUsuario.addWidget(self.CasillaUsuario, 0, Qt.AlignHCenter)

        self.horizontalSpacer_23 = QSpacerItem(140, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutInputUsuario.addItem(self.horizontalSpacer_23)


        self.LayOutInternoUsuario.addLayout(self.LayOutInputUsuario)


        self.LayOutUsuario.addLayout(self.LayOutInternoUsuario)

        self.IzqSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutUsuario.addItem(self.IzqSpacer)


        self.TODO.addLayout(self.LayOutUsuario)

        self.LayOutContrasenia = QHBoxLayout()
        self.LayOutContrasenia.setObjectName(u"LayOutContrasenia")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutContrasenia.addItem(self.horizontalSpacer)

        self.LayOutInternoContrasena = QVBoxLayout()
        self.LayOutInternoContrasena.setObjectName(u"LayOutInternoContrasena")
        self.CONTRASENA = QLabel(self.verticalLayoutWidget)
        self.CONTRASENA.setObjectName(u"CONTRASENA")
        sizePolicy.setHeightForWidth(self.CONTRASENA.sizePolicy().hasHeightForWidth())
        self.CONTRASENA.setSizePolicy(sizePolicy)
        self.CONTRASENA.setFont(font1)
        self.CONTRASENA.setAlignment(Qt.AlignCenter)

        self.LayOutInternoContrasena.addWidget(self.CONTRASENA)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.inputPassword = QLineEdit(self.verticalLayoutWidget)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setMinimumSize(QSize(150, 0))
        self.inputPassword.setMaximumSize(QSize(300, 16777215))
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.inputPassword)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.LayOutInternoContrasena.addLayout(self.horizontalLayout_3)

        self.LayOutIngresar = QHBoxLayout()
        self.LayOutIngresar.setSpacing(5)
        self.LayOutIngresar.setObjectName(u"LayOutIngresar")
        self.LayOutIngresar.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutIngresar.addItem(self.horizontalSpacer_13)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(200, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 193, 13);\n"
"color:white;\n"
"border:none;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"font-family:Fira Sans;\n"
"padding: 5px 5px 7px 5px;\n"
"border-radius:5px;")

        self.LayOutIngresar.addWidget(self.pushButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutIngresar.addItem(self.horizontalSpacer_14)


        self.LayOutInternoContrasena.addLayout(self.LayOutIngresar)


        self.LayOutContrasenia.addLayout(self.LayOutInternoContrasena)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutContrasenia.addItem(self.horizontalSpacer_2)


        self.TODO.addLayout(self.LayOutContrasenia)

        self.LayOutDelFondo = QHBoxLayout()
        self.LayOutDelFondo.setObjectName(u"LayOutDelFondo")
        self.LayOutDelFondo.setContentsMargins(25, -1, 6, -1)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: transparent;\n"
"color:blue;\n"
"font-weight: bold;")

        self.LayOutDelFondo.addWidget(self.pushButton_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutDelFondo.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutDelFondo.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.LayOutDelFondo.addItem(self.horizontalSpacer_7)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(55, 55))
        self.label_5.setSizeIncrement(QSize(25, 25))
        self.label_5.setPixmap(QPixmap(u":/Logos/Escudo-Club.png"))
        self.label_5.setScaledContents(True)

        self.LayOutDelFondo.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setSizeIncrement(QSize(25, 25))
        font2 = QFont()
        font2.setFamilies([u"Noto Serif Display Bold"])
        font2.setBold(True)
        self.label_6.setFont(font2)
        self.label_6.setTextFormat(Qt.RichText)
        self.label_6.setWordWrap(True)

        self.LayOutDelFondo.addWidget(self.label_6)


        self.TODO.addLayout(self.LayOutDelFondo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1396, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gestion de Inventario", None))
        self.LabelUsuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Usuario</span></p></body></html>", None))
        self.CONTRASENA.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Contrase\u00f1a</span></p></body></html>", None))
        self.inputPassword.setInputMask("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"INGRESAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u00bfProblemas para\n"
" iniciar sesi\u00f3n?", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Club Atl\u00e9tico <span style=\" font-size:12pt;\">Sarmiento</span></p></body></html>", None))
    # retranslateUi

