# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(734, 403)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.hlOutput = QtGui.QHBoxLayout()
        self.hlOutput.setObjectName(_fromUtf8("hlOutput"))
        self.labelOutput = QtGui.QLabel(self.centralwidget)
        self.labelOutput.setMinimumSize(QtCore.QSize(80, 50))
        self.labelOutput.setMaximumSize(QtCore.QSize(80, 50))
        self.labelOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutput.setObjectName(_fromUtf8("labelOutput"))
        self.hlOutput.addWidget(self.labelOutput)
        self.leOutput = QtGui.QLineEdit(self.centralwidget)
        self.leOutput.setReadOnly(True)
        self.leOutput.setObjectName(_fromUtf8("leOutput"))
        self.hlOutput.addWidget(self.leOutput)
        self.pbOutput = QtGui.QPushButton(self.centralwidget)
        self.pbOutput.setMinimumSize(QtCore.QSize(100, 50))
        self.pbOutput.setMaximumSize(QtCore.QSize(100, 50))
        self.pbOutput.setObjectName(_fromUtf8("pbOutput"))
        self.hlOutput.addWidget(self.pbOutput)
        self.hlOutput.setStretch(0, 1)
        self.hlOutput.setStretch(1, 6)
        self.hlOutput.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.hlOutput)
        self.hlControls = QtGui.QHBoxLayout()
        self.hlControls.setObjectName(_fromUtf8("hlControls"))
        self.lcdControls = QtGui.QLCDNumber(self.centralwidget)
        self.lcdControls.setMinimumSize(QtCore.QSize(350, 80))
        self.lcdControls.setMaximumSize(QtCore.QSize(16777215, 128))
        self.lcdControls.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdControls.setAutoFillBackground(False)
        self.lcdControls.setFrameShape(QtGui.QFrame.Box)
        self.lcdControls.setFrameShadow(QtGui.QFrame.Sunken)
        self.lcdControls.setDigitCount(12)
        self.lcdControls.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdControls.setProperty("value", 0.0)
        self.lcdControls.setObjectName(_fromUtf8("lcdControls"))
        self.hlControls.addWidget(self.lcdControls)
        self.gfControls = QtGui.QFrame(self.centralwidget)
        self.gfControls.setMaximumSize(QtCore.QSize(16777215, 128))
        self.gfControls.setFrameShape(QtGui.QFrame.Box)
        self.gfControls.setFrameShadow(QtGui.QFrame.Sunken)
        self.gfControls.setObjectName(_fromUtf8("gfControls"))
        self.glHLControls = QtGui.QGridLayout(self.gfControls)
        self.glHLControls.setObjectName(_fromUtf8("glHLControls"))
        self.labelControls = QtGui.QLabel(self.gfControls)
        self.labelControls.setMinimumSize(QtCore.QSize(80, 80))
        self.labelControls.setMaximumSize(QtCore.QSize(100, 100))
        self.labelControls.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelControls.setWordWrap(True)
        self.labelControls.setObjectName(_fromUtf8("labelControls"))
        self.glHLControls.addWidget(self.labelControls, 2, 1, 2, 1)
        self.rbCRLoops = QtGui.QRadioButton(self.gfControls)
        self.rbCRLoops.setObjectName(_fromUtf8("rbCRLoops"))
        self.glHLControls.addWidget(self.rbCRLoops, 3, 2, 1, 1)
        self.rbCRTime = QtGui.QRadioButton(self.gfControls)
        self.rbCRTime.setObjectName(_fromUtf8("rbCRTime"))
        self.glHLControls.addWidget(self.rbCRTime, 2, 2, 1, 1)
        self.hlCSLoops = QtGui.QHBoxLayout()
        self.hlCSLoops.setObjectName(_fromUtf8("hlCSLoops"))
        self.spinLoops = QtGui.QSpinBox(self.gfControls)
        self.spinLoops.setAlignment(QtCore.Qt.AlignCenter)
        self.spinLoops.setMinimum(1)
        self.spinLoops.setProperty("value", 1)
        self.spinLoops.setObjectName(_fromUtf8("spinLoops"))
        self.hlCSLoops.addWidget(self.spinLoops)
        self.labelLoops = QtGui.QLabel(self.gfControls)
        self.labelLoops.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoops.setObjectName(_fromUtf8("labelLoops"))
        self.hlCSLoops.addWidget(self.labelLoops)
        self.glHLControls.addLayout(self.hlCSLoops, 3, 3, 1, 1)
        self.teCSDuration = QtGui.QTimeEdit(self.gfControls)
        self.teCSDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.teCSDuration.setCurrentSection(QtGui.QDateTimeEdit.HourSection)
        self.teCSDuration.setObjectName(_fromUtf8("teCSDuration"))
        self.glHLControls.addWidget(self.teCSDuration, 2, 3, 1, 1)
        self.tbControls = QtGui.QToolButton(self.gfControls)
        self.tbControls.setMinimumSize(QtCore.QSize(80, 80))
        self.tbControls.setMaximumSize(QtCore.QSize(128, 128))
        self.tbControls.setStyleSheet(_fromUtf8("opacity: 50%;"))
        self.tbControls.setIconSize(QtCore.QSize(256, 256))
        self.tbControls.setObjectName(_fromUtf8("tbControls"))
        self.glHLControls.addWidget(self.tbControls, 2, 0, 2, 1)
        self.hlControls.addWidget(self.gfControls)
        self.hlControls.setStretch(0, 3)
        self.verticalLayout_2.addLayout(self.hlControls)
        self.tabGroup = QtGui.QTabWidget(self.centralwidget)
        self.tabGroup.setObjectName(_fromUtf8("tabGroup"))
        self.tabCam = QtGui.QWidget()
        self.tabCam.setObjectName(_fromUtf8("tabCam"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabCam)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.hlTabCam = QtGui.QHBoxLayout()
        self.hlTabCam.setObjectName(_fromUtf8("hlTabCam"))
        self.lwCam = QtGui.QListWidget(self.tabCam)
        self.lwCam.setObjectName(_fromUtf8("lwCam"))
        self.hlTabCam.addWidget(self.lwCam)
        self.vlCam = QtGui.QVBoxLayout()
        self.vlCam.setObjectName(_fromUtf8("vlCam"))
        self.pbCamAdd = QtGui.QPushButton(self.tabCam)
        self.pbCamAdd.setMaximumSize(QtCore.QSize(200, 30))
        self.pbCamAdd.setObjectName(_fromUtf8("pbCamAdd"))
        self.vlCam.addWidget(self.pbCamAdd)
        self.pbCamEdit = QtGui.QPushButton(self.tabCam)
        self.pbCamEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.pbCamEdit.setObjectName(_fromUtf8("pbCamEdit"))
        self.vlCam.addWidget(self.pbCamEdit)
        self.pbCamOpen = QtGui.QPushButton(self.tabCam)
        self.pbCamOpen.setMaximumSize(QtCore.QSize(200, 30))
        self.pbCamOpen.setObjectName(_fromUtf8("pbCamOpen"))
        self.vlCam.addWidget(self.pbCamOpen)
        self.pbCamRemove = QtGui.QPushButton(self.tabCam)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbCamRemove.sizePolicy().hasHeightForWidth())
        self.pbCamRemove.setSizePolicy(sizePolicy)
        self.pbCamRemove.setMaximumSize(QtCore.QSize(200, 30))
        self.pbCamRemove.setObjectName(_fromUtf8("pbCamRemove"))
        self.vlCam.addWidget(self.pbCamRemove)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlCam.addItem(spacerItem)
        self.hlTabCam.addLayout(self.vlCam)
        self.hlTabCam.setStretch(0, 4)
        self.hlTabCam.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.hlTabCam)
        self.tabGroup.addTab(self.tabCam, _fromUtf8(""))
        self.tabScreen = QtGui.QWidget()
        self.tabScreen.setObjectName(_fromUtf8("tabScreen"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tabScreen)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.hlTabScreen = QtGui.QHBoxLayout()
        self.hlTabScreen.setObjectName(_fromUtf8("hlTabScreen"))
        self.lwScreen = QtGui.QListWidget(self.tabScreen)
        self.lwScreen.setObjectName(_fromUtf8("lwScreen"))
        self.hlTabScreen.addWidget(self.lwScreen)
        self.vlScreen = QtGui.QVBoxLayout()
        self.vlScreen.setObjectName(_fromUtf8("vlScreen"))
        self.pbScreenAdd = QtGui.QPushButton(self.tabScreen)
        self.pbScreenAdd.setMaximumSize(QtCore.QSize(200, 30))
        self.pbScreenAdd.setObjectName(_fromUtf8("pbScreenAdd"))
        self.vlScreen.addWidget(self.pbScreenAdd)
        self.pbScreenEdit = QtGui.QPushButton(self.tabScreen)
        self.pbScreenEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.pbScreenEdit.setObjectName(_fromUtf8("pbScreenEdit"))
        self.vlScreen.addWidget(self.pbScreenEdit)
        self.pbScreenOpen = QtGui.QPushButton(self.tabScreen)
        self.pbScreenOpen.setMaximumSize(QtCore.QSize(200, 30))
        self.pbScreenOpen.setObjectName(_fromUtf8("pbScreenOpen"))
        self.vlScreen.addWidget(self.pbScreenOpen)
        self.pbScreenRemove = QtGui.QPushButton(self.tabScreen)
        self.pbScreenRemove.setMaximumSize(QtCore.QSize(200, 30))
        self.pbScreenRemove.setObjectName(_fromUtf8("pbScreenRemove"))
        self.vlScreen.addWidget(self.pbScreenRemove)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlScreen.addItem(spacerItem1)
        self.hlTabScreen.addLayout(self.vlScreen)
        self.hlTabScreen.setStretch(0, 4)
        self.hlTabScreen.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.hlTabScreen)
        self.tabGroup.addTab(self.tabScreen, _fromUtf8(""))
        self.tabDevices = QtGui.QWidget()
        self.tabDevices.setObjectName(_fromUtf8("tabDevices"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tabDevices)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.hlTabDevices = QtGui.QHBoxLayout()
        self.hlTabDevices.setObjectName(_fromUtf8("hlTabDevices"))
        self.lwDevices = QtGui.QListWidget(self.tabDevices)
        self.lwDevices.setObjectName(_fromUtf8("lwDevices"))
        self.hlTabDevices.addWidget(self.lwDevices)
        self.vlDevices = QtGui.QVBoxLayout()
        self.vlDevices.setObjectName(_fromUtf8("vlDevices"))
        self.pbDevicesAdd = QtGui.QPushButton(self.tabDevices)
        self.pbDevicesAdd.setMaximumSize(QtCore.QSize(200, 30))
        self.pbDevicesAdd.setObjectName(_fromUtf8("pbDevicesAdd"))
        self.vlDevices.addWidget(self.pbDevicesAdd)
        self.pbDevicesEdit = QtGui.QPushButton(self.tabDevices)
        self.pbDevicesEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.pbDevicesEdit.setObjectName(_fromUtf8("pbDevicesEdit"))
        self.vlDevices.addWidget(self.pbDevicesEdit)
        self.pbDevicesOpen = QtGui.QPushButton(self.tabDevices)
        self.pbDevicesOpen.setMaximumSize(QtCore.QSize(200, 30))
        self.pbDevicesOpen.setObjectName(_fromUtf8("pbDevicesOpen"))
        self.vlDevices.addWidget(self.pbDevicesOpen)
        self.pbDevicesRemove = QtGui.QPushButton(self.tabDevices)
        self.pbDevicesRemove.setMaximumSize(QtCore.QSize(200, 30))
        self.pbDevicesRemove.setObjectName(_fromUtf8("pbDevicesRemove"))
        self.vlDevices.addWidget(self.pbDevicesRemove)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlDevices.addItem(spacerItem2)
        self.hlTabDevices.addLayout(self.vlDevices)
        self.hlTabDevices.setStretch(0, 4)
        self.hlTabDevices.setStretch(1, 1)
        self.horizontalLayout_6.addLayout(self.hlTabDevices)
        self.tabGroup.addTab(self.tabDevices, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabGroup)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 7)
        self.verticalLayout_2.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuAdd = QtGui.QMenu(self.menubar)
        self.menuAdd.setObjectName(_fromUtf8("menuAdd"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Config = QtGui.QAction(MainWindow)
        self.actionNew_Config.setObjectName(_fromUtf8("actionNew_Config"))
        self.actionOpen_Config = QtGui.QAction(MainWindow)
        self.actionOpen_Config.setObjectName(_fromUtf8("actionOpen_Config"))
        self.actionSave_Config = QtGui.QAction(MainWindow)
        self.actionSave_Config.setObjectName(_fromUtf8("actionSave_Config"))
        self.actionSave_Config_As = QtGui.QAction(MainWindow)
        self.actionSave_Config_As.setObjectName(_fromUtf8("actionSave_Config_As"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setIconVisibleInMenu(True)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionCamera = QtGui.QAction(MainWindow)
        self.actionCamera.setObjectName(_fromUtf8("actionCamera"))
        self.actionVideo = QtGui.QAction(MainWindow)
        self.actionVideo.setObjectName(_fromUtf8("actionVideo"))
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionNew_Config)
        self.menuFile.addAction(self.actionOpen_Config)
        self.menuFile.addAction(self.actionSave_Config)
        self.menuFile.addAction(self.actionSave_Config_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addAction(self.actionStop)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAdd.addAction(self.actionCamera)
        self.menuAdd.addAction(self.actionVideo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabGroup.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelOutput.setText(_translate("MainWindow", "TextLabel", None))
        self.pbOutput.setText(_translate("MainWindow", "PushButton", None))
        self.labelControls.setText(_translate("MainWindow", "TextLabel", None))
        self.rbCRLoops.setText(_translate("MainWindow", "RadioButton", None))
        self.rbCRTime.setText(_translate("MainWindow", "RadioButton", None))
        self.labelLoops.setText(_translate("MainWindow", "TextLabel", None))
        self.teCSDuration.setDisplayFormat(_translate("MainWindow", "hh:mm:ss", None))
        self.tbControls.setText(_translate("MainWindow", "...", None))
        self.pbCamAdd.setText(_translate("MainWindow", "PushButton", None))
        self.pbCamEdit.setText(_translate("MainWindow", "PushButton", None))
        self.pbCamOpen.setText(_translate("MainWindow", "PushButton", None))
        self.pbCamRemove.setText(_translate("MainWindow", "PushButton", None))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.tabCam), _translate("MainWindow", "Tab 2", None))
        self.pbScreenAdd.setText(_translate("MainWindow", "PushButton", None))
        self.pbScreenEdit.setText(_translate("MainWindow", "PushButton", None))
        self.pbScreenOpen.setText(_translate("MainWindow", "PushButton", None))
        self.pbScreenRemove.setText(_translate("MainWindow", "PushButton", None))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.tabScreen), _translate("MainWindow", "Page", None))
        self.pbDevicesAdd.setText(_translate("MainWindow", "PushButton", None))
        self.pbDevicesEdit.setText(_translate("MainWindow", "PushButton", None))
        self.pbDevicesOpen.setText(_translate("MainWindow", "PushButton", None))
        self.pbDevicesRemove.setText(_translate("MainWindow", "PushButton", None))
        self.tabGroup.setTabText(self.tabGroup.indexOf(self.tabDevices), _translate("MainWindow", "Tab 1", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuAdd.setTitle(_translate("MainWindow", "Add", None))
        self.actionNew_Config.setText(_translate("MainWindow", "New Config", None))
        self.actionNew_Config.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionOpen_Config.setText(_translate("MainWindow", "Open Config...", None))
        self.actionOpen_Config.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSave_Config.setText(_translate("MainWindow", "Save Config", None))
        self.actionSave_Config.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSave_Config_As.setText(_translate("MainWindow", "Save Config As...", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1", None))
        self.actionCamera.setText(_translate("MainWindow", "Camera...", None))
        self.actionVideo.setText(_translate("MainWindow", "Video...", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

