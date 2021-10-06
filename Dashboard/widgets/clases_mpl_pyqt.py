from PyQt5.QtWidgets import* 
from PyQt5.QtGui import* 
from PyQt5.QtCore import* 

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MplCanvas11(FigureCanvas):
    def __init__(self):
        self.fig = Figure(facecolor = "0.94")
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)

class MplCanvas22(FigureCanvas):
    def __init__(self):
        self.fig = Figure(facecolor = "0.94")
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222)
        self.ax3 = self.fig.add_subplot(223)
        self.ax4 = self.fig.add_subplot(224)
        FigureCanvas.__init__(self, self.fig)

class MatplotlibWidget11(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas11()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbl.addWidget(self.toolbar)
        self.setLayout(self.vbl)

class MatplotlibWidget11_sin(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas11()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

class MatplotlibWidget22(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas22()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbl.addWidget(self.toolbar)
        self.setLayout(self.vbl)

class MatplotlibWidget22_sin(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas22()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)





