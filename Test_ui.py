# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDial, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(467, 277)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnLed = QPushButton(self.centralwidget)
        self.btnLed.setObjectName(u"btnLed")
        self.btnLed.setGeometry(QRect(90, 40, 91, 41))
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(320, 30, 81, 91))
        self.dial.setMaximum(255)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(80, 190, 331, 23))
        self.progressBar.setValue(24)
        self.lblbtn = QLabel(self.centralwidget)
        self.lblbtn.setObjectName(u"lblbtn")
        self.lblbtn.setGeometry(QRect(80, 130, 191, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnLed.setText(QCoreApplication.translate("MainWindow", u"Prender", None))
        self.lblbtn.setText(QCoreApplication.translate("MainWindow", u"Sin Presionar", None))
    # retranslateUi

