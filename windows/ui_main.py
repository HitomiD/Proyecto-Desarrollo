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
    QMenuBar, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 692)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"")
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 80))
        self.label_2.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/Logos/Escudo-Club.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"image: url(:/Lupa/Lupa.png);\n"
"filter:invert(100%);\n"
"color:white;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

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

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"font: 30pt \"Roboto\";\n"
"color: rgb(148, 148, 148);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 15):
            self.tableWidget.setRowCount(15)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem28)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setBackground(brush);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(1, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(1, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(2, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(2, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(3, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(3, 4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(4, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(4, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 5, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(5, 3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(5, 4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 5, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(6, 3, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(6, 4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 5, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(7, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(7, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(8, 2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(8, 3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(8, 4, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(8, 5, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(9, 2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(9, 3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(9, 4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(9, 5, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget.setItem(10, 0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(10, 2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(10, 3, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(10, 4, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(10, 5, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget.setItem(11, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget.setItem(11, 1, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(11, 2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(11, 3, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(11, 4, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(11, 5, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget.setItem(12, 0, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget.setItem(12, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(12, 2, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(12, 3, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(12, 4, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(12, 5, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget.setItem(13, 0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget.setItem(13, 1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(13, 2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(13, 3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(13, 4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(13, 5, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget.setItem(14, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget.setItem(14, 1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(14, 2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(14, 3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget.setItem(14, 4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(14, 5, __qtablewidgetitem110)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: white;\n"
"color:black;")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)

        self.verticalLayout.addWidget(self.tableWidget)


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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Club sarmiento</span></p></body></html>", None))
        self.label_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por nombre", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700; color:#545454;\">Menu Principal</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio unitario", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo ingreso", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"034", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Papas", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"$30,5", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"10/08/2022", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"158", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Hamburguesas", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"90", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"$500", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"20/11/2022", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"008", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Cebolla", None));
        ___qtablewidgetitem20 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem21 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"$75", None));
        ___qtablewidgetitem22 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem23 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem24 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"009", None));
        ___qtablewidgetitem25 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Acelga", None));
        ___qtablewidgetitem26 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"06", None));
        ___qtablewidgetitem27 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"$120", None));
        ___qtablewidgetitem28 = self.tableWidget.item(3, 4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem29 = self.tableWidget.item(3, 5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem30 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"256", None));
        ___qtablewidgetitem31 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Harina", None));
        ___qtablewidgetitem32 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem33 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"$600", None));
        ___qtablewidgetitem34 = self.tableWidget.item(4, 4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem35 = self.tableWidget.item(4, 5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem36 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"100", None));
        ___qtablewidgetitem37 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Pan (Com\u00fan)", None));
        ___qtablewidgetitem38 = self.tableWidget.item(5, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"03", None));
        ___qtablewidgetitem39 = self.tableWidget.item(5, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"$300", None));
        ___qtablewidgetitem40 = self.tableWidget.item(5, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem41 = self.tableWidget.item(5, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem42 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"101", None));
        ___qtablewidgetitem43 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Pan (Hamburguesas)", None));
        ___qtablewidgetitem44 = self.tableWidget.item(6, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"95", None));
        ___qtablewidgetitem45 = self.tableWidget.item(6, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"$400", None));
        ___qtablewidgetitem46 = self.tableWidget.item(6, 4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem47 = self.tableWidget.item(6, 5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem48 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"102", None));
        ___qtablewidgetitem49 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Pan (Sandwich)", None));
        ___qtablewidgetitem50 = self.tableWidget.item(7, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem51 = self.tableWidget.item(7, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"$300", None));
        ___qtablewidgetitem52 = self.tableWidget.item(7, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem53 = self.tableWidget.item(7, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem54 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"103", None));
        ___qtablewidgetitem55 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Pan (Pebete)", None));
        ___qtablewidgetitem56 = self.tableWidget.item(8, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"45", None));
        ___qtablewidgetitem57 = self.tableWidget.item(8, 3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"$330", None));
        ___qtablewidgetitem58 = self.tableWidget.item(8, 4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Del Pueblo", None));
        ___qtablewidgetitem59 = self.tableWidget.item(8, 5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"30/11/2022", None));
        ___qtablewidgetitem60 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"505", None));
        ___qtablewidgetitem61 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Coca-Cola", None));
        ___qtablewidgetitem62 = self.tableWidget.item(9, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem63 = self.tableWidget.item(9, 3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"$700", None));
        ___qtablewidgetitem64 = self.tableWidget.item(9, 4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem65 = self.tableWidget.item(9, 5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem66 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"506", None));
        ___qtablewidgetitem67 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Sprite", None));
        ___qtablewidgetitem68 = self.tableWidget.item(10, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem69 = self.tableWidget.item(10, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"$500", None));
        ___qtablewidgetitem70 = self.tableWidget.item(10, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem71 = self.tableWidget.item(10, 5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem72 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"520", None));
        ___qtablewidgetitem73 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Quilmes", None));
        ___qtablewidgetitem74 = self.tableWidget.item(11, 2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"26", None));
        ___qtablewidgetitem75 = self.tableWidget.item(11, 3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"$650", None));
        ___qtablewidgetitem76 = self.tableWidget.item(11, 4)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem77 = self.tableWidget.item(11, 5)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"23/11/2022", None));
        ___qtablewidgetitem78 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"048", None));
        ___qtablewidgetitem79 = self.tableWidget.item(12, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Queso", None));
        ___qtablewidgetitem80 = self.tableWidget.item(12, 2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem81 = self.tableWidget.item(12, 3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"$1000", None));
        ___qtablewidgetitem82 = self.tableWidget.item(12, 4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"La Elisa S.A.", None));
        ___qtablewidgetitem83 = self.tableWidget.item(12, 5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem84 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"035", None));
        ___qtablewidgetitem85 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Tomate", None));
        ___qtablewidgetitem86 = self.tableWidget.item(13, 2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem87 = self.tableWidget.item(13, 3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"$80", None));
        ___qtablewidgetitem88 = self.tableWidget.item(13, 4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Nadur", None));
        ___qtablewidgetitem89 = self.tableWidget.item(13, 5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"29/11/2022", None));
        ___qtablewidgetitem90 = self.tableWidget.item(14, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"257", None));
        ___qtablewidgetitem91 = self.tableWidget.item(14, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Aceite", None));
        ___qtablewidgetitem92 = self.tableWidget.item(14, 2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem93 = self.tableWidget.item(14, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"$700", None));
        ___qtablewidgetitem94 = self.tableWidget.item(14, 4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"San Jorge", None));
        ___qtablewidgetitem95 = self.tableWidget.item(14, 5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"10/10/2022", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

