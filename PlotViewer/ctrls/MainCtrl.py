
import os
genpath = os.path.join('views','gen')
import sys
sys.path.append(genpath)


from PyQt4 import QtGui
##from PyQt4.uic import loadUiType
##import os
from ui_main_view import Ui_MainWindow

##from matplotlib.figure import Figure
##from matplotlib.backends.backend_qt4agg import (
##    FigureCanvasQTAgg as FigureCanvas,
##    NavigationToolbar2QT as NavigationToolbar)

from ctrls.MplCtrl import Mpl

##view_path = os.path.join('views','MainView.ui')
##Ui_MainWindow, QMainWindow = loadUiType(view_path)

def main():
    app = QtGui.QApplication([])
    return Main(app)

##class Main(QMainWindow, Ui_MainWindow):
class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        self.app = app
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}
        self.name_list = []
        self.mpl_list = []

    def show(self):
        self.add_mpl()
        super(Main,self).show()
        self.app.exec_()
        
    def addfig(self, name, fig):
        self.fig_dict[name] = fig
        self.name_list.append(name)

    def add_mpl(self):
        self.mpl_list.append(Mpl(self.fig_dict,self.name_list))
        self.gridLayout.addWidget(self.mpl_list[-1])
        
