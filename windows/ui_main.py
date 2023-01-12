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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
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
        if (self.tablaInventario.columnCount() < 6):
            self.tablaInventario.setColumnCount(6)
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
        if (self.tablaInventario.rowCount() < 15):
            self.tablaInventario.setRowCount(15)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(0, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(0, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 1, __qtablewidgetitem28)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setBackground(brush);
        self.tablaInventario.setItem(1, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(1, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(1, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(2, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(2, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(3, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(3, 4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(4, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(4, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(5, 3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(5, 4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(6, 3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(6, 4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 5, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(7, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(7, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(8, 3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(8, 4, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 5, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(9, 3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(9, 4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 5, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(10, 3, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(10, 4, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 5, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(11, 3, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(11, 4, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 5, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tablaInventario.setItem(12, 0, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tablaInventario.setItem(12, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 2, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(12, 3, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(12, 4, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 5, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tablaInventario.setItem(13, 0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tablaInventario.setItem(13, 1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(13, 3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(13, 4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 5, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tablaInventario.setItem(14, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tablaInventario.setItem(14, 1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(14, 3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaInventario.setItem(14, 4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 5, __qtablewidgetitem110)
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
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tablaProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem116)
        if (self.tablaProveedores.rowCount() < 6):
            self.tablaProveedores.setRowCount(6)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(4, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tablaProveedores.setVerticalHeaderItem(5, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 0, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 1, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(0, 2, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(0, 3, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(0, 4, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tablaProveedores.setItem(0, 5, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 1, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 2, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 3, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 4, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tablaProveedores.setItem(1, 5, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 0, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 1, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        __qtablewidgetitem137.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(2, 2, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(2, 3, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(2, 4, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tablaProveedores.setItem(2, 5, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 0, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 1, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(3, 2, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(3, 3, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(3, 4, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tablaProveedores.setItem(3, 5, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 0, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 1, __qtablewidgetitem148)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem149 = QTableWidgetItem()
        __qtablewidgetitem149.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem149.setBackground(brush1);
        self.tablaProveedores.setItem(4, 2, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        __qtablewidgetitem150.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tablaProveedores.setItem(4, 3, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        __qtablewidgetitem151.setTextAlignment(Qt.AlignCenter);
        self.tablaProveedores.setItem(4, 4, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tablaProveedores.setItem(4, 5, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 1, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 2, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 3, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 4, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tablaProveedores.setItem(5, 5, __qtablewidgetitem158)
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

        self.tabWidget.setCurrentIndex(0)


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
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio unitario", None));
        ___qtablewidgetitem4 = self.tablaInventario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem5 = self.tablaInventario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo ingreso", None));

        __sortingEnabled = self.tablaInventario.isSortingEnabled()
        self.tablaInventario.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tablaInventario.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"034", None));
        ___qtablewidgetitem7 = self.tablaInventario.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Papas", None));
        ___qtablewidgetitem8 = self.tablaInventario.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem9 = self.tablaInventario.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"$30,5", None));
        ___qtablewidgetitem10 = self.tablaInventario.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem11 = self.tablaInventario.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10/08/2022", None));
        ___qtablewidgetitem12 = self.tablaInventario.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"158", None));
        ___qtablewidgetitem13 = self.tablaInventario.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Hamburguesas", None));
        ___qtablewidgetitem14 = self.tablaInventario.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"90", None));
        ___qtablewidgetitem15 = self.tablaInventario.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"$500", None));
        ___qtablewidgetitem16 = self.tablaInventario.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem17 = self.tablaInventario.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"20/11/2022", None));
        ___qtablewidgetitem18 = self.tablaInventario.item(2, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"008", None));
        ___qtablewidgetitem19 = self.tablaInventario.item(2, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Cebolla", None));
        ___qtablewidgetitem20 = self.tablaInventario.item(2, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem21 = self.tablaInventario.item(2, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"$75", None));
        ___qtablewidgetitem22 = self.tablaInventario.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem23 = self.tablaInventario.item(2, 5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem24 = self.tablaInventario.item(3, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"009", None));
        ___qtablewidgetitem25 = self.tablaInventario.item(3, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Acelga", None));
        ___qtablewidgetitem26 = self.tablaInventario.item(3, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"06", None));
        ___qtablewidgetitem27 = self.tablaInventario.item(3, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"$120", None));
        ___qtablewidgetitem28 = self.tablaInventario.item(3, 4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem29 = self.tablaInventario.item(3, 5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem30 = self.tablaInventario.item(4, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"256", None));
        ___qtablewidgetitem31 = self.tablaInventario.item(4, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Harina", None));
        ___qtablewidgetitem32 = self.tablaInventario.item(4, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem33 = self.tablaInventario.item(4, 3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"$600", None));
        ___qtablewidgetitem34 = self.tablaInventario.item(4, 4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem35 = self.tablaInventario.item(4, 5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem36 = self.tablaInventario.item(5, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem37 = self.tablaInventario.item(5, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Pan (Com\u00fan)", None));
        ___qtablewidgetitem38 = self.tablaInventario.item(5, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"03", None));
        ___qtablewidgetitem39 = self.tablaInventario.item(5, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"$300", None));
        ___qtablewidgetitem40 = self.tablaInventario.item(5, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem41 = self.tablaInventario.item(5, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem42 = self.tablaInventario.item(6, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"101", None));
        ___qtablewidgetitem43 = self.tablaInventario.item(6, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Pan (Hamburguesas)", None));
        ___qtablewidgetitem44 = self.tablaInventario.item(6, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"95", None));
        ___qtablewidgetitem45 = self.tablaInventario.item(6, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"$400", None));
        ___qtablewidgetitem46 = self.tablaInventario.item(6, 4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem47 = self.tablaInventario.item(6, 5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem48 = self.tablaInventario.item(7, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"102", None));
        ___qtablewidgetitem49 = self.tablaInventario.item(7, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Pan (Sandwich)", None));
        ___qtablewidgetitem50 = self.tablaInventario.item(7, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem51 = self.tablaInventario.item(7, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"$300", None));
        ___qtablewidgetitem52 = self.tablaInventario.item(7, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem53 = self.tablaInventario.item(7, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem54 = self.tablaInventario.item(8, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"103", None));
        ___qtablewidgetitem55 = self.tablaInventario.item(8, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Pan (Pebete)", None));
        ___qtablewidgetitem56 = self.tablaInventario.item(8, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem57 = self.tablaInventario.item(8, 3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"$330", None));
        ___qtablewidgetitem58 = self.tablaInventario.item(8, 4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem59 = self.tablaInventario.item(8, 5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem60 = self.tablaInventario.item(9, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"505", None));
        ___qtablewidgetitem61 = self.tablaInventario.item(9, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Coca-Cola", None));
        ___qtablewidgetitem62 = self.tablaInventario.item(9, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem63 = self.tablaInventario.item(9, 3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"$700", None));
        ___qtablewidgetitem64 = self.tablaInventario.item(9, 4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem65 = self.tablaInventario.item(9, 5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem66 = self.tablaInventario.item(10, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"506", None));
        ___qtablewidgetitem67 = self.tablaInventario.item(10, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Sprite", None));
        ___qtablewidgetitem68 = self.tablaInventario.item(10, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem69 = self.tablaInventario.item(10, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"$500", None));
        ___qtablewidgetitem70 = self.tablaInventario.item(10, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem71 = self.tablaInventario.item(10, 5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem72 = self.tablaInventario.item(11, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"520", None));
        ___qtablewidgetitem73 = self.tablaInventario.item(11, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Quilmes", None));
        ___qtablewidgetitem74 = self.tablaInventario.item(11, 2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem75 = self.tablaInventario.item(11, 3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"$650", None));
        ___qtablewidgetitem76 = self.tablaInventario.item(11, 4)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem77 = self.tablaInventario.item(11, 5)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem78 = self.tablaInventario.item(12, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"048", None));
        ___qtablewidgetitem79 = self.tablaInventario.item(12, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Queso", None));
        ___qtablewidgetitem80 = self.tablaInventario.item(12, 2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem81 = self.tablaInventario.item(12, 3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"$1000", None));
        ___qtablewidgetitem82 = self.tablaInventario.item(12, 4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"La Elisa S.A.", None));
        ___qtablewidgetitem83 = self.tablaInventario.item(12, 5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem84 = self.tablaInventario.item(13, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"035", None));
        ___qtablewidgetitem85 = self.tablaInventario.item(13, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Tomate", None));
        ___qtablewidgetitem86 = self.tablaInventario.item(13, 2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem87 = self.tablaInventario.item(13, 3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"$80", None));
        ___qtablewidgetitem88 = self.tablaInventario.item(13, 4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem89 = self.tablaInventario.item(13, 5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem90 = self.tablaInventario.item(14, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"257", None));
        ___qtablewidgetitem91 = self.tablaInventario.item(14, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Aceite", None));
        ___qtablewidgetitem92 = self.tablaInventario.item(14, 2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem93 = self.tablaInventario.item(14, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"$700", None));
        ___qtablewidgetitem94 = self.tablaInventario.item(14, 4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem95 = self.tablaInventario.item(14, 5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"10/10/2022", None));
        self.tablaInventario.setSortingEnabled(__sortingEnabled)

        self.btnNuevoProducto.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModProducto.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnElimProducto.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInventario), QCoreApplication.translate("MainWindow", u"Inventario", None))
        ___qtablewidgetitem96 = self.tablaProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem97 = self.tablaProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n social", None));
        ___qtablewidgetitem98 = self.tablaProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem99 = self.tablaProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Correo electr\u00f3nico", None));
        ___qtablewidgetitem100 = self.tablaProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem101 = self.tablaProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Nota", None));

        __sortingEnabled1 = self.tablaProveedores.isSortingEnabled()
        self.tablaProveedores.setSortingEnabled(False)
        ___qtablewidgetitem102 = self.tablaProveedores.item(0, 0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"034", None));
        ___qtablewidgetitem103 = self.tablaProveedores.item(0, 1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Juan Carlos", None));
        ___qtablewidgetitem104 = self.tablaProveedores.item(0, 2)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"23423899", None));
        ___qtablewidgetitem105 = self.tablaProveedores.item(0, 3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"juancarlos@mail.com", None));
        ___qtablewidgetitem106 = self.tablaProveedores.item(0, 4)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Estados Unidos 277", None));
        ___qtablewidgetitem107 = self.tablaProveedores.item(0, 5)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Bebidas", None));
        ___qtablewidgetitem108 = self.tablaProveedores.item(1, 0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"234", None));
        ___qtablewidgetitem109 = self.tablaProveedores.item(1, 1)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"El Chancho Peludo", None));
        ___qtablewidgetitem110 = self.tablaProveedores.item(1, 2)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"      07324938", None));
        ___qtablewidgetitem111 = self.tablaProveedores.item(1, 3)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"elchancho@mail.com.ar", None));
        ___qtablewidgetitem112 = self.tablaProveedores.item(1, 4)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"      Alem 343", None));
        ___qtablewidgetitem113 = self.tablaProveedores.item(1, 5)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Carniceria", None));
        ___qtablewidgetitem114 = self.tablaProveedores.item(2, 0)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"008", None));
        ___qtablewidgetitem115 = self.tablaProveedores.item(2, 1)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Los Hermanos", None));
        ___qtablewidgetitem116 = self.tablaProveedores.item(2, 2)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"20431234", None));
        ___qtablewidgetitem117 = self.tablaProveedores.item(2, 3)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"loshermanos@email.com", None));
        ___qtablewidgetitem118 = self.tablaProveedores.item(2, 4)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Rivadavia 842", None));
        ___qtablewidgetitem119 = self.tablaProveedores.item(2, 5)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Verduleria", None));
        ___qtablewidgetitem120 = self.tablaProveedores.item(3, 0)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"009", None));
        ___qtablewidgetitem121 = self.tablaProveedores.item(3, 1)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Marcelo Rodriguez", None));
        ___qtablewidgetitem122 = self.tablaProveedores.item(3, 2)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"38243038", None));
        ___qtablewidgetitem123 = self.tablaProveedores.item(3, 3)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"mrodriguez@correo.com.ar", None));
        ___qtablewidgetitem124 = self.tablaProveedores.item(3, 4)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Finlandia 893", None));
        ___qtablewidgetitem125 = self.tablaProveedores.item(3, 5)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Papelera", None));
        ___qtablewidgetitem126 = self.tablaProveedores.item(4, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"158", None));
        ___qtablewidgetitem127 = self.tablaProveedores.item(4, 1)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"Matias Perez", None));
        ___qtablewidgetitem128 = self.tablaProveedores.item(4, 2)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"23901298", None));
        ___qtablewidgetitem129 = self.tablaProveedores.item(4, 3)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"matiasperes@mail.com.ar", None));
        ___qtablewidgetitem130 = self.tablaProveedores.item(4, 4)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Alem 284", None));
        ___qtablewidgetitem131 = self.tablaProveedores.item(5, 0)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"341", None));
        ___qtablewidgetitem132 = self.tablaProveedores.item(5, 1)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"Mercedes Paredes", None));
        ___qtablewidgetitem133 = self.tablaProveedores.item(5, 2)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"      23432235", None));
        ___qtablewidgetitem134 = self.tablaProveedores.item(5, 4)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"   Finlandia 234", None));
        ___qtablewidgetitem135 = self.tablaProveedores.item(5, 5)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"Limpieza", None));
        self.tablaProveedores.setSortingEnabled(__sortingEnabled1)

        self.btnNuevoProveedor.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModProveedor.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnElimProveedor.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProveedores), QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

