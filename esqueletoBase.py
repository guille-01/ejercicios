from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Título de la ventana")
        f.Show()
        return True

app = MyApp()
app.MainLoop()
