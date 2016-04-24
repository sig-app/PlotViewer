import sys
from PyQt4 import QtGui
import numpy as np
from ctrls.MainCtrl import Main

##fig1 = Figure()
##ax1f1 = fig1.add_subplot(111)
##ax1f1.plot(np.random.rand(5))
##
##fig2 = Figure()
##ax1f2 = fig2.add_subplot(121)
##ax1f2.plot(np.random.rand(5))
##ax2f2 = fig2.add_subplot(122)
##ax2f2.plot(np.random.rand(10))
##
##fig3 = Figure()
##ax1f3 = fig3.add_subplot(111)
##ax1f3.pcolormesh(np.random.rand(20,20))

app = QtGui.QApplication(sys.argv)
main = Main()
##main.addfig('One plot', fig1)
##main.addfig('Two plots', fig2)
##main.addfig('Pcolormesh', fig3)
main.show()
sys.exit(app.exec_())
