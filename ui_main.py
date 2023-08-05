# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(869, 641)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_3 = QVBoxLayout(self.page_home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(214, 214, 214);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_home)
        self.page_meta = QWidget()
        self.page_meta.setObjectName(u"page_meta")
        self.page_meta.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.page_meta)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.page_meta)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setSizeIncrement(QSize(0, 0))
        self.frame_2.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(6)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(25, 15, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.table_metas_inseridas = QTableWidget(self.frame_2)
        if (self.table_metas_inseridas.columnCount() < 4):
            self.table_metas_inseridas.setColumnCount(4)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.table_metas_inseridas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.table_metas_inseridas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.table_metas_inseridas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.table_metas_inseridas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_metas_inseridas.setObjectName(u"table_metas_inseridas")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table_metas_inseridas.sizePolicy().hasHeightForWidth())
        self.table_metas_inseridas.setSizePolicy(sizePolicy2)
        self.table_metas_inseridas.setMinimumSize(QSize(0, 0))
        self.table_metas_inseridas.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(184, 184, 184);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"     border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(184, 184, 184);\n"
"	padding: 3px;\n"
"}\n"
"")
        self.table_metas_inseridas.horizontalHeader().setDefaultSectionSize(130)
        self.table_metas_inseridas.verticalHeader().setDefaultSectionSize(42)

        self.gridLayout_3.addWidget(self.table_metas_inseridas, 2, 0, 1, 3)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1)

        self.caminho_excel = QLineEdit(self.frame_2)
        self.caminho_excel.setObjectName(u"caminho_excel")
        self.caminho_excel.setMinimumSize(QSize(0, 30))
        self.caminho_excel.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border-radius:5px;")

        self.gridLayout_3.addWidget(self.caminho_excel, 6, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 0))
        self.label_9.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.label_9, 6, 1, 1, 1)

        self.btn_exportar = QPushButton(self.frame_2)
        self.btn_exportar.setObjectName(u"btn_exportar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_exportar.sizePolicy().hasHeightForWidth())
        self.btn_exportar.setSizePolicy(sizePolicy3)
        self.btn_exportar.setMinimumSize(QSize(0, 30))
        self.btn_exportar.setMaximumSize(QSize(200, 16777215))
        self.btn_exportar.setFont(font1)
        self.btn_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 127);\n"
" 	 border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(19,10,41);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-top: 3px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/adicionar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exportar.setIcon(icon)
        self.btn_exportar.setIconSize(QSize(30, 25))
        self.btn_exportar.setAutoRepeatDelay(300)

        self.gridLayout_3.addWidget(self.btn_exportar, 6, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.page_meta)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 450))
        self.frame_4.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"\n"
"QComboBox {\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit {\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setStyleSheet(u"border-radius:10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(15, 9, 9, 9)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy5)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(375, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_8.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_10, 1, 3, 5, 1)

        self.horizontalSpacer = QSpacerItem(100, 0, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 6, 3, 1, 1)

        self.erros = QTextEdit(self.frame_12)
        self.erros.setObjectName(u"erros")
        self.erros.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius:10px;")

        self.gridLayout_2.addWidget(self.erros, 4, 0, 1, 2)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.btn_limpar = QPushButton(self.frame_12)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setMaximumSize(QSize(100, 60))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.btn_limpar.setFont(font3)
        self.btn_limpar.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 127);\n"
