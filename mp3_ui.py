# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mp3.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_Main_MP3(object):
    def setupUi(self, Main_MP3):
        if not Main_MP3.objectName():
            Main_MP3.setObjectName(u"Main_MP3")
        Main_MP3.setEnabled(True)
        Main_MP3.resize(639, 364)
        Main_MP3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.centralwidget = QWidget(Main_MP3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.opMusic = QComboBox(self.centralwidget)
        self.opMusic.addItem("")
        self.opMusic.setObjectName(u"opMusic")
        self.opMusic.setGeometry(QRect(150, 10, 231, 22))
        self.btnAnterior = QPushButton(self.centralwidget)
        self.btnAnterior.setObjectName(u"btnAnterior")
        self.btnAnterior.setGeometry(QRect(170, 60, 61, 41))
        self.btnReprPausa = QPushButton(self.centralwidget)
        self.btnReprPausa.setObjectName(u"btnReprPausa")
        self.btnReprPausa.setGeometry(QRect(240, 60, 61, 41))
        self.btnSiguiente = QPushButton(self.centralwidget)
        self.btnSiguiente.setObjectName(u"btnSiguiente")
        self.btnSiguiente.setGeometry(QRect(310, 60, 61, 41))
        self.sonido = QProgressBar(self.centralwidget)
        self.sonido.setObjectName(u"sonido")
        self.sonido.setEnabled(True)
        self.sonido.setGeometry(QRect(160, 130, 221, 23))
        self.sonido.setValue(0)
        self.btnSubirV = QPushButton(self.centralwidget)
        self.btnSubirV.setObjectName(u"btnSubirV")
        self.btnSubirV.setGeometry(QRect(410, 50, 75, 24))
        self.btnBajarV = QPushButton(self.centralwidget)
        self.btnBajarV.setObjectName(u"btnBajarV")
        self.btnBajarV.setGeometry(QRect(410, 140, 75, 24))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajarV.sizePolicy().hasHeightForWidth())
        self.btnBajarV.setSizePolicy(sizePolicy)
        Main_MP3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_MP3)

        QMetaObject.connectSlotsByName(Main_MP3)
    # setupUi

    def retranslateUi(self, Main_MP3):
        Main_MP3.setWindowTitle(QCoreApplication.translate("Main_MP3", u"Radio", None))
        self.opMusic.setItemText(0, QCoreApplication.translate("Main_MP3", u"MUSICA", None))

        self.btnAnterior.setText(QCoreApplication.translate("Main_MP3", u"\u23ea", None))
        self.btnReprPausa.setText(QCoreApplication.translate("Main_MP3", u"\u23ef\ufe0f", None))
        self.btnSiguiente.setText(QCoreApplication.translate("Main_MP3", u"\u23e9", None))
        self.btnSubirV.setText(QCoreApplication.translate("Main_MP3", u"subir", None))
        self.btnBajarV.setText(QCoreApplication.translate("Main_MP3", u"bajar", None))
    # retranslateUi

