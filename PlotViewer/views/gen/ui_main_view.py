# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotViewer\views\MainView.ui'
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
        MainWindow.resize(640, 617)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFiles = QtGui.QMenu(self.menuBar)
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))
        self.menuGrid = QtGui.QMenu(self.menuBar)
        self.menuGrid.setObjectName(_fromUtf8("menuGrid"))
        MainWindow.setMenuBar(self.menuBar)
        self.action1x1 = QtGui.QAction(MainWindow)
        self.action1x1.setObjectName(_fromUtf8("action1x1"))
        self.action1x2 = QtGui.QAction(MainWindow)
        self.action1x2.setObjectName(_fromUtf8("action1x2"))
        self.action2x2 = QtGui.QAction(MainWindow)
        self.action2x2.setObjectName(_fromUtf8("action2x2"))
        self.action1x3 = QtGui.QAction(MainWindow)
        self.action1x3.setObjectName(_fromUtf8("action1x3"))
        self.action2x3 = QtGui.QAction(MainWindow)
        self.action2x3.setObjectName(_fromUtf8("action2x3"))
        self.action3x3 = QtGui.QAction(MainWindow)
        self.action3x3.setObjectName(_fromUtf8("action3x3"))
        self.action2x1 = QtGui.QAction(MainWindow)
        self.action2x1.setObjectName(_fromUtf8("action2x1"))
        self.action3x1 = QtGui.QAction(MainWindow)
        self.action3x1.setObjectName(_fromUtf8("action3x1"))
        self.action3x2 = QtGui.QAction(MainWindow)
        self.action3x2.setObjectName(_fromUtf8("action3x2"))
        self.menuGrid.addAction(self.action1x1)
        self.menuGrid.addAction(self.action1x2)
        self.menuGrid.addAction(self.action2x1)
        self.menuGrid.addAction(self.action2x2)
        self.menuGrid.addAction(self.action1x3)
        self.menuGrid.addAction(self.action3x1)
        self.menuGrid.addAction(self.action2x3)
        self.menuGrid.addAction(self.action3x2)
        self.menuGrid.addAction(self.action3x3)
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuGrid.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFiles.setTitle(_translate("MainWindow", "Files", None))
        self.menuGrid.setTitle(_translate("MainWindow", "Grid", None))
        self.action1x1.setText(_translate("MainWindow", "1x1", None))
        self.action1x2.setText(_translate("MainWindow", "1x2", None))
        self.action2x2.setText(_translate("MainWindow", "2x2", None))
        self.action1x3.setText(_translate("MainWindow", "1x3", None))
        self.action2x3.setText(_translate("MainWindow", "2x3", None))
        self.action3x3.setText(_translate("MainWindow", "3x3", None))
        self.action2x1.setText(_translate("MainWindow", "2x1", None))
        self.action3x1.setText(_translate("MainWindow", "3x1", None))
        self.action3x2.setText(_translate("MainWindow", "3x2", None))

