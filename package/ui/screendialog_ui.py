# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screendialog.ui'
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

class Ui_screenDialog(object):
    def setupUi(self, screenDialog):
        screenDialog.setObjectName(_fromUtf8("screenDialog"))
        screenDialog.resize(367, 174)
        self.verticalLayout = QtGui.QVBoxLayout(screenDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formScreen = QtGui.QFormLayout()
        self.formScreen.setObjectName(_fromUtf8("formScreen"))
        self.labelScreenName = QtGui.QLabel(screenDialog)
        self.labelScreenName.setObjectName(_fromUtf8("labelScreenName"))
        self.formScreen.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelScreenName)
        self.rbScreenVideo = QtGui.QRadioButton(screenDialog)
        self.rbScreenVideo.setObjectName(_fromUtf8("rbScreenVideo"))
        self.formScreen.setWidget(2, QtGui.QFormLayout.LabelRole, self.rbScreenVideo)
        self.rbScreenColor = QtGui.QRadioButton(screenDialog)
        self.rbScreenColor.setObjectName(_fromUtf8("rbScreenColor"))
        self.formScreen.setWidget(2, QtGui.QFormLayout.FieldRole, self.rbScreenColor)
        self.leScreenName = QtGui.QLineEdit(screenDialog)
        self.leScreenName.setObjectName(_fromUtf8("leScreenName"))
        self.formScreen.setWidget(0, QtGui.QFormLayout.FieldRole, self.leScreenName)
        self.pbScreenVideo = QtGui.QPushButton(screenDialog)
        self.pbScreenVideo.setObjectName(_fromUtf8("pbScreenVideo"))
        self.formScreen.setWidget(3, QtGui.QFormLayout.LabelRole, self.pbScreenVideo)
        self.leScreenVideo = QtGui.QLineEdit(screenDialog)
        self.leScreenVideo.setReadOnly(True)
        self.leScreenVideo.setObjectName(_fromUtf8("leScreenVideo"))
        self.formScreen.setWidget(3, QtGui.QFormLayout.FieldRole, self.leScreenVideo)
        self.pbScreenColor = QtGui.QPushButton(screenDialog)
        self.pbScreenColor.setObjectName(_fromUtf8("pbScreenColor"))
        self.formScreen.setWidget(4, QtGui.QFormLayout.LabelRole, self.pbScreenColor)
        self.leScreenColor = QtGui.QLineEdit(screenDialog)
        self.leScreenColor.setReadOnly(True)
        self.leScreenColor.setObjectName(_fromUtf8("leScreenColor"))
        self.formScreen.setWidget(4, QtGui.QFormLayout.FieldRole, self.leScreenColor)
        self.labelMonNum = QtGui.QLabel(screenDialog)
        self.labelMonNum.setObjectName(_fromUtf8("labelMonNum"))
        self.formScreen.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelMonNum)
        self.cbMonNum = QtGui.QComboBox(screenDialog)
        self.cbMonNum.setObjectName(_fromUtf8("cbMonNum"))
        self.formScreen.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbMonNum)
        self.verticalLayout.addLayout(self.formScreen)
        self.bbScreen = QtGui.QDialogButtonBox(screenDialog)
        self.bbScreen.setOrientation(QtCore.Qt.Horizontal)
        self.bbScreen.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbScreen.setObjectName(_fromUtf8("bbScreen"))
        self.verticalLayout.addWidget(self.bbScreen)

        self.retranslateUi(screenDialog)
        QtCore.QObject.connect(self.bbScreen, QtCore.SIGNAL(_fromUtf8("accepted()")), screenDialog.accept)
        QtCore.QObject.connect(self.bbScreen, QtCore.SIGNAL(_fromUtf8("rejected()")), screenDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(screenDialog)

    def retranslateUi(self, screenDialog):
        screenDialog.setWindowTitle(_translate("screenDialog", "Dialog", None))
        self.labelScreenName.setText(_translate("screenDialog", "TextLabel", None))
        self.rbScreenVideo.setText(_translate("screenDialog", "RadioButton", None))
        self.rbScreenColor.setText(_translate("screenDialog", "RadioButton", None))
        self.pbScreenVideo.setText(_translate("screenDialog", "PushButton", None))
        self.pbScreenColor.setText(_translate("screenDialog", "PushButton", None))
        self.labelMonNum.setText(_translate("screenDialog", "TextLabel", None))

