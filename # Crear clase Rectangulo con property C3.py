# Crear clase Rectangulo con property area y perimetro

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
            return self.ancho * self.alto

    @property
    def perimetro(self):
            return (self.ancho + self.alto) * 2


rectangulo = Rectangulo(10, 5)

print("Area", rectangulo.area)
print("Perimetro", rectangulo.perimetro)