" 	 border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(19,10,41);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-top: 3px;\n"
"}")

        self.gridLayout_2.addWidget(self.btn_limpar, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_12, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_meta)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border-radius: 10px;\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 13, 9, 12)
        self.filtro_Empresa = QComboBox(self.frame_7)
        self.filtro_Empresa.addItem("")
        self.filtro_Empresa.addItem("")
        self.filtro_Empresa.addItem("")
        self.filtro_Empresa.addItem("")
        self.filtro_Empresa.setObjectName(u"filtro_Empresa")
        self.filtro_Empresa.setMinimumSize(QSize(0, 30))
        self.filtro_Empresa.setFont(font3)
        self.filtro_Empresa.setStyleSheet(u"QComboBox {\n"
"border-radius: 5px;\n"
"background-color: rgb(19,10,41);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_5.addWidget(self.filtro_Empresa)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_5.addWidget(self.label_14)

        self.filtro_unidade = QComboBox(self.frame_7)
        self.filtro_unidade.addItem("")
        self.filtro_unidade.setObjectName(u"filtro_unidade")
        self.filtro_unidade.setMinimumSize(QSize(0, 30))
        self.filtro_unidade.setFont(font3)
        self.filtro_unidade.setStyleSheet(u"QComboBox {\n"
"border-radius: 5px;\n"
"background-color: rgb(19,10,41);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_5.addWidget(self.filtro_unidade)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.filtro_mes = QComboBox(self.frame_7)
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.addItem("")
        self.filtro_mes.setObjectName(u"filtro_mes")
        self.filtro_mes.setMinimumSize(QSize(0, 30))
        self.filtro_mes.setMaximumSize(QSize(16777215, 16777215))
        self.filtro_mes.setFont(font3)
        self.filtro_mes.setStyleSheet(u"QComboBox {\n"
"border-radius: 5px;\n"
"background-color: rgb(19,10,41);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_5.addWidget(self.filtro_mes)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.filtro_ano = QComboBox(self.frame_7)
        self.filtro_ano.addItem("")
        self.filtro_ano.addItem("")
        self.filtro_ano.addItem("")
        self.filtro_ano.addItem("")
        self.filtro_ano.addItem("")
        self.filtro_ano.addItem("")
        self.filtro_ano.setObjectName(u"filtro_ano")
        self.filtro_ano.setMinimumSize(QSize(0, 30))
        self.filtro_ano.setMaximumSize(QSize(16777215, 16777215))
        self.filtro_ano.setFont(font3)
        self.filtro_ano.setStyleSheet(u"QComboBox {\n"
"border-radius: 5px;\n"
"background-color: rgb(19,10,41);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_5.addWidget(self.filtro_ano)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)

        self.btn_filtro = QPushButton(self.frame_7)
        self.btn_filtro.setObjectName(u"btn_filtro")
        sizePolicy3.setHeightForWidth(self.btn_filtro.sizePolicy().hasHeightForWidth())
        self.btn_filtro.setSizePolicy(sizePolicy3)
        self.btn_filtro.setMinimumSize(QSize(0, 30))
        self.btn_filtro.setMaximumSize(QSize(200, 16777215))
        self.btn_filtro.setFont(font3)
        self.btn_filtro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filtro.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 127);\n"
" 	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(51, 27, 113);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-top: 3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/filtrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_filtro.setIcon(icon1)
        self.btn_filtro.setIconSize(QSize(30, 25))
        self.btn_filtro.setAutoRepeatDelay(300)

        self.verticalLayout_5.addWidget(self.btn_filtro)

        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 40))

        self.verticalLayout_5.addWidget(self.label_16)

        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.total = QLineEdit(self.frame_7)
        self.total.setObjectName(u"total")
        self.total.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setPointSize(11)
        self.total.setFont(font4)
        self.total.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border- radius: 10px;\n"
"")

        self.verticalLayout_5.addWidget(self.total)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.btn_excel = QPushButton(self.frame_7)
        self.btn_excel.setObjectName(u"btn_excel")
        sizePolicy3.setHeightForWidth(self.btn_excel.sizePolicy().hasHeightForWidth())
        self.btn_excel.setSizePolicy(sizePolicy3)
        self.btn_excel.setMinimumSize(QSize(0, 30))
        self.btn_excel.setMaximumSize(QSize(200, 16777215))
        self.btn_excel.setFont(font3)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 127);\n"
