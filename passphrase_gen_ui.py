# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passphrase_gen.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_passphrase_gen(object):
    def setupUi(self, passphrase_gen):
        if not passphrase_gen.objectName():
            passphrase_gen.setObjectName(u"passphrase_gen")
        passphrase_gen.resize(715, 518)
        passphrase_gen.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(passphrase_gen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.island = QWidget(self.centralwidget)
        self.island.setObjectName(u"island")
        self.island.setGeometry(QRect(30, 130, 661, 371))
        self.island.setMinimumSize(QSize(661, 371))
        self.island.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.gen_button = QPushButton(self.island)
        self.gen_button.setObjectName(u"gen_button")
        self.gen_button.setGeometry(QRect(190, 240, 281, 71))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.gen_button.setFont(font)
        self.gen_button.setStyleSheet(u"background-color: rgb(51, 209, 122);")
        self.copy_button = QPushButton(self.island)
        self.copy_button.setObjectName(u"copy_button")
        self.copy_button.setGeometry(QRect(480, 80, 51, 41))
        icon = QIcon()
        icon.addFile(u"images/copy-icon-4804.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_button.setIcon(icon)
        self.copy_button.setIconSize(QSize(26, 26))
        self.layoutWidget = QWidget(self.island)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 160, 621, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.afri_button = QRadioButton(self.layoutWidget)
        self.afri_button.setObjectName(u"afri_button")

        self.horizontalLayout.addWidget(self.afri_button)

        self.eng_button = QRadioButton(self.layoutWidget)
        self.eng_button.setObjectName(u"eng_button")

        self.horizontalLayout.addWidget(self.eng_button)

        self.xhosa_button = QRadioButton(self.layoutWidget)
        self.xhosa_button.setObjectName(u"xhosa_button")

        self.horizontalLayout.addWidget(self.xhosa_button)

        self.zulu_button = QRadioButton(self.layoutWidget)
        self.zulu_button.setObjectName(u"zulu_button")

        self.horizontalLayout.addWidget(self.zulu_button)

        self.sotho_button = QRadioButton(self.layoutWidget)
        self.sotho_button.setObjectName(u"sotho_button")

        self.horizontalLayout.addWidget(self.sotho_button)

        self.lb_output = QLabel(self.island)
        self.lb_output.setObjectName(u"lb_output")
        self.lb_output.setGeometry(QRect(130, 80, 341, 41))
        self.lb_output.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.logo_island = QWidget(self.centralwidget)
        self.logo_island.setObjectName(u"logo_island")
        self.logo_island.setGeometry(QRect(30, 10, 661, 121))
        self.logo_island.setMinimumSize(QSize(661, 121))
        self.logo_island.setStyleSheet(u"background-color: rgb(69, 184, 197);")
        self.za_island = QWidget(self.logo_island)
        self.za_island.setObjectName(u"za_island")
        self.za_island.setGeometry(QRect(0, 0, 191, 121))
        self.label = QLabel(self.za_island)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 191, 131))
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setPixmap(QPixmap(u"images/za_logo.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2 = QLabel(self.logo_island)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 0, 481, 71))
        self.label_2.setMinimumSize(QSize(471, 61))
        self.label_2.setPixmap(QPixmap(u"images/zapass2_logo.png"))
        self.label_3 = QLabel(self.logo_island)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 60, 441, 61))
        self.label_3.setPixmap(QPixmap(u"images/zagen2_logo.png"))
        passphrase_gen.setCentralWidget(self.centralwidget)

        self.retranslateUi(passphrase_gen)

        QMetaObject.connectSlotsByName(passphrase_gen)
    # setupUi

    def retranslateUi(self, passphrase_gen):
        passphrase_gen.setWindowTitle(QCoreApplication.translate("passphrase_gen", u"MainWindow", None))
        self.gen_button.setText(QCoreApplication.translate("passphrase_gen", u"Generate", None))
        self.copy_button.setText("")
        self.afri_button.setText(QCoreApplication.translate("passphrase_gen", u"Afrikaans", None))
        self.eng_button.setText(QCoreApplication.translate("passphrase_gen", u"English", None))
        self.xhosa_button.setText(QCoreApplication.translate("passphrase_gen", u"IsiXhosa", None))
        self.zulu_button.setText(QCoreApplication.translate("passphrase_gen", u"IsiZulu", None))
        self.sotho_button.setText(QCoreApplication.translate("passphrase_gen", u"SeSotho", None))
        self.lb_output.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

