import tkinter
from time import *

class Interfaz:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.hora_alarma = tkinter.StringVar(self.ventana)
        self.entrada_hora = tkinter.StringVar(self.ventana)
        self.entrada_nombre = tkinter.StringVar(self.ventana)
        self.mensaje_inicial = tkinter.Label(text="ALARMA", font=("Black", 40), foreground="white", background="black", width=30, height=1)
        self.hora_total = self.obtener_hora_actual()
        
        self.ventana.geometry("500x700")
        self.ventana.configure(background = 'black')
        tkinter.Wm.wm_title(self.ventana, 'Alarma App')


        self.pantalla_hora = tkinter.Label(
            text = self.hora_total,
            font = ("Radioland", 30),
            foreground = "green",
            background = "black",
            width = 30,
            height = 2
        )

        self.mensaje_usuario = tkinter.Label(
            textvariable = self.hora_alarma,
            font = ("Courier", 16),
            foreground = "black",
            background = "cyan",
            width = 70,
            height = 0
        )

        self.boton1 = tkinter.Button(
            text = "Poner Alarma",
            font = ("Courier", 16),
            width = 0,
            height = 0,
            bg = "red",
            fg = "white",
            command = self.on_click,
            relief = "flat"
        )

        self.mensaje_alarma = tkinter.Label(
            text = "Introduzca la hora(hh:mm)",
            font = ("Black", 22),
            foreground = "white",
            background = "black",
            width = 30,
            height = 2,
            justify = "left"
        )

        self.input_alarma = tkinter.Entry(
            fg = "black",
            bg = "white",
            font = ("Courier", 18),
            width = 70,
            justify = "center",
            textvariable = self.entrada_hora
        )

        self.mensaje_nombre = tkinter.Label(
            text = "Introduzca nombre de alarma: ",
            font = ("Black", 22),
            foreground = "white",
            background = "black",
            width = 30,
            height = 0,
            justify = "left"
        )

        self.input_nombre = tkinter.Entry(
            fg = "black",
            bg = "white",
            font = ("Courier", 18),
            width = 70,
            justify = "center",
            textvariable = self.entrada_nombre
        )

        self.alarma_configurada =  tkinter.Label(
            textvariable = self.entrada_nombre,
            font = ("Courier", 16),
            foreground = "black",
            background = "green",
            width = 70,
            height = 0
        )


    def on_click(self):
        datos_input_hora = self.entrada_hora.get()
        datos_input_nombre = self.entrada_nombre.get()
        return self.hora_alarma.set("Alarma: " + datos_input_nombre + "\n" + "configurada para: " + datos_input_hora)
    
    def obtener_hora_actual(self):
        hora = strftime('%H')
        minuto = strftime('%M')
        segundo = strftime('%S')
        hora_total = (hora + ':' + minuto + ':' + segundo)

        return hora_total

    def packear(self):

        self.hora_alarma.set("Configurando... ")

        self.pantalla_hora.pack()
        self.mensaje_inicial.pack()
        self.mensaje_alarma.pack()
        self.input_alarma.pack()
        self.mensaje_nombre.pack()
        self.input_nombre.pack()
        self.mensaje_usuario.pack()
        self.boton1.pack()
        
        
        self.alarma_configurada.pack()
        

        self.ventana.mainloop()
    


if __name__ == "__main__":
    app = Interfaz()
    app.packear()