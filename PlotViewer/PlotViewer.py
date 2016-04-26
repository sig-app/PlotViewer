import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path = os.path.join(currentdir,'views','gen')
sys.path.insert(0,path)
from PyQt4 import QtGui
from ctrls.MainCtrl import Main

def plot_viwer():
    app = QtGui.QApplication([])
    return Main(app)
