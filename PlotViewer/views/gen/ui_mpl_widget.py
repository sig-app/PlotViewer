# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotViewer\views\MplWidget.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mplwindow = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.mplvl = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.ltMPL = QtGui.QVBoxLayout()
        self.ltMPL.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.ltMPL.setObjectName(_fromUtf8("ltMPL"))
        self.mplvl.addLayout(self.ltMPL)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.wgtToolbox = QtGui.QWidget(self.mplwindow)
        self.wgtToolbox.setObjectName(_fromUtf8("wgtToolbox"))
        self.ltToolbox = QtGui.QHBoxLayout(self.wgtToolbox)
        self.ltToolbox.setObjectName(_fromUtf8("ltToolbox"))
        self.horizontalLayout.addWidget(self.wgtToolbox)
        self.ltNavigate = QtGui.QHBoxLayout()
        self.ltNavigate.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.ltNavigate.setObjectName(_fromUtf8("ltNavigate"))
        self.btnBack = QtGui.QPushButton(self.mplwindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBack.sizePolicy().hasHeightForWidth())
        self.btnBack.setSizePolicy(sizePolicy)
        self.btnBack.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/fig/back_arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setObjectName(_fromUtf8("btnBack"))
        self.ltNavigate.addWidget(self.btnBack)
        self.comboBoxSelect = QtGui.QComboBox(self.mplwindow)
        self.comboBoxSelect.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSelect.sizePolicy().hasHeightForWidth())
        self.comboBoxSelect.setSizePolicy(sizePolicy)
        self.comboBoxSelect.setMinimumSize(QtCore.QSize(0, 24))
        self.comboBoxSelect.setObjectName(_fromUtf8("comboBoxSelect"))
        self.ltNavigate.addWidget(self.comboBoxSelect)
        self.btnForward = QtGui.QPushButton(self.mplwindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnForward.sizePolicy().hasHeightForWidth())
        self.btnForward.setSizePolicy(sizePolicy)
        self.btnForward.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/fig/forward_arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon1)
        self.btnForward.setObjectName(_fromUtf8("btnForward"))
        self.ltNavigate.addWidget(self.btnForward)
        self.horizontalLayout.addLayout(self.ltNavigate)
        self.mplvl.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.mplwindow, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

import icons_rc
