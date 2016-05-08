from PyQt4 import QtGui
from ui_mpl_widget import Ui_Form

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

class Mpl(QtGui.QWidget, Ui_Form):
    def __init__(self, fig_dict, name_list):
        super(Mpl, self).__init__()
        self.setupUi(self)
        self.fig_dict = fig_dict
        self.name_list = name_list
        self.index = 0

        self.btnBack.clicked.connect(self.back)
        self.btnForward.clicked.connect(self.forward)

        self.comboBoxSelect.addItems(self.name_list)
        self.comboBoxSelect.setCurrentIndex(self.index)
        self.comboBoxSelect.activated.connect(self.select)
        
        if self.fig_dict and self.name_list:
            fig = self.fig_dict[self.name_list[self.index]]
        else:
            fig = Figure()
        self.addmpl(fig)

    def changefig(self,):
        self.comboBoxSelect.setCurrentIndex(self.index)
        fig = self.fig_dict[self.name_list[self.index]]
        self.rmmpl()
        self.addmpl(fig)

    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        # self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
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

    def back(self):
        self.index = self.index-1 if self.index!=0 else len(self.name_list)-1
        self.changefig()

    def forward(self):
        self.index = self.index+1 if self.index!=len(self.name_list)-1 else 0
        self.changefig()

    def select(self):
        self.index = self.comboBoxSelect.currentIndex()
        self.changefig()
