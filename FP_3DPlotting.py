import os
import wx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
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
        # Creating the canvas for graph
        self.figurecanvas = FigureCanvas(self, -1, self.figure)
        
        # Creating the "Label", which shows you static text
        self.quote0 = wx.StaticText(self, label = "Please, choose your drawing style:")
        self.quote1 = wx.StaticText(self, label = "Please, insert your funtion:")
        self.quote2 = wx.StaticText(self, label = "f(x,y)=")
        # Quotes for range (x)
        self.quote3_x = wx.StaticText(self, label = "x: from")
        self.quote4_x = wx.StaticText(self, label = "to")
        self.quote5_x = wx.StaticText(self, label = "Step:")
        # Quotes for range (y)
        self.quote3_y = wx.StaticText(self, label = "y: from")
        self.quote4_y = wx.StaticText(self, label = "to")
        self.quote5_y = wx.StaticText(self, label = "Step:")
        
        # Creating the ComboBox fox chosing optimal graph style
        self.plottingStyleList = ["Parametric Curve", "Surface", "Wire Frame", "Contour"]
                #self.combo = wx.ComboBox(self, choices=phasesList)
        self.combo = wx.ComboBox(self, choices = self.plottingStyleList, style = wx.CB_DROPDOWN)
        # Bindingan event for combobox
        self.combo.Bind(wx.EVT_COMBOBOX, self.EvtComboBox)
        
        # Creating the "TextCtrl". You can type here
        self.editFunction = wx.TextCtrl(self, value = "", size = (-1, -1))
        
        # Creating the "TextCtrl" for range (x)
        self.fromCtrl_x = wx.TextCtrl(self, value = "", size = (-1, -1))
        self.toCtrl_x = wx.TextCtrl(self, value = "", size = (-1, -1))
        self.stepCtrl_x = wx.TextCtrl(self, value = "", size = (-1, -1))
        # Creating the "TextCtrl" for range (y)
        self.fromCtrl_y = wx.TextCtrl(self, value = "", size = (-1, -1))
        self.toCtrl_y = wx.TextCtrl(self, value = "", size = (-1, -1))
        self.stepCtrl_y = wx.TextCtrl(self, value = "", size = (-1, -1))
        
        # Creating the "Button", which will delete the text in the cell
        self.deleteTextButton1 = wx.Button(self, label = "X", size=(30, 30))
        self.deleteTextButton2_x = wx.Button(self, label = "X", size=(30, 30))
        self.deleteTextButton2_y = wx.Button(self, label = "X", size=(30, 30))
        
        # Creating the "Button", which will plot your graph
        self.plotButton = wx.Button(self, label = "Plot", size = (-1, -1))
        # Creating a button which will erase your graph
        self.eraseButton = wx.Button(self, label = "Erase", size = (-1, -1))
        # Creating a button which will save your graph
        self.saveButton = wx.Button(self, label = "Save", size = (-1, -1))
        
        # Setting a main sizeer
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a graph sizer
        self.graphSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Setting the main button sizer (vertical sizer)
        self.buttonSizer = wx.BoxSizer(wx.VERTICAL)
        # Setting a very first (ground) horizontal line
        self.sizer0 = wx.BoxSizer(wx.HORIZONTAL) 
        # Setting a firstline horizontal sizer
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a secondline horizontal sizer
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting the fourthline - range for x
        self.sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting the fourthline - range for y
        self.sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a fifths line horizontal sizer
        self.sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        # Adding a ComboBox
        self.sizer0.Add(self.quote0, proportion = 1, border = 2, flag=wx.ALL)
        self.sizer0.Add(self.combo, proportion = 1, border = 2, flag=wx.ALL)
        # Adding a quote1
        self.sizer1.Add(self.quote1, proportion = 1, border = 2, flag=wx.ALL)
        # Adding a Text label, Text Column and Erase Text Button (Labeled as "X")
        self.sizer2.Add(self.quote2, proportion = 1.5, border = 2, flag=wx.ALL)
        self.sizer2.Add(self.editFunction, proportion = 18.5, border = 2, flag = wx.ALL)
        self.sizer2.Add(self.deleteTextButton1, proportion = 0, border = 2, flag = wx.ALL)
        # Adding the range parameters (quotes, textbars etc.) - for x
        self.sizer3.Add(self.quote3_x, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.fromCtrl_x, proportion = 2, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.quote4_x, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.toCtrl_x, proportion = 2, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.quote5_x, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.stepCtrl_x, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.deleteTextButton2_x, proportion = 0, border = 2, flag = wx.ALL)
        # Adding the range parameters (quotes, textbars etc.) - for y
        self.sizer4.Add(self.quote3_y, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer4.Add(self.fromCtrl_y, proportion = 2, border = 2, flag = wx.ALL)
        self.sizer4.Add(self.quote4_y, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer4.Add(self.toCtrl_y, proportion = 2, border = 2, flag = wx.ALL)
        self.sizer4.Add(self.quote5_y, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer4.Add(self.stepCtrl_y, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer4.Add(self.deleteTextButton2_y, proportion = 0, border = 2, flag = wx.ALL)
        # Adding three buttons for plotting
        self.sizer5.Add(self.plotButton, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer5.Add(self.eraseButton, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer5.Add(self.saveButton, proportion = 1, border = 2, flag = wx.ALL)
        # Combining Sizers 0, 1, 2, 3 together
        self.buttonSizer.Add(self.sizer0, 0, wx.ALIGN_BOTTOM)
        self.buttonSizer.Add(self.sizer1, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer2, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer3, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer4, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer5, 0, wx.ALIGN_TOP)
        # Adding graph to Graph Sizer
        self.graphSizer.Add(self.figurecanvas, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        # Combining Grapth and Button Sizers
        self.mainSizer.Add(self.graphSizer, 5, wx.EXPAND)
        self.mainSizer.Add(self.buttonSizer, 1, wx.EXPAND)
        self.SetSizer(self.mainSizer)
        
            
        '''Method Summoning'''
        # Summoning the method for Erasing Formulas' text
        self.deleteTextButton1.Bind(wx.EVT_BUTTON, self.DeleteTextOnPress1)
        self.deleteTextButton2_x.Bind(wx.EVT_BUTTON, self.DeleteTextOnPress2_X)
        self.deleteTextButton2_y.Bind(wx.EVT_BUTTON, self.DeleteTextOnPress2_Y)
        # Summoning the method for Drawing Graphs
        self.plotButton.Bind(wx.EVT_BUTTON, self.PlotOnPress3D)
        # Summoning the method for Clearing the axes
        self.eraseButton.Bind(wx.EVT_BUTTON, self.ErasePlotOnPress)
    
    # Method for erasing your text from the TextControl (deleting the graph formula)
    def DeleteTextOnPress1(self, evt):
        self.editFunction.SetValue('')
    def DeleteTextOnPress2_X(self, evt):
        self.fromCtrl_x.SetValue('')
        self.toCtrl_x.SetValue('')
        self.stepCtrl_x.SetValue('')
    def DeleteTextOnPress2_Y(self, evt):
        self.fromCtrl_y.SetValue('')
        self.toCtrl_y.SetValue('')
        self.stepCtrl_y.SetValue('')
    
    def PlotOnPress3D(self, evt):
        self.figure.set_canvas(self.figurecanvas)
        # Clearing the axes
        self.axe.clear()
        
        # We are checking whether we have a range or not
        _from_x = self.fromCtrl_x.GetValue()
        _to_x = self.toCtrl_x.GetValue()
        _step_x = self.stepCtrl_x.GetValue()
        if (_from_x == ''):
            _from_x = '-5'
        if (_to_x == ''):
            _to_x = '5'
        if (_step_x == ''):
            _step_x = '0.25'
        # Setting the axes values (calculation range for x)
        x_from = float(_from_x)
        x_to = float(_to_x)
        x_step = float(_step_x)
        x = np.arange(x_from, x_to, x_step)
        
        # The same procedure applies for y
        # We are checking whether we have a range or not
        _from_y = self.fromCtrl_y.GetValue()
        _to_y = self.toCtrl_y.GetValue()
        _step_y = self.stepCtrl_y.GetValue()
        if (_from_y == ''):
            _from_y = '-5'
        if (_to_y == ''):
            _to_y = '5'
        if (_step_y == ''):
            _step_y = '0.25'
        # Setting the axes values (calculation range for y)
        y_from = float(_from_y)
        y_to = float(_to_y)
        y_step = float(_step_y)
        y = np.arange(y_from, y_to, y_step)
        
        #x = np.arange(-5, 5, 0.25)
        #y = np.arange(-5, 5, 0.25)
        # Forming a grid
        x, y = np.meshgrid(x, y)
        #R = np.sqrt(X**2 + Y**2)
        #Z = np.sin(R)
        
        # For chosing between graph styles
        if (j == 0):
            theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
            z = np.linspace(-2, 2, 100)
            r = z**2 + 1
            x = r * np.sin(theta)
            y = r * np.cos(theta)
            self.axe.plot(x, y, z, label='Parametric curve')
            self.axe.legend()

        elif (j == 1):
            # Getting value from the function given
            z_xy = self.editFunction.GetValue()
            surf = self.axe.plot_surface(x, y, np.sin(eval(z_xy)), rstride=1, cstride=1, cmap=cm.coolwarm,
                    linewidth=0, antialiased=False)
            self.axe.set_zlim3d(-1.01, 1.01)
        elif (j == 2):

            X, Y, Z = axes3d.get_test_data(0.1)
            self.axe.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

            for angle in range(0, 360):
                self.axe.view_init(30, angle)
                self.figurecanvas.draw()
                
        elif (j == 3):
            X, Y, Z = axes3d.get_test_data(0.05)
            self.axe.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
            cset = self.axe.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
            cset = self.axe.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
            cset = self.axe.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

            self.axe.set_xlabel('X')
            self.axe.set_xlim(-40, 40)
            self.axe.set_ylabel('Y')
            self.axe.set_ylim(-40, 40)
            self.axe.set_zlabel('Z')
            self.axe.set_zlim(-100, 100)

        #self.figure.colorbar(surf, shrink=0.5, aspect=10)
        # Drawing a figure
        self.figurecanvas.draw()
        
    # Method for erasing the plotted graph
    def ErasePlotOnPress(self, evt):
        # Clearing the current axes
        self.axe.clear()
        self.figurecanvas.draw() # basically, we draw the "empty" graph
        
    # Method for shosing color of your graph
    def EvtComboBox(self, event):
        #if  event.GetString() == self.phasesList[0]:
        i = event.GetInt()
        print i
        global j
        j = i
        #global _color
        #_color = 'black'
        #print i
        #if (i == 0):
        #    _color = 'black'
        #elif (i == 1):
        #    _color = 'green'
        #elif (i == 2):
        #    _color = 'red'
        #print _color