# Crear clase Empleado y subclases Programador y Diseñador. Cada implementa trabajar()

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def trabajar(self):
        return "Trabajando"


class Programador(Empleado):
    def trabajar(self):
        return "Programando"


class Diseñador(Empleado):
    def trabajar(self):
        return "Diseñando"


empleado1 = Programador("Jose")
empleado2 = Diseñador("Maria")

print(empleado1.nombre, empleado1.trabajar())
print(empleado2.nombre, empleado2.trabajar())
