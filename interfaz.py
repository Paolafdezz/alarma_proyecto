import tkinter
from time import *

ventana = tkinter.Tk()
fecha = tkinter.StringVar(ventana)
entrada = tkinter.StringVar(ventana)

hora = strftime('%H')
minuto = strftime('%M')
segundo = strftime('%S')

hora_total = (hora + ':' + minuto + ':' + segundo)

ventana.geometry("400x700")
ventana.configure(background = 'black')
tkinter.Wm.wm_title(ventana, 'Alarma App')

def on_click():
    fecha.set("Configurada para: " + entrada.get())

fecha.set("Configurando... ")

mensaje_inicial = tkinter.Label(
    text = "Alarma:",
    font = ("Black", 22),
    foreground = "white",
    background = "black",
    width = 30,
    height = 2
)

pantalla_hora = tkinter.Label(
    text = hora_total,
    font = ("Radioland", 30),
    foreground = "red",
    background = "white",
    width = 30,
    height = 2
)

mensaje_usuario = tkinter.Label(
    textvariable = fecha,
    font = ("Courier", 16),
    foreground = "blue",
    background = "yellow",
    width = 30,
    height = 2
)

boton1 = tkinter.Button(
    text = "Poner Alarma",
    font = ("Courier", 16),
    width = 0,
    height = 0,
    bg = "blue",
    fg = "yellow",
    command = on_click,
    relief = "flat"
)

cajon_alarma = tkinter.Entry(
    fg = "white",
    bg = "red",
    font = ("Courier", 18),
    width = 50,
    justify = "center",
    textvariable = entrada
)

# cajon_texto = tkinter.Text()

def packear():

    pantalla_hora.pack(fill=tkinter.BOTH, expand=True)
    mensaje_inicial.pack(fill=tkinter.BOTH, expand=True)
    cajon_alarma.pack(fill=tkinter.BOTH, expand=True)
    mensaje_usuario.pack(fill=tkinter.BOTH, expand=True)
    boton1.pack()
    # cajon_texto.pack(fill=tkinter.BOTH, expand=True)

    ventana.mainloop()

if __name__ == "__main__":
    packear()