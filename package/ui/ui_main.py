# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        if not MenuPrincipal.objectName():
            MenuPrincipal.setObjectName(u"MenuPrincipal")
        MenuPrincipal.setEnabled(True)
        MenuPrincipal.resize(846, 663)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MenuPrincipal.sizePolicy().hasHeightForWidth())
        MenuPrincipal.setSizePolicy(sizePolicy)
        MenuPrincipal.setMaximumSize(QSize(846, 663))
        icon = QIcon()
        icon.addFile(u"windows/assets/Logo_Ventanas.png", QSize(), QIcon.Normal, QIcon.Off)
        MenuPrincipal.setWindowIcon(icon)
        MenuPrincipal.setWindowOpacity(1.000000000000000)
        MenuPrincipal.setStyleSheet(u"background-color: white;\n"
"")
        self.actionAcerca_de = QAction(MenuPrincipal)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        icon1 = QIcon()
        icon1.addFile(u"windows/assets/Interrogation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAcerca_de.setIcon(icon1)
        self.actionExportar_como_PDF = QAction(MenuPrincipal)
        self.actionExportar_como_PDF.setObjectName(u"actionExportar_como_PDF")
        icon2 = QIcon()
        icon2.addFile(u"windows/assets/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExportar_como_PDF.setIcon(icon2)
        self.actionManual_del_Usuario = QAction(MenuPrincipal)
        self.actionManual_del_Usuario.setObjectName(u"actionManual_del_Usuario")
        icon3 = QIcon()
        icon3.addFile(u"windows/assets/Info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionManual_del_Usuario.setIcon(icon3)
        self.centralwidget = QWidget(MenuPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 10, 857, 100))
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(857, 100))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(84, 84, 84)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.LogoInterno = QLabel(self.frame)
        self.LogoInterno.setObjectName(u"LogoInterno")
        self.LogoInterno.setEnabled(True)
        self.LogoInterno.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(False)
        self.LogoInterno.setFont(font1)
        self.LogoInterno.setStyleSheet(u"")
        self.LogoInterno.setTextFormat(Qt.RichText)
        self.LogoInterno.setPixmap(QPixmap(u"windows/assets/Escudo-Interno - copia.png"))

        self.horizontalLayout_2.addWidget(self.LogoInterno)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 116, 841, 511))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabInventario = QWidget()
        self.tabInventario.setObjectName(u"tabInventario")
        self.frame_5 = QFrame(self.tabInventario)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 0, 141, 421))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(9, 10, 120, 391))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(120, 0))
        self.lblFiltroProv = QLabel(self.groupBox)
        self.lblFiltroProv.setObjectName(u"lblFiltroProv")
        self.lblFiltroProv.setGeometry(QRect(7, 150, 61, 20))
        self.filtroProveedor = QComboBox(self.groupBox)
        self.filtroProveedor.addItem("")
        self.filtroProveedor.setObjectName(u"filtroProveedor")
        self.filtroProveedor.setGeometry(QRect(10, 170, 101, 23))
        self.frame_6 = QFrame(self.tabInventario)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(180, 0, 641, 421))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.groupBox_2 = QGroupBox(self.frame_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 621, 391))
        self.tablaInventario = QTableWidget(self.groupBox_2)
        if (self.tablaInventario.columnCount() < 7):
            self.tablaInventario.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaInventario.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tablaInventario.setObjectName(u"tablaInventario")
        self.tablaInventario.setEnabled(True)
        self.tablaInventario.setGeometry(QRect(0, 20, 621, 371))
        sizePolicy2.setHeightForWidth(self.tablaInventario.sizePolicy().hasHeightForWidth())
        self.tablaInventario.setSizePolicy(sizePolicy2)
        self.tablaInventario.setMaximumSize(QSize(815, 414))
        self.tablaInventario.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.tablaInventario.setInputMethodHints(Qt.ImhNone)
        self.tablaInventario.setFrameShape(QFrame.Panel)
        self.tablaInventario.setFrameShadow(QFrame.Plain)
        self.tablaInventario.setLineWidth(1)
        self.tablaInventario.setMidLineWidth(0)
        self.tablaInventario.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaInventario.setAutoScroll(True)
        self.tablaInventario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaInventario.setAlternatingRowColors(True)
        self.tablaInventario.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaInventario.setTextElideMode(Qt.ElideMiddle)
        self.tablaInventario.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tablaInventario.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tablaInventario.setSortingEnabled(False)
        self.tablaInventario.setWordWrap(True)
        self.tablaInventario.setRowCount(0)
        self.tablaInventario.setColumnCount(7)
        self.tablaInventario.horizontalHeader().setVisible(True)
        self.tablaInventario.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaInventario.horizontalHeader().setMinimumSectionSize(40)
        self.tablaInventario.horizontalHeader().setDefaultSectionSize(108)
        self.tablaInventario.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaInventario.horizontalHeader().setStretchLastSection(False)
        self.tablaInventario.verticalHeader().setVisible(False)
        self.tablaInventario.verticalHeader().setMinimumSectionSize(30)
        self.tablaInventario.verticalHeader().setDefaultSectionSize(30)
        self.tablaInventario.verticalHeader().setHighlightSections(True)
        self.tablaInventario.verticalHeader().setProperty("showSortIndicator", True)
        self.tablaInventario.verticalHeader().setStretchLastSection(False)
        self.widget = QWidget(self.tabInventario)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 432, 821, 42))
        self.layoutBtnInventario = QHBoxLayout(self.widget)
        self.layoutBtnInventario.setObjectName(u"layoutBtnInventario")
        self.layoutBtnInventario.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_9)

        self.btnNuevoProducto = QPushButton(self.tabInventario)
        self.btnNuevoProducto.setObjectName(u"btnNuevoProducto")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnNuevoProducto.sizePolicy().hasHeightForWidth())
        self.btnNuevoProducto.setSizePolicy(sizePolicy3)
        self.btnNuevoProducto.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.btnNuevoProducto.setFont(font3)
        self.btnNuevoProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoProducto.setStyleSheet(u"background-color: #6daa44;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"windows/assets/Plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNuevoProducto.setIcon(icon4)
        self.btnNuevoProducto.setIconSize(QSize(35, 35))

        self.layoutBtnInventario.addWidget(self.btnNuevoProducto)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_2)

        self.btnModProducto = QPushButton(self.tabInventario)
        self.btnModProducto.setObjectName(u"btnModProducto")
        self.btnModProducto.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.btnModProducto.setFont(font3)
        self.btnModProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModProducto.setStyleSheet(u"background-color: #006dab;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"windows/assets/Pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnModProducto.setIcon(icon5)
        self.btnModProducto.setIconSize(QSize(30, 30))

        self.layoutBtnInventario.addWidget(self.btnModProducto)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_4)

        self.btnElimProducto = QPushButton(self.tabInventario)
        self.btnElimProducto.setObjectName(u"btnElimProducto")
        self.btnElimProducto.setMinimumSize(QSize(150, 0))
        self.btnElimProducto.setFont(font3)
        self.btnElimProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimProducto.setStyleSheet(u"background-color: #c80000;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"windows/assets/Trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnElimProducto.setIcon(icon6)
        self.btnElimProducto.setIconSize(QSize(35, 35))

        self.layoutBtnInventario.addWidget(self.btnElimProducto)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_12)

        self.tabWidget.addTab(self.tabInventario, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(380, 0, 441, 421))
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.groupBoxProveedor = QGroupBox(self.frame_2)
        self.groupBoxProveedor.setObjectName(u"groupBoxProveedor_6")
        self.groupBoxProveedor.setEnabled(False)
        self.groupBoxProveedor.setGeometry(QRect(10, 10, 421, 151))
        self.groupBoxProveedor.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.groupBoxProveedor.setFlat(False)
        self.groupBoxProveedor.setCheckable(False)
        self.groupBoxProveedor.setChecked(False)
        self.gridLayout_7 = QGridLayout(self.groupBoxProveedor)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tagProveedor = QLabel(self.groupBoxProveedor)
        self.tagProveedor.setObjectName(u"tagProveedor")

        self.gridLayout_7.addWidget(self.tagProveedor, 0, 0, 1, 1)

        self.nombreProveedor = QLineEdit(self.groupBoxProveedor)
        self.nombreProveedor.setObjectName(u"nombreProveedor")

        self.gridLayout_7.addWidget(self.nombreProveedor, 0, 1, 1, 1)

        self.telefonoProveedor = QLineEdit(self.groupBoxProveedor)
        self.telefonoProveedor.setObjectName(u"telefonoProveedor")

        self.gridLayout_7.addWidget(self.telefonoProveedor, 2, 1, 1, 1)

        self.tagCUIL_6 = QLabel(self.groupBoxProveedor)
        self.tagCUIL_6.setObjectName(u"tagCUIL_6")

        self.gridLayout_7.addWidget(self.tagCUIL_6, 1, 0, 1, 1)

        self.tagTelefono_6 = QLabel(self.groupBoxProveedor)
        self.tagTelefono_6.setObjectName(u"tagTelefono_6")

        self.gridLayout_7.addWidget(self.tagTelefono_6, 2, 0, 1, 1)

        self.cuilProveedor = QLineEdit(self.groupBoxProveedor)
        self.cuilProveedor.setObjectName(u"cuilProveedor")
        self.cuilProveedor.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.gridLayout_7.addWidget(self.cuilProveedor, 1, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.frame_2)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 170, 422, 231))
        sizePolicy1.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy1)
        self.tablaIngresosDetalle = QTableWidget(self.groupBox_10)
        if (self.tablaIngresosDetalle.columnCount() < 3):
            self.tablaIngresosDetalle.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.tablaIngresosDetalle.setObjectName(u"tablaIngresosDetalle")
        self.tablaIngresosDetalle.setEnabled(True)
        self.tablaIngresosDetalle.setGeometry(QRect(0, 18, 422, 211))
        sizePolicy1.setHeightForWidth(self.tablaIngresosDetalle.sizePolicy().hasHeightForWidth())
        self.tablaIngresosDetalle.setSizePolicy(sizePolicy1)
        self.tablaIngresosDetalle.setMinimumSize(QSize(422, 0))
        self.tablaIngresosDetalle.setMaximumSize(QSize(424, 16777215))
        self.tablaIngresosDetalle.setMouseTracking(False)
        self.tablaIngresosDetalle.setTabletTracking(False)
        self.tablaIngresosDetalle.setLayoutDirection(Qt.LeftToRight)
        self.tablaIngresosDetalle.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaIngresosDetalle.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaIngresosDetalle.setAlternatingRowColors(True)
        self.tablaIngresosDetalle.setWordWrap(False)
        self.tablaIngresosDetalle.setCornerButtonEnabled(False)
        self.tablaIngresosDetalle.verticalHeader().setVisible(False)
        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 430, 831, 42))
        self.layoutBtnProveedores_4 = QHBoxLayout(self.layoutWidget_2)
        self.layoutBtnProveedores_4.setObjectName(u"layoutBtnProveedores_4")
        self.layoutBtnProveedores_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_31)

        self.btnNuevoIngreso = QPushButton(self.layoutWidget_2)
        self.btnNuevoIngreso.setObjectName(u"btnNuevoIngreso")
        sizePolicy3.setHeightForWidth(self.btnNuevoIngreso.sizePolicy().hasHeightForWidth())
        self.btnNuevoIngreso.setSizePolicy(sizePolicy3)
        self.btnNuevoIngreso.setMinimumSize(QSize(150, 0))
        self.btnNuevoIngreso.setFont(font3)
        self.btnNuevoIngreso.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoIngreso.setStyleSheet(u"background-color: #6daa44;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        self.btnNuevoIngreso.setIcon(icon4)
        self.btnNuevoIngreso.setIconSize(QSize(35, 35))

        self.layoutBtnProveedores_4.addWidget(self.btnNuevoIngreso)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_36)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 0, 341, 421))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.groupBox_5 = QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 321, 391))
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.tablaIngresos = QTableWidget(self.groupBox_5)
        if (self.tablaIngresos.columnCount() < 3):
            self.tablaIngresos.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setForeground(brush);
        self.tablaIngresos.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.tablaIngresos.setObjectName(u"tablaIngresos")
        self.tablaIngresos.setEnabled(True)
        self.tablaIngresos.setGeometry(QRect(0, 20, 321, 371))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tablaIngresos.sizePolicy().hasHeightForWidth())
        self.tablaIngresos.setSizePolicy(sizePolicy4)
        self.tablaIngresos.setMinimumSize(QSize(0, 0))
        self.tablaIngresos.setMaximumSize(QSize(16777215, 16777215))
        self.tablaIngresos.setBaseSize(QSize(0, 0))
        self.tablaIngresos.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tablaIngresos.setStyleSheet(u"background-color: white;\n"
"color:black;\n"
"gridline-color: black;\n"
"selection-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.tablaIngresos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaIngresos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaIngresos.setAutoScroll(True)
        self.tablaIngresos.setAutoScrollMargin(10)
        self.tablaIngresos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaIngresos.setTabKeyNavigation(True)
        self.tablaIngresos.setProperty("showDropIndicator", False)
        self.tablaIngresos.setDragEnabled(False)
        self.tablaIngresos.setAlternatingRowColors(True)
        self.tablaIngresos.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaIngresos.setShowGrid(True)
        self.tablaIngresos.setGridStyle(Qt.SolidLine)
        self.tablaIngresos.setSortingEnabled(False)
        self.tablaIngresos.setCornerButtonEnabled(True)
        self.tablaIngresos.horizontalHeader().setVisible(True)
        self.tablaIngresos.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaIngresos.horizontalHeader().setMinimumSectionSize(20)
        self.tablaIngresos.horizontalHeader().setDefaultSectionSize(100)
        self.tablaIngresos.horizontalHeader().setHighlightSections(True)
        self.tablaIngresos.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaIngresos.horizontalHeader().setStretchLastSection(False)
        self.tablaIngresos.verticalHeader().setVisible(False)
        self.tablaIngresos.verticalHeader().setHighlightSections(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.layoutBtnProveedores_3 = QHBoxLayout()
        self.layoutBtnProveedores_3.setObjectName(u"layoutBtnProveedores_3")
        self.layoutBtnProveedores_3.setSizeConstraint(QLayout.SetFixedSize)
        self.layoutBtnProveedores_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_3.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_3.addItem(self.horizontalSpacer_20)

        self.btnNuevoProveedor = QPushButton(self.tab)
        self.btnNuevoProveedor.setObjectName(u"btnNuevoProveedor")
        sizePolicy3.setHeightForWidth(self.btnNuevoProveedor.sizePolicy().hasHeightForWidth())
        self.btnNuevoProveedor.setSizePolicy(sizePolicy3)
        self.btnNuevoProveedor.setMinimumSize(QSize(150, 0))
        self.btnNuevoProveedor.setFont(font3)
        self.btnNuevoProveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoProveedor.setStyleSheet(u"background-color: #6daa44;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        self.btnNuevoProveedor.setIcon(icon4)
        self.btnNuevoProveedor.setIconSize(QSize(35, 35))

        self.layoutBtnProveedores_3.addWidget(self.btnNuevoProveedor)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_3.addItem(self.horizontalSpacer_21)

        self.btnModProveedor = QPushButton(self.tab)
        self.btnModProveedor.setObjectName(u"btnModProveedor")
        self.btnModProveedor.setMinimumSize(QSize(150, 0))
        self.btnModProveedor.setFont(font3)
        self.btnModProveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModProveedor.setStyleSheet(u"background-color: #006dab;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        self.btnModProveedor.setIcon(icon5)
        self.btnModProveedor.setIconSize(QSize(30, 30))

        self.layoutBtnProveedores_3.addWidget(self.btnModProveedor)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_3.addItem(self.horizontalSpacer_22)

        self.btnElimProveedor = QPushButton(self.tab)
        self.btnElimProveedor.setObjectName(u"btnElimProveedor")
        self.btnElimProveedor.setMinimumSize(QSize(150, 0))
        self.btnElimProveedor.setFont(font3)
        self.btnElimProveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimProveedor.setStyleSheet(u"background-color: #c80000;\n"
"color: white;\n"
"border-radius:5px;\n"
"height: 40%;\n"
"font-weight: 600;\n"
"")
        self.btnElimProveedor.setIcon(icon6)
        self.btnElimProveedor.setIconSize(QSize(35, 35))

        self.layoutBtnProveedores_3.addWidget(self.btnElimProveedor)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_3.addItem(self.horizontalSpacer_29)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_3.addItem(self.horizontalSpacer_30)


        self.gridLayout_2.addLayout(self.layoutBtnProveedores_3, 2, 0, 1, 1)

        self.tablaProveedores = QTableWidget(self.tab)
        if (self.tablaProveedores.columnCount() < 6):
            self.tablaProveedores.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.tablaProveedores.setObjectName(u"tablaProveedores")
        self.tablaProveedores.setEnabled(False)
        sizePolicy.setHeightForWidth(self.tablaProveedores.sizePolicy().hasHeightForWidth())
        self.tablaProveedores.setSizePolicy(sizePolicy)
        self.tablaProveedores.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaProveedores.setFrameShadow(QFrame.Plain)
        self.tablaProveedores.setLineWidth(5)
        self.tablaProveedores.setMidLineWidth(0)
        self.tablaProveedores.setAutoScroll(True)
        self.tablaProveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaProveedores.setAlternatingRowColors(True)
        self.tablaProveedores.horizontalHeader().setVisible(True)
        self.tablaProveedores.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaProveedores.horizontalHeader().setMinimumSectionSize(7)
        self.tablaProveedores.horizontalHeader().setDefaultSectionSize(131)
        self.tablaProveedores.horizontalHeader().setHighlightSections(True)
        self.tablaProveedores.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaProveedores.horizontalHeader().setStretchLastSection(False)
        self.tablaProveedores.verticalHeader().setVisible(False)
        self.tablaProveedores.verticalHeader().setCascadingSectionResizes(False)
        self.tablaProveedores.verticalHeader().setMinimumSectionSize(25)
        self.tablaProveedores.verticalHeader().setDefaultSectionSize(30)
        self.tablaProveedores.verticalHeader().setHighlightSections(True)
        self.tablaProveedores.verticalHeader().setProperty("showSortIndicator", False)
        self.tablaProveedores.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tablaProveedores, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        MenuPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MenuPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        MenuPrincipal.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MenuPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 20))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MenuPrincipal.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionExportar_como_PDF)
        self.menuAyuda.addAction(self.actionManual_del_Usuario)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(MenuPrincipal)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MenuPrincipal)
    # setupUi

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QCoreApplication.translate("MenuPrincipal", u"Menu Principal", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MenuPrincipal", u"Acerca de", None))
        self.actionExportar_como_PDF.setText(QCoreApplication.translate("MenuPrincipal", u"Exportar como PDF", None))
        self.actionManual_del_Usuario.setText(QCoreApplication.translate("MenuPrincipal", u"Manual del Usuario", None))
        self.LogoInterno.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MenuPrincipal", u"Filtros", None))
        self.lblFiltroProv.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None))
        self.filtroProveedor.setItemText(0, QCoreApplication.translate("MenuPrincipal", u"Todos", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MenuPrincipal", u"Inventario", None))
        ___qtablewidgetitem = self.tablaInventario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem1 = self.tablaInventario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MenuPrincipal", u"Nombre", None));
        ___qtablewidgetitem2 = self.tablaInventario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MenuPrincipal", u"Stock", None));
        ___qtablewidgetitem3 = self.tablaInventario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MenuPrincipal", u"S. minimo", None));
        ___qtablewidgetitem4 = self.tablaInventario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MenuPrincipal", u"Precio unitario", None));
        ___qtablewidgetitem5 = self.tablaInventario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None));
        ___qtablewidgetitem6 = self.tablaInventario.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MenuPrincipal", u"\u00daltimo ingreso", None));
        self.btnNuevoProducto.setText(QCoreApplication.translate("MenuPrincipal", u"  Nuevo", None))
        self.btnModProducto.setText(QCoreApplication.translate("MenuPrincipal", u"  Modificar", None))
        self.btnElimProducto.setText(QCoreApplication.translate("MenuPrincipal", u"  Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInventario), QCoreApplication.translate("MenuPrincipal", u"Inventario", None))
        self.groupBoxProveedor.setTitle(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None))
        self.tagProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None))
        self.nombreProveedor.setText("")
        self.telefonoProveedor.setText("")
        self.tagCUIL_6.setText(QCoreApplication.translate("MenuPrincipal", u"CUIL/CUIT ", None))
        self.tagTelefono_6.setText(QCoreApplication.translate("MenuPrincipal", u"Tel\u00e9fono", None))
        self.cuilProveedor.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MenuPrincipal", u"Detalle de ingreso", None))
        ___qtablewidgetitem7 = self.tablaIngresosDetalle.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem8 = self.tablaIngresosDetalle.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MenuPrincipal", u"Descripcion", None));
        ___qtablewidgetitem9 = self.tablaIngresosDetalle.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MenuPrincipal", u"Cantidad", None));
        self.btnNuevoIngreso.setText(QCoreApplication.translate("MenuPrincipal", u"  Nuevo", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ingresos", None))
        ___qtablewidgetitem10 = self.tablaIngresos.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem11 = self.tablaIngresos.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MenuPrincipal", u"Fecha", None));
        ___qtablewidgetitem12 = self.tablaIngresos.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MenuPrincipal", u"Ingresos", None))
        self.btnNuevoProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"  Nuevo", None))
        self.btnModProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"  Modificar", None))
        self.btnElimProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"  Eliminar", None))
        ___qtablewidgetitem13 = self.tablaProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem14 = self.tablaProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MenuPrincipal", u"Raz\u00f3n social", None));
        ___qtablewidgetitem15 = self.tablaProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MenuPrincipal", u"Tel\u00e9fono", None));
        ___qtablewidgetitem16 = self.tablaProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MenuPrincipal", u"Correo electr\u00f3nico", None));
        ___qtablewidgetitem17 = self.tablaProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MenuPrincipal", u"Direcci\u00f3n", None));
        ___qtablewidgetitem18 = self.tablaProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MenuPrincipal", u"Nota", None));
#if QT_CONFIG(whatsthis)
        self.tablaProveedores.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.tablaProveedores.setAccessibleName(QCoreApplication.translate("MenuPrincipal", u"Esta es una lista de ", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.tablaProveedores.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MenuPrincipal", u"Proveedores", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MenuPrincipal", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ayuda", None))
    # retranslateUi

