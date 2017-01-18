from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx

class PlottingPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # Creating the "Label", which shows you static text
        self.quote = wx.StaticText(self, label = "Please, insert the function:", pos = (20, 30))
        self.quote = wx.StaticText(self, label = "f(x)=", pos = (20, 60))
        # Just for Checking whther it is working or not
        # self.logger = wx.TextCtrl(self, pos = (300, 20), size = (100, 100), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # Creating the "TextCtrl". You can type here
        self.editfunction = wx.TextCtrl(self, value = "", pos = (50, 60), size = (200, -1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editfunction)
        # Creating the "Button", which will delete the text in the cell
        self.deleteTextButton = wx.Button(self, label = "X", pos=(250, 59), size=(30, 30))
        # Creating the "Button", which will plot your graph
        self.plotButton = wx.Button(self, label = "Plot", pos = (30, 100))
        # Creating a button which will erase your graph
        self.eraseButton = wx.Button(self, label = "Erase", pos = (150, 100))
        
    # This one is for experimental purposes (will be rewritten soon)
    def EvtText(self, event):
        self.logger.AppendText('Evttext: %s\n' %event.GetString())
        
    'Creating the panel for graph'
class PlottingFrame(wx.Frame):
    def GraphPanel(self):
        wx.Panel.GraphPanel(self, None, -1,
                          'GraphPanel', size=(550, 350))

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)

        self.axes.plot(t, s)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
        