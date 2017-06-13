# from https://wiki.wxpython.org/WxHowtoSmallEditor


import wx

class Bitmap(wx.StaticBitmap):
    def __init__(self, parent, imagepath):
        self._image = wx.Image(imagepath, wx.BITMAP_TYPE_ANY)
        super().__init__(parent, label=wx.Bitmap(self._image))
        self.Bind(wx.EVT_SIZE, self.onSize, self)
        print(dir(self._image))
    def onSize(self, event):
        slotwidth, slotheight = self.Size
        imgwidth = self._image.GetWidth()
        imgheight = self._image.GetHeight()
        vfactor = slotheight / imgheight
        hfactor = slotwidth / imgwidth
        factor = min(2, hfactor, vfactor)
        scaled_image = self._image.Scale(max(2, factor * imgwidth), max(2, factor*imgheight))
        self.SetBitmap(wx.Bitmap(scaled_image))


class MainWindow(wx.Frame):
    def __init__(self, imagepath):
        super().__init__(None, size=(200,200))

        self.imagepath = imagepath
        self.images = []
        self.CreateInteriorWindowComponents()
        self.CreateExteriorWindowComponents

    def CreateInteriorWindowComponents(self):
        self.panel = wx.Panel(self)
        self.sizer = wx.GridSizer(cols=4, hgap=5, vgap=5)
        for i in range(1, 8):
            #img = wx.Image(self.imagepath, wx.BITMAP_TYPE_ANY)
            image = Bitmap(self.panel, 'test_%s.png'%i)
            self.sizer.Add(image, proportion=1, flag=wx.EXPAND|wx.ALIGN_LEFT)
            self.images.append(image)
        self.panel.SetSizer(self.sizer)
        self.sizer.Fit(self)

        #self.SetSizeHints(200, 200, 400, 400)

    def CreateExteriorWindowComponents(self):
        self.CreateMenu()
        self.CreateStatusBar()
        self.SetTitle()

    def CreateMenu(self):
        ...

    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, 'A sample editor\n'
            'in wxPython', 'About Sample Editor', wx.OK)
        dialog.ShowModal()
        dialog.Destroy()

    def OnExit(self, event):
        self.Close()  # Close the main window.


app = wx.App()
frame = MainWindow('GIFPAL.png')
frame.Show()
app.MainLoop()
