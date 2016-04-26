from PyQt4 import QtGui
from ui_main_view import Ui_MainWindow
from ctrls.MplCtrl import Mpl

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
        
