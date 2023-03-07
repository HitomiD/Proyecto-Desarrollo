# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import windows.Recursos_rc
import crud

class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        if not MenuPrincipal.objectName():
            MenuPrincipal.setObjectName(u"MenuPrincipal")
        MenuPrincipal.resize(829, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MenuPrincipal.sizePolicy().hasHeightForWidth())
        MenuPrincipal.setSizePolicy(sizePolicy)
        MenuPrincipal.setStyleSheet(u"background-color: white;\n"
"")
        self.actionAcerca_de = QAction(MenuPrincipal)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.actionExportar_como_PDF = QAction(MenuPrincipal)
        self.actionExportar_como_PDF.setObjectName(u"actionExportar_como_PDF")
        self.centralwidget = QWidget(MenuPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 810, 100))
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(84, 84, 84)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.escudoClub = QLabel(self.frame)
        self.escudoClub.setObjectName(u"escudoClub")
        self.escudoClub.setMaximumSize(QSize(70, 80))
        self.escudoClub.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(16)
        self.escudoClub.setFont(font)
        self.escudoClub.setStyleSheet(u"")
        self.escudoClub.setPixmap(QPixmap(u":/Logos/Escudo-Club.png"))
        self.escudoClub.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.escudoClub)

        self.tituloTab = QLabel(self.frame)
        self.tituloTab.setObjectName(u"tituloTab")
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(False)
        self.tituloTab.setFont(font1)
        self.tituloTab.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.tituloTab)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.barraBusqueda = QLineEdit(self.frame)
        self.barraBusqueda.setObjectName(u"barraBusqueda")
        self.barraBusqueda.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.barraBusqueda.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.barraBusqueda)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 116, 811, 511))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabInventario = QWidget()
        self.tabInventario.setObjectName(u"tabInventario")
        self.verticalLayout_3 = QVBoxLayout(self.tabInventario)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tablaInventario = QTableWidget(self.tabInventario)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tablaInventario.sizePolicy().hasHeightForWidth())
        self.tablaInventario.setSizePolicy(sizePolicy1)
        self.tablaInventario.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaInventario.setFrameShape(QFrame.Panel)
        self.tablaInventario.setFrameShadow(QFrame.Plain)
        self.tablaInventario.setLineWidth(1)
        self.tablaInventario.setMidLineWidth(0)
        self.tablaInventario.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaInventario.setAutoScroll(False)
        self.tablaInventario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaInventario.setAlternatingRowColors(True)
        self.tablaInventario.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tablaInventario.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaInventario.setTextElideMode(Qt.ElideMiddle)
        self.tablaInventario.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tablaInventario.setRowCount(0)
        self.tablaInventario.setColumnCount(7)
        self.tablaInventario.horizontalHeader().setVisible(True)
        self.tablaInventario.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaInventario.horizontalHeader().setMinimumSectionSize(40)
        self.tablaInventario.horizontalHeader().setDefaultSectionSize(108)
        self.tablaInventario.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaInventario.horizontalHeader().setStretchLastSection(False)
        self.tablaInventario.verticalHeader().setDefaultSectionSize(30)
        self.tablaInventario.verticalHeader().setHighlightSections(True)

        #Setup tabla inventario
        
        crud.poblarQTableInventario(self.tablaInventario)
        
        #Fin setup tabla inventario

        self.verticalLayout_3.addWidget(self.tablaInventario)

        self.layoutBtnInventario = QHBoxLayout()
        self.layoutBtnInventario.setObjectName(u"layoutBtnInventario")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_9)

        self.btnNuevoProducto = QPushButton(self.tabInventario)
        self.btnNuevoProducto.setObjectName(u"btnNuevoProducto")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnNuevoProducto.sizePolicy().hasHeightForWidth())
        self.btnNuevoProducto.setSizePolicy(sizePolicy2)
        self.btnNuevoProducto.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.btnNuevoProducto.setFont(font2)
        self.btnNuevoProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoProducto.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnInventario.addWidget(self.btnNuevoProducto)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_2)

        self.btnModProducto = QPushButton(self.tabInventario)
        self.btnModProducto.setObjectName(u"btnModProducto")
        self.btnModProducto.setMinimumSize(QSize(150, 0))
        self.btnModProducto.setFont(font2)
        self.btnModProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModProducto.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnInventario.addWidget(self.btnModProducto)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_4)

        self.btnElimProducto = QPushButton(self.tabInventario)
        self.btnElimProducto.setObjectName(u"btnElimProducto")
        self.btnElimProducto.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setKerning(False)
        self.btnElimProducto.setFont(font3)
        self.btnElimProducto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimProducto.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnInventario.addWidget(self.btnElimProducto)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.layoutBtnInventario)

        self.tabWidget.addTab(self.tabInventario, "")
        self.tabProveedores = QWidget()
        self.tabProveedores.setObjectName(u"tabProveedores")
        self.verticalLayoutWidget = QWidget(self.tabProveedores)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 811, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tablaProveedores = QTableWidget(self.verticalLayoutWidget)
        if (self.tablaProveedores.columnCount() < 6):
            self.tablaProveedores.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tablaProveedores.setObjectName(u"tablaProveedores")
        self.tablaProveedores.setEnabled(False)
        self.tablaProveedores.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaProveedores.setAutoScroll(True)
        self.tablaProveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaProveedores.setAlternatingRowColors(True)
        self.tablaProveedores.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaProveedores.horizontalHeader().setVisible(True)
        self.tablaProveedores.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaProveedores.horizontalHeader().setMinimumSectionSize(0)
        self.tablaProveedores.horizontalHeader().setDefaultSectionSize(131)
        self.tablaProveedores.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaProveedores.horizontalHeader().setStretchLastSection(False)
        self.tablaProveedores.verticalHeader().setVisible(False)
        self.tablaProveedores.verticalHeader().setCascadingSectionResizes(False)
        self.tablaProveedores.verticalHeader().setMinimumSectionSize(25)
        self.tablaProveedores.verticalHeader().setDefaultSectionSize(30)
        self.tablaProveedores.verticalHeader().setHighlightSections(True)
        self.tablaProveedores.verticalHeader().setProperty("showSortIndicator", False)
        self.tablaProveedores.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tablaProveedores)

        #poblado tabla proveedores
        crud.poblarQTableProveedores(self.tablaProveedores)

        self.layoutBtnProveedores = QHBoxLayout()
        self.layoutBtnProveedores.setObjectName(u"layoutBtnProveedores")
        self.layoutBtnProveedores.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_17)

        self.btnNuevoProveedor = QPushButton(self.verticalLayoutWidget)
        self.btnNuevoProveedor.setObjectName(u"btnNuevoProveedor")
        sizePolicy2.setHeightForWidth(self.btnNuevoProveedor.sizePolicy().hasHeightForWidth())
        self.btnNuevoProveedor.setSizePolicy(sizePolicy2)
        self.btnNuevoProveedor.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setBold(True)
        self.btnNuevoProveedor.setFont(font4)
        self.btnNuevoProveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoProveedor.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30,30 ,30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnProveedores.addWidget(self.btnNuevoProveedor)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_14)

        self.btnModProveedor = QPushButton(self.verticalLayoutWidget)
        self.btnModProveedor.setObjectName(u"btnModProveedor")
        self.btnModProveedor.setMinimumSize(QSize(150, 0))
        self.btnModProveedor.setFont(font4)
        self.btnModProveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModProveedor.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnProveedores.addWidget(self.btnModProveedor)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_15)

        self.btnElimProveedor = QPushButton(self.verticalLayoutWidget)
        self.btnElimProveedor.setObjectName(u"btnElimProveedor")
        self.btnElimProveedor.setMinimumSize(QSize(150, 0))
        self.btnElimProveedor.setFont(font4)
        self.btnElimProveedor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimProveedor.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnProveedores.addWidget(self.btnElimProveedor)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_18)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_16)


        self.verticalLayout.addLayout(self.layoutBtnProveedores)

        self.tabWidget.addTab(self.tabProveedores, "")
        self.tabIngresos = QWidget()
        self.tabIngresos.setObjectName(u"tabIngresos")
        self.frame1 = QFrame(self.tabIngresos)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(350, 30, 441, 391))
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.groupBoxProveedor = QGroupBox(self.frame1)
        self.groupBoxProveedor.setObjectName(u"groupBoxProveedor")
        self.groupBoxProveedor.setEnabled(False)
        self.groupBoxProveedor.setGeometry(QRect(10, 10, 421, 151))
        self.groupBoxProveedor.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.groupBoxProveedor.setFlat(False)
        self.groupBoxProveedor.setCheckable(False)
        self.groupBoxProveedor.setChecked(False)
        self.gridLayout = QGridLayout(self.groupBoxProveedor)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tagProveedor = QLabel(self.groupBoxProveedor)
        self.tagProveedor.setObjectName(u"tagProveedor")

        self.gridLayout.addWidget(self.tagProveedor, 0, 0, 1, 1)

        self.telefonoProveedor = QLineEdit(self.groupBoxProveedor)
        self.telefonoProveedor.setObjectName(u"telefonoProveedor")

        self.gridLayout.addWidget(self.telefonoProveedor, 2, 1, 1, 1)

        self.cuilProveedor = QLineEdit(self.groupBoxProveedor)
        self.cuilProveedor.setObjectName(u"cuilProveedor")
        self.cuilProveedor.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")

        self.gridLayout.addWidget(self.cuilProveedor, 1, 1, 1, 1)

        self.nombreProveedor = QLineEdit(self.groupBoxProveedor)
        self.nombreProveedor.setObjectName(u"nombreProveedor")

        self.gridLayout.addWidget(self.nombreProveedor, 0, 1, 1, 1)

        self.tagCUIL = QLabel(self.groupBoxProveedor)
        self.tagCUIL.setObjectName(u"tagCUIL")

        self.gridLayout.addWidget(self.tagCUIL, 1, 0, 1, 1)

        self.tagTelefono = QLabel(self.groupBoxProveedor)
        self.tagTelefono.setObjectName(u"tagTelefono")

        self.gridLayout.addWidget(self.tagTelefono, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 160, 422, 221))
        self.tablaIngresosDetalle = QTableWidget(self.groupBox_2)
        if (self.tablaIngresosDetalle.columnCount() < 4):
            self.tablaIngresosDetalle.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.tablaIngresosDetalle.setObjectName(u"tablaIngresosDetalle")
        self.tablaIngresosDetalle.setEnabled(True)
        self.tablaIngresosDetalle.setGeometry(QRect(0, 18, 424, 201))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tablaIngresosDetalle.sizePolicy().hasHeightForWidth())
        self.tablaIngresosDetalle.setSizePolicy(sizePolicy3)
        self.tablaIngresosDetalle.setMinimumSize(QSize(424, 0))
        self.tablaIngresosDetalle.setMaximumSize(QSize(424, 16777215))
        self.tablaIngresosDetalle.setMouseTracking(False)
        self.tablaIngresosDetalle.setTabletTracking(False)
        self.tablaIngresosDetalle.setLayoutDirection(Qt.LeftToRight)
        self.tablaIngresosDetalle.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaIngresosDetalle.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaIngresosDetalle.setAlternatingRowColors(True)
        self.tablaIngresosDetalle.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablaIngresosDetalle.setWordWrap(False)
        self.tablaIngresosDetalle.setCornerButtonEnabled(False)
        self.tablaIngresosDetalle.verticalHeader().setVisible(False)
        self.widget = QWidget(self.tabIngresos)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 440, 790, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_21)

        self.btnNuevoIngreso = QPushButton(self.widget)
        self.btnNuevoIngreso.setObjectName(u"btnNuevoIngreso")
        sizePolicy2.setHeightForWidth(self.btnNuevoIngreso.sizePolicy().hasHeightForWidth())
        self.btnNuevoIngreso.setSizePolicy(sizePolicy2)
        self.btnNuevoIngreso.setMinimumSize(QSize(150, 0))
        self.btnNuevoIngreso.setFont(font4)
        self.btnNuevoIngreso.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoIngreso.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.horizontalLayout.addWidget(self.btnNuevoIngreso)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.btnModIngreso = QPushButton(self.widget)
        self.btnModIngreso.setObjectName(u"btnModIngreso")
        self.btnModIngreso.setMinimumSize(QSize(150, 0))
        self.btnModIngreso.setFont(font4)
        self.btnModIngreso.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModIngreso.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.horizontalLayout.addWidget(self.btnModIngreso)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_20)

        self.btnElimIngreso = QPushButton(self.widget)
        self.btnElimIngreso.setObjectName(u"btnElimIngreso")
        self.btnElimIngreso.setMinimumSize(QSize(150, 0))
        self.btnElimIngreso.setFont(font4)
        self.btnElimIngreso.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimIngreso.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.horizontalLayout.addWidget(self.btnElimIngreso)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_22)

        self.groupBox_3 = QGroupBox(self.tabIngresos)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 321, 411))
        self.tablaIngresos = QTableWidget(self.groupBox_3)
        if (self.tablaIngresos.columnCount() < 3):
            self.tablaIngresos.setColumnCount(3)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        self.tablaIngresos.setObjectName(u"tablaIngresos")
        self.tablaIngresos.setEnabled(True)
        self.tablaIngresos.setGeometry(QRect(0, 19, 321, 392))
        sizePolicy3.setHeightForWidth(self.tablaIngresos.sizePolicy().hasHeightForWidth())
        self.tablaIngresos.setSizePolicy(sizePolicy3)
        self.tablaIngresos.setMinimumSize(QSize(0, 0))
        self.tablaIngresos.setMaximumSize(QSize(16777215, 16777215))
        self.tablaIngresos.setBaseSize(QSize(0, 0))
        self.tablaIngresos.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tablaIngresos.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaIngresos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tablaIngresos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablaIngresos.setAutoScroll(False)
        self.tablaIngresos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaIngresos.setTabKeyNavigation(False)
        self.tablaIngresos.setAlternatingRowColors(True)
        self.tablaIngresos.setSelectionBehavior(QAbstractItemView.SelectRows)
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
        
        #poblado tabla ingresos
        crud.poblarQTableIngresos(self.tablaIngresos)

        
        self.label_4 = QLabel(self.tabIngresos)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 12, 111, 16))
        self.btnElimProveedor_2 = QPushButton(self.tabIngresos)
        self.btnElimProveedor_2.setObjectName(u"btnElimProveedor_2")
        self.btnElimProveedor_2.setGeometry(QRect(907, 440, 150, 24))
        self.btnElimProveedor_2.setMinimumSize(QSize(150, 0))
        self.btnElimProveedor_2.setStyleSheet(u"background-color: rgb(232, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.tabIngresos, "")
        MenuPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MenuPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        MenuPrincipal.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MenuPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 829, 20))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MenuPrincipal.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionExportar_como_PDF)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(MenuPrincipal)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MenuPrincipal)
    # setupUi

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QCoreApplication.translate("MenuPrincipal", u"MainWindow", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MenuPrincipal", u"Acerca de", None))
        self.actionExportar_como_PDF.setText(QCoreApplication.translate("MenuPrincipal", u"Exportar como PDF", None))
        self.escudoClub.setText("")
        self.tituloTab.setText(QCoreApplication.translate("MenuPrincipal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Club Sarmiento</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MenuPrincipal", u"<html><head/><body><p><img src=\":/Iconos/Lupa v2.png\"/></p></body></html>", None))
        self.barraBusqueda.setPlaceholderText(QCoreApplication.translate("MenuPrincipal", u"Buscar por nombre", None))
        ___qtablewidgetitem = self.tablaInventario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem1 = self.tablaInventario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MenuPrincipal", u"Nombre", None));
        ___qtablewidgetitem2 = self.tablaInventario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MenuPrincipal", u"Stock", None));
        ___qtablewidgetitem3 = self.tablaInventario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MenuPrincipal", u"Stock minimo", None));
        ___qtablewidgetitem4 = self.tablaInventario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MenuPrincipal", u"Precio unitario", None));
        ___qtablewidgetitem5 = self.tablaInventario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None));
        ___qtablewidgetitem6 = self.tablaInventario.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MenuPrincipal", u"\u00daltimo ingreso", None));
        self.btnNuevoProducto.setText(QCoreApplication.translate("MenuPrincipal", u"Nuevo", None))
        self.btnModProducto.setText(QCoreApplication.translate("MenuPrincipal", u"Modificar", None))
        self.btnElimProducto.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInventario), QCoreApplication.translate("MenuPrincipal", u"Inventario", None))
        ___qtablewidgetitem7 = self.tablaProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MenuPrincipal", u"CUIL/CUIT", None));
        ___qtablewidgetitem8 = self.tablaProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MenuPrincipal", u"Raz\u00f3n social", None));
        ___qtablewidgetitem9 = self.tablaProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MenuPrincipal", u"Tel\u00e9fono", None));
        ___qtablewidgetitem10 = self.tablaProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MenuPrincipal", u"Correo electr\u00f3nico", None));
        ___qtablewidgetitem11 = self.tablaProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MenuPrincipal", u"Direcci\u00f3n", None));
        ___qtablewidgetitem12 = self.tablaProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MenuPrincipal", u"Nota", None));
        self.btnNuevoProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"Nuevo", None))
        self.btnModProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"Modificar", None))
        self.btnElimProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProveedores), QCoreApplication.translate("MenuPrincipal", u"Proveedores", None))
        self.groupBoxProveedor.setTitle(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None))
        self.tagProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None))
        self.telefonoProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"2456980234", None))
        self.cuilProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"23423134", None))
        self.nombreProveedor.setText(QCoreApplication.translate("MenuPrincipal", u"Juan Carlos", None))
        self.tagCUIL.setText(QCoreApplication.translate("MenuPrincipal", u"CUIL/CUIT ", None))
        self.tagTelefono.setText(QCoreApplication.translate("MenuPrincipal", u"Tel\u00e9fono", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MenuPrincipal", u"Detalle de ingreso", None))
        ___qtablewidgetitem13 = self.tablaIngresosDetalle.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MenuPrincipal", u"Producto", None));
        ___qtablewidgetitem14 = self.tablaIngresosDetalle.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MenuPrincipal", u"Precio de compra", None));
        ___qtablewidgetitem15 = self.tablaIngresosDetalle.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MenuPrincipal", u"Cantidad", None));
        ___qtablewidgetitem16 = self.tablaIngresosDetalle.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MenuPrincipal", u"Precio total", None));
        self.btnNuevoIngreso.setText(QCoreApplication.translate("MenuPrincipal", u"Nuevo", None))
        self.btnModIngreso.setText(QCoreApplication.translate("MenuPrincipal", u"Modificar", None))
        self.btnElimIngreso.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ingresos", None))
        ___qtablewidgetitem17 = self.tablaIngresos.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem18 = self.tablaIngresos.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MenuPrincipal", u"Fecha", None));
        ___qtablewidgetitem19 = self.tablaIngresos.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None));
        self.label_4.setText(QCoreApplication.translate("MenuPrincipal", u"Detalle de ingreso:", None))
        self.btnElimProveedor_2.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIngresos), QCoreApplication.translate("MenuPrincipal", u"Ingresos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MenuPrincipal", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ayuda", None))
    # retranslateUi

