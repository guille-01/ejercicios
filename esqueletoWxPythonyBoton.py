from wx import* 

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Título de la ventana")
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.sNombre = sNombre = StaticText(p, -1, "Ingrese nombre: ")
        self.tNombre = tNombre = TextCtrl(p)

        self.b = b = Button(p, -1, "Botoncito")
        b.Bind(EVT_BUTTON, self.accion)
        b.Bind(EVT_SET_FOCUS, self.cambiaColor)

        s.Add(sNombre, 0, TOP, 20)
        s.Add(tNombre, 0, ALL, 20)
        s.Add(b,       0, TOP, 20)
        
        p.SetSizer(s)
        f.Show()
        return True

    def cambiaColor(self, event):
        self.b.SetForegroundColour("BLue")

    def accion(self, event):
        v = self.tNombre.GetValue()
        self.sNombre.SetLabel(v)
        f2 = Frame(None, title ="Otra ventana", pos = (2000,2))
        f2.Show()


app = MyApp()
app.MainLoop()