# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Historial.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import Recursos_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(671, 627)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -6, 671, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(84, 84, 84)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.escudoClub = QLabel(self.frame)
        self.escudoClub.setObjectName(u"escudoClub")
        self.escudoClub.setEnabled(True)
        self.escudoClub.setMaximumSize(QSize(100, 150))
        self.escudoClub.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(16)
        self.escudoClub.setFont(font)
        self.escudoClub.setStyleSheet(u"width:25px;\n"
"height:25px;")
        self.escudoClub.setPixmap(QPixmap(u":/Logos/Escudo-Club.png"))
        self.escudoClub.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.escudoClub)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

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

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 110, 681, 511))
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setTabBarAutoHide(True)
        self.tabHistorial = QWidget()
        self.tabHistorial.setObjectName(u"tabHistorial")
        self.verticalLayout_3 = QVBoxLayout(self.tabHistorial)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tablaInventario = QTableWidget(self.tabHistorial)
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
        if (self.tablaInventario.rowCount() < 19):
            self.tablaInventario.setRowCount(19)
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
        self.tablaInventario.setVerticalHeaderItem(15, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(16, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(17, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tablaInventario.setVerticalHeaderItem(18, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tablaInventario.setItem(0, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(0, 5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tablaInventario.setItem(1, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(1, 5, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tablaInventario.setItem(2, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(2, 5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tablaInventario.setItem(3, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(3, 5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tablaInventario.setItem(4, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(4, 5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 1, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tablaInventario.setItem(5, 2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(5, 5, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tablaInventario.setItem(6, 2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(6, 5, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 1, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tablaInventario.setItem(7, 2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(7, 5, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tablaInventario.setItem(8, 2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(8, 5, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tablaInventario.setItem(9, 2, __qtablewidgetitem81)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem82.setBackground(brush);
        self.tablaInventario.setItem(9, 3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 4, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(9, 5, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tablaInventario.setItem(10, 2, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 3, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(10, 5, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tablaInventario.setItem(11, 2, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 3, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 4, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(11, 5, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tablaInventario.setItem(12, 1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tablaInventario.setItem(12, 2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 4, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(12, 5, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 0, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tablaInventario.setItem(13, 1, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tablaInventario.setItem(13, 2, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 3, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 4, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(13, 5, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tablaInventario.setItem(14, 1, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tablaInventario.setItem(14, 2, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 3, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 4, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        __qtablewidgetitem114.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(14, 5, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        __qtablewidgetitem115.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(15, 0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tablaInventario.setItem(15, 1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tablaInventario.setItem(15, 2, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(15, 3, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(15, 4, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(15, 5, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(16, 0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tablaInventario.setItem(16, 1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tablaInventario.setItem(16, 2, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(16, 3, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(16, 4, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(16, 5, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(17, 0, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tablaInventario.setItem(17, 1, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tablaInventario.setItem(17, 2, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(17, 3, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(17, 4, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setTextAlignment(Qt.AlignCenter);
        self.tablaInventario.setItem(17, 5, __qtablewidgetitem132)
        self.tablaInventario.setObjectName(u"tablaInventario")
        self.tablaInventario.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tablaInventario.sizePolicy().hasHeightForWidth())
        self.tablaInventario.setSizePolicy(sizePolicy1)
        self.tablaInventario.setMaximumSize(QSize(657, 487))
        self.tablaInventario.setStyleSheet(u"background-color: white;\n"
"color:black;")
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
        self.tablaInventario.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tablaInventario.setWordWrap(True)
        self.tablaInventario.setRowCount(19)
        self.tablaInventario.setColumnCount(6)
        self.tablaInventario.horizontalHeader().setVisible(True)
        self.tablaInventario.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaInventario.horizontalHeader().setMinimumSectionSize(40)
        self.tablaInventario.horizontalHeader().setDefaultSectionSize(105)
        self.tablaInventario.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablaInventario.horizontalHeader().setStretchLastSection(False)
        self.tablaInventario.verticalHeader().setDefaultSectionSize(30)
        self.tablaInventario.verticalHeader().setHighlightSections(True)

        self.verticalLayout_3.addWidget(self.tablaInventario)

        self.tabWidget.addTab(self.tabHistorial, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.escudoClub.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/Logos/Escudo-Club - copia v2.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/Iconos/Lupa v2.png\"/></p></body></html>", None))
        self.barraBusqueda.setPlaceholderText(QCoreApplication.translate("Dialog", u"Buscar por nombre", None))
        ___qtablewidgetitem = self.tablaInventario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Fecha", None));
        ___qtablewidgetitem1 = self.tablaInventario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Responsable", None));
        ___qtablewidgetitem2 = self.tablaInventario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Producto", None));
        ___qtablewidgetitem3 = self.tablaInventario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Stock Anterior", None));
        ___qtablewidgetitem4 = self.tablaInventario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Stock Actual", None));
        ___qtablewidgetitem5 = self.tablaInventario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Proveedor", None));

        __sortingEnabled = self.tablaInventario.isSortingEnabled()
        self.tablaInventario.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tablaInventario.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"14/05/2018", None));
        ___qtablewidgetitem7 = self.tablaInventario.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Ma\u00f1ana", None));
        ___qtablewidgetitem8 = self.tablaInventario.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Cebolla", None));
        ___qtablewidgetitem9 = self.tablaInventario.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"15", None));
        ___qtablewidgetitem10 = self.tablaInventario.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"30", None));
        ___qtablewidgetitem11 = self.tablaInventario.item(0, 5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem12 = self.tablaInventario.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"25/09/2018", None));
        ___qtablewidgetitem13 = self.tablaInventario.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"Tarde", None));
        ___qtablewidgetitem14 = self.tablaInventario.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"Acelga", None));
        ___qtablewidgetitem15 = self.tablaInventario.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"06", None));
        ___qtablewidgetitem16 = self.tablaInventario.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qtablewidgetitem17 = self.tablaInventario.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem18 = self.tablaInventario.item(2, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"31/10/2018", None));
        ___qtablewidgetitem19 = self.tablaInventario.item(2, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"Tarde", None));
        ___qtablewidgetitem20 = self.tablaInventario.item(2, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"Papas", None));
        ___qtablewidgetitem21 = self.tablaInventario.item(2, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"150", None));
        ___qtablewidgetitem22 = self.tablaInventario.item(2, 4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"200", None));
        ___qtablewidgetitem23 = self.tablaInventario.item(2, 5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem24 = self.tablaInventario.item(3, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Dialog", u"02/12/2018", None));
        ___qtablewidgetitem25 = self.tablaInventario.item(3, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Dialog", u"Ma\u00f1ana", None));
        ___qtablewidgetitem26 = self.tablaInventario.item(3, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Dialog", u"Hamburguesas", None));
        ___qtablewidgetitem27 = self.tablaInventario.item(3, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Dialog", u"40", None));
        ___qtablewidgetitem28 = self.tablaInventario.item(3, 4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Dialog", u"30", None));
        ___qtablewidgetitem29 = self.tablaInventario.item(3, 5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem30 = self.tablaInventario.item(4, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Dialog", u"14/02/2019", None));
        ___qtablewidgetitem31 = self.tablaInventario.item(4, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Dialog", u"Ma\u00f1ana", None));
        ___qtablewidgetitem32 = self.tablaInventario.item(4, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Dialog", u"Queso", None));
        ___qtablewidgetitem33 = self.tablaInventario.item(4, 3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qtablewidgetitem34 = self.tablaInventario.item(4, 4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Dialog", u"50", None));
        ___qtablewidgetitem35 = self.tablaInventario.item(4, 5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Dialog", u"La Elisa S.A.", None));
        ___qtablewidgetitem36 = self.tablaInventario.item(5, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Dialog", u"11/03/2019", None));
        ___qtablewidgetitem37 = self.tablaInventario.item(5, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Dialog", u"Noche", None));
        ___qtablewidgetitem38 = self.tablaInventario.item(5, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Dialog", u"Pan (Com\u00fan)", None));
        ___qtablewidgetitem39 = self.tablaInventario.item(5, 3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Dialog", u"03", None));
        ___qtablewidgetitem40 = self.tablaInventario.item(5, 4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qtablewidgetitem41 = self.tablaInventario.item(5, 5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Dialog", u"Del Pueblo", None));
        ___qtablewidgetitem42 = self.tablaInventario.item(6, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Dialog", u"21/05/2019", None));
        ___qtablewidgetitem43 = self.tablaInventario.item(6, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Dialog", u"Tarde", None));
        ___qtablewidgetitem44 = self.tablaInventario.item(6, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Dialog", u"Pan (Hamburguesas)", None));
        ___qtablewidgetitem45 = self.tablaInventario.item(6, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Dialog", u"95", None));
        ___qtablewidgetitem46 = self.tablaInventario.item(6, 4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Dialog", u"100", None));
        ___qtablewidgetitem47 = self.tablaInventario.item(6, 5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Dialog", u"Del Pueblo", None));
        ___qtablewidgetitem48 = self.tablaInventario.item(7, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Dialog", u"09/08/2019", None));
        ___qtablewidgetitem49 = self.tablaInventario.item(7, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Dialog", u"Tarde", None));
        ___qtablewidgetitem50 = self.tablaInventario.item(7, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Dialog", u"Pan (Sandwich)", None));
        ___qtablewidgetitem51 = self.tablaInventario.item(7, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Dialog", u"50", None));
        ___qtablewidgetitem52 = self.tablaInventario.item(7, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Dialog", u"100", None));
        ___qtablewidgetitem53 = self.tablaInventario.item(7, 5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Dialog", u"Del Pueblo", None));
        ___qtablewidgetitem54 = self.tablaInventario.item(8, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Dialog", u"15/05/2020", None));
        ___qtablewidgetitem55 = self.tablaInventario.item(8, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Dialog", u"Noche", None));
        ___qtablewidgetitem56 = self.tablaInventario.item(8, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Dialog", u"Pan (Pebete)", None));
        ___qtablewidgetitem57 = self.tablaInventario.item(8, 3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Dialog", u"45", None));
        ___qtablewidgetitem58 = self.tablaInventario.item(8, 4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Dialog", u"100", None));
        ___qtablewidgetitem59 = self.tablaInventario.item(8, 5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Dialog", u"Del Pueblo", None));
        ___qtablewidgetitem60 = self.tablaInventario.item(9, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Dialog", u"19/08/2020", None));
        ___qtablewidgetitem61 = self.tablaInventario.item(9, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Dialog", u"Noche", None));
        ___qtablewidgetitem62 = self.tablaInventario.item(9, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Dialog", u"Hamburguesas", None));
        ___qtablewidgetitem63 = self.tablaInventario.item(9, 3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Dialog", u"90", None));
        ___qtablewidgetitem64 = self.tablaInventario.item(9, 4)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Dialog", u"100", None));
        ___qtablewidgetitem65 = self.tablaInventario.item(9, 5)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Dialog", u"San Jorge", None));
        ___qtablewidgetitem66 = self.tablaInventario.item(10, 0)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Dialog", u"28/12/2020", None));
        ___qtablewidgetitem67 = self.tablaInventario.item(10, 1)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Dialog", u"Ma\u00f1ana", None));
        ___qtablewidgetitem68 = self.tablaInventario.item(10, 2)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Dialog", u"Harina", None));
        ___qtablewidgetitem69 = self.tablaInventario.item(10, 3)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qtablewidgetitem70 = self.tablaInventario.item(10, 4)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("Dialog", u"15", None));
        ___qtablewidgetitem71 = self.tablaInventario.item(10, 5)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("Dialog", u"San Jorge", None));
        ___qtablewidgetitem72 = self.tablaInventario.item(11, 0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("Dialog", u"14/06/2021", None));
        ___qtablewidgetitem73 = self.tablaInventario.item(11, 1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("Dialog", u"Noche", None));
        ___qtablewidgetitem74 = self.tablaInventario.item(11, 2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("Dialog", u"Aceite", None));
        ___qtablewidgetitem75 = self.tablaInventario.item(11, 3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Dialog", u"10", None));
        ___qtablewidgetitem76 = self.tablaInventario.item(11, 4)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qtablewidgetitem77 = self.tablaInventario.item(11, 5)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("Dialog", u"San Jorge", None));
        ___qtablewidgetitem78 = self.tablaInventario.item(12, 0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("Dialog", u"24/09/2021", None));
        ___qtablewidgetitem79 = self.tablaInventario.item(12, 1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("Dialog", u"Tarde", None));
        ___qtablewidgetitem80 = self.tablaInventario.item(12, 2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("Dialog", u"Cebolla", None));
        ___qtablewidgetitem81 = self.tablaInventario.item(12, 3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("Dialog", u"20", None));
        ___qtablewidgetitem82 = self.tablaInventario.item(12, 4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("Dialog", u"30", None));
        ___qtablewidgetitem83 = self.tablaInventario.item(12, 5)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem84 = self.tablaInventario.item(13, 0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("Dialog", u"18/12/2021", None));
        ___qtablewidgetitem85 = self.tablaInventario.item(13, 1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("Dialog", u"Noche", None));
        ___qtablewidgetitem86 = self.tablaInventario.item(13, 2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("Dialog", u"Hamburguesas", None));
        ___qtablewidgetitem87 = self.tablaInventario.item(13, 3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("Dialog", u"15", None));
        ___qtablewidgetitem88 = self.tablaInventario.item(13, 4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("Dialog", u"40", None));
        ___qtablewidgetitem89 = self.tablaInventario.item(13, 5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem90 = self.tablaInventario.item(14, 0)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("Dialog", u"22/03/2022", None));
        ___qtablewidgetitem91 = self.tablaInventario.item(14, 1)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("Dialog", u"Ma\u00f1ana", None));
        ___qtablewidgetitem92 = self.tablaInventario.item(14, 2)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("Dialog", u"Harina", None));
        ___qtablewidgetitem93 = self.tablaInventario.item(14, 3)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("Dialog", u"02", None));
        ___qtablewidgetitem94 = self.tablaInventario.item(14, 4)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("Dialog", u"15", None));
        ___qtablewidgetitem95 = self.tablaInventario.item(14, 5)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("Dialog", u"San Jorge", None));
        ___qtablewidgetitem96 = self.tablaInventario.item(15, 0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("Dialog", u"19/04/2022", None));
        ___qtablewidgetitem97 = self.tablaInventario.item(15, 1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("Dialog", u"Noche", None));
        ___qtablewidgetitem98 = self.tablaInventario.item(15, 2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("Dialog", u"Papas", None));
        ___qtablewidgetitem99 = self.tablaInventario.item(15, 3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("Dialog", u"50", None));
        ___qtablewidgetitem100 = self.tablaInventario.item(15, 4)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("Dialog", u"200", None));
        ___qtablewidgetitem101 = self.tablaInventario.item(15, 5)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        ___qtablewidgetitem102 = self.tablaInventario.item(16, 0)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("Dialog", u"01/10/2022", None));
        ___qtablewidgetitem103 = self.tablaInventario.item(16, 1)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("Dialog", u"Ma\u00f1ana", None));
        ___qtablewidgetitem104 = self.tablaInventario.item(16, 2)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("Dialog", u"Pan (Sandwich)", None));
        ___qtablewidgetitem105 = self.tablaInventario.item(16, 3)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("Dialog", u"150", None));
        ___qtablewidgetitem106 = self.tablaInventario.item(16, 4)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("Dialog", u"100", None));
        ___qtablewidgetitem107 = self.tablaInventario.item(16, 5)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("Dialog", u"Del Pueblo", None));
        ___qtablewidgetitem108 = self.tablaInventario.item(17, 0)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("Dialog", u"16/12/2022", None));
        ___qtablewidgetitem109 = self.tablaInventario.item(17, 1)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("Dialog", u"Tarde", None));
        ___qtablewidgetitem110 = self.tablaInventario.item(17, 2)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("Dialog", u"Hamburguesas", None));
        ___qtablewidgetitem111 = self.tablaInventario.item(17, 3)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("Dialog", u"60", None));
        ___qtablewidgetitem112 = self.tablaInventario.item(17, 4)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("Dialog", u"40", None));
        ___qtablewidgetitem113 = self.tablaInventario.item(17, 5)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("Dialog", u"Nadur", None));
        self.tablaInventario.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHistorial), QCoreApplication.translate("Dialog", u"Historial", None))
    # retranslateUi

