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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 692)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"")
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.actionExportar_como_PDF = QAction(MainWindow)
        self.actionExportar_como_PDF.setObjectName(u"actionExportar_como_PDF")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
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

        self.horizontalLayout_2.addWidget(self.tituloTab)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.barraBusqueda = QLineEdit(self.frame)
        self.barraBusqueda.setObjectName(u"barraBusqueda")
        self.barraBusqueda.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.barraBusqueda.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.barraBusqueda)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
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
        if (self.tablaInventario.rowCount() < 15):
            self.tablaInventario.setRowCount(15)
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
        self.tablaInventario.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(0, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(0, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 1, __qtablewidgetitem29)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setBackground(brush);
        self.tablaInventario.setItem(1, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(1, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(1, 5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(2, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(2, 5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 6, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(3, 4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(3, 5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(4, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(4, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 6, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(5, 4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(5, 5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 6, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(6, 4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(6, 5, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 6, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(7, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(7, 5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 6, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(8, 4, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(8, 5, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 6, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 2, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(9, 4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(9, 5, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 6, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 2, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(10, 4, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(10, 5, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 6, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(11, 4, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(11, 5, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 6, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tablaInventario.setItem(12, 0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tablaInventario.setItem(12, 1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 2, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(12, 4, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(12, 5, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 6, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tablaInventario.setItem(13, 0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tablaInventario.setItem(13, 1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 2, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(13, 4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(13, 5, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 6, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tablaInventario.setItem(14, 0, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tablaInventario.setItem(14, 1, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 2, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(14, 4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(14, 5, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 6, __qtablewidgetitem111)
        self.tablaInventario.setObjectName(u"tablaInventario")
        self.tablaInventario.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaInventario.setAutoScroll(True)
        self.tablaInventario.horizontalHeader().setVisible(True)
        self.tablaInventario.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaInventario.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaInventario.horizontalHeader().setStretchLastSection(False)
        self.tablaInventario.verticalHeader().setHighlightSections(True)

        self.verticalLayout_3.addWidget(self.tablaInventario)

        self.layoutBtnInventario = QHBoxLayout()
        self.layoutBtnInventario.setObjectName(u"layoutBtnInventario")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_9)

        self.btnNuevoProducto = QPushButton(self.tabInventario)
        self.btnNuevoProducto.setObjectName(u"btnNuevoProducto")
        self.btnNuevoProducto.setMinimumSize(QSize(150, 0))

        self.layoutBtnInventario.addWidget(self.btnNuevoProducto)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_2)

        self.btnModProducto = QPushButton(self.tabInventario)
        self.btnModProducto.setObjectName(u"btnModProducto")
        self.btnModProducto.setMinimumSize(QSize(150, 0))

        self.layoutBtnInventario.addWidget(self.btnModProducto)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_4)

        self.btnElimProducto = QPushButton(self.tabInventario)
        self.btnElimProducto.setObjectName(u"btnElimProducto")
        self.btnElimProducto.setMinimumSize(QSize(150, 0))

        self.layoutBtnInventario.addWidget(self.btnElimProducto)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnInventario.addItem(self.horizontalSpacer_12)


        self.verticalLayout_3.addLayout(self.layoutBtnInventario)

        self.tabWidget.addTab(self.tabInventario, "")
        self.tabProveedores = QWidget()
        self.tabProveedores.setObjectName(u"tabProveedores")
        self.verticalLayout_4 = QVBoxLayout(self.tabProveedores)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tablaProveedores = QTableWidget(self.tabProveedores)
        if (self.tablaProveedores.columnCount() < 6):
            self.tablaProveedores.setColumnCount(6)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem117)
        if (self.tablaProveedores.rowCount() < 6):
            self.tablaProveedores.setRowCount(6)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(0, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(1, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(2, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(3, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(4, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(5, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 0, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 1, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(0, 2, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(0, 3, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(0, 4, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 5, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 2, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 3, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 4, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 5, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 1, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(2, 2, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(2, 3, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        __qtablewidgetitem140.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(2, 4, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 5, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 1, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(3, 2, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(3, 3, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(3, 4, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 5, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 0, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 1, __qtablewidgetitem149)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem150 = QTableWidgetItem()
        __qtablewidgetitem150.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem150.setBackground(brush1);
        self.tablaProveedores.setItem(4, 2, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        __qtablewidgetitem151.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(4, 3, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        __qtablewidgetitem152.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(4, 4, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 5, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 0, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 1, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 2, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 3, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 4, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 5, __qtablewidgetitem159)
        self.tablaProveedores.setObjectName(u"tablaProveedores")
        self.tablaProveedores.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaProveedores.setAutoScroll(True)
        self.tablaProveedores.horizontalHeader().setVisible(True)
        self.tablaProveedores.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaProveedores.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaProveedores.horizontalHeader().setStretchLastSection(False)
        self.tablaProveedores.verticalHeader().setHighlightSections(True)

        self.verticalLayout_4.addWidget(self.tablaProveedores)

        self.layoutBtnProveedores = QHBoxLayout()
        self.layoutBtnProveedores.setObjectName(u"layoutBtnProveedores")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_17)

        self.btnNuevoProveedor = QPushButton(self.tabProveedores)
        self.btnNuevoProveedor.setObjectName(u"btnNuevoProveedor")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNuevoProveedor.sizePolicy().hasHeightForWidth())
        self.btnNuevoProveedor.setSizePolicy(sizePolicy)
        self.btnNuevoProveedor.setMinimumSize(QSize(150, 0))

        self.layoutBtnProveedores.addWidget(self.btnNuevoProveedor)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_14)

        self.btnModProveedor = QPushButton(self.tabProveedores)
        self.btnModProveedor.setObjectName(u"btnModProveedor")
        self.btnModProveedor.setMinimumSize(QSize(150, 0))

        self.layoutBtnProveedores.addWidget(self.btnModProveedor)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_15)

        self.btnElimProveedor = QPushButton(self.tabProveedores)
        self.btnElimProveedor.setObjectName(u"btnElimProveedor")
        self.btnElimProveedor.setMinimumSize(QSize(150, 0))

        self.layoutBtnProveedores.addWidget(self.btnElimProveedor)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_18)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores.addItem(self.horizontalSpacer_16)


        self.verticalLayout_4.addLayout(self.layoutBtnProveedores)

        self.tabWidget.addTab(self.tabProveedores, "")
        self.tabIngresos = QWidget()
        self.tabIngresos.setObjectName(u"tabIngresos")
        self.verticalLayout_7 = QVBoxLayout(self.tabIngresos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.tablaProveedores_3 = QTableWidget(self.tabIngresos)
        if (self.tablaProveedores_3.columnCount() < 3):
            self.tablaProveedores_3.setColumnCount(3)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tablaProveedores_3.setHorizontalHeaderItem(0, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tablaProveedores_3.setHorizontalHeaderItem(1, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tablaProveedores_3.setHorizontalHeaderItem(2, __qtablewidgetitem162)
        if (self.tablaProveedores_3.rowCount() < 6):
            self.tablaProveedores_3.setRowCount(6)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tablaProveedores_3.setVerticalHeaderItem(0, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tablaProveedores_3.setVerticalHeaderItem(1, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tablaProveedores_3.setVerticalHeaderItem(2, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tablaProveedores_3.setVerticalHeaderItem(3, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tablaProveedores_3.setVerticalHeaderItem(4, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tablaProveedores_3.setVerticalHeaderItem(5, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(0, 0, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(0, 1, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(0, 2, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(1, 0, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(1, 1, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(1, 2, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(2, 0, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(2, 1, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(2, 2, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(3, 0, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(3, 1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(3, 2, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(4, 0, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(4, 1, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(4, 2, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(5, 0, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(5, 1, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tablaProveedores_3.setItem(5, 2, __qtablewidgetitem186)
        self.tablaProveedores_3.setObjectName(u"tablaProveedores_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tablaProveedores_3.sizePolicy().hasHeightForWidth())
        self.tablaProveedores_3.setSizePolicy(sizePolicy1)
        self.tablaProveedores_3.setMinimumSize(QSize(303, 0))
        self.tablaProveedores_3.setMaximumSize(QSize(303, 16777215))
        self.tablaProveedores_3.setBaseSize(QSize(0, 0))
        self.tablaProveedores_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tablaProveedores_3.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tablaProveedores_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tablaProveedores_3.setAutoScroll(True)
        self.tablaProveedores_3.setShowGrid(True)
        self.tablaProveedores_3.setCornerButtonEnabled(True)
        self.tablaProveedores_3.horizontalHeader().setVisible(True)
        self.tablaProveedores_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaProveedores_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaProveedores_3.horizontalHeader().setStretchLastSection(False)
        self.tablaProveedores_3.verticalHeader().setHighlightSections(True)

        self.horizontalLayout.addWidget(self.tablaProveedores_3)

        self.horizontalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)

        self.frame1 = QFrame(self.tabIngresos)
        self.frame1.setObjectName(u"frame1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy2)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_8 = QVBoxLayout(self.frame1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setContentsMargins(100, -1, 100, -1)
        self.label_2 = QLabel(self.frame1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.frame1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lineEdit = QLineEdit(self.frame1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.verticalLayout_8.addLayout(self.formLayout)

        self.tableWidget = QTableWidget(self.frame1)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem190)
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem210)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.frame1)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.layoutBtnProveedores_4 = QHBoxLayout()
        self.layoutBtnProveedores_4.setObjectName(u"layoutBtnProveedores_4")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_37)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_38)

        self.btnNuevoIngreso = QPushButton(self.tabIngresos)
        self.btnNuevoIngreso.setObjectName(u"btnNuevoIngreso")
        sizePolicy.setHeightForWidth(self.btnNuevoIngreso.sizePolicy().hasHeightForWidth())
        self.btnNuevoIngreso.setSizePolicy(sizePolicy)
        self.btnNuevoIngreso.setMinimumSize(QSize(150, 0))

        self.layoutBtnProveedores_4.addWidget(self.btnNuevoIngreso)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_39)

        self.btnModIngreso = QPushButton(self.tabIngresos)
        self.btnModIngreso.setObjectName(u"btnModIngreso")
        self.btnModIngreso.setMinimumSize(QSize(150, 0))

        self.layoutBtnProveedores_4.addWidget(self.btnModIngreso)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_40)

        self.btnHistorial = QPushButton(self.tabIngresos)
        self.btnHistorial.setObjectName(u"btnHistorial")
        self.btnHistorial.setMinimumSize(QSize(150, 0))

        self.layoutBtnProveedores_4.addWidget(self.btnHistorial)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_41)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layoutBtnProveedores_4.addItem(self.horizontalSpacer_42)


        self.verticalLayout_7.addLayout(self.layoutBtnProveedores_4)

        self.tabWidget.addTab(self.tabIngresos, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 20))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionExportar_como_PDF)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.actionExportar_como_PDF.setText(QCoreApplication.translate("MainWindow", u"Exportar como PDF", None))
        self.escudoClub.setText("")
        self.tituloTab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Club sarmiento</span></p></body></html>", None))
        self.barraBusqueda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por nombre", None))
        ___qtablewidgetitem = self.tablaInventario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tablaInventario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tablaInventario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem3 = self.tablaInventario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Stock minimo", None));
        ___qtablewidgetitem4 = self.tablaInventario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Precio unitario", None));
        ___qtablewidgetitem5 = self.tablaInventario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem6 = self.tablaInventario.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo ingreso", None));

        __sortingEnabled = self.tablaInventario.isSortingEnabled()
        self.tablaInventario.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tablaInventario.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"034", None));
        ___qtablewidgetitem8 = self.tablaInventario.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Papas", None));
        ___qtablewidgetitem9 = self.tablaInventario.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem10 = self.tablaInventario.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"$30,5", None));
        ___qtablewidgetitem11 = self.tablaInventario.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem12 = self.tablaInventario.item(0, 6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"10/08/2022", None));
        ___qtablewidgetitem13 = self.tablaInventario.item(1, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"158", None));
        ___qtablewidgetitem14 = self.tablaInventario.item(1, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Hamburguesas", None));
        ___qtablewidgetitem15 = self.tablaInventario.item(1, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"90", None));
        ___qtablewidgetitem16 = self.tablaInventario.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"$500", None));
        ___qtablewidgetitem17 = self.tablaInventario.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem18 = self.tablaInventario.item(1, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"20/11/2022", None));
        ___qtablewidgetitem19 = self.tablaInventario.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"008", None));
        ___qtablewidgetitem20 = self.tablaInventario.item(2, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Cebolla", None));
        ___qtablewidgetitem21 = self.tablaInventario.item(2, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem22 = self.tablaInventario.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"$75", None));
        ___qtablewidgetitem23 = self.tablaInventario.item(2, 5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem24 = self.tablaInventario.item(2, 6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem25 = self.tablaInventario.item(3, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"009", None));
        ___qtablewidgetitem26 = self.tablaInventario.item(3, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Acelga", None));
        ___qtablewidgetitem27 = self.tablaInventario.item(3, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"06", None));
        ___qtablewidgetitem28 = self.tablaInventario.item(3, 4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"$120", None));
        ___qtablewidgetitem29 = self.tablaInventario.item(3, 5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem30 = self.tablaInventario.item(3, 6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem31 = self.tablaInventario.item(4, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"256", None));
        ___qtablewidgetitem32 = self.tablaInventario.item(4, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Harina", None));
        ___qtablewidgetitem33 = self.tablaInventario.item(4, 2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem34 = self.tablaInventario.item(4, 4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"$600", None));
        ___qtablewidgetitem35 = self.tablaInventario.item(4, 5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem36 = self.tablaInventario.item(4, 6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem37 = self.tablaInventario.item(5, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem38 = self.tablaInventario.item(5, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Pan (Com\u00fan)", None));
        ___qtablewidgetitem39 = self.tablaInventario.item(5, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"03", None));
        ___qtablewidgetitem40 = self.tablaInventario.item(5, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"$300", None));
        ___qtablewidgetitem41 = self.tablaInventario.item(5, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem42 = self.tablaInventario.item(5, 6)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem43 = self.tablaInventario.item(6, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"101", None));
        ___qtablewidgetitem44 = self.tablaInventario.item(6, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Pan (Hamburguesas)", None));
        ___qtablewidgetitem45 = self.tablaInventario.item(6, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"95", None));
        ___qtablewidgetitem46 = self.tablaInventario.item(6, 4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"$400", None));
        ___qtablewidgetitem47 = self.tablaInventario.item(6, 5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem48 = self.tablaInventario.item(6, 6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem49 = self.tablaInventario.item(7, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"102", None));
        ___qtablewidgetitem50 = self.tablaInventario.item(7, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Pan (Sandwich)", None));
        ___qtablewidgetitem51 = self.tablaInventario.item(7, 2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem52 = self.tablaInventario.item(7, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"$300", None));
        ___qtablewidgetitem53 = self.tablaInventario.item(7, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem54 = self.tablaInventario.item(7, 6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem55 = self.tablaInventario.item(8, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"103", None));
        ___qtablewidgetitem56 = self.tablaInventario.item(8, 1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Pan (Pebete)", None));
        ___qtablewidgetitem57 = self.tablaInventario.item(8, 2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem58 = self.tablaInventario.item(8, 4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"$330", None));
        ___qtablewidgetitem59 = self.tablaInventario.item(8, 5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem60 = self.tablaInventario.item(8, 6)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem61 = self.tablaInventario.item(9, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"505", None));
        ___qtablewidgetitem62 = self.tablaInventario.item(9, 1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Coca-Cola", None));
        ___qtablewidgetitem63 = self.tablaInventario.item(9, 2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem64 = self.tablaInventario.item(9, 4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"$700", None));
        ___qtablewidgetitem65 = self.tablaInventario.item(9, 5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem66 = self.tablaInventario.item(9, 6)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem67 = self.tablaInventario.item(10, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"506", None));
        ___qtablewidgetitem68 = self.tablaInventario.item(10, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Sprite", None));
        ___qtablewidgetitem69 = self.tablaInventario.item(10, 2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem70 = self.tablaInventario.item(10, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"$500", None));
        ___qtablewidgetitem71 = self.tablaInventario.item(10, 5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem72 = self.tablaInventario.item(10, 6)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem73 = self.tablaInventario.item(11, 0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"520", None));
        ___qtablewidgetitem74 = self.tablaInventario.item(11, 1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Quilmes", None));
        ___qtablewidgetitem75 = self.tablaInventario.item(11, 2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem76 = self.tablaInventario.item(11, 4)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"$650", None));
        ___qtablewidgetitem77 = self.tablaInventario.item(11, 5)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem78 = self.tablaInventario.item(11, 6)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem79 = self.tablaInventario.item(12, 0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"048", None));
        ___qtablewidgetitem80 = self.tablaInventario.item(12, 1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Queso", None));
        ___qtablewidgetitem81 = self.tablaInventario.item(12, 2)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem82 = self.tablaInventario.item(12, 4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"$1000", None));
        ___qtablewidgetitem83 = self.tablaInventario.item(12, 5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"La Elisa S.A.", None));
        ___qtablewidgetitem84 = self.tablaInventario.item(12, 6)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem85 = self.tablaInventario.item(13, 0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"035", None));
        ___qtablewidgetitem86 = self.tablaInventario.item(13, 1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Tomate", None));
        ___qtablewidgetitem87 = self.tablaInventario.item(13, 2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem88 = self.tablaInventario.item(13, 4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"$80", None));
        ___qtablewidgetitem89 = self.tablaInventario.item(13, 5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem90 = self.tablaInventario.item(13, 6)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem91 = self.tablaInventario.item(14, 0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"257", None));
        ___qtablewidgetitem92 = self.tablaInventario.item(14, 1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Aceite", None));
        ___qtablewidgetitem93 = self.tablaInventario.item(14, 2)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem94 = self.tablaInventario.item(14, 4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"$700", None));
        ___qtablewidgetitem95 = self.tablaInventario.item(14, 5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem96 = self.tablaInventario.item(14, 6)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"10/10/2022", None));
        self.tablaInventario.setSortingEnabled(__sortingEnabled)

        self.btnNuevoProducto.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModProducto.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnElimProducto.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInventario), QCoreApplication.translate("MainWindow", u"Inventario", None))
        ___qtablewidgetitem97 = self.tablaProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem98 = self.tablaProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n social", None));
        ___qtablewidgetitem99 = self.tablaProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem100 = self.tablaProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Correo electr\u00f3nico", None));
        ___qtablewidgetitem101 = self.tablaProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem102 = self.tablaProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Nota", None));

        __sortingEnabled1 = self.tablaProveedores.isSortingEnabled()
        self.tablaProveedores.setSortingEnabled(False)
        ___qtablewidgetitem103 = self.tablaProveedores.item(0, 0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"034", None));
        ___qtablewidgetitem104 = self.tablaProveedores.item(0, 1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Juan Carlos", None));
        ___qtablewidgetitem105 = self.tablaProveedores.item(0, 2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"23423899", None));
        ___qtablewidgetitem106 = self.tablaProveedores.item(0, 3)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"juancarlos@mail.com", None));
        ___qtablewidgetitem107 = self.tablaProveedores.item(0, 4)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Estados Unidos 277", None));
        ___qtablewidgetitem108 = self.tablaProveedores.item(0, 5)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Bebidas", None));
        ___qtablewidgetitem109 = self.tablaProveedores.item(1, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"234", None));
        ___qtablewidgetitem110 = self.tablaProveedores.item(1, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"El Chancho Peludo", None));
        ___qtablewidgetitem111 = self.tablaProveedores.item(1, 2)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"      07324938", None));
        ___qtablewidgetitem112 = self.tablaProveedores.item(1, 3)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"elchancho@mail.com.ar", None));
        ___qtablewidgetitem113 = self.tablaProveedores.item(1, 4)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"      Alem 343", None));
        ___qtablewidgetitem114 = self.tablaProveedores.item(1, 5)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Carniceria", None));
        ___qtablewidgetitem115 = self.tablaProveedores.item(2, 0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"008", None));
        ___qtablewidgetitem116 = self.tablaProveedores.item(2, 1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Los Hermanos", None));
        ___qtablewidgetitem117 = self.tablaProveedores.item(2, 2)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"20431234", None));
        ___qtablewidgetitem118 = self.tablaProveedores.item(2, 3)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"loshermanos@email.com", None));
        ___qtablewidgetitem119 = self.tablaProveedores.item(2, 4)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Rivadavia 842", None));
        ___qtablewidgetitem120 = self.tablaProveedores.item(2, 5)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Verduleria", None));
        ___qtablewidgetitem121 = self.tablaProveedores.item(3, 0)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"009", None));
        ___qtablewidgetitem122 = self.tablaProveedores.item(3, 1)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Marcelo Rodriguez", None));
        ___qtablewidgetitem123 = self.tablaProveedores.item(3, 2)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"38243038", None));
        ___qtablewidgetitem124 = self.tablaProveedores.item(3, 3)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"mrodriguez@correo.com.ar", None));
        ___qtablewidgetitem125 = self.tablaProveedores.item(3, 4)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Finlandia 893", None));
        ___qtablewidgetitem126 = self.tablaProveedores.item(3, 5)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Papelera", None));
        ___qtablewidgetitem127 = self.tablaProveedores.item(4, 0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"158", None));
        ___qtablewidgetitem128 = self.tablaProveedores.item(4, 1)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"Matias Perez", None));
        ___qtablewidgetitem129 = self.tablaProveedores.item(4, 2)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"23901298", None));
        ___qtablewidgetitem130 = self.tablaProveedores.item(4, 3)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"matiasperes@mail.com.ar", None));
        ___qtablewidgetitem131 = self.tablaProveedores.item(4, 4)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"Alem 284", None));
        ___qtablewidgetitem132 = self.tablaProveedores.item(5, 0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"341", None));
        ___qtablewidgetitem133 = self.tablaProveedores.item(5, 1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"Mercedes Paredes", None));
        ___qtablewidgetitem134 = self.tablaProveedores.item(5, 2)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"      23432235", None));
        ___qtablewidgetitem135 = self.tablaProveedores.item(5, 4)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"   Finlandia 234", None));
        ___qtablewidgetitem136 = self.tablaProveedores.item(5, 5)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Limpieza", None));
        self.tablaProveedores.setSortingEnabled(__sortingEnabled1)

        self.btnNuevoProveedor.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModProveedor.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnElimProveedor.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProveedores), QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem137 = self.tablaProveedores_3.horizontalHeaderItem(0)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem138 = self.tablaProveedores_3.horizontalHeaderItem(1)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem139 = self.tablaProveedores_3.horizontalHeaderItem(2)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));

        __sortingEnabled2 = self.tablaProveedores_3.isSortingEnabled()
        self.tablaProveedores_3.setSortingEnabled(False)
        ___qtablewidgetitem140 = self.tablaProveedores_3.item(0, 0)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"034", None));
        ___qtablewidgetitem141 = self.tablaProveedores_3.item(0, 1)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None));
        ___qtablewidgetitem142 = self.tablaProveedores_3.item(0, 2)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"Juan Carlos", None));
        ___qtablewidgetitem143 = self.tablaProveedores_3.item(1, 0)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"234", None));
        ___qtablewidgetitem144 = self.tablaProveedores_3.item(1, 1)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None));
        ___qtablewidgetitem145 = self.tablaProveedores_3.item(1, 2)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"El chancho peludo", None));
        ___qtablewidgetitem146 = self.tablaProveedores_3.item(2, 0)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"008", None));
        ___qtablewidgetitem147 = self.tablaProveedores_3.item(2, 1)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None));
        ___qtablewidgetitem148 = self.tablaProveedores_3.item(2, 2)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"Los hermanos", None));
        ___qtablewidgetitem149 = self.tablaProveedores_3.item(3, 0)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"009", None));
        ___qtablewidgetitem150 = self.tablaProveedores_3.item(3, 1)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None));
        ___qtablewidgetitem151 = self.tablaProveedores_3.item(3, 2)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"Marcelo Rodriguez", None));
        ___qtablewidgetitem152 = self.tablaProveedores_3.item(4, 0)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"158", None));
        ___qtablewidgetitem153 = self.tablaProveedores_3.item(4, 1)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None));
        ___qtablewidgetitem154 = self.tablaProveedores_3.item(4, 2)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Matias perez", None));
        ___qtablewidgetitem155 = self.tablaProveedores_3.item(5, 0)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"341", None));
        ___qtablewidgetitem156 = self.tablaProveedores_3.item(5, 1)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None));
        ___qtablewidgetitem157 = self.tablaProveedores_3.item(5, 2)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"El chancho peludo", None));
        self.tablaProveedores_3.setSortingEnabled(__sortingEnabled2)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CUIL/CUIT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Juan Carlos", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"23423134", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"17/12/22", None))
        ___qtablewidgetitem158 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem159 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"Precio de compra", None));
        ___qtablewidgetitem160 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem161 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"Precio total", None));

        __sortingEnabled3 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem162 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"Coca coca cero 1L", None));
        ___qtablewidgetitem163 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"250", None));
        ___qtablewidgetitem164 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem165 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"Esprait 500ml", None));
        ___qtablewidgetitem166 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"250", None));
        ___qtablewidgetitem167 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"23", None));
        ___qtablewidgetitem168 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"Fantasiosa 500ml", None));
        ___qtablewidgetitem169 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"180", None));
        ___qtablewidgetitem170 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"542", None));
        ___qtablewidgetitem171 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"Monstruo 380ml", None));
        ___qtablewidgetitem172 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"340", None));
        ___qtablewidgetitem173 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem174 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"kilmes 2.5L", None));
        ___qtablewidgetitem175 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"500", None));
        ___qtablewidgetitem176 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"75", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled3)

        self.btnNuevoIngreso.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModIngreso.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnHistorial.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIngresos), QCoreApplication.translate("MainWindow", u"Ingresos", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

