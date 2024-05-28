# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 40, 342, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.fileBtn = QPushButton(self.layoutWidget1)
        self.fileBtn.setObjectName(u"fileBtn")

        self.horizontalLayout.addWidget(self.fileBtn)

        self.lineEdit_FilePath = QLineEdit(self.layoutWidget1)
        self.lineEdit_FilePath.setObjectName(u"lineEdit_FilePath")

        self.horizontalLayout.addWidget(self.lineEdit_FilePath)

        self.xml_title_info = QTextEdit(self.centralwidget)
        self.xml_title_info.setObjectName(u"xml_title_info")
        self.xml_title_info.setGeometry(QRect(150, 80, 281, 251))
        self.pushButton_xml_header = QPushButton(self.centralwidget)
        self.pushButton_xml_header.setObjectName(u"pushButton_xml_header")
        self.pushButton_xml_header.setGeometry(QRect(20, 90, 111, 31))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(480, 70, 271, 21))
        self.ExcuteResult = QPushButton(self.centralwidget)
        self.ExcuteResult.setObjectName(u"ExcuteResult")
        self.ExcuteResult.setGeometry(QRect(560, 120, 121, 31))
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(480, 40, 241, 22))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.ResultName = QLineEdit(self.layoutWidget2)
        self.ResultName.setObjectName(u"ResultName")

        self.horizontalLayout_5.addWidget(self.ResultName)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(41, 370, 441, 141))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.selectFirstTitle = QComboBox(self.layoutWidget3)
        self.selectFirstTitle.setObjectName(u"selectFirstTitle")

        self.horizontalLayout_2.addWidget(self.selectFirstTitle)

        self.lineEdit_first_title = QLineEdit(self.layoutWidget3)
        self.lineEdit_first_title.setObjectName(u"lineEdit_first_title")

        self.horizontalLayout_2.addWidget(self.lineEdit_first_title)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.selectSecondTitle = QComboBox(self.layoutWidget3)
        self.selectSecondTitle.setObjectName(u"selectSecondTitle")

        self.horizontalLayout_3.addWidget(self.selectSecondTitle)

        self.lineEdit_second_title = QLineEdit(self.layoutWidget3)
        self.lineEdit_second_title.setObjectName(u"lineEdit_second_title")

        self.horizontalLayout_3.addWidget(self.lineEdit_second_title)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_auto_produce = QPushButton(self.layoutWidget3)
        self.pushButton_auto_produce.setObjectName(u"pushButton_auto_produce")

        self.verticalLayout_2.addWidget(self.pushButton_auto_produce)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8981\u89e3\u6790\u7684doc\u6587\u4ef6", None))
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9doc\u6587\u4ef6", None))
        self.pushButton_xml_header.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u6240\u6709\u6807\u9898\u4fe1\u606f", None))
        self.ExcuteResult.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u7ed3\u679cexcel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"excel\u6587\u4ef6\u6807\u9898", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u".xls", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u7ea7\u6807\u9898\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ea7\u6807\u9898\u9009\u62e9", None))
        self.pushButton_auto_produce.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u751f\u6210\u4e09\u7ea7\u4ee5\u4e0a\u8868\u683c", None))
    # retranslateUi

