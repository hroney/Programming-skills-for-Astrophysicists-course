import os
import wx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas



class MainWindow3D(wx.Panel):
    def __init__(self, parent): 
        wx.Panel.__init__(self, parent)
        #wx.Panel.__init__(self, None, wx.NewId(), "Final Project")
        
        self.figure = Figure(figsize = (1,2))
        #self.axe = self.figure.add_subplot(111)
        self.axe = self.figure.add_subplot(111, projection='3d')
        self.figurecanvas = FigureCanvas(self, -1, self.figure)
        
        # Setting a main sizeer
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a graph sizer
        self.graphSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Setting the main button sizer (vertical sizer)
        self.buttonSizer = wx.BoxSizer(wx.VERTICAL)
        # Adding graph to Graph Sizer
        self.graphSizer.Add(self.figurecanvas, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        # Combining Grapth and Button Sizers
        self.mainSizer.Add(self.graphSizer, 5, wx.EXPAND)
        self.mainSizer.Add(self.buttonSizer, 1, wx.ALIGN_TOP)
        self.SetSizer(self.mainSizer)