" 	 border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	color: rgb(255, 255, 255);	\n"
"	background-color: rgb(34, 102, 50);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-top: 3px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/icons8-exportar-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excel.setIcon(icon2)
        self.btn_excel.setIconSize(QSize(30, 25))
        self.btn_excel.setAutoRepeatDelay(300)

        self.verticalLayout_5.addWidget(self.btn_excel)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 25))

        self.verticalLayout_5.addWidget(self.label_17)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.table_filtro = QTableView(self.frame)
        self.table_filtro.setObjectName(u"table_filtro")

        self.horizontalLayout_4.addWidget(self.table_filtro)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.gridLayout_6.addWidget(self.frame_3, 0, 1, 1, 1)

        self.menu_bar = QFrame(self.centralwidget)
        self.menu_bar.setObjectName(u"menu_bar")
        sizePolicy4.setHeightForWidth(self.menu_bar.sizePolicy().hasHeightForWidth())
        self.menu_bar.setSizePolicy(sizePolicy4)
        self.menu_bar.setMinimumSize(QSize(60, 0))
        self.menu_bar.setMaximumSize(QSize(0, 16777215))
        self.menu_bar.setStyleSheet(u"QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 9px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 127);\n"
" 	 border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.menu_bar.setFrameShape(QFrame.NoFrame)
        self.menu_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.menu_bar)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(16777215, 70))
        self.logo.setStyleSheet(u"")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 9, 0, 0)
        self.btn_logo = QPushButton(self.logo)
        self.btn_logo.setObjectName(u"btn_logo")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_logo.sizePolicy().hasHeightForWidth())
        self.btn_logo.setSizePolicy(sizePolicy6)
        self.btn_logo.setMinimumSize(QSize(50, 50))
        self.btn_logo.setSizeIncrement(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.btn_logo.setFont(font5)
        self.btn_logo.setStyleSheet(u"border: none;\n"
"border-top: 3px;\n"
"color: rgb(0, 0, 0);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logo.setIcon(icon3)
        self.btn_logo.setIconSize(QSize(50, 40))

        self.horizontalLayout_2.addWidget(self.btn_logo)


        self.verticalLayout.addWidget(self.logo)

        self.menu = QFrame(self.menu_bar)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(0, 0))
        self.menu.setMaximumSize(QSize(16777215, 16777215))
        self.menu.setBaseSize(QSize(0, 0))
        self.menu.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(170, 0, 127);\n"
" 	 border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(19,10,41);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray; \n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-top: 3px;\n"
"}")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 4, 0)
        self.btn_menu = QPushButton(self.menu)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy5.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy5)
        self.btn_menu.setMinimumSize(QSize(50, 50))
        self.btn_menu.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.btn_menu.setFont(font6)
        self.btn_menu.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon4)
        self.btn_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_menu)

        self.btn_metas = QPushButton(self.menu)
        self.btn_metas.setObjectName(u"btn_metas")
        self.btn_metas.setMinimumSize(QSize(50, 50))
        self.btn_metas.setFont(font2)
        self.btn_metas.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/meta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_metas.setIcon(icon5)
        self.btn_metas.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_metas)

        self.btn_consulta = QPushButton(self.menu)
        self.btn_consulta.setObjectName(u"btn_consulta")
        self.btn_consulta.setMinimumSize(QSize(50, 50))
        self.btn_consulta.setFont(font2)
        self.btn_consulta.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/icons8-lista-de-verifica\u00e7\u00e3o-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_consulta.setIcon(icon6)
        self.btn_consulta.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_consulta)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.menu)


        self.gridLayout_6.addWidget(self.menu_bar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.page_home.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icon/logo_completa_2.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"O Excel Inserido precisa ter as colunas nesse mesmo padr\u00e3o ", None))
        self.label_6.setText("")
        ___qtablewidgetitem = self.table_metas_inseridas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"COLOCAR OS NOMES ", None));
        ___qtablewidgetitem1 = self.table_metas_inseridas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DAS COLUNAS ", None));
        ___qtablewidgetitem2 = self.table_metas_inseridas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"QUE PRECISA", None));
        ___qtablewidgetitem3 = self.table_metas_inseridas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"TER COMO EXEMPLO", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Insira o Caminho do Excel ", None))
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_9.setText("")
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"       Adicionar", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icon/logo agrocompetence 3.png\"width=\"330\" height=\"90\"/></p></body></html>\n"
"", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Se houver erros ir\u00e3o aparecer aqui ", None))
        self.btn_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.filtro_Empresa.setItemText(0, QCoreApplication.translate("MainWindow", u"EMPRESA", None))
        self.filtro_Empresa.setItemText(1, QCoreApplication.translate("MainWindow", u"004 - RECH IMPORTADORA", None))
        self.filtro_Empresa.setItemText(2, QCoreApplication.translate("MainWindow", u"006 - RECH AGRICOLA", None))
        self.filtro_Empresa.setItemText(3, QCoreApplication.translate("MainWindow", u"008 - TELMAC", None))

        self.filtro_Empresa.setCurrentText(QCoreApplication.translate("MainWindow", u"EMPRESA", None))
        self.label_14.setText("")
        self.filtro_unidade.setItemText(0, QCoreApplication.translate("MainWindow", u"UNIDADE", None))

        self.filtro_unidade.setCurrentText(QCoreApplication.translate("MainWindow", u"UNIDADE", None))
        self.label_11.setText("")
        self.filtro_mes.setItemText(0, QCoreApplication.translate("MainWindow", u"M\u00caS", None))
        self.filtro_mes.setItemText(1, QCoreApplication.translate("MainWindow", u"Janeiro", None))
        self.filtro_mes.setItemText(2, QCoreApplication.translate("MainWindow", u"Fevereiro", None))
        self.filtro_mes.setItemText(3, QCoreApplication.translate("MainWindow", u"Mar\u00e7o", None))
        self.filtro_mes.setItemText(4, QCoreApplication.translate("MainWindow", u"Abril", None))
        self.filtro_mes.setItemText(5, QCoreApplication.translate("MainWindow", u"Maio", None))
        self.filtro_mes.setItemText(6, QCoreApplication.translate("MainWindow", u"Junho", None))
        self.filtro_mes.setItemText(7, QCoreApplication.translate("MainWindow", u"Julho", None))
        self.filtro_mes.setItemText(8, QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.filtro_mes.setItemText(9, QCoreApplication.translate("MainWindow", u"Setembro", None))
        self.filtro_mes.setItemText(10, QCoreApplication.translate("MainWindow", u"Outubro", None))
        self.filtro_mes.setItemText(11, QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.filtro_mes.setItemText(12, QCoreApplication.translate("MainWindow", u"Dezembro", None))

        self.label_12.setText("")
        self.filtro_ano.setItemText(0, QCoreApplication.translate("MainWindow", u"ANO", None))
        self.filtro_ano.setItemText(1, QCoreApplication.translate("MainWindow", u"2019", None))
        self.filtro_ano.setItemText(2, QCoreApplication.translate("MainWindow", u"2020", None))
        self.filtro_ano.setItemText(3, QCoreApplication.translate("MainWindow", u"2021", None))
        self.filtro_ano.setItemText(4, QCoreApplication.translate("MainWindow", u"2022", None))
        self.filtro_ano.setItemText(5, QCoreApplication.translate("MainWindow", u"2023", None))

        self.label_13.setText("")
        self.btn_filtro.setText(QCoreApplication.translate("MainWindow", u" Filtrar", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TOTAL", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"  Exportar", None))
        self.label_17.setText("")
        self.btn_logo.setText(QCoreApplication.translate("MainWindow", u"    In\u00edcio", None))
#if QT_CONFIG(whatsthis)
        self.menu.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"     Menu", None))
        self.btn_metas.setText(QCoreApplication.translate("MainWindow", u"       Metas", None))
        self.btn_consulta.setText(QCoreApplication.translate("MainWindow", u"       Consulta", None))
    # retranslateUi

