# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scpirt.ui'
#
# Created: Thu May 21 13:43:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/scpirt/resources/scpwiki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(520, 325))
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 745))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.imagebox_layout = QtGui.QVBoxLayout()
        self.imagebox_layout.setObjectName("imagebox_layout")
        self.gridLayout_2.addLayout(self.imagebox_layout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.File = QtGui.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Images = QtGui.QMenu(self.menubar)
        self.Images.setObjectName("Images")
        self.series1 = QtGui.QMenu(self.Images)
        self.series1.setObjectName("series1")
        self.series2 = QtGui.QMenu(self.Images)
        self.series2.setObjectName("series2")
        self.series3 = QtGui.QMenu(self.Images)
        self.series3.setObjectName("series3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.tales = QtGui.QAction(MainWindow)
        self.tales.setObjectName("tales")
        self.misc = QtGui.QAction(MainWindow)
        self.misc.setObjectName("misc")
        self.scp0 = QtGui.QAction(MainWindow)
        self.scp0.setObjectName("scp0")
        self.scp1 = QtGui.QAction(MainWindow)
        self.scp1.setObjectName("scp1")
        self.scp2 = QtGui.QAction(MainWindow)
        self.scp2.setObjectName("scp2")
        self.scp3 = QtGui.QAction(MainWindow)
        self.scp3.setObjectName("scp3")
        self.scp4 = QtGui.QAction(MainWindow)
        self.scp4.setObjectName("scp4")
        self.scp5 = QtGui.QAction(MainWindow)
        self.scp5.setObjectName("scp5")
        self.scp6 = QtGui.QAction(MainWindow)
        self.scp6.setObjectName("scp6")
        self.scp7 = QtGui.QAction(MainWindow)
        self.scp7.setObjectName("scp7")
        self.scp8 = QtGui.QAction(MainWindow)
        self.scp8.setObjectName("scp8")
        self.scp9 = QtGui.QAction(MainWindow)
        self.scp9.setObjectName("scp9")
        self.scp10 = QtGui.QAction(MainWindow)
        self.scp10.setObjectName("scp10")
        self.scp11 = QtGui.QAction(MainWindow)
        self.scp11.setObjectName("scp11")
        self.scp12 = QtGui.QAction(MainWindow)
        self.scp12.setObjectName("scp12")
        self.scp13 = QtGui.QAction(MainWindow)
        self.scp13.setObjectName("scp13")
        self.scp14 = QtGui.QAction(MainWindow)
        self.scp14.setObjectName("scp14")
        self.scp15 = QtGui.QAction(MainWindow)
        self.scp15.setObjectName("scp15")
        self.scp16 = QtGui.QAction(MainWindow)
        self.scp16.setObjectName("scp16")
        self.scp17 = QtGui.QAction(MainWindow)
        self.scp17.setObjectName("scp17")
        self.scp18 = QtGui.QAction(MainWindow)
        self.scp18.setObjectName("scp18")
        self.scp19 = QtGui.QAction(MainWindow)
        self.scp19.setObjectName("scp19")
        self.scp20 = QtGui.QAction(MainWindow)
        self.scp20.setObjectName("scp20")
        self.scp21 = QtGui.QAction(MainWindow)
        self.scp21.setObjectName("scp21")
        self.scp22 = QtGui.QAction(MainWindow)
        self.scp22.setObjectName("scp22")
        self.scp23 = QtGui.QAction(MainWindow)
        self.scp23.setObjectName("scp23")
        self.scp24 = QtGui.QAction(MainWindow)
        self.scp24.setObjectName("scp24")
        self.scp25 = QtGui.QAction(MainWindow)
        self.scp25.setObjectName("scp25")
        self.scp26 = QtGui.QAction(MainWindow)
        self.scp26.setObjectName("scp26")
        self.scp27 = QtGui.QAction(MainWindow)
        self.scp27.setObjectName("scp27")
        self.scp28 = QtGui.QAction(MainWindow)
        self.scp28.setObjectName("scp28")
        self.scp29 = QtGui.QAction(MainWindow)
        self.scp29.setObjectName("scp29")
        self.File.addAction(self.action_Quit)
        self.series1.addAction(self.scp0)
        self.series1.addAction(self.scp1)
        self.series1.addAction(self.scp2)
        self.series1.addAction(self.scp3)
        self.series1.addAction(self.scp4)
        self.series1.addAction(self.scp5)
        self.series1.addAction(self.scp6)
        self.series1.addAction(self.scp7)
        self.series1.addAction(self.scp8)
        self.series1.addAction(self.scp9)
        self.series2.addAction(self.scp10)
        self.series2.addAction(self.scp11)
        self.series2.addAction(self.scp12)
        self.series2.addAction(self.scp13)
        self.series2.addAction(self.scp14)
        self.series2.addAction(self.scp15)
        self.series2.addAction(self.scp16)
        self.series2.addAction(self.scp17)
        self.series2.addAction(self.scp18)
        self.series2.addAction(self.scp19)
        self.series3.addAction(self.scp20)
        self.series3.addAction(self.scp21)
        self.series3.addAction(self.scp22)
        self.series3.addAction(self.scp23)
        self.series3.addAction(self.scp24)
        self.series3.addAction(self.scp25)
        self.series3.addAction(self.scp26)
        self.series3.addAction(self.scp27)
        self.series3.addAction(self.scp28)
        self.series3.addAction(self.scp29)
        self.Images.addAction(self.series1.menuAction())
        self.Images.addAction(self.series2.menuAction())
        self.Images.addAction(self.series3.menuAction())
        self.Images.addAction(self.tales)
        self.Images.addAction(self.misc)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Images.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SCPIRT", None, QtGui.QApplication.UnicodeUTF8))
        self.File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.Images.setTitle(QtGui.QApplication.translate("MainWindow", "&Images", None, QtGui.QApplication.UnicodeUTF8))
        self.series1.setTitle(QtGui.QApplication.translate("MainWindow", "SCP Series 1", None, QtGui.QApplication.UnicodeUTF8))
        self.series2.setTitle(QtGui.QApplication.translate("MainWindow", "SCP Series 2", None, QtGui.QApplication.UnicodeUTF8))
        self.series3.setTitle(QtGui.QApplication.translate("MainWindow", "SCP Series 3", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.tales.setText(QtGui.QApplication.translate("MainWindow", "Tales", None, QtGui.QApplication.UnicodeUTF8))
        self.misc.setText(QtGui.QApplication.translate("MainWindow", "Misc.", None, QtGui.QApplication.UnicodeUTF8))
        self.scp0.setText(QtGui.QApplication.translate("MainWindow", "002 - 099", None, QtGui.QApplication.UnicodeUTF8))
        self.scp1.setText(QtGui.QApplication.translate("MainWindow", "100 - 199", None, QtGui.QApplication.UnicodeUTF8))
        self.scp2.setText(QtGui.QApplication.translate("MainWindow", "200 - 299", None, QtGui.QApplication.UnicodeUTF8))
        self.scp3.setText(QtGui.QApplication.translate("MainWindow", "300 - 399", None, QtGui.QApplication.UnicodeUTF8))
        self.scp4.setText(QtGui.QApplication.translate("MainWindow", "400 - 499", None, QtGui.QApplication.UnicodeUTF8))
        self.scp5.setText(QtGui.QApplication.translate("MainWindow", "500 - 599", None, QtGui.QApplication.UnicodeUTF8))
        self.scp6.setText(QtGui.QApplication.translate("MainWindow", "600 - 699", None, QtGui.QApplication.UnicodeUTF8))
        self.scp7.setText(QtGui.QApplication.translate("MainWindow", "700 - 799", None, QtGui.QApplication.UnicodeUTF8))
        self.scp8.setText(QtGui.QApplication.translate("MainWindow", "800 - 899", None, QtGui.QApplication.UnicodeUTF8))
        self.scp9.setText(QtGui.QApplication.translate("MainWindow", "900 - 999", None, QtGui.QApplication.UnicodeUTF8))
        self.scp10.setText(QtGui.QApplication.translate("MainWindow", "1000 - 1099", None, QtGui.QApplication.UnicodeUTF8))
        self.scp11.setText(QtGui.QApplication.translate("MainWindow", "1100 - 1199", None, QtGui.QApplication.UnicodeUTF8))
        self.scp12.setText(QtGui.QApplication.translate("MainWindow", "1200 - 1299", None, QtGui.QApplication.UnicodeUTF8))
        self.scp13.setText(QtGui.QApplication.translate("MainWindow", "1300 - 1399", None, QtGui.QApplication.UnicodeUTF8))
        self.scp14.setText(QtGui.QApplication.translate("MainWindow", "1400 - 1499", None, QtGui.QApplication.UnicodeUTF8))
        self.scp15.setText(QtGui.QApplication.translate("MainWindow", "1500 - 1599", None, QtGui.QApplication.UnicodeUTF8))
        self.scp16.setText(QtGui.QApplication.translate("MainWindow", "1600 - 1699", None, QtGui.QApplication.UnicodeUTF8))
        self.scp17.setText(QtGui.QApplication.translate("MainWindow", "1700 - 1799", None, QtGui.QApplication.UnicodeUTF8))
        self.scp18.setText(QtGui.QApplication.translate("MainWindow", "1800 - 1899", None, QtGui.QApplication.UnicodeUTF8))
        self.scp19.setText(QtGui.QApplication.translate("MainWindow", "1900 - 1999", None, QtGui.QApplication.UnicodeUTF8))
        self.scp20.setText(QtGui.QApplication.translate("MainWindow", "2000 - 2099", None, QtGui.QApplication.UnicodeUTF8))
        self.scp21.setText(QtGui.QApplication.translate("MainWindow", "2100 - 2199", None, QtGui.QApplication.UnicodeUTF8))
        self.scp22.setText(QtGui.QApplication.translate("MainWindow", "2200 - 2299", None, QtGui.QApplication.UnicodeUTF8))
        self.scp23.setText(QtGui.QApplication.translate("MainWindow", "2300 - 2399", None, QtGui.QApplication.UnicodeUTF8))
        self.scp24.setText(QtGui.QApplication.translate("MainWindow", "2400 - 2499", None, QtGui.QApplication.UnicodeUTF8))
        self.scp25.setText(QtGui.QApplication.translate("MainWindow", "2500 - 2599", None, QtGui.QApplication.UnicodeUTF8))
        self.scp26.setText(QtGui.QApplication.translate("MainWindow", "2600 - 2699", None, QtGui.QApplication.UnicodeUTF8))
        self.scp27.setText(QtGui.QApplication.translate("MainWindow", "2700 - 2799", None, QtGui.QApplication.UnicodeUTF8))
        self.scp28.setText(QtGui.QApplication.translate("MainWindow", "2800 - 2899", None, QtGui.QApplication.UnicodeUTF8))
        self.scp29.setText(QtGui.QApplication.translate("MainWindow", "2900 - 2999", None, QtGui.QApplication.UnicodeUTF8))

import scpirt_rc
