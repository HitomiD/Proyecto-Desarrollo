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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(820, 520))
        MainWindow.setMaximumSize(QSize(820, 520))
        icon = QIcon()
        icon.addFile(u"../assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        icon1 = QIcon()
        icon1.addFile(u"../assets/Interrogation - 60x60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAcerca_de.setIcon(icon1)
        self.actionCrear_Usuario = QAction(MainWindow)
        self.actionCrear_Usuario.setObjectName(u"actionCrear_Usuario")
        icon2 = QIcon()
        icon2.addFile(u"../assets/Info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCrear_Usuario.setIcon(icon2)
        self.actionCrear_Usuario_2 = QAction(MainWindow)
        self.actionCrear_Usuario_2.setObjectName(u"actionCrear_Usuario_2")
        icon3 = QIcon()
        icon3.addFile(u"../assets/User.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCrear_Usuario_2.setIcon(icon3)
        self.actionCrear_Usuario_2.setShortcutContext(Qt.WindowShortcut)
        self.actionEliminar_Usuario = QAction(MainWindow)
        self.actionEliminar_Usuario.setObjectName(u"actionEliminar_Usuario")
        icon4 = QIcon()
        icon4.addFile(u"../assets/BanUser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar_Usuario.setIcon(icon4)
        self.actionModificar_Usuario = QAction(MainWindow)
        self.actionModificar_Usuario.setObjectName(u"actionModificar_Usuario")
        icon5 = QIcon()
        icon5.addFile(u"../assets/ModUser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionModificar_Usuario.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 821, 501))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: transparent;\n"
"color:blue;\n"
"font-weight: bold;\n"
"margin-left:30px;")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"margin-right:30px;")
        self.label.setPixmap(QPixmap(u"../assets/Escudo-black.png"))

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_39)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_38)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 200))
        self.label_2.setPixmap(QPixmap(u"../assets/Logo_Ventanas.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.gridLayoutWidget)
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

        self.horizontalLayout.addWidget(self.label_4)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_41)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_40)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_37)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_34)

        self.LabelUsuario = QLabel(self.gridLayoutWidget)
        self.LabelUsuario.setObjectName(u"LabelUsuario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LabelUsuario.sizePolicy().hasHeightForWidth())
        self.LabelUsuario.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(15)
        self.LabelUsuario.setFont(font1)
        self.LabelUsuario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.LabelUsuario)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_36)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_35)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_30)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_31)

        self.inputUsuario = QLineEdit(self.gridLayoutWidget)
        self.inputUsuario.setObjectName(u"inputUsuario")
        self.inputUsuario.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.inputUsuario.sizePolicy().hasHeightForWidth())
        self.inputUsuario.setSizePolicy(sizePolicy2)
        self.inputUsuario.setMinimumSize(QSize(180, 0))
        self.inputUsuario.setMaximumSize(QSize(180, 22))
        self.inputUsuario.setBaseSize(QSize(0, 0))
        self.inputUsuario.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.inputUsuario)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_33)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_32)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_26)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_27)

        self.CONTRASENA = QLabel(self.gridLayoutWidget)
        self.CONTRASENA.setObjectName(u"CONTRASENA")
        sizePolicy1.setHeightForWidth(self.CONTRASENA.sizePolicy().hasHeightForWidth())
        self.CONTRASENA.setSizePolicy(sizePolicy1)
        self.CONTRASENA.setFont(font1)
        self.CONTRASENA.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.CONTRASENA)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_29)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_28)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_23)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_22)

        self.inputPassword = QLineEdit(self.gridLayoutWidget)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setMinimumSize(QSize(180, 22))
        self.inputPassword.setMaximumSize(QSize(300, 22))
        self.inputPassword.setStyleSheet(u"border-color: rgb(255, 0, 255);")
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.inputPassword)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_25)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_24)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_42)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_18)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_20)

        self.btnIngresar = QPushButton(self.gridLayoutWidget)
        self.btnIngresar.setObjectName(u"btnIngresar")
        self.btnIngresar.setMaximumSize(QSize(200, 16777215))
        self.btnIngresar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnIngresar.setStyleSheet(u"background-color: rgb(0, 193, 13);\n"
"color:white;\n"
"border:none;\n"
"border-radius:3px;\n"
"font-size: 14px;\n"
"font-weight: 500;\n"
"padding: 5px 5px 7px 5px;\n"
"margin-top:15px;\n"
"")

        self.horizontalLayout_2.addWidget(self.btnIngresar)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_21)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_43)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_19)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 20))
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuUsuarios = QMenu(self.menubar)
        self.menuUsuarios.setObjectName(u"menuUsuarios")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuUsuarios.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuAyuda.addAction(self.actionCrear_Usuario)
        self.menuUsuarios.addAction(self.actionCrear_Usuario_2)
        self.menuUsuarios.addAction(self.actionModificar_Usuario)
        self.menuUsuarios.addAction(self.actionEliminar_Usuario)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Club Atletico Sarmiento - Gestion de Inventario", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Manual del Usuario", None))
        self.actionCrear_Usuario.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
        self.actionCrear_Usuario_2.setText(QCoreApplication.translate("MainWindow", u"Crear Usuario", None))
        self.actionEliminar_Usuario.setText(QCoreApplication.translate("MainWindow", u"Eliminar Usuario", None))
        self.actionModificar_Usuario.setText(QCoreApplication.translate("MainWindow", u"Modificar Usuario", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u00bfProblemas para\n"
" iniciar sesi\u00f3n?", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gestion de Inventario", None))
        self.LabelUsuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Usuario</span></p></body></html>", None))
        self.CONTRASENA.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Contrase\u00f1a</span></p></body></html>", None))
        self.inputPassword.setInputMask("")
        self.btnIngresar.setText(QCoreApplication.translate("MainWindow", u"INGRESAR", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuUsuarios.setTitle(QCoreApplication.translate("MainWindow", u"Usuarios", None))
    # retranslateUi

