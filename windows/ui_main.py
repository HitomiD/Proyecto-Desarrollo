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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import Recursos_rc

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
        if (self.tablaInventario.rowCount() < 19):
            self.tablaInventario.setRowCount(19)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(16, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(17, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(18, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(0, 4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(0, 5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(1, 4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(1, 5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 6, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(2, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(2, 5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(3, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(3, 5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(4, 4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(4, 5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 6, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(5, 4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(5, 5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 6, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 0, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 1, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 2, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(6, 4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(6, 5, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 6, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(7, 4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(7, 5, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 6, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 2, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(8, 4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(8, 5, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 6, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 0, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 1, __qtablewidgetitem81)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem82.setBackground(brush);
        self.tablaInventario.setItem(9, 2, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(9, 4, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(9, 5, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 6, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(10, 4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(10, 5, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 6, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 2, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(11, 4, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(11, 5, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 6, __qtablewidgetitem97)
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
        self.tablaInventario.setTextElideMode(Qt.ElideMiddle)
        self.tablaInventario.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tablaInventario.setRowCount(19)
        self.tablaInventario.setColumnCount(7)
        self.tablaInventario.horizontalHeader().setVisible(True)
        self.tablaInventario.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaInventario.horizontalHeader().setMinimumSectionSize(40)
        self.tablaInventario.horizontalHeader().setDefaultSectionSize(108)
        self.tablaInventario.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaInventario.horizontalHeader().setStretchLastSection(False)
        self.tablaInventario.verticalHeader().setDefaultSectionSize(30)
        self.tablaInventario.verticalHeader().setHighlightSections(True)

        self.verticalLayout_3.addWidget(self.tablaInventario)

        self.layoutBtnInventario = QHBoxLayout()
        self.layoutBtnInventario.setObjectName(u"layoutBtnInventario")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_9)

        self.btnNuevoProveedor_3 = QPushButton(self.tabInventario)
        self.btnNuevoProveedor_3.setObjectName(u"btnNuevoProveedor_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnNuevoProveedor_3.sizePolicy().hasHeightForWidth())
        self.btnNuevoProveedor_3.setSizePolicy(sizePolicy2)
        self.btnNuevoProveedor_3.setMinimumSize(QSize(150, 0))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.btnNuevoProveedor_3.setFont(font2)
        self.btnNuevoProveedor_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoProveedor_3.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnInventario.addWidget(self.btnNuevoProveedor_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_2)

        self.btnModProveedor_3 = QPushButton(self.tabInventario)
        self.btnModProveedor_3.setObjectName(u"btnModProveedor_3")
        self.btnModProveedor_3.setMinimumSize(QSize(150, 0))
        self.btnModProveedor_3.setFont(font2)
        self.btnModProveedor_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModProveedor_3.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnInventario.addWidget(self.btnModProveedor_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_4)

        self.btnElimProveedor_4 = QPushButton(self.tabInventario)
        self.btnElimProveedor_4.setObjectName(u"btnElimProveedor_4")
        self.btnElimProveedor_4.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setKerning(False)
        self.btnElimProveedor_4.setFont(font3)
        self.btnElimProveedor_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimProveedor_4.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:5px;\n"
"height:25%;")

        self.layoutBtnInventario.addWidget(self.btnElimProveedor_4)

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
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem103)
        if (self.tablaProveedores.rowCount() < 14):
            self.tablaProveedores.setRowCount(14)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(2, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(3, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(4, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(5, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(6, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(7, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(8, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(9, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(10, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(11, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(12, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(13, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 0, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 1, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(0, 2, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(0, 3, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(0, 4, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 5, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 0, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 1, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(1, 2, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 3, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(1, 4, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 5, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(2, 2, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(2, 3, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(2, 4, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 5, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(3, 2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(3, 3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        __qtablewidgetitem140.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(3, 4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 1, __qtablewidgetitem143)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem144.setBackground(brush1);
        self.tablaProveedores.setItem(4, 2, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(4, 3, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(4, 4, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 5, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 0, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 1, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        __qtablewidgetitem150.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(5, 2, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 3, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        __qtablewidgetitem152.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(5, 4, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 5, __qtablewidgetitem153)
        self.tablaProveedores.setObjectName(u"tablaProveedores")
        self.tablaProveedores.setEnabled(False)
        self.tablaProveedores.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaProveedores.setAutoScroll(True)
        self.tablaProveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaProveedores.setAlternatingRowColors(True)
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
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(0, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(1, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(2, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tablaIngresosDetalle.setHorizontalHeaderItem(3, __qtablewidgetitem157)
        if (self.tablaIngresosDetalle.rowCount() < 7):
            self.tablaIngresosDetalle.setRowCount(7)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(0, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(1, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(2, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(3, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(4, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(5, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tablaIngresosDetalle.setVerticalHeaderItem(6, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(0, 0, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(0, 1, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(0, 2, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(0, 3, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(1, 0, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(1, 1, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(1, 2, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(2, 0, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(2, 1, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(2, 2, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(3, 0, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(3, 1, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(3, 2, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(4, 0, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(4, 1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(4, 2, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(5, 0, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(5, 1, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(5, 2, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(6, 0, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(6, 1, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(6, 2, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tablaIngresosDetalle.setItem(6, 3, __qtablewidgetitem187)
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

        self.btnNuevoProveedor_2 = QPushButton(self.widget)
        self.btnNuevoProveedor_2.setObjectName(u"btnNuevoProveedor_2")
        sizePolicy2.setHeightForWidth(self.btnNuevoProveedor_2.sizePolicy().hasHeightForWidth())
        self.btnNuevoProveedor_2.setSizePolicy(sizePolicy2)
        self.btnNuevoProveedor_2.setMinimumSize(QSize(150, 0))
        self.btnNuevoProveedor_2.setFont(font4)
        self.btnNuevoProveedor_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnNuevoProveedor_2.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.horizontalLayout.addWidget(self.btnNuevoProveedor_2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.btnModProveedor_2 = QPushButton(self.widget)
        self.btnModProveedor_2.setObjectName(u"btnModProveedor_2")
        self.btnModProveedor_2.setMinimumSize(QSize(150, 0))
        self.btnModProveedor_2.setFont(font4)
        self.btnModProveedor_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnModProveedor_2.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.horizontalLayout.addWidget(self.btnModProveedor_2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_20)

        self.btnElimProveedor_3 = QPushButton(self.widget)
        self.btnElimProveedor_3.setObjectName(u"btnElimProveedor_3")
        self.btnElimProveedor_3.setMinimumSize(QSize(150, 0))
        self.btnElimProveedor_3.setFont(font4)
        self.btnElimProveedor_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnElimProveedor_3.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);\n"
"border-radius:5px;\n"
"height:25%;")

        self.horizontalLayout.addWidget(self.btnElimProveedor_3)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_22)

        self.groupBox_3 = QGroupBox(self.tabIngresos)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 321, 411))
        self.tablaIngresos = QTableWidget(self.groupBox_3)
        if (self.tablaIngresos.columnCount() < 3):
            self.tablaIngresos.setColumnCount(3)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(0, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(1, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tablaIngresos.setHorizontalHeaderItem(2, __qtablewidgetitem190)
        if (self.tablaIngresos.rowCount() < 13):
            self.tablaIngresos.setRowCount(13)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(0, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(1, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(2, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(3, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(4, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(5, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(6, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(7, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(8, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(9, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(10, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(11, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tablaIngresos.setVerticalHeaderItem(12, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tablaIngresos.setItem(0, 0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tablaIngresos.setItem(0, 1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tablaIngresos.setItem(0, 2, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tablaIngresos.setItem(1, 0, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tablaIngresos.setItem(1, 1, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tablaIngresos.setItem(1, 2, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tablaIngresos.setItem(2, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tablaIngresos.setItem(2, 1, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tablaIngresos.setItem(2, 2, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.tablaIngresos.setItem(3, 0, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.tablaIngresos.setItem(3, 1, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tablaIngresos.setItem(3, 2, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        self.tablaIngresos.setItem(4, 0, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.tablaIngresos.setItem(4, 1, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tablaIngresos.setItem(4, 2, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        self.tablaIngresos.setItem(5, 0, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        self.tablaIngresos.setItem(5, 1, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tablaIngresos.setItem(5, 2, __qtablewidgetitem221)
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
        self.menubar.setGeometry(QRect(0, 0, 829, 22))
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

        self.tabWidget.setCurrentIndex(1)


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

        __sortingEnabled = self.tablaInventario.isSortingEnabled()
        self.tablaInventario.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tablaInventario.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MenuPrincipal", u"008", None));
        ___qtablewidgetitem8 = self.tablaInventario.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MenuPrincipal", u"Cebolla", None));
        ___qtablewidgetitem9 = self.tablaInventario.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MenuPrincipal", u"15", None));
        ___qtablewidgetitem10 = self.tablaInventario.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MenuPrincipal", u"$75", None));
        ___qtablewidgetitem11 = self.tablaInventario.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MenuPrincipal", u"Nadur", None));
        ___qtablewidgetitem12 = self.tablaInventario.item(0, 6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MenuPrincipal", u"29/11/2022", None));
        ___qtablewidgetitem13 = self.tablaInventario.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MenuPrincipal", u"009", None));
        ___qtablewidgetitem14 = self.tablaInventario.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MenuPrincipal", u"Acelga", None));
        ___qtablewidgetitem15 = self.tablaInventario.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MenuPrincipal", u"06", None));
        ___qtablewidgetitem16 = self.tablaInventario.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MenuPrincipal", u"$120", None));
        ___qtablewidgetitem17 = self.tablaInventario.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MenuPrincipal", u"Nadur", None));
        ___qtablewidgetitem18 = self.tablaInventario.item(1, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MenuPrincipal", u"29/11/2022", None));
        ___qtablewidgetitem19 = self.tablaInventario.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MenuPrincipal", u"034", None));
        ___qtablewidgetitem20 = self.tablaInventario.item(2, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MenuPrincipal", u"Papas", None));
        ___qtablewidgetitem21 = self.tablaInventario.item(2, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MenuPrincipal", u"150", None));
        ___qtablewidgetitem22 = self.tablaInventario.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MenuPrincipal", u"$30,5", None));
        ___qtablewidgetitem23 = self.tablaInventario.item(2, 5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MenuPrincipal", u"Nadur", None));
        ___qtablewidgetitem24 = self.tablaInventario.item(2, 6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MenuPrincipal", u"10/08/2022", None));
        ___qtablewidgetitem25 = self.tablaInventario.item(3, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MenuPrincipal", u"035", None));
        ___qtablewidgetitem26 = self.tablaInventario.item(3, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MenuPrincipal", u"Tomate", None));
        ___qtablewidgetitem27 = self.tablaInventario.item(3, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MenuPrincipal", u"40", None));
        ___qtablewidgetitem28 = self.tablaInventario.item(3, 4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MenuPrincipal", u"$80", None));
        ___qtablewidgetitem29 = self.tablaInventario.item(3, 5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MenuPrincipal", u"Nadur", None));
        ___qtablewidgetitem30 = self.tablaInventario.item(3, 6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MenuPrincipal", u"29/11/2022", None));
        ___qtablewidgetitem31 = self.tablaInventario.item(4, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MenuPrincipal", u"048", None));
        ___qtablewidgetitem32 = self.tablaInventario.item(4, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MenuPrincipal", u"Queso", None));
        ___qtablewidgetitem33 = self.tablaInventario.item(4, 2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MenuPrincipal", u"10", None));
        ___qtablewidgetitem34 = self.tablaInventario.item(4, 4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MenuPrincipal", u"$1000", None));
        ___qtablewidgetitem35 = self.tablaInventario.item(4, 5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MenuPrincipal", u"La Elisa S.A.", None));
        ___qtablewidgetitem36 = self.tablaInventario.item(4, 6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MenuPrincipal", u"29/11/2022", None));
        ___qtablewidgetitem37 = self.tablaInventario.item(5, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MenuPrincipal", u"100", None));
        ___qtablewidgetitem38 = self.tablaInventario.item(5, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MenuPrincipal", u"Pan (Com\u00fan)", None));
        ___qtablewidgetitem39 = self.tablaInventario.item(5, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MenuPrincipal", u"03", None));
        ___qtablewidgetitem40 = self.tablaInventario.item(5, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MenuPrincipal", u"$300", None));
        ___qtablewidgetitem41 = self.tablaInventario.item(5, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MenuPrincipal", u"Del Pueblo", None));
        ___qtablewidgetitem42 = self.tablaInventario.item(5, 6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MenuPrincipal", u"30/11/2022", None));
        ___qtablewidgetitem43 = self.tablaInventario.item(6, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MenuPrincipal", u"101", None));
        ___qtablewidgetitem44 = self.tablaInventario.item(6, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MenuPrincipal", u"Pan (Hamburguesas)", None));
        ___qtablewidgetitem45 = self.tablaInventario.item(6, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MenuPrincipal", u"95", None));
        ___qtablewidgetitem46 = self.tablaInventario.item(6, 4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MenuPrincipal", u"$400", None));
        ___qtablewidgetitem47 = self.tablaInventario.item(6, 5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MenuPrincipal", u"Del Pueblo", None));
        ___qtablewidgetitem48 = self.tablaInventario.item(6, 6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MenuPrincipal", u"30/11/2022", None));
        ___qtablewidgetitem49 = self.tablaInventario.item(7, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MenuPrincipal", u"102", None));
        ___qtablewidgetitem50 = self.tablaInventario.item(7, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MenuPrincipal", u"Pan (Sandwich)", None));
        ___qtablewidgetitem51 = self.tablaInventario.item(7, 2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MenuPrincipal", u"50", None));
        ___qtablewidgetitem52 = self.tablaInventario.item(7, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MenuPrincipal", u"$300", None));
        ___qtablewidgetitem53 = self.tablaInventario.item(7, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MenuPrincipal", u"Del Pueblo", None));
        ___qtablewidgetitem54 = self.tablaInventario.item(7, 6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MenuPrincipal", u"30/11/2022", None));
        ___qtablewidgetitem55 = self.tablaInventario.item(8, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MenuPrincipal", u"103", None));
        ___qtablewidgetitem56 = self.tablaInventario.item(8, 1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MenuPrincipal", u"Pan (Pebete)", None));
        ___qtablewidgetitem57 = self.tablaInventario.item(8, 2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MenuPrincipal", u"45", None));
        ___qtablewidgetitem58 = self.tablaInventario.item(8, 4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MenuPrincipal", u"$330", None));
        ___qtablewidgetitem59 = self.tablaInventario.item(8, 5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MenuPrincipal", u"Del Pueblo", None));
        ___qtablewidgetitem60 = self.tablaInventario.item(8, 6)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MenuPrincipal", u"30/11/2022", None));
        ___qtablewidgetitem61 = self.tablaInventario.item(9, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MenuPrincipal", u"158", None));
        ___qtablewidgetitem62 = self.tablaInventario.item(9, 1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MenuPrincipal", u"Hamburguesas", None));
        ___qtablewidgetitem63 = self.tablaInventario.item(9, 2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MenuPrincipal", u"90", None));
        ___qtablewidgetitem64 = self.tablaInventario.item(9, 4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MenuPrincipal", u"$500", None));
        ___qtablewidgetitem65 = self.tablaInventario.item(9, 5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MenuPrincipal", u"San Jorge", None));
        ___qtablewidgetitem66 = self.tablaInventario.item(9, 6)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MenuPrincipal", u"20/11/2022", None));
        ___qtablewidgetitem67 = self.tablaInventario.item(10, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MenuPrincipal", u"256", None));
        ___qtablewidgetitem68 = self.tablaInventario.item(10, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MenuPrincipal", u"Harina", None));
        ___qtablewidgetitem69 = self.tablaInventario.item(10, 2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MenuPrincipal", u"10", None));
        ___qtablewidgetitem70 = self.tablaInventario.item(10, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MenuPrincipal", u"$600", None));
        ___qtablewidgetitem71 = self.tablaInventario.item(10, 5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MenuPrincipal", u"San Jorge", None));
        ___qtablewidgetitem72 = self.tablaInventario.item(10, 6)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MenuPrincipal", u"23/11/2022", None));
        ___qtablewidgetitem73 = self.tablaInventario.item(11, 0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MenuPrincipal", u"257", None));
        ___qtablewidgetitem74 = self.tablaInventario.item(11, 1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MenuPrincipal", u"Aceite", None));
        ___qtablewidgetitem75 = self.tablaInventario.item(11, 2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MenuPrincipal", u"10", None));
        ___qtablewidgetitem76 = self.tablaInventario.item(11, 4)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MenuPrincipal", u"$700", None));
        ___qtablewidgetitem77 = self.tablaInventario.item(11, 5)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MenuPrincipal", u"San Jorge", None));
        ___qtablewidgetitem78 = self.tablaInventario.item(11, 6)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MenuPrincipal", u"10/10/2022", None));
        self.tablaInventario.setSortingEnabled(__sortingEnabled)

        self.btnNuevoProveedor_3.setText(QCoreApplication.translate("MenuPrincipal", u"Nuevo", None))
        self.btnModProveedor_3.setText(QCoreApplication.translate("MenuPrincipal", u"Modificar", None))
        self.btnElimProveedor_4.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInventario), QCoreApplication.translate("MenuPrincipal", u"Inventario", None))
        ___qtablewidgetitem79 = self.tablaProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem80 = self.tablaProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MenuPrincipal", u"Raz\u00f3n social", None));
        ___qtablewidgetitem81 = self.tablaProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MenuPrincipal", u"Tel\u00e9fono", None));
        ___qtablewidgetitem82 = self.tablaProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MenuPrincipal", u"Correo electr\u00f3nico", None));
        ___qtablewidgetitem83 = self.tablaProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MenuPrincipal", u"Direcci\u00f3n", None));
        ___qtablewidgetitem84 = self.tablaProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MenuPrincipal", u"Nota", None));

        __sortingEnabled1 = self.tablaProveedores.isSortingEnabled()
        self.tablaProveedores.setSortingEnabled(False)
        ___qtablewidgetitem85 = self.tablaProveedores.item(0, 0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MenuPrincipal", u"034", None));
        ___qtablewidgetitem86 = self.tablaProveedores.item(0, 1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MenuPrincipal", u"Juan Carlos", None));
        ___qtablewidgetitem87 = self.tablaProveedores.item(0, 2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MenuPrincipal", u"23423899", None));
        ___qtablewidgetitem88 = self.tablaProveedores.item(0, 3)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MenuPrincipal", u"juancarlos@mail.com", None));
        ___qtablewidgetitem89 = self.tablaProveedores.item(0, 4)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MenuPrincipal", u"Estados Unidos 277", None));
        ___qtablewidgetitem90 = self.tablaProveedores.item(0, 5)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MenuPrincipal", u"Bebidas", None));
        ___qtablewidgetitem91 = self.tablaProveedores.item(1, 0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MenuPrincipal", u"234", None));
        ___qtablewidgetitem92 = self.tablaProveedores.item(1, 1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MenuPrincipal", u"El Chancho Peludo", None));
        ___qtablewidgetitem93 = self.tablaProveedores.item(1, 2)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MenuPrincipal", u"07324938", None));
        ___qtablewidgetitem94 = self.tablaProveedores.item(1, 3)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MenuPrincipal", u"elchancho@mail.com.ar", None));
        ___qtablewidgetitem95 = self.tablaProveedores.item(1, 4)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MenuPrincipal", u"Alem 343", None));
        ___qtablewidgetitem96 = self.tablaProveedores.item(1, 5)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MenuPrincipal", u"Carniceria", None));
        ___qtablewidgetitem97 = self.tablaProveedores.item(2, 0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MenuPrincipal", u"008", None));
        ___qtablewidgetitem98 = self.tablaProveedores.item(2, 1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MenuPrincipal", u"Los Hermanos", None));
        ___qtablewidgetitem99 = self.tablaProveedores.item(2, 2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MenuPrincipal", u"20431234", None));
        ___qtablewidgetitem100 = self.tablaProveedores.item(2, 3)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MenuPrincipal", u"loshermanos@email.com", None));
        ___qtablewidgetitem101 = self.tablaProveedores.item(2, 4)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MenuPrincipal", u"Rivadavia 842", None));
        ___qtablewidgetitem102 = self.tablaProveedores.item(2, 5)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MenuPrincipal", u"Verduleria", None));
        ___qtablewidgetitem103 = self.tablaProveedores.item(3, 0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MenuPrincipal", u"009", None));
        ___qtablewidgetitem104 = self.tablaProveedores.item(3, 1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MenuPrincipal", u"Marcelo Rodriguez", None));
        ___qtablewidgetitem105 = self.tablaProveedores.item(3, 2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MenuPrincipal", u"38243038", None));
        ___qtablewidgetitem106 = self.tablaProveedores.item(3, 3)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MenuPrincipal", u"mrodriguez@correo.com.ar", None));
        ___qtablewidgetitem107 = self.tablaProveedores.item(3, 4)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MenuPrincipal", u"Finlandia 893", None));
        ___qtablewidgetitem108 = self.tablaProveedores.item(3, 5)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MenuPrincipal", u"Papelera", None));
        ___qtablewidgetitem109 = self.tablaProveedores.item(4, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MenuPrincipal", u"158", None));
        ___qtablewidgetitem110 = self.tablaProveedores.item(4, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MenuPrincipal", u"Matias Perez", None));
        ___qtablewidgetitem111 = self.tablaProveedores.item(4, 2)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MenuPrincipal", u"23901298", None));
        ___qtablewidgetitem112 = self.tablaProveedores.item(4, 3)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MenuPrincipal", u"matiasperes@mail.com.ar", None));
        ___qtablewidgetitem113 = self.tablaProveedores.item(4, 4)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MenuPrincipal", u"Alem 284", None));
        ___qtablewidgetitem114 = self.tablaProveedores.item(5, 0)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MenuPrincipal", u"341", None));
        ___qtablewidgetitem115 = self.tablaProveedores.item(5, 1)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MenuPrincipal", u"Mercedes Paredes", None));
        ___qtablewidgetitem116 = self.tablaProveedores.item(5, 2)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MenuPrincipal", u"23432235", None));
        ___qtablewidgetitem117 = self.tablaProveedores.item(5, 4)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MenuPrincipal", u"Finlandia 234", None));
        ___qtablewidgetitem118 = self.tablaProveedores.item(5, 5)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MenuPrincipal", u"Limpieza", None));
        self.tablaProveedores.setSortingEnabled(__sortingEnabled1)

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
        ___qtablewidgetitem119 = self.tablaIngresosDetalle.horizontalHeaderItem(0)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MenuPrincipal", u"Producto", None));
        ___qtablewidgetitem120 = self.tablaIngresosDetalle.horizontalHeaderItem(1)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MenuPrincipal", u"Precio de compra", None));
        ___qtablewidgetitem121 = self.tablaIngresosDetalle.horizontalHeaderItem(2)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MenuPrincipal", u"Cantidad", None));
        ___qtablewidgetitem122 = self.tablaIngresosDetalle.horizontalHeaderItem(3)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MenuPrincipal", u"Precio total", None));

        __sortingEnabled2 = self.tablaIngresosDetalle.isSortingEnabled()
        self.tablaIngresosDetalle.setSortingEnabled(False)
        ___qtablewidgetitem123 = self.tablaIngresosDetalle.item(0, 0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MenuPrincipal", u"Coca coca cero 1L", None));
        ___qtablewidgetitem124 = self.tablaIngresosDetalle.item(0, 1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MenuPrincipal", u"250", None));
        ___qtablewidgetitem125 = self.tablaIngresosDetalle.item(0, 2)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MenuPrincipal", u"45", None));
        ___qtablewidgetitem126 = self.tablaIngresosDetalle.item(1, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MenuPrincipal", u"Esprait 500ml", None));
        ___qtablewidgetitem127 = self.tablaIngresosDetalle.item(1, 1)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MenuPrincipal", u"250", None));
        ___qtablewidgetitem128 = self.tablaIngresosDetalle.item(1, 2)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MenuPrincipal", u"23", None));
        ___qtablewidgetitem129 = self.tablaIngresosDetalle.item(2, 0)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MenuPrincipal", u"Fantasiosa 500ml", None));
        ___qtablewidgetitem130 = self.tablaIngresosDetalle.item(2, 1)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MenuPrincipal", u"180", None));
        ___qtablewidgetitem131 = self.tablaIngresosDetalle.item(2, 2)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MenuPrincipal", u"542", None));
        ___qtablewidgetitem132 = self.tablaIngresosDetalle.item(3, 0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MenuPrincipal", u"Monstruo 380ml", None));
        ___qtablewidgetitem133 = self.tablaIngresosDetalle.item(3, 1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MenuPrincipal", u"340", None));
        ___qtablewidgetitem134 = self.tablaIngresosDetalle.item(3, 2)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MenuPrincipal", u"2", None));
        ___qtablewidgetitem135 = self.tablaIngresosDetalle.item(4, 0)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MenuPrincipal", u"kilmes 2.5 Ltr.", None));
        ___qtablewidgetitem136 = self.tablaIngresosDetalle.item(4, 1)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MenuPrincipal", u"500", None));
        ___qtablewidgetitem137 = self.tablaIngresosDetalle.item(4, 2)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MenuPrincipal", u"75", None));
        ___qtablewidgetitem138 = self.tablaIngresosDetalle.item(5, 0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MenuPrincipal", u"Amstel 1 Ltr.", None));
        ___qtablewidgetitem139 = self.tablaIngresosDetalle.item(5, 1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MenuPrincipal", u"300", None));
        ___qtablewidgetitem140 = self.tablaIngresosDetalle.item(5, 2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MenuPrincipal", u"50", None));
        ___qtablewidgetitem141 = self.tablaIngresosDetalle.item(6, 0)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MenuPrincipal", u"Jack Daniels 750ml.", None));
        ___qtablewidgetitem142 = self.tablaIngresosDetalle.item(6, 1)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MenuPrincipal", u"1500", None));
        ___qtablewidgetitem143 = self.tablaIngresosDetalle.item(6, 2)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MenuPrincipal", u"5", None));
        self.tablaIngresosDetalle.setSortingEnabled(__sortingEnabled2)

        self.btnNuevoProveedor_2.setText(QCoreApplication.translate("MenuPrincipal", u"Nuevo", None))
        self.btnModProveedor_2.setText(QCoreApplication.translate("MenuPrincipal", u"Modificar", None))
        self.btnElimProveedor_3.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ingresos", None))
        ___qtablewidgetitem144 = self.tablaIngresos.horizontalHeaderItem(0)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MenuPrincipal", u"ID", None));
        ___qtablewidgetitem145 = self.tablaIngresos.horizontalHeaderItem(1)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MenuPrincipal", u"Fecha", None));
        ___qtablewidgetitem146 = self.tablaIngresos.horizontalHeaderItem(2)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MenuPrincipal", u"Proveedor", None));

        __sortingEnabled3 = self.tablaIngresos.isSortingEnabled()
        self.tablaIngresos.setSortingEnabled(False)
        ___qtablewidgetitem147 = self.tablaIngresos.item(0, 0)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MenuPrincipal", u"034", None));
        ___qtablewidgetitem148 = self.tablaIngresos.item(0, 1)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MenuPrincipal", u"17/12/22", None));
        ___qtablewidgetitem149 = self.tablaIngresos.item(0, 2)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MenuPrincipal", u"Juan Carlos", None));
        ___qtablewidgetitem150 = self.tablaIngresos.item(1, 0)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MenuPrincipal", u"234", None));
        ___qtablewidgetitem151 = self.tablaIngresos.item(1, 1)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MenuPrincipal", u"17/12/22", None));
        ___qtablewidgetitem152 = self.tablaIngresos.item(1, 2)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MenuPrincipal", u"El chancho peludo", None));
        ___qtablewidgetitem153 = self.tablaIngresos.item(2, 0)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MenuPrincipal", u"008", None));
        ___qtablewidgetitem154 = self.tablaIngresos.item(2, 1)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MenuPrincipal", u"17/12/22", None));
        ___qtablewidgetitem155 = self.tablaIngresos.item(2, 2)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MenuPrincipal", u"Los hermanos", None));
        ___qtablewidgetitem156 = self.tablaIngresos.item(3, 0)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MenuPrincipal", u"009", None));
        ___qtablewidgetitem157 = self.tablaIngresos.item(3, 1)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MenuPrincipal", u"17/12/22", None));
        ___qtablewidgetitem158 = self.tablaIngresos.item(3, 2)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MenuPrincipal", u"Marcelo Rodriguez", None));
        ___qtablewidgetitem159 = self.tablaIngresos.item(4, 0)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MenuPrincipal", u"158", None));
        ___qtablewidgetitem160 = self.tablaIngresos.item(4, 1)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MenuPrincipal", u"17/12/22", None));
        ___qtablewidgetitem161 = self.tablaIngresos.item(4, 2)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MenuPrincipal", u"Matias perez", None));
        ___qtablewidgetitem162 = self.tablaIngresos.item(5, 0)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MenuPrincipal", u"341", None));
        ___qtablewidgetitem163 = self.tablaIngresos.item(5, 1)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MenuPrincipal", u"17/12/22", None));
        ___qtablewidgetitem164 = self.tablaIngresos.item(5, 2)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MenuPrincipal", u"El chancho peludo", None));
        self.tablaIngresos.setSortingEnabled(__sortingEnabled3)

        self.label_4.setText(QCoreApplication.translate("MenuPrincipal", u"Detalle de ingreso:", None))
        self.btnElimProveedor_2.setText(QCoreApplication.translate("MenuPrincipal", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIngresos), QCoreApplication.translate("MenuPrincipal", u"Ingresos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MenuPrincipal", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MenuPrincipal", u"Ayuda", None))
    # retranslateUi

