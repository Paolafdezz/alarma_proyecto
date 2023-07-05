import tkinter
from time import *

ventana = tkinter.Tk()
hora_alarma = tkinter.StringVar(ventana)
entrada = tkinter.StringVar(ventana)

hora = strftime('%H')
minuto = strftime('%M')
segundo = strftime('%S')

hora_total = (hora + ':' + minuto + ':' + segundo)

ventana.geometry("500x700")
ventana.configure(background = 'black')
tkinter.Wm.wm_title(ventana, 'Alarma App')

def on_click():
    datos_input = entrada.get()
    hora_alarma.set("Configurada para: " + datos_input)
    print(datos_input)

hora_alarma.set("Configurando... ")

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
    foreground = "green",
    background = "black",
    width = 30,
    height = 2
)

mensaje_usuario = tkinter.Label(
    textvariable = hora_alarma,
    font = ("Courier", 16),
    foreground = "black",
    background = "cyan",
    width = 70,
    height = 0
)

boton1 = tkinter.Button(
    text = "Poner Alarma",
    font = ("Courier", 16),
    width = 0,
    height = 0,
    bg = "red",
    fg = "white",
    command = on_click,
    relief = "flat"
)

mensaje_alarma = tkinter.Label(
    text = "Alarma:",
    font = ("Black", 22),
    foreground = "white",
    background = "black",
    width = 30,
    height = 2
)

input_alarma = tkinter.Entry(
    fg = "black",
    bg = "white",
    font = ("Courier", 18),
    width = 70,
    justify = "center",
    textvariable = entrada
)


# cajon_texto = tkinter.Text()

def packear():

    pantalla_hora.pack()
    mensaje_inicial.pack()
    mensaje_alarma()
    input_alarma.pack()
    mensaje_usuario.pack()
    boton1.pack()
    # cajon_texto.pack(fill=tkinter.BOTH, expand=True)

    ventana.mainloop()

if __name__ == "__main__":
    packear()