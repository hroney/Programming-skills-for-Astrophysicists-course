import os
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(wx.Frame):
    
    def __init__(self): 
        wx.Frame.__init__(self, None, wx.NewId(), "Final Project")

        self.figure = Figure(figsize=(1,2))
        self.axe = self.figure.add_subplot(111)
        self.figurecanvas = FigureCanvas(self, -1, self.figure)
        
        # Creating the "Label", which shows you static text
        self.quote1 = wx.StaticText(self, label = "Please, insert the function:", pos = (20, 30))
        self.quote2 = wx.StaticText(self, label = "f(x)=", pos = (20, 60))
        
        # Just for Checking whther it is working or not
        # self.logger = wx.TextCtrl(self, pos = (300, 20), size = (100, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        
        # Creating the "TextCtrl". You can type here
        self.editFunction = wx.TextCtrl(self, value = "", size = (200, -1))
        #self.Bind(wx.EVT_TEXT, self.EvtText, self.editfunction)
        
        # Creating the "Button", which will delete the text in the cell
        self.deleteTextButton = wx.Button(self, label = "X", size=(30, 30))
        # Creating the "Button", which will plot your graph
        self.plotButton = wx.Button(self, label = "Plot", size = (wx.ALIGN_LEFT, -1))
        # Creating a button which will erase your graph
        self.eraseButton = wx.Button(self, label = "Erase", size = (wx.ALIGN_RIGHT, -1))

        # Setting a main sizeer
        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a graph sizer
        self.graphSizer = wx.BoxSizer(wx.HORIZONTAL)
        # Setting the main button sizer (vertical sizer)
        self.buttonSizer = wx.BoxSizer(wx.VERTICAL)
        # Setting a firstline horizaontal sizer
        self.sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting s secondline horizontal sizer
        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        # Setting a third line horizontal sizer
        self.sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        # Creating a Sizer Interface
        # Adding a quote1
        self.sizer1.Add(self.quote1, proportion = 1, border = 2, flag=wx.ALL)
        # Adding a Text label, Text Column and Erase Text Button
        self.sizer2.Add(self.quote2, proportion = 0, border = 2, flag=wx.ALL)
        self.sizer2.Add(self.editFunction, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer2.Add(self.deleteTextButton, proportion = 0, border = 2, flag = wx.ALL)
        # Adding two buttons for plotting
        self.sizer3.Add(self.plotButton, proportion = 1, border = 2, flag = wx.ALL)
        self.sizer3.Add(self.eraseButton, proportion = 1, border = 2, flag = wx.ALL)
        # Combining Sizers 1, 2, 3 together
        self.buttonSizer.Add(self.sizer1, 0, wx.ALIGN_BOTTOM)
        self.buttonSizer.Add(self.sizer2, 0, wx.EXPAND)
        self.buttonSizer.Add(self.sizer3, 0, wx.ALIGN_TOP)
        # Adding graph to Graph Sizer
        self.graphSizer.Add(self.figurecanvas, proportion=1, border=5, flag=wx.ALL | wx.EXPAND)
        # Combining Grapth and Button Sizers
        self.mainSizer.Add(self.graphSizer, 1, wx.EXPAND)
        self.mainSizer.Add(self.buttonSizer, 1, wx.EXPAND)
        self.SetSizer(self.mainSizer)
        
        # Summoning the method for Drawing Graphs
        self.plotButton.Bind(wx.EVT_BUTTON, self.PlotOnPress)
        
        # Creating statusBar in the bottom of the Window
        self.CreateStatusBar()
        
        # Setting up the menu
        filemenu = wx.Menu() 
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")
        
        # Creating the menubar
        menuBar = wx.MenuBar()
        # Adding the "filemenu" to the MenuBar
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        
        # Set events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Show(True)
        
    # Method for plotting graphs    
    def PlotOnPress(self, evt):
        self.figure.set_canvas(self.figurecanvas)
        self.axe.clear()
        self.axe.plot(range(int(self.editFunction.GetValue())), color = 'green')
        self.figurecanvas.draw()
        
    def OnAbout(self, e):
        # A message dialog box with an OK button
        dlg = wx.MessageDialog(self,"About FP", "Final project for Computer skills class", wx.OK)
        # Show it
        dlg.ShowModal()
        # Destroying after finishing
        dlg.Destroy
    
    # Method for closing the frame
    def OnExit(self, e):
        self.Close(True)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MainWindow()
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop() 