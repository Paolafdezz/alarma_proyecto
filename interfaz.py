import tkinter
from time import *

BASE_COLOR = "azure2"


class Interfaz:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.geometry("500x700")
        tkinter.Wm.wm_title(self.ventana, "Alarma App")
        self.ventana.configure(background=BASE_COLOR)
        self.hora_actual = tkinter.StringVar(self.ventana)
        self.hora_alarma = tkinter.StringVar(self.ventana)
        self.entrada_hora = tkinter.StringVar(self.ventana)
        self.entrada_nombre = tkinter.StringVar(self.ventana)

        self.actualizar_hora()

        self.createIfnterace()
        self.packear()
        self.ventana.mainloop()

    def createIfnterace(self):
        colors = {
            "base": {
                "foreground": "black",
                "background": BASE_COLOR,
            },
            "label": {
                "foreground": "black",
                "background": "white",
            },
            "accent": {
                "foreground": "green",
                "background": BASE_COLOR,
            },
            "action": {
                "foreground": "white",
                "background": "red",
            },
        }

        fonts = {
            "big": {"font": ("Black", 40)},
            "normal": {"font": ("Radioland", 16)},
        }

        size = {
            "full": {"width": 30},
            "half": {"width": 15},
            "label": {"width": 30, "height": 2},
        }

        self.mensaje_inicial = tkinter.Label(
            **dict(
                {
                    "text": "ALARMA",
                    "height": 1,
                },
                **colors["base"],
                **size["full"],
                **fonts["big"]
            )
        )

        self.pantalla_hora = tkinter.Label(
            **dict(
                {
                    "textvariable": self.hora_actual,
                },
                **colors["accent"],
                **size["label"],
                **fonts["big"]
            )
        )

        self.mensaje_usuario = tkinter.Label(
            **dict(
                {
                    "textvariable": self.hora_alarma,
                },
                **colors["accent"],
                **size["label"],
                **fonts["normal"]
            )
        )

        self.boton1 = tkinter.Button(
            **dict(
                {
                    "text": "Poner Alarma",
                    "command": self.on_click,
                    "relief": "flat",
                },
                **colors["action"],
                **fonts["normal"]
            )
        )

        self.mensaje_alarma = tkinter.Label(
            **dict(
                {
                    "text": "Introduzca la hora(hh:mm)",
                },
                **colors["base"],
                **size["label"],
                **fonts["normal"]
            )
        )

        self.input_alarma = tkinter.Entry(
            **dict(
                {
                    "textvariable": self.entrada_hora,
                },
                **colors["label"],
                **size["full"],
                **fonts["normal"]
            )
        )

        self.mensaje_nombre = tkinter.Label(
            **dict(
                {
                    "text": "Introduzca nombre de alarma: ",
                },
                **colors["base"],
                **size["label"],
                **fonts["normal"]
            )
        )

        self.input_nombre = tkinter.Entry(
            **dict(
                {
                    "textvariable": self.entrada_nombre,
                },
                **colors["label"],
                **size["full"],
                **fonts["normal"]
            )
        )

        self.alarma_configurada = tkinter.Label(
            **dict(
                {
                    "textvariable": self.entrada_nombre,
                },
                **colors["accent"],
                **size["full"],
                **fonts["normal"]
            )
        )

    def on_click(self):
        datos_input_hora = self.entrada_hora.get()
        datos_input_nombre = self.entrada_nombre.get()
        return self.hora_alarma.set(
            "Alarma: "
            + datos_input_nombre
            + "\n"
            + "configurada para: "
            + datos_input_hora
        )

    def actualizar_hora(self):
        def obtener_hora_actual():
            hora = strftime("%H")
            minuto = strftime("%M")
            segundo = strftime("%S")
            hora_total = hora + ":" + minuto + ":" + segundo

            return hora_total

        self.hora_actual.set(obtener_hora_actual())

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


if __name__ == "__main__":
    app = Interfaz()
