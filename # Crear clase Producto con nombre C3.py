# Crear clase Producto con nombre, precio y property para validar precio positivo

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


    @property
    def precio(self):
        return self._precio

    @property.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser positivo")
        self._precio = valor



producto = Producto("Monitor", 10000)

print(producto.nombre)
print(producto.precio)

producto.precio = 12000

print(producto.precio)
