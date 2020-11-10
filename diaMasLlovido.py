# Ingresar la lluvia caída en milímetros para cada día de la semana.
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió. (Todos los días llovió distinta cantidad)

from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Dia mas llovido")
        p = Panel(f)
        self.listCantidades = []
        self.lun      = TextCtrl(p, -1, "Miligramos llovidos el Lunes?",    (0,0),   (250,30))
        self.mar      = TextCtrl(p, -1, "Miligramos llovidos el Martes?",   (0,45),  (250,30))
        self.mier     = TextCtrl(p, -1, "Miligramos llovidos el Miercoles?",(0,110),  (250,30))
        self.jue      = TextCtrl(p, -1, "Miligramos llovidos el Jueves?",   (0,165), (250,30))
        self.vier     = TextCtrl(p, -1, "Miligramos llovidos el Viernes?",  (0,220), (250,30))
        self.sab      = TextCtrl(p, -1, "Miligramos llovidos el Sabado?",   (0,280), (250,30))
        self.dom      = TextCtrl(p, -1, "Miligramos llovidos el Domingo?",  (0,340), (250,30))
        self.dia      = StaticText(p,-1, "Dia mas llovido: ", (0,400)) + sacarDiaMasLlovido()

        f.Show()
        return True

        self.listCantidades.append(int(self.lun.  GetLabel()))
        self.listCantidades.append(int(self.mar.  GetLabel()))
        self.listCantidades.append(int(self.mier. GetLabel()))
        self.listCantidades.append(int(self.jue.  GetLabel()))
        self.listCantidades.append(int(self.vier. GetLabel()))
        self.listCantidades.append(int(self.sab.  GetLabel()))
        self.listCantidades.append(int(self.dom.  GetLabel()))

    def sacarDiaMasLlovido(self):
        mayor = 0
        for cantidad in self.listCantidades:
            if cantidad > mayor:
                mayor = cantidad
        return mayor        

app = MyApp()
app.MainLoop()