##import sys
##from PyQt4 import QtGui
import numpy as np
from matplotlib.figure import Figure
from ctrls.MainCtrl import main

fig1 = Figure()
ax1f1 = fig1.add_subplot(111)
ax1f1.plot(np.random.rand(5))

fig2 = Figure()
ax1f2 = fig2.add_subplot(121)
ax1f2.plot(np.random.rand(5))
ax2f2 = fig2.add_subplot(122)
ax2f2.plot(np.random.rand(10))

fig3 = Figure()
ax1f3 = fig3.add_subplot(111)
ax1f3.pcolormesh(np.random.rand(20,20))



##app = QtGui.QApplication(sys.argv)
M = main()
M.addfig('One plot', fig1)
M.addfig('Two plots', fig2)
M.addfig('Pcolormesh', fig3)
M.show()
##sys.exit(app.exec_())
