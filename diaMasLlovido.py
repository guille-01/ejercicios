# Ingresar la lluvia caída en milímetros para cada día de la semana.
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió. (Todos los días llovió distinta cantidad)

from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Dia mas llovido")
        p = Panel(f)
        lun      = TextCtrl(p, -1, "Miligramos llovidos el Lunes?",    (0,0),   (250,30))
        mar      = TextCtrl(p, -1, "Miligramos llovidos el Martes?",   (0,45),  (250,30))
        mier     = TextCtrl(p, -1, "Miligramos llovidos el Miercoles?",(0,110),  (250,30))
        jue      = TextCtrl(p, -1, "Miligramos llovidos el Jueves?",   (0,165), (250,30))
        vier     = TextCtrl(p, -1, "Miligramos llovidos el Viernes?",  (0,220), (250,30))
        sab      = TextCtrl(p, -1, "Miligramos llovidos el Sabado?",   (0,280), (250,30))
        dom      = TextCtrl(p, -1, "Miligramos llovidos el Domingo?",  (0,340), (250,30))
        f.Show()
        return True

app = MyApp()
app.MainLoop()