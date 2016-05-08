from PyQt4 import QtGui
from ui_main_view import Ui_MainWindow
from ctrls.MplCtrl import Mpl
import pickle

class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        self.app = app
        super(Main, self).__init__()
        self.setupUi(self)
        self.fig_dict = {}
        self.name_list = []
        self.mpl_list = [[None for i in range(3)] for ii in range(3)]

        self.action1x1.triggered.connect(self.grid_1x1)
        self.action1x2.triggered.connect(self.grid_1x2)
        self.action1x3.triggered.connect(self.grid_1x3)
        self.action2x1.triggered.connect(self.grid_2x1)
        self.action2x2.triggered.connect(self.grid_2x2)
        self.action2x2.triggered.connect(self.grid_2x3)
        self.action3x1.triggered.connect(self.grid_3x1)
        self.action3x2.triggered.connect(self.grid_3x2)
        self.action3x3.triggered.connect(self.grid_3x3)

        self.actionSave_Figure_list.triggered.connect(self.save)
        self.actionLoad_Figure_list.triggered.connect(self.load)

    def show(self):
        self.grid_1x1()
        super(Main,self).show()
        self.app.exec_()
        
    def addfig(self, name, fig):
        self.fig_dict[name] = fig
        self.name_list.append(name)

    def add_mpl(self,row,col):
        self.mpl_list[row][col] = Mpl(self.fig_dict,self.name_list)
        self.gridLayout.addWidget(self.mpl_list[row][col],row,col)

    def remove_mpl(self,row,col):
        self.gridLayout.removeWidget(self.mpl_list[row][col])
        self.mpl_list[row][col].deleteLater()
        self.mpl_list[row][col] = None

    def save(self):
        pickle.dump(self.fig_dict, open('myplot.p', 'wb'))

    def load(self):
        self.fig_dict = pickle.load(open("myplot.p", "rb"))
        for row in range(3):
            for col in range(3):
                if self.mpl_list[row][col]:
                    self.remove_mpl(row, col)
                    self.add_mpl(row, col)

    def grid_1x1(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row,col)

    def grid_1x2(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row, col)

    def grid_1x3(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 2:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row, col)
    def grid_2x1(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row,col)

    def grid_2x2(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row, col)

    def grid_2x3(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 2:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 2:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row, col)
    def grid_3x1(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 2 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row,col)

    def grid_3x2(self):
        for row in range(3):
            for col in range(3):
                if row == 0 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 0 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 1 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 2 and col == 0:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                elif row == 2 and col == 1:
                    if not self.mpl_list[row][col]:
                        self.add_mpl(row, col)
                else:
                    if self.mpl_list[row][col]:
                        self.remove_mpl(row, col)

    def grid_3x3(self):
        for row in range(3):
            for col in range(3):
                if not self.mpl_list[row][col]:
                    self.add_mpl(row, col)