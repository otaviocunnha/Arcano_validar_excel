# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import icon_login_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(819, 630)
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(58, 31, 127);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(400, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 550))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(214, 214, 214);\n"
"border-top: 10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, -10, 381, 201))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 0px;\n"
"	border: 0px solid gray; \n"
"	background-position: left center;\n"
"	background-repeat: no-repeat;\n"
"	border-top: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon_login/icon/Blue_and_Purple_Astronaut_E-Sports_Team_Logo____5_-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(400, 250))

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 25, 0, 30)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(30, 15, 30, 25)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_2)

        self.txt_usuario = QLineEdit(self.frame_6)
        self.txt_usuario.setObjectName(u"txt_usuario")
        font2 = QFont()
        font2.setPointSize(13)
        self.txt_usuario.setFont(font2)
        self.txt_usuario.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray; \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"")

        self.verticalLayout_5.addWidget(self.txt_usuario)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 1, 30, 50)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout_6.addWidget(self.label)

        self.txt_senha = QLineEdit(self.frame_7)
        self.txt_senha.setObjectName(u"txt_senha")
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_senha.setFont(font3)
        self.txt_senha.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray; \n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border-radius: 5px")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(250, -1, -1, -1)
        self.btn_login = QPushButton(self.frame_5)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy1)
        self.btn_login.setMinimumSize(QSize(0, 30))
        self.btn_login.setStyleSheet(u"QPushButton:hover {\n"
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

        self.verticalLayout_7.addWidget(self.btn_login)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.label_3.setText(QCoreApplication.translate("login", u"Seja bem-vindo,", None))
        self.label_4.setText(QCoreApplication.translate("login", u"Identifique-se abaixo para usar a linha de produtos Arcano </> ", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Usu\u00e1rio", None))
        self.label.setText(QCoreApplication.translate("login", u"Senha", None))
        self.txt_senha.setPlaceholderText("")
        self.btn_login.setText(QCoreApplication.translate("login", u"Entrar", None))
    # retranslateUi

