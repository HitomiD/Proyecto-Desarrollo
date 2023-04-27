# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget,
    QWizard, QWizardPage)

class Ui_Crear_usuario(object):
    def setupUi(self, Crear_usuario):
        if not Crear_usuario.objectName():
            Crear_usuario.setObjectName(u"Crear_usuario")
        Crear_usuario.setEnabled(True)
        Crear_usuario.resize(373, 259)
        Crear_usuario.setMinimumSize(QSize(373, 259))
        Crear_usuario.setMaximumSize(QSize(373, 259))
        icon = QIcon()
        icon.addFile(u"windows/assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        Crear_usuario.setWindowIcon(icon)
        Crear_usuario.setStyleSheet(u"")
        Crear_usuario.setInputMethodHints(Qt.ImhNone)
        Crear_usuario.setSizeGripEnabled(False)
        Crear_usuario.setModal(False)
        Crear_usuario.setWizardStyle(QWizard.ModernStyle)
        Crear_usuario.setOptions(QWizard.HaveHelpButton|QWizard.NoBackButtonOnStartPage)
        Crear_usuario.setTitleFormat(Qt.PlainText)
        self.PrimeraPagina = QWizardPage()
        self.PrimeraPagina.setObjectName(u"PrimeraPagina")
        self.PrimeraPagina.setLocale(QLocale(QLocale.Spanish, QLocale.Argentina))
        self.verticalLayout_2 = QVBoxLayout(self.PrimeraPagina)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Titulo_label = QLabel(self.PrimeraPagina)
        self.Titulo_label.setObjectName(u"Titulo_label")
        font = QFont()
        font.setPointSize(16)
        self.Titulo_label.setFont(font)
        self.Titulo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.Titulo_label)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.Nombre_edit = QLineEdit(self.PrimeraPagina)
        self.Nombre_edit.setObjectName(u"Nombre_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Nombre_edit.sizePolicy().hasHeightForWidth())
        self.Nombre_edit.setSizePolicy(sizePolicy)
        self.Nombre_edit.setMaximumSize(QSize(220, 22))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.Nombre_edit)

        self.Telefono_label = QLabel(self.PrimeraPagina)
        self.Telefono_label.setObjectName(u"Telefono_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Telefono_label.sizePolicy().hasHeightForWidth())
        self.Telefono_label.setSizePolicy(sizePolicy1)
        self.Telefono_label.setStyleSheet(u"margin-right: 10px;\n"
"margin-left: 2px;")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.Telefono_label)

        self.Correo_edit = QLineEdit(self.PrimeraPagina)
        self.Correo_edit.setObjectName(u"Correo_edit")
        self.Correo_edit.setMaximumSize(QSize(220, 22))
        self.Correo_edit.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.Correo_edit)

        self.Nombre_label = QLabel(self.PrimeraPagina)
        self.Nombre_label.setObjectName(u"Nombre_label")
        self.Nombre_label.setStyleSheet(u"margin-right: 10px;\n"
"margin-left: 2px;")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.Nombre_label)

        self.Correo_label = QLabel(self.PrimeraPagina)
        self.Correo_label.setObjectName(u"Correo_label")
        self.Correo_label.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(30)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Correo_label.sizePolicy().hasHeightForWidth())
        self.Correo_label.setSizePolicy(sizePolicy2)
        self.Correo_label.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.Correo_label.setFont(font1)
        self.Correo_label.setStyleSheet(u"margin-right: 8px;\n"
"margin-left: 2px;")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.Correo_label)

        self.Telefono_edit = QLineEdit(self.PrimeraPagina)
        self.Telefono_edit.setObjectName(u"Telefono_edit")
        self.Telefono_edit.setMaximumSize(QSize(220, 22))
        self.Telefono_edit.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.Telefono_edit.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhPreferNumbers)
        self.Telefono_edit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.Telefono_edit)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.dataAbajo_label = QLabel(self.PrimeraPagina)
        self.dataAbajo_label.setObjectName(u"dataAbajo_label")
        self.dataAbajo_label.setScaledContents(False)
        self.dataAbajo_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.dataAbajo_label)

        Crear_usuario.addPage(self.PrimeraPagina)
        self.Crear_contrasea = QWizardPage()
        self.Crear_contrasea.setObjectName(u"Crear_contrasea")
        self.verticalLayout_3 = QVBoxLayout(self.Crear_contrasea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.Crear_contrasea)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.contraseniaLabel = QLabel(self.Crear_contrasea)
        self.contraseniaLabel.setObjectName(u"contraseniaLabel")
        self.contraseniaLabel.setStyleSheet(u"margin-left: 2px;")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.contraseniaLabel)

        self.contraseniaLineEdit = QLineEdit(self.Crear_contrasea)
        self.contraseniaLineEdit.setObjectName(u"contraseniaLineEdit")
        self.contraseniaLineEdit.setMaximumSize(QSize(220, 22))
        self.contraseniaLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.contraseniaLineEdit)

        self.confirmarContraseniaLabel = QLabel(self.Crear_contrasea)
        self.confirmarContraseniaLabel.setObjectName(u"confirmarContraseniaLabel")
        self.confirmarContraseniaLabel.setStyleSheet(u"margin-left: 2px;")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.confirmarContraseniaLabel)

        self.confirmarContraseniaLineEdit = QLineEdit(self.Crear_contrasea)
        self.confirmarContraseniaLineEdit.setObjectName(u"confirmarContraseniaLineEdit")
        self.confirmarContraseniaLineEdit.setMaximumSize(QSize(220, 22))
        self.confirmarContraseniaLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.confirmarContraseniaLineEdit)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.label_10 = QLabel(self.Crear_contrasea)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        Crear_usuario.addPage(self.Crear_contrasea)

        self.retranslateUi(Crear_usuario)

        QMetaObject.connectSlotsByName(Crear_usuario)
    # setupUi

    def retranslateUi(self, Crear_usuario):
        Crear_usuario.setWindowTitle(QCoreApplication.translate("Crear_usuario", u"Configuraci\u00f3n inicial", None))
        self.Titulo_label.setText(QCoreApplication.translate("Crear_usuario", u"<html><head/><body><p><span style=\" font-weight:700;\">Crear Usuario</span></p></body></html>", None))
        self.Nombre_edit.setPlaceholderText(QCoreApplication.translate("Crear_usuario", u"Ej.: Rodrigo Alvarez", None))
        self.Telefono_label.setText(QCoreApplication.translate("Crear_usuario", u"Tel\u00e9fono", None))
        self.Correo_edit.setPlaceholderText(QCoreApplication.translate("Crear_usuario", u"Ej.: ejemplo@ejemplo.com", None))
        self.Nombre_label.setText(QCoreApplication.translate("Crear_usuario", u"<html><head/><body><p>Nombre y apellido<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.Correo_label.setText(QCoreApplication.translate("Crear_usuario", u"<html><head/><body><p>Correo electr\u00f3nico<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.Telefono_edit.setInputMask("")
        self.Telefono_edit.setText("")
        self.Telefono_edit.setPlaceholderText(QCoreApplication.translate("Crear_usuario", u"Ej.: 2222554499", None))
        self.dataAbajo_label.setText(QCoreApplication.translate("Crear_usuario", u"<html><head/><body><p>Los campos se\u00f1alados con <span style=\" font-weight:700; color:#ff0000;\">*</span> son <span style=\" font-weight:700;\">obligatorios</span>. El correo electr\u00f3nico ser\u00e1 utilizado como medio de recuperaci\u00f3n de la contrase\u00f1a.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Crear_usuario", u"Crear Contrase\u00f1a", None))
        self.contraseniaLabel.setText(QCoreApplication.translate("Crear_usuario", u"<html><head/><body><p>Contrase\u00f1a<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.contraseniaLineEdit.setText("")
        self.confirmarContraseniaLabel.setText(QCoreApplication.translate("Crear_usuario", u"<html><head/><body><p>Confirmar contrase\u00f1a<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.confirmarContraseniaLineEdit.setText("")
        self.label_10.setText(QCoreApplication.translate("Crear_usuario", u"Se recomienda utilizar una contrase\u00f1a de 8 caracteres como m\u00ednimo y compuesta por may\u00fasculas,min\u00fasculas y n\u00fameros.", None))
    # retranslateUi

