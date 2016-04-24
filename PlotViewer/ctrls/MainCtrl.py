from PyQt4.uic import loadUiType
import os

##from matplotlib.figure import Figure
##from matplotlib.backends.backend_qt4agg import (
##    FigureCanvasQTAgg as FigureCanvas,
##    NavigationToolbar2QT as NavigationToolbar)

from ctrls.MplCtrl import Mpl

view_path = os.path.join('views','MainView.ui')
Ui_MainWindow, QMainWindow = loadUiType(view_path)
        
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.gridLayout.addWidget(Mpl())
##        self.fig_dict = {}

##        self.mplfigs.itemClicked.connect(self.changefig)
##
##        fig = Figure()
##        self.addmpl(fig)
##
##    def changefig(self, item):
##        text = item.text()
##        self.rmmpl()
##        self.addmpl(self.fig_dict[text])
##
##    def addfig(self, name, fig):
##        self.fig_dict[name] = fig
##        self.mplfigs.addItem(name)
##
##    def addmpl(self, fig):
##        self.canvas = FigureCanvas(fig)
##        self.mplvl.addWidget(self.canvas)
##        self.canvas.draw()
##        self.toolbar = NavigationToolbar(self.canvas, 
##                self.mplwindow, coordinates=True)
##        self.mplvl.addWidget(self.toolbar)
### This is the alternate toolbar placement. Susbstitute the three lines above
### for these lines to see the different look.
####        self.toolbar = NavigationToolbar(self.canvas,
####                self, coordinates=True)
####        self.addToolBar(self.toolbar)
##
##    def rmmpl(self,):
##        self.mplvl.removeWidget(self.canvas)
##        self.canvas.close()
##        self.mplvl.removeWidget(self.toolbar)
##        self.toolbar.close()


