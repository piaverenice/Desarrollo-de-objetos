# Modelar auto con composición: Auto tiene Motor. El metodo arrancar() usa el motor


class Motor:
    def arrancar(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.arrancar()


auto = Auto()

auto.arrancar()
