import os
import wx
# Importing the Class from another file
from FP_PlottingPanel import PlottingPanel
#from example import ExamplePanel

class MainWindow(wx.Frame):
    
    def __init__(self, parent, title):
        
        wx.Frame.__init__(self, parent, title=title, size=(900, 500))
        #self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
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
        
app = wx.App(False)
frame = MainWindow(None, "Final Project")
panel = PlottingPanel(frame)
frame.Show()
app.MainLoop()