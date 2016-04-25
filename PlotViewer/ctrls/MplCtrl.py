##from PyQt4.uic import loadUiType
##import os
from PyQt4 import QtGui
from ui_mpl_widget import Ui_Form

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

##view_path = os.path.join('views','MplWidget.ui')
##Ui_Widget, QWidget = loadUiType(view_path)
        
##class Mpl(QWidget, Ui_Widget):
class Mpl(QtGui.QWidget, Ui_Form):
    def __init__(self, fig_dict, name_list):
        super(Mpl, self).__init__()
        self.setupUi(self)
        self.fig_dict = fig_dict
        self.name_list = name_list

##        self.mplfigs.itemClicked.connect(self.changefig)
        if self.fig_dict and self.name_list:
            fig = self.fig_dict[self.name_list[0]]
        else:
            fig = Figure()
        self.addmpl(fig)

    def changefig(self, item):
        text = item.text()
        self.rmmpl()
        self.addmpl(self.fig_dict[text])

##    def addfig(self, name, fig):
##        self.fig_dict[name] = fig
##        self.mplfigs.addItem(name)

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        self.ltMPL.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                self.wgtToolbox, coordinates=True)
        self.ltToolbox.addWidget(self.toolbar)

    def rmmpl(self,):
        self.ltMPL.removeWidget(self.canvas)
        self.canvas.close()
        self.ltToolbox.removeWidget(self.toolbar)
        self.toolbar.close()


