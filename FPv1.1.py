import wx
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
from matplotlib.backends.backend_wx import _load_bitmap
from FP_2DPlotting import MainWindow2D
from FP_3DPlotting import MainWindow3D

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title = "FP", size = (1000,700))
        nb = wx.Notebook(frame)
        
        nb.AddPage(MainWindow2D(nb), "2D")
        nb.AddPage(MainWindow3D(nb), "3D")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True
        
app = MyApp(0)
app.MainLoop() 