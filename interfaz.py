import tkinter
from time import *

ventana = tkinter.Tk()
hora_alarma = tkinter.StringVar(ventana)
entrada_hora = tkinter.StringVar(ventana)
entrada_nombre = tkinter.StringVar(ventana)

hora = strftime('%H')
minuto = strftime('%M')
segundo = strftime('%S')

hora_total = (hora + ':' + minuto + ':' + segundo)

ventana.geometry("500x700")
ventana.configure(background = 'black')
tkinter.Wm.wm_title(ventana, 'Alarma App')

def on_click():
    datos_input_hora = entrada_hora.get()
    datos_input_nombre = entrada_nombre.get()
    hora_alarma.set("Alarma: " + datos_input_nombre + "\n" + "configurada para: " + datos_input_hora)

hora_alarma.set("Configurando... ")

def choice(option):
   pop.destroy()
   if option == "yes":
      tkinter.Label.config(text="Hello, How are You?")
   else:
      tkinter.Label.config(text="You have selected No")
      ventana.destroy()

def click_fun():
   global pop
   pop = tkinter.Toplevel(ventana)
   pop.title("Confirmation")
   pop.geometry("300x150")
   pop.config(bg="white")
   # Create a Label Text
   label = tkinter.Label(pop, text="Seguro que quieres borrar la alarma?",
   font=('Aerial', 12))
   label.pack(pady=20)
   frame = tkinter.Frame(pop, bg="gray71")
   frame.pack(pady=10)
   button1 = tkinter.Button(frame, text="Yes", command=lambda: choice("yes"), bg="blue", fg="white")
   button1.grid(row=0, column=1)
   button2 = tkinter.Button(frame, text="No", command=lambda: choice("no"), bg="blue", fg="white")
   button2.grid(row=0, column=2)
   label = tkinter.Label(ventana, text="", font=('Aerial', 14))
   label.pack(pady=40)


mensaje_inicial = tkinter.Label(
    text = "ALARMA",
    font = ("Black", 40),
    foreground = "white",
    background = "black",
    width = 30,
    height = 1
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
    text = "Introduzca la hora(hh:mm)",
    font = ("Black", 22),
    foreground = "white",
    background = "black",
    width = 30,
    height = 2,
    justify = "left"
)

input_alarma = tkinter.Entry(
    fg = "black",
    bg = "white",
    font = ("Courier", 18),
    width = 70,
    justify = "center",
    textvariable = entrada_hora
)

mensaje_nombre = tkinter.Label(
    text = "Introduzca nombre de alarma: ",
    font = ("Black", 22),
    foreground = "white",
    background = "black",
    width = 30,
    height = 0,
    justify = "left"
)

input_nombre = tkinter.Entry(
    fg = "black",
    bg = "white",
    font = ("Courier", 18),
    width = 70,
    justify = "center",
    textvariable = entrada_nombre
)

alarma_configurada =  tkinter.Label(
    textvariable = entrada_nombre,
    font = ("Courier", 16),
    foreground = "black",
    background = "green",
    width = 70,
    height = 0
)

boton_borrar = tkinter.Button(
    (ventana), 
    text="Borrar", 
    command=click_fun
)


# cajon_texto = tkinter.Text()

def packear():

    pantalla_hora.pack()
    mensaje_inicial.pack()
    mensaje_alarma.pack()
    input_alarma.pack()
    mensaje_nombre.pack()
    input_nombre.pack()
    mensaje_usuario.pack()
    boton1.pack()
    boton_borrar.pack()
    
    
    alarma_configurada.pack()
    # cajon_texto.pack(fill=tkinter.BOTH, expand=True)

    ventana.mainloop()

if __name__ == "__main__":
    packear()