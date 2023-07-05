import time

from playsound import playsound


class Alarma:
    def init(self, hora_alarma):
        self.hora_alarma = hora_alarma

    def validar_hora(self):
        try:
            time.strptime(self.hora_alarma, "%H:%M")
            return True
        except ValueError:
            return False

    def mostrar_mensaje(self):
        print("¡DESPIERTA!")
        playsound("C:\Users\Manal\Downloads\gun.mp3")

    def posponer_alarma(self):
        print("La alarma se pospone 5 minutos.")
        time.sleep(3)
        playsound("C:\Users\Manal\Downloads\gun.mp3")

    def detener_alarma(self):
        print("La alarma se ha detenido.")

    def iniciar_alarma(self):
        while True:
            if self.validar_hora():
                break
            else:
                print("Hora invalida, intentalo otra vez.")

        hora_alarma = time.strptime(self.hora_alarma, "%H:%M")

        while True:
            hora_actual = time.localtime()

            if (
                hora_actual.tm_hour == hora_alarma.tm_hour
                and hora_actual.tm_min == hora_alarma.tm_min
            ):
                self.mostrar_mensaje()
                while True:
                    opcion = input("¿Deseas posponer la alarma? (s/n): ")
                    if opcion.lower() == "s":
                        self.posponer_alarma()
                        break
                    elif opcion.lower() == "n":
                        self.detener_alarma()
                        return
                    else:
                        print("Opción inválida. Intente nuevamente.")

            time.sleep(1)


hora_alarma = input("Ingrese la hora de la alarma (formato HH:MM): ")
alarma = Alarma(hora_alarma)
alarma.iniciar_alarma()
