from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Mayores de 23")
        p = Panel(f)
        self.mayores = []

        self.sNombre = sNombre = StaticText(p, -1, "Ingrese debajo 10 numeros: ")
        self.tNombre  = tNombre  = TextCtrl(parent = p, id = -1, pos = (0, 50))

        self.ok =  ok = Button(p, -1, "Listo", (0,100))

        self.numero = int(self.sNombre.GetLabel())
        esMayor()

        f.Show()
        return True
        
    def esMayor(self):
        if numero > 23:
            self.mayores.append(self.numero)
app = MyApp()
app.MainLoop()