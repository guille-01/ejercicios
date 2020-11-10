#Ingresar números sucesivos en una misma caja de texto hasta que no haya más y mostrar el promedio.


from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, -1, "Numeros sucesivos")
        p = Panel(f)
        self.listaNumeros = []
        self.unicaCajita = unicacajita = TextCtrl(p, -1, "Numero")
        self.botoncito = botoncito = Button(p, -1, "ok")
        botoncito.Bind(EVT_BUTTON, self.tomarYreiniciar)
        tomarYreiniciar()
        sumarNumeros()
        f.Show()
        return True


    def tomarYreiniciar(self, event):
        numero = int(unicaCajita.GetLabel())
        self.unicaCajita = None

    def sumarNumeros(self, num):
        if int(self.unicaCajita.GetLabel()) == True:
            numero = self.unicaCajita.GetLabel()
            numero.append(self.listaNumeros)

app = MyApp()
app.MainLoop()