from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Sumar dos numeros")
        p = Panel(f)

        self.sNombre  = sNombre  = StaticText(p, -1, "Ingrese el primer numero: ",(0, 50))
        self.tNombre  = tNombre  = TextCtrl  (parent = p, id = -1, pos = (0, 80))
        self.sNombre2 = sNombre2 = StaticText(p, -1, "Ingrese el segundo numero: ", (0,162))
        self.tNombre2 = tNombre2  = TextCtrl(parent = p, id = -1, pos = (0,200))

        self.resultado = resultado = StaticText(p, -1, "Resultado: ", (0, 350))
        self.BotonSuma = b = Button(p, -1, "Sumar", (0,250))
        b.Bind(EVT_BUTTON, self.suma)  
        
        f.Show()
        return True

    def suma(self, event):
        n1 = int(self.tNombre.GetValue())
        n2 = int(self.tNombre2.GetValue())
        resultado = n1 + n2
        salida = str(resultado) 
        self.resultado.SetLabel(salida)
    


app = MyApp()
app.MainLoop()