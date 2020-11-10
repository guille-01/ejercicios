from wx import* 

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Título de la ventana")
        p = Panel(f)
        s = BoxSizer(VERTICAL)
        self.sNombre = sNombre = StaticText(p, -1, "Ingrese numero: ")
        self.tNombre = tNombre = TextCtrl(p)

        self.b = b = Button(p, -1, "el doble")
        self.b2 = b2 = Button (p, -1, "el triple")
        self.resultado = StaticText(p, -1, "Resultado")
        b.Bind(EVT_BUTTON, self.accion)
        b.Bind(EVT_SET_FOCUS, self.cambiaColor)
        b2.Bind(EVT_BUTTON, self.triplicar)
        s.Add(sNombre, 0, TOP, 20)
        s.Add(tNombre, 0, ALL|EXPAND, 10)
        s.Add(b,       0, TOP|CENTER, 20)
        s.Add(b2,      0, TOP|CENTER, 30)
        s.Add(self.resultado, ALL|CENTER, 20)
        p.SetSizer(s)
        f.Show()
        return True

    def cambiaColor(self, event):
        self.b.SetForegroundColour("Blue")


    def accion(self, event):
        v = int(self.tNombre.GetValue())
        salida = self.resultado.GetLabel() + " = " + str(v*2)
        self.resultado.SetLabel(salida)

    def triplicar(self, event):
        d = int(self.tNombre.GetValue())
        output = self.resultado.GetLabel() + " = " + str(d*3)
        self.resultado.SetLabel(output)

app = MyApp()
app.MainLoop()



