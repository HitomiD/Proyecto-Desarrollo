# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget,
    QWizard, QWizardPage)

class Ui_Wizard(object):
    def setupUi(self, Wizard):
        if not Wizard.objectName():
            Wizard.setObjectName(u"Wizard")
        Wizard.resize(404, 329)
        Wizard.setStyleSheet(u"")
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.wizardPage1.setLocale(QLocale(QLocale.Spanish, QLocale.Argentina))
        self.verticalLayout_2 = QVBoxLayout(self.wizardPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.wizardPage1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lineEdit_2 = QLineEdit(self.wizardPage1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_5 = QLabel(self.wizardPage1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_4 = QLineEdit(self.wizardPage1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.wizardPage1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_5)

        self.label_6 = QLabel(self.wizardPage1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.wizardPage1)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_7)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_8 = QLabel(self.wizardPage1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_8)

        Wizard.addPage(self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.verticalLayout_3 = QVBoxLayout(self.wizardPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.wizardPage2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.contraseniaLabel = QLabel(self.wizardPage2)
        self.contraseniaLabel.setObjectName(u"contraseniaLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.contraseniaLabel)

        self.contraseniaLineEdit = QLineEdit(self.wizardPage2)
        self.contraseniaLineEdit.setObjectName(u"contraseniaLineEdit")
        self.contraseniaLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.contraseniaLineEdit)

        self.confirmarContraseniaLabel = QLabel(self.wizardPage2)
        self.confirmarContraseniaLabel.setObjectName(u"confirmarContraseniaLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.confirmarContraseniaLabel)

        self.confirmarContraseniaLineEdit = QLineEdit(self.wizardPage2)
        self.confirmarContraseniaLineEdit.setObjectName(u"confirmarContraseniaLineEdit")
        self.confirmarContraseniaLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.confirmarContraseniaLineEdit)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.label_10 = QLabel(self.wizardPage2)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_10.setFont(font1)
        self.label_10.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_11 = QLabel(self.wizardPage2)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setBold(True)
        self.label_11.setFont(font2)
        self.label_11.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_11)

        Wizard.addPage(self.wizardPage2)

        self.retranslateUi(Wizard)

        QMetaObject.connectSlotsByName(Wizard)
    # setupUi

    def retranslateUi(self, Wizard):
        Wizard.setWindowTitle(QCoreApplication.translate("Wizard", u"Configuraci\u00f3n inicial", None))
        self.label.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p><span style=\" font-weight:700;\">Informaci\u00f3n Administrador</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Wizard", u"Tel\u00e9fono", None))
        self.label_6.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>Nombre y apellido<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>Correo electr\u00f3nico<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>Los campos se\u00f1alados con <span style=\" font-weight:700; color:#ff0000;\">*</span> son obligatorios. El correo electr\u00f3nico ser\u00e1 utilizado como medio de recuperaci\u00f3n de la contrase\u00f1a.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Wizard", u"Crear contrase\u00f1a", None))
        self.contraseniaLabel.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>Contrase\u00f1a<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.contraseniaLineEdit.setText("")
        self.confirmarContraseniaLabel.setText(QCoreApplication.translate("Wizard", u"<html><head/><body><p>Confirmar contrase\u00f1a<span style=\" font-weight:700; color:#ff0000;\">*</span></p></body></html>", None))
        self.confirmarContraseniaLineEdit.setText("")
        self.label_10.setText(QCoreApplication.translate("Wizard", u"Se recomienda utilizar una contrase\u00f1a de 8 caracteres como m\u00ednimo y compuesta por may\u00fasculas,min\u00fasculas y n\u00fameros.", None))
        self.label_11.setText(QCoreApplication.translate("Wizard", u"En caso de p\u00e9rdida se utilizar\u00e1 la direcci\u00f3n de correo electr\u00f3nico del administrador como medio de recuperaci\u00f3n.", None))
    # retranslateUi

