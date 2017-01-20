import os
import wx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure


class MainWindow2D(wx.Panel):
    
    def __init__(self, parent): 
        wx.Panel.__init__(self, parent)
        #wx.Panel.__init__(self, None, wx.NewId(), "Final Project")
        
        self.figure = Figure(figsize = (1,2))
        self.axe = self.figure.add_subplot(111)
        self.figurecanvas = FigureCanvas(self, -1, self.figure)
        
        # Creating the "Label", which shows you static text
        self.quote1 = wx.StaticText(self, label = "Please, insert the function:")
        self.quote2 = wx.StaticText(self, label = "f(x)=")
        # Quotes for range
        self.quote3 = wx.StaticText(self, label = "x: from")
        self.quote4 = wx.StaticText(self, label = "to")
        self.quote5 = wx.StaticText(self, label = "Step:")
        # Quotes for advanced settings - Color and Style
        #self.quoteColor = wx.StaticText(self, label = "Color:")
        #self.quoteStyle = wx.StaticText(self, label = "Style:")
        # Radio Boxes for Color and Style
        colorList = ['Black', 'Green', 'Red']
        self.colorRadioBox = wx.RadioBox(self, label = "Color:", pos = (20, 210), choices = colorList, majorDimension = 1,
                         style = wx.RA_SPECIFY_COLS)
        styleList = ['Solid', 'Dashed', 'Dotted']
        self.styleRadioBox = wx.RadioBox(self, label = "Style:", pos = (20, 210), choices = styleList, majorDimension = 1,
                         style = wx.RA_SPECIFY_COLS)
        
        # Just for Checking whther it is working or not
        # self.logger = wx.TextCtrl(self, pos = (300, 20), size = (100, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        
        # Creating the "TextCtrl". You can type here
        self.editFunction = wx.TextCtrl(self, value = "", size = (-1, -1))
        # Creating the "TextCtrl" for range
        self.fromCtrl = wx.TextCtrl(self, value = "", size = (-1, -1))
        self.toCtrl = wx.TextCtrl(self, value = "", size = (-1, -1))
        self.stepCtrl = wx.TextCtrl(self, value = "", size = (-1, -1))
        #self.Bind(wx.EVT_TEXT, self.EvtText, self.editfunction)
        
        # Creating the "Button", which will delete the text in the cell
        self.deleteTextButton1 = wx.Button(self, label = "X", size=(30, 30))
        self.deleteTextButton2 = wx.Button(self, label = "X", size=(30, 30))
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
        # Setting a firstline horizaontal sizer
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a secondline horizontal sizer
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting up the "Range Sizer" - the third line horizontal sizer
        self.sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        # Addint the fourths line - Advanced settings
        self.sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.colorSizer = wx.BoxSizer(wx.VERTICAL)
        self.styleSizer = wx.BoxSizer(wx.VERTICAL)
        # Setting a fifths line horizontal sizer
        self.sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        
        # Creating a Sizer Interface
        # Adding a quote1
        self.sizer1.Add(self.quote1, proportion = 1, border = 2, flag=wx.ALL)
        # Adding a Text label, Text Column and Erase Text Button (Labeled as "X")
        self.sizer2.Add(self.quote2, proportion = 1.5, border = 2, flag=wx.ALL)
        self.sizer2.Add(self.editFunction, proportion = 18.5, border = 2, flag = wx.ALL)
        self.sizer2.Add(self.deleteTextButton1, proportion = 0, border = 2, flag = wx.ALL)
        # Adding the range parameters (quotes, textbars etc.)
        self.sizer3.Add(self.quote3, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.fromCtrl, proportion = 2, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.quote4, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.toCtrl, proportion = 2, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.quote5, proportion = 0, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.stepCtrl, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.deleteTextButton2, proportion = 0, border = 2, flag = wx.ALL)
        # Adding the Advanced settings - Color, Style etc.
        self.colorSizer.Add(self.colorRadioBox, proportion = 0, border = 2, flag=wx.ALL)
        self.styleSizer.Add(self.styleRadioBox, proportion = 0, border = 2, flag=wx.ALL)
        self.sizer4.Add(self.colorSizer, proportion = 0, border = 2, flag=wx.ALL)
        self.sizer4.Add(self.styleSizer, proportion = 0, border = 2, flag=wx.ALL)
        # Adding two buttons for plotting
        self.sizer5.Add(self.plotButton, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer5.Add(self.eraseButton, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer5.Add(self.saveButton, proportion = 1, border = 2, flag = wx.ALL)
        # Combining Sizers 1, 2, 3 together
        self.buttonSizer.Add(self.sizer1, 0, wx.ALIGN_BOTTOM)
        self.buttonSizer.Add(self.sizer2, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer3, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer4, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.sizer5, 0, wx.ALIGN_TOP)
        # Adding graph to Graph Sizer
        self.graphSizer.Add(self.figurecanvas, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        # Combining Grapth and Button Sizers
        self.mainSizer.Add(self.graphSizer, 5, wx.EXPAND)
        self.mainSizer.Add(self.buttonSizer, 1, wx.ALIGN_TOP)
        self.SetSizer(self.mainSizer)
    
    
        '''Method Summoning'''
        # Summoning the method for Erasing Formulas' text
        self.deleteTextButton1.Bind(wx.EVT_BUTTON, self.DeleteTextOnPress1)
        self.deleteTextButton2.Bind(wx.EVT_BUTTON, self.DeleteTextOnPress2)
        # Summoning the method for Drawing Graphs
        self.plotButton.Bind(wx.EVT_BUTTON, self.PlotOnPress)
        # Summoning the method for Clearing the axes
        self.eraseButton.Bind(wx.EVT_BUTTON, self.ErasePlotOnPress)
        # Summoning the method for Saving your plot
        self.saveButton.Bind(wx.EVT_BUTTON, self.SavePlotOnPress)
        #self.Bind(wx.EVT_RADIOBOX, self.EvtColorRadioBox, self.colorRadioBox)
        # Summoning methods from RadioBoxes
        self.Bind(wx.EVT_RADIOBOX, self.EvtColorRadioBox, self.colorRadioBox)
        self.Bind(wx.EVT_RADIOBOX, self.EvtStyleRadioBox, self.styleRadioBox)
        
        # Creating statusBar in the bottom of the Window
        #self.CreateStatusBar()
        
        # Setting up the menu
        #filemenu = wx.Menu() 
        #menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        #menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")
        
        # Creating the menubar
        #menuBar = wx.MenuBar()
        # Adding the "filemenu" to the MenuBar
        #menuBar.Append(filemenu, "&File")
        #self.SetMenuBar(menuBar)
        
        # Set events
        #self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        #self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        #self.Show(True)
    
    # Method for erasing your text from the TextControl (deleting the graph formula)
    def DeleteTextOnPress1(self, evt):
        self.editFunction.SetValue('')
    def DeleteTextOnPress2(self, evt):
        self.fromCtrl.SetValue('')
        self.toCtrl.SetValue('')
        self.stepCtrl.SetValue('')
    
    # Method for shosing color of your graph
    def EvtColorRadioBox(self, event):
        i = event.GetInt()
        global _color
        _color = 'black'
        print i
        if (i == 0):
            _color = 'black'
        elif (i == 1):
            _color = 'green'
        elif (i == 2):
            _color = 'red'
        #print _color
        return _color
    
     # Method for shosing color of your graph
    def EvtStyleRadioBox(self, event):
        i = event.GetInt()
        global _style_shape
        global _style_width
        #global _style_marker
        #_style_shape = ''
        #_style_width = 1
        print i
        if (i == 0):
            _style_shape = 'solid'
            _style_width = 2
            #_style_marker = 'none'
        elif (i == 1):
            _style_shape = 'dashed'
            _style_width = 2
            #_style_marker = 'none'
        elif (i == 2):
            _style_shape = 'dotted'
            _style_width = 2
            #_style_marker = '*'
        #print _color
        return (_style_shape, _style_width)
    
        #self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
        
    # Method for plotting graphs by Pressing Button    
    def PlotOnPress(self, evt):
        self.figure.set_canvas(self.figurecanvas)
        # Clearing the axes
        self.axe.clear()
        # We are checking whether we have a range or not
        _from = self.fromCtrl.GetValue()
        _to = self.toCtrl.GetValue()
        _step = self.stepCtrl.GetValue()
        if (_from == ''):
            _from = '-10'
        if (_to == ''):
            _to = '10'
        if (_step == ''):
            _step = '1'
        # Setting the axes values (calculation range)
        x_from = float(_from)
        x_to = float(_to)
        x_step = float(_step)
        x = np.arange(x_from, x_to, x_step)
        # Converting what is written in our Box into formulas
        f_x = self.editFunction.GetValue()
        # Creating the global variable to be able saving properly the image
        global figureName
        figureName = 'f(x)=' + f_x
        # Drawing our plot
        self.axe.set_xlabel('X') # setting the label on X-Axis
        self.axe.set_ylabel('Y') # setting the label on Y-Axis
        self.axe.set_title('f(x)='+f_x) # setting the title for the graph
        self.axe.plot(x, eval(f_x), linewidth = _style_width, linestyle = _style_shape, color = _color)
        #self.axe.plot(range(int(self.editFunction.GetValue())), color = 'green')
        self.figurecanvas.draw()
        
    # Method for erasing the plotted graph
    def ErasePlotOnPress(self, evt):
        # Clearing the current axes
        self.axe.clear()
        self.figurecanvas.draw() # basically, we draw the "empty" graph
        
    # Method for saving your graph
    def SavePlotOnPress(self, evt):
        print figureName
        self.figure.savefig(figureName + '.jpg', dpi=400)
        
#    def OnAbout(self, e):
#        # A message dialog box with an OK button
#        dlg = wx.MessageDialog(self,"About FP", "Final project for Computer skills class", wx.OK)
#        # Show it
#        dlg.ShowModal()
        # Destroying after finishing
#        dlg.Destroy
    
    # Method for closing the frame
#    def OnExit(self, e):
#        self.Close(True)
        
#class MyApp(wx.App):
#    def OnInit(self):
#        frame = MainWindow()
#        frame.Show(True)
#        self.SetTopWindow(frame)
#        return True



#app = wx.App(False)
#frame = wx.Frame(None, title = "Demo with Notebook", size = (500,400))
#nb = wx.Notebook(frame)

#nb.AddPage(MainWindow(nb), "Absolute Positioning")
#nb.AddPage(MainWindow(nb), "Page Two")
#nb.AddPage(MainWindow(nb), "Page Three")
#frame.Show()
#app.MainLoop()