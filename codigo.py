import time
import pygame
import threading


class Alarma:

    def __init__(self, hora_alarma):
        self.hora_alarma = hora_alarma

    def validar_hora(self):
        try:
            time.strptime(self.hora_alarma, "%H:%M")
            return True
        except ValueError:
            return False

    def mostrar_mensaje(self):
        print("¡DESPIERTA!")
        pygame.mixer.init()
        pygame.mixer.music.load("sound/buenosdias.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    def posponer_alarma(self):
        print("La alarma se pospone 5 minutos.")
        time.sleep(300)  
        self.mostrar_mensaje()

    def detener_alarma(self):
        print("La alarma se ha detenido.")

    def iniciar_alarma(self):
        while True:
            while not self.validar_hora():
                print("Hora inválida, inténtalo otra vez.")
                hora_alarma = input("Ingrese la hora de la alarma (formato HH:MM): ")
                self.hora_alarma = hora_alarma

            hora_alarma = time.strptime(self.hora_alarma, "%H:%M")

            while True:
                hora_actual = time.localtime()

                if hora_actual.tm_hour == hora_alarma.tm_hour and hora_actual.tm_min == hora_alarma.tm_min:
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


def configurar_alarma():
    hora_alarma = input("Ingrese la hora de la alarma (formato HH:MM): ")
    alarma = Alarma(hora_alarma)
    alarma.iniciar_alarma()


def demo():
    num_alarmas = int(input("Ingrese el número de alarmas que desea configurar: "))
    threads = []
    for _ in range(num_alarmas):
        t = threading.Thread(target=configurar_alarma)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    demo()