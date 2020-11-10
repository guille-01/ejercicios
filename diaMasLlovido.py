# Ingresar la lluvia caída en milímetros para cada día de la semana.
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió. (Todos los días llovió distinta cantidad)

from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Dia mas llovido")
        p = Panel(f)
        lun      = TextCtrl()
        mar      = TextCtrl()
        mier     = TextCtrl()
        jueves   = TextCtrl()
        viernes  = TextCtrl()
        sabado   = TextCtrl()
        domingo  = TextCtrl()
        f.Show()
        return True

app = MyApp()
app.MainLoop()