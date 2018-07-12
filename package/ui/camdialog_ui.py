# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camdialog.ui'
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

class Ui_CamDialog(object):
    def setupUi(self, CamDialog):
        CamDialog.setObjectName(_fromUtf8("CamDialog"))
        CamDialog.resize(367, 146)
        self.verticalLayout = QtGui.QVBoxLayout(CamDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formCam = QtGui.QFormLayout()
        self.formCam.setObjectName(_fromUtf8("formCam"))
        self.labelCamName = QtGui.QLabel(CamDialog)
        self.labelCamName.setObjectName(_fromUtf8("labelCamName"))
        self.formCam.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelCamName)
        self.labelCamLink = QtGui.QLabel(CamDialog)
        self.labelCamLink.setObjectName(_fromUtf8("labelCamLink"))
        self.formCam.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCamLink)
        self.cbCamLink = QtGui.QComboBox(CamDialog)
        self.cbCamLink.setObjectName(_fromUtf8("cbCamLink"))
        self.formCam.setWidget(1, QtGui.QFormLayout.FieldRole, self.cbCamLink)
        self.labelCamRes = QtGui.QLabel(CamDialog)
        self.labelCamRes.setObjectName(_fromUtf8("labelCamRes"))
        self.formCam.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelCamRes)
        self.cbCamRes = QtGui.QComboBox(CamDialog)
        self.cbCamRes.setObjectName(_fromUtf8("cbCamRes"))
        self.formCam.setWidget(2, QtGui.QFormLayout.FieldRole, self.cbCamRes)
        self.leCamName = QtGui.QLineEdit(CamDialog)
        self.leCamName.setObjectName(_fromUtf8("leCamName"))
        self.formCam.setWidget(0, QtGui.QFormLayout.FieldRole, self.leCamName)
        self.verticalLayout.addLayout(self.formCam)
        self.bbCam = QtGui.QDialogButtonBox(CamDialog)
        self.bbCam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bbCam.setOrientation(QtCore.Qt.Horizontal)
        self.bbCam.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.bbCam.setObjectName(_fromUtf8("bbCam"))
        self.verticalLayout.addWidget(self.bbCam)

        self.retranslateUi(CamDialog)
        QtCore.QObject.connect(self.bbCam, QtCore.SIGNAL(_fromUtf8("accepted()")), CamDialog.accept)
        QtCore.QObject.connect(self.bbCam, QtCore.SIGNAL(_fromUtf8("rejected()")), CamDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CamDialog)

    def retranslateUi(self, CamDialog):
        CamDialog.setWindowTitle(_translate("CamDialog", "Dialog", None))
        self.labelCamName.setText(_translate("CamDialog", "TextLabel", None))
        self.labelCamLink.setText(_translate("CamDialog", "TextLabel", None))
        self.labelCamRes.setText(_translate("CamDialog", "TextLabel", None))

